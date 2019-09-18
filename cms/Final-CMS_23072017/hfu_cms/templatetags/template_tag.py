from django import template
from hfu_cms.models import *
from django.db.models import Q

register = template.Library()


####################################################################
# Name - can_edit                                                  #
# Owner - Visnu Badal                                              #
#                                                                  #
#                                                                  #
####################################################################

@register.filter(name='can_edit')
def can_edit(user, obj=None):
    user_can_edit = False
    if not user.is_superuser:
        user_can_edit = True
    return user_can_edit





####################################################################
# Name - can_view_admin                                            #
# Owner - Visnu Badal                                              #
#                                                                  #
#                                                                  #
####################################################################

@register.filter(name='can_view_admin')
def can_view_admin(user, obj=None):
    user_can_view_admin = False
    if user.is_superuser:
        user_can_view_admin = True
    return user_can_view_admin


####################################################################
# Name - can_view_caller                                           #
# Owner - Visnu Badal                                              #
#                                                                  #
#                                                                  #
####################################################################

@register.filter(name='can_view_caller')
def can_view_caller(user, obj=None):
    user_can_view_caller = False
    user = UserManagement.objects.filter(user_id=user.id, is_caller=True)
    if user:
        user_can_view_caller = True
    return user_can_view_caller

####################################################################
# Name - can_view_reviewer                                    #
# Owner - Visnu Badal                                              #
#                                                                  #
#                                                                  #
####################################################################

@register.filter(name='can_view_reviewer')
def can_view_reviewer(user, obj=None):
    user_can_view_reviewer = False
    user = UserManagement.objects.filter(user_id=user.id, is_reviewer=True)
    if user:
        user_can_view_reviewer = True
    return user_can_view_reviewer


####################################################################
# Name - can_view_review                                           #
# Owner - Visnu Badal                                              #
#                                                                  #
#                                                                  #
####################################################################

@register.filter(name='can_view_review')
def can_view_review(user, obj=None):
    user_can_view_review = False
    #user = UserManagement.objects.filter(user_id=user.id, is_doctor_reviewer=True)
    user = UserManagement.objects.filter(user_id=user.id, is_reviewer=True)
    if user:
        user_can_view_review = True
    return user_can_view_review


####################################################################
# Name - can_view_review_doc_org                                   #
# Owner - Visnu Badal                                              #
#                                                                  #
#                                                                  #
####################################################################

@register.filter(name='can_view_review_doc_org')
def can_view_review_doc_org(user, obj=None):
    user_can_view_review_doc_org = False
    user = UserManagement.objects.filter(user_id=user.id,is_reviewer=True, is_doctor_reviewer=True)
    if user:
        user_can_view_review_doc_org = True
    return user_can_view_review_doc_org

@register.filter(name='can_view_review_physio_rehab')
def can_view_review_physio_rehab(user, obj=None):
    user_can_view_review_physio_rehab = False
    user = UserManagement.objects.filter(user_id=user.id,is_reviewer=True, is_physio_rehab_reviewer=True)
    if user:
        user_can_view_review_physio_rehab = True
    return user_can_view_review_physio_rehab


####################################################################
# Name - can_view_caller_doc_org                                   #
# Owner - Visnu Badal                                              #
#                                                                  #
#                                                                  #
####################################################################

@register.filter(name='can_view_caller_doc_org')
def can_view_caller_doc_org(user, obj=None):
    user_can_view_caller_doc_org = False
    user = UserManagement.objects.filter(user_id=user.id,is_caller=True ,is_doctor_caller=True)
    if user:
        user_can_view_caller_doc_org = True
    return user_can_view_caller_doc_org

####################################################################
# Name - can_view_review_news                                      #
# Owner - Visnu Badal                                              #
#                                                                  #
#                                                                  #
####################################################################

@register.filter(name='can_view_review_news')
def can_view_review_news(user, obj=None):
    user_can_view_review_news = False
    user = UserManagement.objects.filter(user_id=user.id,is_news_reviewer=True)
    if user:
        user_can_view_review_news = True
    return user_can_view_review_news


####################################################################
# Name - can_view_news                                             #
# Owner - Visnu Badal                                              #
#                                                                  #
#                                                                  #
####################################################################

