from django.db import models
from django.db.models.signals import pre_save,post_save
from .utils import unique_slug_generator


class productManager(models.Manager):
    def featured(self):
        return self.get_queryset().filter(featured=True)




    def getbyid(self,id):
        qs=self.get_queryset().filter(id=id)
        if qs.count()==1:
            return qs.first()
        return None
# Create your models here.
class product(models.Model):
    title=models.CharField(max_length=120)
    slug=models.SlugField(blank=True,unique=True)
    description=models.TextField()
    price=models.DecimalField(decimal_places=2,max_digits=10,null=True)
    image=models.ImageField(upload_to='products/',null=True,blank=True)
    featured=models.BooleanField(default=False)
    objects=productManager()

    def get_absolute_url(self):
        return "/products/{slug}/".format(slug=self.slug)


    def __str__(self):

        return self.title

    def __unicode__(self):
        return self.title    


def product_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
pre_save.connect(product_pre_save_receiver,sender=product)        