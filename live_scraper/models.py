from django.db import models


class LiveInfo(models.Model):
    data = models.JSONField()  # Usando JSON para armazenar as informações
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Live {self.timestamp}"
