from django.urls import path, include

from rest_framework import routers

from .authors.views import AuthorViewSet
from .books.views import BookViewSet
from .users.views import SignupView, LoginView, ProfileView, MyBooksViewSet


router = routers.DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)
router.register('my_books', MyBooksViewSet, base_name='my_books')


urlpatterns = [
    path('users/signup', SignupView.as_view()),
    path('users/login', LoginView.as_view()),
    path('profile', ProfileView.as_view()),
    path('', include(router.urls)),
]
