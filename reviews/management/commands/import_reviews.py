import csv
from django.core.management.base import BaseCommand
from reviews.models import Review
from movies.models import Movie


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        file_name = kwargs["file_name"]
        with open(file_name, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                movie = Movie.objects.get(title=row["movie"])
                stars = row["stars"]
                comment = row["comment"]
                self.stdout.write(self.style.NOTICE(movie))
                Review.objects.create(movie=movie, stars=stars, comment=comment)
        self.stdout.write(self.style.SUCCESS("Reviews imported successfully!"))

    def add_arguments(self, parser):
        parser.add_argument(
            "file_name",
            type=str,
            help="The path to the CSV file containing reviews",
        )
