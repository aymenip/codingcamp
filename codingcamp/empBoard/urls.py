from django.urls import path
from . import views
urlpatterns = [
    path("emp-dashboard/<str:pk_user>", views.dashboardPage, name='emp-dashboard'),
    path("apply/<str:pk_tr>/<str:pk_user>", views.applyPage, name='apply'),
    path("cancel/<str:pk_tr>", views.cancelPage, name='cancel'),
    path("messages/<str:pk_user>", views.messagesPage, name='messages'),
    path("message-delete/<str:pk_msg>/<str:pk_user>", views.deleteMessage, name='message-delete'),
    path("my-trainings/<str:pk_user>", views.myTrainingsPage, name='my-trainings'),
    path("rate/<str:pk_tr>/<str:pk_user>", views.ratePage, name='rate'),
]

