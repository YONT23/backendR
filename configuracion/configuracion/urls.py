from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rentas/', include('apps.rentas.api.urls')),
]
