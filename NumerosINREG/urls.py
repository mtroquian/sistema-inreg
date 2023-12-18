from django.urls import path
from . import views

urlpatterns = [

    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('index', views.index, name='index'),
    path('crear', views.crear, name='crear'),
    path('editar', views.editar, name='editar'),
    path('abc', views.abc, name='abc')
]