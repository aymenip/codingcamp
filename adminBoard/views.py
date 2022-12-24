from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from authentication.models import EmployeeRegisterRequest
from cataloge.models import Training, Organization


def adminPage(request):

    context = {
               'requestes_len' : EmployeeRegisterRequest.objects.count(),
               'trainings_len' : Training.objects.count(),
               'organizations_len' : Organization.objects.count(),
    }
    return render(request, 'adminBoard/adminBoard.html', context)


def usersPage(request):
    context = {
        'users' : User.objects.all()
    }
    return render(request, 'adminBoard/users.html', context)



def requestesPage(request):
    context = {
        'requestes' : EmployeeRegisterRequest.objects.all()
    }
    return render(request, 'adminBoard/requestes.html', context)


def handleReq(request):
    q, username = request.GET['username'][0], request.GET['username'][1:]
    emp = EmployeeRegisterRequest.objects.get(username=username)
    if q == 'a':
        new_user = User.objects.create_user(emp.username, emp.email, emp.password)
        new_user.first_name = emp.first_name
        new_user.last_name = emp.last_name
        new_user.save()
        attr = ["employ was accepted !!", "admin-panel"]
    elif q == 'r':
        attr = ["employ was rejected !!", "admin-panel"]
    emp.delete()
    return render(request, 'adminBoard/wait.html', context={'msg':attr[0], 'goto': attr[1]})

