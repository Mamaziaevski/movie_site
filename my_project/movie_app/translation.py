from .models import Country, Director, Actor, Genre, Movie, MovieLanguages
from modeltranslation.translator import TranslationOptions,register

@register(Country)
class CountryTranslationOptions(TranslationOptions):
    list_display = ("country_name",)

@register(Director)
class DirectorTranslationOptions(TranslationOptions):
    list_display = ("director_name", "bio")

@register(Actor)
class ActorTranslationOptions(TranslationOptions):
    list_display = ("Actor", "bio")

@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    list_display = ("genre_name",)

@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    list_display = ("movie_name", "description")

@register(MovieLanguages)
class MovieLanguagesTranslationOptions(TranslationOptions):
    list_display = ("language",)