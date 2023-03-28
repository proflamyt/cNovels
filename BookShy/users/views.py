from rest_framework.views import APIView
from .serializers import UserSerializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class UserView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        serializer =  UserSerializers(request.user)
        return Response({
            "status": "success",
           "data": serializer.data})
        