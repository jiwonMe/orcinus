from django.db import models


class Letter(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)

    def __str__(self) -> str:
        return self.title
