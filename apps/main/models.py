from django.db import models


class Url(models.Model):
    short = models.URLField()
    url = models.URLField()
