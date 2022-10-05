from django.db import models

# musicians/models.py

class Content(models.Model):
    title = models.CharField(max_length=50)
    module = models.TextField()
    students = models.IntegerField()
    description = models.TextField()
    is_active = models.BooleanField(default = False)

