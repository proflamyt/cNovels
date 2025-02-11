from .views import (GenresView, NovelView, NovelSearchView, MapView,
RecentReadViewSet, RenderMap, ReadChapterView, UserBookGoalList, SnapShotsView)

from django.urls import path


urlpatterns = [
    path('', NovelView.as_view(), name='novels'),
    path('<int:pk>', NovelView.as_view(), name='novels'),
    path('<int:pk>/map', MapView.as_view(), name='map'),
    path('<int:pk>/snapshots', SnapShotsView.as_view(), name='snapshots'),
    path('recent-reads', RecentReadViewSet.as_view(), name='recent-reads'),
    path('search/', NovelSearchView.as_view(), name='search_novels'),
    path('tiles/<zoom>/<y>/<x>/<z>', RenderMap.as_view()),
    path('<int:book>/chapters/<int:chapter>/', ReadChapterView.as_view(), name='read_chapter'),
    path('goals/', UserBookGoalList.as_view(), name='user-book-goal-list'),
    path('genres', GenresView.as_view())
    

]