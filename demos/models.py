from django.conf import settings

from django.db import models
from django.utils import timezone


class QAData(models.Model):

    context = models.TextField()
    question = models.TextField()
    answer = models.TextField()
    user = models.TextField()
    published_date = models.DateTimeField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.user
