from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.

def register(request):
    form = RegisterForm(request.POST)
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home-page')
        else:
            form = RegisterForm()
    else:
        form = RegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'user_registration/register.html', context)
