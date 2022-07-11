from django.db import models


class Profile(models.Model):
    tg_id = models.PositiveIntegerField(
        verbose_name='ID пользователя',
        primary_key=True,
    )
    username = models.CharField(
        max_length=50,
        verbose_name='Логин пользователя',
        unique=True,
    )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.username