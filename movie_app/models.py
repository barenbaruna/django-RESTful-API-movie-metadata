from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from PIL import Image

# Create your models here.
class User(AbstractUser):
    is_authors = models.BooleanField(default = False)
    is_visitors = models.BooleanField(default = False)

    def __str__(self):
        return str(self.username) + '' + str(self.first_name) + ' ' + str(self.last_name)

class Profile(models.Model):
    status_choices = (
        ('Aktif','Aktif'),
        ('Tidak Aktif', 'Tidak Aktif'),
    )
    user = models.OneToOneField(User, related_name = 'user_profile', on_delete= models.PROTECT)
    birth = models.DateField(blank = True, null=True, default=None)
    avatar = models.ImageField(default= 'profile_images/person.png', upload_to= 'profile_images', blank = True, null= True)
    bio = models.TextField(blank = True, null=True, default=None)
    status = models.CharField(max_length = 15, choices= status_choices, default = 'Aktif')
    user_create = models.ForeignKey(User, related_name= 'user_create_profile', blank = True, null = True, on_delete = models.SET_NULL)
    user_update = models.ForeignKey(User, related_name= 'user_update_profile', blank = True, null = True, on_delete = models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.user.first_name + ' ' + str(self.user.last_name))

    def save(self, *args, **kwargs):
        super().save()
        try:
            img = Image.open(self.avatar_path)
            if img.height > 200 or img.width > 200:
                new_img = (200, 200)
                img.thumbnail(new_img)
                img.save(self.avatar.path)
        except:
            pass

class Aktor(models.Model):
    nama_aktor = models.CharField(max_length = 255)

    def __str__(self):
        return self.nama_aktor

class Sutradara(models.Model):
    nama_sutradara = models.CharField(max_length = 255)

    def __str__(self):
        return self.nama_sutradara
    
class Genre(models.Model):
    genre = models.CharField(max_length = 255)

    def __str__(self):
        return self.genre

class Negara(models.Model):
    negara = models.CharField(max_length = 255)

    def __str__(self):
        return self.negara

class Bahasa(models.Model):
    bahasa = models.CharField(max_length = 100)

    def __str__(self):
        return self.bahasa
    
class Film(models.Model):
    status_film = (
        ('Released', 'Released'),
        ('Upcoming', 'Upcoming'),
    )
    judul = models.CharField(max_length= 255)
    thumbnail = models.ImageField(default= 'film_images/film-default.png', upload_to= 'film_images/', blank = True, null= True)
    status = models.CharField(max_length = 15, choices = status_film, default = 'Released')
    tahun = models.PositiveIntegerField(validators =[MaxValueValidator(9999)])
    deskripsi = models.TextField()
    durasi = models.PositiveIntegerField(help_text='Format: in Minutes')
    sutradara = models.ManyToManyField(Sutradara, related_name = 'sutradara_film')
    aktor = models.ManyToManyField(Aktor, related_name = 'aktor_film')
    genre = models.ManyToManyField(Genre, related_name = 'genre_film')
    negara = models.ManyToManyField(Negara, related_name = 'negara_film')
    bahasa = models.ManyToManyField(Bahasa, related_name = 'bahasa_film')
    user_create = models.ForeignKey(User, related_name = 'user_create_film', blank = True, null = True, on_delete = models.SET_NULL)
    user_update = models.ForeignKey(User, related_name = 'user_update_film', blank = True, null = True, on_delete = models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    
    def clean(self):
        super().clean()

        # aturan ukuran gambar maksimum adalah 1 MB (1048576 bytes)
        if self.thumbnail:
            img = Image.open(self.thumbnail)
            if self.thumbnail.size > 1048576:
                raise ValidationError(_('File gambar terlalu besar. Ukuran maksimal adalah 1 MB'))

    def __str__(self):
        return str(self.judul) + ' ' + str(self.status) + ' in ' + str(self.tahun)

class Rating(models.Model):
    user = models.ForeignKey(User, related_name = 'user_reviewed_made_by', on_delete = models.CASCADE)
    film = models.ForeignKey(Film, related_name = 'user_reviewed_film', on_delete = models.CASCADE)
    rating = models.DecimalField(max_digits = 3, decimal_places = 1,validators = [MinValueValidator(0.0), MaxValueValidator(10.0)])
    user_create = models.ForeignKey(User, related_name = 'user_create_ulasan', blank = True, null = True, on_delete = models.SET_NULL)
    user_update = models.ForeignKey(User, related_name = 'user_update_ulasan', blank = True, null = True, on_delete = models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)

    # User hanya bisa memberikan satu Ulasan untuk satu Film.
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'film'], name='nama_pengulas_film_unique')
        ]
    def __str__(self):
        return str(self.user) + ' memberikan rating ' + str(self.rating) + ' untuk film ' + str(self.film)
