from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import TrainingForm, OrganizationForm
from .models import Training, Organization, TrainingRequest
from empBoard.models import Messages, UserTrainings

def CatalogePage(request):
    trainings = Training.objects.all()
    context = {
        'trainings' : trainings,
    }
    return render(request, 'cataloge/main_cataloge.html', context)




def TrainingPage(request):
    context = {
        'trainings' : Training.objects.all(),
    }

    return render(request, 'cataloge/training.html', context)


def OrganizationPage(request):
    context = {
        'organizations' : Organization.objects.all(),
    }
    return render(request, 'cataloge/organization.html', context)


def processPage(request, pk_tr):
    training = Training.objects.get(id = pk_tr)
    p_trainings = TrainingRequest.objects.filter(training = training)
    return render(request, 'cataloge/process.html', {'p_trainings': p_trainings})

def handleProcessPage(request, pk_tr):
    p_training = TrainingRequest.objects.get(id = pk_tr)
    training = p_training.training
    user = p_training.user
    training.requests -= 1
    training.save()
    p = request.GET['q']
    if p == 'a':
        UserTrainings.objects.create(user = user, training = training, status = False).save()
        p_training.status = True
        p_training.save()
        newmsg = Messages.objects.create(user = user, result = "acceptd", training_name = training.title, content_url = training.content.url)
    else:
        p_training.delete()
        newmsg = Messages.objects.create(user = user, result = "rejectd", training_name = training.title, content_url = "#")
    newmsg.save()
    return redirect("cataloge")
