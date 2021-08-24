from rest_framework import serializers
from .models import BookModel


class BookSerializer(serializers.ModelSerializer):

    def validate(self, data):
        title = data['title']
        if title:
            start_letter = title[0]
            if start_letter.islower():
                raise serializers.ValidationError("Must start with capital letter")
            return data




    class Meta:
        model = BookModel
        fields = "__all__"