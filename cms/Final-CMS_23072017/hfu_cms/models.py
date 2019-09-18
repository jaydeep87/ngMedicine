from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from datetime import datetime
#from providers.models import ServiceProvider, PlanCategory
from django.contrib.postgres.fields import ArrayField
# Create your models here.


vf_schema = [
        {"Name": False}, {"Category": False}, {"Speciality": False}, {"Service-Offered": False},
        {"Registration-Detail": False},{"Zone": False},{"Zone-Location": False},
        {"Qualification": False}, {"Years-of-Experience": False}, {"Talk-to-Doc": False}, {"Talk-To-Doc-Fee": False},
        {"Gender": False}, {"DOB": False},
        {"Mobile": False}, {"Telephone": False}, {"Email": False}, {"Secondary-Email": False}, {"Skype-ID": False},
        {"Emergency-Services": False}, {"Emergency-Fee": False}, {"Emergency-Country": False},
        {"Emergency-State": False},
        {"Emergency-City": False}, {"Emergency-Locality": False},
        {"Rewards-and-Recognition": False}, {"Membership": False},
        {"Education": False}, {"Experience": False},
        {"Attached-Organisation-Name": False}, {"Organisation-Consultation-Timing": False},
        {"Consultation-Fees": False}
    ]

# vf_schema_organisation = [
#         {"Is-hospital-or-Clinic": False},{"Name": False}, {"Category": False}, {"Type": False}, {"Department": False},
#         {"Facility": False},{"Other-Facility": False},{"Address": False},
#         {"Country": False}, {"State": False}, {"City": False}, {"Location": False},
#         {"Pincode": False}, {"Niche-Department": False},
#         {"Package": False}, {"Phone": False}, {"DID": False}, {"Extension": False}, {"Email": False},
#         {"Fax": False}, {"Mobile": False}, {"Website": False},
#         {"Emergency-Contact-No": False},{"Latitude": False},{"Longitude": False},
#         {"Ambulance-Service-No": False},{"Broucher": False},{"Year-Of-Establishment": False},
#         {"Doctor-On-Board": False},{"No-of-Beds": False},{"Year-Of-Establishment": False},
#         {"Ambulance-Services": False},{"Trauma-Center": False},{"Burn-Center": False},
#         {"Emergency-Services": False},{"Doctor-Association": False},{"Profile-Image": False}
# ]

vf_schema_organisation = [
        {"Is-hospital-or-Clinic": False},{"Name": False}, {"Category": False}, {"Type": False}, {"Department": False},
        {"Facility": False},{"Other-Facility": False},{"Address": False},
        {"Country": False}, {"State": False}, {"City": False}, {"Location": False},
        {"Pincode": False}, {"Niche-Department": False},
        {"Package": False}, {"Phone": False}, {"DID": False}, {"Extension": False}, {"Email": False},
        {"Fax": False}, {"Mobile": False}, {"Website": False},
        {"Emergency-Contact-No": False},{"Latitude": False},{"Longitude": False},
        {"Ambulance-Service-No": False},{"Broucher": False},{"Year-Of-Establishment": False},
        {"Doctor-On-Board": False},{"No-of-Beds": False},{"Year-Of-Establishment": False},
        {"Ambulance-Services": False},{"Trauma-Center": False},{"Burn-Center": False},
        {"Emergency-Services": False},{"Doctor-Association": False},{"Profile-Image": False}, {"Clinic Tag Line":False},
        {"Alternative Email":False},{"Clinic OPD timings":False},{"Rewards and Recognization":False},{"Registration Details":False},
        {"Owner Name":False},{"Owner DOB":False},{"Owner Mobile No":False},{"Owner Phone No":False},{"Owner Email id":False},
        {"Owner Alternative Email":False},{"Names of Consultant Doctor":False},{"Names of Associate":False},{"Clinic Branches & Details":False}

    ]

vf_schema_lab = [
        {"Name": False},{"Address": False}, {"Pincode": False},
        {"Lab-Type": False}, {"Lab-Accredition-Body": False},{"Lab-Services": False},
        {"Lab-Departments": False}, {"Country": False},{"States": False},
        {"City": False}, {"Location": False},{"Area-Covered": False},
        {"Emergency-Services": False}, {"Telephone": False},{"Mobile": False},
        {"DID": False}, {"Extension": False},{"Email": False},
        {"Lab-Collection-Timings": False}, {"Ratings": False},{"Lab-Authorised-Person-Name": False},
        {"Lab-Authorised-Person-Designation": False},{"Lab-Authorised-Person-Contact-No": False},
        {"Lab-Authorised-Person-Emailid": False},{"Lab-Website": False},
        {"Pathology-Doctor-Names": False},{"Lab-Tests": False}
]

vf_schema_bloodbank = [
        {"Name": False},{"Address-1": False},{"Address-2": False}, {"Services": False},
        {"Country": False}, {"States": False}, {"City": False}, {"Location": False},
        {"Pincode": False},
        {"Blood-Bank-Doctor": False}, {"Education": False},{"Telephone": False},
        {"License": False}, {"Mobile": False},{"Stars": False},
        {"Pricing": False},{"Emergency-Services": False}
]

vf_schema_live_doctor = [
    {"First-Name": False}, {"Last-Name": False}, {"Category": False}, {"Speciality": False}, {"Service-Offered": False},
    {"Gender": False}, {"DOB": False}, {"Zone": False}, {"Zone-Location": False}, {"DID": False}, {"Extension": False},
    {"Mobile": False}, {"Telephone": False}, {"Fax": False}, {"Email": False}, {"Secondary-Email": False},
    {"Skype-ID": False},
    {"Education": False}, {"Registration-Detail": False}, {"Experience": False}, {"Rewards-and-Recognition": False},
    {"Membership": False}, {"Qualification": False}, {"Years-of-Experience": False}, {"Talk-to-Doc": False},
    {"Talk-To-Doc-Fee": False},
    {"Emergency-Services": False}, {"Emergency-Fee": False}, {"Emergency-Country": False}, {"Emergency-State": False},
    {"Emergency-City": False}, {"Emergency-Locality": False}, {"Attached-Organisation-Name": False},
    {"Organisation-Consultation-Timing": False},
    {"Consultation-Fees": False}, {"Attached-Organisation-DID": False}, {"Attached-Organisation-Extension": False},
    {"Attached-Organisation-State": False}, {"Attached-Organisation-City": False},
    {"Attached-Organisation-Locality": False},
    {"Certificate": False}, {"Adhar-Card-Copy": False}
]


import json
tempvf = json.dumps(vf_schema)
tempvf2 = json.loads(tempvf)

tempvf_org = json.dumps(vf_schema_organisation)
tempvf2_org = json.loads(tempvf_org)

tempvf_lab = json.dumps(vf_schema_lab)
tempvf2_lab = json.loads(tempvf_lab)

tempvf_bb = json.dumps(vf_schema_bloodbank)
tempvf2_bb = json.loads(tempvf_bb)

tempvf_live_doctor = json.dumps(vf_schema_live_doctor)
tempvf2_live_doctor = json.loads(tempvf_live_doctor)


