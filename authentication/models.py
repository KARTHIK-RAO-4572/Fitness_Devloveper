from django.db import models

class User_Data(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(primary_key=True)
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

    