from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Task, Category, Project, Comment, Attachment, Label


class TaskCreate(CreateView):
    template_name = "agendas/form.html"
    model = Task
    success_url = reverse_lazy("listar-tarefas")
    fields = ["title", "description", "status", "due_date", "priority", "project", "category", "labels"]
    extra_context = {"titulo": "Cadastro de Tarefa",
                     "model_name": "tarefas"}

class CategoryCreate(CreateView):
    template_name = "agendas/form.html"
    model = Category
    success_url = reverse_lazy("listar-categorias")
    fields = ["name", "description"]
    extra_context = {"titulo": "Cadastro de Categoria",
                     "model_name": "categorias"}


class ProjectCreate(CreateView):
    template_name = "agendas/form.html"
    model = Project
    success_url = reverse_lazy("listar-projetos")
    fields = ["name", "description"]
    extra_context = {"titulo": "Cadastro de Projeto",
                     "model_name": "projetos"}


class CommentCreate(CreateView):
    template_name = "agendas/form.html"
    model = Comment
    success_url = reverse_lazy("listar-comentarios")
    fields = ["content", "task"]
    extra_context = {"titulo": "Cadastro de Comentário",
                     "model_name": "comentarios"}


class AttachmentCreate(CreateView):
    template_name = "agendas/form.html"
    model = Attachment
    success_url = reverse_lazy("listar-anexos")
    fields = ["file", "task"]
    extra_context = {"titulo": "Cadastro de Anexo",
                     "model_name": "anexos"}


class LabelCreate(CreateView):
    template_name = "agendas/form.html"
    model = Label
    success_url = reverse_lazy("listar-etiquetas")
    fields = ["name", "color"]
    extra_context = {"titulo": "Cadastro de Etiqueta",
                     "model_name": "etiquetas"}


# Edit Views
class TaskUpdate(UpdateView):
    template_name = "agendas/form.html"
    model = Task
    success_url = reverse_lazy("listar-tarefas")
    fields = ["title", "description", "status", "due_date", "priority", "project", "category", "labels"]
    extra_context = {"titulo": "Editar Tarefa",
                     "model_name": "tarefas"}


class CategoryUpdate(UpdateView):
    template_name = "agendas/form.html"
    model = Category
    success_url = reverse_lazy("listar-categorias")
    fields = ["name", "description"]
    extra_context = {"titulo": "Editar Categoria",
                     "model_name": "categorias"}


class ProjectUpdate(UpdateView):
    template_name = "agendas/form.html"
    model = Project
    success_url = reverse_lazy("listar-projetos")
    fields = ["name", "description"]
    extra_context = {"titulo": "Editar Projeto",
                     "model_name": "projetos"}


class CommentUpdate(UpdateView):
    template_name = "agendas/form.html"
    model = Comment
    success_url = reverse_lazy("listar-comentarios")
    fields = ["content", "task"]
    extra_context = {"titulo": "Editar Comentário",
                     "model_name": "comentarios"}


class AttachmentUpdate(UpdateView):
    template_name = "agendas/form.html"
    model = Attachment
    success_url = reverse_lazy("listar-anexos")
    fields = ["file", "task"]
    extra_context = {"titulo": "Editar Anexo",
                     "model_name": "anexos"}


class LabelUpdate(UpdateView):
    template_name = "agendas/form.html"
    model = Label
    success_url = reverse_lazy("listar-etiquetas")
    fields = ["name", "color"]
    extra_context = {"titulo": "Editar Etiqueta",
                     "model_name": "etiquetas"}


#Delete Views
class TaskDelete(DeleteView):
    template_name = "agendas/form.html"
    model = Task
    success_url = reverse_lazy("listar-tarefas")
    extra_context = {"titulo": "Deletar Tarefa"}

class CategoryDelete(DeleteView):
    template_name = "agendas/form.html"
    model = Category
    success_url = reverse_lazy("listar-categorias")
    extra_context = {"titulo": "Deletar Categoria"}

class ProjectDelete(DeleteView):
    template_name = "agendas/form.html"
    model = Project
    success_url = reverse_lazy("listar-projetos")
    extra_context = {"titulo": "Deletar Projeto"}

class CommentDelete(DeleteView):
    template_name = "agendas/form.html"
    model = Comment
    success_url = reverse_lazy("listar-comentarios")
    extra_context = {"titulo": "Deletar Comentário"}

class AttachmentDelete(DeleteView):
    template_name = "agendas/form.html"
    model = Attachment
    success_url = reverse_lazy("listar-anexos")
    extra_context = {"titulo": "Deletar Anexo"}

class LabelDelete(DeleteView):
    template_name = "agendas/form.html"
    model = Label
    success_url = reverse_lazy("listar-etiquetas")
    extra_context = {"titulo": "Deletar Etiqueta"}


# List Views
class TaskList(ListView):
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

class CategoryList(ListView):
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

class ProjectList(ListView):
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

class CommentList(ListView):
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

class AttachmentList(ListView):
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

class LabelList(ListView):
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
