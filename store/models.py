from email.policy import default
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db import IntegrityError, models, router, transaction


class cafe(models.Model):
    City=(
        ('Riyadh','Riyadh'),
        ('Jeddah','Jeddah'),
        ('Dammam','Dammam')
    )
   # working=(
        #('Morning','Morning'),
        #('Night','Night'),
     

    #)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
 
    name=models.CharField(max_length=200)
    disc=models.TextField(default=" Cozy cafe ")
    picture=models.ImageField(upload_to="media/images/")
    recent_picture=models.FileField(upload_to="media/images/recent_picture")
    recent_picture_2=models.FileField(upload_to="media/images/recent_picture_2")
    recent_picture_3=models.FileField(upload_to="media/images/recent_picture_3")
    city=models.CharField( max_length= 200, choices=City)
    working_hours=models.CharField(max_length= 200)
    signture=models.CharField(max_length=200)
    #menu=models.
    created_on=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
      if not self.id:
        self.slug = slugify(self.name)

      super(cafe, self).save(*args, **kwargs)

class Review(models.Model):
    rate_choese=[
            ("1","1"),
            ("2","2"),
            ("3","3"),
            ("4","4"),
            ("5","5"),
            ("6","6"),
        ]
    cafe_name=models.ForeignKey(cafe,related_name="comments",on_delete=models.CASCADE)
    rating=models.CharField(choices=rate_choese ,default=3,max_length=100)
    content=models.TextField()
    created_by=models.ForeignKey(User,on_delete=CASCADE)
    user_picture=models.ImageField(upload_to="media/images/profile" , default='user.png')
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.cafe_name.name+'|'+ str(self.created_by)








