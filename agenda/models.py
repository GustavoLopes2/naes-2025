from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name="título")
    descrption = models.CharField(max_length=200, verbose_name="descrição", blank=True)
    #status =
    due_date = models.DateField(verbose_name="data vencimento")
    priority = models.CharField(max_length=30, verbose_name="prioridade")
    created_at = models.DateTimeField(verbose_name="criado em", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="atualizado em", auto_now=True)

    #Método ToString() para imprimir objetos
    def __str__(self):
        if():
            return f"Data de vencimento ({self.due_date}) é antes da data de criação ({self.created_at})"
        else:
            return f"{self.title}"
            

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="nome")
    description = models.CharField(max_length=200, verbose_name="descrição", blank=True)
    task = models.ForeignKey(
        Task, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name}"      


class Project(models.Model):
    name = models.CharField(max_length=50, verbose_name="nome")
    description = models.CharField(max_length=200, verbose_name="descrição", blank=True)
    created_at = models.DateTimeField(verbose_name="criado em", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="atualizado em", auto_now=True)
    task = models.ForeignKey(
        Task, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name}"
