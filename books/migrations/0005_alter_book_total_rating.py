# Generated by Django 5.0.1 on 2024-02-07 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_remove_author_total_books_remove_book_average_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='total_rating',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]