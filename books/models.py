
from django.db import models
class Author(models.Model):
    name = models.CharField(max_length=200)
    total_rating = models.IntegerField(default=0)
    average_rating = models.FloatField(default=0) 
    def book_count(self):
        return self.book_set.count()
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    total_rating = models.IntegerField(default=0)
    average_rating = models.FloatField(default=0)

    def __str__(self):
        return self.title

class Review(models.Model):
    RATING_CHOICES = [(i, i) for i in range(1, 6)]  # Ratings from 1 to 5
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  
        self.update_ratings()

    def update_ratings(self):
       
        book_reviews = Review.objects.filter(book=self.book)
        self.book.total_rating = sum(review.rating for review in book_reviews)
        self.book.average_rating = self.book.total_rating / book_reviews.count()
        self.book.save()

        author_reviews = Review.objects.filter(author=self.author)
        self.author.total_rating = sum(review.rating for review in author_reviews)
        self.author.average_rating = self.author.total_rating / author_reviews.count()
        self.author.save()