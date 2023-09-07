from django.db import models
from news.validators import most_common_validation


class Categories(models.Model):
    name = models.CharField(**most_common_validation)

    def __str__(self):
        return self.name
