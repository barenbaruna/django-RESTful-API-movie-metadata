# Generated by Django 4.2.1 on 2023-05-04 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "movie_app",
            "0008_rating_remove_film_ulasan_delete_ulasan_rating_film_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="film",
            name="thumbnail",
            field=models.ImageField(
                blank=True,
                default="film_images/film.jpg",
                null=True,
                upload_to="film_images/",
            ),
        ),
    ]
