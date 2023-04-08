from rest_framework.views import APIView
from .serialiazers import PostSerializer

from utils.pubs import publish_data_on_redis, redis_client
# create post

class PostView(APIView):

    def get(self, request):
        ...

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            publish_data_on_redis(serializer.data, 'notifications')
            serializer.save()
        ...
        
