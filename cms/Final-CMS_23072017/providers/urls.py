from django.conf.urls import url, include
from . import views

""" url description """

""" Home Service URL"""
home_service_urlpatterns = [
    url(r'^providers/listing/$', views.listing_home_provider, name='home-service-providers'),
    url(r'^add/providers/$', views.add_provider, name='providers-add'),
    url(r'^edit/providers/(?P<providers_id>[0-9]+)/$', views.edit_providers, name='providers-edit'),

]

""" End Home Service URL Here"""

""" Life Service Providers """
life_service_urlpatterns = [
    url(r'^providers/listing/$', views.listing_life_provider, name='life-service-providers'),
    url(r'^add/providers/$', views.add_provider, name='life-service-providers-add'),
]

""" End Life Service URL here """

""" Enterprise Service URL """
enterprise_service_urlpatterns = [
    # url(r'^providers/listing/$', views.listing_enterprise_provider, name='enterprise-service-providers'),
    # url(r'^add/providers/$', views.listing_home_provider, name='enterprise-service-providers-add'),
]
""" End Enterprise Service URL here """


""" Publisher URl Here """
#added New url publish_to_live
#url(r'^home/plan/listing/$', views.get_news_data_publisher, {'news_type': 1}, name='get-publish-global-feed'),
    #rl(r'^life/plan/listing/$', views.get_news_data_publisher, {'news_type': 2}, name='get-publish-wellness-feed'),
    #url(r'^enterprise/plan/listing/$', views.put_data_global_file, name='put-publish-global-feed'),
publisher_urlpatterns = [

   url(r'^home/plan/listing/$', views.homeplan_publisher_listing, name='publisher-homeplan-listing'),
   url(r'^life/plan/listing/$', views.lifeplan_publisher_listing, name='publisher-lifeplan-listing'),
   url(r'^enterprise/plan/listing/$', views.enterpriseplan_publisher_listing, name='publisher-enterpriseplan-listing'),
   url(r'^service/plan/listing/$', views.serviceplan_publisher_listing, name='publisher-serviceplan-listing'),
]

plan_master_urlpatterns = [
    url(r'^service-plan/masters/$', views.service_plans_masters, name='service_plans_masters'),
    url(r'^service-plan/masters/category/$', views.category_listing, name='category_listing'),
    url(r'^service-plan/masters/category/add/$', views.add_edit_plan_category, name='add_plan_category'),
    url(r'^service-plan/masters/category/edit/(?P<cat_id>[0-9]+)/$', views.add_edit_plan_category, name='edit_plan_category'),
    url(r'^service-plan/masters/sub-category/$', views.sub_category_listing, name='sub_category_listing'),
    url(r'^service-plan/masters/sub-category/add/$', views.add_edit_plan_sub_category, name='add_plan_sub_category'),
    url(r'^service-plan/masters/sub-category/edit/(?P<subcat_id>[0-9]+)/$', views.add_edit_plan_sub_category, name='edit_plan_sub_category'),
    url(r'^service-plan/masters/details/$', views.plan_details_listing, name='plan_details_listing'),
    url(r'^service-plan/masters/details/add/$', views.add_edit_plan_details, name='add_plan_details'),
    url(r'^service-plan/masters/details/edit/(?P<detail_id>[0-9]+)/$', views.add_edit_plan_details, name='edit_plan_details'),
    url(r'^service-plan/masters/component/$', views.component_listing, name='component_listing'),
    url(r'^service-plan/masters/component/add/$', views.add_edit_plan_component, name='add_plan_component'),
    url(r'^service-plan/masters/component/edit/(?P<component_id>[0-9]+)/$', views.add_edit_plan_component, name='edit_plan_component'),
    url(r'^service-plan/masters/sub-component/$', views.sub_component_listing, name='sub_component_listing'),
    url(r'^service-plan/masters/sub-component/add/$', views.add_edit_plan_sub_component, name='add_plan_sub_component'),
    url(r'^service-plan/masters/sub-component/edit/(?P<subcomponent_id>[0-9]+)/$', views.add_edit_plan_sub_component, name='edit_plan_sub_component'),
]
plan_new_urlpatterns = [
    url(r'^service-plan/listing/$', views.service_plans_listing, name='plan-name-listing'),
    url(r'^service-plan/listing-admin/$', views.service_plans_listing_admin, name='plan-name-listing-admin'),
    url(r'service-plan/add/$', views.service_plan_add, name='plannew-add'),
    url(r'cat-subcat/$', views.cat_subcat, name='cat_subcat'),
    url(r'detail-component/$', views.detail_component, name='detail_component'),
    url(r'component-subcomponent/$', views.component_subcomponent, name='component_subcomponent'),
    # url(r'count-amount/$', views.count_amount, name='count_amount'),
    url(r'service-plan/edit/(?P<plannew_id>[0-9]+)/$', views.service_plan_edit, name='plannew-edit'),
    url(r'service-plan/test/delete/(?P<plannew_id>[0-9]+)/$', views.delete_test, name='delete-test'),
    url(r'^search/serviceplan/by/publisher-stage/$', views.search_service_plan_by_publisher_stage, name='search_service_plan_by_publisher'),
    url(r'^search/serviceplan/by/admin/$', views.search_service_plan_by_admin, name='search_service_plan_by_admin'),
    url(r'^search/serviceplan/by/user/$', views.search_service_plan_by_user, name='search_service_plan_by_admin'),
    url(r'^search/serviceplan/by/publisher/$', views.search_service_plan_by_publisher, name='search_service_plan_by_publisher'),
    url(r'^assign/serviceplan/$', views.assign_serviceplan, name='assign-serviceplan'),
]

