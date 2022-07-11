from django.db import models


class UserProfile(models.Model):
    tg_id = models.PositiveIntegerField(
        verbose_name='ID пользователя',
        primary_key=True,
    )
    username = models.CharField(
        max_length=50,
        verbose_name='Логин пользователя',
        unique=True,
    )
    is_get_contact = models.BooleanField(
        verbose_name='Оставил контакт',
        default=False,
    )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.username