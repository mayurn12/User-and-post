from django.urls import path
from .import views
from. views import HomePage,CreateViewUser
urlpatterns = [
    path('',HomePage.as_view()),
    path('create/',CreateViewUser.as_view())
]