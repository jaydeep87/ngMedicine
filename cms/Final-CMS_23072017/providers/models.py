from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
import uuid
from django.contrib.postgres.fields import JSONField
from hfu_cms.models import *

# Create your models here.


# plan category Master
# Added By Vishnu
class PlanCategory(models.Model):
    name = models.CharField(max_length=500, null=True)
    is_delete = models.BooleanField(default=False)
    # Field added by Ashutosh on 19 July
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = PlanCategory.objects.all()
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
        super(PlanCategory, self).save(*args, **kwargs)
# Business Master


class BusinessType(models.Model):
    name = models.CharField(max_length=200)
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = PlanCategory.objects.all()
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
        super(PlanCategory, self).save(*args, **kwargs)
    class Meta:
        ordering = ('name',)


class ServiceProvider(models.Model):
    stage = models.ForeignKey(Stage, null=True)
    current_user = models.ForeignKey(User, null=True)
    business_type = models.ForeignKey(BusinessType)
    previous_user = models.IntegerField(null=True)
    free_text = models.TextField(max_length=5000, help_text='', blank=True, null=True)
    enterprise_service_provider = models.BooleanField(default=False)
    home_service_provider = models.BooleanField(default=False)
    life_service_provider = models.BooleanField(default=False)

    added_on = models.DateTimeField(auto_now=True)

    # Organisational Details
    provider_unique_id = models.CharField(null=True, default=uuid.uuid4, blank=True, max_length=200, unique=True)
    hs_list = models.CharField(null=True, blank=True, max_length=1000)
    ls_list = models.CharField(null=True, blank=True, max_length=1000)
    es_list = models.CharField(null=True, blank=True, max_length=1000)
    organisation_name = models.CharField(null=True, blank=True, max_length=1000)
    owner_name = models.CharField(null=True, blank=True, max_length=200)
    years_in_service = models.CharField(null=True, blank=True, max_length=200)
    quality_certification = models.CharField(null=True, blank=True, max_length=200)
    website = models.CharField(null=True, blank=True, max_length=200)

    # contact details

    person_name = models.CharField(null=True, blank=True, max_length=200)
    mobile = models.CharField(null=True, blank=True, max_length=200)
    email = models.CharField(null=True, blank=True, max_length=200)

    # Address Details:

    # Registered Office Address

    r_house_door_bldg_no = models.CharField(null=True, blank=True, max_length=200)
    r_street = models.CharField(null=True, blank=True, max_length=200)
    r_location = models.CharField(null=True, blank=True, max_length=200)
    r_city = models.CharField(null=True, blank=True, max_length=200)
    r_state = models.CharField(null=True, blank=True, max_length=200)
    r_zip_code = models.CharField(null=True, blank=True, max_length=200)
    r_phone_number = models.CharField(null=True, blank=True, max_length=200)

    # Correspondence Address

    c_house_door_bldg_no = models.CharField(null=True, blank=True, max_length=200)
    c_street = models.CharField(null=True, blank=True, max_length=200)
    c_location = models.CharField(null=True, blank=True, max_length=200)
    c_city = models.CharField(null=True, blank=True, max_length=200)
    c_state = models.CharField(null=True, blank=True, max_length=200)
    c_zip_code = models.CharField(null=True, blank=True, max_length=200)
    c_phone_number = models.CharField(null=True, blank=True, max_length=200)
    # Bank Details
    beneficiary_name = models.CharField(null=True, blank=True, max_length=200)
    bank_name = models.CharField(null=True, blank=True, max_length=200)
    branch_name = models.CharField(null=True, blank=True, max_length=200)
    account_no = models.CharField(null=True, blank=True, max_length=200)
    ifsc_code = models.CharField(null=True, blank=True, max_length=200)

    # Some New Field Added Here
    certification_validity = models.CharField(null=True, blank=True, max_length=200)
    preferred_location = models.CharField(null=True, blank=True, max_length=200)
    tat = models.CharField(null=True, blank=True, max_length=500)
    home_rate_card = models.FileField(upload_to='rate_card/', null=True)
    life_rate_card = models.FileField(upload_to='rate_card/', null=True)
    enterprise_rate_card = models.FileField(upload_to='rate_card/', null=True)
    remarks = models.TextField(null=True)

    # Field added by Ashutosh on 19 July
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = ServiceProvider.objects.all()
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
        super(ServiceProvider, self).save(*args, **kwargs)
    class Meta:
        ordering = ('organisation_name',)


