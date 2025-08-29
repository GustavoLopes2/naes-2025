from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Task, Category, Project, Comment, Attachment, Label
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

class TaskCreate(LoginRequiredMixin, CreateView):
    template_name = "agendas/form.html"
    model = Task
    success_url = reverse_lazy("listar-tarefas")
    fields = ["title", "description", "status", "due_date", "priority", "project", "category", "labels"]
    extra_context = {"titulo": "Cadastro de Tarefa",
                     "model_name": "tarefas"}
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.criado_por = self.request.user
        return super().form_valid(form)

class CategoryCreate(LoginRequiredMixin, CreateView):
    template_name = "agendas/form.html"
    model = Category
    success_url = reverse_lazy("listar-categorias")
    fields = ["name", "description"]
    extra_context = {"titulo": "Cadastro de Categoria",
                     "model_name": "categorias"}
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.criado_por = self.request.user
        return super().form_valid(form)


class ProjectCreate(LoginRequiredMixin, CreateView):
    template_name = "agendas/form.html"
    model = Project
    success_url = reverse_lazy("listar-projetos")
    fields = ["name", "description"]
    extra_context = {"titulo": "Cadastro de Projeto",
                     "model_name": "projetos"}
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.criado_por = self.request.user
        return super().form_valid(form)


class CommentCreate(LoginRequiredMixin, CreateView):
    template_name = "agendas/form.html"
    model = Comment
    success_url = reverse_lazy("listar-comentarios")
    fields = ["content", "task"]
    extra_context = {"titulo": "Cadastro de Comentário",
                     "model_name": "comentarios"}


class AttachmentCreate(LoginRequiredMixin, CreateView):
    template_name = "agendas/form.html"
    model = Attachment
    success_url = reverse_lazy("listar-anexos")
    fields = ["file", "task"]
    extra_context = {"titulo": "Cadastro de Anexo",
                     "model_name": "anexos"}


class LabelCreate(LoginRequiredMixin, CreateView):
    template_name = "agendas/form.html"
    model = Label
    success_url = reverse_lazy("listar-etiquetas")
    fields = ["name", "color"]
    extra_context = {"titulo": "Cadastro de Etiqueta",
                     "model_name": "etiquetas"}


# Edit Views
class TaskUpdate(LoginRequiredMixin, UpdateView):
    template_name = "agendas/form.html"
    model = Task
    success_url = reverse_lazy("listar-tarefas")
    fields = ["title", "description", "status", "due_date", "priority", "project", "category", "labels"]
    extra_context = {"titulo": "Editar Tarefa",
                     "model_name": "tarefas"}
    
    def get_object(self):
        return get_object_or_404(Task, pk=self.kwargs["pk"], criado_por=self.request.user)


class CategoryUpdate(LoginRequiredMixin, UpdateView):
    template_name = "agendas/form.html"
    model = Category
    success_url = reverse_lazy("listar-categorias")
    fields = ["name", "description"]
    extra_context = {"titulo": "Editar Categoria",
                     "model_name": "categorias"}
    
    def get_object(self):
        return get_object_or_404(Category, pk=self.kwargs["pk"], criado_por=self.request.user)


class ProjectUpdate(LoginRequiredMixin, UpdateView):
    template_name = "agendas/form.html"
    model = Project
    success_url = reverse_lazy("listar-projetos")
    fields = ["name", "description"]
    extra_context = {"titulo": "Editar Projeto",
                     "model_name": "projetos"}
    
    def get_object(self):
        return get_object_or_404(Project, pk=self.kwargs["pk"], criado_por=self.request.user)


class CommentUpdate(LoginRequiredMixin, UpdateView):
    template_name = "agendas/form.html"
    model = Comment
    success_url = reverse_lazy("listar-comentarios")
    fields = ["content", "task"]
    extra_context = {"titulo": "Editar Comentário",
                     "model_name": "comentarios"}


class AttachmentUpdate(LoginRequiredMixin, UpdateView):
    template_name = "agendas/form.html"
    model = Attachment
    success_url = reverse_lazy("listar-anexos")
    fields = ["file", "task"]
    extra_context = {"titulo": "Editar Anexo",
                     "model_name": "anexos"}


