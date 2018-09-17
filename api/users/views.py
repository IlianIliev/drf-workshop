from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from api.books.serializers import BookSerializer
from api.users.serializers import SignupSerializer, ProfileSerializer

from books.models import Book


class SignupView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)
        else:
            return Response(data={}, status=HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        form = AuthenticationForm(data=request.data)

        if form.is_valid():
            login(request, form.get_user())
            return Response({})
        else:
            return Response(form.errors, HTTP_400_BAD_REQUEST)


class ProfileView(RetrieveAPIView, UpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        return self.request.user



class MyBooksViewSet(viewsets.ModelViewSet):
    model = Book
    serializer_class = BookSerializer

    def get_queryset(self):
        qs = Book.objects.all()
        qs = qs.filter(owner=self.request.user)
        return qs
