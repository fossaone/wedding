from django.db import models

'''YES_OR_NO = (
    (True, 'Yes'),
    (False, 'No')
)'''
# Create your models here.
class Guest(models.Model):
    name = models.CharField(max_length=128)
    email_address = models.EmailField(max_length=75)
    #date = models.DateTimeField('date entered')
    significant_other = models.CharField(max_length=128, blank=True)
    children = models.IntegerField(default=0)    # of kids between 3 and 12.
    babies = models.IntegerField(default=0)                 # of kids under 3
    rehersal_dinner = models.BooleanField()
    wedding = models.BooleanField()
    stay_in_cabin = models.BooleanField()
    vegetarian = models.BooleanField()
    notes = models.CharField(max_length=256)
    #paid = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name
        

#class Payment(models.Model):
    #guests = models..IntegerField()    
    #date = models.DateField(auto_now=True)
    #amount = models.FloatField()