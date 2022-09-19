from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index,name='index'),
    path('creat/', views.creat,name='creat'),
    path('<int:a>/pow/<int:b>', views.mypow,name='mypow'),
    path('factorial/<int:n>', views.factorial,name='fact'),
    path('<int:question_id>/', views.detail,name='detail'),
    path('<int:question_id>/result/', views.result,name='result'),
    path('<int:question_id>/vate/', views.vate,name='vate'),


]
