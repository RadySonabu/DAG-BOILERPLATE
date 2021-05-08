from django.db import models

# Create your models here.
class SampleModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class SampleModelForeignKey(models.Model):
    name = models.CharField(max_length=50)
    sample_model_id = models.ForeignKey(SampleModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
