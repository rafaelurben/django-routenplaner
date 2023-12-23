from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.conf import settings

from . import views

#######################

app_name = 'routenplaner'
urlpatterns = [
    path('route/<object_id>/', views.view_route, name="view-route"),
    path('route/', views.routes, name="routes"),
    path('manifest.json', views.manifest, name="manifest")
]
