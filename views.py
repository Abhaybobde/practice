from django.shortcuts import render,redirect
from .models import PlatinumModel,goldModel,silverModel
from .form import PlatinumForms,goldForms,silverForms,SignupForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def gold_view(r):
    form  = goldForms()
    if r.method =="POST":
        form = goldForms(r.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(r,"credit/Gold.html",{'form':form})
@login_required
def platinum_view(r):
    form = PlatinumForms()
    if r.method =="POST":
        form = PlatinumForms(r.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(r,"credit/platinum.html", {'form':form})
@login_required
def silver_view(r):
    form = silverForms()
    if r.method =="POST":
        form = silverForms(r.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(r,"credit/Silver.html", {'form':form})

def Signupview(r):
    form = SignupForm()
    if r.method == "POST":
        form = SignupForm(r.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return redirect('/accounts/login/')
    return render(r,'registration/signup.html', {'form': form})


