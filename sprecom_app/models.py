from django.db import models

# Create your models here.
class spre_URL(models.Model):
    spre_url = models.CharField(max_length=80)

    def __str__(self):
        return self.spre_url_text