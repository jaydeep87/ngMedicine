from django.conf.urls import url, include
from . import views
import hfu_cms.errorlog_functions

""" url description """
""" Search News Data """

search_urlpatterns = [
    url(r'^global/$', views.search_global_news_admin, name='search-publish-global-feed'),
    url(r'^wellness/$', views.search_wellness_news_admin, name='search-publish-wellness-feed'),
    url(r'^health/$', views.search_health_news_admin, name='search-publish-health-feed'),
    url(r'^wellness/by/users/$', views.search_wellness_by_users_admin, name='search-wellness-feed-by-users'),
    url(r'^global/by/users/$', views.search_global_by_users_admin, name='search-global-feed-by-users'),
    url(r'^health/by/users/$', views.search_health_by_users_admin, name='search-health-feed-by-users'),
    url(r'^wellness/by/stages/$', views.search_wellness_by_stages_by_admin, name='search-wellness-feed-by-stages'),
    url(r'^global/by/stages/$', views.search_global_by_stages_by_admin, name='search-global-feed-by-stages'),
    url(r'^health/by/stages/$', views.search_health_by_stages_by_admin, name='search-health-feed-by-stages'),
    url(r'^global/by-name/publisher/$', views.global_by_name_publisher, name='global_by_name_publisher'),
    url(r'^wellness/by-name/publisher/$', views.wellness_by_name_publisher, name='wellness_by_name_publisher'),
    url(r'^health/by-name/publisher/$', views.health_by_name_publisher, name='health_by_name_publisher'),
]
""" End here News Data """


""" Publisher URl Here """
#added New url publish_to_live
publish_urlpatterns = [
    url(r'^get/global/$', views.get_news_data_publisher, {'news_type': 1}, name='get-publish-global-feed'),
    url(r'^get/wellness/$', views.get_news_data_publisher, {'news_type': 2}, name='get-publish-wellness-feed'),
    url(r'^get/health/$', views.get_news_data_publisher, {'news_type': 3}, name='get-publish-health-feed'),
    url(r'^global-publish/$', views.put_data_global_file, name='put-publish-global-feed'),
    url(r'^global-unpublish/$', views.put_data_global_unpublish, name='out-publish-global-feed'),
    url(r'^global-search/$', views.search_news_by_stages_by_publisher, name='search-publish-global-feed'),
    url(r'^global-wellness-health-publish/$', views.publish_news_to_live, name='publish-to-live'),
    url(r'^newsfeed/error_logs/$', hfu_cms.errorlog_functions.newsfeed_error_logs, name='newsfeed_error_logs'),
    url(r'^doctorsfeed/listing/$', views.publisher_doctorsfeed_listing, name='publisher_doctorsfeed_listing'),
    url(r'^doctorsfeed/publish-unpublish/$', views.publish_unpublish_docsfeed, name='publish_unpublish_doctorsfeed'),

]

""" END Publisher URL"""


""" Mark Complete URL """

mark_urlpatterns = [
    url(r'^set/reviewer/global/$', views.set_reviewer_mark, {'news_type': 'global'}, name='set-mark-caller-global'),
    url(r'^set/reviewer/wellness/$', views.set_reviewer_mark, {'news_type': 'wellness'},
        name='set-mark-caller-wellness'),
    url(r'^set/reviewer/health/$', views.set_reviewer_mark, {'news_type': 'health'},
        name='set-mark-caller-health'),
    url(r'^set/caller/global/$', views.set_caller_mark, {'news_type': 'global'}, name='set-mark-reviewer-global'),
    url(r'^set/caller/wellness/$', views.set_caller_mark, {'news_type': 'wellness'}, name='set-mark-reviewer-wellness'),
    url(r'^set/caller/health/$', views.set_caller_mark, {'news_type': 'health'}, name='set-mark-reviewer-health'),
    url(r'^set/publisher/wellness/$', views.set_publisher_mark, {'news_type': 'wellness'},
        name='set-mark-publisher-wellness'),
    url(r'^set/publisher/global/$', views.set_publisher_mark, {'news_type': 'global'},
        name='set-mark-publisher-global'),
    url(r'^set/publisher/health/$', views.set_publisher_mark, {'news_type': 'health'},
        name='set-mark-publisher-health'),

]

""" End Mark Complete URL """

""" Block URL Here """
bock_urlpatterns = [
    url(r'^block-unblock/(?P<news_id>[0-9]+)/$', views.blocking_news, name='block-unblock-feed'),

]
""" End Block URL Here """

""" Assign URL Here """

