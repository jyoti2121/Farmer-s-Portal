from django.db import models

# Create your models here.
class Services(models.Model):
    service_name = models.CharField(max_length=50)
    service_image = models.ImageField(upload_to='pics')
    service_description = models.TextField()

class News(models.Model):
    news_name = models.CharField(max_length=50)
    news_image = models.ImageField(upload_to='pics')
    news_date = models.DateField()
    news_hidden_text =models.CharField(max_length=50)
    news_description = models.TextField()

class Plantation(models.Model):
    plantation_name = models.CharField(max_length=50)
    plantation_image =models.ImageField(upload_to='pics')

class Teams(models.Model):
    team_name = models.CharField(max_length=50) 
    team_image = models.ImageField(upload_to='pics')
    team_role = models.CharField(max_length=50)

class Gallery(models.Model):
    gallery_text = models.CharField(max_length=50)
    gallery_image = models.ImageField(upload_to='pics')

class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_image = models.ImageField(upload_to='pics')
    customer_title = models.TextField()
    customer_description = models.TextField()
    customer_rating = models.FloatField()

class What_we_do(models.Model):
    what_name = models.CharField(max_length=50)
    what_image = models.ImageField(upload_to='pics')
    what_description = models.TextField()

class Labour(models.Model):
        farmer_id = models.IntegerField()
        labour_name = models.CharField(max_length=50)
        labour_state = models.CharField(max_length=50)
        labours_city = models.CharField(max_length=50)
        labours_role = models.CharField(max_length=50)
        labour_salary = models.IntegerField()

class Tasks(models.Model):
    farmer_id = models.IntegerField()
    task_name = models.CharField(max_length=50)
    task_date = models.DateField()
    task_priority = models.CharField(max_length=50)
    task_complete = models.BooleanField()   
