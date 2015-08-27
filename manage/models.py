from django.db import models

# Create your models here.

class Client_eva(models.Model):  # eva - evaluate
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    projectname = models.CharField(max_length=50)
    eva_progress = models.IntegerField()
    eva_quality = models.IntegerField()
    eva_service = models.IntegerField()
    eva_content = models.CharField(max_length=1000)
    add_time = models.DateTimeField(auto_now_add=True)


class Freelancer_eva(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    projectname = models.CharField(max_length=50)
    eva_requirement = models.IntegerField()
    eva_management = models.IntegerField()
    eva_communication = models.IntegerField()
    eva_content = models.CharField(max_length=1000)
    add_time = models.DateTimeField(auto_now_add=True)
