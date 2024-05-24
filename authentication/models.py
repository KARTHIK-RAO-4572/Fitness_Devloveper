from django.db import models
# from django_cryptography.fields import encrypt

class User_Data(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    email = models.EmailField(primary_key=True)
    phone = models.IntegerField(unique=True)
    
    def __str__(self):
        return self.username
    def returnUsername(self):
        return self.username
    def returnPassword(self):
        return self.password
    def returnEmail(self):
        return self.email
    def returnPhone(self):
        return self.phone

    