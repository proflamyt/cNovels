from django.http.response import Http404
from novel.models import Audio, Genre, Novel, Poems, Weekly, NovelMap
from rest_framework import generics, serializers, viewsets, status, filters, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes, action
from .serializers import AudioSerializer, GenreSerializer, NovelSerializer, PoemSerializer, UserSerializer,NovelMapSerializer,  WeeklySerializer
from django.contrib.auth import get_user_model
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.views import APIView
User = get_user_model()
from django.shortcuts import get_object_or_404


class NovelRealease(generics.ListAPIView):
    queryset = Novel.objects.all().order_by('-date_uploaded')
    serializer_class = NovelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

class NovelSearchView(generics.ListAPIView):
    """
    Displays all novels with just 'get request' , filters the searches with ?search query ;
    e.g
     /novel-search?search=ola 
    
    will return all novel objects relating to ola
    
    
    """
    queryset = Novel.objects.all()
    serializer_class = NovelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__authorName', 'genre__name', 'chapters__title']
    def get_queryset(self):
        user = self.request.user
        return user.recently_viewed_novels.all()


class PoemsSearchView(generics.ListAPIView):
    """
    Displays all poems with just 'get request' , filters the searches with ?search query ;
    e.g
     /poem-search?search=ola 
    
    will return all poems objects relating to ola
    
    
    """
    queryset = Poems.objects.all()
    serializer_class = PoemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'authorName', 'genre', 'chapter_title']

class AudiosListView(generics.ListAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'authorName', 'genre', 'chapter_title']


class PoemsListView(generics.ListAPIView):
    queryset = Poems.objects.all()
    serializer_class = NovelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'authorName', 'genre', 'chapter_title']


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def home(request):
    '''
    Displays Genres 
    
    '''
    weekly = Weekly.objects.all()
    week_serializer = WeeklySerializer(weekly, many=True)
    genres  =  Genre.objects.all()
    genre_serializer = GenreSerializer(genres, many=True)
    #add blog
    return Response({'genres':genre_serializer.data, 'weekly':week_serializer.data})



class RecentReadViewSet(APIView):
    """
  recently viewed
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            novel = Novel.objects.get(slug=pk)
            return novel
            
        except Novel.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        """
        Return a list of all users.
        """
        if pk:
            novel = self.get_object(pk=pk)
            request.user.recently_viewed_novels.add(novel)
            request.user.save()
            return Response({"massage": "recent novel updated"})

        recents = request.user.recently_viewed_novels
        serializer  = NovelSerializer(recents, many=True)
        return Response(serializer.data)



class NovelViewMap(APIView):
    def get_object(self , pk):
        novel  = get_object_or_404(NovelMap, novel__id=pk)
        return novel

    def get(self,request, pk):
        novel_map = self.get_object(pk)
        #serialize map and return
        serializer  = NovelMapSerializer(novel_map)
        return Response(serializer.data)

