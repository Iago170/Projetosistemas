from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('crud/', include('crud.urls')),
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico')),
    path('', RedirectView.as_view(url='/crud/', permanent=True)),  # Redireciona a raiz para /crud/
]
