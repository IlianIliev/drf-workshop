from rest_framework import serializers

from authors.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'date_of_birth', 'website', 'bio')
