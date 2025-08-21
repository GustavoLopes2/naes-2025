from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class TelaInicial(TemplateView):
    template_name = 'paginasweb/modelos/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nome"] = "Gustavo L."
        return context

class DashboardView(TemplateView):
    template_name = 'paginasweb/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nome"] = "Gustavo L."
        return context

class SobreView(TemplateView):
    template_name = "paginasweb/sobre.html"

class AgendaView(LoginRequiredMixin, TemplateView):
    template_name = "paginasweb/index.html"
    login_url = 'login'
