from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
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
    
# one to many
    
class ProjectReview(models.Model):
    project= models.ForeignKey(projectVariety, on_delete=models.CASCADE, related_name='reviews')
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    rating= models.IntegerField()
    comment=models.TextField()
    date_added= models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.user.username} review for {self.project.name}'
    
# Many to Many
    
class Store(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    project_varieties=models.ManyToManyField(projectVariety,related_name='stores')
    
    def __str__(self):
        return self.name
        
#One to One

class ProjectCertificate(models.Model):
    project= models.OneToOneField(projectVariety,on_delete=models.CASCADE,related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default= timezone.now)
    valid_untill = models.DateTimeField()
    
    def __str__(self):
        return f'Certificate for {self.name.project}'