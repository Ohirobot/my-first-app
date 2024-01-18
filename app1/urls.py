from django.urls import path
from . import views

app_name = 'app1'
urlpatterns = [
    #ex: /app1/
    path('', views.index, name='index'),
    #ex: /app1/5
    path('<int:question_id>/', views.detail, name='detail'),
    #ex: /app1/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    #ex: /app1/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]