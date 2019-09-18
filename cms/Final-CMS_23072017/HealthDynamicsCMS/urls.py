"""HealthDynamicsCMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from hfu_cms import views, data_publisher
from django.conf.urls.static import static
from django.conf import settings
import hfu_cms.search_data
import hfu_cms.excel
import hfu_cms.special_functions
from hfu_cms.models import Doctor
import hfu_cms.errorlog_functions
from hfu_cms import elasticsearch_client,views_two
from rest_framework import routers, serializers, viewsets

"""# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # current_user, previous_user,free_text, is_disable, id, resource_validate,stage,unique_id
        fields = ('name','image_url','category','zone','zone_location','speciality','service_offered','dob','mobile_no','phone',
                  'skype_id','email','secondary_email','doctor_experience_year','qualification_data','registration_data','male_doctor',
                  'female_doctor')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'doctors', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

"""










enable_disable_urlpatterns = [
    url(r'^deactivate/(?P<doctor_id>[0-9]+)/$', views.disable_doctor_data, name='doctor-data-deactivate'),
    url(r'^enable/(?P<doctor_id>[0-9]+)/$', views.enable_doctor_data, name='doctor-data-enable'),
    url(r'^de/(?P<organisation_id>[0-9]+)/$', views.disable_organisation_data, name='organisation-data-deactivate'),
    url(r'^ena/(?P<organisation_id>[0-9]+)/$', views.enable_organisation_data, name='organisation-data-enable'),
    url(r'^master-general-deactivate/(?P<object_id>[0-9]+)/(?P<object_type>[0-9]+)/$', views.deactivate_any_master_type, name='any-master-object-deactivate'),
    url(r'^master-general-activate/(?P<object_id>[0-9]+)/(?P<object_type>[0-9]+)/$', views.activate_any_master_type, name='any-master-object-activate'),
    url(r'^deactivate/unpublish/(?P<doctor_id>[0-9]+)/$', views.disable_unpublish_doctor_data, name='doctor-data-deactivate-unpublish'),
    url(r'^enable/no-publish/(?P<doctor_id>[0-9]+)/$', views.enable_nopublish_doctor_data, name='doctor-data-enable-nopublish'),

    url(r'^deactivate/live_org/(?P<organisation_id>[0-9]+)/$', views_two.disable_live_organisation_data, name='deactivate_live_organisation'),
    url(r'^activate/live_org(?P<organisation_id>[0-9]+)/$', views_two.activate_live_organisation, name='activate-live-organisation'),
]

edit_doctor_data_urlpatterns = [
    url(r'^reward/$', views.edit_reward, name='edit-reward-data'),
    url(r'^member/$', views.edit_member, name='edit-member-data'),
    url(r'^education/$', views.edit_education, name='edit-education-data'),
    url(r'^experience/$', views.edit_experience, name='edit-exp-data'),
    url(r'^attach/$', views.edit_attach_data, name='edit-attach-data'),

]

delete_data_urlpatterns = [
    url(r'^reward/(?P<reward_id>[0-9]+)/$', views.delete_reward, name='delete-reward'),
    url(r'^membership/(?P<member_id>[0-9]+)/$', views.delete_membership, name='delete-member'),
    url(r'^education/(?P<education_id>[0-9]+)/$', views.delete_education, name='delete-education'),
    url(r'^experience/(?P<experience_id>[0-9]+)/$', views.delete_experience, name='delete-experience'),
    url(r'^schedule/(?P<doctor_id>[0-9]+)/(?P<organisation_id>[0-9]+)/$', views.delete_schedule, name='delete-schedule'),
    url(r'^schedule/dietitian/(?P<dietitian_id>[0-9]+)/(?P<organisation_id>[0-9]+)/$', views.delete_dietitian_schedule, name='delete-dietitian-schedule'),
    url(r'^schedule/therapist/(?P<therapist_id>[0-9]+)/(?P<organisation_id>[0-9]+)/$', views.delete_therapist_schedule, name='delete-therapist-schedule'),
    url(r'^schedule/lab/delete/$', views.delete_lab_schedule, name='delete-lab-schedule'),
    url(r'^schedule/bloodbank/delete/$', views.delete_bloodbank_schedule, name='delete-bloodbank-schedule'),
    url(r'^schedule/lab/branch/delete/$', views.delete_lab_branch_schedule, name='delete-lab-branch-schedule'),
    url(r'^delete_schedule_organisation/(?P<organisation_id>[0-9]+)/$', views.delete_schedule_organisation, name='delete_schedule_organisation'),
    url(r'^delete_consultancy_schedule/(?P<doctor_id>[0-9]+)/$', views.delete_consultancy_schedule, name='delete_consultancy_schedule'),
    url(r'^organisation/(?P<organisation_id>[0-9]+)/(?P<attach_id>[0-9]+)/$', views.delete_organisation, name='delete-organisation'),
    url(r'^organisation/association_doctor/(?P<organisation_id>[0-9]+)/(?P<id>[0-9]+)/$', views.association_doctor_delete, name='association_doctor_delete'),
    url(r'^schedule/rehab/delete/$', views.delete_rehab_schedule, name='delete-rehab-schedule'),
    url(r'^schedule/nurse_bureau/delete/$', views.delete_nurse_bureau_schedule, name='delete-nurse_bureau-schedule'),
    url(r'^schedule/pharmacy/delete/$', views.delete_pharmacy_schedule, name='delete-pharmacy-schedule'),
    url(r'^disease/(?P<disease_id>[0-9]+)/$', views.delete_disease, name='delete_disease'),
    url(r'^symptoms/(?P<symptoms_id>[0-9]+)/$', views.delete_symptoms, name='delete_symptoms'),
    url(r'^schedule/doctor-care/delete/$', views.delete_doctor_care_schedule, name='delete-doctor-care-schedule'),
]


search_urlpatterns = [
    url(r'^doctor/$', hfu_cms.search_data.search_doctor_caller, name='doctor-search'),
    url(r'^care/doctor/$', hfu_cms.search_data.search_care_doctor, name='care-doctor-search'),
    url(r'^doctor/for-publisher/$', hfu_cms.search_data.search_doctor_for_publisher, name='search-doctor-for-publisher'),
    url(r'^live-doctor/for-publisher/$', hfu_cms.search_data.search_live_doctor_for_publisher, name='search-live-doctor-for-publisher'),
    url(r'^organisation/for-publisher/$', hfu_cms.search_data.search_organisation_for_publisher, name='search-organisation-for-publisher'),
    url(r'^pharmacy/for-publisher/$', hfu_cms.search_data.search_pharmacy_for_publisher, name='search-pharmacy-for-publisher'),
    url(r'^lab/for-publisher/$', hfu_cms.search_data.search_lab_for_publisher, name='search-lab-for-publisher'),
    url(r'^bloodbank/for-publisher/$', hfu_cms.search_data.search_bloodbank_for_publisher, name='search-bloodbank-for-publisher'),
    url(r'^therapist/for-publisher/$', hfu_cms.search_data.search_therapist_for_publisher, name='search-therapist-for-publisher'),
    url(r'^ambulance/for-publisher/$', hfu_cms.search_data.search_ambulance_for_publisher, name='search-ambulance-for-publisher'),
    url(r'^rehab/for-publisher/$', hfu_cms.search_data.search_rehab_for_publisher, name='search-rehab-for-publisher'),
    url(r'^nurse_bureau/for-publisher/$', hfu_cms.search_data.search_nurse_bureau_for_publisher, name='search-nurse_bureau-for-publisher'),
    url(r'^doctor/assign/admin/$', hfu_cms.search_data.search_doctor_assign_admin, name='doctor-search-assign-admin'),
    url(r'^live-doctor/assign/admin/$', hfu_cms.search_data.search_live_doctor_assign_admin, name='live-doctor-search-assign-admin'),
    url(r'^live-doctor/deleted-schedules-with-sponsored-ranks/$', hfu_cms.search_data.deleted_schedules_with_sponsored_ranks, name='deleted_schedules_with_sponsored_ranks'),
    url(r'^doctor/deleted-schedules-with-sponsored-ranks/$', hfu_cms.search_data.doctor_deleted_schedules_with_sponsored_ranks, name='doctor_deleted_schedules_with_sponsored_ranks'),
    url(r'^doctor/assign/search_doctor_on_stage_user/$', hfu_cms.search_data.search_doctor_admin_on_stage_user, name='search_doctor_admin_on_stage_user'),
    url(r'^live_doctor/by-name/on-by-stage-page/$', hfu_cms.search_data.search_live_doctor_by_name_on_by_stage_page, name='search_live_doctor_by_name_on_by_stage_page'),
    url(r'^organisation/assign/admin/$', hfu_cms.search_data.search_organisation_assign_admin, name='organisation-search-assign-admin'),
    url(r'^organisation/$', hfu_cms.search_data.search_organisation_caller, name='organisation-search'),
    url(r'^doctor/admin/$', hfu_cms.search_data.search_doctor_admin, name='doctor-admin-search'),


    url(r'^whole_live_organisation/$', hfu_cms.search_data.search_whole_live_organisation, name='search-whole-live-organisation'),
    url(r'^live_organsiation/by/user/$', hfu_cms.search_data.filter_live_organisation_by_users, name='filter_live_organisation_by_users'),
    url(r'^live_organisation/for-publisher/$', hfu_cms.search_data.search_live_organisation_for_publisher, name='search-live-organisation-for-publisher'),
    # url(r'^whole_live_organisation/$', hfu_cms.search_data.search_whole_live_organisation, name='search-whole-live-organisation'),
    # url(r'^live_organsiation/byuser/$', hfu_cms.search_data.filter_live_organisation_by_users, name='filter_live_organisation_by_users'),
    # url(r'^whole_live_organisation/$', hfu_cms.search_data.search_whole_live_organisation, name='search-whole-live-organisation'),
    # url(r'^live_organsation/byuser/$', hfu_cms.search_data.filter_live_organisation_by_users, name='filter_live_organisation_by_users'),
    url(r'^live_organisation/by/stages/$', hfu_cms.search_data.filter_live_organisation_by_stages, name='filter-live-organisation-by-stage'),
    url(r'^live_organisation/by/publisher/$', hfu_cms.search_data.search_live_organisation_by_publisher, name='live-organisation-search-publisher'),
    url(r'^live_organisation/$', hfu_cms.search_data.search_live_organisation_caller, name='live_organisation-search'),
    url(r'^live_organisation/admin/$', hfu_cms.search_data.search_live_organisation_by_stage_admin, name='organisation-admin-search'),

    url(r'^doctor/by/users/$', hfu_cms.search_data.search_doctor_by_users_by_admin, name='doctor-users-search-admin'),
    url(r'^live-doctor/by/users/$', hfu_cms.search_data.search_live_doctor_by_users_by_admin, name='live_doctor-users-search-admin'),
    url(r'^organisation/admin/$', hfu_cms.search_data.search_organisation_admin, name='organisation-admin-search'),
    url(r'^organisation/by/stages/$', hfu_cms.search_data.search_organisation_by_stages_by_admin, name='organisation-by-stage-search'),
    url(r'^organisation/by/users/$', hfu_cms.search_data.search_organisation_by_users_by_admin, name='organisation-by-users-search'),
    url(r'^doctor/by/stages/$', hfu_cms.search_data.search_doctor_by_stages_by_admin, name='doctor-by-stages-search'),
    url(r'^live-doctor/by/stages/$', hfu_cms.search_data.search_live_doctor_by_stages_by_admin, name='live_doctor-by-stages-search'),
    url(r'^doctor/by/publisher/$', hfu_cms.search_data.search_doctor_by_stages_by_publisher, name='doctor-by-stages-search-publisher'),
    url(r'^organisation/by/publisher/$', hfu_cms.search_data.search_organisation_by_stages_by_publisher, name='organisation-by-stages-search-publisher'),
    url(r'^organisation/association/user/$', hfu_cms.search_data.search_doctor_association_by_user, name='search_doctor_association_by_user'),
    url(r'^lab/$', hfu_cms.search_data.search_lab_caller, name='lab-search'),
    url(r'^lab/assign/admin/$', hfu_cms.search_data.search_lab_assign_admin, name='lab-search-assign-admin'),
    url(r'^lab/assign/search_lab_on_stage_user/$', hfu_cms.search_data.search_lab_admin_on_stage_user, name='search_lab_admin_on_stage_user'),
    url(r'^lab/by/users/$', hfu_cms.search_data.search_lab_by_users_by_admin, name='search_lab_by_users_by_admin'),
    url(r'^lab/by/stages/$', hfu_cms.search_data.search_lab_by_stages_by_admin, name='search_lab_by_stages_by_admin'),
    url(r'^lab/by/publisher/$', hfu_cms.search_data.search_lab_by_stages_by_publisher, name='lab-by-stages-search-publisher'),

    url(r'^question/by/type/admin/', hfu_cms.search_data.search_question_by_type_admin, name='search_question_by_type_admin'),
    url(r'^feedback/by/status/admin/', hfu_cms.search_data.feedback_by_status_admin, name='feedback_by_status_admin'),

    url(r'^rehab/$', hfu_cms.search_data.search_rehab_caller, name='rehab-search'),
    url(r'^rehab/by/publisher/$', hfu_cms.search_data.search_rehab_by_stages_by_publisher, name='rehab-by-stages-search-publisher'),
    url(r'^rehab/by/users/$', hfu_cms.search_data.search_rehab_by_users_by_admin, name='search_rehab_by_users_by_admin'),
    url(r'^rehab/assign/search_rehab_on_stage_user/$', hfu_cms.search_data.search_rehab_admin_on_stage_user, name='search_rehab_admin_on_stage_user'),
    url(r'^rehab/by/stages/$', hfu_cms.search_data.search_rehab_by_stages_by_admin, name='search_rehab_by_stages_by_admin'),
    url(r'^rehab/assign/admin/$', hfu_cms.search_data.search_rehab_assign_admin, name='rehab-search-assign-admin'),

    url(r'^nurse_bureau/$', hfu_cms.search_data.search_nurse_bureau_caller, name='nurse_bureau-search'),
    url(r'^nurse_bureau/by/publisher/$', hfu_cms.search_data.search_nurse_bureau_by_stages_by_publisher, name='nurse_bureau-by-stages-search-publisher'),
    url(r'^nurse_bureau/by/users/$', hfu_cms.search_data.search_nurse_bureau_by_users_by_admin, name='search_nurse_bureau_by_users_by_admin'),
    url(r'^nurse_bureau/assign/search_nurse_bureau_on_stage_user/$', hfu_cms.search_data.search_nurse_bureau_admin_on_stage_user, name='search_nurse_bureau_admin_on_stage_user'),
    url(r'^nurse_bureau/by/stages/$', hfu_cms.search_data.search_nurse_bureau_by_stages_by_admin, name='search_nurse_bureau_by_stages_by_admin'),
    url(r'^nurse_bureau/assign/admin/$', hfu_cms.search_data.search_nurse_bureau_assign_admin, name='nurse_bureau-search-assign-admin'),

    url(r'^dietitian/$', hfu_cms.search_data.search_dietitian_caller, name='dietitian-search'),
    url(r'^dietitian/by/publisher/$', hfu_cms.search_data.search_dietitian_by_stages_by_publisher, name='dietitian-by-stages-search-publisher'),
    url(r'^dietitian/by/users/$', hfu_cms.search_data.search_dietitian_by_users_by_admin, name='search_dietitian_by_users_by_admin'),
    url(r'^dietitian/assign/search_dietitian_on_stage_user/$', hfu_cms.search_data.search_dietitian_admin_on_stage_user, name='search_dietitian_admin_on_stage_user'),
    url(r'^dietitian/by/stages/$', hfu_cms.search_data.search_dietitian_by_stages_by_admin, name='search_dietitian_by_stages_by_admin'),
    url(r'^dietitian/assign/admin/$', hfu_cms.search_data.search_dietitian_assign_admin, name='dietitian-search-assign-admin'),


    url(r'^therapist/$', hfu_cms.search_data.search_therapist_caller, name='therapist-search'),
    url(r'^therapist/by/publisher/$', hfu_cms.search_data.search_therapist_by_stages_by_publisher, name='therapist-by-stages-search-publisher'),
    url(r'^therapist/by/users/$', hfu_cms.search_data.search_therapist_by_users_by_admin, name='search_therapist_by_users_by_admin'),
    url(r'^therapist/assign/search_therapist_on_stage_user/$', hfu_cms.search_data.search_therapist_admin_on_stage_user, name='search_therapist_admin_on_stage_user'),
    url(r'^therapist/by/stages/$', hfu_cms.search_data.search_therapist_by_stages_by_admin, name='search_therapist_by_stages_by_admin'),
    url(r'^therapist/assign/admin/$', hfu_cms.search_data.search_therapist_assign_admin, name='therapist-search-assign-admin'),


    url(r'^blood-bank/$', hfu_cms.search_data.search_bloodbank_caller, name='bloodbank-search'),
    url(r'^blood-bank/assign/search_bloodbank_on_stage_user/$', hfu_cms.search_data.search_bloodbank_admin_on_stage_user, name='search_bloodbank_admin_on_stage_user'),
    url(r'^blood-bank/assign/admin/$', hfu_cms.search_data.search_bloodbank_assign_admin, name='bloodbank-search-assign-admin'),
    url(r'^blood-bank/by/stages/$', hfu_cms.search_data.search_bloodbank_by_stages_by_admin, name='search_bloodbank_by_stages_by_admin'),
    url(r'^blood_bank/by/publisher/$', hfu_cms.search_data.search_blood_bank_by_stages_by_publisher, name='blood_bank-by-stages-search-publisher'),

    url(r'^bloodbank/by/users/$', hfu_cms.search_data.search_bloodbank_by_users_by_admin, name='search_bloodbank_by_users_by_admin'),
    url(r'^ambulance/$', hfu_cms.search_data.search_ambulance_caller, name='ambulance-search'),
    url(r'^ambulance/assign/search_ambulance_on_stage_user/$', hfu_cms.search_data.search_ambulance_admin_on_stage_user, name='search_ambulance_admin_on_stage_user'),
    url(r'^ambulance/assign/admin/$', hfu_cms.search_data.search_ambulance_assign_admin, name='ambulance-search-assign-admin'),
    url(r'^ambulance/by/publisher/$', hfu_cms.search_data.search_ambulance_by_stages_by_publisher, name='ambulance-by-stages-search-publisher'),


    url(r'^ambulance/by/stages/$', hfu_cms.search_data.search_ambulance_by_stages_by_admin, name='search_ambulance_by_stages_by_admin'),
    url(r'^pharmacy/by/users/$', hfu_cms.search_data.search_pharmacy_by_users_by_admin, name='search_pharmacy_by_users_by_admin'),
    url(r'^ambulance/by/users/$', hfu_cms.search_data.search_ambulance_by_users_by_admin, name='search_ambulance_by_users_by_admin'),
    url(r'^pharmacy/assign/search_pharmacy_on_stage_user/$', hfu_cms.search_data.search_pharmacy_admin_on_stage_user, name='search_pharmacy_admin_on_stage_user'),
    url(r'^pharmacy/by/stages/$', hfu_cms.search_data.search_pharmacy_by_stages_by_admin, name='search_pharmacy_by_stages_by_admin'),
    url(r'^pharmacy/assign/admin/$', hfu_cms.search_data.search_pharmacy_assign_admin, name='pharmacy-search-assign-admin'),
    url(r'^pharmacy/$', hfu_cms.search_data.search_pharmacy_caller, name='pharmacy-search'),
    url(r'^pharmacy/by/publisher/$', hfu_cms.search_data.search_pharmacy_by_stages_by_publisher, name='pharmacy-by-stages-search-publisher'),


    url(r'^disease/by/users/$', hfu_cms.search_data.search_disease_by_users_by_admin,name='search_disease_by_users_by_admin'),
    url(r'^disease/assign/search_disease_on_stage_user/$', hfu_cms.search_data.search_disease_admin_on_stage_user, name='search_disease_admin_on_stage_user'),
    url(r'^disease/by/stages/$', hfu_cms.search_data.search_disease_by_stages_by_admin, name='search_disease_by_stages_by_admin'),
    url(r'^disease/assign/admin/$', hfu_cms.search_data.search_disease_assign_admin ,name='disease-search-assign-admin'),
    url(r'^disease/$', hfu_cms.search_data.search_disease_caller, name='disease-search'),
    url(r'^disease/by/publisher/$', hfu_cms.search_data.search_disease_by_stages_by_publisher, name='disease-by-stages-search-publisher'),


    url(r'^symptoms/by/users/$', hfu_cms.search_data.search_symptoms_by_users_by_admin,name='search_symptoms_by_users_by_admin'),
    url(r'^symptoms/assign/search_symptoms_on_stage_user/$', hfu_cms.search_data.search_symptoms_admin_on_stage_user, name='search_symptoms_admin_on_stage_user'),
    url(r'^symptoms/by/stages/$', hfu_cms.search_data.search_symptoms_by_stages_by_admin, name='search_symptoms_by_stages_by_admin'),
    url(r'^symptoms/assign/admin/$', hfu_cms.search_data.search_symptoms_assign_admin ,name='symptoms-search-assign-admin'),
    url(r'^symptoms/$', hfu_cms.search_data.search_symptoms_caller, name='symptoms-search'),
    url(r'^symptoms/by/publisher/$', hfu_cms.search_data.search_symptoms_by_stages_by_publisher, name='symptoms-by-stages-search-publisher'),


    url(r'^drug/by/users/$', hfu_cms.search_data.search_drug_by_users_by_admin, name='search_drug_by_users_by_admin'),
    url(r'^drug/assign/search_drug_on_stage_user/$', hfu_cms.search_data.search_drug_admin_on_stage_user, name='search_drug_admin_on_stage_user'),
    url(r'^drug/by/stages/$', hfu_cms.search_data.search_drug_by_stages_by_admin, name='search_drug_by_stages_by_admin'),
    url(r'^drug/assign/admin/$', hfu_cms.search_data.search_drug_assign_admin, name='drug-search-assign-admin'),
    url(r'^drug/$', hfu_cms.search_data.search_drug_caller, name='drug-search'),
    url(r'^drug/by/publisher/$', hfu_cms.search_data.search_drug_by_stages_by_publisher, name='drug-by-stages-search-publisher'),


    url(r'^global/$', hfu_cms.search_data.search_global_caller, name='global-feed-search'),
    url(r'^health/$', hfu_cms.search_data.search_health_caller, name='health-feed-search'),
    url(r'^wellness/$', hfu_cms.search_data.search_wellness_caller, name='wellness-feed-search'),
    url(r'^home-plan/$', hfu_cms.search_data.search_home_plan_caller, name='home-plan-search'),
    url(r'^life-plan/$', hfu_cms.search_data.search_life_plan_caller, name='life-plan-search'),
    url(r'^enterprise-plan/$', hfu_cms.search_data.search_enterprise_plan_caller, name='enterprise-plan-search'),

    url(r'^service-offered/by/category/$', hfu_cms.search_data.search_serviceoffered_by_category_admin, name='serviceoffered-by-category-search'),
    url(r'^speciality/by/category/$', hfu_cms.search_data.search_speciality_by_category_admin, name='speciality-by-category-search'),
    url(r'^userbyname/admin/$', hfu_cms.search_data.search_user_by_name_admin, name='user-by-name-search'),
    url(r'^localitybyname/admin/$', hfu_cms.search_data.search_locality_by_name_admin, name='locality-by-name-search'),
    url(r'^DoctorNewSOByName/admin/$', hfu_cms.search_data.search_DoctorNewSO_by_name_admin, name='DoctorNewSO-by-name-search'),
    url(r'^DoctorNewSOLooserByName/admin/$', hfu_cms.search_data.search_DoctorNewSOLooser_by_name_admin, name='DoctorNewSOLooser-by-name-search'),
    url(r'^DoctorNewSPEByName/admin/$', hfu_cms.search_data.search_DoctorNewSPE_by_name_admin, name='DoctorNewSPE-by-name-search'),
    url(r'^zonelocationbyname/admin/$', hfu_cms.search_data.search_zonelocation_by_name_admin, name='zonelocation-by-name-search'),
    url(r'^ambulance-service-by-name-admin/admin/$', hfu_cms.search_data.search_ambulance_service_by_name_admin, name='ambulance-service-by-name-search'),
    url(r'^ambulance-type-by-name-admin/admin/$', hfu_cms.search_data.search_ambulance_type_by_name_admin, name='ambulance-type-by-name-search'),

    url(r'^global_search_for_all_users/$', hfu_cms.search_data.global_search_for_all_users, name='global_search_for_all_users'),

    url(r'^disease/by-name/publisher/$', hfu_cms.search_data.search_disease_by_name_publisher, name='search_disease_by_name_publisher'),
    url(r'^symptom/by-name/publisher/$', hfu_cms.search_data.search_symptom_by_name_publisher, name='search_symptom_by_name_publisher'),
    url(r'^service_offered/search_service_offered/$',hfu_cms.search_data.search_service_offered,name='search_service_offered'),
    url(r'^localitymaster/admin/$', hfu_cms.search_data.search_locality_master, name='localitymaster_admin'),
    url(r'^citymaster/admin/$', hfu_cms.search_data.search_city_master, name='citymaster_admin'),
    url(r'^statemaster/admin/$', hfu_cms.search_data.search_state_master, name='statemaster_admin'),
    url(r'^categorymaster/by-name/$', hfu_cms.search_data.search_categorymaster_byname, name='search_categorymaster_byname'),
    url(r'^speciality/by-name/$', hfu_cms.search_data.search_specialitymaster_byname, name='search_specialitymaster_byname'),
    url(r'^facility/by-name/$', hfu_cms.search_data.search_facility_byname, name='search_facility_byname'),
    url(r'^disease/by-name/$', hfu_cms.search_data.search_disease_byname, name='search_disease_byname'),
    url(r'^diseasemaster/by-name/$', hfu_cms.search_data.search_diseasemaster_byname, name='search_diseasemaster_byname'),
    url(r'^labtest/by-name/$', hfu_cms.search_data.search_labtest_byname, name='search_labtest_byname'),
    url(r'^symptommaster/by-name/$', hfu_cms.search_data.search_symptommaster_byname, name='search_symptommaster_byname'),


    url(r'^localitybycity/$', hfu_cms.search_data.filter_localitybycity, name='filter_localitybycity'),
    url(r'^citybystate/$', hfu_cms.search_data.filter_citybystate, name='filter_citybystate'),

]



master_data_manage_urlpatterns = [
    url(r'^data/manage/$', views.master_data, name='master_data_page'),
    url(r'^manage/country/$', views.country_data, name='country_data_page'),
    url(r'^country/add/$', views.country_add_edit, name='country_add'),
    url(r'^country/edit/(?P<country_id>[0-9]+)/$', views.country_add_edit, name='country_edit'),
    url(r'^manage/state/$', views.state_data, name='state_data_page'),
    url(r'^state/add/$', views.state_add_edit, name='state_add'),
    url(r'^state/edit/(?P<state_id>[0-9]+)/$', views.state_add_edit, name='state_edit'),
    url(r'^manage/city/$', views.city_data, name='city_data_page'),
    url(r'^city/add/$', views.city_add_edit, name='city_add'),
    url(r'^city/edit/(?P<city_id>[0-9]+)/$', views.city_add_edit, name='city_edit'),
    url(r'^manage/locality/$', views.locality_data, name='locality_data_page'),
    url(r'^locality/add/$', views.locality_add_edit, name='locality_add'),
    url(r'^locality/edit/(?P<locality_id>[0-9]+)/$', views.locality_add_edit, name='locality_edit'),
    url(r'^manage/category/$', views.category_data, name='category_data_page'),
    url(r'^category/add/$', views.category_add_edit, name='category_add'),
    url(r'^category/edit/(?P<category_id>[0-9]+)/$', views.category_add_edit, name='category_edit'),

    
    url(r'^manage/new-service-offered/$', views.new_service_offered_data, name='new_service_offered_data_page'),
    url(r'^new-service-offered/add/$', views.new_service_offered_add_edit, name='new_service_offered_add'),
    url(r'^new-service-offered/edit/(?P<service_offered_id>[0-9]+)/$', views.new_service_offered_add_edit, name='new_service_offered_edit'),
    url(r'^new-service-offered/view-newso-loosers-data/$', views.view_newso_loosers_data, name='view_newso_loosers_data'),
    url(r'^new-service-offered/move-so-looser-to-winners-list/(?P<looser_so_id>[0-9]+)/$', views.move_so_looser_to_winners_list, name='move_so_looser_to_winners_list'),



    url(r'^manage/new-speciality/$', views.new_speciality_data, name='new_speciality_data_page'),
    url(r'^new-speciality/add/$', views.new_speciality_add_edit, name='new_speciality_add'),
    url(r'^new-speciality/edit/(?P<speciality_id>[0-9]+)/$', views.new_speciality_add_edit, name='new_speciality_edit'),

    url(r'^manage/cat-spl-so-association-new/$', views.new_association_data, name='new_association_data_page'),
    url(r'^new-association/add/$', views.new_association_add, name='new_association_add'),
    url(r'^new-association/edit/(?P<association_id>[0-9]+)/$', views.new_association_edit, name='new_association_edit'), 


    url(r'^manage/facility/$', views.facility_data, name='facility_data_page'),
    url(r'^facility/add/$', views.facility_add_edit, name='facility_add'),
    url(r'^facility/edit/(?P<facility_id>[0-9]+)/$', views.facility_add_edit, name='facility_edit'),

    url(r'^manage/department/$', views.department_data, name='department_data_page'),
    url(r'^department/add/$', views.department_add_edit, name='department_add'),
    url(r'^department/edit/(?P<department_id>[0-9]+)/$', views.department_add_edit, name='department_edit'),

    url(r'^manage/speciality/$', views.speciality_data, name='speciality_data_page'),
    url(r'^speciality/add/$', views.speciality_add_edit, name='speciality_add'),
    url(r'^speciality/edit/(?P<speciality_id>[0-9]+)/$', views.speciality_add_edit, name='speciality_edit'),
    url(r'^manage/service-offered/$', views.service_offered_data, name='service_offered_data_page'),
    url(r'^service-offered/add/$', views.service_offered_add_edit, name='service_offered_add'),
    url(r'^service-offered/edit/(?P<service_offered_id>[0-9]+)/$', views.service_offered_add_edit, name='service_offered_edit'),
    url(r'^manage/zone/$', views.zone_data, name='zone_data_page'),
    url(r'^zone/add/$', views.zone_add_edit, name='zone_add'),
    url(r'^zone/edit/(?P<zone_id>[0-9]+)/$', views.zone_add_edit, name='zone_edit'),
    url(r'^manage/zone-location/$', views.zone_location_data, name='zone_location_data_page'),
    url(r'^zone-location/add/$', views.zone_location_add_edit, name='zone_location_add'),
    url(r'^zone-location/edit/(?P<zone_location_id>[0-9]+)/$', views.zone_location_add_edit, name='zone_location_edit'),
    url(r'^manage/organisation_types/$', views.organisation_types_data, name='organisation_types_data_page'),
    url(r'^organisation_types/add/$', views.organisation_types_add_edit, name='organisation_types_add'),
    url(r'^organisation_types/edit/(?P<organisation_types_id>[0-9]+)/$', views.organisation_types_add_edit, name='organisation_types_edit'),
    url(r'^manage/organisation_categories/$', views.organisation_categories_data, name='organisation_categories_data_page'),
    url(r'^organisation_categories/add/$', views.organisation_categories_add_edit, name='organisation_categories_add'),
    url(r'^organisation_categories/edit/(?P<organisation_categories_id>[0-9]+)/$', views.organisation_categories_add_edit, name='organisation_categories_edit'),
    url(r'^manage/organisation_facilities/$', views.organisation_facilities_data, name='organisation_facilities_data_page'),
    url(r'^organisation_facilities/add/$', views.organisation_facilities_add_edit, name='organisation_facilities_add'),
    url(r'^organisation_facilities/edit/(?P<organisation_facilities_id>[0-9]+)/$', views.organisation_facilities_add_edit, name='organisation_facilities_edit'),
    url(r'^manage/disease_category/$', views.disease_category_data, name='disease_category_data_page'),
    url(r'^disease_category/add/$', views.disease_category_add_edit, name='disease_category_add'),
    url(r'^disease_category/edit/(?P<disease_category_id>[0-9]+)/$', views.disease_category_add_edit,name='disease_category_edit'),
    url(r'^manage/pharmacy_type/$', views.pharmacy_type_data, name='pharmacy_type_data_page'),
    url(r'^pharmacy_type/add/$', views.pharmacy_type_add_edit, name='pharmacy_type_add'),
    url(r'^pharmacy_type/edit/(?P<pharmacy_type_id>[0-9]+)/$', views.pharmacy_type_add_edit, name='pharmacy_type_edit'),
    url(r'^manage/pharmacy_services/$', views.pharmacy_services_data, name='pharmacy_services_data_page'),
    url(r'^pharmacy_services/add/$', views.pharmacy_services_add_edit, name='pharmacy_services_add'),
    url(r'^pharmacy_services/edit/(?P<pharmacy_services_id>[0-9]+)/$', views.pharmacy_services_add_edit, name='pharmacy_services_edit'),
    url(r'^manage/lab_accreditation_master/$', views.lab_accreditation_master_data,name='lab_accreditation_master_data_page'),
    url(r'^lab_accreditation_master/add/$', views.lab_accreditation_master_add_edit,name='lab_accreditation_master_add'),
    url(r'^lab_accreditation_master/edit/(?P<lab_accreditation_master_id>[0-9]+)/$',views.lab_accreditation_master_add_edit, name='lab_accreditation_master_edit'),
    url(r'^manage/lab_type_master/$', views.lab_type_master_data, name='lab_type_master_data_page'),
    url(r'^lab_type_master/add/$', views.lab_type_master_add_edit, name='lab_type_master_add'),
    url(r'^lab_type_master/edit/(?P<lab_type_master_id>[0-9]+)/$', views.lab_type_master_add_edit, name='lab_type_master_edit'),
    url(r'^manage/lab_test_master/$', views.lab_test_master_data, name='lab_test_master_data_page'),
    url(r'^lab_test_master/add/$', views.lab_test_master_add_edit, name='lab_test_master_add'),
    url(r'^lab_test_master/edit/(?P<lab_test_master_id>[0-9]+)/$', views.lab_test_master_add_edit,name='lab_test_master_edit'),
    url(r'^manage/lab_services_master/$', views.lab_services_master_data, name='lab_services_master_data_page'),
    url(r'^lab_services_master/add/$', views.lab_services_master_add_edit, name='lab_services_master_add'),
    url(r'^lab_services_master/edit/(?P<lab_services_master_id>[0-9]+)/$', views.lab_services_master_add_edit,name='lab_services_master_edit'),
    url(r'^manage/lab_department_master/$', views.lab_department_master_data, name='lab_department_master_data_page'),
    url(r'^lab_department_master/add/$', views.lab_department_master_add_edit, name='lab_department_master_add'),
    url(r'^lab_department_master/edit/(?P<lab_department_master_id>[0-9]+)/$', views.lab_department_master_add_edit,name='lab_department_master_edit'),
    url(r'^manage/bloodbank_services_master/$', views.bloodbank_services_master_data, name='bloodbank_services_master_data_page'),
    url(r'^bloodbank_services_master/add/$', views.bloodbank_services_master_add_edit,name='bloodbank_services_master_add'),
    url(r'^bloodbank_services_master/edit/(?P<bloodbank_services_master_id>[0-9]+)/$',views.bloodbank_services_master_add_edit, name='bloodbank_services_master_edit'),
     # Comment from here
    url(r'^manage/rehab_services_master/$', views.rehab_services_master_data, name='rehab_services_master_data_page'),
    url(r'^rehab_services_master/add/$', views.rehab_services_master_add_edit,name='rehab_services_master_add'),
    url(r'^rehab_services_master/edit/(?P<rehab_services_master_id>[0-9]+)/$',views.rehab_services_master_add_edit, name='rehab_services_master_edit'),

    url(r'^manage/rehab_type_master/$', views.rehab_type_master_data, name='rehab_type_master_data_page'),
    url(r'^rehab_type_master/add/$', views.rehab_type_master_add_edit, name='rehab_type_master_add'),
    url(r'^rehab_type_master/edit/(?P<rehab_type_master_id>[0-9]+)/$', views.rehab_type_master_add_edit, name='rehab_type_master_edit'),

    url(r'^manage/rehab_speciality_master/$', views.rehab_speciality_master_data, name='rehab_speciality_master_data_page'),
    url(r'^rehab_speciality_master/add/$', views.rehab_speciality_master_add_edit, name='rehab_speciality_master_add'),
    url(r'^rehab_speciality_master/edit/(?P<rehab_speciality_master_id>[0-9]+)/$', views.rehab_speciality_master_add_edit, name='rehab_speciality_master_edit'),

    url(r'^manage/nurse_bureau_services_master/$', views.nurse_bureau_services_master_data, name='nurse_bureau_services_master_data_page'),
    url(r'^nurse_bureau_services_master/add/$', views.nurse_bureau_services_master_add_edit,name='nurse_bureau_services_master_add'),
    url(r'^nurse_bureau_services_master/edit/(?P<nurse_bureau_services_master_id>[0-9]+)/$',views.nurse_bureau_services_master_add_edit, name='nurse_bureau_services_master_edit'),

    url(r'^manage/nurse_bureau_speciality_master/$', views.nurse_bureau_speciality_master_data, name='nurse_bureau_speciality_master_data_page'),
    url(r'^nurse_bureau_speciality_master/add/$', views.nurse_bureau_speciality_master_add_edit, name='nurse_bureau_speciality_master_add'),
    url(r'^nurse_bureau_speciality_master/edit/(?P<nurse_bureau_speciality_master_id>[0-9]+)/$', views.nurse_bureau_speciality_master_add_edit, name='nurse_bureau_speciality_master_edit'),

    url(r'^manage/dietitian_services_master/$', views.dietitian_services_master_data,name='dietitian_services_master_data_page'),
    url(r'^dietitian_services_master/add/$', views.dietitian_services_master_add_edit,name='dietitian_services_master_add'),
    url(r'^dietitian_services_master/edit/(?P<dietitian_services_master_id>[0-9]+)/$',views.dietitian_services_master_add_edit, name='dietitian_services_master_edit'),

    url(r'^manage/dietitian_type_master/$', views.dietitian_type_master_data, name='dietitian_type_master_data_page'),
    url(r'^dietitian_type_master/add/$', views.dietitian_type_master_add_edit, name='dietitian_type_master_add'),
    url(r'^dietitian_type_master/edit/(?P<dietitian_type_master_id>[0-9]+)/$', views.dietitian_type_master_add_edit,name='dietitian_type_master_edit'),

    url(r'^manage/disease_type_master/$', views.disease_type_master_data, name='disease_type_master_data_page'),
    url(r'^disease_type_master/add/$', views.disease_type_master_add_edit, name='disease_type_master_add'),
    url(r'^disease_type_master/edit/(?P<disease_type_master_id>[0-9]+)/$', views.disease_type_master_add_edit,name='disease_type_master_edit'),

    url(r'^manage/therapist_services_master/$', views.therapist_services_master_data,name='therapist_services_master_data_page'),
    url(r'^therapist_services_master/add/$', views.therapist_services_master_add_edit,name='therapist_services_master_add'),
    url(r'^therapist_services_master/edit/(?P<therapist_services_master_id>[0-9]+)/$',views.therapist_services_master_add_edit, name='therapist_services_master_edit'),

    url(r'^manage/therapist_type_master/$', views.therapist_type_master_data, name='therapist_type_master_data_page'),
    url(r'^therapist_type_master/add/$', views.therapist_type_master_add_edit, name='therapist_type_master_add'),
    url(r'^therapist_type_master/edit/(?P<therapist_type_master_id>[0-9]+)/$', views.therapist_type_master_add_edit,name='therapist_type_master_edit'),

    url(r'^manage/therapist_speciality_master/$', views.therapist_speciality_master_data, name='therapist_speciality_master_data_page'),
    url(r'^therapist_speciality_master/add/$', views.therapist_speciality_master_add_edit, name='therapist_speciality_master_add'),
    url(r'^therapist_speciality_master/edit/(?P<therapist_speciality_master_id>[0-9]+)/$', views.therapist_speciality_master_add_edit,name='therapist_speciality_master_edit'),


    url(r'^manage/ambulance_services_master/$', views.ambulance_services_master_data, name='ambulance_services_master_data_page'),
    url(r'^ambulance_services_master/add/$', views.ambulance_services_master_add_edit,name='ambulance_services_master_add'),
    url(r'^ambulance_services_master/edit/(?P<ambulance_services_master_id>[0-9]+)/$',views.ambulance_services_master_add_edit, name='ambulance_services_master_edit'),

    url(r'^manage/ambulance_type_master/$', views.ambulance_type_master_data, name='ambulance_type_master_data_page'),
    url(r'^ambulance_type_master/add/$', views.ambulance_type_master_add_edit, name='ambulance_type_master_add'),
    url(r'^ambulance_type_master/edit/(?P<ambulance_type_master_id>[0-9]+)/$', views.ambulance_type_master_add_edit, name='ambulance_type_master_edit'),

    url(r'^manage/kurables_type_master/$', views.kurables_type_master_data, name='kurables_type_master_data_page'),
    url(r'^kurables_type_master/add/$', views.kurables_type_master_add_edit, name='kurables_type_master_add'),
    url(r'^kurables_type_master/edit/(?P<kurables_type_master_id>[0-9]+)/$', views.kurables_type_master_add_edit, name='kurables_type_master_edit'),

    url(r'^manage/healthoholic_type_master/$', views.healthoholic_type_master_data, name='healthoholic_type_master_data_page'),
    url(r'^healthoholic_type_master/add/$', views.healthoholic_type_master_add_edit, name='healthoholic_type_master_add'),
    url(r'^healthoholic_type_master/edit/(?P<healthoholic_type_master_id>[0-9]+)/$', views.healthoholic_type_master_add_edit, name='healthoholic_type_master_edit'),

    url(r'^manage/caresidense_type_master/$', views.caresidense_type_master_data, name='caresidense_type_master_data_page'),
    url(r'^caresidense_type_master/add/$', views.caresidense_type_master_add_edit, name='caresidense_type_master_add'),
    url(r'^caresidense_type_master/edit/(?P<caresidense_type_master_id>[0-9]+)/$', views.caresidense_type_master_add_edit, name='caresidense_type_master_edit'),

    url(r'^manage/doc_care_services_master/$', views.doc_care_services_master_data, name='doc_care_services_master_data_page'),
    url(r'^doc_care_services_master/add/$', views.doc_care_services_master_add_edit, name='doc_care_services_master_add'),
    url(r'^doc_care_services_master/edit/(?P<doc_care_services_master_id>[0-9]+)/$', views.doc_care_services_master_add_edit, name='doc_care_services_master_edit'),

    url(r'^manage/disease_search_master/$', views.disease_search_master_data, name='disease_search_master_data_page'),
    url(r'^disease_search_master/add/$', views.disease_search_master_add_edit, name='disease_search_master_add'),
    url(r'^disease_search_master/edit/(?P<disease_search_master_id>[0-9]+)/$', views.disease_search_master_add_edit,name='disease_search_master_edit'),

    url(r'^manage/symptoms_search_master/$', views.symptoms_search_master_data, name='symptoms_search_master_data_page'),
    url(r'^symptoms_search_master/add/$', views.symptoms_search_master_add_edit, name='symptoms_search_master_add'),
    url(r'^symptoms_search_master/edit/(?P<symptoms_search_master_id>[0-9]+)/$', views.symptoms_search_master_add_edit,name='symptoms_search_master_edit'),

    ################################## New Country State City Locality  Master #############################################
    url(r'^manage/country_data/$', views.country_data_master, name='country_data_master'),
    url(r'^add/master_country/$', views.add_edit_master_country, name='add_master_country'),
    url(r'^edit/master_country/(?P<country_id>[0-9]+)/$', views.add_edit_master_country, name='edit_master_country'),

    url(r'^manage/state_data/$', views.state_data_master, name='state_data_master'),
    url(r'^add/master_state/$', views.add_edit_master_state, name='add_master_state'),
    url(r'^edit/master_state/(?P<state_id>[0-9]+)/$', views.add_edit_master_state, name='edit_master_state'),

    url(r'^manage/city_data/$', views.city_data_master, name='city_data_master'),
    url(r'^add/master_city/$', views.add_edit_master_city, name='add_master_city'),
    url(r'^edit/master_city/(?P<city_id>[0-9]+)/$', views.add_edit_master_city, name='edit_master_city'),

    url(r'^manage/locality_data/$', views.locality_data_master, name='locality_data_master'),
    url(r'^add/master_locality/$', views.add_edit_master_locality, name='add_master_locality'),
    url(r'^edit/master_locality/(?P<locality_id>[0-9]+)/$', views.add_edit_master_locality, name='edit_master_locality'),

    url(r'^manage/master-deactivate/(?P<object_id>[0-9]+)/(?P<object_type>[0-9]+)/$', views.manage_master_deactivate,
        name='manage-master-deactivate'),
    url(r'^manage/master-activate/(?P<object_id>[0-9]+)/(?P<object_type>[0-9]+)/$', views.manage_master_activate,
        name='manage-master-activate'),
    url(r'^manage/country_state_city_location/$', views.manage_country_state_city_location,
        name='manage_country_state_city_location'),

    # url(r'^publish_any_new_master/(?P<object_type>[0-9]+)/$', views.publish_any_new_master, name='publish_any_new_master'),
    # url(r'^unpublish_any_new_master/(?P<object_type>[0-9]+)/$', views.unpublish_any_new_master, name='unpublish_any_new_master'),
    # url(r'^publish_unpublish/$', views.publish_unpublish,
    #     name='publish_unpublish'),

    # url(r'^view/state_vise_city_data/$', views.view_state_vise_city_data, name='view_state_vise_city_data')

    url(r'^select-date/user-activity/$', views_two.user_activity_data_date_selection, name='user_activity_data_date_selection'),
    url(r'^view/user-activity/$', views_two.show_activity_list, name='show_activity_list'),

    url(r'^manage/country/$', views.country_data, name='country_data_page'), #DELETE THIS
    #Added by Ashutosh on 24 July
    url(r'^publish_unpublish/any_master_two/$', views_two.publish_unpublish_any_master_two, name='publish_unpublish_any_master_two'),
]

#url(r'^zone/manage/country/add-or-edit/$', views.add_edit_country, name='country_add_edit')
# url(r'^zone-location/manage/$', views.zone_location_data, name='zone-location_data_page'),

publisher_urlpatterns = [
    url(r'^doctor/listing/$', views.doctor_publisher_listing, name='publisher-doctor-listing'),
    url(r'^live-doctor/listing/$', views.live_doctor_publisher_listing, name='publisher-live-doctor-listing'),
    url(r'^organisation/listing/$', views.organisation_publisher_listing, name='publisher-organisation-listing'),
    url(r'^live_organisation/listing/$', views_two.live_organisation_publisher_listing, name='publisher-live-organisation-listing'),

    url(r'^publish/$', views.publish_doctor, name='data-publish'),
    url(r'^lab/listing/$', views.lab_publisher_listing, name='publisher-lab-listing'),
    url(r'^pharmacy/listing/$', views.pharmacy_publisher_listing, name='publisher-pharmacy-listing'),
    url(r'^ambulance/listing/$', views.ambulance_publisher_listing, name='publisher-ambulance-listing'),
    url(r'^blood-bank/listing/$', views.bloodbank_publisher_listing, name='publisher-bloodbank-listing'),
    url(r'^disease/listing/$', views.disease_publisher_listing, name='publisher-disease-listing'),
    url(r'^drug/listing/$', views.drug_publisher_listing, name='publisher-drug-listing'),
    url(r'^symptoms/listing/$', views.symptoms_publisher_listing, name='publisher-symptoms-listing'),
    url(r'^rehab/listing/$', views.rehab_publisher_listing, name='publisher-rehab-listing'),
    url(r'^nurse_bureau/listing/$', views.nurse_bureau_publisher_listing, name='publisher-nurse_bureau-listing'),
    url(r'^dietitian/listing/$', views.dietitian_publisher_listing, name='publisher-dietitian-listing'),
    url(r'^therapist/listing/$', views.therapist_publisher_listing, name='publisher-therapist-listing'),


    url(r'^delete/error_logs/(?P<log_id>[0-9]+)/$', hfu_cms.errorlog_functions.delete_error_log, name='delete-error-log'),

    url(r'^doctor/error_logs/$', hfu_cms.errorlog_functions.doctor_error_logs, name='doctor_error_logs'),
    url(r'^organisation/error_logs/$', hfu_cms.errorlog_functions.organisation_error_logs, name='organisation_error_logs'),
    url(r'^lab/error_logs/$', hfu_cms.errorlog_functions.lab_error_logs, name='lab_error_logs'),
    url(r'^bloodbank/error_logs/$', hfu_cms.errorlog_functions.bloodbank_error_logs, name='bloodbank_error_logs'),
    url(r'^ambulance/error_logs/$', hfu_cms.errorlog_functions.ambulance_error_logs, name='ambulance_error_logs'),
    url(r'^pharmacy/error_logs/$', hfu_cms.errorlog_functions.pharmacy_error_logs, name='pharmacy_error_logs'),
    url(r'^rehab/error_logs/$', hfu_cms.errorlog_functions.rehab_error_logs, name='rehab_error_logs'),
    url(r'^disease/error_logs/$', hfu_cms.errorlog_functions.disease_error_logs, name='disease_error_logs'),
    url(r'^symptoms/error_logs/$', hfu_cms.errorlog_functions.symptoms_error_logs, name='symptoms_error_logs'),
    url(r'^Serviceplan/error_logs/$', hfu_cms.errorlog_functions.Serviceplan_error_logs, name='Serviceplan_error_logs'),

]

login_urlpatterns = [
    url(r'^$', views.index, name='index-page'),
    url(r'^cms/user/$', views.user_page, name='user-page'),
    url(r'^forgot/$', views.forgot_password, name='forgot-page'),
    url(r'^locate/us/$', views.locate_us_data, name='locate_us-page'),
    url(r'^cms/login/$', views.login_user, name='users-login'),
    url(r'^cms/logout/$', views.logout_doc, name='users-logout'),
    url(r'^cms/dashboard/$', views.dashboard, name='users-dashboard'),
    url(r'^cms/data/management/$', views.data_management, name='users-data-management'),
    url(r'^cms/disease-symptom-drug/management/$', views.disease_symptom_drug_home, name='disease_symptom_drug_home'),
    url(r'^cms/care-residence/management/$', views.care_residence_home, name='care_residence_home'),

    url(r'^cms/care-residence/management/doctors/$', views.doctor_care_listing, name='doctor-care-listing'),
    url(r'^cms/care-residence/management/doctor/add/$', views.add_care_doctor, name='doctor-care-add'),
    url(r'^cms/care-residence/management/doctor/edit/(?P<doctor_id>[0-9]+)/$', views.edit_care_doctor, name='doctor-care-edit'),
    url(r'^cms/care-residence/management/doctor/remove/(?P<doctor_id>[0-9]+)/$', views.remove_care_doctor, name='doctor-care-remove'),
    url(r'^cms/care-residence/management/doctor/schedule/(?P<doctor_id>[0-9]+)/$', views.schedule_care_doctor,name='time-schedule-care-doctor'),

    # url(r'^cms/care-residence/management/labs/$', views.lab_care_listing, name='lab-care-listing'),
    # url(r'^cms/care-residence/management/lab/add/$', views.add_care_lab, name='lab-care-add'),
    # url(r'^cms/care-residence/management/lab/edit/(?P<lab_id>[0-9]+)/$', views.edit_care_lab, name='lab-care-edit'),
    # url(r'^cms/care-residence/management/lab/remove/(?P<lab_id>[0-9]+)/$', views.remove_care_lab, name='lab-care-remove'),
    # url(r'^cms/care-residence/management/lab/schedule/(?P<lab_id>[0-9]+)/$', views.schedule_care_lab,name='time-schedule-care-lab'),


]

user_manage_urlpatterns = [
    url(r'^cms/users/$', views.MyUser.as_view(), name='user-management'),
    url(r'^cms/users/deactivate/(?P<user_id>[0-9]+)/$', views.deactivate_user, name='user-deactivate'),
    url(r'^cms/users/activate/(?P<user_id>[0-9]+)/$', views.activate_user, name='user-activate'),
    url(r'^hfu/cms/caller/$', views.caller_user, name='user-caller'),
    url(r'^hfu/cms/reviewer/$', views.reviewer_user, name='user-reviewer'),
    url(r'^hfu/cms/publisher/$', views.publisher_user, name='user-publisher'),
    url(r'^hfu/cms/news/$', views.news_user, name='user-news'),
    url(r'^hfu/cms/service/$', views.service_user, name='user-service'),
    url(r'^hfu/cms/admin/$', views.admin_user, name='user-admin'),
    url(r'^hfu/cms/add/user/$', views.MyUserList.as_view(user_cms='caller'), name='get-caller-users'),
    url(r'^hfu/cms/add/reviewer/$', views.MyUserList.as_view(user_cms='reviewer'), name='get-reviewer-users'),
    url(r'^hfu/cms/add/admin/$', views.MyUserList.as_view(user_cms='admin'), name='get-admin-users'),
    url(r'^hfu/cms/add/publisher/$', views.MyUserList.as_view(user_cms='publisher'), name='get-publisher-users'),
    url(r'^hfu/cms/add/news/$', views.MyUserList.as_view(user_cms='news'), name='get-news-users'),
    url(r'^hfu/cms/add/service/$', views.MyUserList.as_view(user_cms='service'), name='get-service-users'),
    url(r'^hfu/cms/check/username/$', views.check_username, name='check-username'),
    url(r'^hfu/cms/username/edit/(?P<user_id>[0-9]+)/$', views.users_edit, name='users-edit'),

]

doctor_manage_urlpatterns = [
    url(r'^management/$', views.doctor_data_manage, name='doctor-management'),
    url(r'^users/$', views.doctor_data_by_users, name='doctor-by-users'),
    url(r'^doctor/stages/$', views.doctor_data_by_stages, name='doctor-by-stages'),
    url(r'^listing/$', views.doctor_listing, name='doctor-listing'),
    url(r'^edit/(?P<doctor_id>[0-9]+)/$', views.doctor_listing_edit, name='doctor-listing-edit'),
    #url(r'^edit/((?P<doctor_id>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}))/$', views.doctor_uuidlisting_edit, name='doctor-listing-edit'),
    url(r'^add/$', views.add_doctor, name='doctor-add'),
    url(r'^reward/(?P<doctor_id>[0-9]+)/$', views.reward_doctor, name='doctor-reward'),
    url(r'^education/(?P<doctor_id>[0-9]+)/$', views.education_doctor, name='doctor-education'),
    url(r'^attached/(?P<doctor_id>[0-9]+)/$', views.attach_doctor, name='doctor-attach'),
    url(r'^verified-fields/(?P<doctor_id>[0-9]+)/$', views.doctor_verified_fields, name='doctor_verified_fields'),
    url(r'^schedule/(?P<doctor_id>[0-9]+)/(?P<organisation_id>[0-9]+)/$', views.schedule_doctor,
        name='time-schedule-doctor'),
    url(r'^zone_location/$', views.zone_location, name='zone_location'),
    url(r'^category/$', views.category, name='category'),
    url(r'^category_two/$', views.category_two, name='category_two'),
    url(r'^assignment/$', views.assignment, name='doctor-assignment'),
    #abbed by ashutosh on 22nd july
    url(r'^markascomplete/$', views_two.markascomplete, name='markascomplete'),
    url(r'^mark-for-search-results/$', views_two.doctor_mark_for_search_results, name='doctor-mark-for-search-results'),
    url(r'^get-doctors-for-search-results/$', views_two.get_doctors_for_search_results, name='get-doctors-for-search-results'),
    url(r'^save-doctor-rank/$', views_two.save_doctor_rank, name='save-doctor-rank'),
    url(r'^upload/profile_pic_doc/(?P<doctor_id>[0-9]+)/$', views.upload_profile_pic_doc, name='upload_profile_pic_doc'),
    url(r'^delete/profile_pic_doc/(?P<doctor_id>[0-9]+)/$', views.delete_profile_pic_doc, name='delete_profile_pic_doc'),
    url(r'^gallery-images-doctor/(?P<doctor_id>[0-9]+)/$', views.gallery_images_doctor, name='gallery_images_doctor'),
    url(r'^doc-gallery-images-changes/(?P<doctor_id>[0-9]+)/$', views.doc_gallery_images_changes, name='doc_gallery_images_changes'),
    url(r'^schedule/stopdate/notification/$', views_two.doc_schedule_stopdate_notification, name='doc_schedule_stopdate_notification'),

    url(r'^sponsored-ranks-deleted-schedules/$', views_two.doctor_sponsored_ranks_deleted_schedules,
        name='doctor_sponsored_ranks_deleted_schedules'),

    url(r'^reset-doctor-sponsranks-deleted-schedules/$', views_two.reset_doctor_sponsranks_deleted_schedules, name='reset_doctor_sponsranks_deleted_schedules'),

]

live_doctor_manage_urlpatterns = [
      url(r'^live-doc-management/$', views.live_doctor_data_manage, name='live_doctor_management'),
      url(r'^by-users/$', views.live_doctor_by_users, name='live_doctor_by_users'),
      url(r'^by-stages/$', views.live_doctor_by_stages, name='live_doctor_by_stages'),
      url(r'^type/$', views.live_doctor_type, name='live-doctor-type'),
      url(r'^listing/new-registrations/$', views.live_doctor_new_registrations_listing, name='live_doctor_new_registrations_listing'),
#     url(r'^listing/update-existing/$', views.live_doctor_update_existing, name='live_doctor_update_existing'),
      url(r'^update/education/(?P<doctor_id>[0-9]+)/(?P<edu_id>[0-9]+)/$', views.live_doctor_update_education,
        name='live_doctor_update_education'),
      url(r'^update/experience/(?P<doctor_id>[0-9]+)/(?P<exp_id>[0-9]+)/$', views.live_doctor_update_experience,
        name='live_doctor_update_experience'),
      url(r'^update/membership/(?P<doctor_id>[0-9]+)/(?P<mem_id>[0-9]+)/$', views.live_doctor_update_membership,
        name='live_doctor_update_membership'),


      url(r'^add/qualification/(?P<doctor_id>[0-9]+)/$', views.live_doctor_add_qualification, name='live_doctor_add_qualification'),
      url(r'^update/totalexperience/(?P<doctor_id>[0-9]+)/$', views_two.live_doctor_update_totalexperience, name='live_doctor_update_totalexperience'),
      url(r'^add/', views.live_doctor_listing_add, name='live_doctor_listing_add'),
      url(r'^edit/(?P<doctor_id>[0-9]+)/$', views.live_doctor_listing_edit, name='live_doctor_listing_edit'),
      url(r'^delete/membership/(?P<doctor_id>[0-9]+)/(?P<memship_id>[0-9]+)/$', views.delete_live_doctor_membership, name='delete_live_doctor_membership'),
      url(r'^delete/experience/(?P<doctor_id>[0-9]+)/(?P<exp_id>[0-9]+)/$', views.delete_live_doctor_experience, name='delete_live_doctor_experience'),
      url(r'^delete/reward-recognition/(?P<doctor_id>[0-9]+)/(?P<reward_id>[0-9]+)/$', views.delete_live_doctor_reward_recog, name='delete_live_doctor_reward_recog'),
      url(r'^update/registration/(?P<doctor_id>[0-9]+)/$', views.live_doctor_update_registration, name='live_doctor_update_registration'),
      url(r'^delete/education/(?P<doctor_id>[0-9]+)/(?P<edu_id>[0-9]+)/$', views.live_doctor_delete_education, name='live_doctor_delete_education'),
      url(r'^upload/registration-pic/(?P<doctor_id>[0-9]+)/$', views.upload_registration_pic, name='upload_registration_pic'),
      url(r'^upload/aadhar-pic/(?P<doctor_id>[0-9]+)/$', views.upload_aadhar_pic, name='upload_aadhar_pic'),
      url(r'^upload/stamp-pic/(?P<doctor_id>[0-9]+)/$', views.upload_stamp_pic, name='upload_stamp_pic'),
      url(r'^upload/signature_pic/(?P<doctor_id>[0-9]+)/$', views.upload_signature_pic, name='upload_signature_pic'),
      url(r'^upload/profile_pic/(?P<doctor_id>[0-9]+)/$', views.upload_profile_pic, name='upload_profile_pic'),
      url(r'^upload/gallery_pic/(?P<doctor_id>[0-9]+)/$', views.upload_gallery_pic, name='upload_gallery_pic'),
      url(r'^live_doctor/registration/backend/(?P<doctor_id>[0-9]+)/$', views.create_user_account, name='create_user_account'),
      url(r'^live_doctor/activate/backend/(?P<doctor_id>[0-9]+)/$', views.activate_doctor_account, name='activate_doctor_account'),
      url(r'^live_doctor/deactivate/backend/(?P<doctor_id>[0-9]+)/$', views.deactivate_doctor_account, name='deactivate_doctor_account'),
      url(r'^delete/schedule/(?P<doctor_id>[0-9]+)/(?P<sch_id>[0-9]+)/$', views.live_doctor_delete_schedule, name='live_doctor_delete_schedule'),
      url(r'^manage/talk-to-doc/(?P<doctor_id>[0-9]+)/$', views.live_doctor_talk_to_doc, name='live_doctor_talk_to_doc'),
      url(r'^manage/emergency/(?P<doctor_id>[0-9]+)/$', views.live_doctor_emergency, name='live_doctor_emergency'),
      url(r'^delete/gallery-images/(?P<doctor_id>[0-9]+)/$', views.delete_live_doc_gallery_images, name='delete_live_doc_gallery_images'),
      url(r'^view-duplicates/(?P<doctor_id>[0-9]+)/$', views.view_duplicates, name='view_duplicates'),
      url(r'^merge-duplicates/(?P<merge_id>[0-9]+)/(?P<doctor_id>[0-9]+)$', views_two.merge_duplicates, name='merge-duplicates'),

      url(r'^notification/$', views_two.live_doc_notification, name='live_doc_notification'),
      url(r'^schedule/notification/$', views_two.live_doc_schedule_delete_notification, name='live_doc_schedule_delete_notification'),
      url(r'^schedule/stopdate/notification/$', views_two.live_doc_schedule_stopdate_notification, name='live_doc_schedule_stopdate_notification'),

#     url(r'^add/$', views.add_doctor, name='doctor-add'),
#     url(r'^reward/(?P<doctor_id>[0-9]+)/$', views.reward_doctor, name='doctor-reward'),
#     url(r'^education/(?P<doctor_id>[0-9]+)/$', views.education_doctor, name='doctor-education'),
#     url(r'^attached/(?P<doctor_id>[0-9]+)/$', views.attach_doctor, name='doctor-attach'),
#     url(r'^schedule/(?P<doctor_id>[0-9]+)/(?P<organisation_id>[0-9]+)/$', views.schedule_doctor,
#         name='time-schedule-doctor'),
#     url(r'^zone_location/$', views.zone_location, name='zone_location'),
#     url(r'^category/$', views.category, name='category'),
      url(r'^assignment/$', views.live_doctor_assignment, name='live_doctor_assignment'),
      url(r'^sponsored-ranks-deleted-schedules/$', views.sponsored_ranks_deleted_schedules, name='sponsored_ranks_deleted_schedules'),
      url(r'^deactivate-single-live-doctor/(?P<doctor_id>[0-9]+)/$', views.deactivate_single_live_doctor, name='deactivate_single_live_doctor'),
      url(r'^activate-single-live-doctor/(?P<doctor_id>[0-9]+)/$', views.activate_single_live_doctor, name='activate_single_live_doctor'),
      url(r'^update-did-extension-live-doc-schedule/(?P<schedule_id>[0-9]+)/$', views.update_did_extension_live_doc_schedule, name='update_did_extension_live_doc_schedule'),

      url(r'^update/login/(?P<doctor_id>[0-9]+)/$', views.live_doc_update_login, name='live_doc_update_login'),
      url(r'^upload/privateimage/(?P<doctor_id>[0-9]+)/$', views_two.upload_privateimage, name='upload_private_images'),
      url(r'^delete/private-images/(?P<doctor_id>[0-9]+)/$', views_two.delete_live_doc_private_images, name='delete_live_doc_private_images'),
      url(r'^edit/manageaccountlivedoctor/$', views.update_manage_account_live_doctor, name='update-manage-account-live-doctor'),
      url(r'^delete-receipt/(?P<doctor_id>[0-9]+)/(?P<record_id>[0-9]+)/$', views.delete_receipt, name='live-doctor-delete-receipt'),
      url(r'^delete-invoice/(?P<doctor_id>[0-9]+)/(?P<record_id>[0-9]+)/$', views.delete_invoice, name='live-doctor-delete-invoice'),
      url(r'^mark-for-search-results/$', views_two.live_doc_mark_for_search_results, name='live-doc-mark-for-search-results'),
      url(r'^get-live-docs-for-search-results/$', views_two.get_live_docs_for_search_results, name='get-live-docs-for-search-results'),
      url(r'^save-live-doctor-rank/$', views_two.save_live_doctor_rank, name='save-live-doctor-rank'),
      url(r'^reset-livedoctor-sponsranks-deleted-schedules/$', views_two.reset_livedoctor_sponsranks_deleted_schedules, name='reset_livedoctor_sponsranks_deleted_schedules'),
      url(r'^set-live-doctor-subscribed-ranks/(?P<doctor_id>[0-9]+)/$', views_two.set_live_doctor_subscribed_ranks, name='set_live_doctor_subscribed_ranks'),


 ]


organisation_manage_urlpatterns = [

    url(r'^listing/$', views.organisation_listing, name='organisation-listing'),
    url(r'^add/$', views.organisation_adding, name='organisation-adding'),
    url(r'^management/$', views.organisation_data_manage, name='organisation-management'),
    url(r'^by/users/$', views.organisation_data_by_users, name='organisation-by-users'),
    url(r'^by/stages/$', views.organisation_data_by_stages, name='organisation-by-stages'),
    url(r'^assignment/users/$', views.organisation_assignment, name='organisation-assignment'),
    url(r'^address/$', views.organisation_address, name='organisation-address'),
    url(r'^edit/(?P<organisation_id>[0-9]+)/$', views.organisation_listing_edit, name='organisation-listing-edit',kwargs={'getcoordinates':'GET','setcoordinates':'UNSET'}),
    url(r'^organisation-profile-image/(?P<org_id>[0-9]+)/$', views_two.organisation_profile_image, name='organisation-profile-image'),
    url(r'^schedule/(?P<organisation_id>[0-9]+)/$', views.schedule_hospital,name='time-schedule-hospital'),
    url(r'^getcoordinatess/(?P<organisation_id>[0-9]+)/$', views.getcoordinatess,name='organisation_getcoordinatess'),
    url(r'^discardcoordinatess/(?P<organisation_id>[0-9]+)/$', views.discardcoordinatess,name='discardcoordinatess'),
    url(r'^savecoordinatess/(?P<organisation_id>[0-9]+)/$', views.savecoordinatess,name='savecoordinatess'),
]

notification_manage_urlpattern = [
    # url(r'^live_doctor/bydate$', views_two.live_doctor_notification_bydate, name='live_doctor_notification_bydate'),
    url(r'^live_doctor/bydate$', views_two.live_doctor_notification_bydate, name='live_doctor_notification_bydate'),
    url(r'^live_doctor_schedule/bydate$', views_two.live_doctor_schedule_notification_bydate, name='live_doctor_schedule_notification_bydate'),
    # url(r'^live-doctor/byname$', views_two.live_doctor_notification_byname, name='live_doctor_notification_byname'),
    url(r'^live-organisation$', views_two.live_organisation_notification, name='live-organisation-notification'),
    url(r'^live-organisation/bydate$', views_two.live_organisation_notification_bydate, name='live-organisation-notification-bydate'),
    url(r'^livedoctor-delete-older-than-fifteen-days$', views_two.livedoctor_delete_older_than_fifteen_days, name='livedoctor_delete_older_than_fifteen_days'),
    #url(r'^live-doc-management/$', views.live_doctor_data_manage, name='live_doctor_management'),
    url(r'^doctor-rank-module/$', views_two.doctor_rank_module, name='doctor_rank_module'),
    url(r'^doctor-rank-module/old-doctor/$', views_two.old_doctor_rank_module, name='old_doctor_rank_module'),
    url(r'^doctor-rank-module/live-doctor/$', views_two.live_doctor_rank_module, name='live_doctor_rank_module'),
    url(r'^live-doctor-sponsored-ranks-report/$', views_two.sponsored_ranks_report, name='sponsored_ranks_report'),
    url(r'^live-doctorsubscribed-ranks-report/$', views_two.subscribed_ranks_report, name='subscribed_ranks_report'),
    url(r'^doctor-sponsored-ranks-report/$', views_two.doctor_sponsored_ranks_report, name='doctor_sponsored_ranks_report'),
]
live_organisation_manage_urlpatterns = [

    url(r'^listing/$', views_two.live_organisation_listing, name='live-organisation-listing'),
    url(r'^edit/(?P<organisation_id>[0-9]+)/$', views.live_organisation_listing_edit, name='live-organisation-listing-edit'),
    url(r'^delete/schedule/(?P<organisation_id>[0-9]+)/$', views_two.live_organisation_delete_schedule, name='delete-live-organisation-schedule'),
    # url(r'^add/$', views_two.live_organisation_adding, name='organisation-adding'),
    url(r'^management/$', views_two.live_organisation_data_manage, name='live-organisation-management'),
    url(r'^by/users/$', views_two.live_organisation_data_by_users, name='live-organisation-by-users'),
    url(r'^by/stages/$', views_two.live_organisation_data_by_stages, name='live-organisation-by-stages'),
    url(r'^assignment/users/$', views_two.live_organisation_assignment, name='live-organisation-assignment'),
    url(r'^create_user_account/(?P<organisation_id>[0-9]+)/$', views_two.create_user_account_for_live_organisation, name='create_user_account_for_live_organisation'),
    # url(r'^address/$', views_two.live_organisation_address, name='organisation-address'),
    # url(r'^schedule/(?P<organisation_id>[0-9]+)/$', views_two.live_schedule_hospital,
    #     name='time-schedule-hospital'),
    url(r'^view-duplicates/(?P<organisation_id>[0-9]+)/$', views_two.view_duplicates_organisation, name='view_duplicates_organisation'),
    url(r'^merge-duplicate-/(?P<old_clinic_id>[0-9]+)/(?P<new_clinic_id>[0-9]+)$', views_two.merge_duplicate_organisation, name='merge_duplicate_organisation'),
    url(r'^assign/$', views_two.assign_live_organisation, name='live-assign-organisation'),
    # url(r'^finalise/(?P<organisation_id>[0-9]+)/$', views_two.finalise_live_organisatioin, name='finalise_live_organisation'),
    url(r'^finalise/(?P<organisation_id>[0-9]+)/$', views_two.finalise_live_organisatioin, name='finalise_live_organisation'),
    url(r'^associate/(?P<organisation_id>[0-9]+)/(?P<doctor_id>[0-9]+)/$', views_two.associate_disassociate_live_organisation, name='associate-disassociate-live-organisation'),
    url(r'^upload/image/(?P<organisation_id>[0-9]+)/$', views_two.live_org_upload_image, name='live_org_upload_image'),
    url(r'^disable-enable/branches/(?P<organisation_id>[0-9]+)/$', views_two.live_org_disable_enable_branches, name='live_org_disable_enable_branches'),

    url(r'^delete/rew_recog/(?P<rewrecog_id>[0-9]+)/$', views_two.live_org_delete_rewrecog, name='live_org_delete_rewrecog'),
]

#added by jaydeep

lab_manage_urlpatterns = [
    url(r'^assignment/users/$', views.lab_assignment, name='lab-assignment'),
    url(r'^management/$', views.lab_data_manage, name='lab-management'),
    url(r'^by/users/$', views.lab_data_by_users, name='lab-by-users'),
    url(r'^by/stages/$', views.lab_data_by_stages, name='lab-by-stages'),
    url(r'^listing/$', views.lab_listing, name='lab-listing'),
    url(r'^add/$', views.add_lab, name='add_lab'),
    url(r'^edit/(?P<lab_id>[0-9]+)/$', views.lab_listing_edit, name='lab-listing-edit'),
    url(r'^schedule/(?P<lab_id>[0-9]+)/$', views.schedule_lab,name='time-schedule-lab'),
    url(r'^schedule/lab/(?P<lab_id>[0-9]+)/branch/(?P<lab_branch_id>[0-9]+)/$', views.schedule_lab_branch,name='time-schedule-lab-branch'),
]


rehab_manage_urlpatterns = [
     url(r'^assignment/users/$', views.rehab_assignment, name='rehab-assignment'),
     url(r'^management/$', views.rehab_data_manage, name='rehab-management'),
     url(r'^by/users/$', views.rehab_data_by_users, name='rehab-by-users'),
     url(r'^by/stages/$', views.rehab_data_by_stages, name='rehab-by-stages'),
     url(r'^listing/$', views.rehab_listing, name='rehab-listing'),
     url(r'^add/$', views.add_rehab, name='add_rehab'),
     url(r'^edit/(?P<rehab_id>[0-9]+)/$', views.rehab_listing_edit, name='rehab-listing-edit'),
     url(r'^schedule/(?P<rehab_id>[0-9]+)/$', views.schedule_rehab,name='time-schedule-rehab'),

 ]


nurse_bureau_manage_urlpatterns = [
     url(r'^assignment/users/$', views.nurse_bureau_assignment, name='nurse_bureau-assignment'),
     url(r'^management/$', views.nurse_bureau_data_manage, name='nurse_bureau-management'),
     url(r'^by/users/$', views.nurse_bureau_data_by_users, name='nurse_bureau-by-users'),
     url(r'^by/stages/$', views.nurse_bureau_data_by_stages, name='nurse_bureau-by-stages'),
     url(r'^listing/$', views.nurse_bureau_listing, name='nurse_bureau-listing'),
     url(r'^add/$', views.add_nurse_bureau, name='add_nurse_bureau'),
     url(r'^edit/(?P<nurse_bureau_id>[0-9]+)/$', views.nurse_bureau_listing_edit, name='nurse_bureau-listing-edit'),
     url(r'^schedule/(?P<nurse_bureau_id>[0-9]+)/$', views.schedule_nurse_bureau,name='time-schedule-nurse_bureau'),

 ]

dietitian_manage_urlpatterns = [
     url(r'^assignment/users/$', views.dietitian_assignment, name='dietitian-assignment'),
     url(r'^management/$', views.dietitian_data_manage, name='dietitian-management'),
     url(r'^by/users/$', views.dietitian_data_by_users, name='dietitian-by-users'),
     url(r'^by/stages/$', views.dietitian_data_by_stages, name='dietitian-by-stages'),
     url(r'^listing/$', views.dietitian_listing, name='dietitian-listing'),
     url(r'^add/$', views.add_dietitian, name='add_dietitian'),
     url(r'^edit/(?P<dietitian_id>[0-9]+)/$', views.dietitian_listing_edit, name='dietitian-listing-edit'),
     url(r'^schedule/(?P<dietitian_id>[0-9]+)/(?P<organisation_id>[0-9]+)/$', views.dietitian_org_schedule,name='time-schedule-dietitian'),
 ]

therapist_manage_urlpatterns = [
     url(r'^assignment/users/$', views.therapist_assignment, name='therapist-assignment'),
     url(r'^management/$', views.therapist_data_manage, name='therapist-management'),
     url(r'^by/users/$', views.therapist_data_by_users, name='therapist-by-users'),
     url(r'^by/stages/$', views.therapist_data_by_stages, name='therapist-by-stages'),
     url(r'^listing/$', views.therapist_listing, name='therapist-listing'),
     url(r'^add/$', views.add_therapist, name='add_therapist'),
     url(r'^edit/(?P<therapist_id>[0-9]+)/$', views.therapist_listing_edit, name='therapist-listing-edit'),
     url(r'^schedule/(?P<therapist_id>[0-9]+)/(?P<organisation_id>[0-9]+)/$', views.therapist_org_schedule,name='time-schedule-therapist'),
 ]

blood_bank_manage_urlpatterns = [
    url(r'^assignment/users/$', views.bloodbank_assignment, name='bloodbank-assignment'),
    url(r'^management/$', views.bloodbank_data_manage, name='bloodbank-management'),
    url(r'^by/users/$', views.bloodbank_data_by_users, name='bloodbank-by-users'),
    url(r'^by/stages/$', views.bloodbank_data_by_stages, name='bloodbank-by-stages'),
    url(r'^listing/$', views.bloodbank_listing, name='bloodbank-listing'),
    url(r'^add/$', views.add_bloodbank, name='add_bloodbank'),
    url(r'^edit/(?P<bloodbank_id>[0-9]+)/$', views.bloodbank_listing_edit, name='bloodbank-listing-edit'),
    url(r'^schedule/(?P<bloodbank_id>[0-9]+)/$', views.schedule_bloodbank,name='time-schedule-bloodbank'),
    url(r'^verified-fields/(?P<bloodbank_id>[0-9]+)/$', views.bloodbank_verified_fields, name='bloodbank_verified_fields'),
]


drug_manage_urlpatterns = [
    url(r'^assignment/users/$', views.drug_assignment, name='drug-assignment'),
    url(r'^management/$', views.drug_data_manage, name='drug-management'),
    url(r'^by/users/$', views.drug_data_by_users, name='drug-by-users'),
    url(r'^by/stages/$', views.drug_data_by_stages, name='drug-by-stages'),
    url(r'^listing/$', views.drug_listing, name='drug-listing'),
    url(r'^add/$', views.add_drug, name='add_drug'),
    url(r'^edit/(?P<drug_id>[0-9]+)/$', views.drug_listing_edit, name='drug-listing-edit'),
]

disease_manage_urlpatterns = [
    url(r'^assignment/users/$', views.disease_assignment, name='disease-assignment'),
    url(r'^management/$', views.disease_data_manage, name='disease-management'),
    url(r'^by/users/$', views.disease_data_by_users, name='disease-by-users'),
    url(r'^by/stages/$', views.disease_data_by_stages, name='disease-by-stages'),
    url(r'^listing/$', views.disease_listing, name='disease-listing'),
    url(r'^add/$', views.add_disease, name='add_disease'),
    url(r'^edit/(?P<disease_id>[0-9]+)/$', views.disease_listing_edit, name='disease-listing-edit'),

]

symptoms_manage_urlpatterns = [
    url(r'^assignment/users/$', views.symptoms_assignment, name='symptoms-assignment'),
    url(r'^management/$', views.symptoms_data_manage, name='symptoms-management'),
    url(r'^by/users/$', views.symptoms_data_by_users, name='symptoms-by-users'),
    url(r'^by/stages/$', views.symptoms_data_by_stages, name='symptoms-by-stages'),
    url(r'^listing/$', views.symptoms_listing, name='symptoms-listing'),
    url(r'^add/$', views.add_symptoms, name='add_symptoms'),
    url(r'^edit/(?P<symptoms_id>[0-9]+)/$', views.symptoms_listing_edit, name='symptoms-listing-edit'),

]


ambulance_manage_urlpatterns = [
    url(r'^assignment/users/$', views.ambulance_assignment, name='ambulance-assignment'),
    url(r'^management/$', views.ambulance_data_manage, name='ambulance-management'),
    url(r'^by/users/$', views.ambulance_data_by_users, name='ambulance-by-users'),
    url(r'^by/stages/$', views.ambulance_data_by_stages, name='ambulance-by-stages'),
    url(r'^listing/$', views.ambulance_listing, name='ambulance-listing'),
    url(r'^add/$', views.add_ambulance, name='add_ambulance'),
    url(r'^edit/(?P<ambulance_id>[0-9]+)/$', views.ambulance_listing_edit, name='ambulance-listing-edit'),

]

pharmacy_manage_urlpatterns = [
    url(r'^assignment/users/$', views.pharmacy_assignment, name='pharmacy-assignment'),
    url(r'^management/$', views.pharmacy_data_manage, name='pharmacy-management'),
    url(r'^by/users/$', views.pharmacy_data_by_users, name='pharmacy-by-users'),
    url(r'^by/stages/$', views.pharmacy_data_by_stages, name='pharmacy-by-stages'),
    url(r'^listing/$', views.pharmacy_listing, name='pharmacy-listing'),
    url(r'^add/$', views.add_pharmacy, name='add_pharmacy'),
    url(r'^edit/(?P<pharmacy_id>[0-9]+)/$', views.pharmacy_listing_edit, name='pharmacy-listing-edit'),
    url(r'^schedule/(?P<pharmacy_id>[0-9]+)/$', views.schedule_pharmacy,name='time-schedule-pharmacy'),
]



push_data_urlpatterns =[
   url(r'^data_pooling_in_cms/$', views.data_pooling_in_cms, name='data_pooling_in_cms'),
]

mark_as_urlpatterns = [
   url(r'^complete/$', views.mark_as_complete_caller, name='mark-caller'),
   url(r'^complete/lab/$', views.mark_as_complete_caller_lab, name='mark-caller-complete-lab'),
   url(r'^complete/lab/reviewer/$', views.mark_as_complete_reviewer_lab, name='mark-reviewer-complete-lab'),
   url(r'^reverse/caller/lab/$', views.mark_as_reverse_caller_lab, name='mark-reverse-lab-to-caller'),
   url(r'^reverse/reviewer/lab/$', views.mark_as_reverse_reviewer_lab, name='mark-reverse-lab-to-reviewer'),
   url(r'^complete/lab/publisher/$', views.mark_as_complete_publisher_lab, name='mark-complete-publisher-lab-stage-four'),


   url(r'^complete/rehab/$', views.mark_as_complete_caller_rehab, name='mark-caller-complete-rehab'),
   url(r'^complete/rehab/reviewer/$', views.mark_as_complete_reviewer_rehab, name='mark-reviewer-complete-rehab'),
   url(r'^reverse/caller/rehab/$', views.mark_as_reverse_caller_rehab, name='mark-reverse-rehab-to-caller'),
   url(r'^reverse/reviewer/rehab/$', views.mark_as_reverse_reviewer_rehab, name='mark-reverse-rehab-to-reviewer'),
   url(r'^complete/rehab/publisher/$', views.mark_as_complete_publisher_rehab, name='mark-complete-publisher-rehab-stage-four'),

   url(r'^complete/nurse_bureau/$', views.mark_as_complete_caller_nurse_bureau, name='mark-caller-complete-nurse_bureau'),
   url(r'^complete/nurse_bureau/reviewer/$', views.mark_as_complete_reviewer_nurse_bureau, name='mark-reviewer-complete-nurse_bureau'),
   url(r'^reverse/caller/nurse_bureau/$', views.mark_as_reverse_caller_nurse_bureau, name='mark-reverse-nurse_bureau-to-caller'),
   url(r'^reverse/reviewer/nurse_bureau/$', views.mark_as_reverse_reviewer_nurse_bureau, name='mark-reverse-nurse_bureau-to-reviewer'),
   url(r'^complete/nurse_bureau/publisher/$', views.mark_as_complete_publisher_nurse_bureau, name='mark-complete-publisher-nurse_bureau-stage-four'),

   url(r'^complete/dietitian/$', views.mark_as_complete_caller_dietitian, name='mark-caller-complete-dietitian'),
   url(r'^complete/dietitian/reviewer/$', views.mark_as_complete_reviewer_dietitian,name='mark-reviewer-complete-dietitian'),
   url(r'^reverse/caller/dietitian/$', views.mark_as_reverse_caller_dietitian,name='mark-reverse-dietitian-to-caller'),
   url(r'^reverse/reviewer/dietitian/$', views.mark_as_reverse_reviewer_dietitian,name='mark-reverse-dietitian-to-reviewer'),
   url(r'^complete/dietitian/publisher/$', views.mark_as_complete_publisher_dietitian,name='mark-complete-publisher-dietitian-stage-four'),

   url(r'^complete/therapist/$', views.mark_as_complete_caller_therapist, name='mark-caller-complete-therapist'),
   url(r'^complete/therapist/reviewer/$', views.mark_as_complete_reviewer_therapist,name='mark-reviewer-complete-therapist'),
   url(r'^reverse/caller/therapist/$', views.mark_as_reverse_caller_therapist,name='mark-reverse-therapist-to-caller'),
   url(r'^reverse/reviewer/therapist/$', views.mark_as_reverse_reviewer_therapist,name='mark-reverse-therapist-to-reviewer'),
   url(r'^complete/therapist/publisher/$', views.mark_as_complete_publisher_therapist,name='mark-complete-publisher-therapist-stage-four'),



   url(r'^complete/organisation/$', views.mark_as_complete_caller_organisation, name='mark-caller-organisation'),
   url(r'^complete/reviewer/$', views.mark_as_complete_reviewer, name='mark-reviewer'),
   url(r'^complete/organisation/reviewer/$', views.mark_as_complete_reviewer_organisation, name='mark-reviewer-organisation'),
   url(r'^complete/doctor/publisher/$', views.mark_as_complete_publisher, name='mark-publisher'),
   url(r'^complete/organisation/publisher/$', views.mark_as_complete_publisher_organisation, name='mark-publisher-organisation'),

   url(r'^reverse/reviewer/organisation/$', views.mark_as_reverse_reviewer_organisation, name='mark-reverse-organisation-to-reviewer'),
   #url(r'^reverse/caller/organisation/$', views.mark_as_reverse_caller_organisation, name='mark-reverse-organisation-to-caller'),
   url(r'^reverse/reviewer/doctor/$', views.mark_as_reverse_reviewer_doctor, name='mark-reverse-doctor-to-reviewer'),

   url(r'^complete/bloodbank/$', views.mark_as_complete_caller_bloodbank, name='mark-caller-complete-bloodbank'),
   url(r'^reverse/caller/bloodbank/$', views.mark_as_reverse_caller_bloodbank , name='mark-reverse-bloodbank-to-caller'),
   url(r'^reverse/reviewer/bloodbank/$', views.mark_as_reverse_reviewer_bloodbank , name='mark-reverse-bloodbank-to-reviewer'),
   url(r'^complete/bloodbank/reviewer/$', views.mark_as_complete_reviewer_bloodbank, name='mark-reviewer-complete-bloodbank'),
   url(r'^complete/bloodbank/publisher/$', views.mark_as_complete_publisher_bloodbank, name='mark-complete-publisher-bloodbank-stage-four'),

   url(r'^complete/ambulance/$', views.mark_as_complete_caller_ambulance, name='mark-caller-complete-ambulance'),
   url(r'^reverse/caller/ambulance/$', views.mark_as_reverse_caller_ambulance , name='mark-reverse-ambulance-to-caller'),
   url(r'^reverse/reviewer/ambulance/$', views.mark_as_reverse_reviewer_ambulance , name='mark-reverse-ambulance-to-reviewer'),
   url(r'^complete/ambulance/reviewer/$', views.mark_as_complete_reviewer_ambulance, name='mark-reviewer-complete-ambulance'),
   url(r'^complete/ambulance/publisher/$', views.mark_as_complete_publisher_ambulance, name='mark-complete-publisher-ambulance-stage-four'),

   url(r'^complete/pharmacy/$', views.mark_as_complete_caller_pharmacy, name='mark-caller-complete-pharmacy'),
   url(r'^reverse/caller/pharmacy/$', views.mark_as_reverse_caller_pharmacy , name='mark-reverse-pharmacy-to-caller'),
   url(r'^reverse/reviewer/pharmacy/$', views.mark_as_reverse_reviewer_pharmacy , name='mark-reverse-pharmacy-to-reviewer'),
   url(r'^complete/pharmacy/reviewer/$', views.mark_as_complete_reviewer_pharmacy, name='mark-reviewer-complete-pharmacy'),
   url(r'^complete/pharmacy/publisher/$', views.mark_as_complete_publisher_pharmacy, name='mark-complete-publisher-pharmacy-stage-four'),

   url(r'^complete/disease/$', views.mark_as_complete_caller_disease, name='mark-caller-complete-disease'),
   url(r'^reverse/caller/disease/$', views.mark_as_reverse_caller_disease , name='mark-reverse-disease-to-caller'),
   url(r'^reverse/reviewer/disease/$', views.mark_as_reverse_reviewer_disease , name='mark-reverse-disease-to-reviewer'),
   url(r'^complete/disease/reviewer/$', views.mark_as_complete_reviewer_disease, name='mark-reviewer-complete-disease'),
   url(r'^complete/disease/publisher/$', views.mark_as_complete_publisher_disease, name='mark-complete-publisher-disease-stage-four'),

   url(r'^complete/drug/$', views.mark_as_complete_caller_drug, name='mark-caller-complete-drug'),
   url(r'^reverse/caller/drug/$', views.mark_as_reverse_caller_drug , name='mark-reverse-drug-to-caller'),
   url(r'^reverse/reviewer/drug/$', views.mark_as_reverse_reviewer_drug , name='mark-reverse-drug-to-reviewer'),
   url(r'^complete/drug/reviewer/$', views.mark_as_complete_reviewer_drug, name='mark-reviewer-complete-drug'),
   url(r'^complete/drug/publisher/$', views.mark_as_complete_publisher_drug, name='mark-complete-publisher-drug-stage-four'),

   url(r'^complete/symptoms/$', views.mark_as_complete_caller_symptoms, name='mark-caller-complete-symptoms'),
   url(r'^reverse/caller/symptoms/$', views.mark_as_reverse_caller_symptoms , name='mark-reverse-symptoms-to-caller'),
   url(r'^reverse/reviewer/symptoms/$', views.mark_as_reverse_reviewer_symptoms , name='mark-reverse-symptoms-to-reviewer'),
   url(r'^complete/symptoms/reviewer/$', views.mark_as_complete_reviewer_symptoms, name='mark-reviewer-complete-symptoms'),
   url(r'^complete/symptoms/publisher/$', views.mark_as_complete_publisher_symptoms, name='mark-complete-publisher-symptoms-stage-four'),

   url(r'^complete/life-plan/$', views.mark_as_complete_caller_life_plan, name='mark-caller-complete-life-plan'),
   url(r'^reverse/caller/life-plan/$', views.mark_as_reverse_caller_life_plan , name='mark-reverse-life-plan-to-caller'),
   url(r'^reverse/reviewer/life-plan/$', views.mark_as_reverse_reviewer_life_plan , name='mark-reverse-life-plan-to-reviewer'),
   url(r'^complete/life-plan/reviewer/$', views.mark_as_complete_reviewer_life_plan, name='mark-reviewer-complete-life-plan'),
   url(r'^complete/life-plan/publisher/$', views.mark_as_complete_publisher_life_plan, name='mark-complete-publisher-life-plan-stage-four'),

   url(r'^complete/home-plan/$', views.mark_as_complete_caller_home_plan, name='mark-caller-complete-home-plan'),
   url(r'^reverse/caller/home-plan/$', views.mark_as_reverse_caller_home_plan , name='mark-reverse-home-plan-to-caller'),
   url(r'^reverse/reviewer/home-plan/$', views.mark_as_reverse_reviewer_home_plan , name='mark-reverse-home-plan-to-reviewer'),
   url(r'^complete/home-plan/reviewer/$', views.mark_as_complete_reviewer_home_plan, name='mark-reviewer-complete-home-plan'),
   url(r'^complete/home-plan/publisher/$', views.mark_as_complete_publisher_home_plan, name='mark-complete-publisher-home-plan-stage-four'),

   url(r'^complete/enterprise-plan/$', views.mark_as_complete_caller_enterprise_plan, name='mark-caller-complete-enterprise-plan'),
   url(r'^reverse/caller/enterprise-plan/$', views.mark_as_reverse_caller_enterprise_plan , name='mark-reverse-enterprise-plan-to-caller'),
   url(r'^reverse/reviewer/enterprise-plan/$', views.mark_as_reverse_reviewer_enterprise_plan , name='mark-reverse-enterprise-plan-to-reviewer'),
   url(r'^complete/enterprise-plan/reviewer/$', views.mark_as_complete_reviewer_enterprise_plan, name='mark-reviewer-complete-enterprise-plan'),
   url(r'^complete/enterprise-plan/publisher/$', views.mark_as_complete_publisher_enterprise_plan, name='mark-complete-publisher-enterprise-plan-stage-four'),

   #added by ashutosh on 22nd July
   url(r'^reverseto/anyuser/$', views_two.reverse_to_any_user, name='reverse_to_any_user'),

]


elastic_search_data_patterns =[
     #url(r'^default_search_mapping/$', data_publisher.default_mapping, name='default_mapping'),
     url(r'^demo_data_publish/$', data_publisher.demo_data_publish, name='default_mapping'),
     url(r'^publish_all_models/$', data_publisher.publish_all_models, name='publish_all_models'),
     url(r'^publish_all_models_two/$', data_publisher.publish_all_models_two, name='publish_all_models_two'),
     url(r'^publish_all_models_two/$', data_publisher.publish_all_models_two, name='publish_all_models_two'),
     url(r'^get_all_doc_elastic_ids/$', elasticsearch_client.get_all_doc_elastic_ids, name='get_all_doc_elastic_ids'),

]

special_functions = [
    url(r'^publish_live_n_old_docs_7Feb2018/$', hfu_cms.special_functions.publish_live_n_old_docs_7Feb2018, name='publish_live_n_old_docs_7Feb2018'),
    #url(r'^show-mailer/$', hfu_cms.special_functions.show_mailer, name='show_mailer'),
    url(r'^truncate/$', hfu_cms.special_functions.truncate, name='truncate'),
    url(r'^basedir/$', hfu_cms.special_functions.abasedir, name='basedir'),
    url(r'^(?P<model>[A-Za-z]+)/$', hfu_cms.special_functions.makeFirstLetterCapital, name='makeFirstLetterCapital'),
    url(r'^doctor_set_unpublish/$', hfu_cms.special_functions.doctor_set_unpublish, name='doctor_set_unpublish'),
    url(r'^organisation_set_unpublish/$', hfu_cms.special_functions.organisation_set_unpublish, name='organisation_set_unpublish'),
    url(r'^ambulance_set_unpublish/$', hfu_cms.special_functions.ambulance_set_unpublish, name='ambulance_set_unpublish'),
    url(r'^dietitian_set_unpublish/$', hfu_cms.special_functions.dietitian_set_unpublish, name='dietitian_set_unpublish'),
    url(r'^publish_locality_master/$', hfu_cms.special_functions.publish_locality_master, name='publish_locality_master'),
    url(r'^publish_speciality_master/$', hfu_cms.special_functions.publish_speciality_master, name='publish_speciality_master'),
    url(r'^unpublish_organisation_for_publisher/$', hfu_cms.special_functions.unpublish_organisation_for_publisher, name='unpublish_organisation_for_publisher'),
    url(r'^unpublish_doctor_for_publisher/$', hfu_cms.special_functions.unpublish_doctor_for_publisher, name='unpublish_doctor_for_publisher'),
    url(r'^publish_for_publisher/$', hfu_cms.special_functions.publish_for_publisher, name='publish_for_publisher'),
    url(r'^publish_SO_master/$', hfu_cms.special_functions.publish_SO_master, name='publish_SO_master'),
    url(r'^publish_SPE_master/$', hfu_cms.special_functions.publish_SPE_master, name='publish_SPE_master'),
    url(r'^disease_search_master_attach_disease_with_doctors/$', hfu_cms.special_functions.disease_search_master_attach_disease_with_doctors, name='disease_search_master_attach_disease_with_doctors'),
    url(r'^symptoms_search_master_attach_symptoms_with_doctors/$', hfu_cms.special_functions.symptoms_search_master_attach_symptoms_with_doctors, name='symptoms_search_master_attach_symptoms_with_doctors'),
    url(r'^symptoms_search_master_attach_symptoms_with_doctors_in_part/$', hfu_cms.special_functions.symptoms_search_master_attach_symptoms_with_doctors_in_part, name='symptoms_search_master_attach_symptoms_with_doctors_in_part'),
    url(r'^remove-decimal-disease-search-master/$', hfu_cms.special_functions.rem_decimal_disease_search_master, name='rem_decimal_disease_search_master'),
    url(r'^remove-decimal-symptoms-search-master/$', hfu_cms.special_functions.rem_decimal_symptoms_search_master, name='rem_decimal_symptoms_search_master'),
    url(r'^publish-diease-search-master/$', hfu_cms.special_functions.publish_diease_search_master, name='publish_diease_search_master'),
    url(r'^publish-symptom-search-master/$', hfu_cms.special_functions.publish_symptom_search_master, name='publish_symptom_search_master'),

    url(r'^test-disease-user-change/$', hfu_cms.special_functions.test_disease_user_change, name='test_disease_user_change'),
    url(r'^assign-all-disease-to mrinalini/$', hfu_cms.special_functions.assign_all_disease_to_mrinalini, name='assign_all_disease_to_mrinalini'),
    url(r'^copy-department-associate-to-attach/$', hfu_cms.special_functions.copy_department_associate_to_attach, name='copy_department_associate_to_attach'),
    #url(r'^unpublish-live-docs/$', hfu_cms.special_functions.unpublish_live_docs, name='unpublish_live_docs'),
    url(r'^to-del-del/$', hfu_cms.special_functions.to_del_del, name='to_del_del'),
    url(r'^copy_Speciality/$', hfu_cms.special_functions.copy_Speciality, name='copy_Speciality'),
    url(r'^copy_serviceoffered/$', hfu_cms.special_functions.copy_serviceoffered, name='copy_serviceoffered'),
    #url(r'^copy_serviceoffered_7872/$', hfu_cms.special_functions.copy_serviceoffered_7872, name='copy_serviceoffered_7872'),
    url(r'^publish-for-ashutosh/$', hfu_cms.special_functions.publish_for_ashutosh, name='publish_for_ashutosh'),
    #url(r'^temp-doctor-derviceoffered-new/$', hfu_cms.special_functions.temp_doctor_derviceoffered_new, name='temp_doctor_derviceoffered_new'),

    url(r'^emptyspeinDocCatSOSpecialityAssociationFinalfor7cats/$', hfu_cms.special_functions.empty_spe_in_Doc_Cat_SO_Speciality_Association_Final_for7cats, name='empty_spe_in_Doc_Cat_SO_Speciality_Association_Final_for7cats'),
    url(r'^emptydoctorsnewspecialityfinalfor7cats/$', hfu_cms.special_functions.empty_doctors_new_speciality_final_for7cats, name='empty_doctors_new_speciality_final_for7cats'),
    url(r'^publish_3_masters/$', hfu_cms.special_functions.publish_3_masters, name='publish_3_masters'),
    url(r'^org_update_lat_long/$', hfu_cms.special_functions.org_update_lat_long, name='org_update_lat_long'),

]


questions =[

    url(r'^listing/$', views.questions_listing, name='questions_listing'),
    url(r'^associate-live-doctor-with-question/(?P<question_id>[0-9]+)/$', views.associate_live_doc_with_question, name='associate_live_doc_with_question'),
]

feedback =[

    url(r'^listing/$', views.feedback_listing, name='feedback_listing'),
    url(r'^approve-feedback/(?P<feedback_id>[0-9]+)/$', views.approve_feedback, name='approve_feedback'),
    url(r'^disapprove-feedback/(?P<feedback_id>[0-9]+)/$', views.disapprove_feedback, name='disapprove_feedback'),
]


global_search=[

    url(r'^lab/(?P<lab_id>[0-9]+)/$', views.lab_global_search, name='lab-global-search'),
    url(r'^organisation/(?P<organisation_id>[0-9]+)/$', views.organisation_global_search, name='organisation-global-search'),
    url(r'^verify/(?P<doctor_id>[0-9]+)/$', views.doctor_global_search_verify,name='doctor-global-search-verify'),
    url(r'^attach/(?P<doctor_id>[0-9]+)/$', views.doctor_global_search_attach,name='doctor-global-search-attach'),
    url(r'^education/(?P<doctor_id>[0-9]+)/$', views.doctor_global_search_education,name='doctor-global-search-education'),
    url(r'^reward/(?P<doctor_id>[0-9]+)/$', views.doctor_global_search_reward, name='doctor-global-search-reward'),
    url(r'^doctor/(?P<doctor_id>[0-9]+)/$', views.doctor_global_search, name='doctor-global-search'),
    url(r'^pharmacy/(?P<pharmacy_id>[0-9]+)/$', views.pharmacy_global_search, name='pharmacy-global-search'),
    url(r'^rehab/(?P<rehab_id>[0-9]+)/$', views.rehab_global_search, name='rehab-global-search'),
    url(r'^ambulance/(?P<ambulance_id>[0-9]+)/$', views.ambulance_global_search, name='ambulance-global-search'),
    url(r'^therapist/(?P<therapist_id>[0-9]+)/$', views.therapist_global_search, name='therapist-global-search'),
    url(r'^nurse_bureau/(?P<nurse_bureau_id>[0-9]+)/$', views.nurse_bureau_global_search, name='nurse-bureau-global-search'),
    url(r'^dietitian/(?P<dietitian_id>[0-9]+)/$', views.dietitian_global_search, name='dietitian_global_search'),
    url(r'^bloodbank/(?P<bloodbank_id>[0-9]+)/$', views.bloodbank_global_search, name='bloodbank_global_search'),
    url(r'^verified-fields/(?P<bloodbank_id>[0-9]+)/$', views.gs_bloodbank_verified_fields,name='gs_bloodbank_verified_fields'),
    url(r'^live-doctor/(?P<doctor_id>[0-9]+)/$', views_two.liveDoctor_global_search, name='liveDoctor_global_search'),
]
urlpatterns = [
    url(r'^global_search/',include(global_search)),
    url(r'^occupied-ranks/update/$',views_two.update_occupied_ranks, name='update_occupied_ranks'),
    url(r'^doctor-occupied-ranks/update/$',views_two.update_doctor_occupied_ranks, name='update_occupied_ranks'),
    url(r'^notification/',include(notification_manage_urlpattern)),
    url(r'^news-feed/', include('news.urls')),
    url(r'^special-functions/', include(special_functions)),
    url(r'^questions/', include(questions)),
    url(r'^feedback/', include(feedback)),
    url(r'^service/', include('providers.urls')),
    url(r'^', include(login_urlpatterns)),
    url(r'^search/', include(search_urlpatterns)),
    url(r'^', include(user_manage_urlpatterns)),
    url(r'^mark/', include(mark_as_urlpatterns)),
    url(r'^publisher/', include(publisher_urlpatterns)),
    url(r'^', include(push_data_urlpatterns)),
    url(r'^master/', include(master_data_manage_urlpatterns)),
    url(r'^doctor/', include(doctor_manage_urlpatterns)),
    url(r'^live-doctor/', include(live_doctor_manage_urlpatterns)),
    url(r'^organisation/', include(organisation_manage_urlpatterns)),
    url(r'^live_organisation/', include(live_organisation_manage_urlpatterns)),
    url(r'^app/', include(elastic_search_data_patterns)),
    url(r'^lab/', include(lab_manage_urlpatterns)),
    url(r'^blood-bank/', include(blood_bank_manage_urlpatterns)),
    url(r'^pharmacy/', include(pharmacy_manage_urlpatterns)),
    url(r'^disease/', include(disease_manage_urlpatterns)),
    url(r'^drug/', include(drug_manage_urlpatterns)),
    url(r'^symptoms/', include(symptoms_manage_urlpatterns)),
    url(r'^ambulance/', include(ambulance_manage_urlpatterns)),
    url(r'^rehab/', include(rehab_manage_urlpatterns)),
    url(r'^nurse_bureau/', include(nurse_bureau_manage_urlpatterns)),
    url(r'^dietitian/', include(dietitian_manage_urlpatterns)),
    url(r'^therapist/', include(therapist_manage_urlpatterns)),
    url(r'^delete/', include(delete_data_urlpatterns)),
    url(r'^edit/', include(edit_doctor_data_urlpatterns)),
    url(r'^admin/activate/', include(enable_disable_urlpatterns)),
    url(r'^admin/', admin.site.urls),

    url(r'^state_vise_city_data/$', views.state_vise_city_data, name='state_vise_city_data'),

    url(r'^get-cities-list/$', views_two.get_cities_list, name='get_cities_list'),
    url(r'^get_city/$', views.get_city, name='get_city'),
    url(r'^get_city_byname/$', views.get_city_byname, name='get_city'),
    url(r'^get_location/$', views.get_location, name='get_location'),
    url(r'^get_location_byname/$', views.get_location_byname, name='get_location_byname'),
    url(r'^get_organisatin_byname/$', views.get_organisatin_byname, name='get_organisatin_byname'),
    url(r'^get_org_locality_and_stg4or5/$', views.get_org_locality_and_stg4or5, name='get_org_locality_and_stg4or5'),
    url(r'^get/user/$', views.get_users_stage, name='get_users'),
    url(r'^assign/doctor/$', views.assign, name='assign-doctor'),
    url(r'^assign/live-doctor/$', views.assign_live_doctor, name='assign-live-doctor'),
    url(r'^assign/organisation/$', views.assign_organisation, name='assign-organisation'),
    url(r'^assign/lab/$', views.assign_lab, name='assign-lab'),
    url(r'^assign/rehab/$', views.assign_rehab, name='assign-rehab'),
    url(r'^assign/nurse_bureau/$', views.assign_nurse_bureau, name='assign-nurse_bureau'),
    url(r'^assign/dietitian/$', views.assign_dietitian, name='assign-dietitian'),
    url(r'^assign/therapist/$', views.assign_therapist, name='assign-therapist'),
    url(r'^assign/jitendra/$', views.update, name='jitendra'),
    url(r'^assign/bloodbank/$', views.assign_bloodbank, name='assign-bloodbank'),
    url(r'^assign/ambulance/$', views.assign_ambulance, name='assign-ambulance'),
    url(r'^assign/pharmacy/$', views.assign_pharmacy, name='assign-pharmacy'),
    url(r'^assign/disease/$', views.assign_disease, name='assign-disease'),
    url(r'^assign/drug/$', views.assign_drug, name='assign-drug'),
    url(r'^get/csv/doctor/$', hfu_cms.excel.get_data, name='excel-doctor'),
    url(r'^get/csv/organisation/$', hfu_cms.excel.get_data_org, name='excel-organisation'),
    url(r'^get/csv/docs_attached_with_orgs/$', hfu_cms.excel.get_docs_attached_with_orgs, name='get_docs_attached_with_orgs'),
    url(r'^get/csv/docs_sch_missin_endtime/$', hfu_cms.excel.docs_sch_missin_endtime, name='docs_sch_missin_endtime'),
    url(r'^get/csv/org-without-attached-docs/$', hfu_cms.excel.org_without_attached_docs, name='org_without_attached_docs'),
    url(r'^get/csv/org-without-attached-docs/$', hfu_cms.excel.org_without_attached_docs, name='org_without_attached_docs'),
    url(r'^get/csv/org-without-emails/$', hfu_cms.excel.org_without_emails, name='org_without_emails'),
    url(r'^get/csv/org-category-ayurveda/$', hfu_cms.excel.org_category_ayurveda, name='org_category_ayurveda'),
    url(r'^get/csv/published-doc-mumbai/$', hfu_cms.excel.published_doc_mumbai, name='published_doc_mumbai'),
    url(r'^get/csv/orgs-without-attached-docs/$', hfu_cms.excel.orgs_without_attached_docs, name='orgs_without_attached_docs'),
    url(r'^get/csv/all-orgs-limited-field-export/$', hfu_cms.excel.all_orgs_limited_field_export, name='all_orgs_limited_field_export'),
    url(r'^get/csv/all-labs-limited-field-export/$', hfu_cms.excel.all_labs_limited_field_export, name='all_labs_limited_field_export'),
    url(r'^get/csv/attach-with-doctor-export/$', hfu_cms.excel.attach_with_doctor_export, name='attach_with_doctor_export'),
    url(r'^get/csv/doc-edit-missing-combination/$', hfu_cms.excel.doc_edit_missing_combination, name='doc_edit_missing_combination'),
    url(r'^get/csv/Jodhpur-attached-organisations/$', hfu_cms.excel.Jodhpur_attached_organisations, name='Jodhpur_attached_organisations'),
    url(r'^get/csv/Pune-doctors/$', hfu_cms.excel.Pune_doctors, name='Pune_doctors'),
    url(r'^get/csv/Ahmedabad-doctors/$', hfu_cms.excel.Ahmedabad_doctors, name='Ahmedabad_doctors'),
    url(r'^get/csv/Mumbai-All-doctors/$', hfu_cms.excel.Mumbai_All_doctors, name='Mumbai_All_doctors'),
    url(r'^get/csv/new-speciality-master/$', hfu_cms.excel.new_speciality_export, name='new_speciality_export'),
    url(r'^get/csv/new-serviceoffered-master/$', hfu_cms.excel.new_serviceoffered_export,      name='new_serviceoffered_export'),
    #url(r'^get/csv/cats-mapto_newunique_so_mastervalues/$', hfu_cms.excel.cats_mappedto_newunique_serviceoffered_mastervalues,      name='cats_mappedto_newunique_serviceoffered_mastervalues'),
    #url(r'^get/csv/new-serviceoffered-master-7872/$', hfu_cms.excel.new_serviceoffered_export_7872,  name='new_serviceoffered_export_7872'),
    url(r'^get/csv/all-so-all-docs-15June/$', hfu_cms.excel.all_so_all_docs_15June,  name='all_so_all_docs_15June'),
    url(r'^get/csv/all-Mumbai-docs-with-email/$', hfu_cms.excel.all_Mumbai_docs_with_email,  name='all_Mumbai_docs_with_email'),
    url(r'^get/csv/docs_export/$', hfu_cms.excel.docs_export,  name='docs_export'),
    url(r'^get/csv/live_doctor_export/$', hfu_cms.excel.live_doctor_export,  name='live_doctor_export'),
    url(r'^get/csv/all_orgs_lat_long/$', hfu_cms.excel.all_orgs_lat_long,  name='all_orgs_lat_long'),
    url(r'^get/csv/orgs_lat_long_pre_filled/$', hfu_cms.excel.orgs_lat_long_pre_filled,  name='orgs_lat_long_pre_filled'),
    url(r'^get/csv/orgs_with_lat_AND_OR_long_OR_BOTH_missing/$', hfu_cms.excel.orgs_with_lat_AND_OR_long_OR_BOTH_missing,  name='orgs_with_lat_AND_OR_long_OR_BOTH_missing'),
    url(r'^get/csv/Doctor_rank_extract/$', hfu_cms.excel.Doctor_rank_extract,  name='Doctor_rank_extract'),
    #url(r'^get/csv/published-live-doc-mumbai/$', hfu_cms.excel.published_live_doc_mumbai, name='published_live_doc_mumbai'),


    url(r'^assign/symptoms/$', views.assign_symptoms, name='assign-symptoms'),
    #url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('remote.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


