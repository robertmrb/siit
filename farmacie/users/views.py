from django.shortcuts import render, redirect
from users.forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Inregistrare cu succes.")
            return redirect('homepage')
        messages.error(request, "Inregistrare esuata. Informatii invalide.")
    form = NewUserForm()
    return render(request, 'register.html', {'register_form': form})
