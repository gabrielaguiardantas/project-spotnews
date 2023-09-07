from django.db import models
from news.validators import most_common_validation


class Users(models.Model):
    name = models.CharField(**most_common_validation)
    email = models.EmailField(**most_common_validation)
    password = models.CharField(**most_common_validation)
    role = models.CharField(**most_common_validation)

    def __str__(self):
        return self.name
