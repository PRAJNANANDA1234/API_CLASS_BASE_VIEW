from django.db import models

# Create your models here.
class Product_catagory(models.Model):
    pc_name=models.CharField(max_length=100)
    pc_id=models.IntegerField(primary_key=True)
    
    def __str__(self):
        return self.pc_name

class Product(models.Model):
    pc_name=models.ForeignKey(Product_catagory,on_delete=models.CASCADE)
    pid=models.IntegerField()
    pname=models.CharField(max_length=100)
    pprice=models.IntegerField()
    pdate=models.DateField()

    def __str__(self):
        return self.pname