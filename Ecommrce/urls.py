from django.contrib import admin
from django.urls import path, include 
urlpatterns = [
    path('', include('core.urls', namespace='core')), 
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'))
]