from django.contrib import admin
from models import *
from hfu_cms.models import *
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from django.contrib.auth.models import User

# Register your models here.
# admin.site.register(Zone)
# admin.site.register(ZoneLocation)
#admin.site.register(Category)
#admin.site.register(Speciality)
#admin.site.register(Service_Offred)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
#admin.site.register(Locality)
admin.site.register(ValidateByChoice)


# AttachWithDoctor

class AttachWithDoctorResource(resources.ModelResource):
    class Meta:
        model = AttachWithDoctor
        fields = ('doctor__name', 'organisation__name')


class AttachWithDoctorAdmin(ImportExportModelAdmin):
    resource_class = AttachWithDoctorResource
    pass


# AssociateDoctorWithOrganization


class AssociateDoctorWithOrganizationResource(resources.ModelResource):
    # doctor = fields.Field(column_name='doctor', attribute='doctor', widget=ForeignKeyWidget(Doctor, 'name'))

    class Meta:
        model = AssociateDoctorWithOrganization
        fields = ('department__name','doctor__name', 'organisation__name')


class AssociateDoctorWithOrganizationAdmin(ImportExportModelAdmin):
    resources_class = AssociateDoctorWithOrganizationResource
    fields = ('department__name','doctor__name', 'organisation__name')
    # fields = ['doctor', 'organisation']
    pass


# Adding import export for doctor and organisation

class DoctorResource(resources.ModelResource):
    # current_user = fields.Field(column_name='current_user', attribute='current_user', widget=ForeignKeyWidget(User,'username'))
    class Meta:
        model = Doctor
        fields = ('resource_validate', 'stage__stage_name','current_user__username','previous_user','free_text','unique_id','name','image_url', 'category__name','zone__name','zone_location__name','speciality', 'service_offered','dob','mobile_no','phone','skype_id','email','secondary_email','doctor_experience_year','qualification_data','registration_data','is_disable','male_doctor','female_doctor','publish','is_emergency',
                  'emergency_fee','country__name','state__name','city__name','localities')


class DoctorAdmin(ImportExportModelAdmin):
    resource_class = DoctorResource
    fields = ['resource_validate__name', 'stage__stage_name','current_user__username','previous_user','free_text','unique_id','name','image_url', 'category__name','zone__name','zone_location__name','speciality', 'service_offered','dob','mobile_no','phone','skype_id','email','secondary_email','doctor_experience_year','qualification_data','registration_data','is_disable','male_doctor','female_doctor','publish'
    ,'is_emergency','emergency_fee','country__name','state__name','city__name','localities']
    search_fields = ['name']
    pass

# class OrganisationResource(resources.ModelResource):
#     class Meta:
#         model = OrganisationName
#         fields = ('resource_validate', 'stage','current_user','facility','previous_user','free_text','name','is_hospital','is_clinic','street','locality','city','state','country','pincode','phone','mobile_no','fax','email','emergency_no','website','department','niche_department','doctors_on_board','broucher','category','type','ambulance_service','trauma_center','burn_center',
#                   'ambulance_service_no','year_of_establishment ','package','latitude','longitude','schedule_data','publish','is_disable','other_facility','no_of_beds','is_emergency')
#
#
# class OrganisationAdmin(ImportExportModelAdmin):
#     resource_class = OrganisationResource
#     fields = ['resource_validate', 'stage','current_user','facility','previous_user','free_text','name','is_hospital','is_clinic','street','locality','city','state','country','pincode','phone','mobile_no','fax','email','emergency_no','website','department','niche_department','doctors_on_board','broucher','category','type','ambulance_service','trauma_center','burn_center',
#                   'ambulance_service_no','year_of_establishment ','package','latitude','longitude','schedule_data','publish','is_disable','other_facility','no_of_beds','is_emergency']
#
#     search_fields = ['name']
#     pass

class OrganisationResource(resources.ModelResource):
    class Meta:
        model = OrganisationName
        fields = ('id','did','extension')


class OrganisationAdmin(ImportExportModelAdmin):
    resource_class = OrganisationResource
    fields = ['did','extension']
    Search_fields = ['did']
    pass



class ZoneResource(resources.ModelResource):
    class Meta:
        model = Zone
        # fields = ['doctor', 'telecaller', 'reviewer']
        fields = ('id', 'name','delete')


