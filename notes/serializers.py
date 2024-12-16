from rest_framework import serializers
from .models import Note
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
  class Meta:
      model = get_user_model()
      fields = ['id', 'username', 'email']

class NoteSerializer(serializers.ModelSerializer):
  user = UserSerializer(read_only=True)

  class Meta:
      model = Note
      fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'user']