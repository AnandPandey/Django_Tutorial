from django.db import models
from django.utils import timezone
# Create your models here.
class projectVariety(models.Model):
    PROJECT_TYPE_CHOICE = [
        ('ML','MACHINE LEARNING'),
        ('AI', 'ARTIFICIAL INTELLIGENCE'),
        ( 'WD','WEB DEVELOPMENT'),
        ('SEIR','SEARCH ENGINE INFO RETRIEVAL')
    ]
    name=models.CharField(max_length=100)
    image= models.ImageField(upload_to= 'projects/')
    date_added= models.DateTimeField(default= timezone.now)
    type= models.CharField(max_length=4, choices= PROJECT_TYPE_CHOICE)
    description = models.TextField(default='')
    
    def __str__(self):
        return self.name