import numpy as np
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
 def handle(self, *args, **kwargs):
    for movie in Movie.objects.all():
        embedding_vector = np.frombuffer(movie.emb, dtype=np.float32)
        print(movie.title, embedding_vector[:5])  # Muestra los primeros valores