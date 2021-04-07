from django.db import models
from datetime import datetime, date

class TodayList(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500,blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ["-created_date"]
        unique_together = ["title", "description",]
