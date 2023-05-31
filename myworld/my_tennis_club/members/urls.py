from django.urls import path
from .views import *

urlpatterns = [
    path('overview/', SnippetOverviewView.as_view(), name='snippet_overview'),
    path('create/', SnippetCreateView.as_view(), name='snippet_create'),
    path('detail/<int:snippet_id>/', SnippetDetailView.as_view(), name='snippet_detail'),
    path('update/<int:snippet_id>/', SnippetUpdateView.as_view(), name='snippet_update'),
    path('delete/<int:snippet_id>/', SnippetDeleteView.as_view(), name='snippet_delete'),
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('tag/<int:tag_id>/', TagDetailView.as_view(), name='tag_detail'),
    # path('loginview/',LoginView.as_view(),name="login"),
    # path('token/',RefreshView.as_view(),name="dd")
    path('login/',Loginview.as_view(),name='dd')
]