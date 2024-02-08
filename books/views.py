from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Author, Book, Review
from .serializers import AuthorSerializer, BookSerializer, ReviewSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes,permission_classes

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):
        author = self.get_object()
        reviews = Review.objects.filter(author=author)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        review = serializer.instance
        review.update_ratings()
        serializer = self.get_serializer(review)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class CustomAuthTokenLogin(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'FirstName' : user.first_name,
            'LastName' : user.last_name,
        })