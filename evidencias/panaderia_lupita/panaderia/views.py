from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactoForm

def home(request):
   
    
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Formulario enviado correctamente!')
            return redirect('home')
    else:
        form = ContactoForm()
    
    return render(request, 'panaderia/index.html', {
        'form': form
    })