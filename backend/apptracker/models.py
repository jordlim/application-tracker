from django.db import models

class Application(models.Model):
    title = models.CharField(max_length=120)
    company = models.CharField(max_length=120)
    applied = models.BooleanField(default=False)

    def _str_(self):
        return self.title