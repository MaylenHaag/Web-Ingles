from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Curso
from .forms import CursoForm



# Vista para la página principal con formularios y listas
def index(request):
    if request.method == 'POST':
        if 'curso_submit' in request.POST:
            form = CursoForm(request.POST)
            if form.is_valid():
                form.save()
            
    cursos = Curso.objects.all()
    
    return render(request, 'AppMaylen/index.html', {
        'curso_form': CursoForm(),
        'cursos': cursos
    })


def about(request) :
    return render(request, "AppMaylen/about.html")



# Vista para crear un curso
class CursoCreateView(LoginRequiredMixin, CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'AppMaylen/create_curso.html'
    success_url = reverse_lazy('lista_curso')

    def form_valid(self, form):
        form.instance.autor = self.request.user 
        return super().form_valid(form)

# Vista para listar cursos
class CursoListView(ListView):
    model = Curso
    template_name = "AppMaylen/lista_curso.html"
    context_object_name = 'cursos'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print("Usuario autenticado:", request.user)
        else:
            print("Usuario no autenticado")
        return super().get(request, *args, **kwargs)


class CursoDetailView(DetailView):
    model = Curso
    template_name = "AppMaylen/detalle_curso.html"


class CursoUpdateView(UpdateView):
    model = Curso
    template_name = "AppMaylen/editar_curso.html"
    success_url = reverse_lazy('lista_curso')
    fields = ['nombre', 'camada', 'horario']


class CursoDeleteView(DeleteView):
    model = Curso
    template_name = "AppMaylen/borrar_curso.html"
    success_url = reverse_lazy("lista_curso")




class AboutUsView(TemplateView):
    template_name = "AppMaylen/about.html"

class ContactUsView(TemplateView):
    template_name = "AppMaylen/contact.html"


