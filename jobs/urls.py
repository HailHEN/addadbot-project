from django.urls import path

from . import views

app_name = "jobs"

urlpatterns = [
    path("",views.viewStats,name="view_stats"),
]



