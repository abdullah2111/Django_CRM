from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    ROLE_CHOICE = [
        ('Sales Rep' , 'Sales Representative'),
    ] 

    full_name = models.CharField(max_length=150)
    role =  models.CharField(max_length=250, choices=ROLE_CHOICE, default='Sales Rep')
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, blank=True, null=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['full_name', 'role']
    

    def __str__(self):
        return self.email
    



class Contact(models.Model):
    STATUS_CHOICES =[
        ('New Lead', 'New Lead'),
        ('Contacted', 'Contacted'),
        ('Qualified', 'Qualified'),
        ('Converted', 'Converted'),
        ('Lost', 'Lost'),
    ]

    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name= 'contacts')
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    company = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New Lead')
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self): return self.full_name 





# class Activity(models.Model):
#     ACTIVITY_CHOICES = [
#         ('Call', 'Call'),
#         ('Email', 'Email'),
#         ('Meeting', 'Meeting'),
#         ('Follow-up', 'Follow-up'),
#         ('Converted', 'Converted'),
#         ('Lost', 'Lost'),
#     ]
    
#     contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='activities')
#     activity_type = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.activity_type} - {self.contact.full_name}'

