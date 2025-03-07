from django.db import models

class ScriptInfo(models.Model):
    ScriptName = models.CharField(max_length=30)
    
    def __str__(self):
        return self.ScriptName  

    class Meta:
        ordering=["ScriptName"]
        
class UserInfo(models.Model):
    Name = models.CharField(max_length=30)
    EmailId = models.CharField(max_length=30)
    ContactNo = models.CharField(max_length=15)
    UserName = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    Img = models.ImageField()
    
    def __str__(self):
        return self.UserName
    class Meta:
        ordering=["UserName"]
    
class BuyInfo(models.Model):
    Buydate = models.DateField()
    ScriptName = models.ForeignKey(ScriptInfo,on_delete=models.CASCADE)
    UserName = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    Quantity = models.PositiveBigIntegerField()
    Rate = models.PositiveBigIntegerField()
    Amount = models.PositiveBigIntegerField()
    
class SellInfo(models.Model):
    Selldate = models.DateField(max_length=30)
    ScriptName = models.ForeignKey(ScriptInfo,on_delete=models.CASCADE)
    UserName = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    Quantity = models.PositiveBigIntegerField()
    Rate = models.PositiveBigIntegerField()
    Amount = models.PositiveBigIntegerField()

class PlaceInfo(models.Model):
    Placename = models.CharField(max_length=30)
    Days = models.IntegerField(max_length=30)
    Nights = models.IntegerField(max_length=15)
    Img = models.ImageField()

# Create your models here.
