from django.shortcuts import redirect, render
from cataloge.models import Training, TrainingRequest
from django.contrib.auth.models import User
from .models import Messages, UserTrainings

# Create your views here.
def applyPage(request, pk_tr, pk_user):
    training = Training.objects.get(id = pk_tr)
    user = User.objects.get(id = pk_user)
    training.requests += 1
    newRequest = TrainingRequest.objects.create(user = user, training = training)
    newRequest.save()
    training.save()
    msg = "your requeste was apply wait for admin process"
    return render(request, 'empBoard/apply.html', {'msg': msg})


def dashboardPage(request, pk_user):
    user = User.objects.get(id = pk_user)
    msgs = Messages.objects.filter(user = user)
    user_requestes = TrainingRequest.objects.filter(user = user)
    context = {
        'user_requestes' : user_requestes,
        'user_requestes_len' : user_requestes.count(),
        'msgs_len' : msgs.count(),
    }
    return render(request, 'empBoard/empDashboard.html', context)

def cancelPage(request, pk_tr):
    training = TrainingRequest.objects.get(id = pk_tr)
    c_training_id = training.training.id
    c_training = Training.objects.get(id = c_training_id)
    c_training.requests -= 1
    c_training.save()
    training.delete()
    msg = "training request was canceled succuesfully"
    return render(request, 'empBoard/cancel.html', {'msg': msg})

def messagesPage(request, pk_user):
    user = User.objects.get(id = pk_user)
    msgs = ''
    if not user.is_superuser:
        msgs = Messages.objects.filter(user = user)
    return render(request, 'empBoard/messages.html', {'msgs' : msgs})

def deleteMessage(request, pk_msg, pk_user):
    Messages.objects.get(id = pk_msg).delete()
    msg = "message was deleted !!"
    context = {
        'msg' : msg,
        'goto' : f'/messages/{pk_user}'
    }
    return render(request, 'empBoard/messageDelete.html', context)

def myTrainingsPage(request, pk_user):
    user = User.objects.get(id = pk_user)
    context = {
        'userTrainigs' : UserTrainings.objects.filter(user = user),
    }
    return render(request, 'empBoard/trainings.html', context)

def ratePage(request, pk_tr, pk_user):
    if request.method == "POST":
        user = User.objects.get(id = pk_user) 
        training = Training.objects.get(id = pk_tr)
        rate = float(request.POST['rate'])
        training.participants += 1
        training.rate = round((training.rate + rate) / training.participants)
        training.save()
        user_tr = UserTrainings.objects.get(user=user, training = training)
        user_tr.status = True
        user_tr.save()
    return render(request, "empBoard/rate.html")