class ZoneAdmin(ImportExportModelAdmin):
    resource_class = ZoneResource
    fields = ['name']
    search_fields = ['name']
    pass



class ZoneLocationResource(resources.ModelResource):
    class Meta:
        model = ZoneLocation
        fields = ('id', 'name', 'zone','delete')


class ZoneLocationAdmin(ImportExportModelAdmin):
    fields = ['name', 'zone']
    resource_class = ZoneLocationResource
    list_display = ('name', 'zone')
    search_fields = ['name']
    list_filter = ['zone__name']
    pass



#------------- By Nishank ----------------


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        # fields = ['doctor', 'telecaller', 'reviewer']
        fields = ('id', 'name','delete')


class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource
    fields = ['name']
    search_fields = ['name']
    pass

class SpecialityResource(resources.ModelResource):
    class Meta:
        model = Speciality
        # fields = ['doctor', 'telecaller', 'reviewer']
        fields = ('id', 'name','delete','approve','category')


class SpecialityAdmin(ImportExportModelAdmin):
    resource_class = SpecialityResource
    fields = ['name']
    search_fields = ['name']
    pass


class Service_OffredResource(resources.ModelResource):
    class Meta:
        model = Service_Offred
        # fields = ['doctor', 'telecaller', 'reviewer']
        fields = ('id', 'name','delete','approve','category')


class Service_OffredAdmin(ImportExportModelAdmin):
    resource_class = Service_OffredResource
    fields = ['name']
    search_fields = ['name']
    pass

class BloodBankResource(resources.ModelResource):
    # current_user = fields.Field(column_name='current_user', attribute='current_user', widget=ForeignKeyWidget(User,'username'))



    locality = fields.Field(
        column_name='locality_id',
        attribute='locality',
        widget=ForeignKeyWidget(Locality, 'id'))

    city= fields.Field(
        column_name='city_id',
        attribute='city',
        widget=ForeignKeyWidget(City, 'id'))

    state = fields.Field(
        column_name='state_id',
        attribute='state',
        widget=ForeignKeyWidget(State, 'id'))

    country = fields.Field(
        column_name='country_id',
        attribute='country',
        widget=ForeignKeyWidget(Country, 'id'))

    current_user = fields.Field(
        column_name='current_user_id',
        attribute='current_user',
        widget=ForeignKeyWidget(User, 'id'))

    stage = fields.Field(
        column_name='stage_id',
        attribute='stage',
        widget=ForeignKeyWidget(Stage, 'id'))

    class Meta:
        model = BloodBank
        #fields = ('id','name','license','address_1','address_2','locality_id','city_id','state_id','pincode','telephone','mobile','services','blood_bank_doctor','country_id','stage_id','current_user_id')
        fields = (
        'name', 'license', 'address_1', 'address_2', 'locality', 'city', 'state', 'pincode', 'telephone','telephone_2','telephone_3',
        'mobile', 'services', 'blood_bank_doctor', 'country', 'stage', 'current_user','education','stars', 'is_disable','timings','is_emergency','pricing','publish'
        )


class BloodBankAdmin(ImportExportModelAdmin):
    resource_class = BloodBankResource

    #fields = ['id','name','license','address_1','address_2','locality_id','city_id','state_id','pincode','telephone','mobile','services','blood_bank_doctor','country_id','stage_id','current_user_id']
    fields = ['name', 'license', 'address_1', 'address_2', 'locality', 'city', 'state', 'pincode', 'telephone','telephone_2','telephone_3',
        'mobile', 'services', 'blood_bank_doctor', 'country', 'stage', 'current_user','education','stars', 'is_disable','timings','is_emergency','pricing','publish']
    search_fields = ['name']
    pass



#---------------

