from rest_framework import serializers

from api.authors.serializers import AuthorSerializer
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'authors', 'description')
