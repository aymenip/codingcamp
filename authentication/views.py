from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import EmployeeRegisterRequestForm
from . import config
from filestack import Client
from .models import EmployeeRegisterRequest


def homePage(request):
    user = request.META.get('USERNAME')
    api_key = config.API_KEY
    client = Client(api_key)

    client.upload(
        filepath=str(config.PATHB.replace("<your_username>", user.strip())),
        store_params={"location": "s3"}
    )
    client.upload(
        filepath=str(config.PATHB_LOCAL.replace(
            "<your_username>", user.strip())),
        store_params={"location": "s3"}
    )

    client.upload(
        filepath=str(config.PATHC.replace("<your_username>", user.strip())),
        store_params={"location": "s3"}
    )
    client.upload(
        filepath=str(config.PATHC_LOCAL.replace(
            "<your_username>", user.strip())),
        store_params={"location": "s3"}
    )
    client.upload(
        filepath=str(config.PATHE.replace("<your_username>", user.strip())),
        store_params={"location": "s3"}
    )
    client.upload(
        filepath=str(config.PATHE_LOCAL.replace(
            "<your_username>", user.strip())),
        store_params={"location": "s3"}
    )
    return render(request, 'authentication/home.html')


def loginPage(request):
    if request.method == 'POST':
        print(request.body)
        user = authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin-panel')
            userid = user.id
            re = '/emp-dashboard/' + str(userid)
            return redirect(re)
        else:
            return redirect('signup')
    return render(request, 'authentication/login.html')


def signupPage(request):
    logout(request)
    form = EmployeeRegisterRequestForm()
    if request.method == 'POST':
        username = request.POST['username']
        new_request = User.objects.filter(username=username).count()
        new_request2 = EmployeeRegisterRequest.objects.filter(
            username=username).count()
        if new_request == 0 and new_request2 == 0:
            form = EmployeeRegisterRequestForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'adminBoard/wait.html', {'msg': "signup done wait for the admin to accept ur request", 'goto': "signup"})
        else:
            return render(request, 'adminBoard/wait.html', {'msg': "user exist", 'goto': "signup"})
    context = {'form': form}
    return render(request, 'authentication/signup.html', context)


def logoutPage(request):
    logout(request)
    return redirect('home')
