from .models import(UserProfile, Country, Director, Actor, Genre, Movie, MovieLanguages, Moments, Rating, Favorite, FavoriteMovie, History)
from .serializers import(UserProfileSerializer, CountrySerializer, DirectorSerializer, ActorSerializer,
                         GenreSerializer, MovieListSerializer, MovieDetailSerializer, MovieLanguagesSerializer, MomentsSerializer,
                         RatingSerializer, FavoriteSerializer, FavoriteMovieSerializer, HistorySerializer)
from rest_framework import viewsets

class UserProfileSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CountrySet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class DirectorSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class ActorSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class GenreSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class MovieSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieLanguagesSet(viewsets.ModelViewSet):
    queryset = MovieLanguages.objects.all()
    serializer_class = MovieLanguagesSerializer

class MomentsSet(viewsets.ModelViewSet):
    queryset = Moments.objects.all()
    serializer_class = MomentsSerializer

class RatingSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class FavoriteSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class FavoriteMovieSet(viewsets.ModelViewSet):
    queryset = FavoriteMovie.objects.all()
    serializer_class = FavoriteMovieSerializer

class HistorySet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
