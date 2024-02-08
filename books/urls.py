from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books.views import AuthorViewSet, BookViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]