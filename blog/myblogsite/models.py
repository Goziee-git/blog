from django.db import models
from django.utils import timezone
from django.conf import settings 


# Create your models here.
class PublishedManager(models.Manager):
   def get_queryset(self):
      return(
         super().get_queryset().filter(status=Post.status.PUBLISHED)
      )
#data model for blog post. 
class Post(models.Model):
   '''
   A ommon frature for blogs is to save post as drafts until they are published, so we add a status field to allow us manage 
   the status of blog post 
   '''
   class Status(models.TextChoices):
      DRAFT = 'DF', 'Draft'
      PUBLISHED = 'PB', 'Published'
   
   objects = models.Manager() #the defaut manager
   published = PublishedManager() #our custom manager
   title = models.CharField(max_length=250) #the post tile
   slug = models.SlugField(max_length=250) #SlugField translates in a VARCHAR column ib the SQL db
   author = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE,
      related_name='blog_posts'
   )
   body = models.TextField() #stores the body of the post. TestField that translates into a text column in the SQL db
   publish = models.DateTimeField(default=timezone.now) #translares into a DATETIME colun in the SQL db
   '''
   in Django5, another method to define default values for model fields is usinf database computed default values, allowing for the use of underlying Db functions 
   to generate default values, eg, the following code will use the DB server's current data time as the default for the publish field
   >> from django.db.models.functions import Now 
   - within the class, add to the publish field with this
   >> publish = models.DateTimeField(db_default=Now())
   '''
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   status = models.CharField(
      max_length=2,
      choices=Status,
      default=Status.DRAFT
   )
   '''
   We can access Post.Status.choices to obtain the available choices, Post.Status.names to obtain the 
   names of the choices, Post.Status.labels to obtain the human-readable names, and Post.Status.
   values to obtain the actual values of the choices.
   created = this field uses the auto_now_add to store the date and time when the new post is created automatically
   updated = this field uses the auto_now to store the last data and time when the posr was updated when saving a post object.
   '''
   class Meta: 
      #this nested Meta class defines metadata for the model.uses the ordering attribute for sorting the post objects by the publish field
      #the ordering will apply be default when no other order is specified on default. the - before the field name indicates descending order, thus posr
      #will be returned in reverse chronological order by default
      ordering = ['-publish']
      indexes = [
         models.Index(fields=['-publish']),
      ]


   def __str__(self):
      return self.title