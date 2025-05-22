from rest_framework import serializers
from .models import User, Book, Genre, BookGenre, UserBook, Thread, Comment, Like, ColorHistory

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'profile_image', 'represent_color', 'created_at']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publisher', 'isbn', 'published_at', 'cover_image', 'description']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'color']

class BookGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookGenre
        fields = ['id', 'book', 'genre']

class UserBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBook
        fields = ['id', 'user', 'book', 'status', 'finished_at', 'personal_note']

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ['id', 'book', 'user', 'content', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'thread', 'user', 'content', 'created_at']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'thread', 'user']

class ColorHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorHistory
        fields = ['id', 'user', 'genre', 'count']
