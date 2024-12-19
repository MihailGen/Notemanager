from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from .serializers import NoteSerializer, UserSerializer
from django.shortcuts import render
#from django import request
from .models import Note


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

    def get_queryset(self):
        #return Note.objects.filter(user=self.request.user)
        #return render(request, 'notes_list.html', {'notes': notes})
        #return render(self.request, 'notes_list.html', {'notes': Note.objects.filter(user=self.request.user)})
        notes = Note.objects.filter(user=self.request.user)
        print(notes[0].description)
        print(notes[0].title)
        print(self.request.user)
        return render(self.request, 'notes_list.html', {'notes':  notes})

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)