class UserManagement(models.Model):
    user = models.ForeignKey(User)
    is_caller = models.BooleanField(default=False)
    is_reviewer = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)
    is_news = models.BooleanField(default=False)
    is_service_plan = models.BooleanField(default=False)
    is_news_reviewer = models.BooleanField(default=False)
    is_doctor_reviewer = models.BooleanField(default=False)
    is_service_reviewer = models.BooleanField(default=False)
    # Reviewer Data added by vishnu
    is_path_reviewer = models.BooleanField(default=False)
    is_blood_reviewer = models.BooleanField(default=False)
    is_ambulance_reviewer = models.BooleanField(default=False)
    is_phar_reviewer = models.BooleanField(default=False)
    is_disease_reviewer = models.BooleanField(default=False)

    #Added by Nishank on 5Dec
    is_physio_rehab_reviewer = models.BooleanField(default=False)

    # Added by Nishank on  16Dec
    is_nurse_bureau_reviewer = models.BooleanField(default=False)

    # Added by Nishank on  20Dec
    is_dietitian_reviewer = models.BooleanField(default=False)

    # Added by Nishank on  28 Dec
    is_therapist_reviewer  = models.BooleanField(default=False)

    # Caller data added by Nishank 26-9-16
    is_doctor_caller = models.BooleanField(default=False)
    is_phar_caller = models.BooleanField(default=False)
    is_path_caller = models.BooleanField(default=False)
    is_ambulance_caller = models.BooleanField(default=False)
    is_blood_caller = models.BooleanField(default=False)
    is_disease_caller = models.BooleanField(default=False)

    # Added by Nishank on  5Dec
    is_physio_rehab_caller = models.BooleanField(default=False)

    # Added by Nishank on  16Dec
    is_nurse_bureau_caller = models.BooleanField(default=False)

    # Added by Nishank on  20Dec
    is_dietitian_caller = models.BooleanField(default=False)

    # Added by Nishank on  28 Dec
    is_therapist_caller = models.BooleanField(default=False)

    # Added by Nishank on  28 March 2017 #$#$#$#$
    is_doctor = models.BooleanField(default=False)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = UserManagement.objects.all()
        flag = 0
        for obj in allobj:
            if obj.id == idd:
                flag = 1
                break
        if flag == 1:
            self.updatedAt = now
        else:
            self.updatedAt = now
            self.created_at = now
        super(UserManagement, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.user.username

class Country(models.Model):
    name = models.CharField(max_length=10000, help_text='', blank=True)
    country_code = models.CharField(max_length=10, null=True,
                                    blank=True)
    delete = models.BooleanField(default=False, help_text='Deactivate Country')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Country.objects.all()
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
        super(Country, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Country'
        verbose_name_plural = 'Country'


class ValidateByChoice(models.Model):
    name = models.CharField(max_length=10000, null=True, blank=True)
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = ValidateByChoice.objects.all()
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
        super(ValidateByChoice, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=10000, help_text='', blank=True)
    state_code = models.CharField(max_length=10, null=True, blank=True)
    delete = models.BooleanField(default=False, help_text='Deactivate State')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = State.objects.all()
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
        super(State, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'State'
        verbose_name_plural = 'States'


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=10000, help_text='', blank=True)
    city_code = models.CharField(max_length=10, null=True, blank=True)
    delete = models.BooleanField(default=False, help_text='')
    new_record = models.BooleanField(default=False)

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = City.objects.all()
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
        super(City, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class Locality(models.Model):
    city = models.ForeignKey(City)
    name = models.CharField(max_length=10000, help_text='', blank=True)
    latitude = models.CharField(max_length=10000, null=True, blank=True)
    longitude = models.CharField(max_length=10000, null=True, blank=True)
    delete = models.BooleanField(default=False, help_text='Deactivate Locality')

    new_record = models.BooleanField(default=False)

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Locality.objects.all()
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
        super(Locality, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Locality'
        verbose_name_plural = 'Localities'


class Facility(models.Model):
    name = models.CharField(max_length=1000, help_text='facility')
    #ADDED BY NISHANK 8 NOV 16
    delete = models.BooleanField(default=False)

    new_record = models.BooleanField(default=False)
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Facility.objects.all()
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
        super(Facility, self).save(*args, **kwargs)

class Stage(models.Model):
    stage_name = models.CharField(max_length=1000, help_text='Stages')
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)
    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Stage.objects.all()
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
        super(Stage, self).save(*args, **kwargs)

class Department(models.Model):
    name = models.CharField(max_length=1000, help_text='department_master')
    #23Jan 2017
    delete = models.BooleanField(default=False)
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Department.objects.all()
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
        super(Department, self).save(*args, **kwargs)

class Zone(models.Model):
    name = models.CharField(max_length=10000,
                            help_text='Listing of Zone')
    delete = models.BooleanField(default=False, help_text='Deactivate Zone')

    new_record = models.BooleanField(default=False)

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Zone.objects.all()
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
        super(Zone, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Zone'
        verbose_name_plural = 'Zones'


class ZoneLocation(models.Model):
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    name = models.CharField(max_length=10000, help_text='Listing of Zone location')
    delete = models.BooleanField(default=False, help_text='Deactivate Zone Location')

    new_record = models.BooleanField(default=False)
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = ZoneLocation.objects.all()
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
        super(ZoneLocation, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Zone Location'
        verbose_name_plural = 'Zone Locations'


# Category Master
class Category(models.Model):
    name = models.CharField(max_length=10000, help_text='', blank=True)
    delete = models.BooleanField(default=False, help_text='Deactivate Category')

    new_record = models.BooleanField(default=False)
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Category.objects.all()
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
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Speciality(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=10000, help_text='', blank=True)
    delete = models.BooleanField(default=False, help_text='')
    approve = models.BooleanField(default=False, help_text='')
    new_record = models.BooleanField(default=False)

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Speciality.objects.all()
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
        super(Speciality, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Speciality'
        verbose_name_plural = 'Specialities'


class Service_Offred(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=10000, help_text='', blank=True)
    delete = models.BooleanField(default=False, help_text='')
    approve = models.BooleanField(default=False, help_text='')
    new_record = models.BooleanField(default=False)

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Service_Offred.objects.all()
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
        super(Service_Offred, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Service Offer'
        verbose_name_plural = 'Service Offers'


# Doctor Data Table

class Doctor(models.Model):
    resource_validate = models.ForeignKey(ValidateByChoice, null=True)
    stage = models.ForeignKey(Stage, null=True)
    current_user = models.ForeignKey(User, null=True)
    previous_user = models.IntegerField(null=True)
    free_text = models.TextField(max_length=5000, help_text='', blank=True, null=True)
    unique_id = models.CharField(max_length=100, null=True,
                                 unique=True, blank=True)
    name = models.CharField(max_length=10000,
                            help_text='Listing of Doctor View')
    image_url = models.CharField(max_length=10000, null=True, blank=True)
    profile_photo = models.CharField(max_length=10000, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, null=True, blank=True)
    zone_location = models.ForeignKey(ZoneLocation, blank=True, null=True, )
    speciality = models.CharField(max_length=10000, blank=True, null=True)
    service_offered = models.CharField(max_length=10000, help_text='',
                                       blank=True, null=True)
    dob = models.DateField(null=True, blank=True, help_text='')
    mobile_no = models.CharField(max_length=10000, help_text='',
                                 blank=True, null=True)
    phone = models.CharField(max_length=10000, help_text='', blank=True,
                             null=True)
    skype_id = models.CharField(max_length=10000, help_text='',
                                blank=True)
    email = models.CharField(max_length=10000, help_text='', blank=True,
                             null=True)

    secondary_email = models.CharField(max_length=10000, help_text='',
                                       blank=True, null=True)
    doctor_experience_year = models.CharField(max_length=500, blank=True, null=True)
    qualification_data = models.TextField(null=True)
    registration_data = models.TextField(null=True)
    is_disable = models.BooleanField(default=False)
    male_doctor = models.BooleanField(default=False)
    female_doctor = models.BooleanField(default=False)
    publish = models.BooleanField(default=False)

    #Added by Nishank  on 7Nov 16
    #ALL BELOW FIELDS ARE FOR EMERGENCY
    is_emergency  = models.BooleanField(default=False)
    emergency_fee = models.TextField(max_length=500,blank=True, null=True,default='')
    country = models.ForeignKey(Country, null=True)
    state = models.ForeignKey(State, null=True)
    city = models.ForeignKey(City, null=True)
    localities = models.TextField(max_length=1000,blank=True, null=True,default='')

    talk_to_doc = models.BooleanField(default=False)
    talk_fee = models.TextField(max_length=500, blank=True, null=True, default='')

    #All below firlds provided are for CARE AT HOME
    provides_home_care = models.BooleanField(default=False)
    care_services_provided =  models.CharField(max_length=500, help_text='', blank=True, null=True)
    doctor_alternate_phone_number = models.CharField(max_length=500, help_text='', blank=True, null=True)
    doctor_areas_covered = models.CharField(max_length=500, help_text='', blank=True, null=True)
    doctor_rates = models.CharField(max_length=500, help_text='', blank=True, null=True)
    doctors_packages = models.CharField(max_length=1000, help_text='', blank=True, null=True)
    doctor_care_schedule_data = JSONField(null=True)

    #Below fields are to associate doctors with diseases and symptoms via categories
    #  using the symptom_search_master and disease_search_master
    associated_diseases =  models.TextField(max_length=10000,blank=True, null=True,default='')
    associated_symptoms =  models.TextField(max_length=10000,blank=True, null=True,default='')

    # did and extension added on 27march 2017 by Nishank
    did = models.TextField(blank=True, null=True,default='',help_text='Doctor hfu DID')
    extension = models.TextField(blank=True, null=True,default='',help_text='Doctor hfu extension')

    # points added on 1April 2017 by Nishank
    points = models.FloatField(null=True,default = 0)


    verified_fields = JSONField(null=True,default=tempvf2)

    catJSON = JSONField(null=True)
    new_record = models.BooleanField(default=False)

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    new_service_offered = models.TextField(default='', blank=True, null=True)
    new_service_offered_final = models.TextField(default='', blank=True, null=True)

    new_speciality = models.TextField(default='', blank=True, null=True)
    new_speciality_final = models.TextField(default='', blank=True, null=True)

    audio = models.BooleanField(default=False)
    video = models.BooleanField(default=False)
    chat = models.BooleanField(default=False)

    # 14 February Fields
    # 4 May Fields Nishank
    sponsored_rank = JSONField(default={'CC_RANK_list': {}, 'CLC_RANK_list': {}})
    sponsored_start_dates = JSONField(default=dict({}))
    sponsored_end_dates = JSONField(default=dict({}))
    # USELESS subscribed_rank = JSONField(default={'CC_RANK_list': {}, 'CLC_RANK_list': {}})
    # USELESS trial_rank = JSONField(default={'CC_RANK_list': {}, 'CLC_RANK_list': {}})

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Doctor.objects.all()
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
        super(Doctor, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Doctor_Imagegallery(models.Model):
    doctor = models.ForeignKey(Doctor, null=True)
    name = models.TextField(blank=True, null=True)
    publish = models.BooleanField(default=False)
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Doctor_Imagegallery.objects.all()
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
        super(Doctor_Imagegallery, self).save(*args, **kwargs)

    def __unicode__(self):
    	return '%s' % (self.name)

class Doctor_Education(models.Model):
    doctor = models.ForeignKey(Doctor)
    education_data = models.TextField(null=True)
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Doctor_Education.objects.all()
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
        super(Doctor_Education, self).save(*args, **kwargs)


class RewardRecognisation(models.Model):
    doctor = models.ForeignKey(Doctor, null=True)
    reward_data = models.TextField(null=True)
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = RewardRecognisation.objects.all()
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
        super(RewardRecognisation, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.free_text

        # Organisation


class Membership(models.Model):
    doctor = models.ForeignKey(Doctor, null=True)
    name = models.CharField(max_length=10000, help_text='', blank=True)
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Membership.objects.all()
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
        super(Membership, self).save(*args, **kwargs)


class Doctor_Experience(models.Model):
    doctor = models.ForeignKey(Doctor, null=True)
    experience_data = models.TextField()
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Doctor_Experience.objects.all()
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
        super(Doctor_Experience, self).save(*args, **kwargs)


class Doc_Care_services_master(models.Model):
    name = models.CharField(max_length=10000, help_text='Name')
    delete = models.BooleanField(default=False, help_text='Deactivate_doc_care_service_type')
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Doc_Care_services_master.objects.all()
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
        super(Doc_Care_services_master, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class OrganisationName(models.Model):
    resource_validate = models.ForeignKey(ValidateByChoice, null=True)
    stage = models.ForeignKey(Stage, null=True)
    current_user = models.ForeignKey(User, null=True)
    facility = models.CharField(max_length=10000, help_text='', blank=True)
    previous_user = models.IntegerField(null=True)
    free_text = models.TextField(max_length=5000, help_text='', blank=True, null=True)
    name = models.CharField(max_length=10000, help_text='Name')
    is_hospital = models.BooleanField(default=False)
    is_clinic = models.BooleanField(default=False)
    street = models.CharField(max_length=10000, help_text='', blank=True)
    locality = models.ForeignKey(Locality, models.SET_NULL, null=True)
    city = models.ForeignKey(City, null=True)
    state = models.ForeignKey(State, null=True)
    country = models.ForeignKey(Country, null=True)
    pincode = models.CharField(max_length=10, help_text='Pin code', blank=True)
    phone = models.CharField(max_length=10000, help_text='', blank=True)
    mobile_no = models.CharField(max_length=10000, help_text='', blank=True)
    fax = models.CharField(max_length=10000, help_text='', null=True, blank=True)
    email = models.CharField(max_length=10000, help_text='', blank=True)
    emergency_no = models.CharField(max_length=10000, help_text='',
                                    blank=True)
    website = models.CharField(max_length=10000, null=True, blank=True)
    department = models.CharField(max_length=10000, null=True, blank=True)
    niche_department = models.CharField(max_length=10000, null=True, blank=True)
    doctors_on_board = models.CharField(max_length=10000, null=True, blank=True)
    broucher = models.CharField(max_length=10000, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    ambulance_service = models.BooleanField(default=False)
    trauma_center = models.BooleanField(default=False)
    burn_center = models.BooleanField(default=False)
    ambulance_service_no = models.CharField(max_length=10000, null=True, blank=True)
    year_of_establishment = models.CharField(max_length=10000, null=True, blank=True)
    package = models.CharField(max_length=10000, null=True, blank=True)
    latitude = models.CharField(max_length=10000, null=True, blank=True)
    longitude = models.CharField(max_length=10000, null=True, blank=True)
    schedule_data = JSONField(null=True)
    publish = models.BooleanField(default=False)
    is_disable = models.BooleanField(default=False)
    other_facility = models.CharField(max_length=10000, null=True, blank=True)

    # Below field 'no_of_beds' Added by Nishank 16  7 Nov
    no_of_beds =  models.CharField(max_length=10000, default ='1')
    is_emergency = models.BooleanField(default=False)

    # did and extension added on 27march 2017 by Nishank
    did = models.TextField(blank=True, null=True, default='', help_text='Organisation hfu DID')
    extension = models.TextField(blank=True, null=True, default='', help_text='Organisation hfu extension')

    verified_fields = JSONField(null=True, default=tempvf2_org)

    hos_url = models.TextField(blank=True, null=True, default='')
    new_record = models.BooleanField(default=False)

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    #Added 28August17
    user_id = models.TextField(blank=True, null=True, default='')
    tagline = models.TextField(blank=True, null=True, default='')
    stamp = models.TextField(blank=True, null=True, default='')
    logo = models.TextField(blank=True, null=True, default='')
    profileImage = models.TextField(blank=True, null=True, default='')
    registration_details = models.TextField(blank=True, null=True, default='')
    alternateEmail = models.TextField(blank=True, null=True, default='')

    customer_organisation = models.BooleanField(default=False)
    activation = models.BooleanField(default=False)
    hfuId = models.TextField(db_column='hfuId', blank=True, null=True)
    deelete = models.BooleanField(default=False)

    is_live_org = models.BooleanField(default=False)
    merge_field = JSONField(null=True, default=[])
    finalise = models.BooleanField(default=False)

    updated_via = models.TextField(blank=True, null=True, default='')
    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = OrganisationName.objects.all()
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
        super(OrganisationName, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

#Added by Nishank 16  3 Nov
class Organisation_profile_img(models.Model):
   organisation = models.ForeignKey(OrganisationName, null=True)
   image = models.ImageField(upload_to="org_profile_image", null=True)
   image_url = models.CharField(null=True, blank=True, max_length=600)
   createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
   updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

   # Added by Ashutosh on 18 July 2017
   def save(self, *args, **kwargs):
       now = datetime.now()
       idd = self.id
       allobj = Organisation_profile_img.objects.all()
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
       super(Organisation_profile_img, self).save(*args, **kwargs)


#Added by Nishank 16  4 Nov
class Organisation_branches(models.Model):
   organisation = models.ForeignKey(OrganisationName, null=True)
   branches = JSONField(null=True)
   createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
   updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)
    # Added by Ashutosh on 18 July 2017
   def save(self, *args, **kwargs):
       now = datetime.now()
       idd = self.id
       allobj = Organisation_branches.objects.all()
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
       super(Organisation_branches, self).save(*args, **kwargs)

#Added by Nishank 16  5n7 Nov
class Organisation_plan(models.Model):
   organisation = models.ForeignKey(OrganisationName)
   package_details =  JSONField(null=True)

   createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
   updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)
    # Added by Ashutosh on 18 July 2017
   def save(self, *args, **kwargs):
       now = datetime.now()
       idd = self.id
       allobj = Organisation_plan.objects.all()
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
       super(Organisation_plan, self).save(*args, **kwargs)


#Added by Nishank 16  7 Nov
class Organisation_types(models.Model):
    type_name = models.CharField(max_length=1000, help_text='', blank=True,unique=True)
    delete = models.BooleanField(default=False, help_text='Deactivate Hospital Type')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)
    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Organisation_types.objects.all()
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
        super(Organisation_types, self).save(*args, **kwargs)

#Added by Nishank 16  7 Nov
class Organisation_categories(models.Model):
    category_name = models.CharField(max_length=1000, help_text='', blank=True,unique=True)
    delete = models.BooleanField(default=False, help_text='Deactivate Hospital Category')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Organisation_categories.objects.all()
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
        super(Organisation_categories, self).save(*args, **kwargs)

class AttachWithDoctor(models.Model):
    doctor = models.ForeignKey(Doctor)
    organisation = models.ForeignKey(OrganisationName)
    consultancy_fee = models.CharField(max_length=10000, help_text='',
                                       blank=True, null=True)
    email_attach = models.CharField(max_length=10000, help_text='',
                                    blank=True, null=True)
    telephone_attach = models.CharField(max_length=10000, help_text='',
                                        blank=True, null=True)

    #Added 28 March 2017 NISHANK
    did = models.TextField(blank=True, null=True, default='', help_text='Org attach with doctor  DID')
    extension = models.TextField(blank=True, null=True, default='', help_text='Org attach with doctor extension')
    department = models.TextField(blank=True, null=True, default='')

    new_record = models.BooleanField(default=False)

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = AttachWithDoctor.objects.all()
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
        super(AttachWithDoctor, self).save(*args, **kwargs)

    class Meta:
        ordering = ('id',)


class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    organisation = models.ForeignKey(OrganisationName, on_delete=models.CASCADE)
    schedule_data = JSONField(null=True)
    by_appointment = models.BooleanField(default=False)

    new_record = models.BooleanField(default=False)
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Schedule.objects.all()
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
        super(Schedule, self).save(*args, **kwargs)

class AssociateDoctorWithOrganization(models.Model):
    department = models.ForeignKey(Department, null=True)
    doctor = models.ForeignKey(Doctor, null=True)
    organisation = models.ForeignKey(OrganisationName, null=True)

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = AssociateDoctorWithOrganization.objects.all()
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
        super(AssociateDoctorWithOrganization, self).save(*args, **kwargs)

    class Meta:
        ordering = ('id',)

    def __unicode__(self):
        return self.doctor.name


class OranisationImagery(models.Model):
    organisation = models.ForeignKey(OrganisationName, null=True)
    image = models.CharField(max_length=10000, help_text='image_url',
                             blank=True, null=True)

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)
    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = OranisationImagery.objects.all()
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
        super(OranisationImagery, self).save(*args, **kwargs)

# Added the MODEL on Nov 21
class Lab_accreditation_body_master(models.Model):
    name = models.CharField(max_length=10000, help_text='Name')
    address = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    pincode = models.CharField(max_length=10, help_text='Pin code', blank=True)
    telephone = models.CharField(max_length=200, help_text='Pathology_Telephone', blank=True, null=True)
    delete = models.BooleanField(default=False, help_text='Deactivate_Lab_Accredition_Body')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Lab_accreditation_body_master.objects.all()
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
        super(Lab_accreditation_body_master, self).save(*args, **kwargs)

# Added the MODEL on Nov 21
class Lab_type_master(models.Model):
    name = models.CharField(max_length=10000, help_text='Name')
    delete = models.BooleanField(default=False, help_text='Deactivate_Lab_Type')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Lab_type_master.objects.all()
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
        super(Lab_type_master, self).save(*args, **kwargs)

# Added the MODEL on Nov nOV25
class Lab_test_master(models.Model):
    name = models.CharField(max_length=10000, help_text='Name')
    delete = models.BooleanField(default=False, help_text='Deactivate_Lab_Test')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Lab_test_master.objects.all()
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
        super(Lab_test_master, self).save(*args, **kwargs)

# Added the MODEL on Nov nOV26
class Lab_services_master(models.Model):
    name = models.CharField(max_length=10000, help_text='Name')
    delete = models.BooleanField(default=False, help_text='Deactivate_Lab_services')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Lab_services_master.objects.all()
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
        super(Lab_services_master, self).save(*args, **kwargs)

# Added the MODEL on Nov nOV28
class Lab_department_master(models.Model):
    name = models.CharField(max_length=10000, help_text='Name')
    delete = models.BooleanField(default=False, help_text='Deactivate_Lab_department')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Lab_department_master.objects.all()
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
        super(Lab_department_master, self).save(*args, **kwargs)

class Labs(models.Model):
    resource_validate = models.ForeignKey(ValidateByChoice, null=True) #--
    stage = models.ForeignKey(Stage, models.SET_NULL, null=True)
    country = models.ForeignKey(Country, models.SET_NULL, null=True) #--
    current_user = models.ForeignKey(User, null=True)
    previous_user = models.IntegerField(null=True)
    city = models.ForeignKey(City, models.SET_NULL, null=True) #--
    state = models.ForeignKey(State, models.SET_NULL, null=True) #--
    free_text = models.TextField(max_length=5000, help_text='', blank=True, null=True) #--
    name = models.CharField(max_length=10000, help_text='Name') #--
    locality = models.ForeignKey(Locality, models.SET_NULL, null=True, help_text="Location") #--
    telephone = models.CharField(max_length=200, help_text='Pathology Telephone', blank=True, null=True) #--
    address = models.CharField(max_length=10000, help_text='', blank=True, null=True) #--
    pincode = models.CharField(max_length=10, help_text='Pin code', blank=True) #--

    #ON 2 DEC RENAMED working_hours to lab_collection_timing
    #and increased length from 200 to 1000
    #working_hours = models.CharField(max_length=200, help_text='Pathology Timings', blank=True)
    lab_collection_timing = models.CharField(max_length=1000, help_text='Lab Collection Timing', blank=True) #--

    ratings = models.CharField(max_length=50, help_text='', blank=True) #--

    # >>>> Below field is NOT USED ANYMORE
    pathology_doctor_name = models.CharField(max_length=200, help_text='', blank=True)

    pathology_email = models.CharField(max_length=100, help_text='', blank=True) #--

    # >>>>>>>> Below field is NOT USED ANYMORE
    authorization_body = models.CharField(max_length=100, help_text='', blank=True)

    # >>>>>>>> Below field is NOT USED ANYMORE
    home_sample_collection = models.BooleanField(default=False)
    # home_sample_collection_no = models.BooleanField(default=False)

    #>>>>>>> Below field is NOT USED ANYMORE
    e_reporting_dispatch = models.BooleanField(default=False)
    # e_reporting_dispatch_no = models.BooleanField(default=False)

    # >>>>>>>> Below field is NOT USED ANYMORE
    rate = models.CharField(max_length=100, help_text='', blank=True)

    is_disable = models.BooleanField(default=False) #--

    # >>>>>>>> Below field is NOT USED ANYMORE
    # Added by Nishank on 15
    timings = models.CharField(max_length=10000, help_text='Lab timing', blank=True, null=True)

    # Chaged the field to json type Nov 19
    #tests = models.CharField(max_length=90000, help_text='Lab available_tests', blank=True, null=True)
    tests = JSONField(null=True) #--

    # Added the text field on Nov 19
    lab_doctors_on_board =  models.CharField(max_length=20000, help_text='', blank=True,null=True) #-

    # # Added the text field below on Nov 21
    lab_authorised_person_name   = models.CharField(max_length=20000, help_text='', blank=True,null=True) #--
    # # Added the text field below on Nov 21
    lab_authorised_person_designation    = models.CharField(max_length=20000, help_text='', blank=True,null=True) #--
    # # Added the text field below on Nov 21
    lab_authorised_person_contact_no = models.CharField(max_length=20000, help_text='', blank=True,null=True) # --
    # # Added the text field below on Nov 21
    lab_authorised_person_emailid = models.CharField(max_length=20000, help_text='', blank=True,null=True) # --

    # #Added the text field below on Nov 21  Below field is NOT USED ANYMORE
    lab_emailid  = models.CharField(max_length=20000, help_text='', blank=True,null=True)

    # # Added the text field below on Nov 21
    lab_website = models.CharField(max_length=1000, help_text='', blank=True,null=True) #--
    # # Added the text field below on Nov 21
    #lab_accreditation_body = models.ForeignKey(Lab_accreditation_body_master, models.SET_NULL, null=True, help_text="Lab Accreditation Body Master")
    # # Added the text field below on Nov 21
    lab_type = models.ForeignKey(Lab_type_master, models.SET_NULL, null=True, help_text="Accreditation Body Master") #--

    # # Added the field below on Nov25
    lab_locality_coverage_from = models.ForeignKey(Locality, models.SET_NULL, null=True, help_text="Location coverage from",related_name = 'locality_from') #--
    # # Added the field below on Nov25
    lab_locality_coverage_to = models.ForeignKey(Locality, models.SET_NULL, null=True, help_text="Location coverage to",related_name = 'locality_to') #--
    # Added by Nishank  on Nov25 16
    is_emergency = models.BooleanField(default=False) #--
    # # Added the field below on Nov25
    lab_accreditation_body = models.CharField(max_length=2000, help_text='', blank=True, null=True) #--


    # # Added the field below on Nov26 >>>>>>Below field is NOT USED ANYMORE
    lab_mobile = models.CharField(max_length=2000, help_text='', blank=True, null=True) #--
    # # Added the field below on Nov26
    lab_services = models.CharField(max_length=2000, help_text='', blank=True, null=True) #--

    #ADDED Nov28 2016
    lab_schedule = JSONField(null=True)
    # # Added the field below on Nov28
    lab_departments = models.CharField(max_length=2000, help_text='', blank=True, null=True) #--
    publish = models.BooleanField(default=False)

    # did and extension added on 27march 2017 by Nishank
    did = models.TextField(blank=True, null=True, default='', help_text='Lab hfu DID')
    extension = models.TextField(blank=True, null=True, default='', help_text='Lab hfu extension')

    verified_fields = JSONField(null=True, default=tempvf2_lab)
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Labs.objects.all()
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
        super(Labs, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name

# Added by Nishank 21  Nov
class Lab_branches(models.Model):
    lab = models.ForeignKey(Labs, null=True)
    branches = JSONField(null=True)

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Lab_branches.objects.all()
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
        super(Lab_branches, self).save(*args, **kwargs)

#Added by Nishank 21  5n7 Nov
class Labs_plan(models.Model):
   lab = models.ForeignKey(Labs)
   package_details =  JSONField(null=True)

   createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
   updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

   # Added by Ashutosh on 18 July 2017
   def save(self, *args, **kwargs):
       now = datetime.now()
       idd = self.id
       allobj = Labs_plan.objects.all()
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
       super(Labs_plan, self).save(*args, **kwargs)

class BloodBankServices(models.Model):
    name = models.CharField(max_length=10000, help_text='Listing of Blood Bank Services')
    delete = models.BooleanField(default=False, help_text='Deactivate Blood Bank Service')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = BloodBankServices.objects.all()
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
        super(BloodBankServices, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name

# Conceptually using address_1 and telephone_1 as primary
class BloodBank(models.Model):
    resource_validate = models.ForeignKey(ValidateByChoice, null=True)
    name = models.CharField(max_length=10000, help_text='Name')
    license = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    address_1 = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    address_2 = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    locality = models.ForeignKey(Locality, models.SET_NULL, null=True)
    city = models.ForeignKey(City, models.SET_NULL, null=True)
    state = models.ForeignKey(State, models.SET_NULL, null=True)
    country = models.ForeignKey(Country, null=True)  # additional from given form
    pincode = models.CharField(max_length=10, help_text='Pin code', blank=True)

    # telephone_1  renamed to  telephone  oN 30 NOV nOT TO USE telephone_2 AND telephone_3
    #AND LENGHTH CHANGED FROM 20 TO 20000
    #telephone_1 = models.CharField(max_length=20, help_text='Blood Bank Telephone_1', blank=True, null=True)
    telephone = models.CharField(max_length=20000, help_text='Blood Bank Telephone', blank=True, null=True)

    telephone_2 = models.CharField(max_length=20, help_text='Blood Bank Telephone_2', blank=True, null=True)
    telephone_3 = models.CharField(max_length=20, help_text='Blood Bank Telephone_3', blank=True, null=True)

    # Changed lengthto 20000 from 20
    #mobile = models.CharField(max_length=20, help_text='Blood Bank mobile', blank=True, null=True)
    mobile = models.CharField(max_length=20000, help_text='Blood Bank mobile', blank=True, null=True)

    #30 nov changed
    # services = models.ForeignKey(BloodBankServices, models.SET_NULL, null=True)
    # TO
    services = models.CharField(max_length=2000, help_text='', blank=True, null=True)

    #contact_person  renamed to  blood_bank_doctor  oN 30 NOV
    #contact_person = models.CharField(max_length=10000, help_text='Contact Person', blank=True, null=True)
    blood_bank_doctor = models.CharField(max_length=10000, help_text='Blood Bank Doctor', blank=True, null=True)

    education = models.CharField(max_length=10000, help_text='Education Rename', blank=True, null=True)
    stars = models.CharField(max_length=10000, null=True, blank=True)
    stage = models.ForeignKey(Stage, null=True)
    current_user = models.ForeignKey(User, null=True)
    previous_user = models.IntegerField(null=True)
    is_disable = models.BooleanField(default=False)
    free_text = models.TextField(max_length=5000, help_text='', blank=True, null=True)

    #ADDED BY Nishank on 15 Nov
    timings = models.CharField(max_length=10000, help_text='Bloodbank timing', blank=True, null=True)

    # ADDED BY Nishank on 30 Nov
    bloodbank_schedule = JSONField(null=True)

    # ADDED BY Nishank on 30 Nov
    is_emergency = models.BooleanField(default=False)

    # ADDED BY Nishank on 30 Nov
    pricing = models.CharField(max_length=20000, help_text='Blood Bank Pricing', blank=True, null=True)
    publish = models.BooleanField(default=False)

    verified_fields = JSONField(null=True, default=tempvf2_bb)

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = BloodBank.objects.all()
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
        super(BloodBank, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

        # free_text = models.TextField(max_length=5000, help_text='', blank=True, null=True)
        # location = models.CharField(max_length=500, help_text='Blood Bank Location', blank=True, null=True)
        # working_hours = models.CharField(max_length=200, help_text='Blood Bank Timings', blank=True)
        # ratings = models.CharField(max_length=50, help_text='', blank=True)
        # name_of_Blood_bank_doctor = models.CharField(max_length=200, help_text='', blank=True)
        # blood_bank_doctor_qualification = models.CharField(max_length=500, help_text='', blank=True)
        # blood_bank_FDA_license_no = models.CharField(max_length=100, help_text='', blank=True)
        # is_serve_in_emergency = models.BooleanField(default=False)
        # mobile_services = models.BooleanField(default=False)
        # blood_type = models.CharField(max_length=100, help_text='', blank=True)
        # contact_person  = models.CharField(max_length=500, help_text='', blank=True)


class Ambulance(models.Model):
    resource_validate = models.ForeignKey(ValidateByChoice, null=True)
    name = models.CharField(max_length=10000, help_text='Name')

    #Renamed to address_1 to address 11 december morning sunday
    #address_1 = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    address = models.CharField(max_length=10000, help_text='', blank=True, null=True)

    # Deleted by commenting 11 december morning sunday
    #address_2 = models.CharField(max_length=10000, help_text='', blank=True, null=True)

    locality = models.ForeignKey(Locality, models.SET_NULL, null=True)
    city = models.ForeignKey(City, models.SET_NULL, null=True)
    state = models.ForeignKey(State, models.SET_NULL, null=True)
    country = models.ForeignKey(Country, null=True)  # additional from given form
    pincode = models.CharField(max_length=10, help_text='Pin code', blank=True)

    # Renamed to telephone_1 to telephone 11 december morning sunday
    #telephone_1 = models.CharField(max_length=20, help_text='Ambulance Telephone_1', blank=True, null=True)
    telephone = models.CharField(max_length=20000, help_text='Ambulance Telephone', blank=True, null=True)

    #Deleted by commenting 11 december morning sunday
    #telephone_2 = models.CharField(max_length=20, help_text='Ambulance Telephone_2', blank=True, null=True)

    # Deleted by commenting 11 december morning sunday
    #telephone_3 = models.CharField(max_length=20, help_text='Ambulance Telephone_3', blank=True, null=True)


    #Changed lengthto 20000 from 20
    #mobile = models.CharField(max_length=20, help_text='Ambulance mobile', blank=True, null=True)
    mobile = models.CharField(max_length=20000, help_text='Ambulance mobile', blank=True, null=True)

    type = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    service = models.CharField(max_length=10000, help_text='', blank=True, null=True)

    # deleted teh field by commenting below on 9DECEMBER
    #area_covered = models.CharField(max_length=10000, help_text='', blank=True, null=True)

    service_contact_person = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    remarks = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    stage = models.ForeignKey(Stage, null=True)
    current_user = models.ForeignKey(User, null=True)
    previous_user = models.IntegerField(null=True)
    is_disable = models.BooleanField(default=False)
    free_text = models.TextField(max_length=5000, help_text='', blank=True, null=True)
    # Added by Nishank  on 7Nov 16 # NOT ADDED TO LIVE
    is_emergency = models.BooleanField(default=False)

    # Added the field below on 9DECEMBER
    ambulance_locality_coverage_from = models.ForeignKey(Locality, models.SET_NULL, null=True,
                                                     help_text="Ambulance Location coverage from",
                                                     related_name='Ambulance_locality_from')
    # Added the field below on 9DECEMBER
    ambulance_locality_coverage_to = models.ForeignKey(Locality, models.SET_NULL, null=True,
                                                   help_text="Ambulance Location coverage to",
                                                   related_name='Ambulance_locality_to')

    # Added the field below on 11 dECEMBER Sunday
    rates = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    publish = models.BooleanField(default=False)

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Ambulance.objects.all()
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
        super(Ambulance, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name

# ADDED BY Nishank on Dec 9
class AmbulanceServices(models.Model):
    name = models.CharField(max_length=10000, help_text='Listing of Ambulance Services')
    delete = models.BooleanField(default=False, help_text='Deactivate Ambulance Service')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = AmbulanceServices.objects.all()
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
        super(AmbulanceServices, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name

# ADDED BY Nishank on Dec 9
class Ambulance_type_master(models.Model):
    name = models.CharField(max_length=10000, help_text='Name')
    delete = models.BooleanField(default=False, help_text='Deactivate_Ambulance_Type')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Ambulance_type_master.objects.all()
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
        super(Ambulance_type_master, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name

# +++++++++ comment this to delete this
# class RehabCenter(models.Model):
#     resource_validate = models.ForeignKey(ValidateByChoice, null=True)
#     stage = models.ForeignKey(Stage, null=True)
#     user = models.ForeignKey(User, null=True)
#     free_text = models.TextField(max_length=5000, help_text='', blank=True, null=True)
#     name = models.CharField(max_length=10000, help_text='Name')
#     location = models.CharField(max_length=500, help_text='Rehab Center Location', blank=True, null=True)
#     telephone = models.CharField(max_length=20, help_text='Rehab Center Telephone', blank=True, null=True)
#     address = models.CharField(max_length=10000, help_text='', blank=True, null=True)
#     city = models.ForeignKey(City, models.SET_NULL, null=True)
#     state = models.ForeignKey(State, models.SET_NULL, null=True)
#     country = models.ForeignKey(Country, null=True)  # additional from given form
#     pincode = models.CharField(max_length=10, help_text='Pin code', blank=True)
#     working_hours = models.CharField(max_length=200, help_text='Rehab Center Timings', blank=True)
#     ratings = models.CharField(max_length=50, help_text='', blank=True)
#     doctors_associated = models.CharField(max_length=50, help_text='', blank=True)
#     rehab_doctor_name = models.CharField(max_length=100, help_text='', blank=True)
#     rehab_type = models.CharField(max_length=100, help_text='', blank=True)
#     rehab_type_name = models.CharField(max_length=100, help_text='', blank=True)
#     rehab_doctor_qualification = models.CharField(max_length=200, help_text='', blank=True)
#     email = models.CharField(max_length=100, help_text='', blank=True)
#     is_disable = models.BooleanField(default=False)


# ADDED BY Nishank on Dec 2
class RehabServices(models.Model):
    name = models.CharField(max_length=10000, help_text='Listing of Rehab Services')
    delete = models.BooleanField(default=False, help_text='Deactivate Rehab Service')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = RehabServices.objects.all()
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
        super(RehabServices, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name

# ADDED BY Nishank on Dec 2
class Rehab_type_master(models.Model):
    name = models.CharField(max_length=10000, help_text='Name')
    delete = models.BooleanField(default=False, help_text='Deactivate_Rehab_Type')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Rehab_type_master.objects.all()
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
        super(Rehab_type_master, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name


# ADDED BY Nishank on Dec 2
class Rehab_speciality_master(models.Model):
    name = models.CharField(max_length=10000, help_text='Name')
    delete = models.BooleanField(default=False, help_text='Deactivate_Rehab_Type')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Rehab_speciality_master.objects.all()
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
        super(Rehab_speciality_master, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name


# BY NISHANK ON 1ST DEC
class RehabCenter(models.Model):
    resource_validate = models.ForeignKey(ValidateByChoice, null=True)
    stage = models.ForeignKey(Stage, null=True)
    current_user = models.ForeignKey(User, null=True)
    previous_user = models.IntegerField(null=True)
    free_text = models.TextField(max_length=5000, help_text='', blank=True, null=True)
    clinic_name = models.CharField(max_length=10000, help_text='Name')

    #changed length from 100 to 30000
    #doctor_name = models.CharField(max_length=100, help_text='', blank=True)
    doctor_name = models.CharField(max_length=30000, help_text='', blank=True)

    experience = models.CharField(max_length=30000, help_text='', blank=True, null=True)
    qualification = models.CharField(max_length=30000, help_text='', blank=True, null=True)
    country = models.ForeignKey(Country, null=True)
    state = models.ForeignKey(State, models.SET_NULL, null=True)
    city = models.ForeignKey(City, models.SET_NULL, null=True)
    address = models.CharField(max_length=10000, help_text='Rehab Center  Address', blank=True, null=True)
    pincode = models.CharField(max_length=10, help_text='Pin code', blank=True)
    locality = models.ForeignKey(Locality, models.SET_NULL, null=True)
    # # Added the field below on Nov25
    rehab_locality_coverage_from = models.ForeignKey(Locality, models.SET_NULL, null=True, help_text="Rehab Location coverage from",related_name = 'Rehab_locality_from')
      # Added the field below on Nov25
    rehab_locality_coverage_to = models.ForeignKey(Locality, models.SET_NULL, null=True, help_text="Rehab Location coverage to",related_name = 'Rehab_locality_to')
    services = models.CharField(max_length=20000, help_text='Rehab Services', blank=True, null=True)
    telephone = models.CharField(max_length=20000, help_text='Rehab Center Telephone', blank=True, null=True)
    mobile = models.CharField(max_length=20000, help_text='Rehab Center Telephone', blank=True, null=True)
    email = models.CharField(max_length=1000, help_text='Rehab Center Email', blank=True, null=True)
    rates = models.CharField(max_length=1000, help_text='Rehab Rates', blank=True, null=True)
    type = models.CharField(max_length=20000, help_text='Rehab Type', blank=True, null=True)
    speciality = models.CharField(max_length=20000, help_text='Rehab Speciality', blank=True, null=True)
    rehab_schedule = JSONField(null=True)
    is_disable = models.BooleanField(default=False)
    is_emergency = models.BooleanField(default=False)

    # Added 8 Dec AFTERNOON
    website = models.CharField(max_length=10000, null=True, blank=True)
    publish = models.BooleanField(default=False)

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = RehabCenter.objects.all()
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
        super(RehabCenter, self).save(*args, **kwargs)


class Dietician(models.Model):
    resource_validate = models.ForeignKey(ValidateByChoice, null=True)
    stage = models.ForeignKey(Stage, null=True)
    current_user = models.ForeignKey(User, null=True)
    previous_user = models.IntegerField(null=True)
    free_text = models.TextField(max_length=5000, help_text='', blank=True, null=True)
    name = models.CharField(max_length=10000, help_text='Name')
    location = models.CharField(max_length=500, help_text='Dietician Location', blank=True, null=True)
    telephone = models.CharField(max_length=20, help_text='Dietician Telephone', blank=True, null=True)
    working_hours = models.CharField(max_length=200, help_text='Dietician Timings', blank=True)
    ratings = models.CharField(max_length=50, help_text='', blank=True)
    email = models.CharField(max_length=100, help_text='', blank=True)
    associated_organisation = models.CharField(max_length=500, help_text='', blank=True)
    address = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    city = models.ForeignKey(City, models.SET_NULL, null=True)
    state = models.ForeignKey(State, models.SET_NULL, null=True)
    country = models.ForeignKey(Country, null=True)  # additional from given form
    pincode = models.CharField(max_length=10, help_text='Pin code', blank=True)
    packages = models.CharField(max_length=100, help_text='', blank=True)
    is_disable = models.BooleanField(default=False)

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Dietician.objects.all()
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
        super(Dietician, self).save(*args, **kwargs)


class MedicalPharmacyStoreServices(models.Model):
    name = models.CharField(max_length=10000, help_text='Listing of Medical Pharmacy  Services')
    delete = models.BooleanField(default=False, help_text='Deactivate Medical Pharmacy Service')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = MedicalPharmacyStoreServices.objects.all()
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
        super(MedicalPharmacyStoreServices, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name


class MedicalPharmacyStoreType(models.Model):
    name = models.CharField(max_length=10000, help_text='Medical Pharmacy Type')
    delete = models.BooleanField(default=False, help_text='Deactivate Medical Pharmacy Type')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = MedicalPharmacyStoreType.objects.all()
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
        super(MedicalPharmacyStoreType, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name


class MedicalPharmacyStore(models.Model):
    resource_validate = models.ForeignKey(ValidateByChoice, null=True)
    name = models.CharField(max_length=10000, help_text='Name')
    address = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    locality = models.ForeignKey(Locality, models.SET_NULL, null=True)
    city = models.ForeignKey(City, models.SET_NULL, null=True)
    state = models.ForeignKey(State, models.SET_NULL, null=True)
    country = models.ForeignKey(Country, null=True)  # additional from given form
    pincode = models.CharField(max_length=10, help_text='Pin code', blank=True)

    #changed length to 20000
    telephone = models.CharField(max_length=20000, help_text='Pharmacy Telephone', blank=True, null=True)
    #changed length to 20000
    mobile = models.CharField(max_length=20000, help_text='Pharmacy mobile', blank=True, null=True)

    #DELETED ON 7 dec
    #type = models.ForeignKey(MedicalPharmacyStoreType, null=True)
    #ADDED ON 7 DEC
    type =  models.CharField(max_length=20000, help_text='Pharmacy Type', blank=True, null=True)

    #DELETED ON 7 dec
    #services = models.ForeignKey(MedicalPharmacyStoreServices, null=True)
    # ADDED ON 7 DEC
    services =  models.CharField(max_length=20000, help_text='Pharmacy Service', blank=True, null=True)

    timings = models.CharField(max_length=10000, help_text='timings', null=True)
    contact_person = models.CharField(max_length=10000, help_text='', blank=True, null=True)

    stage = models.ForeignKey(Stage, null=True)
    current_user = models.ForeignKey(User, null=True)
    previous_user = models.IntegerField(null=True)
    is_disable = models.BooleanField(default=False)
    free_text = models.TextField(max_length=5000, help_text='', blank=True, null=True)

    #Added 8 DEC
    pharmacy_schedule = JSONField(null=True)

    #Added 12dec
    fax = models.CharField(max_length=10000, help_text='', null=True, blank=True)
    email = models.CharField(max_length=10000, help_text='', blank=True)
    website = models.CharField(max_length=10000, null=True, blank=True)
    is_emergency  = models.BooleanField(default=False)
    publish = models.BooleanField(default=False)

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = MedicalPharmacyStore.objects.all()
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
        super(MedicalPharmacyStore, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name

    """ EARLIER STRUCTURE BY DEFAULT - Nishank"""
    """resource_validate = models.ForeignKey(ValidateByChoice, null=True)
    stage = models.ForeignKey(Stage, null=True)
    current_user = models.ForeignKey(User, null=True)
    previous_user = models.IntegerField(null=True)
    free_text = models.TextField(max_length=5000, help_text='', blank=True, null=True)
    name = models.CharField(max_length=10000, help_text='Name')
    pharmacy_type = models.CharField(max_length=100, help_text='', blank=True)
    location = models.CharField(max_length=500, help_text='Pharmacy Location', blank=True, null=True)
    telephone = models.CharField(max_length=20, help_text='Pharmacy Telephone', blank=True, null=True)
    address = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    city = models.ForeignKey(City, models.SET_NULL, null=True)
    state = models.ForeignKey(State, models.SET_NULL, null=True)
    country = models.ForeignKey(Country, null=True)  # additional from given form
    pincode = models.CharField(max_length=10, help_text='Pin code', blank=True)
    working_hours = models.CharField(max_length=200, help_text='Pharmacy Timings', blank=True)
    ratings = models.CharField(max_length=50, help_text='', blank=True)
    email = models.CharField(max_length=50, help_text='Pharmacy Email', blank=True)
    fax = models.CharField(max_length=50, help_text='Pharmacy Fax', blank=True)
    pharmacy_branch = models.CharField(max_length=200, help_text='', blank=True)
    home_delivery = models.BooleanField(default=False)
    is_disable = models.BooleanField(default=False)"""


class Therapists(models.Model):
    resource_validate = models.ForeignKey(ValidateByChoice, null=True)
    stage = models.ForeignKey(Stage, null=True)
    current_user = models.ForeignKey(User, null=True)
    previous_user = models.IntegerField(null=True)
    free_text = models.TextField(max_length=5000, help_text='', blank=True, null=True)
    name = models.CharField(max_length=10000, help_text='Name')
    location = models.CharField(max_length=500, help_text='Therapist Location', blank=True, null=True)
    telephone = models.CharField(max_length=20, help_text='Therapist Telephone', blank=True, null=True)
    address = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    city = models.ForeignKey(City, models.SET_NULL, null=True)
    state = models.ForeignKey(State, models.SET_NULL, null=True)
    country = models.ForeignKey(Country, null=True)  # additional from given form
    pincode = models.CharField(max_length=10, help_text='Pin code', blank=True)
    working_hours = models.CharField(max_length=200, help_text='Therapist Timings', blank=True)
    ratings = models.CharField(max_length=50, help_text='', blank=True)
    therapist_qualification = models.CharField(max_length=200, help_text='', blank=True)
    email = models.CharField(max_length=100, help_text='', blank=True)
    services_at_home = models.BooleanField(default=False)
    is_disable = models.BooleanField(default=False)

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Therapists.objects.all()
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
        super(Therapists, self).save(*args, **kwargs)


class Disease_type_master(models.Model):
    name = models.CharField(max_length=10000, help_text='Name')
    delete = models.BooleanField(default=False, help_text='deactivate_disease_type')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Disease_type_master.objects.all()
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
        super(Disease_type_master, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name

from django.conf import settings

class Disease(models.Model):
    resource_validate = models.ForeignKey(ValidateByChoice, null=True)

    topic_title = models.CharField(max_length=30000, help_text='Topic Title',blank=True, null=True)
    doctors_category = models.CharField(max_length=30000, help_text='Topic Title', blank=True, null=True)
    disease_image_file_name = models.CharField(max_length=30000, help_text='Topic Title', blank=True, null=True)
    related_topics = models.TextField(max_length=30000, help_text='', blank=True, null=True)

    small_description = models.CharField(max_length=30000, blank=True, null=True)
    publish_date = models.DateTimeField(null=True, blank=True)

    disease_docx_file = models.FileField(max_length=30000, upload_to=settings.DOCX_PATH_DISEASE, null=True)
    disease_html_raw = models.TextField(null=True)
    disease_html_refined = models.TextField(null=True)

    tag_string = models.TextField(max_length=30000, help_text='', blank=True, null=True)


    stage = models.ForeignKey(Stage, null=True)
    current_user = models.ForeignKey(User, null=True)
    previous_user = models.IntegerField(null=True)
    is_disable = models.BooleanField(default=False)
    free_text = models.TextField(max_length=5000, help_text='', blank=True, null=True)
    publish = models.BooleanField(default=False)

    page_title = models.TextField(max_length= 250, help_text='', blank=True, null=True)
    page_keywords = models.TextField(max_length= 500, help_text='', blank=True, null=True)
    page_description = models.TextField(max_length= 800, help_text='', blank=True, null=True)

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Disease.objects.all()
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
        super(Disease, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.topic_title

# class Disease(models.Model):
#     resource_validate = models.ForeignKey(ValidateByChoice, null=True)
#
#     disease_docx_file = models.FileField(max_length=100, upload_to=settings.DOCX_PATH_DISEASE, null=True)
#     disease_html_raw = models.TextField(null=True)
#     disease_html_refined = models.TextField(null=True)
#
#     tag_string = models.TextField(max_length=30000, help_text='', blank=True, null=True)
#     link_article_with = models.TextField(max_length=30000, help_text='', blank=True, null=True)
#     type = models.CharField(max_length=20000, help_text='Disease Type', blank=True, null=True)
#
#     stage = models.ForeignKey(Stage, null=True)
#     current_user = models.ForeignKey(User, null=True)
#     previous_user = models.IntegerField(null=True)
#     is_disable = models.BooleanField(default=False)
#     free_text = models.TextField(max_length=5000, help_text='', blank=True, null=True)
#
#     def __unicode__(self):
#         return self.tag_string

# class Disease(models.Model):
#     resource_validate = models.ForeignKey(ValidateByChoice, null=True)
#     topic_title = models.CharField(max_length=10000, help_text='Topic Title')
#     related_topics = models.CharField(max_length=10000, help_text='', blank=True, null=True)
#     tag_string = models.TextField(max_length=30000, help_text='', blank=True, null=True)
#     image = models.ImageField(upload_to="hfucms_disease_image", null=True)
#     image_url = models.CharField(null=True, blank=True, max_length=600)
#     article_body_description = models.TextField(max_length=30000, help_text='', blank=True, null=True)
#     article_body_cause = models.TextField(max_length=30000, help_text='', blank=True, null=True)
#     article_body_symptoms = models.TextField(max_length=30000, help_text='', blank=True, null=True)
#     article_body_test_n_diagnosis = models.TextField(max_length=30000, help_text='', blank=True, null=True)
#     article_body_treatment = models.TextField(max_length=30000, help_text='', blank=True, null=True)
#     article_body_prevention = models.TextField(max_length=30000, help_text='', blank=True, null=True)
#     link_article_with = models.TextField(max_length=30000, help_text='', blank=True, null=True)
#     stage = models.ForeignKey(Stage, null=True)
#     current_user = models.ForeignKey(User, null=True)
#     previous_user = models.IntegerField(null=True)
#     is_disable = models.BooleanField(default=False)
#     free_text = models.TextField(max_length=5000, help_text='', blank=True, null=True)
#
#     def __unicode__(self):
#         return self.topic_title



#aDDED BY NISHANK 8 Nov
class Disease_Category_search_mapping(models.Model):

   disease_name = models.CharField(max_length=10000, help_text='Disease Name')
   categories = models.CharField(max_length=10000, help_text='Stores the ids of categories in the category table',#
                                      blank=True, null=True)
   disease_name_translation = models.CharField(max_length=10000, help_text='Disease Name Translation',blank=True, null=True)
   disease_name_transliteration = models.CharField(max_length=10000, help_text='Disease Name Transliteration',blank=True, null=True)
   delete = models.BooleanField(default=False, help_text='Deactivate Country Disease Mapping')

   createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
   updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

   # Added by Ashutosh on 18 July 2017
   def save(self, *args, **kwargs):
       now = datetime.now()
       idd = self.id
       allobj = Disease_Category_search_mapping.objects.all()
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
       super(Disease_Category_search_mapping, self).save(*args, **kwargs)

class Drug(models.Model):
    resource_validate = models.ForeignKey(ValidateByChoice, null=True)
    name = models.CharField(max_length=10000, help_text='Topic Title')
    generic_name = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    brand_name = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    manufacturer_name = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    composition = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    form_n_rate = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    dosage = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    mode_of_administration = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    indication = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    overdose = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    contraindication = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    special_precaution = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    adverse_drug_reactions = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    drug_interaction = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    lab_interference = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    mechanism_of_action = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    drug_class = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    atc_classification = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    schedule_classification = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    stage = models.ForeignKey(Stage, null=True)
    current_user = models.ForeignKey(User, null=True)
    previous_user = models.IntegerField(null=True)
    is_disable = models.BooleanField(default=False)
    free_text = models.TextField(max_length=5000, help_text='', blank=True, null=True)

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Drug.objects.all()
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
        super(Drug, self).save(*args, **kwargs)
    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name



class Symptoms(models.Model):
    resource_validate = models.ForeignKey(ValidateByChoice, null=True)

    topic_title = models.CharField(max_length=30000, help_text='Topic Title',blank=True, null=True)
    doctors_category = models.CharField(max_length=30000, help_text='Topic Title', blank=True, null=True)
    symptoms_image_file_name = models.CharField(max_length=30000, help_text='Topic Title', blank=True, null=True)
    related_topics = models.TextField(max_length=30000, help_text='', blank=True, null=True)

    small_description = models.CharField(max_length=30000, blank=True, null=True)
    publish_date = models.DateTimeField(null=True, blank=True)

    symptoms_docx_file = models.FileField(max_length=30000, upload_to=settings.DOCX_PATH_SYMPTOMS, null=True)
    symptoms_html_raw = models.TextField(null=True)
    symptoms_html_refined = models.TextField(null=True)

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

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Symptoms.objects.all()
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
        super(Symptoms, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.topic_title

# class Symptoms(models.Model):
#     resource_validate = models.ForeignKey(ValidateByChoice, null=True)
#     topic_title = models.CharField(max_length=10000, help_text='Topic Title')
#     tag_string = models.TextField(max_length=30000, help_text='', blank=True, null=True)
#     image = models.ImageField(upload_to="hfucms_symptoms_image", null=True)
#     image_url = models.CharField(null=True, blank=True, max_length=600)
#     article_body_description = models.TextField(max_length=30000, help_text='', blank=True, null=True)
#     article_body_cause = models.TextField(max_length=30000, help_text='', blank=True, null=True)
#     article_body_self_care = models.TextField(max_length=30000, help_text='', blank=True, null=True)
#     stage = models.ForeignKey(Stage, null=True)
#     current_user = models.ForeignKey(User, null=True)
#     previous_user = models.IntegerField(null=True)
#     is_disable = models.BooleanField(default=False)
#     free_text = models.TextField(max_length=5000, help_text='', blank=True, null=True)
#
#     def __unicode__(self):
#         return self.topic_title

# class Assign(models.Model):
# previous_user = models.IntegerField( null=True)
#     stage = models.ForeignKey(Stage)
#     telecaller = models.ForeignKey(User, related_name='telecaller_name')
#     reviewer = models.ForeignKey(User, related_name='reviewer_name', null=True)
#     send_reviewer = models.BooleanField(default=False)
#     revert = models.BooleanField(default=False)
#     send_odoo = models.BooleanField(default=False)
#     free_text = models.TextField(max_length=5000, help_text='', blank=True, null=True)
#     log_history = JSONField(null=True)
#     user = models.ForeignKey(User,  null=True)
#
#     class Meta:
#         ordering = ('doctor__name',)

# def __unicode__(self):
#     return self.doctor.name


# ADDED BY Nishank on Dec 2
class Nurse_bureauServices(models.Model):
    name = models.CharField(max_length=10000, help_text='Listing of Nurse Bureau Services')
    delete = models.BooleanField(default=False, help_text='Deactivate Nurse Bureau Service')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Nurse_bureauServices.objects.all()
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
        super(Nurse_bureauServices, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name

# ADDED BY Nishank on Dec 2
class Nurse_bureau_speciality_master(models.Model):
    name = models.CharField(max_length=10000, help_text='Name')
    delete = models.BooleanField(default=False, help_text='Deactivate_Nurse_Bureau_Type')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Nurse_bureau_speciality_master.objects.all()
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
        super(Nurse_bureau_speciality_master, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name

#Created 16 dec
class Nurse_Bureau(models.Model):
    resource_validate = models.ForeignKey(ValidateByChoice, null=True)
    stage = models.ForeignKey(Stage, null=True)
    current_user = models.ForeignKey(User, null=True)
    previous_user = models.IntegerField(null=True)
    free_text = models.TextField(max_length=5000, help_text='', blank=True, null=True)
    name = models.CharField(max_length=10000, help_text='Name')
    certification = models.CharField(max_length=10000, help_text='Certification')
    experience = models.CharField(max_length=10000, help_text='experience')
    services = models.CharField(max_length=20000, help_text='Nurse Bureau Services', blank=True, null=True)
    speciality = models.CharField(max_length=20000, help_text='Nurse Bureau Speciality', blank=True, null=True)
    nurse_bureau_locality_coverage_from = models.ForeignKey(Locality, models.SET_NULL, null=True,
                                                     help_text="Nurse Bureau Location coverage from",
                                                     related_name='nurse_bureau_locality_from')

    nurse_bureau_locality_coverage_to = models.ForeignKey(Locality, models.SET_NULL, null=True,
                                                   help_text="Nurse Bureau Location coverage to",
                                                   related_name='nurse_bureau_locality_to')
    country = models.ForeignKey(Country, null=True)
    state = models.ForeignKey(State, models.SET_NULL, null=True)
    city = models.ForeignKey(City, models.SET_NULL, null=True)
    address = models.CharField(max_length=10000, help_text='Nurse Bureau Center  Address', blank=True, null=True)
    pincode = models.CharField(max_length=10, help_text='Pin code', blank=True)
    locality = models.ForeignKey(Locality, models.SET_NULL, null=True)
    email = models.CharField(max_length=1000, help_text='Nurse Bureau Center Email', blank=True, null=True)
    nurse_bureau_schedule = JSONField(null=True)
    rates = models.CharField(max_length=1000, help_text='Nurse Bureau Rates', blank=True, null=True)
    telephone = models.CharField(max_length=20000, help_text='Nurse Bureau Center Telephone', blank=True, null=True)
    mobile = models.CharField(max_length=20000, help_text='Nurse Bureau Center Telephone', blank=True, null=True)
    contact_person = models.CharField(max_length=10000, help_text='Contact Person', blank=True, null=True)
    is_disable = models.BooleanField(default=False)
    branches = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    website = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    nurse_bureau_packages = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    no_of_nurses = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    nurses_experience = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    contact_person_contact_no = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    contact_person_email = models.CharField(max_length=10000, help_text='', blank=True, null=True)
    packages = JSONField(null=True)
    remarks = models.CharField(max_length=30000, help_text='Remarks', blank=True, null=True)
    publish = models.BooleanField(default=False)

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)
    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Nurse_Bureau.objects.all()
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
        super(Nurse_Bureau, self).save(*args, **kwargs)

# ADDED BY Nishank on Dec 20
class DietitianServices(models.Model):
    name = models.CharField(max_length=10000, help_text='Dietitian Services')
    delete = models.BooleanField(default=False, help_text='deactivate_dietitian_service')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = DietitianServices.objects.all()
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
        super(DietitianServices, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name

# ADDED BY Nishank on Dec 20
class Dietitian_type_master(models.Model):
    name = models.CharField(max_length=10000, help_text='Name')
    delete = models.BooleanField(default=False, help_text='deactivate_dietitian_type')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Dietitian_type_master.objects.all()
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
        super(Dietitian_type_master, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name

# ADDED BY Nishank on Dec 20
class Dietitian(models.Model):
    resource_validate = models.ForeignKey(ValidateByChoice, null=True)
    stage = models.ForeignKey(Stage, null=True)
    current_user = models.ForeignKey(User, null=True)
    previous_user = models.IntegerField(null=True)
    free_text = models.TextField(max_length=5000, help_text='', blank=True, null=True)

    name = models.CharField(max_length=10000, help_text='Name')
    institution = models.CharField(max_length=10000, help_text='Institution')
    qualification = models.CharField(max_length=10000, help_text='Qualification')
    experience = models.CharField(max_length=10000, help_text='experience')
    type = models.CharField(max_length=20000, help_text='Dietitian Type', blank=True, null=True)
    services = models.CharField(max_length=20000, help_text='Dietitian Services', blank=True, null=True)

    dietitian_locality_coverage_from = models.ForeignKey(Locality, models.SET_NULL, null=True,
                                                     help_text="Dietitian Location coverage from",
                                                     related_name='Dietitian_Locality_From')

    dietitian_locality_coverage_to = models.ForeignKey(Locality, models.SET_NULL, null=True,
                                                   help_text="Dietitian Location coverage to",
                                                   related_name='Dietitian_Locality_To')
    rates = models.CharField(max_length=1000, help_text='Dietitian Rates', blank=True, null=True)
    packages = JSONField(null=True)
    address = models.CharField(max_length=10000, help_text='Dietitian Center  Address', blank=True, null=True)
    pincode = models.CharField(max_length=10, help_text='Pin code', blank=True)
    country = models.ForeignKey(Country, null=True)
    state = models.ForeignKey(State, models.SET_NULL, null=True)
    city = models.ForeignKey(City, models.SET_NULL, null=True)
    locality = models.ForeignKey(Locality, models.SET_NULL, null=True)
    email = models.CharField(max_length=1000, help_text='Dietitian Email', blank=True, null=True)
    telephone = models.CharField(max_length=20000, help_text='Dietitian Telephone', blank=True, null=True)
    alternate_telephone = models.CharField(max_length=20000, help_text='Dietitian Alternate Telephone', blank=True, null=True)
    mobile = models.CharField(max_length=20000, help_text='Dietitian Telephone', blank=True, null=True)
    is_disable = models.BooleanField(default=False)
    remarks = models.CharField(max_length=30000, help_text='Remarks', blank=True, null=True)
    publish = models.BooleanField(default=False)

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)
    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Dietitian.objects.all()
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
        super(Dietitian, self).save(*args, **kwargs)

# ADDED BY Nishank on Dec 20
class Attach_dietitian_organisation(models.Model):
    dietitian = models.ForeignKey(Dietitian)
    organisation = models.ForeignKey(OrganisationName)
    org_department = models.ForeignKey(Department,null=True)
    consultancy_fee = models.CharField(max_length=10000, help_text='',
                                       blank=True, null=True)
    email_attach = models.CharField(max_length=10000, help_text='',
                                    blank=True, null=True)
    telephone_attach = models.CharField(max_length=10000, help_text='',
                                        blank=True, null=True)
    schedule = JSONField(null=True)
    by_appointment = models.BooleanField(default=False)

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Attach_dietitian_organisation.objects.all()
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
        super(Attach_dietitian_organisation, self).save(*args, **kwargs)
    class Meta:
        ordering = ('id',)

# ADDED BY Nishank on dec 28
class TherapistServices(models.Model):
    name = models.CharField(max_length=10000, help_text='Therapist Services')
    delete = models.BooleanField(default=False, help_text='deactivate_therapist_service')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = TherapistServices.objects.all()
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
        super(TherapistServices, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name

# ADDED BY Nishank on dec 28
class Therapist_type_master(models.Model):
    name = models.CharField(max_length=10000, help_text='Name')
    delete = models.BooleanField(default=False, help_text='deactivate_therapist_type')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Therapist_type_master.objects.all()
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
        super(Therapist_type_master, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name

# ADDED BY Nishank on Dec 28
class Therapist_speciality_master(models.Model):
    name = models.CharField(max_length=10000, help_text='Name')
    delete = models.BooleanField(default=False, help_text='Deactivate_Therapist_Type')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Therapist_speciality_master.objects.all()
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
        super(Therapist_speciality_master, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name

# ADDED BY Nishank on dec 28
class Therapist(models.Model):
    resource_validate = models.ForeignKey(ValidateByChoice, null=True)
    stage = models.ForeignKey(Stage, null=True)
    current_user = models.ForeignKey(User, null=True)
    previous_user = models.IntegerField(null=True)
    free_text = models.TextField(max_length=5000, help_text='', blank=True, null=True)

    name = models.CharField(max_length=10000, help_text='Name')
    institution = models.CharField(max_length=10000, help_text='Institution')
    qualification = models.CharField(max_length=10000, help_text='Qualification')
    experience = models.CharField(max_length=10000, help_text='experience')
    type = models.CharField(max_length=20000, help_text='Therapist Type', blank=True, null=True)
    services = models.CharField(max_length=20000, help_text='Therapist Services', blank=True, null=True)
    speciality = models.CharField(max_length=20000, help_text='Therapist Speciality', blank=True, null=True)
    therapist_locality_coverage_from = models.ForeignKey(Locality, models.SET_NULL, null=True,
                                                     help_text="Therapist Location coverage from",
                                                     related_name='Therapist_Locality_From')

    therapist_locality_coverage_to = models.ForeignKey(Locality, models.SET_NULL, null=True,
                                                   help_text="Therapist Location coverage to",
                                                   related_name='Therapist_Locality_To')
    rates = models.CharField(max_length=1000, help_text='Therapist Rates', blank=True, null=True)
    packages = JSONField(null=True)
    address = models.CharField(max_length=10000, help_text='Therapist Center  Address', blank=True, null=True)
    pincode = models.CharField(max_length=10, help_text='Pin code', blank=True)
    country = models.ForeignKey(Country, null=True)
    state = models.ForeignKey(State, models.SET_NULL, null=True)
    city = models.ForeignKey(City, models.SET_NULL, null=True)
    locality = models.ForeignKey(Locality, models.SET_NULL, null=True)
    email = models.CharField(max_length=1000, help_text='Therapist Email', blank=True, null=True)
    telephone = models.CharField(max_length=20000, help_text='Therapist Telephone', blank=True, null=True)
    alternate_telephone = models.CharField(max_length=20000, help_text='Therapist Alternate Telephone', blank=True, null=True)
    mobile = models.CharField(max_length=20000, help_text='Therapist Telephone', blank=True, null=True)
    is_disable = models.BooleanField(default=False)
    remarks = models.CharField(max_length=30000, help_text='Remarks', blank=True, null=True)

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)
    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Therapist.objects.all()
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
        super(Therapist, self).save(*args, **kwargs)

# ADDED BY Nishank on dec 28
class Attach_therapist_organisation(models.Model):
    therapist = models.ForeignKey(Therapist)
    organisation = models.ForeignKey(OrganisationName)
    org_department = models.ForeignKey(Department,null=True)
    consultancy_fee = models.CharField(max_length=10000, help_text='',
                                       blank=True, null=True)
    email_attach = models.CharField(max_length=10000, help_text='',
                                    blank=True, null=True)
    telephone_attach = models.CharField(max_length=10000, help_text='',
                                        blank=True, null=True)
    schedule = JSONField(null=True)
    by_appointment = models.BooleanField(default=False)

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Attach_therapist_organisation.objects.all()
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
        super(Attach_therapist_organisation, self).save(*args, **kwargs)
    class Meta:
        ordering = ('id',)

class pub_unpub_error_log(models.Model):
    action = models.CharField(max_length=50, null=True,blank=True)
    date_n_time = models.DateField(null=True,blank=True)
    model_type = models.TextField(max_length=5000, help_text='', blank=True, null=True)
    publish_data = JSONField(null=True)
    model_instance_id =  models.IntegerField(default=0,null=True)
    error_message =  models.CharField(max_length=500, null=True,blank=True)

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = pub_unpub_error_log.objects.all()
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
        super(pub_unpub_error_log, self).save(*args, **kwargs)

class Disease_search_master(models.Model):
    name = models.CharField(max_length=350, help_text='Name',blank=True, null= True, unique=True)
    delete = models.BooleanField(default=False, help_text='Deactivate_Disease_search_master')
    doctor_categories = models.CharField(max_length=3000, help_text='', default = '')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Disease_search_master.objects.all()
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
        super(Disease_search_master, self).save(*args, **kwargs)
    # This was CAUSING ERROR IN IMPORT EXPORT
    # def __unicode__(self):
    #     return self.name


    #SO CHANGED TO
    def __unicode__(self):
        return '%s' % (self.name)


class Symptoms_search_master(models.Model):
    name = models.CharField(max_length=350, help_text='Name',blank=True, null= True,unique=True)
    delete = models.BooleanField(default=False, help_text='Deactivate_Symptoms_search_master')
    doctor_categories = models.CharField(max_length=3000, help_text='', default='')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Symptoms_search_master.objects.all()
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
        super(Symptoms_search_master, self).save(*args, **kwargs)
    # This was CAUSING ERROR IN IMPORT EXPORT
    # def __unicode__(self):
    #     return self.name

    # SO CHANGED TO
    def __unicode__(self):
        return '%s' % (self.name)


#---------------------#--------------------------#
# ALL 10 IVE DOCTRS MODULES                      #
#--------------------#---------------------------#

class Live_Doctor_Commonworkschedule(models.Model):
    doctor_id = models.IntegerField(blank=True, null=True)
    # clinic_id = models.TextField(blank=True, null=True)
    clinic_id = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    speciality = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    mobileNo = models.TextField(db_column='mobileNo', blank=True, null=True)  # Field name made lowercase.
    registrationNo = models.TextField(db_column='registrationNo', blank=True, null=True)  # Field name made lowercase.
    # elastic_unique_id = models.TextField(blank=True, null=True)
    elastic_unique_id = models.IntegerField(blank=True, null=True)
    confirmation = models.TextField(blank=True, null=True)  # This field type is a guess.
    dataSharing = models.TextField(db_column='dataSharing', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hospital = models.TextField(blank=True, null=True)  # This field type is a guess.
    designation = models.TextField(blank=True, null=True)
    # appointmentMinute = models.TextField(db_column='appointmentMinute', blank=True, null=True)  # Field name made lowercase.
    appointmentMinute = models.IntegerField(db_column='appointmentMinute', blank=True, null=True)
    # consultingCharge = models.TextField(db_column='consultingCharge', blank=True, null=True)  # Field name made lowercase.
    consultingCharge = models.IntegerField(db_column='consultingCharge', blank=True, null=True)
    time_type = models.TextField(blank=True, null=True)
    time = models.TextField(blank=True, null=True)  # This field type is a guess.
    slot = models.TextField(blank=True, null=True)
    stamp = models.TextField(blank=True, null=True)
    signature = models.TextField(blank=True, null=True)
    defaultClinicFlag = models.BooleanField(default=False)  # Field name made lowercase.

    timing = JSONField(null=True)
    time_object = JSONField(null=True)

    #delete = models.BooleanField(default=False)
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    did = models.TextField(blank=True, null=True, default='', help_text='Live Doctor Schedule DID')
    extension = models.TextField(blank=True, null=True, default='', help_text='Live Doctor Schedule extension')

    department = models.TextField(blank=True, null=True, default='')
    status = models.TextField(blank=True, null=True, default='', help_text='Schedule Status')

    associateWithClinic = models.BooleanField(default=False)
    associated_by = models.TextField(blank=True,null=True,default='')
    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Live_Doctor_Commonworkschedule.objects.all()
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
        super(Live_Doctor_Commonworkschedule, self).save(*args, **kwargs)


    #by_appointment = models.BooleanField(default=False)


    #Required for cms
    # def __unicode__(self):
    # 	return '%s' % (self.registrationNo)


def speciality_default():
    return []


def so_default():
    return []

class Live_Doctor(models.Model):
    # Kanhaiya fields
    user_id = models.TextField(blank=True, null=True)
    firstName = models.TextField(db_column='firstName', blank=True, null=True)  # Field name made lowercase.
    lastName = models.TextField(db_column='lastName', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(blank=True, null=True)
    mobileNo = models.TextField(db_column='mobileNo', blank=True, null=True)  # Field name made lowercase.

    #Changed text field category to integer field 18 March 2017 previusly stored name
    #category = models.TextField(blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)

    #Changed speciality text field to Json field 18 March 2017 Previusly stored names
    #speciality = models.TextField(blank=True, null=True)
    speciality  = JSONField(null=True)

    #speciality = ArrayField(models.CharField(max_length=250,blank=True,null= True), default=speciality_default)
    activate = models.BooleanField(default=False)
    edit = models.BooleanField(default=True)

    # Changed service offered text field to Json field 18 March 2017 Previusly stored names
    #serviceOffered = models.TextField(db_column='serviceOffered', blank=True, null=True)  # Field name made lowercase.
    serviceOffered  = JSONField(null=True)

    #serviceOffered = ArrayField(models.CharField(max_length=250,blank=True, null=True),default=so_default)
    dob = models.TextField(blank=True, null=True)
    mciRegistrationNo = models.TextField(db_column='mciRegistrationNo', blank=True, null=True)  # Field name made lowercase.
    # elastic_unique_id = models.TextField(blank=True, null=True)
    elastic_unique_id = models.IntegerField(blank=True, null=True)
    registrationBoard = models.TextField(db_column='registrationBoard', blank=True, null=True)  # Field name made lowercase.
    # registrationYear = models.TextField(db_column='registrationYear', blank=True, null=True)  # Field name made lowercase.
    registrationYear = models.IntegerField(db_column='registrationYear', blank=True, null=True)
    alternateMobileNo = models.TextField(db_column='alternateMobileNo', blank=True, null=True)  # Field name made lowercase.
    alternateEmail = models.TextField(db_column='alternateEmail', blank=True, null=True)  # Field name made lowercase.
    gender = models.TextField(blank=True, null=True)
    phoneNo = models.TextField(db_column='phoneNo', blank=True, null=True)  # Field name made lowercase.
    fax = models.TextField(blank=True, null=True)
    skypeId = models.TextField(db_column='skypeId', blank=True, null=True)  # Field name made lowercase.
    stamp = models.TextField(blank=True, null=True)
    signature = models.TextField(blank=True, null=True)
    profileImage = models.TextField(db_column='profileImage', blank=True, null=True)  # Field name made lowercase.
    degreeCertImage = models.TextField(db_column='degreeCertImage', blank=True, null=True)  # Field name made lowercase.
    aadhaarCardImage = models.TextField(db_column='aadhaarCardImage', blank=True, null=True)  # Field name made lowercase.
    hfuId = models.TextField(db_column='hfuId', unique=True, blank=True, null=True)  # Field name made lowercase.
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    resource_validate = models.ForeignKey(ValidateByChoice, null=True,default=1)
    stage = models.ForeignKey(Stage, null=True,default=2)
    current_user = models.ForeignKey(User, null=True,default=54)
    previous_user = models.IntegerField(null=True)
    free_text = models.TextField(max_length=5000, help_text='', blank=True, null=True)
    publish = models.BooleanField(default=False)
    cuser = models.IntegerField(null=True,blank=True)
    cstage = models.IntegerField(null=True,blank=True)

    zone = models.ForeignKey(Zone, null=True, blank=True)
    zone_location = models.ForeignKey(ZoneLocation, blank=True, null=True)


    accountCreated =  models.BooleanField(default=False)
    activationStatus =  models.BooleanField(default=False)

    # points added on 1April 2017 by Nishank
    experience_points = models.FloatField(null=True, default=0)
    emergency_points = models.FloatField(null=True, default=0)
    qualification_points = models.FloatField(null=True, default=0)

    is_disable = models.BooleanField(default=False)

    did = models.TextField(blank=True, null=True, default='', help_text='LiveDoctor hfu DID')
    extension = models.TextField(blank=True, null=True, default='', help_text='LIveDoctor hfu extension')

    privateimagepath = models.TextField(blank=True, null=True)
    updated_via = models.TextField(blank=True, null=True)

    associated_diseases = models.TextField(max_length=10000, blank=True, null=True, default='')
    associated_symptoms = models.TextField(max_length=10000, blank=True, null=True, default='')

    verified_fields = JSONField(null=True, default=tempvf2_live_doctor)
    merge_fields = JSONField(null=True, default=[])

    new_service_offered_final = JSONField(null=True)
    new_speciality_final = JSONField(null=True)

    # 7 January Fields
    sponsored_rank = JSONField(default={'CC_RANK_list':{},'CLC_RANK_list':{}} )
    sponsored_start_dates = JSONField(default=dict({}))
    sponsored_end_dates = JSONField(default=dict({}))


    subscribed_rank = JSONField(default={'CC_RANK_list':{},'CLC_RANK_list':{}})

    #USELESStrial_rank = JSONField(default={'CC_RANK_list': {}, 'CLC_RANK_list': {}})

    trial_rank = models.BooleanField(default=True)
    is_subscribed = models.BooleanField(default=False)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Live_Doctor.objects.all()
        flag = 0
        for obj in allobj:
            if obj.id == idd:
                flag = 1
                break
        if flag == 1:
            self.updatedAt = now
            mydocmsg = 'Doctor Updated'
        else:
            self.updatedAt = now
            self.createdAt = now
            mydocmsg = 'Doctor Created'
        super(Live_Doctor, self).save(*args, **kwargs)

        if self.stage:
            stage_nname = self.stage.stage_name
        else:
            stage_nname = ''
        Live_Doctor_Notification.objects.create(notification_creation_date=now,
                                                livedoctor_id=self.id, livedoctorCrAt=self.createdAt,
                                                livedoctorName=self.firstName + ' ' + self.lastName,
                                                livedoctorStage=stage_nname,
                                                update_Type = mydocmsg,
                                                updatedBy='CMS')

    # Required for cms
    def __unicode__(self):
        return '%s' % (self.firstName+' '+self.lastName)


class Live_Doctor_Education(models.Model):
    doctor_id = models.IntegerField(blank=True, null=True)
    degree = models.TextField(blank=True, null=True)
    college = models.TextField(blank=True, null=True)
    # year = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Live_Doctor_Education.objects.all()
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
        if args == ():
            args = ({'NOKEY':100},)
        if 'UPDATE' not in args[0] and 'DELETE'  not in args[0]:
            super(Live_Doctor_Education, self).save(*args, **kwargs)
        lvdr = None
        lvdr = Live_Doctor.objects.get(id=self.doctor_id)
        Live_Doctor_Notification.objects.create(notification_creation_date=now,
                                                livedoctor_id=lvdr.id, livedoctorCrAt=lvdr.createdAt,
                                                livedoctorName=lvdr.firstName + ' ' + lvdr.lastName,
                                                livedoctorStage=lvdr.stage.stage_name,
                                                update_Type='Education Change',
                                                updatedBy='CMS')

    #Required for cms
    def __unicode__(self):
    	return '%s' % (self.degree)

class Live_Doctor_Experience(models.Model):
    doctor_id = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    # fromYear = models.TextField(db_column='fromYear', blank=True, null=True)  # Field name made lowercase.
    fromYear = models.IntegerField(db_column='fromYear', blank=True, null=True)  # Field name made lowercase.
    # toYear = models.TextField(db_column='toYear', blank=True, null=True)  # Field name made lowercase.
    toYear = models.IntegerField(db_column='toYear', blank=True, null=True)  # Field name made lowercase.
    designation = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Live_Doctor_Experience.objects.all()
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
        if args == ():
            args = ({'NOKEY':100},)
        if 'UPDATE' not in args[0] and 'DELETE'  not in args[0]:
            super(Live_Doctor_Experience, self).save(*args, **kwargs)
        lvdr = None
        lvdr = Live_Doctor.objects.get(id=self.doctor_id)
        Live_Doctor_Notification.objects.create(notification_creation_date=now,
                                                livedoctor_id=lvdr.id, livedoctorCrAt=lvdr.createdAt,
                                                livedoctorName=lvdr.firstName + ' ' + lvdr.lastName,
                                                livedoctorStage=lvdr.stage.stage_name,
                                                update_Type='Experience Change',
                                                updatedBy='CMS')

    #Required for cms
    def __unicode__(self):
    	return '%s' % (self.name)


class Live_Doctor_Imagegallery(models.Model):
    doctor_id = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Live_Doctor_Imagegallery.objects.all()
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
        super(Live_Doctor_Imagegallery, self).save(*args, **kwargs)
        lvdr = None
        lvdr = Live_Doctor.objects.get(id=self.doctor_id)
        Live_Doctor_Notification.objects.create(notification_creation_date=now,
                                                livedoctor_id=lvdr.id, livedoctorCrAt=lvdr.createdAt,
                                                livedoctorName=lvdr.firstName + ' ' + lvdr.lastName,
                                                livedoctorStage=lvdr.stage.stage_name,
                                                update_Type='Imagegallery Change',
                                                updatedBy='CMS')

    #Required for cms
    def __unicode__(self):
    	return '%s' % (self.name)


class Live_Doctor_Membership(models.Model):
    doctor_id = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Live_Doctor_Membership.objects.all()
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
        if args == ():
            args = ({'NOKEY':100},)
        if 'DELETE'  not in args[0] and 'UPDATE'  not in args[0]:
            super(Live_Doctor_Membership, self).save(*args, **kwargs)
        lvdr = None
        lvdr = Live_Doctor.objects.get(id=self.doctor_id)
        Live_Doctor_Notification.objects.create(notification_creation_date=now,
                                                livedoctor_id=lvdr.id, livedoctorCrAt=lvdr.createdAt,
                                                livedoctorName=lvdr.firstName + ' ' + lvdr.lastName,
                                                livedoctorStage=lvdr.stage.stage_name,
                                                update_Type='Membership Change',
                                                updatedBy='CMS')

    #Required for cms
    def __unicode__(self):
    	return '%s' % (self.name)


class Live_Doctor_Rewardrecog(models.Model):
    doctor_id = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    # year = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Live_Doctor_Rewardrecog.objects.all()
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
        if args == ():
            args = ({'NOKEY':100},)
        if 'DELETE'  not in args[0]:
            super(Live_Doctor_Rewardrecog, self).save(*args, **kwargs)
        lvdr = None
        lvdr = Live_Doctor.objects.get(id=self.doctor_id)
        Live_Doctor_Notification.objects.create(notification_creation_date=now,
                                                livedoctor_id=lvdr.id, livedoctorCrAt=lvdr.createdAt,
                                                livedoctorName=lvdr.firstName + ' ' + lvdr.lastName,
                                                livedoctorStage=lvdr.stage.stage_name,
                                                update_Type='Reward-Recognition Change',
                                                updatedBy='CMS')

    #Required for cms
    def __unicode__(self):
    	return '%s' % (self.name)

#class Uploadimage(models.Model):


class Live_Doctor_Associated_Data(models.Model):
    doctor_id = models.IntegerField(blank=True, null=True)

    # All below firlds provided are for talk to doc
    talk_to_doc = models.BooleanField(default=False)
    talk_fee = models.TextField(max_length=500, blank=True, null=True, default='')
    # ---Talk to doc end----------------------

    #Added by Ashutosh on 14Nov for online consultancy
    audio = models.BooleanField(default=False)
    video = models.BooleanField(default=False)
    chat = models.BooleanField(default=False)
    # All below firlds provided are for CARE AT HOME
    provides_home_care = models.BooleanField(default=False)
    care_services_provided = models.CharField(max_length=500, help_text='', blank=True, null=True)
    doctor_alternate_phone_number = models.CharField(max_length=500, help_text='', blank=True, null=True)
    doctor_areas_covered = models.CharField(max_length=500, help_text='', blank=True, null=True)
    doctor_rates = models.CharField(max_length=500, help_text='', blank=True, null=True)
    doctors_packages = models.CharField(max_length=1000, help_text='', blank=True, null=True)
    doctor_care_schedule_data = JSONField(null=True)
    #---------CARE AT HOME FIELDS END--------


    # ALL BELOW FIELDS ARE FOR EMERGENCY
    is_emergency = models.BooleanField(default=False)
    emergency_fee = models.TextField(max_length=500, blank=True, null=True, default='')
    country = models.ForeignKey(Country, null=True)
    state = models.ForeignKey(State, null=True)
    city = models.ForeignKey(City, null=True)
    localities = models.TextField(max_length=1000, blank=True, null=True, default='')
    #------Emergency fields end---------

    qualification_data = models.TextField(null=True,blank=True)

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    totalexperience = models.TextField(max_length=100, default='', blank=True, null=True)

    # Added Again By Nishank 11 April 2018
    chat_fee = models.TextField(max_length=500, blank=True, null=True, default='')
    chat_days = models.TextField(max_length=500, blank=True, null=True, default='')

    audio_fee = models.TextField(max_length=500, blank=True, null=True, default='')
    audio_minutes = models.TextField(max_length=500, blank=True, null=True, default='')

    video_fee = models.TextField(max_length=500, blank=True, null=True, default='')
    video_minutes = models.TextField(max_length=500, blank=True, null=True, default='')

    consultancy_schedule = JSONField(null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Live_Doctor_Associated_Data.objects.all()
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
        super(Live_Doctor_Associated_Data, self).save(*args, **kwargs)
        if flag == 1:
            lvdr = None
            lvdr = Live_Doctor.objects.get(id=self.doctor_id)
            Live_Doctor_Notification.objects.create(notification_creation_date=now,
                                                    livedoctor_id=lvdr.id, livedoctorCrAt=lvdr.createdAt,
                                                    livedoctorName=lvdr.firstName + ' ' + lvdr.lastName,
                                                    livedoctorStage=lvdr.stage.stage_name,
                                                    update_Type='Associated-Data Change',
                                                    updatedBy='CMS')

    #Required for cms
    def __unicode__(self):
    	return '%s' % (self.doctor_id)


class patienttoaskquestion(models.Model):
    patient_id = models.TextField(blank=True, null=True, default='')
    # doctor_id to be kept string fields as per discussion with Kanhaiyah 29 March 2017
    doctor_id = models.TextField(blank=True, null=True, default='')
    answer_id = models.TextField(blank=True, null=True, default='')
    questionFor = models.TextField(blank=True, null=True, default='you')
    questionType = models.TextField(blank=True, null=True, default='private')
    questionDescription = models.TextField(blank=True, null=True, default='')
    questionDetail1 = models.TextField(blank=True, null=True, default='')
    questionDetail2 = models.TextField(blank=True, null=True, default='')
    questionDetail3 = models.TextField(blank=True, null=True, default='')
    firstName = models.TextField(blank=True, null=True, default='')
    lastName = models.TextField(blank=True, null=True, default='')
    email = models.TextField(blank=True, null=True, default='')
    mobileNo = models.TextField(blank=True, null=True, default='')
    gender = models.TextField(blank=True, null=True, default='')
    age = models.TextField(blank=True, null=True, default='')
    category = models.TextField(blank=True, null=True, default='')
    relation = models.TextField(blank=True, null=True, default='')
    doctor_name = models.TextField(blank=True, null=True, default='')
    doctor_category = models.TextField(blank=True, null=True, default='')
    # consultation_charge = models.TextField(blank=True, null=True, default='')
    consultation_charge = models.FloatField(blank=True, null=True)
    consultation_charge_type = models.TextField(blank=True, null=True, default='')
    doctor_profile_image = models.TextField(blank=True, null=True, default='')
    free = models.TextField(blank=True, null=True, default='')
    paymentStatus = models.TextField(blank=True, null=True, default='')
    patient_name = models.TextField(blank=True, null=True, default='')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    transaction_id = models.TextField(blank=True, null=True, default='')

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = patienttoaskquestion.objects.all()
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
        super(patienttoaskquestion, self).save(*args, **kwargs)

class patienttodoctorfeedback(models.Model):
    patient_id = models.TextField(blank=True, null=True, default='')
    # doctor_id = models.TextField(blank=True, null=True, default='')
    doctor_id = models.IntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True, default='')
    rating = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True, default='')
    verified = models.BooleanField(default=False)

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    name = models.TextField(blank=True, null=True, default='')
    mobileNo = models.TextField(blank=True, null=True, default='')
    email= models.TextField(blank=True, null=True, default='')
    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = patienttodoctorfeedback.objects.all()
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
        super(patienttodoctorfeedback, self).save(*args, **kwargs)


#### LIVE DOCTOR MODELS END ##############

# KEEP COMMENTED FOR MIGRATION ON LIVE

# Display only 'WINNERS' in views and not 'Loosers' and 'Delete'
class Doctor_ServiceOffered_New(models.Model):
    name = models.TextField(unique=True, null=True, blank=True)
    deleete = models.BooleanField(default=False, help_text='Deactivate Service Offered')
    soids = models.TextField(default='')
    new_record = models.BooleanField(default=False)
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)
    WorL = models.TextField(default='', blank=True, null=True)
    related_winners = models.TextField(default='', blank=True, null=True)
    movedfrom_losertowinner = models.BooleanField(default=False)
    movement_date = models.DateTimeField(blank=True, null=True)

	#tempcat = models.TextField(null=True, blank=True)
    #tempcatIDS = models.TextField(null=True, blank=True)
    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Doctor_ServiceOffered_New.objects.all()
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
        super(Doctor_ServiceOffered_New, self).save(*args, **kwargs)
    # def __unicode__(self):
    #     return self.name
    def __unicode__(self):
        return unicode(self.name) or u''

# Display only 'WINNERS' in views and not 'Loosers' and 'Delete'
class Doctor_Speciality_New(models.Model):
    name = models.TextField(unique=True, null=True, blank=True)
    deleete = models.BooleanField(default=False, help_text='Deactivate Speciality')
    speids = models.TextField(default='')
    new_record = models.BooleanField(default=False)
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)
    WorL = models.TextField(default='', blank=True, null=True)
    related_winners = models.TextField(default='', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Doctor_Speciality_New.objects.all()
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
        super(Doctor_Speciality_New, self).save(*args, **kwargs)
    # def __unicode__(self):
    #     return self.name
    def __unicode__(self):
        return unicode(self.name) or u''
#
class Doc_Cat_SO_Speciality_Association(models.Model):
    category = models.IntegerField(unique=True, null=True, blank=True)
    Specialities = models.TextField(default='')
    ServiceOffered = models.TextField(default='')
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)
    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Doc_Cat_SO_Speciality_Association.objects.all()
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
        super(Doc_Cat_SO_Speciality_Association, self).save(*args, **kwargs)

class Doc_Cat_SO_Speciality_Association_Final(models.Model):
    category = models.IntegerField(unique=True, null=True, blank=True)
    Specialities = models.TextField(default='')
    ServiceOffered = models.TextField(default='')
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    #Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Doc_Cat_SO_Speciality_Association_Final.objects.all()
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
        super(Doc_Cat_SO_Speciality_Association_Final, self).save(*args, **kwargs)


#Temporary for giving extract from old SO master id 1 to 7872  **********DO NOT MIGRATE********
# class DelServiceOfferedNew_7872(models.Model):
#     name = models.TextField(unique=True, null=True, blank=True)
#     deleete = models.BooleanField(default=False, help_text='Deactivate Service Offered')
#     soids = models.TextField(default='')
#     new_record = models.BooleanField(default=False)
#     createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
#     updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)
#
#     def __unicode__(self):
#         return self.name

############################## For master of Country State City Locality #################################


class Countrymaster(models.Model):
    name = models.CharField(max_length=10000, help_text='', blank=True,unique=True)

    deletee = models.BooleanField(default=False, help_text='Deactivate Country')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allcountry = Countrymaster.objects.all()
        flag = 0
        for counrty in allcountry:
            if counrty.id == idd:
                flag = 1
                break
        if flag == 1:
            self.updatedAt = now
        else:
            self.updatedAt = now
            self.createdAt = now
        self.name = self.name.lower()
        super(Countrymaster, self).save(*args, **kwargs)


    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Statemaster(models.Model):
    countrymaster = models.ForeignKey(Countrymaster,null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=10000, help_text='', blank=True, unique=True)

    deletee = models.BooleanField(default=False, help_text='Deactivate Country')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Statemaster.objects.all()
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
        self.name = self.name.lower()
        super(Statemaster, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Citymaster(models.Model):
    statemaster = models.ForeignKey(Statemaster,null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=10000, help_text='', blank=True)

    deletee = models.BooleanField(default=False, help_text='')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Citymaster.objects.all()
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
        super(Citymaster, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)




class Localitymaster(models.Model):
    citymaster = models.ForeignKey(Citymaster,null=True)
    name = models.CharField(max_length=10000, help_text='', blank=True)

    deletee= models.BooleanField(default=False, help_text='Deactivate Locality')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Localitymaster.objects.all()
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
        super(Localitymaster, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Dummy_cat_disease_aasociation(models.Model):
    cat_id =models.AutoField(primary_key=True)
    diseaseid = models.TextField(blank=True,null=True)

    def __unicode__(self):
        return self.cat_id


class organisation_Rewardrecog(models.Model):
   organisation = models.ForeignKey(OrganisationName, on_delete=models.CASCADE)
   name = models.TextField(blank=True, null=True)
   year = models.IntegerField(blank=True, null=True)
   createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
   updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.


   # Added by Ashutosh on 18 July 2017
   def save(self, *args, **kwargs):
       now = datetime.now()
       idd = self.id
       allobj = organisation_Rewardrecog.objects.all()
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
       super(organisation_Rewardrecog, self).save(*args, **kwargs)
   #Required for cms
   def __unicode__(self):
      return '%s' % (self.name)

class organisation_Registrationimages(models.Model):
   organisation = models.ForeignKey(OrganisationName, on_delete=models.CASCADE)
   image = models.TextField(blank=True, null=True)
   createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
   updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

   # Added by Ashutosh on 18 July 2017
   def save(self, *args, **kwargs):
       now = datetime.now()
       idd = self.id
       allobj = organisation_Registrationimages.objects.all()
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
       super(organisation_Registrationimages, self).save(*args, **kwargs)
   #Required for cms
   def __unicode__(self):
      return '%s' % (self.image)


class organisation_Imagegallery(models.Model):
   organisation = models.ForeignKey(OrganisationName, on_delete=models.CASCADE)
   image = models.TextField(blank=True, null=True)
   publish = models.BooleanField(default=False)
   createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
   updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

   # Added by Ashutosh on 18 July 2017
   def save(self, *args, **kwargs):
       now = datetime.now()
       idd = self.id
       allobj = organisation_Imagegallery.objects.all()
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
       super(organisation_Imagegallery, self).save(*args, **kwargs)
   #Required for cms
   def __unicode__(self):
      return '%s' % (self.name)


class Live_Doctor_Manage_Account(models.Model):
    livedoctor = models.ForeignKey(Live_Doctor,on_delete=models.CASCADE)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    plan_name = models.TextField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    amount = models.TextField(blank=True, null=True)
    payment_mode = models.TextField(blank=True, null=True)
    invoice = models.FileField(blank=True, null=True)
    receipt = models.FileField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    # #createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    # #updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)
#
# #Created 19 Dec 2017 to be migrated tomorrow morning
#
class Live_Doctor_Notification(models.Model):

    notification_creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True) # This field will be

    createdAt = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    updatedAt = models.DateTimeField(blank=True, null=True)
    # displayed unbder both 'Date' as well as 'Update Date Time', the only difference being  that under 1st we don't
    # display time while under we 2nd we also display time.

    livedoctor = models.ForeignKey(Live_Doctor, blank=True, null=True)
    livedoctorCrAt = models.DateTimeField(blank=True, null=True) # This will be populated by the Live Doctor's CreateAt
                                                                 # field


    livedoctorName = models.TextField(default='',blank=True, null=True)
    updatedBy = models.TextField(default='',blank=True, null=True) # Cms username / Front-end
    #updatedBy = models.ForeignKey('auth.User',null=True,blank=True,default=current_user.get_current_user)  # Cms username / Front-end
    livedoctorStage = models.TextField(default='',blank=True, null=True) # Live doctor's stage

    update_Type = models.TextField(default='',blank=True, null=True) # LIVE DOCTOR/EDUCATION / EXPERIENCE /
                                                                     # IMAGE Gallery/ADDITIONAL INFO/ACCOUNT/
                                                                     # Membership / Rewardrecog / Common work schedule
    deelete = models.BooleanField(default=False, help_text='Delete Notification')

    def __unicode__(self):
        return '%s' % (self.notification_creation_date.strftime('%d/%m/%Y - %H:%M:%S'))

class Live_Doctor_Schedule_Delete_Notification(models.Model):
    notification_creation_date = models.DateTimeField(auto_now_add=True, blank=True,null=True)  # This field will be

    updatedAt = models.DateTimeField(auto_now=True,blank=True, null=True)

    livedoctor = models.ForeignKey(Live_Doctor, blank=True, null=True)
    livedoctorName = models.TextField(default='', blank=True, null=True)
    category = models.CharField(max_length=150, blank=True, null=True)
    clinic = models.ForeignKey(OrganisationName, blank=True, null=True)
    spon_cc_rank = models.CharField(max_length=50, blank=True, null=True)
    spon_clc_rank = models.CharField(max_length=50, blank=True, null=True)
    spon_cc_key = models.CharField(max_length=20, blank=True, null=True)
    spon_clc_key = models.CharField(max_length=20, blank=True, null=True)
    spon_cc_key_label = models.TextField(blank=True, null=True)
    spon_clc_key_label = models.TextField(blank=True, null=True)

    updatedBy = models.TextField(default='', blank=True, null=True)  # Cms username / Front-end
    # updatedBy = models.ForeignKey('auth.User',null=True,blank=True,default=current_user.get_current_user)  # Cms username / Front-end
    livedoctorCurrentUser = models.TextField(default='', blank=True, null=True)  # Live doctor's stage
    livedoctorStage = models.TextField(default='', blank=True, null=True)  # Live doctor's stage

    update_Type = models.TextField(default='', blank=True, null=True)  # LIVE DOCTOR/EDUCATION / EXPERIENCE /
    deelete = models.BooleanField(default=False, help_text='Delete Notification')

    def __unicode__(self):
        return '%s' % (self.notification_creation_date.strftime('%d/%m/%Y - %H:%M:%S'))

class Live_Doctor_Schedule_Stopdate_Notification(models.Model):
    notification_creation_date = models.DateTimeField(auto_now_add=True, blank=True,
                                                      null=True)  # This field will be

    updatedAt = models.DateTimeField(auto_now=True, blank=True, null=True)

    livedoctor = models.ForeignKey(Live_Doctor, blank=True, null=True)
    livedoctorName = models.TextField(default='', blank=True, null=True)
    category = models.CharField(max_length=150, blank=True, null=True)
    clinic = models.ForeignKey(OrganisationName, blank=True, null=True)
    spon_cc_rank = models.CharField(max_length=50, blank=True, null=True)
    spon_clc_rank = models.CharField(max_length=50, blank=True, null=True)
    spon_cc_key = models.CharField(max_length=20, blank=True, null=True)
    spon_clc_key = models.CharField(max_length=20, blank=True, null=True)
    spon_cc_key_label = models.TextField(blank=True, null=True)
    spon_clc_key_label = models.TextField(blank=True, null=True)

    updatedBy = models.TextField(default='', blank=True, null=True)  # Cms username / Front-end
    # updatedBy = models.ForeignKey('auth.User',null=True,blank=True,default=current_user.get_current_user)  # Cms username / Front-end
    livedoctorCurrentUser = models.TextField(default='', blank=True, null=True)  # Live doctor's stage
    livedoctorStage = models.TextField(default='', blank=True, null=True)  # Live doctor's stage

    days_left_cc = models.IntegerField(default=None,null=True)
    expiry_date_cc = models.DateField(blank=True,null=True)

    days_left_clc = models.IntegerField(default=None,null=True)
    expiry_date_clc = models.DateField(blank=True, null=True)

    update_Type = models.TextField(default='', blank=True, null=True)  # LIVE DOCTOR/EDUCATION / EXPERIENCE /
    deelete = models.BooleanField(default=False, help_text='Delete Notification')

    def __unicode__(self):
        return '%s' % (self.notification_creation_date.strftime('%d/%m/%Y - %H:%M:%S'))

class Doctor_Schedule_Stopdate_Notification(models.Model):
    notification_creation_date = models.DateTimeField(auto_now_add=True, blank=True,
                                                      null=True)  # This field will be

    updatedAt = models.DateTimeField(auto_now=True, blank=True, null=True)

    doctor = models.ForeignKey(Doctor, blank=True, null=True)
    doctorName = models.TextField(default='', blank=True, null=True)
    category = models.CharField(max_length=150, blank=True, null=True)
    clinic = models.ForeignKey(OrganisationName, blank=True, null=True)
    spon_cc_rank = models.CharField(max_length=50, blank=True, null=True)
    spon_clc_rank = models.CharField(max_length=50, blank=True, null=True)
    spon_cc_key = models.CharField(max_length=20, blank=True, null=True)
    spon_clc_key = models.CharField(max_length=20, blank=True, null=True)
    spon_cc_key_label = models.TextField(blank=True, null=True)
    spon_clc_key_label = models.TextField(blank=True, null=True)

    updatedBy = models.TextField(default='', blank=True, null=True)  # Cms username / Front-end
    # updatedBy = models.ForeignKey('auth.User',null=True,blank=True,default=current_user.get_current_user)  # Cms username / Front-end
    doctorCurrentUser = models.TextField(default='', blank=True, null=True)  # Live doctor's stage
    doctorStage = models.TextField(default='', blank=True, null=True)  # Live doctor's stage

    days_left_cc = models.IntegerField(default=None, null=True)
    expiry_date_cc = models.DateField(blank=True, null=True)

    days_left_clc = models.IntegerField(default=None, null=True)
    expiry_date_clc = models.DateField(blank=True, null=True)

    update_Type = models.TextField(default='', blank=True, null=True)  # LIVE DOCTOR/EDUCATION / EXPERIENCE /
    deelete = models.BooleanField(default=False, help_text='Delete Notification')

    def __unicode__(self):
        return '%s' % (self.notification_creation_date.strftime('%d/%m/%Y - %H:%M:%S'))

class Doctor_Schedule_Delete_Notification(models.Model):
    notification_creation_date = models.DateTimeField(auto_now_add=True, blank=True,
                                                      null=True)  # This field will be

    updatedAt = models.DateTimeField(auto_now=True, blank=True, null=True)

    doctor = models.ForeignKey(Doctor, blank=True, null=True)
    doctorName = models.TextField(default='', blank=True, null=True)
    category = models.CharField(max_length=150, blank=True, null=True)
    clinic = models.ForeignKey(OrganisationName, blank=True, null=True)
    spon_cc_rank = models.CharField(max_length=50, blank=True, null=True)
    spon_clc_rank = models.CharField(max_length=50, blank=True, null=True)
    spon_cc_key = models.CharField(max_length=20, blank=True, null=True)
    spon_clc_key = models.CharField(max_length=20, blank=True, null=True)
    spon_cc_key_label = models.TextField(blank=True, null=True)
    spon_clc_key_label = models.TextField(blank=True, null=True)

    updatedBy = models.TextField(default='', blank=True, null=True)  # Cms username / Front-end
    # updatedBy = models.ForeignKey('auth.User',null=True,blank=True,default=current_user.get_current_user)  # Cms username / Front-end
    doctorCurrentUser = models.TextField(default='', blank=True, null=True)  # Live doctor's stage
    doctorStage = models.TextField(default='', blank=True, null=True)  # Live doctor's stage

    update_Type = models.TextField(default='', blank=True, null=True)  # LIVE DOCTOR/EDUCATION / EXPERIENCE /
    deelete = models.BooleanField(default=False, help_text='Delete Notification')

    def __unicode__(self):
        return '%s' % (self.notification_creation_date.strftime('%d/%m/%Y - %H:%M:%S'))


# >>>>>>>>>>>>>   models 29Nv17  Start <<<<<<<<<<<<<<<<<<<<

# STEP2 FOR SO

#Import Hemali ma'am sheet here
class ttteempp_for_association_so(models.Model):
   soid = models.IntegerField(null=True)
   soname = models.TextField(blank=True, null=True)
   categories = models.TextField(blank=True, null=True)
#
# #from ttteempp_for_association_so  above populate this table
class ttteempp_for_association_so_2(models.Model):
   soid = models.IntegerField(null=True)
   categoryid = models.IntegerField(null=True)
#
#
# # from ttteempp_for_association_so_2 populate this table
class ttteempp_for_association_so_3(models.Model):
   categoryid = models.IntegerField(null=True)
   categoryname = models.TextField(blank=True, null=True)
   soids = models.TextField(blank=True, null=True)
#
#
# # STEP 3 FOR SPECIALITY
#
#
# #Import Hemali ma'am sheet here
class ttteempp_for_association_spe(models.Model):
   speid = models.IntegerField(null=True)
   spename = models.TextField(blank=True, null=True)
   categories = models.TextField(blank=True, null=True)
#
# #from ttteempp_for_association_spe above populate this table
class ttteempp_for_association_spe_2(models.Model):
   speid = models.IntegerField(null=True)
   categoryid = models.IntegerField(null=True)
#
#
# # from ttteempp_for_association_spe_2 populate this table
class ttteempp_for_association_spe_3(models.Model):
   categoryid = models.IntegerField(null=True)
   categoryname = models.TextField(blank=True, null=True)
   speids = models.TextField(blank=True, null=True)

# >>>>>>>>>>>>>   models 29Nv17  End <<<<<<<<<<<<<<<<<<<<

# class Occupied_ranks(models.Model):
#     doctor = JSONField(default={'CC':{'Sponsored':{},'Subscribed':{},'trial':{}},'CLC':{'Sponsored':{},'Subscribed':{},'trial':{}}} )
#     createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
#     updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)
#     def save(self, *args, **kwargs):
#         now = datetime.now()
#         idd = self.id
#         allobj = Occupied_ranks.objects.all()
#         flag = 0
#         for obj in allobj:
#             if obj.id == idd:
#                 flag = 1
#                 break
#         if flag == 1:
#             self.updatedAt = now
#         else:
#             self.updatedAt = now
#             self.createdAt = now
#         super(Occupied_ranks, self).save(*args, **kwargs)
#
#     # Required for cms
#     def __unicode__(self):
#        return '%s' % ("Occupied Ranks")


class subs_occupied_cc_ranks(models.Model):
    key = models.TextField(null=True,blank=True,unique=True)
    ranklist = JSONField(null=True,default=list())
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = subs_occupied_cc_ranks.objects.all()
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
        super(subs_occupied_cc_ranks, self).save(*args, **kwargs)

    # Required for cms
    def __unicode__(self):
        return '%s' % ("Subscribed CC_Occupied Ranks")

class subs_occupied_clc_ranks(models.Model):
    key = models.TextField(null=True,blank=True,unique=True)
    ranklist = JSONField(null=True,default=list())
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = subs_occupied_clc_ranks.objects.all()
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
        super(subs_occupied_clc_ranks, self).save(*args, **kwargs)

    # Required for cms
    def __unicode__(self):
        return '%s' % ("Subscribed CLC_Occupied Ranks")

class spons_occupied_cc_ranks(models.Model):
    key = models.TextField(null=True,blank=True,unique=True)
    ranklist = JSONField(null=True,default=list())
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = spons_occupied_cc_ranks.objects.all()
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
        super(spons_occupied_cc_ranks, self).save(*args, **kwargs)

    # Required for cms
    def __unicode__(self):
        return '%s' % ("Sponsored CC_Occupied Ranks")

class spons_occupied_clc_ranks(models.Model):
    key = models.TextField(null=True,blank=True,unique=True)
    ranklist = JSONField(null=True,default=list())
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = spons_occupied_clc_ranks.objects.all()
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
        super(spons_occupied_clc_ranks, self).save(*args, **kwargs)

    # Required for cms
    def __unicode__(self):
        return '%s' % ("Sponsored CLC_Occupied Ranks")