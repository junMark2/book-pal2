from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User, Book, Genre, BookGenre, UserBook, Thread, Comment, Like, ColorHistory
from .serializers import UserSerializer, BookSerializer, GenreSerializer, BookGenreSerializer, UserBookSerializer, ThreadSerializer, CommentSerializer, LikeSerializer, ColorHistorySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticated]

class BookGenreViewSet(viewsets.ModelViewSet):
    queryset = BookGenre.objects.all()
    serializer_class = BookGenreSerializer
    permission_classes = [IsAuthenticated]

class UserBookViewSet(viewsets.ModelViewSet):
    queryset = UserBook.objects.all()
    serializer_class = UserBookSerializer
    permission_classes = [IsAuthenticated]

class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = [IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

class ColorHistoryViewSet(viewsets.ModelViewSet):
    queryset = ColorHistory.objects.all()
    serializer_class = ColorHistorySerializer
    permission_classes = [IsAuthenticated]

class UserRepresentColorViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user = request.user
        color_history = ColorHistory.objects.filter(user=user)
        if not color_history.exists():
            return Response({"represent_color": None}, status=status.HTTP_200_OK)

        # Calculate the representational color based on the color history
        most_common_genre = color_history.order_by('-count').first().genre
        represent_color = most_common_genre.color

        return Response({"represent_color": represent_color}, status=status.HTTP_200_OK)
