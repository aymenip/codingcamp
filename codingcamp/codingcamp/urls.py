from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import adminBoard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('adminBoard.urls')),
    path('', include('empBoard.urls')),
    path('', include('authentication.urls')),
    path('', include('cataloge.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
