from django.shortcuts import render
from .forms import LoginForm
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from .forms import SignUpForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,'11index.html')
def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(username,password)
            print("--------------------------")
            print("welcome",username)
            return redirect('homepage')           
    return render(request, '11index.html',{'form':form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print('form is valid')
            form.save()
            msg = 'user created'
            return redirect('index')
        elif User.objects.filter(username = request.POST['username']).exists():
            return render(request, 'user_exist.html')
        elif request.POST['username'] == request.POST['password1']:
            return render(request, 'user_pass_cannot_same.html')
        elif len(request.POST['username']) < 8:
            return render(request, 'password_below_8.html')
        elif request.POST['password1'] and request.POST['password2'] and request.POST['password1']  != request.POST['password2']:
            return render(request , 'pass_cpass_doent_match.html')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
        return render(request,'22signup.html',{'form': form})

def homepage(request):
    return render(request,'33homepage.html')
def logout(request):
    return render(request,'11index.html')
def invest(request):
    return render(request,'44invest.html')
def project_details(request):
    return render(request,'55project_details.html')


