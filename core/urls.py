from django.urls import path
from core import views
from main import TOKEN
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path(f'webhook/{TOKEN}/', views.UpdateBot.as_view(), name='update'),
]