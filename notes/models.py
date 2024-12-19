from django.db import models
from django.contrib.auth import get_user_model
#from django.contrib.auth.models import AbstractUser

class Note(models.Model):

    title = models.CharField(max_length=200, verbose_name='Тема заметки')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

#class CustomUser(AbstractUser):
    # Добавьте дополнительные поля, если необходимо
#    pass