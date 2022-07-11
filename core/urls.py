from django.urls import path
from core import views
from main import TOKEN
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path(f'webhook/{TOKEN}/', csrf_exempt(views.index), name='update'),
]