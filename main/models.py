from django.db import models
from datetime import datetime
# Create your models here.

class learningcatagory(models.Model):
    learning_catagory = models.CharField(max_length=200)
    catagory_summary = models.CharField(max_length=200)
    catagory_slug = models.CharField(max_length=200)


    class Meta:
        verbose_name_plural = "Catagories"

    def __str__(self):
        return self.learning_catagory

class LearningSeries(models.Model):
    learning_series = models.CharField(max_length=200)
    learning_category = models.ForeignKey(learningcatagory,default=1,verbose_name="Catagory", on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
        return self.learning_series


class learning(models.Model):
    learning_title = models.CharField(max_length=200)
    learning_content = models.TextField()
    learning_published = models.DateTimeField("date published",default=datetime.now())

    learning_series = models.ForeignKey(LearningSeries,default=1,verbose_name="Series",on_delete=models.SET_DEFAULT)
    learning_slug = models.CharField(max_length=200,default=1)

    def __str__(self):
        return self.learning_title

