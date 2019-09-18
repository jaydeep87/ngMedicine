from django.conf.urls import url
from remote import views



urlpatterns = [
    url(r'^remote/doctor/list/$', views.doctor_list,name = 'remore-doctor-list' ),
    url(r'^remote/doctor/(?P<pk>[0-9]+)/$', views.doctor_detail,name= 'remote-single-doctor'),
    url(r'^remote/doctor/add/$', views.doctor_add,name='add-a-doctor'),

    url(r'^remote/doctor/education/list/$', views.doctor_education_list,name = 'remote-doctor-education-list'),
    url(r'^remote/doctor/education/(?P<pk>[0-9]+)/$', views.doctor_education_detail,name= 'remote-single-doctor-education'),
    url(r'^remote/doctor/education/add/$', views.doctor_education_add,name= 'add-a-doctor-education'),

    url(r'^remote/reward-recognition/list/$', views.doctor_reward_recognition_list,name = 'remote-reward-recognition-list'),
    url(r'^remote/reward-recognition/(?P<pk>[0-9]+)/$', views.doctor_reward_recognition_detail,name= 'remote-single-reward-recognition'),
    url(r'^remote/reward-recognition/add/$', views.doctor_reward_recognition_add,name= 'add-a-reward-recognition'),

    url(r'^remote/membership/list/$', views.doctor_membership_list,name = 'remote-membership-list'),
    url(r'^remote/membership/(?P<pk>[0-9]+)/$', views.doctor_membership_detail,name= 'remote-single-membership'),
    url(r'^remote/membership/add/$', views.doctor_membership_add,name= 'add-a-membership'),

    url(r'^remote/doctor/experience/list/$', views.doctor_experience_list,name = 'remote-doctor-experience-list'),
    url(r'^remote/doctor/experience/(?P<pk>[0-9]+)/$', views.doctor_experience_detail,name= 'remote-single-doctor-experience'),
    url(r'^remote/doctor/experience/add/$', views.doctor_experience_add,name= 'add-a-doctor-experience'),

    url(r'^remote/get-doctor-organization-attachment-list/$', views.attachwithdoctor_list,name = 'get-doctor-organization-attachment-list'),
    url(r'^remote/get-doctor-organization-attachment-item/(?P<pk>[0-9]+)/$', views.attachwithdoctor_detail,name= 'get-doctor-organization-item'),
    url(r'^remote/attach-organisation-to-doctor/add/$', views.attachwithdoctor_add,name= 'attach-organisation-to-doctor'),

    url(r'^remote/schedule/list/$', views.schedule_list,name = 'remore-schedule-list' ),
    url(r'^remote/schedule/(?P<pk>[0-9]+)/$', views.schedule_detail,name= 'remote-single-schedule'),
    url(r'^remote/schedule/add/$', views.schedule_add,name='add-a-schedule'),

]