from django.urls import path
from . import views
urlpatterns = [
   path('training', views.TrainingPage, name='training'),
   path('organization', views.OrganizationPage, name='organization'),
   path('cataloge', views.CatalogePage, name='cataloge'),
   path('process/<str:pk_tr>', views.processPage, name='process'),
   path('handle-process/<str:pk_tr>', views.handleProcessPage, name='handle-process'),
]
