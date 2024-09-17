from django.urls import path
from AppMaylen import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),

    path('crear-curso/', views.CursoCreateView.as_view(), name='create_curso'),
    path('cursos/', views.CursoListView.as_view(), name='lista_curso'),
    path('detalle-curso/<pk>', views.CursoDetailView.as_view(), name='detalle_curso'),
    path('curso/<pk>/editar', views.CursoUpdateView.as_view(), name='editar_curso'),
    path('curso/<pk>/borrar', views.CursoDeleteView.as_view(), name='borrar_curso'),

    path('about/', views.AboutUsView.as_view(), name="about"),
    path('contact/', views.ContactUsView.as_view(), name="contact"),
]