assign_urlpatterns = [
    url(r'^get/global/$', views.get_assign_data, {'news_type': 1}, name='get-assign-global-feed'),
    url(r'^get/wellness/$', views.get_assign_data, {'news_type': 2}, name='get-assign-wellness-feed'),
    url(r'^get/health/$', views.get_assign_data, {'news_type': 3}, name='get-assign-health-feed'),
    url(r'^set/global/assign/$', views.set_assign_data, {'news_type': 1}, name='set-assign-global-feed'),
    url(r'^set/wellness/assign/$', views.set_assign_data, {'news_type': 2}, name='set-assign-wellness-feed'),
    url(r'^set/health/assign/$', views.set_assign_data, {'news_type': 3}, name='set-assign-health-feed'),

    url(r'^wellness/search_wellness_on_stage_user/$', views.search_wellness_admin_on_stage_user, name='search-wellness-admin-on-stage-user'),
    url(r'^global/search_global_on_stage_user/$', views.search_global_admin_on_stage_user, name='search-global-admin-on-stage-user'),
    url(r'^health/search_health_on_stage_user/$', views.search_health_admin_on_stage_user, name='search-health-admin-on-stage-user'),
]

delete_data_urlpatterns = [
    url(r'^newsfeed/(?P<newsfeed_id>[0-9]+)/(?P<newsfeed_type_id>[0-9]+)/$', views.delete_newsfeed, name='delete_newsfeed'),
]

""" End Assign URL Here"""

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^search-news/', include(search_urlpatterns)),
    url(r'^assign/', include(assign_urlpatterns)),
    url(r'^update/', include(bock_urlpatterns)),
    url(r'^mark/', include(mark_urlpatterns)),
    url(r'^publish/', include(publish_urlpatterns)),
    url(r'^delete/', include(delete_data_urlpatterns)),
    url(r'^home/$', views.news_home, name='news-feed'),
    url(r'^management/global/$', views.news_management, {'type_data': 'global'}, name='global-feed-management'),
    url(r'^management/wellness/$', views.news_management, {'type_data': 'wellness'}, name='wellness-feed-management'),
    url(r'^management/health/$', views.news_management, {'type_data': 'health'}, name='health-feed-management'),
    url(r'^global/listing/$', views.global_listing, name='global-listing'),
    url(r'^wellness/listing/$', views.wellness_listing, name='wellness-listing'),
    url(r'^health/listing/$', views.health_listing, name='health-listing'),
    url(r'^add/global/$', views.adding_news, name='add-global-news'),
    url(r'^edit/global/(?P<news_id>[0-9]+)/$', views.edit_news, name='edit-global-news'),
    url(r'^edit/global/save/(?P<news_id>[0-9]+)/$', views.update_global_news, name='edit-save-global-news'),
    url(r'^add/wellness/$', views.adding_wellness, name='add-wellness-news'),
    url(r'^edit/wellness/(?P<news_id>[0-9]+)/$', views.edit_wellness, name='edit-wellness-news'),
    url(r'^edit/wellness/save/(?P<news_id>[0-9]+)/$', views.update_wellness_news, name='edit-save-wellness-news'),

    url(r'^add/health/$', views.adding_health, name='add-health-news'),
    url(r'^edit/health/(?P<news_id>[0-9]+)/$', views.edit_health, name='edit-health-news'),
    url(r'^edit/health/save/(?P<news_id>[0-9]+)/$', views.update_health_news, name='edit-save-health-news'),

    url(r'^api-get/$', views.get_data, name='api-get'),
    url(r'^wellness-listing/by/users/$', views.wellness_data_by_users, name='wellness-by-users-for-admin'),
    url(r'^global-listing/by/users/$', views.global_data_by_users, name='global-by-users-for-admin'),
    url(r'^health-listing/by/users/$', views.health_data_by_users, name='health-by-users-for-admin'),

    url(r'^wellness-listing/by/stages/$', views.wellness_data_by_stages, name='wellness-by-stages-for-admin'),
    url(r'^global-listing/by/stages/$', views.global_data_by_stages, name='global-by-stages-for-admin'),
    url(r'^health-listing/by/stages/$', views.health_data_by_stages, name='health-by-stages-for-admin'),

    url(r'^manage/newstype_master/$', views.newstype_master_data, name='newstype_master_data_page'),
    url(r'^newstype_master/add/$', views.newstype_master_add_edit, name='newstype_master_add'),
    url(r'^newstype_master/edit/(?P<newstype_master_id>[0-9]+)/$', views.newstype_master_add_edit, name='newstype_master_edit'),
    url(r'^management/doctor/$',views.doctors_feed_listing,name='doctor-feed-management'),
    url(r'^doctorsfeed/$', views.users_doctorsfeed_listing, name='users_doctorsfeed_listing'),
    url(r'^edit/doctors_feed/(?P<feed_id>[0-9]+)/$',views.edit_doctors_feed, name='edit_doctors_feed')
]