#------------- By Nishank ----------------
#
class RehabCenterResource(resources.ModelResource):
    # current_user = fields.Field(column_name='current_user', attribute='current_user', widget=ForeignKeyWidget(User,'username'))

    locality = fields.Field(
        column_name='locality_id',
        attribute='locality',
        widget=ForeignKeyWidget(Locality, 'id'))

    city= fields.Field(
        column_name='city_id',
        attribute='city',
        widget=ForeignKeyWidget(City, 'id'))

    state = fields.Field(
        column_name='state_id',
        attribute='state',
        widget=ForeignKeyWidget(State, 'id'))

    country = fields.Field(
        column_name='country_id',
        attribute='country',
        widget=ForeignKeyWidget(Country, 'id'))

    current_user = fields.Field(
        column_name='current_user_id',
        attribute='current_user',
        widget=ForeignKeyWidget(User, 'id'))

    stage = fields.Field(
        column_name='stage_id',
        attribute='stage',
        widget=ForeignKeyWidget(Stage, 'id'))

    class Meta:
        model = RehabCenter
        fields = ('id', 'clinic_name', 'address', 'locality_id', 'city_id', 'pincode', 'state_id', 'country_id','telephone', 'email', 'website', 'doctor_name', 'current_user', 'stage_id')



class RehabCenterAdmin(ImportExportModelAdmin):
    resource_class = RehabCenterResource

    fields = ['id', 'clinic_name', 'address', 'locality_id', 'city_id', 'pincode', 'state_id', 'country_id','telephone', 'email', 'website', 'doctor_name', 'current_user', 'stage_id']
    search_fields = ['name']
    pass


class Disease_search_masterResource(resources.ModelResource):
    class Meta:
        model = Disease_search_master
        fields = ('id','name','doctor_categories')

class Disease_search_masterAdmin(ImportExportModelAdmin):
    resource_class = Disease_search_masterResource
    fields = ['id','name','doctor_categories']
    search_fields = ['name']
    pass



class Symptoms_search_masterResource(resources.ModelResource):
    class Meta:
        model = Symptoms_search_master
        fields = ('id','name','doctor_categories')

class Symptoms_search_masterAdmin(ImportExportModelAdmin):
    resource_class = Symptoms_search_masterResource
    fields = ['id','name','doctor_categories']
    search_fields = ['name']
    pass


#---------------





# class LabsResource(resources.ModelResource):
#     # current_user = fields.Field(column_name='current_user', attribute='current_user', widget=ForeignKeyWidget(User,'username'))
#
#     locality = fields.Field(
#         column_name='locality_id',
#         attribute='locality',
#         widget=ForeignKeyWidget(Locality, 'id'))
#
#     city = fields.Field(
#         column_name='city_id',
#         attribute='city',
#         widget=ForeignKeyWidget(City, 'id'))
#
#     state = fields.Field(
#         column_name='state_id',
#         attribute='state',
#         widget=ForeignKeyWidget(State, 'id'))
#
#     country = fields.Field(
#         column_name='country_id',
#         attribute='country',
#         widget=ForeignKeyWidget(Country, 'id'))
#
#     class Meta:
#         model = Labs
#         fields = ('id','name','address','locality_id','city_id','pincode','state_id','telephone','pathology_email','country_id',
#                   'lab_collection_timing','ratings','pathology_doctor_name','authorization_body','home_sample_collection',
#                   'lab_doctors_on_board','lab_authorised_person_name','lab_authorised_person_designation','lab_authorised_person_contact_no',
#                   'lab_authorised_person_emailid','lab_emailid','lab_website','lab_type','lab_locality_coverage_from','lab_locality_coverage_to',
#                   'is_emergency','lab_accreditation_body','lab_mobile','lab_services','lab_schedule','lab_departments','publish')
#
#
#
# class LabsAdmin(ImportExportModelAdmin):
#     resource_class =LabsResource
#
#     fields = ['id','name','address','locality_id','city_id','pincode','state_id','telephone','pathology_email','country_id',
#                   'lab_collection_timing','ratings','pathology_doctor_name','authorization_body','home_sample_collection',
#                   'lab_doctors_on_board','lab_authorised_person_name','lab_authorised_person_designation','lab_authorised_person_contact_no',
#                   'lab_authorised_person_emailid','lab_emailid','lab_website','lab_type','lab_locality_coverage_from','lab_locality_coverage_to',
#                   'is_emergency','lab_accreditation_body','lab_mobile','lab_services','lab_schedule','lab_departments','publish' ]
#     search_fields = ['name']
#     pass


class LabsResource(resources.ModelResource):

    class Meta:
        model = Labs
        fields = ('id','did','extension')



class LabsAdmin(ImportExportModelAdmin):
    resource_class =LabsResource
    fields = ['did','extension' ]
    search_fields = ['did']
    pass



