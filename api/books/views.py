from rest_framework.viewsets import ModelViewSet

from api.books.serializers import BookSerializer
from api.utils import IsOwnerOrReadOnly

from books.models import Book


class BookViewSet(ModelViewSet):
    permission_classes = (IsOwnerOrReadOnly, )
    queryset = Book.objects.all()
    serializer_class = BookSerializer
