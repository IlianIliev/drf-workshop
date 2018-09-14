from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.books.serializers import BookSerializer
from api.utils import IsOwnerOrReadOnly

from books.models import Book


class BookViewSet(ModelViewSet):
    permission_classes = (IsOwnerOrReadOnly, )
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(methods=['POST'], detail=True)
    def like(self, request, pk):
        book = self.get_object()
        book.liked_by.add(request.user)

        return Response({})