class AmbulanceResource(resources.ModelResource):
    # current_user = fields.Field(column_name='current_user', attribute='current_user', widget=ForeignKeyWidget(User,'username'))

    locality = fields.Field(
        column_name='locality_id',
        attribute='locality',
        widget=ForeignKeyWidget(Locality, 'id'))

    city = fields.Field(
        column_name='city_id',
        attribute='city',
        widget=ForeignKeyWidget(City, 'id'))

    state = fields.Field(
        column_name='state_id',
        attribute='state',
        widget=ForeignKeyWidget(State, 'id'))

    country = fields.Field(
        column_name='country_id',
        attribute='country',
        widget=ForeignKeyWidget(Country, 'id'))

    stage = fields.Field(
        column_name='stage_id',
        attribute='stage',
        widget=ForeignKeyWidget(Stage, 'id'))

    current_user = fields.Field(
        column_name='current_user_id',
        attribute='current_user',
        widget=ForeignKeyWidget(User, 'id'))

    class Meta:
        model = Ambulance
        # fields = ('id','name','address','locality_id','city_id','state_id','country_id',
        #           'pincode','telephone','mobile','stage_id','current_user_id')
        fields = ( 'name', 'address', 'locality', 'city', 'state', 'country',
                  'pincode', 'telephone', 'mobile', 'stage', 'current_user')


class AmbulanceAdmin(ImportExportModelAdmin):
    resource_class = AmbulanceResource
    # fields = ['id','name','address','locality_id','city_id','state_id','country_id',
    #               'pincode','telephone','mobile','stage_id','current_user_id']

    fields =[ 'name', 'address', 'locality', 'city', 'state', 'country',
    'pincode', 'telephone', 'mobile', 'stage', 'current_user']
    search_fields = ['name']
    pass


#
class Nurse_Bureau_Resource(resources.ModelResource):
    # current_user = fields.Field(column_name='current_user', attribute='current_user', widget=ForeignKeyWidget(User,'username'))

    locality = fields.Field(
        column_name='locality_id',
        attribute='locality',
        widget=ForeignKeyWidget(Locality, 'id'))

    city = fields.Field(
        column_name='city_id',
        attribute='city',
        widget=ForeignKeyWidget(City, 'id'))

    state = fields.Field(
        column_name='state_id',
        attribute='state',
        widget=ForeignKeyWidget(State, 'id'))

    country = fields.Field(
        column_name='country_id',
        attribute='country',
        widget=ForeignKeyWidget(Country, 'id'))

    stage = fields.Field(
        column_name='stage_id',
        attribute='stage',
        widget=ForeignKeyWidget(Stage, 'id'))

    current_user = fields.Field(
        column_name='current_user_id',
        attribute='current_user',
        widget=ForeignKeyWidget(User, 'id'))

    class Meta:
        model = Nurse_Bureau
        fields = ('id','name','address','locality_id','city_id','pincode','state_id','country_id','current_user_id','stage_id','telephone','email','rates','remarks','website')
        # fields = ( 'id','name', 'address', 'locality', 'city', 'state', 'country',
        #           'pincode', 'telephone', 'mobile', 'stage', 'current_user')


class Nurse_BureauAdmin(ImportExportModelAdmin):
    resource_class = Nurse_Bureau_Resource

    fields = ['id','name','address','locality_id','city_id','pincode','state_id','country_id','current_user_id','stage_id','telephone','email','rates','remarks','website']
    search_fields = ['name']
    pass

#


# class DiseaseResource(resources.ModelResource):
#     # current_user = fields.Field(column_name='current_user', attribute='current_user', widget=ForeignKeyWidget(User,'username'))
#     class Meta:
#         model = Disease
#         fields = ('resource_validate','topic_title','related_topics','tag_string','image','image_url','article_body_description','article_body_cause',
#                   'article_body_symptoms','article_body_test_n_diagnosis','article_body_treatment','article_body_prevention','link_article_with',
#                   'stage','current_user','previous_user','is_disable','free_text')
#
#
# class DiseaseAdmin(ImportExportModelAdmin):
#     resource_class = DiseaseResource
#     fields = ['resource_validate','topic_title','related_topics','tag_string','image','image_url','article_body_description','article_body_cause',
#                   'article_body_symptoms','article_body_test_n_diagnosis','article_body_treatment','article_body_prevention','link_article_with',
#                   'stage','current_user','previous_user','is_disable','free_text']
#     search_fields = ['topic_title']
#     pass


