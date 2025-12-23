from .views import(UserProfileSet, CountrySet, DirectorSet, ActorSet, GenreSet,
                   MovieSet, MovieLanguagesSet, MomentsSet, RatingSet, FavoriteSet,
                   FavoriteMovieSet, HistorySet)
from rest_framework import routers
from django.urls import include, path


router = routers.DefaultRouter()
router.register(r'UserProfile', UserProfileSet)
router.register(r'Country', CountrySet)
router.register(r'Director', DirectorSet)
router.register(r'Actor', ActorSet)
router.register(r'Genre', GenreSet)
router.register(r'Movie', MovieSet)
router.register(r'MovieLanguage', MovieLanguagesSet)
router.register(r'Moments', MomentsSet)
router.register(r'Rating', RatingSet)
router.register(r'Favorite', FavoriteSet)
router.register(r'FavoriteMovie', FavoriteMovieSet)
router.register(r'History', HistorySet)

urlpatterns = [
    path('', include(router.urls))
]