from django.db import models

LOC = (
	('bengaluru','Bengaluru'),
	('hydrabad','Hydrabad'),
	('gurgaon','Gurgaon'),
)





class BlogModel(models.Model):
    title   = models.CharField(max_length=100,blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    location    = models.CharField(max_length=40,default='Bengaluru',choices=LOC)
    approved = models.BooleanField(default=False)