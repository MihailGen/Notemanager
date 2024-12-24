from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics, permissions

# from django import request
from .models import Note
from .serializers import NoteSerializer, UserSerializer


# Представления для администраторов:
class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


# Представления для пользователей:
class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def get_queryset(request):
    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def perform_create(self, serializer_class):
        serializer_class.save(user=self.request.user)
        #Note.objects.save(user=self.request.user)



class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)


class NoteListStart(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_listset(request):
        notes = Note.objects.filter(user=request.user)
        # print(notes[0].title) # Отладка
        return render(request, 'notes_list.html', {'notes': notes})
