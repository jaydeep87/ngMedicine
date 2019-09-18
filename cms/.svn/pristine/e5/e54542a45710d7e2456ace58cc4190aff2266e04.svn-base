from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from hfu_cms.models import Stage,ValidateByChoice
from django.contrib.postgres.fields import JSONField

# Create your models here.


class NewsTypeMaster(models.Model):
    name = models.CharField(max_length=1000, help_text="Name of News Type")
    #Added by Nishank on 15Nov 16 NOT ON LIVE SERVER
    delete = models.BooleanField(default=False)

    # Field added by Ashutosh on 19 July
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = NewsTypeMaster.objects.all()
        flag = 0
        for obj in allobj:
            if obj.id == idd:
                flag = 1
                break
        if flag == 1:
            self.updatedAt = now
        else:
            self.updatedAt = now
            self.createdAt = now
        super(NewsTypeMaster, self).save(*args, **kwargs)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

from django.conf import settings

class NewsFeed(models.Model):
    resource_validate = models.ForeignKey(ValidateByChoice, null=True)

    topic_title = models.CharField(max_length=30000, help_text='Topic Title', blank=True, null=True)
    doctors_category = models.CharField(max_length=30000, help_text='', blank=True, null=True)
    newsfeed_image_file_name = models.CharField(max_length=30000, help_text='', blank=True, null=True)
    related_topics = models.TextField(max_length=30000, help_text='', blank=True, null=True)

    news_type = models.ForeignKey(NewsTypeMaster)
    last_updated_date = models.DateTimeField(auto_now=True)
    activation_status = models.BooleanField(default=True)
    publish_date = models.DateTimeField(null=True,blank=True)
    blocked_news = models.BooleanField(default=False)
    publish_data = models.BooleanField(default=False)
    posted_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    small_description = models.CharField(max_length=30000,blank=True, null=True)

    newsfeed_docx_file = models.FileField(max_length=30000, upload_to=settings.DOCX_PATH_NEWSFEED, null=True)
    newsfeed_html_raw = models.TextField(null=True)
    newsfeed_html_refined = models.TextField(null=True)

    tag_string = models.TextField(max_length=30000, help_text='', blank=True, null=True)

    stage = models.ForeignKey(Stage, null=True)
    current_user = models.ForeignKey(User, null=True)
    previous_user = models.IntegerField(null=True)
    is_disable = models.BooleanField(default=False)
    free_text = models.TextField(max_length=5000, help_text='', blank=True, null=True)
    publish = models.BooleanField(default=False)

    page_title = models.TextField(max_length=250, help_text='', blank=True, null=True)
    page_keywords = models.TextField(max_length=500, help_text='', blank=True, null=True)
    page_description = models.TextField(max_length=800, help_text='', blank=True, null=True)
    # Field added by Ashutosh on 19 July
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = NewsFeed.objects.all()
        flag = 0
        for obj in allobj:
            if obj.id == idd:
                flag = 1
                break
        if flag == 1:
            self.updatedAt = now
        else:
            self.updatedAt = now
            self.createdAt = now
        super(NewsFeed, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.topic_title

# class NewsFeed(models.Model):
#     stage = models.ForeignKey(Stage, null=True)
#     current_user = models.ForeignKey(User, null=True)
#     previous_user = models.IntegerField(null=True)
#     free_text = models.TextField(max_length=5000, help_text='', blank=True, null=True)
#     news_type = models.ForeignKey(NewsTypeMaster)
#     news_header = models.CharField(null=True, blank=True, max_length=200)
#     tag_string = models.CharField(null=True, blank=True, max_length=200)
#     small_desc = models.CharField(null=True, blank=True, max_length=500)
#     image = models.ImageField(upload_to="news_post_image", null=True)
#     image_url = models.CharField(null=True, blank=True, max_length=600)
#     article_body = JSONField(null=True)
#     article_intro = models.TextField(null=True)
#     article_conclusion = models.TextField(null=True)
#     activation_status = models.BooleanField(default=True)
#     need_review = models.BooleanField(default=True)
#     posted_date = models.DateTimeField(auto_now_add=True)
#     last_updated_date = models.DateTimeField(auto_now=True)
#     last_reviewed_on = models.DateTimeField(auto_now=True)
#     blocked_news = models.BooleanField(default=False)
#     publish_data = models.BooleanField(default=False)


#####################################################
# naem :Doctor's news feed for live doctor article  #
# owner : Ashutosh kesharvani                       #
#####################################################
from hfu_cms.models import Live_Doctor
class Doctorsfeed(models.Model):
   resource_validate = models.ForeignKey(ValidateByChoice, null=True)
   doctor = models.ForeignKey(Live_Doctor,null=True)
   topic_title = models.CharField(max_length=30000, help_text='Topic Title', blank=True, null=True)
   newsfeed_image_file_name = models.CharField(max_length=30000, help_text='', blank=True, null=True)
   related_topics = models.TextField(max_length=30000, help_text='', blank=True, null=True)

   news_type = models.ForeignKey(NewsTypeMaster,null=True)
   last_updated_date = models.DateTimeField(auto_now=True,null=True,blank=True)
   activation_status = models.BooleanField(default=True)
   publish_date = models.DateTimeField(null=True, blank=True)
   blocked_news = models.BooleanField(default=False)
   publish_data = models.BooleanField(default=False)
   posted_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

   small_description = models.CharField(max_length=30000, blank=True, null=True)

   # newsfeed_docx_file = models.FileField(max_length=30000, upload_to=settings.DOCX_PATH_NEWSFEED, null=True)
   # newsfeed_html_raw = models.TextField(null=True)
   newsfeed_html_refined = models.TextField(null=True)

   tag_string = models.TextField(max_length=30000, help_text='', blank=True, null=True)

   stage = models.ForeignKey(Stage, null=True)
   current_user = models.ForeignKey(User, null=True)
   previous_user = models.IntegerField(null=True)
   is_disable = models.BooleanField(default=False)
   free_text = models.TextField(max_length=5000, help_text='', blank=True, null=True)
   publish = models.BooleanField(default=False)

   page_title = models.TextField(max_length=250, help_text='', blank=True, null=True)
   page_keywords = models.TextField(max_length=500, help_text='', blank=True, null=True)
   page_description = models.TextField(max_length=800, help_text='', blank=True, null=True)
   # Field added by Ashutosh on 19 July
   createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
   updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

   # Added by Ashutosh on 18 July 2017
   def save(self, *args, **kwargs):
       now = datetime.now()
       idd = self.id
       allobj = Doctorsfeed.objects.all()
       flag = 0
       for obj in allobj:
           if obj.id == idd:
               flag = 1
               break
       if flag == 1:
           self.updatedAt = now
       else:
           self.updatedAt = now
           self.createdAt = now
       super(Doctorsfeed, self).save(*args, **kwargs)

   def __unicode__(self):
       return self.topic_title
