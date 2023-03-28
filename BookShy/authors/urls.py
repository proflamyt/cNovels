from django.urls import path
from .views import AuthorView, AuthorDetail

urlpatterns = [
    path('', AuthorView.as_view(), name='authors'),
    path('<int:pk>', AuthorDetail.as_view(), name='author_detail'),
]