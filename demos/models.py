from django.db import models

# Create your models here.
class Demo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    dl_model = models.CharField(max_length=20)
    image = models.FilePathField(path="images/qna.jpg")