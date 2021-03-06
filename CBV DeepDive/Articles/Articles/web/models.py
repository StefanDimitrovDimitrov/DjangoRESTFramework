from django.db import models

# Create your models here.






class Source(models.Model):
    name = models.CharField(max_length=200,)

    url = models.URLField(max_length=200,)

    def __str__(self):
        return self.name


class Articles(models.Model):
    title= models.CharField(
        max_length=100,
    )

    description = models.TextField()
    image_url = models.URLField(
        max_length=200,
    )

    source = models.ForeignKey(Source, on_delete=models.CASCADE)