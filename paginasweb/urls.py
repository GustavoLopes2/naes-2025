from django.urls import path
from .views import DashboardView, SobreView, AgendaView, TelaInicial

urlpatterns = [
    path('', TelaInicial.as_view(), name='inicio'),
    path('dashboard/', DashboardView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('agendas/', AgendaView.as_view(), name='agendas'),
]

