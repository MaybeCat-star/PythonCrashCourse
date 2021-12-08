from django.contrib import admin
from . import views

app_name = 'learning_logs'

urlpatterns = [
    path('', views.index, name='index'),
]
