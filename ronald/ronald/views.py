from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UserForm

def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
    else:
        form = UserForm()
    
    return render(request, 'registration/register.html', { 'form': form })

def about(request):
    return render(request, 'about.html')