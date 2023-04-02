from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='quotes')

    def __str__(self):
        return self.text

