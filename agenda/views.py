from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Task, Category, Project, Comment, Attachment, Label


class TaskCreate(CreateView):
    template_name = "agendas/form.html"
    model = Task
    success_url = reverse_lazy("index")
    fields = ["title", "description", "status", "due_date", "priority", "project", "category", "labels"]
    extra_context = {"titulo": "Cadastro de Tarefa"}


class CategoryCreate(CreateView):
    template_name = "agendas/form.html"
    model = Category
    success_url = reverse_lazy("index")
    fields = ["name", "description"]
    extra_context = {"titulo": "Cadastro de Categoria"}


class ProjectCreate(CreateView):
    template_name = "agendas/form.html"
    model = Project
    success_url = reverse_lazy("index")
    fields = ["name", "description"]
    extra_context = {"titulo": "Cadastro de Projeto"}


class CommentCreate(CreateView):
    template_name = "agendas/form.html"
    model = Comment
    success_url = reverse_lazy("index")
    fields = ["content", "task"]
    extra_context = {"titulo": "Cadastro de Comentário"}


class AttachmentCreate(CreateView):
    template_name = "agendas/form.html"
    model = Attachment
    success_url = reverse_lazy("index")
    fields = ["file", "task"]
    extra_context = {"titulo": "Cadastro de Anexo"}


class LabelCreate(CreateView):
    template_name = "agendas/form.html"
    model = Label
    success_url = reverse_lazy("index")
    fields = ["name", "color"]
    extra_context = {"titulo": "Cadastro de Etiqueta"}


# Edit Views
class TaskUpdate(UpdateView):
    template_name = "agendas/form.html"
    model = Task
    success_url = reverse_lazy("index")
    fields = ["title", "description", "status", "due_date", "priority", "project", "category", "labels"]
    extra_context = {"titulo": "Editar Tarefa"}


class CategoryUpdate(UpdateView):
    template_name = "agendas/form.html"
    model = Category
    success_url = reverse_lazy("index")
    fields = ["name", "description"]
    extra_context = {"titulo": "Editar Categoria"}


class ProjectUpdate(UpdateView):
    template_name = "agendas/form.html"
    model = Project
    success_url = reverse_lazy("index")
    fields = ["name", "description"]
    extra_context = {"titulo": "Editar Projeto"}


class CommentUpdate(UpdateView):
    template_name = "agendas/form.html"
    model = Comment
    success_url = reverse_lazy("index")
    fields = ["content", "task"]
    extra_context = {"titulo": "Editar Comentário"}


class AttachmentUpdate(UpdateView):
    template_name = "agendas/form.html"
    model = Attachment
    success_url = reverse_lazy("index")
    fields = ["file", "task"]
    extra_context = {"titulo": "Editar Anexo"}


class LabelUpdate(UpdateView):
    template_name = "agendas/form.html"
    model = Label
    success_url = reverse_lazy("index")
    fields = ["name", "color"]
    extra_context = {"titulo": "Editar Etiqueta"}


#Delete Views
class TaskDelete(DeleteView):
    template_name = "agendas/form.html"
    model = Task
    success_url = reverse_lazy("index")
    extra_context = {"titulo": "Deletar Tarefa"}

class CategoryDelete(DeleteView):
    template_name = "agendas/form.html"
    model = Category
    success_url = reverse_lazy("index")
    extra_context = {"titulo": "Deletar Categoria"}

class ProjectDelete(DeleteView):
    template_name = "agendas/form.html"
    model = Project
    success_url = reverse_lazy("index")
    extra_context = {"titulo": "Deletar Projeto"}

class CommentDelete(DeleteView):
    template_name = "agendas/form.html"
    model = Comment
    success_url = reverse_lazy("index")
    extra_context = {"titulo": "Deletar Comentário"}

class AttachmentDelete(DeleteView):
    template_name = "agendas/form.html"
    model = Attachment
    success_url = reverse_lazy("index")
    extra_context = {"titulo": "Deletar Anexo"}

class LabelDelete(DeleteView):
    template_name = "agendas/form.html"
    model = Label
    success_url = reverse_lazy("index")
    extra_context = {"titulo": "Deletar Etiqueta"}


#List Views
class TaskList(ListView):
    template_name = "agendas/lista.html"
    model = Task

class CategoryList(ListView):
    template_name = "agendas/lista.html"
    model = Category

class ProjectList(ListView):
    template_name = "agendas/lista.html"
    model = Project

class CommentList(ListView):
    template_name = "agendas/lista.html"
    model = Comment

class AttachmentList(ListView):
    template_name = "agendas/lista.html"
    model = Attachment

class LabelList(ListView):
    template_name = "agendas/lista.html"
    model = Label