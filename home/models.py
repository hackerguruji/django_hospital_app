from django.db import models


# Create your models here.
class Form(models.Model):

    name = models.CharField(max_length=122)
    address = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    age = models.CharField(max_length=122)
    work= models.TextField(max_length=122)
    worktype= models.TextField(max_length=122)
    pain= models.TextField(max_length=122)
    bleeding= models.TextField(max_length=122)
    burning= models.TextField(max_length=122)
    itching= models.TextField(max_length=122)
    constipation= models.TextField(max_length=122)
    discharge= models.TextField(max_length=122)
    prolepse= models.TextField(max_length=122)
    anus= models.TextField(max_length=122)
    othercom= models.TextField(max_length=122)
    familyten= models.TextField(max_length=122)   
    


    def __str__(self):
        return self.name
