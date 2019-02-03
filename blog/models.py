from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

#Custom manager

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status = 'published')

class Post(models.Model):

   # DRAFT = 'draft'
    #PUBLISHED = 'draft'

    BLOG_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length= 70)
    body = models.TextField()
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    slug = models.SlugField(max_length= 250, unique_for_date='publish')
    publish = models.DateTimeField(default= timezone.now)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)
    status = models.CharField(max_length= 15, choices = BLOG_CHOICES, default= 'draft')

    # default manager

    objects = models.Manager()

    # Custom manager

    published = PublishedManager()


    class Meta:
        ordering = ('-publish', )

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post_detail_view',
            args=[self.publish.year, self.publish.strftime('%m'), self.publish.strftime('%d'), self.slug])

