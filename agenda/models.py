from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class TaskStatus(models.TextChoices):
    PENDING = 'Pending', 'Pending'
    IN_PROGRESS = 'In Progress', 'In Progress'
    COMPLETED = 'Completed', 'Completed'


class Task(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tarefas_usuario")
    title = models.CharField(max_length=50, verbose_name="título")
    description = models.CharField(max_length=200, verbose_name="descrição", blank=True)
    status = models.CharField(max_length=20, choices=TaskStatus.choices, default=TaskStatus.PENDING)
    due_date = models.DateField(verbose_name="data vencimento")
    priority = models.CharField(max_length=30, verbose_name="prioridade")
    created_at = models.DateTimeField(verbose_name="criado em", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="atualizado em", auto_now=True)
    project = models.ForeignKey('Project', on_delete=models.PROTECT, related_name='tasks')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='tasks')
    labels = models.ManyToManyField('Label', blank=True, related_name='tasks')
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tarefas_criadas")

    def __str__(self):
        if self.due_date and self.created_at and self.due_date < self.created_at.date():
            return f"Data de vencimento ({self.due_date}) é antes da data de criação ({self.created_at.date()})"
        return f"{self.title}"


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="nome")
    description = models.CharField(max_length=200, verbose_name="descrição", blank=True)
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Project(models.Model):
    name = models.CharField(max_length=50, verbose_name="nome")
    description = models.CharField(max_length=200, verbose_name="descrição", blank=True)
    created_at = models.DateTimeField(verbose_name="criado em", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="atualizado em", auto_now=True)
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projetos")

    def __str__(self):
        return f"{self.name}"


class Comment(models.Model):
    content = models.TextField(verbose_name="conteúdo")
    created_at = models.DateTimeField(verbose_name="criado em", auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comentário: {self.content[:30]}..."


class Attachment(models.Model):
    file = models.FileField(upload_to='attachments/', verbose_name="arquivo")
    uploaded_at = models.DateTimeField(verbose_name="enviado em", auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='attachments')
    enviado_por = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Anexo para tarefa: {self.task.title}"


class Label(models.Model):
    name = models.CharField(max_length=50, verbose_name="nome")
    color = models.CharField(max_length=7, verbose_name="cor", default='#FFFFFF')

    def __str__(self):
        return f"{self.name}"
