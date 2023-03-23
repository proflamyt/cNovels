from .views import NovelView, NovelSearchView, RecentReadViewSet, RenderMap

from django.urls import path


urlpatterns = [
    path('', NovelView.as_view(), name='novels'),
    path('recent-reads', RecentReadViewSet.as_view(), name='recent-reads'),
    path('search/', NovelSearchView.as_view(), name='search_novels'),
    path('/tiles/<zoom>/<y>/<x>/<z>', RenderMap.as_view())

]