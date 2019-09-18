from django.contrib import admin
from models import NewsFeed, NewsTypeMaster
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from django.contrib.auth.models import User
# Register your models here.
#admin.site.register(NewsFeed)
admin.site.register(NewsTypeMaster)


class OrganisationResource(resources.ModelResource):
    class Meta:
        model = NewsFeed
        fields = ('topic_title', 'doctors_category','newsfeed_image_file_name','related_topics','news_type','activation_status',
                  'publish_date','blocked_news','publish_data','newsfeed_docx_file','newsfeed_html_refined','tag_string',
                  'stage','is_disable','free_text')


class NewsFeedAdmin(ImportExportModelAdmin):
    resource_class = OrganisationResource
    fields = ['topic_title', 'doctors_category','newsfeed_image_file_name','related_topics','news_type','activation_status',
                  'publish_date','blocked_news','publish_data','newsfeed_docx_file','newsfeed_html_refined','tag_string',
                  'stage','is_disable','free_text']

    search_fields = ['topic_title']
    pass

admin.site.register(NewsFeed, NewsFeedAdmin)