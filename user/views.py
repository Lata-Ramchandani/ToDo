from django.shortcuts import render,redirect 
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

def register(request):
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        # print(form)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'{ username } your account has been created!!,please log in...')
            return redirect('login')
    else:
        form=UserRegistrationForm()
    
    return render(request, 'user/register.html',{'form':form})
    

