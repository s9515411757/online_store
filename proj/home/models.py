from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Product(models.Model):
    CONSTANT_STR = 15
    title = models.CharField(
        max_length = 255,
        verbose_name="Заголовок",
        help_text="Заголовок объявления"
    )
    text = models.TextField(
        verbose_name="Текст",
        help_text="Укажите текст объявления"
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='product',
        verbose_name='Автор',
        help_text="Автор объявления"
    )
    image = models.ImageField(
        'Картинка',
        upload_to='product/',
        blank=True
    )

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:self.CONSTANT_STR]