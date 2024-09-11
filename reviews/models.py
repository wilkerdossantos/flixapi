from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(
        validators=[
            MinValueValidator(
                0, 'Avaliação deve ser maior ou igual à 0 estrelas!'),
            MaxValueValidator(
                5, 'Avaliação deve ser menor ou igual à 5 estrelas!')
        ]
    )
    comment = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.movie
