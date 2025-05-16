from django.urls import path
from .views import PaginaInicial, SobreView, AgendaView

urlpatterns = [
    path('', PaginaInicial.as_view(), name='index'),
    path("sobre/", SobreView.as_view(), name="sobre"),
    path("agendas/", AgendaView.as_view(), name="agendas"),
]

