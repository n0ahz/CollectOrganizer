from django.db import models


class LibraryPath(models.Model):
    """Defines the db for storing HDD paths for importing Media Collection"""
    media_path = models.CharField(max_length=500)
    media_type = models.CharField(max_length=100)

    class Meta:
        unique_together = ['media_type', 'media_path']

    def __str__(self):
        return self.media_type + " : " + self.media_path