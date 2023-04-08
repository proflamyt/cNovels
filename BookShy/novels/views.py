from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import APIException

from .utils.custom_permission import CanReadBook


from .serializers import (ChapterReadSerializer, GenreSerializer, NovelSerializer, ChapterSerializer,
                           SnapshotSerializer, UserBookGoalSerializer, NovelMarkerSerializer)
from .models import ChapterModel, Genre, Goal, NovelModel, SnapShots, UserBook

from .utils.map_server import map_view

from django_filters.rest_framework.backends import DjangoFilterBackend

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

# Create your views here.
class NovelView(APIView):
    # Only author should create books

    """"

    Get all Books
    ?weekly_featured=true : sends weekly featured
    ?special_featured=true : only specially featured novels
    
    """
    permission_classes = (AllowAny,)

    def get(self, request, pk=None):

        weekly_featured = request.query_params.get('weekly_featured', None)

        special_featured = request.query_params.get('special_featured', None)

        if pk :
            novels = NovelModel.objects.get(id=pk, published=True)

        elif weekly_featured is not None and weekly_featured.lower() == 'true':
            novels = NovelModel.objects.filter(published=True, weekly_featured=True)

        elif special_featured is not None and special_featured.lower() == 'true':
            novels = NovelModel.objects.filter(published=True, special_featured=True)
        
        else:
            novels = NovelModel.objects.filter(published=True)

        serializers = NovelSerializer(novels , many= (pk==None))
        return Response({'status': 'success',
            'data': serializers.data}, status=status.HTTP_200_OK
        )
        


class RecentReadViewSet(APIView):
    """
    list all recently viewed novels chapters of logged in user, 

    """
    
    permission_classes = [IsAuthenticated]
    my_tags = ['Book', 'Home']

    def get(self, request):
        recent = request.user.recently_viewed_chapters.all().select_related('book')
        serializer = ChapterSerializer(recent, many=True)

        return Response({'status': 'success',
            'data': serializer.data}, status=status.HTTP_200_OK
        )
    

class NovelSearchView(generics.ListAPIView):
    """
    Displays all novels with just 'get request' , filters the searches with ?search query ;
    e.g
    novels/search?genre=fantancy : filters genre by fantancy
    novels/search?search=o&genre=o : searched by 

    
    will return all novel objects relating to ola
    
    """
    queryset = NovelModel.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['genre_name']
    search_fields = ['title', 'authors__name']
    serializer_class = NovelSerializer


# cache
class RenderMap(APIView):

    @method_decorator(cache_page(60*60*2))
    def get(self, zoom, x, y, z):    
        response = HttpResponse(map_view(zoom, x, y, z), content_type='image/png')
        return response



class SnapShotsView(APIView):
    def get(self, request, pk):
        try:
            images = SnapShots.objects.filter(novel_id=pk)
            serializer = SnapshotSerializer(images, many=True)
            return Response({
                "status": "success", 
                "data": serializer.data
            })
        except Exception as e:
            
            return Response({
                "status": "fail", 
                "error": "no SnapShot found with the given ID"
            }, status=status.HTTP_400_BAD_REQUEST)





class ReadChapterView(APIView):
    """
     Read Chapter in a Book
    """
    permission_classes = [IsAuthenticated, CanReadBook]

    def get(self, request, book, chapter):
        try:
            novel = UserBook.objects.prefetch_related('book__chapters').get(book=book, user=request.user)
            self.check_object_permissions(request, novel)
            serializer =  ChapterReadSerializer(novel.book.chapters.get(id=chapter))
            return Response({
                "status": "success",
                "data": serializer.data
            })
        except APIException as e: 
            return Response({
                "status": "failed",
                "error": "You do not have permission to read this book"
            }, status=status.HTTP_402_PAYMENT_REQUIRED)
        except Exception as e:
    
            return Response({
                "status": "failed",
                "error": "No Chapter with Id "
            }, status=status.HTTP_400_BAD_REQUEST)


class UserBookGoalList(generics.ListAPIView):
    serializer_class = UserBookGoalSerializer

    def get_queryset(self):
        
        return Goal.objects.filter(user=self.request.user)
    

class MapView(APIView):

    def get(self, request, pk):
        try:
            novel = NovelModel.objects.prefetch_related('maptype__marker_set').get(pk=pk)
            
            serializer = NovelMarkerSerializer(novel.maptype.marker_set, many=True)
            return Response({
                "status":"success",
                "data": serializer.data

            })
        except Exception as e:
            return Response({
                "status":"failed",
                "error": "No Novel with selected ID"

            })



class GenresView(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response({"status": "success", "data": serializer.data})
        