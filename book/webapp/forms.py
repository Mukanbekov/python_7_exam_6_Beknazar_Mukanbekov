from django import forms

from webapp.models import Books


class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ('name', 'text', 'email')


class BookDeleteForm(forms.Form):
    name = forms.CharField(max_length=120, required=True, label='Введите имя, чтобы удалить её')