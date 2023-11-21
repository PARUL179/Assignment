from django.db import models

class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.TextField(unique=True)

class Organization(models.Model):
    org_id = models.AutoField(primary_key=True)
    org_name = models.CharField(max_length=255, unique=True)
    org_phone = models.CharField(max_length=20) 
    org_email = models.EmailField(unique=True)
    
    # Add other fields as needed

    def __str__(self):
        return self.org_name,self.org_email

    service = models.ManyToManyField(Service)