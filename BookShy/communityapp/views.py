from django.http import Http404
from rest_framework.views import APIView

from .utils.custom_permissions import CanEditField
from .serialiazers import GroupSerializer, PostSerializer, RoomSerializer
from rest_framework.response import Response 
from .models import GroupChat, Post, Room
from rest_framework import status, permissions


from utils.pubs import publish_data_on_redis, redis_client
# create post

class PostView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        posts = Post.objects.all().order_by('created_at')[:100]
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            publish_data_on_redis(serializer.data, 'notifications')
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        

class RoomView(APIView):
    permission_classes = [permissions.IsAuthenticated, CanEditField]

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise Http404

    # create room only authors
    def post(self, request):
        serializer = RoomSerializer(data=request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            redis_client.set(f"room:{serializer.id}:name", f"{serializer.name}")
            redis_client.sadd(f"user:{self.request.user.id}:room:{serializer.id}:admins", f"{serializer.admins}")
            return Response(serializer.data)
        return Response(serializer.errors)

    # add users and change room  for creator and  admins(except creator) , only add user for others
    def put(self, request, pk):
        room = self.get_object(pk)
        serializer = RoomSerializer(room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class GroupJoinAPIView(APIView):
    """
    Join a group with the post request , 
    delete request will remove user from the group specified
    and get query should list all current group of user 
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, room):
        try:
            queryset = GroupChat.objects.get(room__name = room)
            return queryset
        except GroupChat.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        snippet = request.user.groupchat_set.all()
        serializer = GroupSerializer(snippet, many=True)
        return Response(serializer.data)
    

    def put(self, request, room, format=None):

        group = self.get_object(room)

        if request.user.groupchat_set.filter(id = group.id):
            return Response('already regis')

        group.citizens.add(request.user)
        group.save()

        redis_client.sadd(f"user:{request.user.id}:rooms", f"{group.id}")
        redis_client.sadd(f"room:{group.id}:users", f"{request.user.name}")

        return Response('serializer.data', status=status.HTTP_201_CREATED)
    

    #leave chat 
    def delete(self, request, room, format=None):
        snippet = self.get_object(room)
        # check if in room
        if request.user.groupchat_set.filter(room__name=room):
            request.user.groupchat_set.remove(room)
            redis_client.srem(f"user:{request.user.id}:rooms", f"{snippet.id}")
            return Response(status=status.HTTP_204_NO_CONTENT)
        return 'not in room'
    


class RoomMessageView(APIView):

    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, room):
        # check if a member of room
        try:
            group = GroupChat.objects.select_related('room__messages').get(room__name=room, citizens=request.user)
            messages = group.room.messages.all()
            return Response()
        except:
            return Response({
                'message': "you are not allowed to acess these messages"
            })
        