class DiseaseResource(resources.ModelResource):
    # current_user = fields.Field(column_name='current_user', attribute='current_user', widget=ForeignKeyWidget(User,'username'))
    class Meta:
        model = Disease
        fields = ('tag_string','free_text')


class DiseaseAdmin(ImportExportModelAdmin):
    resource_class = DiseaseResource
    fields = ['tag_string','free_text']
    search_fields = ['topic_title','free_text']
    pass



class SymptomsResource(resources.ModelResource):
    # current_user = fields.Field(column_name='current_user', attribute='current_user', widget=ForeignKeyWidget(User,'username'))
    class Meta:
        model = Symptoms
        fields = ('resource_validate','topic_title','tag_string','image','image_url','article_body_description','article_body_cause',
                  'article_body_self_care','stage','current_user','previous_user','is_disable','free_text')


class SymptomsAdmin(ImportExportModelAdmin):
    resource_class = SymptomsResource
    fields = ['resource_validate','topic_title','tag_string','image','image_url','article_body_description','article_body_cause',
                  'article_body_self_care','stage','current_user','previous_user','is_disable','free_text']
    search_fields = ['topic_title']
    pass


class DrugResource(resources.ModelResource):
    # current_user = fields.Field(column_name='current_user', attribute='current_user', widget=ForeignKeyWidget(User,'username'))
    class Meta:
        model = Drug
        fields = ('resource_validate','name','generic_name','brand_name','manufacturer_name','composition','form_n_rate',
                  'dosage','mode_of_administration','indication','overdose','contraindication','special_precaution',
                  'adverse_drug_reactions','drug_interaction','lab_interference','mechanism_of_action','drug_class',
                  'atc_classification','schedule_classification',
                  'stage','current_user','previous_user','is_disable','free_text')


class DrugAdmin(ImportExportModelAdmin):
    resource_class = DrugResource
    fields = ['resource_validate','name','generic_name','brand_name','manufacturer_name','composition','form_n_rate',
                  'dosage','mode_of_administration','indication','overdose','contraindication','special_precaution',
                  'adverse_drug_reactions','drug_interaction','lab_interference','mechanism_of_action','drug_class',
                  'atc_classification','schedule_classification',
                  'stage','current_user','previous_user','is_disable','free_text']
    search_fields = ['topic_title']
    pass


class Disease_Category_search_mapping_Resource(resources.ModelResource):
    class Meta:
        model = Disease_Category_search_mapping
        fields = ('id','hfy','categories','disease_name_translation','disease_name_transliteration')


class Disease_Category_search_mapping_Admin(ImportExportModelAdmin):
    resource_class = Disease_Category_search_mapping_Resource
    fields = ['id','disease_name','categories','disease_name_translation','disease_name_transliteration']
    search_fields = ['disease_name']
    pass


class MedicalPharmacyStore_Resource(resources.ModelResource):

    locality = fields.Field(
        column_name='locality_id',
        attribute='locality',
        widget=ForeignKeyWidget(Locality, 'id'))

    city = fields.Field(
        column_name='city_id',
        attribute='city',
        widget=ForeignKeyWidget(City, 'id'))

    state = fields.Field(
        column_name='state_id',
        attribute='state',
        widget=ForeignKeyWidget(State, 'id'))

    country = fields.Field(
        column_name='country_id',
        attribute='country',
        widget=ForeignKeyWidget(Country, 'id'))

    stage = fields.Field(
        column_name='stage_id',
        attribute='stage',
        widget=ForeignKeyWidget(Stage, 'id'))

    current_user = fields.Field(
        column_name='current_user_id',
        attribute='current_user',
        widget=ForeignKeyWidget(User, 'id'))


    class Meta:
        model = MedicalPharmacyStore
        fields=('id','name','address','locality_id','city_id','pincode','state_id','country_id','contact_person','telephone','email','fax','website','stage_id','current_user_id','type','services','timings','is_disable','is_emergency','publish')



