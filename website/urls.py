from django.urls import path
from website import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('portfolio', views.portfolio, name='portfolio'),
]
