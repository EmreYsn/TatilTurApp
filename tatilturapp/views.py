from django.shortcuts import render , redirect
from . import models
from django.urls import reverse , reverse_lazy
from tatilturapp.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

# Create your views here.

def homepage(request):
    if request.method == "post":
        form = SignUpForm(request.post)
        if form.is_valid():
            username = form.cleaned_data["username_input"]
            models.TatilTur.objects.create(username=username)
            return redirect(reverse('tatilturapp:case'))
        else:
            print("error in form!")
            return render(request,'tatilturapp/homepage.html', context={"form":form})
    else:
        form = SignUpForm()
        return render(request,'tatilturapp/homepage.html', context={"form":form})

@login_required(login_url="/login")
def case(request):
    return render(request,'tatilturapp/case.html')

def favourites(request):
    return render(request,'tatilturapp/favourites.html')

@login_required(login_url="/login")
def çanakkale(request):
    return render(request,'tatilturapp/çanakkale.html')

@login_required(login_url="/login")
def caseçanakkale(request):
    return render(request,'tatilturapp/caseçanakkale.html')

@login_required(login_url="/login")
def bursa(request):
    return render(request,'tatilturapp/bursa.html')

@login_required(login_url="/login")
def casebursa(request):
    return render(request,'tatilturapp/casebursa.html')

@login_required(login_url="/login")
def izmir(request):
    return render(request,'tatilturapp/izmir.html')

@login_required(login_url="/login")
def caseizmir(request):
    return render(request,'tatilturapp/caseizmir.html')

@login_required(login_url="/login")
def antalya(request):
    return render(request,'tatilturapp/antalya.html')

@login_required(login_url="/login")
def caseantalya(request):
    return render(request,'tatilturapp/caseantalya.html')

@login_required(login_url="/login")
def istanbul(request):
    return render(request,'tatilturapp/istanbul.html')

@login_required(login_url="/login")
def caseistanbul(request):
    return render(request,'tatilturapp/caseistanbul.html')

@login_required(login_url="/login")
def muğla(request):
    return render(request,'tatilturapp/muğla.html')

@login_required(login_url="/login")
def casemuğla(request):
    return render(request,'tatilturapp/casemuğla.html')

@login_required(login_url="/login")
def trabzon(request):
    return render(request,'tatilturapp/trabzon.html')

@login_required(login_url="/login")
def casetrabzon(request):
    return render(request,'tatilturapp/casetrabzon.html')

@login_required(login_url="/login")
def adana(request):
    return render(request,'tatilturapp/adana.html')

@login_required(login_url="/login")
def caseadana(request):
    return render(request,'tatilturapp/caseadana.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"