@register.filter(name='can_view_news')
def can_view_news(user, obj=None):
    user_can_view_news = False
    user = UserManagement.objects.filter(user_id=user.id, is_news=True)
    if user:
        user_can_view_news = True
    return user_can_view_news



####################################################################
# Name - is_service_reviewer                                       #
# Owner - Visnu Badal                                              #
#                                                                  #
#                                                                  #
####################################################################

@register.filter(name='is_service_reviewer')
def is_service_reviewer(user, obj=None):
    user_can_view_service_reviewer = False
    user = UserManagement.objects.filter(user_id=user.id, is_service_reviewer=True)
    if user:
        user_can_view_service_reviewer = True
    return user_can_view_service_reviewer

####################################################################
# Name - can_view_service_caller                                   #
# Owner - Visnu Badal                                              #
#                                                                  #
#                                                                  #
####################################################################

@register.filter(name='is_service_caller')
def can_view_service_caller(user, obj=None):
    user_can_view_service_caller = False
    user = UserManagement.objects.filter(user_id=user.id, is_service_plan=True)
    if user:
        user_can_view_service_caller = True
    return user_can_view_service_caller


####################################################################
# Name - can_view_review_path                                      #
# Owner - Nishank                                                  #
#                                                                  #
#                                                                  #
####################################################################

@register.filter(name='can_view_review_pathlab')
def can_view_review_pathlab(user, obj=None):
    user_can_view_pathlab = False
    user = UserManagement.objects.filter(Q(user_id=user.id) & Q(is_reviewer=True) & Q(is_path_reviewer=True))
    if user:
        user_can_view_pathlab = True
    return user_can_view_pathlab


####################################################################
# Name - can_view_caller_pathlab                                   #
# Owner - Nishank                                                  #
#                                                                  #
#                                                                  #
####################################################################

@register.filter(name='can_view_caller_pathlab')
def can_view_caller_pathlab(user, obj=None):
    user_can_view_pathlab = False
    user = UserManagement.objects.filter(Q(user_id=user.id) & Q(is_caller=True) & Q(is_path_caller=True))
    if user:
        user_can_view_pathlab = True
    return user_can_view_pathlab

####################################################################
# Name - can_view_review_pharma                                    #
# Owner - Nishank                                                  #
#                                                                  #
#                                                                  #
####################################################################

@register.filter(name='can_view_review_pharma')
def can_view_review_pharma(user, obj=None):
    user_can_view_phar = False
    user = UserManagement.objects.filter(Q(user_id=user.id) & Q(is_reviewer=True) & Q(is_phar_reviewer=True))
    if user:
        user_can_view_phar = True
    return user_can_view_phar

####################################################################
# Name - can_view_caller_pharma                                    #
# Owner - Nishank                                                  #
#                                                                  #
#                                                                  #
####################################################################

@register.filter(name='can_view_caller_pharma')
def can_view_caller_pharma(user, obj=None):
    user_can_view_phar = False
    user = UserManagement.objects.filter(Q(user_id=user.id) & Q(is_caller=True) & Q(is_phar_caller=True))
    if user:
        user_can_view_phar = True
    return user_can_view_phar


####################################################################
# Name - can_view_review_ambu                                      #
# Owner - Nishank                                                  #
#                                                                  #
#                                                                  #
####################################################################

@register.filter(name='can_view_review_ambulance')
def can_view_review_ambu(user, obj=None):
    user_can_view_ambu = False
    user = UserManagement.objects.filter(Q(user_id=user.id) & Q(is_reviewer=True) & Q(is_ambulance_reviewer=True))
    if user:
        user_can_view_ambu = True
    return user_can_view_ambu

####################################################################
# Name - can_view_caller_ambu                                      #
# Owner - Nishank                                                  #
#                                                                  #
#                                                                  #
####################################################################

@register.filter(name='can_view_caller_ambulance')
def can_view_caller_ambu(user, obj=None):
    user_can_view_ambu = False
    user = UserManagement.objects.filter(Q(user_id=user.id) & Q(is_caller=True) & Q(is_ambulance_caller=True))
    if user:
        user_can_view_ambu = True
    return user_can_view_ambu

####################################################################
# Name - can_view_review_blood                                     #
# Owner - Nishank                                                  #
#                                                                  #
#                                                                  #
####################################################################

