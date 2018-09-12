from rest_framework import serializers

from authors.models import Author


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('url', 'name', 'date_of_birth', 'website', 'bio')
