from django.urls import path
from .views import UpdateBot
from main import TOKEN

urlpatterns = [
    path(f'webhook/{TOKEN}/', UpdateBot.as_view(), name='update'),
]