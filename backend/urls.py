from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, BookViewSet, GenreViewSet, BookGenreViewSet, UserBookViewSet, ThreadViewSet, CommentViewSet, LikeViewSet, ColorHistoryViewSet, UserRepresentColorViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'books', BookViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'book-genres', BookGenreViewSet)
router.register(r'user-books', UserBookViewSet)
router.register(r'threads', ThreadViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'color-history', ColorHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user-represent-color/', UserRepresentColorViewSet.as_view({'get': 'list'})),
]
