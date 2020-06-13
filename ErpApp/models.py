from django.db import models


class Register(models.Model):
    user_id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    categeory =models.CharField(max_length=50)
    logintime = models.CharField(max_length=20)

    def __str__(self):
        return self.fullname
    
    

    


