from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Note


class NoteTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_superuser(password='testuser', email="user@inbox.ru", username='testuser')
        self.note = Note.objects.create(title="Test Note", description="Test Description", user=self.user)
        self.client.login(password='testuser', email="user@inbox.ru")

    def test_view_note(self):  # Тест на просмотр заметки. Работает!
        note = Note.objects.get(id=self.note.id)
        self.assertEqual(note.title, "Test Note")
        self.assertEqual(note.description, "Test Description")

    def test_edit_note(self):  # Тест на редактирование заметки. Работает!
        self.note.title = "Updated Title"
        self.note.save()
        updated_note = Note.objects.get(id=self.note.id)
        self.assertEqual(updated_note.title, "Updated Title")

    def test_delete_note(self):  # Тест на удаление заметки. Работает!
        note_id = self.note.id
        self.note.delete()
        with self.assertRaises(Note.DoesNotExist):
            Note.objects.get(id=note_id)

    def test_create_note(self):  # Тест на создание заметки. Работает!
        url = reverse('notes-create')  # есть эндпоинт с именем 'notes-list'
        print(url)
        data = dict(title='Note2', description='Description', user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
