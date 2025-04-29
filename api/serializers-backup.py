from rest_framework import serializers, exceptions
from movie_app.models import User, Profile, Aktor, Sutradara, Genre, Negara, Bahasa, Film, Rating
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.db.models import Avg


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username', '')
        password = data.get('password', '')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active and (user.is_authors or user.is_visitors):
                    data['user'] = user
                else:
                    msg = 'User is deactivated'
                    raise exceptions.ValidationError(msg)
            else:
                msg = 'Unable to login with given credentials'
                raise exceptions.ValidationError(msg)
        else:
            msg = 'Must provide username and password both'
            raise exceptions.ValidationError(msg)

        return data

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = {'id', 'user', 'birth', 'avatar', 'bio', 'status'}

class RegisterAuthorsSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password1 = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_active', 'is_authors', 'is_visitors', 'first_name', 'last_name']
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({
                'password': 'Password field did not match'
            })

        if attrs.get('is_authors') and attrs.get('is_visitors'):
            raise serializers.ValidationError({
                'is_authors': 'Author and visitors can not be selected at the same time'
            })
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            is_active=validated_data['is_active'],
            is_authors=validated_data['is_authors'],
            is_visitors=validated_data['is_visitors'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password1'])
        user.save()
        profile = Profile.objects.create(user=user, user_create=user)
        profile.save()
        return user

class AktorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aktor
        fields = ('id', 'nama_aktor')

class SutradaraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sutradara
        fields = ('id', 'nama_sutradara')

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'genre')

class NegaraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Negara
        fields = ('id', 'negara')

class BahasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bahasa
        fields = ('id', 'bahasa')

# Nested Serializers untuk FilmSerializer
class FilmSerializer(serializers.ModelSerializer):
    sutradara = serializers.PrimaryKeyRelatedField(
        queryset=Sutradara.objects.all(),
        many=True,
        allow_empty=False  # Memastikan tidak boleh kosong
    )
    aktor = serializers.PrimaryKeyRelatedField(
        queryset=Aktor.objects.all(),
        many=True,
        allow_empty=False  # Memastikan tidak boleh kosong
    )
    genre = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        many=True,
        allow_empty=False  # Memastikan tidak boleh kosong
    )
    negara = serializers.PrimaryKeyRelatedField(
        queryset=Negara.objects.all(),
        many=True,
        allow_empty=False  # Memastikan tidak boleh kosong
    )
    bahasa = serializers.PrimaryKeyRelatedField(
        queryset=Bahasa.objects.all(),
        many=True,
        allow_empty=False  # Memastikan tidak boleh kosong
    )

    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Film
        fields = '__all__'

    # Perlu memanggil --> from django.db.models import Avg
    def get_average_rating(self, obj):
        ratings = Rating.objects.filter(film=obj)
        if ratings.exists():
            average = ratings.aggregate(Avg('rating'))['rating__avg']
            return round(average, 1)
        return None

class RatingSerializer(serializers.ModelSerializer):
    film = serializers.PrimaryKeyRelatedField(queryset=Film.objects.all())

    class Meta:
        model = Rating
        fields = '__all__'