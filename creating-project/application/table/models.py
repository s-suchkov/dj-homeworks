from django.db import models
import csv
class Fields(models.Model):
    name = models.TextField()
    width = models.FloatField()
    id = models.IntegerField(primary_key=True)

class Path_csv(models.Model):
    file = models.FileField(upload_to='application/phones.csv')
    @staticmethod
    def get_path(file):
        with open(file) as f:
            reader = csv.reader(f)
            return reader


