from django.db import models
import uuid
from cloudinary.models import CloudinaryField


class Portfolio_Site(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(
        max_length=200, unique=True, blank=False, null=False)
    description = models.CharField(max_length=500)
    image = CloudinaryField(
        'image', default='placeholder', blank=False, null=False)
    link = models.CharField(
        max_length=300, unique=True, blank=False, null=False)
    technologies = models.ManyToManyField('Tech', blank=True)

    class Meta:
        """
        Helper function to organize websites by their id
        """
        ordering = ['id']

    def __str__(self):
        return str(self.title)


class Tech(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)
