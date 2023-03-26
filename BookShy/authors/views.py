from rest_framework.generics import ListAPIView
from .models import AuthorModel
from .serializers import AuthorSerializer

from django_filters.rest_framework.backends import DjangoFilterBackend


class AuthorView(ListAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields =['weekly_featured','special_featured']
    

