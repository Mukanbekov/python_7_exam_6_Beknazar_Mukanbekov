from django.db import models

# Create your models here.
status_choices = (
    ("active", "Активно"),
    ("blocked", "Заблокировано"),
)


class Books(models.Model):
    name = models.CharField(max_length=120, verbose_name='Имя')
    email = models.EmailField(null=False, blank=False, verbose_name='email')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.TextField(null=False, blank=False, choices=status_choices, default='active', verbose_name='Статус')

    class Meta:
        db_table = 'books'
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.id}. {self.name}: {self.email}'