from django.urls import path
from .serializers import NoteSerializer
from . import views

urlpatterns = [
    path('admin/users/', views.UserList.as_view(), name='user-list'),
    path('admin/users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    # path('notes/', views.NoteList.get_queryset, name='note-list'),
    path('notes/', views.NoteList.as_view(), name='notes-list'),
    path('notes/create', views.NoteList.perform_create, name='notes-create'),
    path('notes/<int:pk>/', views.NoteDetail.as_view(), name='note-detail'),
    path('', views.NoteListStart.get_listset, name='notes-list-start'),
]