class Kurable_subtype_master(models.Model):
    name = models.CharField(max_length=10000, help_text='Name')
    delete = models.BooleanField(default=False, help_text='Deactivate_Kurablesub_Type')

    # Field added by Ashutosh on 19 July
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Kurable_subtype_master.objects.all()
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
        super(Kurable_subtype_master, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name

class Healthoholic_subtype_master(models.Model):
    name = models.CharField(max_length=10000, help_text='Name')
    delete = models.BooleanField(default=False, help_text='Deactivate_Kurablesub_Type')

    # Field added by Ashutosh on 19 July
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = Healthoholic_subtype_master.objects.all()
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
        super(Healthoholic_subtype_master, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name

class CaResidense_subtype_master(models.Model):
    name = models.CharField(max_length=10000, help_text='Name')
    delete = models.BooleanField(default=False, help_text='Deactivate_Kurablesub_Type')

    # Field added by Ashutosh on 19 July
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = CaResidense_subtype_master.objects.all()
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
        super(CaResidense_subtype_master, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name

class ServicePlan(models.Model):
    stage = models.ForeignKey(Stage, null=True)
    current_user = models.ForeignKey(User, null=True)
    previous_user = models.IntegerField(null=True)
    free_text = models.TextField(max_length=5000, help_text='', blank=True, null=True)
    provider = models.ForeignKey(ServiceProvider)
    # Added by Vishnu
    plan_category = models.ForeignKey(PlanCategory, null=True)
    no_of_employee = models.IntegerField(null=True, blank=True)
    plan_name = models.CharField(null=True, blank=True, max_length=200)
    plan_title = models.CharField(null=True, blank=True, max_length=200)
    plan_price = models.FloatField(null=True, blank=True, max_length=200)
    # Added by Vishnu
    investigation = JSONField(null=True)
    consultation = JSONField(null=True)
    imaging = JSONField(null=True)

    # Renamed to Others 26 DECEMBER
    #blood_bank = JSONField(null=True)
    others = JSONField(null=True)

    package_description = models.CharField(max_length=1000, null=True)
    # End
    discount_on_plan = models.FloatField(null=True, blank=True)
    price_of_plan_after_discount = models.FloatField(null=True, blank=True, max_length=50)
    plan_validity = models.CharField(null=True, blank=True, max_length=100)
    age_group = models.CharField(null=True, blank=True, max_length=50)
    user_category = models.CharField(null=True, blank=True, max_length=50, help_text='gender')
    # Added By Vishnu
    instructions = models.CharField(null=True, blank=True, max_length=1000)
    timings = models.TextField(null=True)
    image_url = models.CharField(null=True, blank=True, max_length=200)
    need_review = models.BooleanField(default=True)
    activation_status = models.BooleanField(default=True)
    last_reviewed_by = models.ForeignKey(User, null=True, related_name='plan_reviewer_name')
    published_by = models.ForeignKey(User, null=True, related_name='plan_publisher_name')
    submission_date = models.DateField(auto_now=True)
    acceptance_date = models.DateField(null=True, blank=True)
    last_updated_date = models.DateTimeField(auto_now_add=True)
    last_reviewed_on = models.DateTimeField(auto_now_add=True)
    service_offered_in_plan = models.CharField(null=True, blank=True, max_length=300)

    # new field added.....................by.jaydeep
    working_hours = models.CharField(null=True, blank=True, max_length=300)
    corporate_plan = models.BooleanField(default=False)
    nurse_plan = models.BooleanField(default=False)
    wellness_plan = models.BooleanField(default=False)
    hfues_plan = models.BooleanField(default=False)
    is_home_service = models.BooleanField(default=False)  # = care residense id = 2
    is_enterprise_service = models.BooleanField(default=False) # = Healthoholic id = 1
    is_life_service = models.BooleanField(default=False)    # = kurable id = 3

    #Added 26 DECEMBER
    type = models.CharField(max_length=1000, null=True)
    publish = models.BooleanField(default=False)

    kurable_plan_type = models.CharField(max_length=100, default='',null=True,blank=True)
    healthoholic_plan_type = models.CharField(max_length=100, default='',null=True,blank=True)
    caresidense_plan_type = models.CharField(max_length=100, default='',null=True,blank=True)

# Field added by Ashutosh on 19 July
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = ServicePlan.objects.all()
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
        super(ServicePlan, self).save(*args, **kwargs)
# Don't touch this
class PlanAssign(models.Model):
    plan = models.ForeignKey(ServicePlan)
    plan_reviewer = models.ForeignKey(User)
    asked_reviewer = models.BooleanField(default=False)
    revert = models.BooleanField(default=False)
    send_elastic = models.BooleanField(default=False)
    free_text = models.CharField(max_length=5000, help_text='', blank=True, null=True)

    # Field added by Ashutosh on 19 July
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    # Added by Ashutosh on 18 July 2017
    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = PlanAssign.objects.all()
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
        super(PlanAssign, self).save(*args, **kwargs)


#############################################
# Name: Plan Category                       #
# Owner: Dhrumil Shah                       #
#############################################
class PlanCat(models.Model):
    name = models.CharField(max_length=10000, help_text='Name')
    delete = models.BooleanField(default=False, help_text='Deactivate_Plan_Cat')
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = PlanCat.objects.all()
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
        super(PlanCat, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name

#############################################
# Name: Plan Sub Category                   #
# Owner: Dhrumil Shah                       #
#############################################
class PlanSubCat(models.Model):
    name = models.CharField(max_length=10000, help_text='Name')
    category = models.ForeignKey(PlanCat)
    delete = models.BooleanField(default=False, help_text='Deactivate_Plan_SubCat')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = PlanSubCat.objects.all()
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
        super(PlanSubCat, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name

#############################################
# Name: New Plan Module                     #
# Owner: Dhrumil Shah                       #
#############################################

class PlanNew(models.Model):
    stage = models.ForeignKey(Stage, null=True)
    current_user = models.ForeignKey(User, null=True)
    previous_user = models.TextField(User, null=True)
    free_text = models.TextField(max_length=5000, help_text='', blank=True, null=True)
    resource_validate = models.ForeignKey(ValidateByChoice, null=True)
    provider = models.ForeignKey(ServiceProvider)
    plan_category = models.ForeignKey(PlanCat, null=True)
    plan_sub_category = models.ForeignKey(PlanSubCat, null=True)
    other_details = JSONField(null=True)
    activation_status = models.BooleanField(default=True)
    city = models.ForeignKey(Citymaster, null=True)
    test_details = JSONField(null=True)
    total_price = models.IntegerField(null=True, blank=True)
    discounted_price = models.IntegerField(null=True, blank=True)
    publish = models.BooleanField(default=False)

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = PlanNew.objects.all()
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
        super(PlanNew, self).save(*args, **kwargs)

#############################################
# Name: Plan Detail Master                  #
# Owner: Dhrumil Shah                       #
#############################################

class PlanDetails(models.Model):
    name = models.TextField(max_length=500, null=True, blank=True)
    delete = models.BooleanField(default=False, help_text='Deactivate_Plan_Detail')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = PlanDetails.objects.all()
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
        super(PlanDetails, self).save(*args, **kwargs)

#############################################
# Name: Plan Component                      #
# Owner: Dhrumil Shah                       #
#############################################

class PlanComponent(models.Model):
    name = models.TextField(max_length=500, null=True, blank=True)
    plan_details = models.ForeignKey(PlanDetails)
    delete = models.BooleanField(default=False, help_text='Deactivate_Plan_Component')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = PlanComponent.objects.all()
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
        super(PlanComponent, self).save(*args, **kwargs)

#############################################
# Name: Plan Sub Component                  #
# Owner: Dhrumil Shah                       #
#############################################

class PlanSubComponent(models.Model):
    name = models.TextField(max_length=500, null=True, blank=True)
    plan_component = models.ForeignKey(PlanComponent)
    plan_detail = models.ForeignKey(PlanDetails)
    amount = models.IntegerField(null=True)
    delete = models.BooleanField(default=False, help_text='Deactivate_Plan_Sub_Component')

    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', blank=True, null=True)

    def save(self, *args, **kwargs):
        now = datetime.now()
        idd = self.id
        allobj = PlanSubComponent.objects.all()
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
        super(PlanSubComponent, self).save(*args, **kwargs)