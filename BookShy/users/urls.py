from django.urls import path
from .views import UserView


urlpatterns = [

    path('me', UserView.as_view())

]