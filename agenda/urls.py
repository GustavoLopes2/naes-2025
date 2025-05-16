from django.urls import path
from .views import (
    TaskCreate,
    CategoryCreate,
    ProjectCreate,
    CommentCreate,
    AttachmentCreate,
    LabelCreate,
)

from .views import (
    TaskUpdate,
    CategoryUpdate,
    ProjectUpdate,
    CommentUpdate,
    AttachmentUpdate,
    LabelUpdate,
)

from .views import (
    TaskDelete,
    CategoryDelete,
    ProjectDelete,
    CommentDelete,
    AttachmentDelete,
    LabelDelete,
)

from .views import (
    TaskList,
    CategoryList,
    ProjectList,
    CommentList,
    AttachmentList,
    LabelList,
)

urlpatterns = [
    path("cadastrar/tarefa/", TaskCreate.as_view(), name="cadastrar-tarefa"),
    path("cadastrar/categoria/", CategoryCreate.as_view(), name="cadastrar-categoria"),
    path("cadastrar/projeto/", ProjectCreate.as_view(), name="cadastrar-projeto"),
    path("cadastrar/comentario/", CommentCreate.as_view(), name="cadastrar-comentario"),
    path("cadastrar/anexo/", AttachmentCreate.as_view(), name="cadastrar-anexo"),
    path("cadastrar/etiqueta/", LabelCreate.as_view(), name="cadastrar-etiqueta"),

    path("editar/tarefa/<int:pk>/", TaskUpdate.as_view(), name="editar-tarefa"),
    path("editar/categoria/<int:pk>/", CategoryUpdate.as_view(), name="editar-categoria"),
    path("editar/projeto/<int:pk>/", ProjectUpdate.as_view(), name="editar-projeto"),
    path("editar/comentario/<int:pk>/", CommentUpdate.as_view(), name="editar-comentario"),
    path("editar/anexo/<int:pk>/", AttachmentUpdate.as_view(), name="editar-anexo"),
    path("editar/etiqueta/<int:pk>/", LabelUpdate.as_view(), name="editar-etiqueta"),

    path("deletar/tarefa/<int:pk>/", TaskDelete.as_view(), name="deletar-tarefa"),
    path("deletar/categoria/<int:pk>/", CategoryDelete.as_view(), name="deletar-categoria"),
    path("deletar/projeto/<int:pk>/", ProjectDelete.as_view(), name="deletar-projeto"),
    path("deletar/comentario/<int:pk>/", CommentDelete.as_view(), name="deletar-comentario"),
    path("deletar/anexo/<int:pk>/", AttachmentDelete.as_view(), name="deletar-anexo"),
    path("deletar/etiqueta/<int:pk>/", LabelDelete.as_view(), name="deletar-etiqueta"),

    path("listar/tarefas/", TaskList.as_view(), name="listar-tarefas"),
    path("listar/categorias/", CategoryList.as_view(), name="listar-categorias"),
    path("listar/projetos/", ProjectList.as_view(), name="listar-projetos"),
    path("listar/comentarios/", CommentList.as_view(), name="listar-comentarios"),
    path("listar/anexos/", AttachmentList.as_view(), name="listar-anexos"),
    path("listar/etiquetas/", LabelList.as_view(), name="listar-etiquetas"),
]
