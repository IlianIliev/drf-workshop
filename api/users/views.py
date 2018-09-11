from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .serializers import SignupSerializer


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
