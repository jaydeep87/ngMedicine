from .models import *
from news.models import NewsFeed

#Check Doctor

""" Return Doctor """


def return_doc(doctor_id, user_id):
    doctor_obj = Doctor.objects.filter(id=doctor_id, current_user=user_id)
    if len(doctor_obj):
        return doctor_obj
    else:
        return False


""" Return lab """

def return_lab(lab_id, user_id):
    try:
        lab_obj = Labs.objects.get(id=lab_id, current_user=user_id)
        return lab_obj
    except:
        return False

""" Return organisation """

def return_organisation(organisation_id, user_id):
    try:
        organisation_obj = OrganisationName.objects.get(id=organisation_id, current_user=user_id)
        return organisation_obj
    except:
        return False


def check_doctor(doctor_id, user_id, is_super_user=None):
    if is_super_user:
        return True
    else:
        if doctor_id and user_id is not None:
            doctor_obj = Doctor.objects.filter(id=doctor_id, current_user=user_id)
            if len(doctor_obj):
                return True
            else:
                return False
        else:
            return False


def check_organisation_for_schedule(organisation_id, user_id, is_super_user=None):
    if is_super_user:
        return True
    else:
        if organisation_id and user_id is not None:
            organization_obj = OrganisationName.objects.filter(id=organisation_id, current_user=user_id)
            if len(organization_obj):
                return True
            else:
                return False
        else:
            return False


""" Check Organisation Allready attached with Doctor """


def check_organisation(organisation_id, doctor_id):
    if doctor_id and organisation_id is not None:
        attach_obj = AttachWithDoctor.objects.filter(doctor_id=doctor_id, organisation_id=organisation_id)
        if len(attach_obj):
            return True
        else:
            return False
    else:
        return True

""" Check Organisation Edit """


def check_organisation_edit(organisation_id, user_id, is_super_user=None):
    if is_super_user:
        return True
    else:
        if organisation_id and user_id is not None:
            organisation_data = OrganisationName.objects.filter(id=organisation_id, current_user_id=user_id)
            if len(organisation_data):
                return True
            else:
                return False
        else:
            return False

""" Check Organisation complete """


def check_organisation_complete(organisation_id, user_id):
    if organisation_id and user_id is not None:
        organisation_data = OrganisationName.objects.filter(id=organisation_id, current_user_id=user_id)
        if len(organisation_data):
            return organisation_data
        else:
            return False
    else:
        return False


""" Check Point Attach Doctor In Organisation """


def check_attached_doctor_in_publish_stage(organisation_id):
    result_array =[]
    if organisation_id:
        doctor_ass_obj = AssociateDoctorWithOrganization.objects.filter(organisation_id=organisation_id)
        if doctor_ass_obj:
            for d_as in doctor_ass_obj:
                result_obj ={}
                if d_as.doctor.stage_id < 4:
                    result_obj['name'] = d_as.doctor.name
                    result_obj['category'] = d_as.doctor.category.name
                    result_obj['zone'] = d_as.doctor.zone.name
                    result_obj['zone_location'] = d_as.doctor.zone_location.name
                    result_obj['registration_data'] = d_as.doctor.registration_data
                    result_obj['speciality'] = ''
                    if d_as.doctor.speciality:
                        speciality_arr = d_as.doctor.speciality.split(',')
                        speciality_name = Speciality.objects.filter(id__in=speciality_arr).values_list('name',flat=True)
                        result_obj['speciality'] = ','.join(speciality_name)

                    result_array.append(result_obj)
            return result_array
        else:
            return result_array


    else:
        return result_array

""" Check Organisation in doctor attach """


def check_attached_organisation_in_publish_stage(doctor_id):
    result_array =[]
    if doctor_id:
        organisation_ass_obj = AttachWithDoctor.objects.filter(doctor_id=doctor_id)
        if organisation_ass_obj:
            for o_as in organisation_ass_obj:
                result_obj ={}
                if o_as.organisation.stage_id < 4:
                    result_obj['name'] = o_as.organisation.name
                    result_obj['address'] = o_as.organisation.street
                    result_obj['locality'] = o_as.organisation.locality.name
                    result_obj['city'] = o_as.organisation.city.name
                    result_array.append(result_obj)
            return result_array
        else:
            return result_array


    else:
        return result_array

"""News Edit Check Point"""

####################################################################
# Name - edit_rights                                               #
# Owner - Visnu Badal                                              #
# Review by - ?                                                    #
#                                                                  #
####################################################################

def edit_rights(news_id, request, news_type_id):
    if request.user.is_superuser:
        news_obj = NewsFeed.objects.filter(id=news_id)
    else:
        news_obj = NewsFeed.objects.filter(id=news_id, current_user_id=request.user.id, news_type=news_type_id)
        #news_obj = NewsFeed.objects.filter(id=news_id)
    if news_obj:
        return news_obj
    else:
        return False

""" provider check point"""

####################################################################
# Name - add_edit_rights_providers                                 #
# Owner - Visnu Badal                                              #
# Review by - ?                                                    #
#                                                                  #
####################################################################

#def add_edit_rights_providers()


###########################################
#   By Nishank                            #
#                                         #
###########################################
def check_doctor_global_search(doctor_id, user_id, is_super_user=None):
    try:
        if doctor_id and user_id is not None:
            doctor_obj = Doctor.objects.filter(id=doctor_id)
            if len(doctor_obj):
                return True
            else:
                return False
        else:
            return False
    except Exception as e:
        return False