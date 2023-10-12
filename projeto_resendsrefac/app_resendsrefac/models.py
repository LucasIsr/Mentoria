from django.db import models

class Adress(models.Model):
    id_adress=models.AutoField(primary_key=True)
    street=models.CharField(max_length=100,blank=False,null=False)
    number=models.IntegerField(blank=False,null=False)
    cep=models.IntegerField(blank=False,null=False)

class Resident(models.Model):
    id_resident=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,blank=False,null=False)
    surname=models.CharField(max_length=100,blank=False,null=False)
    age=models.IntegerField(blank=False,null=False)
    email=models.CharField(max_length=150,blank=False,null=False)

    def __str__(self)-> str:
        return self.id_resident
    
    def __str__(self)-> str:
        return self.id_adress
    
    