@register.filter(name='can_view_review_bloodbank')
def can_view_review_bloodbank(user, obj=None):
    user_can_view_blood = False
    user = UserManagement.objects.filter(Q(user_id=user.id) & Q(is_reviewer=True) & Q(is_blood_reviewer=True))
    if user:
        user_can_view_blood = True
    return user_can_view_blood


####################################################################
# Name - can_view_caller_blood                                     #
# Owner - Nishank                                                  #
#                                                                  #
#                                                                  #
####################################################################

@register.filter(name='can_view_caller_bloodbank')
def can_view_caller_bloodbank(user, obj=None):
    user_can_view_blood = False
    user = UserManagement.objects.filter(Q(user_id=user.id) & Q(is_caller=True) & Q(is_blood_caller=True))
    if user:
        user_can_view_blood = True
    return user_can_view_blood


####################################################################
# Name - can_view_review_disease                                   #
# Owner - Nishank                                                  #
#                                                                  #
#                                                                  #
####################################################################

@register.filter(name='can_view_review_disease')
def can_view_review_disease(user, obj=None):
    user_can_view_disease = False
    user = UserManagement.objects.filter(Q(user_id=user.id) & Q(is_reviewer=True) & Q(is_disease_reviewer=True))
    if user:
        user_can_view_disease = True
    return user_can_view_disease


####################################################################
# Name - can_view_caller_disease                                   #
# Owner - Nishank                                                  #
#                                                                  #
#                                                                  #
####################################################################

@register.filter(name='can_view_caller_disease')
def can_view_caller_disease(user, obj=None):
    user_can_view_disease = False
    user = UserManagement.objects.filter(Q(user_id=user.id) & Q(is_caller=True) & Q(is_disease_caller=True))
    if user:
        user_can_view_disease = True
    return user_can_view_disease

####################################################################
# Name - can_view_publisher                                        #
# Owner - Visnu Badal                                              #
#                                                                  #
#                                                                  #
####################################################################

@register.filter(name='can_view_publisher')
def can_view_publisher(user, obj=None):
    user_can_view_publisher = False
    user = UserManagement.objects.filter(user_id=user.id, is_publisher=True)
    if user:
        user_can_view_publisher = True
    return user_can_view_publisher


@register.filter(name='doctor_name')
def return_doctor_name(doctor_id, organisation_id=None):
    if doctor_id:
        doctor_name_data = Doctor.objects.get(pk=doctor_id)
        dname = doctor_name_data.name
    else:
        dname = None
    return dname


@register.filter(name='organisation_name')
def return_organisation_name(organisation_id):
    if organisation_id:
        organisation_name_data = OrganisationName.objects.get(pk=organisation_id)
        dname = organisation_name_data.name
    else:
        dname = None
    return dname


""" speciality tag"""


@register.filter(name='speciality')
def speciality(value):
    speciality_str = ''
    try:
        if value:
            value = map(int, value.split(','))
            if len(value):
                Speciality_list = Speciality.objects.filter(id__in=value).values_list('name', flat=True)
                if Speciality_list:
                    speciality_str = ','.join(Speciality_list)
    except Exception as e:
        print e
    return speciality_str

""" Caller type check tags"""

@register.filter(name='can_view_caller_path')
def can_view_caller_path(user, obj=None):
    user_caller_path = False
    user = UserManagement.objects.filter(Q(user_id=user.id) & Q(is_caller=True) & Q(is_path_caller=True))
    if user:
        user_caller_path = True
    return user_caller_path


@register.filter(name='can_view_caller_pharma')
def can_view_caller_pharma(user, obj=None):
    user_caller_pharma = False
    user = UserManagement.objects.filter(Q(user_id=user.id) & Q(is_caller=True) & Q(is_phar_caller=True))
    if user:
        user_caller_pharma = True
    return user_caller_pharma

@register.filter(name='can_view_caller_doctor')
def can_view_caller_doctor(user,obj=None):
    user_caller_doctor = False
    user = UserManagement.objects.filter(Q(user_id=user.id) & Q(is_caller=True) & Q(is_doctor_caller=True))
    if user:
        user_caller_doctor = True
    return  user_caller_doctor

