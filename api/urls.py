from django.urls import path, include

from rest_framework import routers

from .users.views import SignupView


router = routers.DefaultRouter()


urlpatterns = [
    path('users/signup', SignupView.as_view()),
    path('', include(router.urls)),
]
