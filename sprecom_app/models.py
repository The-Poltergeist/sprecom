from django.db import models

# Create your models here.
class React(models.Model):
    spre_url = models.CharField(max_length=80)
    number_of_recs = models.IntegerField(default=1)

    def __str__(self):
        return self.spre_url_text