@register.filter(name='can_view_caller_physio_rehab')
def can_view_caller_physio_rehab(user,obj=None):
    user_caller_physio_rehab = False
    user = UserManagement.objects.filter(Q(user_id=user.id) & Q(is_caller=True) & Q(is_physio_rehab_caller=True))
    if user:
        user_caller_physio_rehab = True
    return  user_caller_physio_rehab


@register.filter(name='can_view_caller_bloodbank')
def can_view_caller_bloodbank(user, obj=None):
    user_caller_bb = False
    user = UserManagement.objects.filter(Q(user_id=user.id) & Q(is_caller=True) & Q(is_blood_caller=True))
    if user:
        user_caller_bb = True
    return  user_caller_bb

@register.filter(name='can_view_caller_ambulance')
def can_view_caller_ambulance(user, obj=None):
    user_caller_amb = False
    user = UserManagement.objects.filter(Q(user_id=user.id) & Q(is_caller=True) & Q(is_ambulance_caller=True))
    if user:
        user_caller_amb = True
    return  user_caller_amb

@register.filter(name='can_view_caller_disease')
def can_view_caller_disease(user, obj=None):
    user_caller_disease = False
    user = UserManagement.objects.filter(Q(user_id=user.id) & Q(is_caller=True) & Q(is_disease_caller =True))
    if user:
        user_caller_disease = True
    return  user_caller_disease



####################################################################
# Name - can_view_review_path                                      #
# Owner - Nishank                                                  #
#                                                                  #
#                                                                  #
####################################################################
@register.filter(name='can_view_reviewer_nurse_bureau')
def can_view_review_nurse_bureau(user, obj=None):
    user_can_view_nurse_bureau = False
    user = UserManagement.objects.filter(Q(user_id=user.id) & Q(is_reviewer=True) & Q(is_nurse_bureau_reviewer=True))
    if user:
        user_can_view_nurse_bureau = True
    return user_can_view_nurse_bureau

####################################################################
# Name - can_view_caller_pathlab                                   #
# Owner - Nishank                                                  #
#                                                                  #
#                                                                  #
####################################################################

@register.filter(name='can_view_caller_nurse_bureau')
def can_view_caller_nurse_bureau(user, obj=None):
    can_view_caller_nurse_bureau = False
    user = UserManagement.objects.filter(Q(user_id=user.id) & Q(is_caller=True) & Q(is_nurse_bureau_caller=True))
    if user:
        can_view_caller_nurse_bureau = True
    return can_view_caller_nurse_bureau


####################################################################
# Name - can_view_review_DIET                                      #
# Owner - Nishank                                                  #
#                                                                  #
#                                                                  #
####################################################################
@register.filter(name='can_view_reviewer_dietitian')
def can_view_review_dietitian(user, obj=None):
    user_can_view_dietitian = False
    user = UserManagement.objects.filter(Q(user_id=user.id) & Q(is_reviewer=True) & Q(is_dietitian_reviewer=True))
    if user:
        user_can_view_dietitian = True
    return user_can_view_dietitian

####################################################################
# Name - can_view_review_therapist                                 #
# Owner - Nishank                                                  #
#                                                                  #
#                                                                  #
####################################################################
@register.filter(name='can_view_reviewer_therapist')
def can_view_review_therapist(user, obj=None):
    user_can_view_therapist = False
    user = UserManagement.objects.filter(Q(user_id=user.id) & Q(is_reviewer=True) & Q(is_therapist_reviewer=True))
    if user:
        user_can_view_therapist = True
    return user_can_view_therapist

####################################################################
# Name - can_view_caller_dietitian                                 #
# Owner - Nishank                                                  #
#                                                                  #
#                                                                  #
####################################################################
@register.filter(name='can_view_caller_dietitian')
def can_view_caller_dietitian(user, obj=None):
    can_view_caller_dietitian = False
    user = UserManagement.objects.filter(Q(user_id=user.id) & Q(is_caller=True) & Q(is_dietitian_caller=True))
    if user:
        can_view_caller_dietitian = True
    return can_view_caller_dietitian

####################################################################
# Name - can_view_caller_therapist                                 #
# Owner - Nishank                                                  #
#                                                                  #
#                                                                  #
####################################################################
@register.filter(name='can_view_caller_therapist')
def can_view_caller_therapist(user, obj=None):
    can_view_caller_therapist = False
    user = UserManagement.objects.filter(Q(user_id=user.id) & Q(is_caller=True) & Q(is_therapist_caller=True))
    if user:
        can_view_caller_therapist = True
    return can_view_caller_therapist


