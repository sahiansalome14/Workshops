import numpy as np
import random
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = "Muestra los embeddings de una película seleccionada al azar"

    def handle(self, *args, **kwargs):
        # Obtener todas las películas
        movies = Movie.objects.all()
        if not movies.exists():
            self.stdout.write(self.style.ERROR("❌ No hay películas en la base de datos"))
            return

        # Seleccionar una película aleatoria
        movie = random.choice(movies)

        # Convertir el campo binario a un vector numpy
        embedding_vector = np.frombuffer(movie.emb, dtype=np.float32)

        # Mostrar resultados
        self.stdout.write(self.style.SUCCESS(f"🎬 Película seleccionada: {movie.title}"))
        self.stdout.write(f"Embedding (primeros 100 valores): {embedding_vector[:100]}")
        self.stdout.write(f"Dimensión del embedding: {embedding_vector.shape[0]}")
