from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from movie_app.models import User, Profile, Aktor, Sutradara, Genre, Negara, Bahasa, Film, Rating
from api.serializers import RegisterAuthorsSerializer, LoginSerializer, AktorSerializer, SutradaraSerializer, GenreSerializer, NegaraSerializer, BahasaSerializer, FilmSerializer, RatingSerializer, ProfileSerializer
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.db import IntegrityError
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import AllowAny


# AKTOR VIEW
class AktorListAPiView(APIView):
    # 1. List all
    def get(self, request, *args, **kwargs):
        aktors = Aktor.objects.all()
        serializer = AktorSerializer(aktors, many= True)
        response = {
            'status' : status.HTTP_200_OK,
            'message' : 'Retrive all data success...',
            'data' : serializer.data
        }
        return Response(response, status = status.HTTP_200_OK)
    
    # 2. Create 
    def post(self, request, *args, **kwargs):
        data = {
            'nama_aktor': request.data.get('nama_aktor')
        }

        serializer = AktorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': status.HTTP_201_CREATED,
                'message' : 'Data aktor created successfully...',
                'data' : serializer.data
            }
            return Response(response, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# AKTOR DETAIL VIEW
class AktorDetailApiview(APIView):
    # 1. Get Object by Id
    def get_object(self, id):
        try:
            return Aktor.objects.get(id=id)
        except Aktor.DoesNotExist:
            return None

    def get(self, request, id, *args, **kwargs):
        aktor_instance = self.get_object(id)
        if not aktor_instance:
            return Response(
                {
                    'status': status.HTTP_404_NOT_FOUND,
                    'message': 'Data aktor does not exist',
                    'data': {}
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = AktorSerializer(aktor_instance)
        response = {
            'status': status.HTTP_200_OK,
            'message': 'Data aktor retrieved successfully',
            'data': serializer.data
        }

        return Response(response, status=status.HTTP_200_OK)
    
    # 2. Put
    def put(self, request, id, *args, **kwargs):
        aktor_instance = self.get_object(id)
        if not aktor_instance:
            return Response(
                {
                    'status' : status.HTTP_400_BAD_REQUEST,
                    'message' : 'Data aktor does not exist',
                    'data' : {}
                }, status = status.HTTP_400_BAD_REQUEST
            )
        
        data = {
            'nama_aktor': request.data.get('nama_aktor')
        }
        serializer = AktorSerializer(instance = aktor_instance, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': status.HTTP_200_OK,
                'message': 'Data aktor updated successfully...',
                'data': serializer.data
            }
            return Response(response, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    # 3. Delete
    def delete(self, request, id, *args, **kwargs):
        aktor_instance = self.get_object(id)
        if not aktor_instance:
            return Response(
                {
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'Data aktor does not exist..',
                    'data' : {}
                }, status = status.HTTP_400_BAD_REQUEST
            )
        aktor_instance.delete()
        response = {
            'status': status.HTTP_200_OK,
            'message': 'Data aktor deleted successfully..',
        }

        return Response(response, status = status.HTTP_200_OK)


# SUTRADARA VIEW
class SutradaraListAPiView(APIView):
    # 1. List all
    def get(self, request, *args, **kwargs):
        sutradaras = Sutradara.objects.all()
        serializer = SutradaraSerializer(sutradaras, many= True)
        response = {
            'status' : status.HTTP_200_OK,
            'message' : 'Retrive all data success...',
            'data' : serializer.data
        }
        return Response(response, status = status.HTTP_200_OK)
    
    # 2. Create 
    def post(self, request, *args, **kwargs):
        data = {
            'nama_sutradara': request.data.get('nama_sutradara')
        }

        serializer = SutradaraSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': status.HTTP_201_CREATED,
                'message' : 'Data sutradara created successfully...',
                'data' : serializer.data
            }
            return Response(response, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
# SUTRADARA DETAIL VIEW
class SutradaraDetailApiview(APIView):
    #1. Get Object by Id
    def get_object(self, id):
        try:
            return Sutradara.objects.get( id = id)
        except Sutradara.DoesNotExist:
            return None
    def get(self, request, id, *args, **kwargs):
        sutradara_instance = self.get_object(id)
        if not sutradara_instance:
            return Response(
                {
                    'status' : status.HTTP_404_NOT_FOUND,
                    'message' : 'Data sutradara does not exists',
                    'data' : {}
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = SutradaraSerializer(sutradara_instance)
        response = {
            'status' : status.HTTP_200_OK,
            'message' : 'Data sutradara retrieve succesfully',
            'data' : serializer.data
        }

        return Response(response, status = status.HTTP_200_OK)
    
    # 2. Put
    def put(self, request, id, *args, **kwargs):
        sutradara_instance = self.get_object(id)
        if not sutradara_instance:
            return Response(
                {
                    'status' : status.HTTP_400_BAD_REQUEST,
                    'message' : 'Data sutradara does not exist',
                    'data' : {}
                }, status = status.HTTP_400_BAD_REQUEST
            )
        
        data = {
            'nama_sutradara': request.data.get('nama_sutradara')
        }
        serializer = SutradaraSerializer(instance = sutradara_instance, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': status.HTTP_200_OK,
                'message': 'Data sutradara updated successfully...',
                'data': serializer.data
            }
            return Response(response, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    # 3. Delete
    def delete(self, request, id, *args, **kwargs):
        sutradara_instance = self.get_object(id)
        if not sutradara_instance:
            return Response(
                {
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'Data sutradara does not exist..',
                    'data' : {}
                }, status = status.HTTP_400_BAD_REQUEST
            )
        sutradara_instance.delete()
        response = {
            'status': status.HTTP_200_OK,
            'message': 'Data sutradara deleted successfully..',
        }

        return Response(response, status = status.HTTP_200_OK)
    
# GENRE VIEW
class GenreListAPiView(APIView):
    # 1. List all
    def get(self, request, *args, **kwargs):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many= True)
        response = {
            'status' : status.HTTP_200_OK,
            'message' : 'Retrive all data success...',
            'data' : serializer.data
        }
        return Response(response, status = status.HTTP_200_OK)
    
    # 2. Create 
    def post(self, request, *args, **kwargs):
        data = {
            'genre': request.data.get('genre')
        }

        serializer = GenreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': status.HTTP_201_CREATED,
                'message' : 'Data genre created successfully...',
                'data' : serializer.data
            }
            return Response(response, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# GENRE DETAIL VIEW
class GenreDetailApiview(APIView):
    #1. Get Object by Id
    def get_object(self, id):
        try:
            return Genre.objects.get( id = id)
        except Genre.DoesNotExist:
            return None
    def get(self, request, id, *args, **kwargs):
        genre_instance = self.get_object(id)
        if not genre_instance:
            return Response(
                {
                    'status' : status.HTTP_404_NOT_FOUND,
                    'message' : 'Data genre does not exists',
                    'data' : {}
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = GenreSerializer(genre_instance)
        response = {
            'status' : status.HTTP_200_OK,
            'message' : 'Data genre retrieve succesfully',
            'data' : serializer.data
        }

        return Response(response, status = status.HTTP_200_OK)
    
    # 2. Put
    def put(self, request, id, *args, **kwargs):
        genre_instance = self.get_object(id)
        if not genre_instance:
            return Response(
                {
                    'status' : status.HTTP_400_BAD_REQUEST,
                    'message' : 'Data genre does not exist',
                    'data' : {}
                }, status = status.HTTP_400_BAD_REQUEST
            )
        
        data = {
            'genre': request.data.get('genre')
        }
        serializer = GenreSerializer(instance = genre_instance, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': status.HTTP_200_OK,
                'message': 'Data genre updated successfully...',
                'data': serializer.data
            }
            return Response(response, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    # 3. Delete
    def delete(self, request, id, *args, **kwargs):
        genre_instance = self.get_object(id)
        if not genre_instance:
            return Response(
                {
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'Data genre does not exist..',
                    'data' : {}
                }, status = status.HTTP_400_BAD_REQUEST
            )
        genre_instance.delete()
        response = {
            'status': status.HTTP_200_OK,
            'message': 'Data genre deleted successfully..',
        }

        return Response(response, status = status.HTTP_200_OK)

# Negara View
class NegaraListAPiView(APIView):
    # 1. List all
    def get(self, request, *args, **kwargs):
        negaras = Negara.objects.all()
        serializer = NegaraSerializer(negaras, many= True)
        response = {
            'status' : status.HTTP_200_OK,
            'message' : 'Retrive all data success...',
            'data' : serializer.data
        }
        return Response(response, status = status.HTTP_200_OK)
    
    # 2. Create 
    def post(self, request, *args, **kwargs):
        data = {
            'negara': request.data.get('negara')
        }

        serializer = NegaraSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': status.HTTP_201_CREATED,
                'message' : 'Data negara created successfully...',
                'data' : serializer.data
            }
            return Response(response, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# Negara Detail View
class NegaraDetailApiview(APIView):
    #1. Get Object by Id
    def get_object(self, id):
        try:
            return Negara.objects.get( id = id)
        except Negara.DoesNotExist:
            return None
    def get(self, request, id, *args, **kwargs):
        negara_instance = self.get_object(id)
        if not negara_instance:
            return Response(
                {
                    'status' : status.HTTP_404_NOT_FOUND,
                    'message' : 'Data negara does not exists',
                    'data' : {}
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = NegaraSerializer(negara_instance)
        response = {
            'status' : status.HTTP_200_OK,
            'message' : 'Data negara retrieve succesfully',
            'data' : serializer.data
        }

        return Response(response, status = status.HTTP_200_OK)
    
    # 2. Put
    def put(self, request, id, *args, **kwargs):
        negara_instance = self.get_object(id)
        if not negara_instance:
            return Response(
                {
                    'status' : status.HTTP_400_BAD_REQUEST,
                    'message' : 'Data negara does not exist',
                    'data' : {}
                }, status = status.HTTP_400_BAD_REQUEST
            )
        
        data = {
            'negara': request.data.get('negara')
        }
        serializer = NegaraSerializer(instance = negara_instance, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': status.HTTP_200_OK,
                'message': 'Data negara updated successfully...',
                'data': serializer.data
            }
            return Response(response, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    # 3. Delete
    def delete(self, request, id, *args, **kwargs):
        negara_instance = self.get_object(id)
        if not negara_instance:
            return Response(
                {
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'Data negara does not exist..',
                    'data' : {}
                }, status = status.HTTP_400_BAD_REQUEST
            )
        negara_instance.delete()
        response = {
            'status': status.HTTP_200_OK,
            'message': 'Data negara deleted successfully..',
        }

        return Response(response, status = status.HTTP_200_OK)
    

# View Bahasa
class BahasaListAPiView(APIView):
    # 1. List all
    def get(self, request, *args, **kwargs):
        bahasas = Bahasa.objects.all()
        serializer = BahasaSerializer(bahasas, many= True)
        response = {
            'status' : status.HTTP_200_OK,
            'message' : 'Retrive all data success...',
            'data' : serializer.data
        }
        return Response(response, status = status.HTTP_200_OK)
    
    # 2. Create 
    def post(self, request, *args, **kwargs):
        data = {
            'bahasa': request.data.get('bahasa')
        }

        serializer = BahasaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': status.HTTP_201_CREATED,
                'message' : 'Data bahasa created successfully...',
                'data' : serializer.data
            }
            return Response(response, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# View Detail Bahasa
class BahasaDetailApiview(APIView):
    #1. Get Object by Id
    def get_object(self, id):
        try:
            return Bahasa.objects.get( id = id)
        except Bahasa.DoesNotExist:
            return None
    def get(self, request, id, *args, **kwargs):
        bahasa_instance = self.get_object(id)
        if not bahasa_instance:
            return Response(
                {
                    'status' : status.HTTP_404_NOT_FOUND,
                    'message' : 'Data bahasa does not exists',
                    'data' : {}
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = BahasaSerializer(bahasa_instance)
        response = {
            'status' : status.HTTP_200_OK,
            'message' : 'Data bahasa retrieve succesfully',
            'data' : serializer.data
        }

        return Response(response, status = status.HTTP_200_OK)
    
    # 2. Put
    def put(self, request, id, *args, **kwargs):
        bahasa_instance = self.get_object(id)
        if not bahasa_instance:
            return Response(
                {
                    'status' : status.HTTP_400_BAD_REQUEST,
                    'message' : 'Data bahasa does not exist',
                    'data' : {}
                }, status = status.HTTP_400_BAD_REQUEST
            )
        
        data = {
            'bahasa': request.data.get('bahasa')
        }
        serializer = BahasaSerializer(instance = bahasa_instance, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': status.HTTP_200_OK,
                'message': 'Data bahasa updated successfully...',
                'data': serializer.data
            }
            return Response(response, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    # 3. Delete
    def delete(self, request, id, *args, **kwargs):
        bahasa_instance = self.get_object(id)
        if not bahasa_instance:
            return Response(
                {
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'Data bahasa does not exist..',
                    'data' : {}
                }, status = status.HTTP_400_BAD_REQUEST
            )
        bahasa_instance.delete()
        response = {
            'status': status.HTTP_200_OK,
            'message': 'Data bahasa deleted successfully..',
        }

        return Response(response, status = status.HTTP_200_OK)

# View Film
class FilmListApiView(APIView):
    #1. List All
    def get(self, request, *args, **kwargs):
        films = Film.objects.all()
        serializer = FilmSerializer(films, many= True)
        response = {
            'status' : status.HTTP_200_OK,
            'message' : 'Retrive all data success...',
            'data' : serializer.data
        }
        return Response(response, status = status.HTTP_200_OK)
    
    # 2. Create 
    def post(self, request, *args, **kwargs):
        data = {
            'judul': request.data.get('judul'),
            'thumbnail': request.data.get('thumbnail'),
            'status': request.data.get('status'),
            'tahun': request.data.get('tahun'),
            'deskripsi': request.data.get('deskripsi'),
            'durasi': request.data.get('durasi'),
            'sutradara': request.data.get('sutradara'),
            'aktor': request.data.get('aktor'),
            'genre': request.data.get('genre'),
            'negara': request.data.get('negara'),
            'bahasa': request.data.get('bahasa')
        }

        serializer = FilmSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': status.HTTP_201_CREATED,
                'message' : 'Data film created successfully...',
                'data' : serializer.data
            }
            return Response(response, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# View Detail Film
class FilmDetailApiview(APIView):
    #1. Get Object by Id
    def get_object(self, id):
        try:
            return Film.objects.get(id=id)
        except Film.DoesNotExist:
            return None
    def get(self, request, id, *args, **kwargs):
        film_instance = self.get_object(id)
        if not film_instance:
            return Response(
                {
                    'status' : status.HTTP_404_NOT_FOUND,
                    'message' : 'Data film does not exists',
                    'data' : {}
                    },
                    status=status.HTTP_404_NOT_FOUND
            )
        serializer = FilmSerializer(film_instance)
        response = {
            'status' : status.HTTP_200_OK,
            'message' : 'Data film retrieve succesfully',
            'data' : serializer.data
            }
        
        return Response(response, status = status.HTTP_200_OK)
    
    #2. Put
    def put(self, request, id, *args, **kwargs):
        film_instance = self.get_object(id)
        if not film_instance:
            return Response(
                {
                    'status' : status.HTTP_400_BAD_REQUEST,
                    'message' : 'Data film does not exist',
                    'data' : {}
                }, status = status.HTTP_400_BAD_REQUEST
            )
        
        data = {
            'judul': request.data.get('judul'),
            'thumbnail': request.data.get('thumbnail'),
            'status': request.data.get('status'),
            'tahun': request.data.get('tahun'),
            'deskripsi': request.data.get('deskripsi'),
            'durasi': request.data.get('durasi'),
            'sutradara': request.data.get('sutradara'),
            'aktor': request.data.get('aktor'),
            'genre': request.data.get('genre'),
            'negara': request.data.get('negara'),
            'bahasa': request.data.get('bahasa')
        }
        serializer = FilmSerializer(instance = film_instance, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': status.HTTP_200_OK,
                'message': 'Data film updated successfully...',
                'data': serializer.data
            }
            return Response(response, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    # 3. Delete
    def delete(self, request, id, *args, **kwargs):
        film_instance = self.get_object(id)
        if not film_instance:
            return Response(
                {
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'Data film does not exist..',
                    'data' : {}
                }, status = status.HTTP_400_BAD_REQUEST
            )
        film_instance.delete()
        response = {
            'status': status.HTTP_200_OK,
            'message': 'Data film deleted successfully..',
        }

        return Response(response, status = status.HTTP_200_OK)
    
# View Rating
class RatingListAPiView(APIView):
    # 1. List all
    def get(self, request, *args, **kwargs):
        ratings = Rating.objects.all()
        serializer = RatingSerializer(ratings, many= True)
        response = {
            'status' : status.HTTP_200_OK,
            'message' : 'Retrive all data success...',
            'data' : serializer.data
        }
        return Response(response, status = status.HTTP_200_OK)
    
    # 2. Create 
    def post(self, request, *args, **kwargs):
        data = {
            'user': request.data.get('user'),
            'film': request.data.get('film'),
            'rating': request.data.get('rating')
        }

        serializer = RatingSerializer(data=data)
        if serializer.is_valid():
            try:
                serializer.save()
                response = {
                    'status': status.HTTP_201_CREATED,
                    'message': 'Data rating created successfully...',
                    'data': serializer.data
                }
                return Response(response, status=status.HTTP_201_CREATED)
            except IntegrityError:
                response = {
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'Rating with this User and Film already exists.',
                    'data': {}
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            response = {
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Invalid data',
                'data': serializer.errors
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
# View Detail Rating
class RatingDetailApiview(APIView):
    #1. Get Object by Id
    def get_object(self, id):
        try:
            return Rating.objects.get(id=id)
        except Rating.DoesNotExist:
            return None
    def get(self, request, id, *args, **kwargs):
        rating_instance = self.get_object(id)
        if not rating_instance:
            return Response(
                {
                    'status' : status.HTTP_404_NOT_FOUND,
                    'message' : 'Data rating does not exists',
                    'data' : {}
                    },
                    status=status.HTTP_404_NOT_FOUND
            )
        serializer = RatingSerializer(rating_instance)
        response = {
            'status' : status.HTTP_200_OK,
            'message' : 'Data rating retrieve succesfully',
            'data' : serializer.data
            }
        
        return Response(response, status = status.HTTP_200_OK)
    
    # 2. Put
    def put(self, request, id, *args, **kwargs):
        rating_instance = self.get_object(id)
        if not rating_instance:
            return Response(
                {
                    'status' : status.HTTP_400_BAD_REQUEST,
                    'message' : 'Data rating does not exist',
                    'data' : {}
                }, status = status.HTTP_400_BAD_REQUEST
            )
        
        data = {
            'user': request.data.get('user'),
            'film': request.data.get('film'),
            'rating': request.data.get('rating')
        }
        serializer = RatingSerializer(instance = rating_instance, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': status.HTTP_200_OK,
                'message': 'Data rating updated successfully...',
                'data': serializer.data
            }
            return Response(response, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    # 3. Delete
    def delete(self, request, id, *args, **kwargs):
        rating_instance = self.get_object(id)
        if not rating_instance:
            return Response(
                {
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'Data rating does not exist..',
                    'data' : {}
                }, status = status.HTTP_400_BAD_REQUEST
            )
        rating_instance.delete()
        response = {
            'status': status.HTTP_200_OK,
            'message': 'Data rating deleted successfully..',
        }

        return Response(response, status = status.HTTP_200_OK)

# USER LOGIN
@authentication_classes([])
@permission_classes([AllowAny])
class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)

        if user.is_authors:
            message = 'You are logged in as author'
        else:
            message = 'You are logged in as visitor'

        profile = Profile.objects.get(user=user)
        profile_serializer = ProfileSerializer(profile)

        return JsonResponse({
            'data': {
                'token': token.key,
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'is_active': user.is_active,
                'is_authors': user.is_authors,
                'birthday': profile_serializer.data['birth'],
                'avatar': profile_serializer.data['avatar'],
                'bio': profile_serializer.data['bio'],
            },
            'status': 200,
            'message': 'You are logged in now...'
        })

# USER LOGOUT
@authentication_classes([])
@permission_classes([AllowAny])
class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return JsonResponse({'message' : 'You have beenn logout...'})

# USER REGISTRATION
@authentication_classes([])
@permission_classes([AllowAny])
class RegisterAuthorsSerializer(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterAuthorsSerializer

    def post(self, request, format = None):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            user = serializer.save()

            response_data = {
                'status' : status.HTTP_201_CREATED,
                'message' : 'Your account has been registered ...',
                'data' : serializer.data,                
            }
            return Response(response_data, status = status.HTTP_201_CREATED)        
        return Response({
            'status' : status.HTTP_400_BAD_REQUEST,
            'message' : 'Error bang...',
            'data' : serializer.errors,
        }, status = status.HTTP_400_BAD_REQUEST)

class ProfileDetailApiView(APIView):
    def get_object(self, user_id):
        try:
            return Profile.objects.get(user = user_id)
        except Profile.DoesNotExist:
            return None
    
    def get(self, request, user_id, *args, **kwargs):
        profile_instance = self.get_object(user_id)
        if not profile_instance:
            return Response(
                {'response' : 'Data does not exists...'},
                status = status.HTTP_400_BAD_REQUEST
            )