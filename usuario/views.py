from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def cadastro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'usuario/cadastro.html', {'form': form})
