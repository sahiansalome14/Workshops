# movie/management/commands/fix_movie_images.py

import os
from django.core.management.base import BaseCommand
from django.conf import settings
from movie.models import Movie

class Command(BaseCommand):
    help = "Update movie images to default if the original file does not exist"

    def handle(self, *args, **kwargs):
        movies = Movie.objects.all()
        self.stdout.write(f"Found {movies.count()} movies")

        for movie in movies:
            image_path = os.path.join(settings.MEDIA_ROOT, movie.image.name)
            if not os.path.exists(image_path):
                movie.image = 'movie/images/sin_image.jpg'
                movie.save(update_fields=['image'])
                self.stdout.write(self.style.WARNING(f"Updated image for {movie.title}"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Image exists for {movie.title}"))
