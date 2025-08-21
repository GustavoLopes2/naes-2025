from django.urls import path
from .views import cadastro_view
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

urlpatterns = [
    
    path("login/", LoginView.as_view(
        template_name = "agendas/form.html",
        extra_context={"titulo": "Login"}), name="login"),
    
    path("logout/", LogoutView.as_view(), name="logout"),
    
    path("alterar-senha/", PasswordChangeView.as_view(
        template_name="agendas/form.html",
        extra_context={"titulo": "Alterar minha senha"}), name="alterar-senha"),
    
    path("cadastro/", cadastro_view, name="cadastro")
]


