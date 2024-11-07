from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login


def index(request):
    login_form = None
    register_form = None
    
    return render(request, "fullstack/auth.html", context={"login_form": login_form, "register_form": register_form})


def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...


def register(request):
    pass


def user_profile(request):
    if not request.user.is_authenticated:
        return redirect(f"/")
