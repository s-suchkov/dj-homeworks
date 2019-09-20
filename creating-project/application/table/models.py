from django.db import models
import csv
class Fields(models.Model):
    name = models.TextField()
    width = models.IntegerField()
    id = models.IntegerField(primary_key=True)

class Path_csv(models.Model):
    file = models.FileField()
    @staticmethod
    def get_path(file):
        with open(file) as f:
            reader = csv.reader(f)
            return reader


