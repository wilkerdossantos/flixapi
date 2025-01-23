import csv
from django.core.management.base import BaseCommand
from movies.models import Movie
from genres.models import Genre
from actors.models import Actor


class Command(BaseCommand):

    def handle(self, *args, **options):
        file_name = options['file_name']
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                title = row['title']
                genre = Genre.objects.get(name=row['genre'])
                release_date = row['release_date']
                resume = row['resume']
                actors = Actor.objects.filter(name__in=row['actors'].split(','))
                self.stdout.write(self.style.NOTICE(title))
                movie = Movie.objects.create(
                    title=title,
                    genre=genre,
                    release_date=release_date,
                    resume=resume
                )
                movie.actors.add(*actors)
        self.stdout.write(self.style.SUCCESS('Movies imported successfully!'))

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Filename with movies.',
        )
