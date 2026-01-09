from django.urls import path
from registrations.views import RegisterPilgrim

urlpatterns = [
    path("api/register/", RegisterPilgrim.as_view()),
]
