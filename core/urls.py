from django.urls import path
from core import views
from main import TOKEN

urlpatterns = [
    path(f'webhook/{TOKEN}/', views.UpdateBot.as_view(), name='update'),
]