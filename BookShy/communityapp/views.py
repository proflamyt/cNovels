from rest_framework.views import APIView
from .serialiazers import PostSerializer
from rest_framework.response import Response 
from .models import Post

from utils.pubs import publish_data_on_redis, redis_client
# create post

class PostView(APIView):

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

    # create room only authors
    def post(self, request):
        ...

        

    # join room  
    def put():
        ...