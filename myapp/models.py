from django.db import models

#suppose in name of product name there is space so this slugigy
#will replace space with any char
from django.utils.text import slugify

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='images/')#install pillow for image field
    #“SlugField stores a URL-friendly version of a string, typically used to create readable and SEO-friendly URLs.”
    slug=models.SlugField(unique=True,blank=True)
    stock=models.IntegerField()
    active=models.BooleanField()

    def save(self,*args,**kwargs):
        if not self.slug:
            #self.slug=slugify(self.name)
            #what if two slugs have same name so for that we will add number with it
            base_slug=slugify(self.name)
            slug=base_slug
            counter=1
            while Product.objects.filter(slug=slug).exists():
                slug=f"{base_slug}-{counter}"
                counter+=1
            self.slug=slug
        super().save(*args,**kwargs)