####################################################################
# Name - is_doctor_reviewer                                        #
# BY Nishank                                                       #
####################################################################
@register.filter(name='is_doctor_reviewer')
def is_doctor_reviewer(user, obj=None):
    user_can_view_review = False
    user_permissions = None
    try:
        user_permissions = UserManagement.objects.filter(user_id=user.id, is_doctor_reviewer=True)
    except:
        user_permissions = None
    if user_permissions:
        user_can_view_review = True
    return user_can_view_review

####################################################################
# Name - check_org_previous_user                                   #
# BY Nishank                                                       #
####################################################################
@register.filter(name='check_org_previous_user')
def check_org_previous_user(org, obj=None):
    try:
        if org.previous_user == None:
            return False
        else:
            qs = UserManagement.objects.filter(user_id = org.previous_user)
            if len(qs) != 0:
                return True
            else:
                return False
    except Exception as e :
        return False


####################################################################
# Name - get_current_departments                                   #
# BY Nishank                                                       #
####################################################################
@register.filter(name='get_current_departments')
def get_current_departments(deparments = None, obj=None):
    try:
        if deparments == None or deparments =='' or deparments ==' ':
            return False
        else:
            current_departments = []
            try:
                tempde = deparments.split(',')
                for dep in tempde:
                    dobj = Department.objects.get(id = int(dep.strip()))
                    current_departments.append(dobj)
                return current_departments
            except:
                pass
    except Exception as e :
        return False

####################################################################
# Name - check_if_talktodoc_is_true                                #
# BY Nishank                                                       #
####################################################################
@register.filter(name='check_if_talktodoc_is_true')
def check_org_previous_user(doc=None):

    try:
        asso_obj = Live_Doctor_Associated_Data.objects.get(doctor_id=doc.id)
        if asso_obj.talk_to_doc == True:
            return True
        else:
            return False

    except Exception as e :
        return False


####################################################################
# Name - get_doctor_name                                           #
# BY Nishank                                                       #
####################################################################
@register.filter(name='get_doctor_name')
def get_doctor_name(doc_id=None):
    try:
        doc = Live_Doctor.objects.get(id=doc_id)
        if doc :

            return doc.firstName + ' ' + doc.lastName
        else:
            return None

    except Exception as e :
        return None

####################################################################
# Date - 9th June                                                    #
# Owner - Ashutosh                                                   #
#                                                                    #
#                                                                    #
####################################################################
@register.filter(name='getdepartment')
def getdepartment(dep):
    department_obj = Department.objects.all().values('id')
    strr=""
    if not dep:
        return "--No department--"
    else:
        lis=dep.split(',')
        for v in department_obj:
            if str(v['id']) in lis:
                j = Department.objects.get(id=v['id'])
                if not strr:
                    strr = j.name
                else:
                    strr=strr+",  "+j.name
    return strr


####################################################################
# Date - 9th june                                                    #
# Owner - Ashutosh                                                   #
#                                                                    #
#                                                                    #
####################################################################
@register.filter(name='getdoctorname')
def getdoctorname(doc_id):
    Live_Doctor_obj=Live_Doctor.objects.get(id=doc_id)
    name = Live_Doctor_obj.firstName +Live_Doctor_obj.lastName
    return name


####################################################################
# Name - get_category     #17June Nishank                          #
# BY Nishank                                                       #
####################################################################
@register.filter(name='get_category')
def get_category(cat_id=None):
    try:
        cat = Category.objects.get(id=cat_id)
        if cat :
            return cat.name.strip()
        else:
            return cat_id
    except Exception as e :
        return cat_id

####################################################################
# Name - get_association_so_list           #17June Nishank         #
# BY Nishank                                                       #
####################################################################
@register.filter(name='get_association_so_list')
def get_association_so_list(so_ids=None):
    try:
        if so_ids != None and so_ids != '' and so_ids != ' ' :
            so_ids = so_ids.strip()
            li = so_ids.split(',')
            return li
        else:
            return []
    except Exception as e :
        return []