class LabelUpdate(LoginRequiredMixin, UpdateView):
    template_name = "agendas/form.html"
    model = Label
    success_url = reverse_lazy("listar-etiquetas")
    fields = ["name", "color"]
    extra_context = {"titulo": "Editar Etiqueta",
                     "model_name": "etiquetas"}


#Delete Views
class TaskDelete(LoginRequiredMixin, DeleteView):
    template_name = "agendas/form.html"
    model = Task
    success_url = reverse_lazy("listar-tarefas")
    extra_context = {"titulo": "Deletar Tarefa"}

    def get_object(self):
        return get_object_or_404(Task, pk=self.kwargs["pk"], criado_por=self.request.user)

class CategoryDelete(LoginRequiredMixin, DeleteView):
    template_name = "agendas/form.html"
    model = Category
    success_url = reverse_lazy("listar-categorias")
    extra_context = {"titulo": "Deletar Categoria"}

    def get_object(self):
        return get_object_or_404(Category, pk=self.kwargs["pk"], criado_por=self.request.user)

class ProjectDelete(LoginRequiredMixin, DeleteView):
    template_name = "agendas/form.html"
    model = Project
    success_url = reverse_lazy("listar-projetos")
    extra_context = {"titulo": "Deletar Projeto"}

    def get_object(self):
        return get_object_or_404(Project, pk=self.kwargs["pk"], criado_por=self.request.user)

class CommentDelete(LoginRequiredMixin, DeleteView):
    template_name = "agendas/form.html"
    model = Comment
    success_url = reverse_lazy("listar-comentarios")
    extra_context = {"titulo": "Deletar Comentário"}

class AttachmentDelete(LoginRequiredMixin, DeleteView):
    template_name = "agendas/form.html"
    model = Attachment
    success_url = reverse_lazy("listar-anexos")
    extra_context = {"titulo": "Deletar Anexo"}

class LabelDelete(LoginRequiredMixin, DeleteView):
    template_name = "agendas/form.html"
    model = Label
    success_url = reverse_lazy("listar-etiquetas")
    extra_context = {"titulo": "Deletar Etiqueta"}


# List Views
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = "agendas/lista.html"
    extra_context = {
        "titulo": "Lista de Tarefas",
        "campos": [
            {"name": f.name, "label": f.verbose_name.title()}
            for f in Task._meta.fields if f.name != "id"
        ],
        "model_name": "tarefa"
    }
    
    def get_queryset(self):
        return Task.objects.filter(usuario=self.request.user)

class CategoryList(LoginRequiredMixin, ListView):
    model = Category
    template_name = "agendas/lista.html"
    extra_context = {
        "titulo": "Lista de Categorias",
        "campos": [
            {"name": f.name, "label": f.verbose_name.title()}
            for f in Category._meta.fields if f.name != "id"
        ],
        "model_name": "categoria"
    }

class ProjectList(LoginRequiredMixin, ListView):
    model = Project
    template_name = "agendas/lista.html"
    extra_context = {
        "titulo": "Lista de Projetos",
        "campos": [
            {"name": f.name, "label": f.verbose_name.title()}
            for f in Project._meta.fields if f.name != "id"
        ],
        "model_name": "projeto"
    }

class CommentList(LoginRequiredMixin, ListView):
    model = Comment
    template_name = "agendas/lista.html"
    extra_context = {
        "titulo": "Lista de Comentários",
        "campos": [
            {"name": f.name, "label": f.verbose_name.title()}
            for f in Comment._meta.fields if f.name != "id"
        ],
        "model_name": "comentario"
    }

class AttachmentList(LoginRequiredMixin, ListView):
    model = Attachment
    template_name = "agendas/lista.html"
    extra_context = {
        "titulo": "Lista de Anexos",
        "campos": [
            {"name": f.name, "label": f.verbose_name.title()}
            for f in Attachment._meta.fields if f.name != "id"
        ],
        "model_name": "anexo"
    }

class LabelList(LoginRequiredMixin, ListView):
    model = Label
    template_name = "agendas/lista.html"
    extra_context = {
        "titulo": "Lista de Etiquetas",
        "campos": [
            {"name": f.name, "label": f.verbose_name.title()}
            for f in Label._meta.fields if f.name != "id"
        ],
        "model_name": "etiqueta"
    }