class MedicalPharmacyStore_Admin(ImportExportModelAdmin):
    resource_class = MedicalPharmacyStore_Resource

    fields =['id','name','address','locality_id','city_id','pincode','state_id','country_id','contact_person','telephone','email','fax','website','stage_id','current_user_id','type','services','timings','is_disable','is_emergency','publish']
    search_fields = ['name']
    pass


class Ambulance_type_master_Resource(resources.ModelResource):
    class Meta:
        model = Ambulance_type_master



class Ambulance_type_master_Admin(ImportExportModelAdmin):
    resource_class = Ambulance_type_master_Resource

    search_fields = ['name']
    pass

class AmbulanceServices_Resource(resources.ModelResource):
    class Meta:
        model = AmbulanceServices



class AmbulanceServices_Admin(ImportExportModelAdmin):
    resource_class = AmbulanceServices_Resource

    search_fields = ['name']
    pass






class DietitianResource(resources.ModelResource):
    # current_user = fields.Field(column_name='current_user', attribute='current_user', widget=ForeignKeyWidget(User,'username'))

    locality = fields.Field(
        column_name='locality_id',
        attribute='locality',
        widget=ForeignKeyWidget(Locality, 'id'))

    city= fields.Field(
        column_name='city_id',
        attribute='city',
        widget=ForeignKeyWidget(City, 'id'))

    state = fields.Field(
        column_name='state_id',
        attribute='state',
        widget=ForeignKeyWidget(State, 'id'))

    country = fields.Field(
        column_name='country_id',
        attribute='country',
        widget=ForeignKeyWidget(Country, 'id'))

    current_user = fields.Field(
        column_name='current_user_id',
        attribute='current_user',
        widget=ForeignKeyWidget(User, 'id'))

    stage = fields.Field(
        column_name='stage_id',
        attribute='stage',
        widget=ForeignKeyWidget(Stage, 'id'))

    class Meta:
        model = Dietitian
        fields = ('id','name','institution','qualification', 'experience','type','services','dietitian_locality_coverage_from_id','dietitian_locality_coverage_to_id', 'rates', 'address', 'locality_id', 'city_id','pincode', 'state_id', 'country_id', 'stage_id', 'current_user_id', 'email', 'telephone', 'alternate_telephone', 'remarks','mobile','is_disable','publish')



class DietitianAdmin(ImportExportModelAdmin):
    resource_class = DietitianResource

    fields = ['id','name','institution','qualification', 'experience','type','services','dietitian_locality_coverage_from_id','dietitian_locality_coverage_to_id', 'rates', 'address', 'locality_id', 'city_id','pincode', 'state_id', 'country_id', 'stage_id', 'current_user_id', 'email', 'telephone', 'alternate_telephone', 'remarks','mobile','is_disable','publish']
    search_fields = ['name']
    pass


#  $$$$$$$$$$$$

class TherapistResource(resources.ModelResource):
    # current_user = fields.Field(column_name='current_user', attribute='current_user', widget=ForeignKeyWidget(User,'username'))

    locality = fields.Field(
        column_name='locality_id',
        attribute='locality',
        widget=ForeignKeyWidget(Locality, 'id'))

    city= fields.Field(
        column_name='city_id',
        attribute='city',
        widget=ForeignKeyWidget(City, 'id'))

    state = fields.Field(
        column_name='state_id',
        attribute='state',
        widget=ForeignKeyWidget(State, 'id'))

    country = fields.Field(
        column_name='country_id',
        attribute='country',
        widget=ForeignKeyWidget(Country, 'id'))

    current_user = fields.Field(
        column_name='current_user_id',
        attribute='current_user',
        widget=ForeignKeyWidget(User, 'id'))

    stage = fields.Field(
        column_name='stage_id',
        attribute='stage',
        widget=ForeignKeyWidget(Stage, 'id'))

    class Meta:
        model = Therapist
        fields = ('id','name','qualification', 'experience','institution','type','services','speciality','therapist_locality_coverage_from_id','therapist_locality_coverage_to_id','address', 'locality_id', 'city_id','pincode', 'state_id', 'country_id', 'current_user_id','stage_id','telephone','mobile','email','rates','remarks','alternate_telephone','is_disable')



class TherapistAdmin(ImportExportModelAdmin):
    resource_class = TherapistResource

    fields = ['id','name','qualification', 'experience','institution','type','services','speciality','therapist_locality_coverage_from_id','therapist_locality_coverage_to_id','address', 'locality_id', 'city_id','pincode', 'state_id', 'country_id', 'current_user_id','stage_id','telephone','mobile','email','rates','remarks','alternate_telephone','is_disable']
    search_fields = ['name']
    pass


