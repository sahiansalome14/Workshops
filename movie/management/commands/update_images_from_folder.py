import os
from django.conf import settings
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = "Update movie images in the database"

    def handle(self, *args, **kwargs):
        movies = Movie.objects.all()
        self.stdout.write(f"Found {movies.count()} movies")

        for movie in movies:
            self.stdout.write(f"Processing: {movie.title}")
            try:
                if not movie.image:
                    movie.image = "movie/images/sin_image.jpg"
                else:
                    # Ruta completa del archivo
                    full_path = os.path.join(settings.MEDIA_ROOT, movie.image.name)
                    if not os.path.exists(full_path):
                        movie.image = "movie/images/sin_image.jpg"

                movie.save()
                self.stdout.write(self.style.SUCCESS(f"Updated image for {movie.title}"))
            except Exception as e:
                self.stderr.write(f"Failed for {movie.title}: {str(e)}")
