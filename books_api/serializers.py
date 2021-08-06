from rest_framework import serializers
from books_api.models import BookModel


class BookSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data.get('title'):
            if not data.get('title')[0].isupper():
                raise serializers.ValidationError('Title mus start with capital')
        return data

    class Meta:
        model = BookModel
        fields = '__all__'