class LocalityResource(resources.ModelResource):
    class Meta:
        model = Locality
        fields = ('id','city','name','delete')


class LocalityAdmin(ImportExportModelAdmin):
    resource_class = LocalityResource
    fields = ['id','city','name','delete']
    search_fields = ['name']
    pass



class UserManagementResource(resources.ModelResource):
    # current_user = fields.Field(column_name='current_user', attribute='current_user', widget=ForeignKeyWidget(User,'username'))

    class Meta:
        model = UserManagement
        fields = ('id','user__username','is_caller','is_reviewer', 'is_publisher','is_news','is_service_plan')



class UserManagementAdmin(ImportExportModelAdmin):
    resource_class = UserManagementResource

    fields = []
    search_fields = ['user__username']
    pass


class CountrymasterResource(resources.ModelResource):
    class Meta:
        model = Countrymaster
        fields = ('id','name')


class CountrymasterAdmin(ImportExportModelAdmin):
    resource_class = CountrymasterResource

    fields = ['id','name']
    search_fields = ['name']
    pass


class StatemasterResource(resources.ModelResource):
    class Meta:
        model = Statemaster
        fields = ('id','countrymaster','name')


class StatemasterAdmin(ImportExportModelAdmin):
    resource_class = StatemasterResource

    fields = ['id','countrymaster','name']
    search_fields = ['name']
    pass



class CitymasterResource(resources.ModelResource):
    class Meta:
        model = Citymaster
        fields = ('id','statemaster','name')


class CitymasterAdmin(ImportExportModelAdmin):
    resource_class = CitymasterResource

    fields = ['id','statemaster','name']
    search_fields = ['name']
    pass



class LocalitymasterResource(resources.ModelResource):
    class Meta:
        model = Localitymaster
        fields = ('id','citymaster','name','deletee')


class LocalitymasterAdmin(ImportExportModelAdmin):
    resource_class = LocalitymasterResource

    fields = ['id','citymaster','name','deletee']
    search_fields = ['name']
    pass
#  $$$$$$$$$$$$
#------------------------------------------

admin.site.register(Zone, ZoneAdmin)
admin.site.register(Doctor, DoctorAdmin)

admin.site.register(AttachWithDoctor, AttachWithDoctorAdmin)
admin.site.register(OrganisationName, OrganisationAdmin)
admin.site.register(ZoneLocation, ZoneLocationAdmin)
admin.site.register(AssociateDoctorWithOrganization, AssociateDoctorWithOrganizationAdmin)
admin.site.register(BloodBank, BloodBankAdmin)
admin.site.register(Ambulance, AmbulanceAdmin)
admin.site.register(Disease, DiseaseAdmin)
admin.site.register(Symptoms, SymptomsAdmin)
admin.site.register(Drug, DrugAdmin)
admin.site.register(Disease_Category_search_mapping, Disease_Category_search_mapping_Admin)
admin.site.register(Labs, LabsAdmin)
admin.site.register(RehabCenter, RehabCenterAdmin)
admin.site.register(MedicalPharmacyStore, MedicalPharmacyStore_Admin)
admin.site.register(Ambulance_type_master, Ambulance_type_master_Admin)
admin.site.register(AmbulanceServices, AmbulanceServices_Admin)
admin.site.register(Nurse_Bureau, Nurse_BureauAdmin)
admin.site.register(Dietitian, DietitianAdmin)
admin.site.register(Therapist, TherapistAdmin)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Speciality, SpecialityAdmin)
admin.site.register(Service_Offred, Service_OffredAdmin)
admin.site.register(Locality, LocalityAdmin)
admin.site.register(UserManagement, UserManagementAdmin)
admin.site.register(Disease_search_master, Disease_search_masterAdmin)
admin.site.register(Symptoms_search_master, Symptoms_search_masterAdmin)
admin.site.register(Countrymaster, CountrymasterAdmin)
admin.site.register(Statemaster, StatemasterAdmin)
admin.site.register(Citymaster, CitymasterAdmin)
admin.site.register(Localitymaster, LocalitymasterAdmin)

