from django.urls import path
from . import views
urlpatterns = [
    path('admin-panel', views.adminPage, name='admin-panel'),
    path('users', views.usersPage, name='users'),
    path('requestes', views.requestesPage, name='requestes'),
    path('handle-requestes', views.handleReq, name='handle-requestes'),
]
