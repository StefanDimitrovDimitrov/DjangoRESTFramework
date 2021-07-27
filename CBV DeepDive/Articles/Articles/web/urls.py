from django.urls import path

from Articles.web.views import ArticleCreateView, ArticleListView, SourceCreateView, SourceDetailsView, \
    SourcesListView

urlpatterns = [
    path('', ArticleListView.as_view(), name='index'),
    path('articles/create', ArticleCreateView.as_view(), name='create article'),
    path('sources/create/', SourceCreateView.as_view(), name='create source'),
    path('sources/', SourcesListView.as_view(), name='list sources'),
    path('sources/<int:pk>', SourceDetailsView.as_view(), name='details source'),
]