####################################################################
# Name - get_association_spl_list           #17June Nishank        #
# BY Nishank                                                       #
####################################################################
@register.filter(name='get_association_spl_list')
def get_association_spl_list(spl_ids=None):
    try:
        if spl_ids != None and spl_ids != '' and spl_ids != ' ' :
            spl_ids = spl_ids.strip()
            li = spl_ids.split(',')
            return li
        else:
            return []
    except Exception as e :
        return []

####################################################################
# Name - check if article already in related topics list           #
# BY Nishank                                                       #
####################################################################
@register.filter(name='article_exist')
def article_exist(article_id=None):
    from news.models import Doctorsfeed
    try:
        article_id = str(article_id)
        article_exist = False
        obj = Doctorsfeed.objects.all()
        for o in obj:
            t = o.related_topics.split(',')
            for i in t:
                if str(i) == article_id:
                    article_exist = True
        return article_exist
    except Exception as e :
        return False

####################################################################
# Name -showcategory                                               #
# Owner - Ashutosh Kesharvani                                      #
#                                                                  #
#                                                                  #
####################################################################
@register.filter(name='showcategory')
def showcategory(catid=None):
    if catid:
        category = Category.objects.get(id = catid)
        print category
    return category

            # ####################################################################
# # Name - get_association_spl_list           #17June Nishank        #
# # BY Nishank                                                       #
# ####################################################################
# @register.filter(name='get_association_spl_list')
# def get_association_spl_list(spl_ids=None):
#     try:
#         if spl_ids != None and spl_ids != '' and spl_ids != ' ' :
#             spl_ids = spl_ids.strip()
#             li = spl_ids.split(',')
#             return li
#         else:
#             return []
#     except Exception as e :
#         return []

####################################################################
# Name - can_view_review_live_doc                                  #
# Date - 23-08-2017                                                #
# By Dhrumil                                                       #
####################################################################
@register.filter(name='can_view_review_live_doc')
def can_view_review_live_doc(user, obj=None):
    user_can_view_review_live_doc = False
    user = UserManagement.objects.filter(user_id=user.id,is_reviewer=True, is_live_doctor_reviewer=True)
    if user:
        user_can_view_review_live_doc = True
    return user_can_view_review_live_doc

####################################################################
# Name - can_view_review_live_doc                                  #
# Date - 23-08-2017                                                #
# By Dhrumil                                                       #
####################################################################
@register.filter(name='can_view_caller_live_doc')
def can_view_caller_live_doc(user, obj=None):
    user_can_view_caller_live_doc = False
    user = UserManagement.objects.filter(user_id=user.id,is_caller=True ,is_live_doctor_caller=True)
    if user:
        user_can_view_caller_live_doc = True
    return user_can_view_caller_live_doc

@register.filter(name='show_dob')
def show_dob(d = None):
    try:
        print d
        dob = d.split('T')
        t = dob[0].split('-')
        tt = t[2] +'-'+ t[1]+'-' + t[0]
        return tt
    except:
        dob = d.split('T')
        return dob[0]
####################################################################
# Name - Datetime format 1                                         #
# By Nishank                                                       #
####################################################################
@register.filter(name='datetimeFormat1')
def datetimeFormat1(datetime_obj=None):
    if datetime_obj :
        from pytz import timezone
        datetime_obj = datetime_obj.astimezone(timezone('Asia/Kolkata'))
        datetime_obj = datetime_obj.strftime('%d/%m/%Y')
    return datetime_obj

####################################################################
# Name - Datetime format 2                                         #
# By Nishank                                                       #
####################################################################
@register.filter(name='datetimeFormattwo')
def datetimeFormattwo(datetime_obj=None):
    if datetime_obj :
        from pytz import timezone
        datetime_obj = datetime_obj.astimezone(timezone('Asia/Kolkata'))
        datetime_obj = datetime_obj.strftime('%d/%m/%Y - %H:%M:%S')
    return datetime_obj


####################################################################
# Name - get_key_type                                              #
# By Nishank                                                       #
####################################################################
@register.filter(name='get_key_type')
def get_key_type(keyobj=None):
    if keyobj :
        if type(keyobj) == int:
            return 'int'
        else:
            return 'not int'

####################################################################
# Name - sort_dict                                                 #
# By Nishank                                                       #
####################################################################
@register.filter(name='sort_dict')
def sort_dict(dictobj=None):
    try :
        if dictobj :
            sd = sorted(dictobj)
            return sd
    except:
        return dictobj


