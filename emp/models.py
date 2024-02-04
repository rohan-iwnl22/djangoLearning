from django.db import models
class Emp(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    working = models.BooleanField(default=True)
    department = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    

class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    testimonial = models.TextField()
    picture = models.ImageField(upload_to="testimonials/")
    rating =models.IntegerField()
    
    def __str__(self) -> str:
        return self.testimonial