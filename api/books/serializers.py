from rest_framework import serializers

from api.authors.serializers import AuthorSerializer

from authors.models import Author
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    set_authors = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Author.objects.all(), write_only=True, source='authors')

    class Meta:
        model = Book
        fields = ('id', 'title', 'authors', 'description', 'set_authors')
