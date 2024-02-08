
from rest_framework import serializers
from .models import Author, Book, Review

class AuthorSerializer(serializers.ModelSerializer):
    book_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'book_count', 'total_rating', 'average_rating']
        read_only_fields = ['total_rating', 'average_rating']

class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field='name')

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'total_rating', 'average_rating']
        read_only_fields = ['total_rating', 'average_rating']
        
class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field='name')
    book = serializers.SlugRelatedField(queryset=Book.objects.all(), slug_field='title')

    class Meta:
        model = Review
        fields = ['id', 'author', 'book', 'rating', 'comment']