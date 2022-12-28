from django.urls import path
from app_1.api.views import PersonListAV, PersonDetailsAV

urlpatterns = [
    path('list/', PersonListAV.as_view()),
    path('list/<int:pk>/', PersonDetailsAV.as_view()),
]