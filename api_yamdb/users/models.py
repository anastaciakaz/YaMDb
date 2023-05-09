import jwt
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Кастомная модель для пользователя."""

    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    ROLE_CHOICES = (
        (ADMIN, 'admin'),
        (MODERATOR, 'moderator'),
        (USER, 'user'),
    )

    email = models.EmailField(
        max_length=254,
        verbose_name='Email',
        help_text='Укажите email',
        unique=True,
        null=False,
    )
    bio = models.TextField(
        max_length=1000,
        verbose_name='Биография',
        help_text='Укажите Биографию',
        blank=True,
    )
    role = models.CharField(
        max_length=9,
        verbose_name='Уровень доступа',
        help_text='Укажите уровень доступа',
        choices=ROLE_CHOICES,
        default=USER,
    )
    confirmation_code = models.CharField(
        max_length=254,
        verbose_name='Код подтверждения',
        blank=True,
    )

    def __str__(self):
        """Строковое представление модели (отображается в консоли)"""
        return self.username

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_user(self):
        return self.role == self.USER

    @property
    def create_confirmation_code(self):
        """
        Позволяет получить код подтверждения пользователя путем
        вызова user.create_confirmation_code.
        """
        return self._generate_confirmation_code()

    def _generate_confirmation_code(self):
        """
        Генерирует confirmation_code, в котором хранится идентификатор
        и имя этого пользователя.
        """

        token = jwt.encode(
            {'id': self.pk, 'username': self.username},
            settings.SECRET_KEY,
            algorithm='HS256',
        )

        return token

    class Meta:
        ordering = ['-id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