mark_as_urlpatterns = [
    url(r'^complete/service-plan/caller/$', views.mark_as_complete_caller_service_plan, name='mark-caller-complete-service-plan'),
    url(r'^reverse/service-plan/caller/$', views.mark_as_reverse_caller_service_plan , name='mark-reverse-service-plan-to-caller'),
    url(r'^complete/service-plan/reviewer/$', views.mark_as_complete_reviewer_service_plan, name='mark-reviewer-complete-service-plan'),
    url(r'^reverse/service-plan/reviewer/$', views.mark_as_reverse_reviewer_service_plan , name='mark-reverse-service-plan-to-reviewer')
]

service_plan_urlpatterns = [
    url(r'^home/plan/listing/$', views.listing_home_service_plan, name='home-service-plan-listing'),
    url(r'^life/plan/listing/$', views.listing_life_service_plan, name='life-service-plan-listing'),
    url(r'^enterprise/plan/listing/$', views.listing_enterprise_service_plan, name='enterprise-service-plan-listing'),

    url(r'^plan/dashboard/$', views.service_plan_home, name='service_plan_home'),

    url(r'^add/home/plan/$', views.add_home_service_plan, {'plan_type': 'home'}, name='home-service-plan-add'),
    url(r'^add/life/plan/$', views.add_life_service_plan, {'plan_type': 'life'}, name='life-service-plan-add'),
    url(r'^add/enterprise/plan/$', views.add_enterprise_service_plan, {'plan_type': 'enterprise'},
        name='enterprise-service-plan-add'),

    url(r'^edit/home/plan/(?P<plan_id>[0-9]+)/$', views.edit_home_service_plan, {'plan_type': 'home'},
        name='home-service-plan-edit'),
    url(r'^edit/life/plan/(?P<plan_id>[0-9]+)/$', views.edit_life_service_plan, {'plan_type': 'life'},
        name='life-service-plan-edit'),
    url(r'^edit/enterprise/plan/(?P<plan_id>[0-9]+)/$', views.edit_enterprise_service_plan, {'plan_type': 'enterprise'},
        name='enterprise-service-plan-edit'),


    url(r'^assignment/home/plan/$', views.home_plan_assignment, name='home-plan-assignment'),
    url(r'^management/home/plan/$', views.home_plan_data_manage, name='home-plan-management'),
    url(r'^by/users/home/plan/$', views.home_plan_data_by_users, name='home-plan-by-users'),
    url(r'^search_home_plan_on_stage_user/$', views.search_home_plan_admin_on_stage_user,
        name='search_home_plan_admin_on_stage_user'),
    url(r'^by/stages/home/plan/$', views.home_plan_data_by_stages, name='home-plan-by-stages'),
    url(r'^homeplan/by/stages/$', views.search_home_plan_by_stages_by_admin, name='search_home_plan_by_stages_by_admin'),

    url(r'^assign/homeplan/$', views.assign_homeplan, name='assign-symptoms'),
    url(r'^homeplan/assign/admin/$', views.search_home_plan_assign_admin ,name='home-plan-search-assign-admin'),



    url(r'^assignment/life/plan/$', views.life_plan_assignment, name='life-plan-assignment'),
    url(r'^management/life/plan/$', views.life_plan_data_manage, name='life-plan-management'),
    url(r'^by/users/life/plan/$', views.life_plan_data_by_users, name='life-plan-by-users'),
    url(r'^search_life_plan_on_stage_user/$', views.search_life_plan_admin_on_stage_user,
        name='search_life_plan_admin_on_stage_user'),

    url(r'^by/stages/life/plan/$', views.life_plan_data_by_stages, name='life-plan-by-stages'),
    url(r'^lifeplan/by/stages/$', views.search_life_plan_by_stages_by_admin, name='search_life_plan_by_stages_by_admin'),

    url(r'^assign/lifeplan/$', views.assign_lifeplan, name='assign-symptoms'),
    url(r'^lifeplan/assign/admin/$', views.search_life_plan_assign_admin ,name='life-plan-search-assign-admin'),



    url(r'^assignment/enterprise/plan/$', views.enterprise_plan_assignment, name='enterprise-plan-assignment'),
    url(r'^management/enterprise/plan/$', views.enterprise_plan_data_manage, name='enterprise-plan-management'),
    url(r'^by/users/enterprise/plan/$', views.enterprise_plan_data_by_users, name='enterprise-plan-by-users'),
    url(r'^search_enterprise_plan_on_stage_user/$', views.search_enterprise_plan_admin_on_stage_user,
        name='search_enterprise_plan_admin_on_stage_user'),

    url(r'^by/stages/enterprise/plan/$', views.enterprise_plan_data_by_stages, name='enterprise-plan-by-stages'),
    url(r'^enterpriseplan/by/stages/$', views.search_enterprise_plan_by_stages_by_admin, name='search_enterprise_plan_by_stages_by_admin'),

    url(r'^assign/enterpriseplan/$', views.assign_enterpriseplan, name='assign-symptoms'),
    url(r'^enterpriseplan/assign/admin/$', views.search_enterprise_plan_assign_admin ,name='enterprise-plan-search-assign-admin'),

    url(r'^search/homeplan/by/users/$', views.search_home_plan_by_users, name='search_home_plan_by_users'),
    url(r'^search/lifeplan/by/users/$', views.search_life_plan_by_users, name='search_life_plan_by_users'),
    url(r'^search/enterpriseplan/by/users/$', views.search_enterprise_plan_by_users, name='search_enterprise_plan_by_users'),

    url(r'^search/homeplan/by/publisher/$', views.search_home_plan_by_publisher, name='search_home_plan_by_publisher'),
    url(r'^search/lifeplan/by/publisher/$', views.search_life_plan_by_publisher, name='search_life_plan_by_publisher'),
    url(r'^search/enterpriseplan/by/publisher/$', views.search_enterprise_plan_by_publisher, name='search_enterprise_plan_by_publisher'),


]

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^home-service/', include(home_service_urlpatterns)),
    url(r'^life-service/', include(life_service_urlpatterns)),
    url(r'^', include(service_plan_urlpatterns)),
    url(r'^enterprise-service/', include(enterprise_service_urlpatterns)),
    url(r'^home/$', views.add_plan_home, name='service-paln_home'),
    url(r'^plan/$', views.service_provider_home, name='service_provider_home'),
    url(r'^plan-masters/', include(plan_master_urlpatterns)),
    url(r'^plan-new/', include(plan_new_urlpatterns)),
    url(r'^publisher/', include(publisher_urlpatterns)),
    url(r'^mark-complete/', include(mark_as_urlpatterns)),
]
