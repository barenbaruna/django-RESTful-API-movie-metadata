# Generated by Django 4.2.1 on 2023-05-04 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie_app", "0005_alter_film_durasi_alter_film_tahun"),
    ]

    operations = [
        migrations.CreateModel(
            name="Bahasa",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("bahasa", models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name="film",
            name="bahasa",
            field=models.ManyToManyField(
                related_name="bahasa_film", to="movie_app.bahasa"
            ),
        ),
    ]
