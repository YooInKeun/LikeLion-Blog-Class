from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import jsonfield


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

# class TimeTable(models.Model):
#     time_table_array = ArrayField(ArrayField(models.CharField(max_length=10), default=list), default=list)

class TimeTable2(models.Model):
    the_json = jsonfield.JSONField()