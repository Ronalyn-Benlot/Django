from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at =models.DateTimeField(auto_now_add=True,db_index=True)
    updated_at= models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class Position(BaseModel):
    description=models.CharField(max_length=100)



