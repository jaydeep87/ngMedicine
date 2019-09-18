from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout, authenticate, login, get_user_model
from hfu_cms.models import *
from django.http.response import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import View, FormView
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.db.models import Q
from HealthDynamicsCMS.settings import DEFAULT_FROM_EMAIL
from news.models import NewsFeed
from django.template.loader import get_template
from django.core.validators import validate_email
# Validator Exception
from django.core.exceptions import ValidationError
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes
from django.template import loader
from django.views.decorators.http import require_GET, require_POST
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
import json
import uuid
from check_point import check_doctor, check_organisation, check_organisation_edit, return_doc, \
    check_organisation_complete, check_organisation_for_schedule, check_attached_doctor_in_publish_stage, \
    check_attached_organisation_in_publish_stage, return_lab,return_organisation,check_doctor_global_search
from datetime import datetime
from master_list import day_list, demo_time_list
from underscore import *
import os
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from providers.models import ServicePlan, ServiceProvider, PlanCategory, Kurable_subtype_master, Healthoholic_subtype_master,CaResidense_subtype_master
from hfu_cms.models import Labs,Organisation_branches
from hfu_cms.data_publisher import data_publisher
from news.models import NewsTypeMaster
from django.template.loader import render_to_string
from django.http.response import HttpResponse, HttpResponseRedirect, Http404
#hospital_type = ['Allopathy', 'Ayurveda', 'Homeopathy', 'Naturopathy']
hospital_category = ['Private', 'Public', 'Nursing Homes']
imageURL = "hfu_cms/static"

baseFolder = "/media/organisation_gallery"


##FOR Localhost CMS
# hostname = 'http://127.0.0.1:'
# port="8094"

##FOR LIVE CMS
#hostname = 'https://stagingapi.healthforu.com'
#port=""
#STATIC_URL_DOMAIN = 'http://cms.healthforu.com/static'

##FOR BETA CMS
hostname = 'https://test.healthforu.com'
port=""
STATIC_URL_DOMAIN = 'http://beta-cms.healthforu.com/static'

authToken = "6Le67BQUAAAAAN_zdhvYdXDiVBrdGaVkPwThfgsjghfsjdgfjs"

from .models import Disease,Symptoms
from django.shortcuts import get_object_or_404
from django.conf import settings
import mammoth
import base64
import os
image_iterator = 0
image_file_name = ''
image_src = ''
image_alt_g=''
import elasticsearch_client
from .data_publisher import master_SingleRecord_elastic_update,__organisation_data_creation,__doctor_data_creation
from django.db import IntegrityError
import datetime

####################################################################
# Name - live_doctor_listing_edit                                  #
# BY - Nishank Gupta                                               #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def liveDoctor_global_search(request, doctor_id=None):

    try:
        tab = None
        try:
            tab = request.GET['tab']
        except:
            tab = None
        if tab and doctor_id is not None:
            year_list =["1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982",
                         "1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995",
                         "1996","1997","1998","1999","2000", "2001", "2002","2003","2004","2005","2006","2007","2008",
                         "2009","2010","2011","2012","2013","2014","2015","2016","2017"]

            live_doctor = Live_Doctor.objects.get(id=doctor_id)
            live_doc_exp_list = Live_Doctor_Experience.objects.filter(doctor_id=doctor_id)
            live_doc_rewardrecog_list = Live_Doctor_Rewardrecog.objects.filter(doctor_id=doctor_id)
            live_doc_memb_list = Live_Doctor_Membership.objects.filter(doctor_id=doctor_id)
            live_doc_education_list = Live_Doctor_Education.objects.filter(doctor_id=doctor_id)
            category_obj = Category.objects.filter(delete=False).order_by('name')
            zone_obj = Zone.objects.filter(delete=False)
            try:
                current_zone_id = live_doctor.zone_id
                dummy = int(current_zone_id)
                current_zone = live_doctor.zone
                zone_based_locations = ZoneLocation.objects.filter(delete=False, zone_id=current_zone_id )
            except:
                current_zone = None
                zone_based_locations = None
            try:
                current_zone_location_id = live_doctor.zone_location_id
                dummy = int(current_zone_location_id)
                current_zone_location = live_doctor.zone_location
            except:
                current_zone_location = None

            if live_doctor.category and live_doctor.category != '' and live_doctor.category != [] and live_doctor.category :
                cat = live_doctor.category
                #curent_cat = Category.objects.get(name=cat)
                curent_cat = cat
                speciality = live_doctor.speciality
                current_specialities = []
                temp = []
                speciality_all = Speciality.objects.filter(delete=False)
                #print speciality_all.count()
                temp_list = []
                if speciality and speciality != []  and speciality != ["[]"] :
                    for obj in speciality:
                        temp_list.append(obj['id'])
                if temp_list != []:
                    for i in temp_list:
                        for j in speciality_all:
                            if int(i) == j.id and j.category_id == curent_cat :
                                temp.append(j)
                    current_specialities = temp
                else:
                    current_specialities = []

                #print current_specialities

                speciality = Speciality.objects.filter(category_id=curent_cat, delete=False)

                ser_off = live_doctor.serviceOffered


                #print ser_off
                current_seroff = []
                temp = []
                seroff_all = Service_Offred.objects.filter(delete=False)
                temp_list = []
                if ser_off and ser_off != [] and ser_off != ["[]"]:
                    for obj in ser_off:
                        temp_list.append(obj['id'])

                if temp_list != []:
                    for i in temp_list:
                        for j in seroff_all:
                            if int(i) == j.id and j.delete == False and j.category_id == curent_cat:
                                temp.append(j)
                    current_seroff = temp
                else:
                    current_seroff = []
                #print   current_seroff
                serviceOffered = Service_Offred.objects.filter(category_id=curent_cat, delete=False)

            else:
                cat = ''
                curent_cat = None
                current_specialities = []
                current_seroff = []
                speciality = []
                serviceOffered = []

            if UserManagement.objects.filter(user_id=request.user.id, is_caller=True):
                user_data = UserManagement.objects.filter(is_reviewer=True, is_doctor_reviewer=True).values('user_id')
                user_publisher_data = []
            elif UserManagement.objects.filter(user_id=request.user.id, is_reviewer=True):
                user_data = UserManagement.objects.filter(is_caller=True, is_doctor_caller=True).values('user_id')
                user_publisher_data = UserManagement.objects.filter(is_publisher=True).values('user_id')
            else:
                user_data = []
                user_publisher_data = []
            reviewer_user_data = User.objects.filter(id__in=user_data, is_active=True)
            publisher_user_data = User.objects.filter(id__in=user_publisher_data, is_active=True)
            valid_choice = ValidateByChoice.objects.all()
            user_data_complete = UserManagement.objects.all()
            emer_localities_list = []
            try:
                asso_obj = Live_Doctor_Associated_Data.objects.get(doctor_id=doctor_id)
                if asso_obj.localities and asso_obj.localities != '' and asso_obj.localities != []:
                    emer_localities_list = asso_obj.localities.split(',')
            except:
                emer_localities_list = []
                asso_obj = None
            if asso_obj:
                qualification = asso_obj.qualification_data
                talk_to_doc = asso_obj.talk_to_doc
                talk_fee = asso_obj.talk_fee
            else:
                qualification = None
                talk_to_doc = False
                talk_fee = 0

            country_obj = Country.objects.filter(delete=False)
            state_obj = State.objects.filter(delete=False)
            city = City.objects.filter(delete=False)
            locality = Locality.objects.filter(delete=False)
            global hostname
            global port
            hostport = hostname + port


            gallery_image_obj_list = None
            try:
                gallery_image_obj_list = Live_Doctor_Imagegallery.objects.filter(doctor_id=int(doctor_id))
                if list(gallery_image_obj_list) != [] :
                    gallery_image_obj_list = gallery_image_obj_list
                else:
                    gallery_image_obj_list = None
            except:
                gallery_image_obj_list = None


            all_departments = Department.objects.all().order_by('name')
            sche_dep = Live_Doctor_Commonworkschedule.objects.filter(doctor_id= doctor_id)
            org_with_current_dep = {}
            for schdeppt in sche_dep :
                if schdeppt.department != None and schdeppt.department != '' and schdeppt.department != ' ':
                    current_departments = schdeppt.department.split(',')
                    org_with_current_dep.update({schdeppt.clinic_id:current_departments})
                else:
                    pass


            # -----------------SCHEDULE DEFAULT FOR ALL TABS STARTS HERE---
            # -------------------------------------------------------------

            #organisation_all = OrganisationName.objects.filter(is_disable=False,stage_id__gte=4).order_by('name')
            country_obj = Country.objects.filter(delete=False)
            state_obj = State.objects.filter(delete=False)
            locality = Locality.objects.filter(delete=False)

            appointment_minutes = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55']

            list_of_schedules = Live_Doctor_Commonworkschedule.objects.filter(Q(doctor_id=doctor_id),~Q(status='delete'))
            mylist = []
            for i in list_of_schedules :
                str = i.time
                schclinic= OrganisationName.objects.get(id = i.clinic_id)
                clinic_details = schclinic.name+' '+schclinic.street+' '+schclinic.locality.name
                if i.time_type == 'single' or i.time_type == 'single_double':
                    temp = json.loads(str)
                    temp.update({'time_type':i.time_type})
                    temp.update({'clinic_id':i.clinic_id})
                    temp.update({'clinic_details':clinic_details})
                    temp.update({'schedule_id':i.id})
                    temp.update({'consultingCharge':i.consultingCharge})
                    temp.update({'appointmentMinute':i.appointmentMinute})
                    temp.update({'did':i.did})
                    temp.update({'extension':i.extension})

                    mylist.append(temp)
                    #print mylist

                if i.time_type == 'multi_double':
                    str2 = i.time
                    temp2 = json.loads(str2)
                    ss_template = {
                        'time_type': i.time_type,
                        'clinic_id': i.clinic_id,
                        'clinic_details':clinic_details,
                        'schedule_id': i.id,
                        'consultingCharge': i.consultingCharge,
                        'appointmentMinute': i.appointmentMinute,
                        'did':i.did,
                        'extension':i.extension,
                        'Mon': {
                            u'value': False,
                            u'name': u'Mon',
                            u'session2': {
                                u'to': u'',
                                u'from': u''
                            },
                            u'session1': {
                                u'to': u'',
                                u'from': u''
                            }
                        },
                         'Tue': {
                            u'value': False,
                            u'name': u'Tue',
                            u'session2': {
                                u'to': u'',
                                u'from': u''
                            },
                            u'session1': {
                                u'to': u'',
                                u'from': u''
                            }
                        },
                        'Wed':{
                            u'value': False,
                            u'name': u'Wed',
                            u'session2': {
                                u'to': u'',
                                u'from': u''
                            },
                            u'session1': {
                                u'to': u'',
                                u'from': u''
                            }
                        },
                        'Thu':{
                            u'value': False,
                            u'name': u'Thu',
                            u'session2': {
                                u'to': u'',
                                u'from': u''
                            },
                            u'session1': {
                                u'to': u'',
                                u'from': u''
                            }
                        },
                        'Fri':{
                            u'value': False,
                            u'name': u'Fri',
                            u'session2': {
                                u'to': u'',
                                u'from': u''
                            },
                            u'session1': {
                                u'to': u'',
                                u'from': u''
                            }
                        },
                        'Sat':{
                            u'value': False,
                            u'name': u'Sat',
                            u'session2': {
                                u'to': u'',
                                u'from': u''
                            },
                            u'session1': {
                                u'to': u'',
                                u'from': u''
                            }
                        },
                        'Sun':{
                            u'value': False,
                            u'name': u'Sun',
                            u'session2': {
                                u'to': u'',
                                u'from': u''
                            },
                            u'session1': {
                                u'to': u'',
                                u'from': u''
                            }
                        }
                    }

                    for jj in temp2 :
                        if jj['name'] == 'Mon':
                            ss_template['Mon']['value'] = jj['value']
                            ss_template['Mon']['session1']['from'] = jj['session1']['from']
                            ss_template['Mon']['session1']['to'] = jj['session1']['to']
                            ss_template['Mon']['session2']['from'] = jj['session2']['from']
                            ss_template['Mon']['session2']['to'] = jj['session2']['to']
                        if jj['name'] == 'Tue':
                            ss_template['Tue']['value'] = jj['value']
                            ss_template['Tue']['session1']['from'] = jj['session1']['from']
                            ss_template['Tue']['session1']['to'] = jj['session1']['to']
                            ss_template['Tue']['session2']['from'] = jj['session2']['from']
                            ss_template['Tue']['session2']['to'] = jj['session2']['to']
                        if jj['name'] == 'Wed':
                            ss_template['Wed']['value'] = jj['value']
                            ss_template['Wed']['session1']['from'] = jj['session1']['from']
                            ss_template['Wed']['session1']['to'] = jj['session1']['to']
                            ss_template['Wed']['session2']['from'] = jj['session2']['from']
                            ss_template['Wed']['session2']['to'] = jj['session2']['to']
                        if jj['name'] == 'Thu':
                            ss_template['Thu']['value'] = jj['value']
                            ss_template['Thu']['session1']['from'] = jj['session1']['from']
                            ss_template['Thu']['session1']['to'] = jj['session1']['to']
                            ss_template['Thu']['session2']['from'] = jj['session2']['from']
                            ss_template['Thu']['session2']['to'] = jj['session2']['to']
                        if jj['name'] == 'Fri':
                            ss_template['Fri']['value'] = jj['value']
                            ss_template['Fri']['session1']['from'] = jj['session1']['from']
                            ss_template['Fri']['session1']['to'] = jj['session1']['to']
                            ss_template['Fri']['session2']['from'] = jj['session2']['from']
                            ss_template['Fri']['session2']['to'] = jj['session2']['to']
                        if jj['name'] == 'Sat':
                            ss_template['Sat']['value'] = jj['value']
                            ss_template['Sat']['session1']['from'] = jj['session1']['from']
                            ss_template['Sat']['session1']['to'] = jj['session1']['to']
                            ss_template['Sat']['session2']['from'] = jj['session2']['from']
                            ss_template['Sat']['session2']['to'] = jj['session2']['to']
                        if jj['name'] == 'Sun':
                            ss_template['Sun']['value'] = jj['value']
                            ss_template['Sun']['session1']['from'] = jj['session1']['from']
                            ss_template['Sun']['session1']['to'] = jj['session1']['to']
                            ss_template['Sun']['session2']['from'] = jj['session2']['from']
                            ss_template['Sun']['session2']['to'] = jj['session2']['to']
                    #print ":::::::",ss_template
                    mylist.append(ss_template)



            list_of_schedules  =   mylist
            # -----------------SCHEDULE DEFAULT FOR ALL TABS ENDS HERE------
            # -------------------------------------------------------------


            # TAB 1----START-----------------------------------------------
            if tab == '1' and request.method == 'GET':

                return render(request, 'global_search/livedoctor/view_live_doctor_data.html', {
                    'tab_listing': 'live_doctor_listing', 'tab': tab,
                    'live_doctor': live_doctor, 'doctor_id': doctor_id,
                    'live_doc_exp_list': live_doc_exp_list, 'live_doc_rewardrecog_list': live_doc_rewardrecog_list,
                    'live_doc_memb_list': live_doc_memb_list, 'live_doc_education_list': live_doc_education_list,
                    'year_list':year_list,
                    'reviewer_user_data': reviewer_user_data,
                    'publisher_user_data': publisher_user_data,
                    'user_data_complete': user_data_complete,'valid_choice': valid_choice,
                    'category_obj': category_obj,
                    'curent_cat': curent_cat, 'current_seroff': current_seroff,
                    'current_specialities': current_specialities,
                    'speciality':speciality,'serviceOffered':serviceOffered,'zone_obj': zone_obj,
                    'current_zone':current_zone,'current_zone_location':current_zone_location,
                    'zone_based_locations':zone_based_locations,
                    'appointment_minutes':appointment_minutes,'list_of_schedules':list_of_schedules,
                    'qualification':qualification,'talk_to_doc':talk_to_doc,'talk_fee':talk_fee,
                    'country_obj': country_obj, 'state_obj': state_obj,
                    'city': city, 'locality': locality,'asso_obj':asso_obj,
                    'emer_localities_list':emer_localities_list,'hostport':hostport,
                    'gallery_image_obj_list':gallery_image_obj_list,'country_obj':country_obj,'state_obj':state_obj,
                    'locality':locality,'all_departments':all_departments,'org_with_current_dep':org_with_current_dep

                    })


            # if tab == '1' and request.method == 'POST':
            #
            #     try:
            #         zone_id = request.POST['zone'].strip()
            #         dummy = int(zone_id)
            #         zone = Zone.objects.get(id = dummy)
            #     except:
            #         zone = None
            #     try:
            #         zone_location_id = request.POST['zone_location'].strip()
            #         dummy = int(zone_location_id)
            #         zone_location = ZoneLocation.objects.get(id= dummy)
            #     except:
            #         zone_location = None
            #
            #     try:
            #         live_did = request.POST['live_did'].strip()
            #     except:
            #         live_did = ''
            #
            #     try:
            #         live_extension = request.POST['live_extension'].strip()
            #     except:
            #         live_extension = ''
            #
            #     try:
            #         firstName = request.POST['firstName'].strip()
            #     except:
            #         firstName = ''
            #     try:
            #         lastName = request.POST['lastName'].strip()
            #     except:
            #         lastName = ''
            #     try:
            #         category = request.POST['category'].strip()
            #         temp = int(category)
            #         category = temp
            #     except:
            #         category = None
            #
            #     try:
            #         service_offered = request.POST.getlist('serviceoffer')
            #     except:
            #         service_offered = []
            #     if service_offered and service_offered != [] and service_offered != '':
            #         temp = ''
            #         #print "so  = ",service_offered
            #         #print type(service_offered)
            #         json_list_so = []
            #         for i in service_offered:
            #             obj = Service_Offred.objects.get(id=int(i))
            #             json_list_so.append({"id": int(i), "name": obj.name})
            #         service_offered = json_list_so
            #
            #     try:
            #         speciality = request.POST.getlist('specialty')
            #     except:
            #         speciality = []
            #     if speciality and speciality != [] and speciality != '':
            #         #print speciality
            #         #print type(speciality)
            #         json_list_spe = []
            #         for i in speciality:
            #             obj = Speciality.objects.get(id=int(i))
            #             json_list_spe.append({"id": int(i), "name": obj.name})
            #         speciality = json_list_spe
            #
            #     try:
            #         gender = request.POST['gender'].strip()
            #     except:
            #         gender = ''
            #     try:
            #         DOB = request.POST['DOB'].strip()
            #     except Exception as e:
            #         DOB = ''
            #     try:
            #         phone = request.POST['phone'].strip()
            #     except Exception as e:
            #         phone = ''
            #     try:
            #         fax = request.POST['fax'].strip()
            #     except Exception as e:
            #         fax = ''
            #     try:
            #         mobile = request.POST['mobile'].strip()
            #     except Exception as e:
            #         mobile = ''
            #     try:
            #         skype = request.POST['skype'].strip()
            #     except Exception as e:
            #         skype = ''
            #     try:
            #         email = request.POST['email'].strip()
            #     except Exception as e:
            #         email = ''
            #     try:
            #         secondary_email = request.POST['secondary_email'].strip()
            #     except Exception as e:
            #         secondary_email = ''
            #
            #     if firstName != '' and lastName != '' and gender != '' and mobile != '' and email != '' and category and category != '':
            #         live_doctor.firstName=firstName
            #         live_doctor.lastName=lastName
            #         live_doctor.category=category
            #         live_doctor.serviceOffered=service_offered
            #         live_doctor.speciality=speciality
            #         live_doctor.gender=gender
            #         live_doctor.dob=DOB
            #         live_doctor.phoneNo=phone
            #         live_doctor.fax=fax
            #         live_doctor.mobileNo=mobile
            #         live_doctor.skypeId=skype
            #         live_doctor.email=email
            #         live_doctor.alternateEmail=secondary_email
            #         live_doctor.did=live_did
            #         live_doctor.extension=live_extension
            #
            #         if zone:
            #             live_doctor.zone = zone
            #         if zone_location:
            #             live_doctor.zone_location = zone_location
            #
            #         live_doctor.save()
            #
            #         messages.success(request, "Doctor Profile Updatedd Successfully")
            #         return redirect(reverse('live_doctor_listing_edit', args=[live_doctor.id]) + "?tab=1")
            #     else:
            #         messages.error(request, "Please Provide all required fields")
            #         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            # TAB 1----END-------------------------------------------------

            # TAB 2----START-----------------------------------------------
            if tab == '2' and request.method == 'GET':
                return render(request, 'global_search/livedoctor/view_live_doctor_data.html', {
                    'tab_listing': 'live_doctor_listing', 'tab': tab,
                    'live_doctor': live_doctor, 'doctor_id': doctor_id,
                    'live_doc_exp_list': live_doc_exp_list,
                    'live_doc_rewardrecog_list': live_doc_rewardrecog_list,
                    'live_doc_memb_list': live_doc_memb_list,
                    'live_doc_education_list': live_doc_education_list,
                    'year_list': year_list,
                    'reviewer_user_data': reviewer_user_data,
                    'publisher_user_data': publisher_user_data,
                    'user_data_complete': user_data_complete, 'valid_choice': valid_choice,
                    'category_obj': category_obj,
                    'curent_cat': curent_cat, 'current_seroff': current_seroff,
                    'current_specialities': current_specialities,
                    'speciality': speciality, 'serviceOffered': serviceOffered, 'zone_obj': zone_obj,
                    'current_zone': current_zone, 'current_zone_location': current_zone_location,
                    'zone_based_locations': zone_based_locations,
                    'appointment_minutes': appointment_minutes, 'list_of_schedules': list_of_schedules,
                    'qualification': qualification, 'talk_to_doc': talk_to_doc, 'talk_fee': talk_fee,
                    'country_obj': country_obj, 'state_obj': state_obj,
                    'city': city, 'locality': locality, 'asso_obj': asso_obj,
                    'emer_localities_list': emer_localities_list,'hostport':hostport,
                    'gallery_image_obj_list':gallery_image_obj_list,'country_obj':country_obj,'state_obj':state_obj,
                    'locality':locality,'all_departments':all_departments,'org_with_current_dep':org_with_current_dep
                })

            # TAB 2----END-------------------------------------------------


            # TAB 3----START-----------------------------------------------
            if tab == '3' and request.method == 'GET':
                return render(request, 'global_search/livedoctor/view_live_doctor_data.html', {
                    'tab_listing': 'live_doctor_listing', 'tab': tab,
                    'live_doctor': live_doctor, 'doctor_id': doctor_id,
                    'live_doc_exp_list': live_doc_exp_list, 'live_doc_rewardrecog_list': live_doc_rewardrecog_list,
                    'live_doc_memb_list': live_doc_memb_list, 'live_doc_education_list': live_doc_education_list,
                    'year_list': year_list,
                    'reviewer_user_data': reviewer_user_data,
                    'publisher_user_data': publisher_user_data,
                    'user_data_complete': user_data_complete, 'valid_choice': valid_choice,
                    'category_obj': category_obj,
                    'curent_cat': curent_cat, 'current_seroff': current_seroff,
                    'current_specialities': current_specialities,
                    'speciality': speciality, 'serviceOffered': serviceOffered,'zone_obj': zone_obj,
                    'current_zone': current_zone, 'current_zone_location': current_zone_location,
                    'zone_based_locations': zone_based_locations,
                    'appointment_minutes': appointment_minutes,'list_of_schedules':list_of_schedules,
                    'qualification':qualification,'talk_to_doc':talk_to_doc,'talk_fee':talk_fee,
                    'country_obj': country_obj, 'state_obj': state_obj,
                    'city': city, 'locality': locality,'asso_obj':asso_obj,
                    'emer_localities_list': emer_localities_list,'hostport':hostport,
                    'gallery_image_obj_list':gallery_image_obj_list,'country_obj':country_obj,'state_obj':state_obj,
                    'locality':locality,'all_departments':all_departments,'org_with_current_dep':org_with_current_dep
                })
            # if tab == '3' and request.method == 'POST':
            #     degree = None
            #     try:
            #         degree = request.POST['degree']
            #     except:
            #         degree = None
            #
            #     college = request.POST['college']
            #     year = request.POST['year']
            #
            #     if degree:
            #         import datetime
            #         now = datetime.datetime.now()
            #         new_education = Live_Doctor_Education(doctor_id=doctor_id, degree=degree,
            #                                               createdAt=now,
            #                                               college=college, year=int(year))
            #         new_education.save()
            #
            #
            #         ldoc3 = Live_Doctor.objects.get(id=doctor_id)
            #         ldoc3.qualification_points = 0
            #         ldoc3.save()
            #         ldoc3_education_list = Live_Doctor_Education.objects.filter(doctor_id=doctor_id)
            #         if list(ldoc3_education_list) != [] :
            #             for edu in ldoc3_education_list :
            #                 if edu.degree.strip().lower() == 'MBBS'.lower() or edu.degree.strip().lower() == 'BHMS'.lower():
            #                     ldoc3.qualification_points  =  ldoc3.qualification_points + 6
            #                     break
            #             for edu in ldoc3_education_list :
            #                 if edu.degree.strip().lower() == 'MD'.lower() or edu.degree.strip().lower() == 'MS'.lower():
            #                     ldoc3.qualification_points  =  ldoc3.qualification_points + 11
            #                     break
            #             if len(list(ldoc3_education_list)) > 1:
            #                 ldoc3.qualification_points = ldoc3.qualification_points + 3
            #         else:
            #             ldoc3.qualification_points = 0
            #         ldoc3.save()
            #
            #
            #
            #
            #
            #         messages.success(request, "Successfully Added Education Entry")
            #         return redirect(reverse('live_doctor_listing_edit', args=[doctor_id]) + '?tab=3')
            #     else:
            #         messages.error(request, "Please provide value for Degree field")
            #         return redirect(reverse('live_doctor_listing_edit', args=[doctor_id]) + '?tab=3')
            # TAB 3----END-------------------------------------------------



            #TAB 4----START-----------------------------------------------
            if tab == '4' and request.method == 'GET' :


                return render(request, 'global_search/livedoctor/view_live_doctor_data.html',{
                    'tab_listing': 'live_doctor_listing','tab':tab,
                    'live_doctor':live_doctor, 'doctor_id':doctor_id,
                    'live_doc_exp_list':live_doc_exp_list,'live_doc_rewardrecog_list':live_doc_rewardrecog_list,
                    'live_doc_memb_list':live_doc_memb_list,'live_doc_education_list':live_doc_education_list,
                    'year_list': year_list,
                    'reviewer_user_data': reviewer_user_data,
                    'publisher_user_data': publisher_user_data,
                    'user_data_complete': user_data_complete,'valid_choice': valid_choice,
                    'category_obj': category_obj,
                    'curent_cat': curent_cat, 'current_seroff': current_seroff,
                    'current_specialities': current_specialities,
                    'speciality': speciality, 'serviceOffered': serviceOffered,'zone_obj': zone_obj,
                    'current_zone': current_zone, 'current_zone_location': current_zone_location,
                    'zone_based_locations': zone_based_locations,
                    'appointment_minutes': appointment_minutes,'list_of_schedules':list_of_schedules,
                    'qualification': qualification,'talk_to_doc':talk_to_doc,'talk_fee':talk_fee,
                    'country_obj': country_obj, 'state_obj': state_obj,
                    'city': city, 'locality': locality,'asso_obj':asso_obj,
                    'emer_localities_list': emer_localities_list,'hostport':hostport,
                    'gallery_image_obj_list':gallery_image_obj_list,'country_obj':country_obj,'state_obj':state_obj,
                    'locality':locality,'all_departments':all_departments,'org_with_current_dep':org_with_current_dep
                })
            # if tab == '4' and request.method == 'POST':
            #     experience = None
            #     try:
            #         experience = request.POST['experience']
            #     except:
            #         experience = None
            #
            #     fromYear = request.POST['fromYear']
            #     toYear = request.POST['toYear']
            #     designation = request.POST['designation']
            #     city = request.POST['city']
            #
            #     if fromYear:
            #         pass
            #     else:
            #         fromYear=0
            #     if toYear:
            #         pass
            #     else:
            #         toYear=0
            #
            #     if experience:
            #         import datetime
            #         now = datetime.datetime.now()
            #         new_experience =  Live_Doctor_Experience(doctor_id = doctor_id,name = experience,createdAt = now,
            #                                                  fromYear=int(fromYear),toYear=int(toYear),designation=designation,city=city)
            #         new_experience.save()
            #
            #         ldoc2 = Live_Doctor.objects.get(id = doctor_id )
            #         ldoc2_experience_list =  Live_Doctor_Experience.objects.filter(doctor_id = doctor_id)
            #         total = 0
            #         if list(ldoc2_experience_list) != []:
            #             for i in ldoc2_experience_list:
            #                 if i.toYear != None and i.fromYear != None :
            #                     total = total + (int(i.toYear) - int(i.fromYear))
            #                 else:
            #                     pass
            #             exppoints = 0
            #             if total < 5 :
            #                 exppoints = 3.5
            #             elif total >= 5 and total <= 10:
            #                 exppoints = 5
            #             elif total >= 10:
            #                 exppoints = 6.5
            #         else:
            #             exppoints = 0
            #
            #         ldoc2.experience_points = exppoints
            #         ldoc2.save()
            #
            #         messages.success(request,"Successfully Added Experience Entry")
            #         return redirect(reverse('live_doctor_listing_edit',args=[doctor_id])+'?tab=4')
            #     else:
            #         messages.error(request, "Please provide value for Experience field")
            #         return redirect(reverse('live_doctor_listing_edit', args=[doctor_id]) + '?tab=4')
            # TAB 4----END-------------------------------------------------


            # TAB 5----START-----------------------------------------------
            if tab == '5' and request.method == 'GET':

                return render(request, 'global_search/livedoctor/view_live_doctor_data.html', {
                    'tab_listing': 'live_doctor_listing', 'tab': tab,
                    'live_doctor': live_doctor, 'doctor_id': doctor_id,
                    'live_doc_exp_list': live_doc_exp_list, 'live_doc_rewardrecog_list': live_doc_rewardrecog_list,
                    'live_doc_memb_list': live_doc_memb_list, 'live_doc_education_list': live_doc_education_list,
                    'year_list': year_list,
                    'reviewer_user_data': reviewer_user_data,
                    'publisher_user_data': publisher_user_data,
                    'user_data_complete': user_data_complete,'valid_choice': valid_choice,
                    'category_obj': category_obj,
                    'curent_cat': curent_cat, 'current_seroff': current_seroff,
                    'current_specialities': current_specialities,
                    'speciality': speciality, 'serviceOffered': serviceOffered,'zone_obj': zone_obj,
                    'current_zone': current_zone, 'current_zone_location': current_zone_location,
                    'zone_based_locations': zone_based_locations,
                    'appointment_minutes': appointment_minutes,'list_of_schedules':list_of_schedules,
                    'qualification': qualification,'talk_to_doc':talk_to_doc,'talk_fee':talk_fee,
                    'country_obj': country_obj, 'state_obj': state_obj,
                    'city': city, 'locality': locality,'asso_obj':asso_obj,
                    'emer_localities_list': emer_localities_list,'hostport':hostport,
                    'gallery_image_obj_list':gallery_image_obj_list,'country_obj':country_obj,'state_obj':state_obj,
                    'locality':locality,'all_departments':all_departments,'org_with_current_dep':org_with_current_dep
                })
    #         if tab == '5' and request.method == 'POST':
    #
    #             time_type = request.POST['schedule'].strip()
    #             hospital_id = request.POST['diet_org_id'].strip()
    #             designation = request.POST['designation'].strip()
    #             app_minutes = request.POST['app_minutes'].strip()
    #             consultation_charges = request.POST['consultation_charges'].strip()
    #             live_schedule_did = request.POST['live_schedule_did'].strip()
    #             live_schedule_extension = request.POST['live_schedule_extension'].strip()
    #             AssoObj = Live_Doctor_Commonworkschedule.objects.filter(doctor_id=doctor_id,clinic_id=int(hospital_id))
    #             if hospital_id == None or hospital_id == '' or hospital_id == ' ':
    #                 messages.error(request,"Please select an Organisation")
    #                 return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    #
    #             if list(AssoObj) == []:
    #                 import datetime
    #                 # now = datetime.datetime.now()
    #                 # new_sch_obj = Live_Doctor_Commonworkschedule(designation=designation, clinic_id=hospital_id,
    #                 #                                              time_type=time_type, appointmentMinute=app_minutes,
    #                 #                                              consultingCharge=consultation_charges,
    #                 #                                              createdAt=now,doctor_id=doctor_id)
    #
    #                 if time_type == "multi_double" :
    #
    #                     varr = [
    #                           {
    #                             "value": False,
    #                             "name": "Mon",
    #                             "session1": {
    #                               "from": "",
    #                               "to": ""
    #                             },
    #                             "session2": {
    #                               "from": "",
    #                               "to": ""
    #                             }
    #                           },
    #                           {
    #                             "value": False,
    #                             "name": "Tue",
    #                             "session1": {
    #                               "from": "",
    #                               "to": ""
    #                             },
    #                             "session2": {
    #                               "from": "",
    #                               "to": ""
    #                             }
    #                           },
    #                           {
    #                             "value": False,
    #                             "name": "Wed",
    #                             "session1": {
    #                               "from": "",
    #                               "to": ""
    #                             },
    #                             "session2": {
    #                               "from": "",
    #                               "to": ""
    #                             }
    #                           },
    #                           {
    #                             "value": False,
    #                             "name": "Thu",
    #                             "session1": {
    #                               "from": "",
    #                               "to": ""
    #                             },
    #                             "session2": {
    #                               "from": "",
    #                               "to": ""
    #                             }
    #                           },
    #                           {
    #                             "value": False,
    #                             "name": "Fri",
    #                             "session1": {
    #                               "from": "",
    #                               "to": ""
    #                             },
    #                             "session2": {
    #                               "from": "",
    #                               "to": ""
    #                             }
    #                           },
    #                           {
    #                             "value": False,
    #                             "name": "Sat",
    #                             "session1": {
    #                               "from": "",
    #                               "to": ""
    #                             },
    #                             "session2": {
    #                               "from": "",
    #                               "to": ""
    #                             }
    #                           },
    #                           {
    #                             "value": False,
    #                             "name": "Sun",
    #                             "session1": {
    #                               "from": "",
    #                               "to": ""
    #                             },
    #                             "session2": {
    #                               "from": "",
    #                               "to": ""
    #                             }
    #                           }
    #                         ]
    #
    #
    #                     try:
    #                         monday = request.POST['Moncheck']
    #                     except:
    #                         monday = "NotChecked"
    #                     if monday == 'Monyes':
    #                         from1 = request.POST['monFROM1']
    #                         to1 = request.POST['monTO1']
    #                         from2 = request.POST['monFROM2']
    #                         to2 = request.POST['monTO2']
    #                         varr[0]['session1']['from'] = from1
    #                         varr[0]['session2']['from'] = from2
    #                         varr[0]['session1']['to'] = to1
    #                         varr[0]['session2']['to'] = to2
    #                         varr[0]['value'] = True
    #
    #
    #                     from1 = to1 = from2 = to2 = ""
    #                     try:
    #                         tuesday = request.POST['Tuecheck']
    #                     except:
    #                         tuesday = "NotChecked"
    #                     if tuesday == 'Tueyes':
    #                         from1 = request.POST['tueFROM1']
    #                         to1 = request.POST['tueTO1']
    #                         from2 = request.POST['tueFROM2']
    #                         to2 = request.POST['tueTO2']
    #                         # list_schedule[1]['session1']['from'] = from1
    #                         # list_schedule[1]['session1']['to'] = to1
    #                         # list_schedule[1]['session2']['from'] = from2
    #                         # list_schedule[1]['session2']['to'] = to2
    #                         varr[1]['session1']['from'] = from1
    #                         varr[1]['session2']['from'] = from2
    #                         varr[1]['session1']['to'] = to1
    #                         varr[1]['session2']['to'] = to2
    #                         varr[1]['value'] = True
    #
    #                     from1 = to1 = from2 = to2 = ""
    #                     try:
    #                         wednesday = request.POST['Wedcheck']
    #                     except:
    #                         wednesday = "NotChecked"
    #                     if wednesday == 'Wedyes':
    #                         from1 = request.POST['wedFROM1']
    #                         to1 = request.POST['wedTO1']
    #                         from2 = request.POST['wedFROM2']
    #                         to2 = request.POST['wedTO2']
    #                         varr[2]['session1']['from'] = from1
    #                         varr[2]['session2']['from'] = from2
    #                         varr[2]['session1']['to'] = to1
    #                         varr[2]['session2']['to'] = to2
    #                         varr[2]['value'] = True
    #
    #                     from1 = to1 = from2 = to2 = ""
    #                     try:
    #                         thursday = request.POST['Thucheck']
    #                     except:
    #                         thursday = "NotChecked"
    #                     if thursday == 'Thuyes':
    #                         from1 = request.POST['thuFROM1']
    #                         to1 = request.POST['thuTO1']
    #                         from2 = request.POST['thuFROM2']
    #                         to2 = request.POST['thuTO2']
    #                         varr[3]['session1']['from'] = from1
    #                         varr[3]['session2']['from'] = from2
    #                         varr[3]['session1']['to'] = to1
    #                         varr[3]['session2']['to'] = to2
    #                         varr[3]['value'] = True
    #
    #                     from1 = to1 = from2 = to2 = ""
    #                     try:
    #                         friday = request.POST['Fricheck']
    #                     except:
    #                         friday = "NotChecked"
    #                     if friday == 'Friyes':
    #                         from1 = request.POST['friFROM1']
    #                         to1 = request.POST['friTO1']
    #                         from2 = request.POST['friFROM2']
    #                         to2 = request.POST['friTO2']
    #                         varr[4]['session1']['from'] = from1
    #                         varr[4]['session2']['from'] = from2
    #                         varr[4]['session1']['to'] = to1
    #                         varr[4]['session2']['to'] = to2
    #                         varr[4]['value'] = True
    #
    #                     from1 = to1 = from2 = to2 = ""
    #                     try:
    #                         saturday = request.POST['Satcheck']
    #                     except:
    #                         saturday = "NotChecked"
    #                     if saturday == 'Satyes':
    #                         from1 = request.POST['satFROM1']
    #                         to1 = request.POST['satTO1']
    #                         from2 = request.POST['satFROM2']
    #                         to2 = request.POST['satTO2']
    #                         varr[5]['session1']['from'] = from1
    #                         varr[5]['session2']['from'] = from2
    #                         varr[5]['session1']['to'] = to1
    #                         varr[5]['session2']['to'] = to2
    #                         varr[5]['value'] = True
    #
    #                     from1 = to1 = from2 = to2 = ""
    #                     try:
    #                         sunday = request.POST['Suncheck']
    #                     except:
    #                         sunday = "NotChecked"
    #                     if sunday == 'Sunyes':
    #                         from1 = request.POST['sunFROM1']
    #                         to1 = request.POST['sunTO1']
    #                         from2 = request.POST['sunFROM2']
    #                         to2 = request.POST['sunTO2']
    #                         varr[6]['session1']['from'] = from1
    #                         varr[6]['session2']['from'] = from2
    #                         varr[6]['session1']['to'] = to1
    #                         varr[6]['session2']['to'] = to2
    #                         varr[6]['value'] = True
    #
    #                     xyz = json.dumps(varr)
    #                     kkk = json.loads(xyz)
    #                     template_service= {
    #                         "doctor_id": 0,
    #                         "hospital": {
    #                             "name": "",
    #                             "id": "",
    #
    #                         },
    #                         "designation": "",
    #                         "appointmentMinute": "",
    #                         "consultingCharge": "",
    #                         "time_type": "",
    #                         "time": {
    #
    #                         }
    #                     }
    #
    #                     template_service["doctor_id"] = int(doctor_id)
    #                     template_service["hospital"]["id"] = int(hospital_id)
    #                     org_single = OrganisationName.objects.get(id = int(hospital_id))
    #                     template_service["hospital"]["name"] = org_single.name
    #                     template_service["designation"] = designation
    #                     #template_service["appointmentMinute"] = int(app_minutes)
    #                     try:
    #                         template_service["appointmentMinute"] = int(app_minutes)
    #                     except:
    #                         template_service["appointmentMinute"] = 15
    #                     template_service["consultingCharge"] = float(consultation_charges)
    #                     template_service["did"] = live_schedule_did
    #                     template_service["extension"] = live_schedule_extension
    #
    #                     template_service["time_type"] = time_type
    #                     template_service["time"] = kkk
    #
    #                     global authToken
    #                     template_service['authToken'] = authToken
    #
    #                     global hostname
    #                     global port
    #                     url_p3 = "/api/v2/doctor/add_work_schedule/"
    #                     urlc = hostname + port + url_p3
    #                     # print urlc
    #                     import requests
    #                     url = urlc
    #                     try:
    #                         r = requests.post(url, json=template_service)
    #                         # tempresp = json.dumps(r.text)
    #                         # print r.text
    #                         # print type(r.text)
    #                         resp = json.loads(r.text)
    #                         # print type(resp)
    #                         # print resp
    #
    #                         if r.status_code == 200 or r.status_code == '200':
    #
    #                             if resp['statusCode'] == 200 or resp['statusCode'] == '200':
    #                                 messages.success(request, "Successfully Updated Schedule")
    #                                 return redirect(reverse('live_doctor_listing_edit', args=[int(doctor_id)]) + "?tab=5")
    #
    #                             else:
    #                                 messages.error(request, resp['statusMessage'])
    #                                 messages.success(request, "Updated Schedule But Problem with timing and time_obj")
    #                                 return redirect(reverse('live_doctor_listing_edit', args=[int(doctor_id)]) + "?tab=5")
    #
    #                         else:
    #                             messages.error(request, resp['statusMessage'])
    #                             messages.success(request, "Updated Schedule But Problem with timing and time_obj")
    #                             return redirect(reverse('live_doctor_listing_edit', args=[int(doctor_id)]) + "?tab=5")
    #
    #                     except Exception as e:
    #                         messages.error(request, e)
    #                         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    #
    #
    #                         # messages.success(request, "Successfully Updated Type 3Schedule")
    #                     # return redirect(reverse('live_doctor_listing_edit', args=[int(doctor_id)]) + "?tab=5")
    #
    # # ---------------------------------------------------------------------------------------------------------------------------------------------
    #                 else:
    #                     schedule_json = {}
    #                     day = {"Mon": "",  "Tue": "", "Wed": "", "Thu": "", "Fri": "", "Sat": "", "Sun": ""}
    #                     session1 = {"from":"","to": ""}
    #                     session2 = {"from": "","to": ""}
    #                     schedule_json.update({'day':day})
    #                     schedule_json.update({'session1':session1})
    #                     schedule_json.update({'session2':session2})
    #
    #
    #
    #
    #
    #                 if time_type == 'single':
    #                     try:
    #                         Mon =  request.POST['single1']
    #                     except:
    #                         Mon = False
    #                     try:
    #                         Tue =  request.POST['single2']
    #                     except:
    #                         Tue = False
    #                     try:
    #                         Wed =  request.POST['single3']
    #                     except:
    #                         Wed = False
    #                     try:
    #                         Thu =  request.POST['single4']
    #                     except:
    #                         Thu = False
    #                     try:
    #                         Fri =  request.POST['single5']
    #                     except:
    #                         Fri = False
    #                     try:
    #                         Sat =  request.POST['single6']
    #                     except:
    #                         Sat = False
    #                     try:
    #                         Sun =  request.POST['single7']
    #                     except:
    #                         Sun = False
    #
    #
    #                     from_time = request.POST['singleFromtime'].strip()
    #                     to_time = request.POST['singleTotime'].strip()
    #                     schedule_json['session1']['from'] = from_time
    #                     schedule_json['session1']['to'] = to_time
    #                     schedule_json['session2']['from'] = ""
    #                     schedule_json['session2']['to'] = ""
    #
    #                 if time_type == 'single_double':
    #                     try:
    #                         Mon = request.POST['single_double1']
    #                     except:
    #                         Mon = False
    #                     try:
    #                         Tue = request.POST['single_double2']
    #                     except:
    #                         Tue = False
    #                     try:
    #                         Wed = request.POST['single_double3']
    #                     except:
    #                         Wed = False
    #                     try:
    #                         Thu = request.POST['single_double4']
    #                     except:
    #                         Thu = False
    #                     try:
    #                         Fri = request.POST['single_double5']
    #                     except:
    #                         Fri = False
    #                     try:
    #                         Sat = request.POST['single_double6']
    #                     except:
    #                         Sat = False
    #                     try:
    #                         Sun = request.POST['single_double7']
    #                     except:
    #                         Sun = False
    #
    #
    #                     from_times1 = request.POST['single_double_sess1_Fromtime'].strip()
    #                     to_times1 = request.POST['single_double_sess1_Totime'].strip()
    #                     from_times2 = request.POST['single_double_sess2_Fromtime'].strip()
    #                     to_times2 = request.POST['single_double_sess2_Totime'].strip()
    #                     schedule_json['session1']['from'] = from_times1
    #                     schedule_json['session1']['to'] = to_times1
    #                     schedule_json['session2']['from'] = from_times2
    #                     schedule_json['session2']['to'] = to_times2
    #
    #                 if time_type == 'single' or time_type == 'single_double':
    #
    #                     if Mon == 'on':
    #                         schedule_json['day']['Mon'] = True
    #                     else:
    #                         schedule_json['day']['Mon'] = False
    #
    #                     if Tue == 'on':
    #                         schedule_json['day']['Tue'] = True
    #                     else:
    #                         schedule_json['day']['Tue'] = False
    #
    #                     if Wed == 'on':
    #                         schedule_json['day']['Wed'] =True
    #                     else:
    #                         schedule_json['day']['Wed'] = False
    #
    #                     if Thu == 'on':
    #                         schedule_json['day']['Thu'] = True
    #                     else:
    #                         schedule_json['day']['Thu'] = False
    #
    #                     if Fri == 'on':
    #                         schedule_json['day']['Fri'] = True
    #                     else:
    #                         schedule_json['day']['Fri'] = False
    #
    #                     if Sat == 'on':
    #                         schedule_json['day']['Sat'] =True
    #                     else:
    #                         schedule_json['day']['Sat'] = False
    #
    #                     if Sun == 'on':
    #                         schedule_json['day']['Sun'] = True
    #                     else:
    #                         schedule_json['day']['Sun'] = False
    #
    #                     xyz = json.dumps(schedule_json)
    #                     kkk = json.loads(xyz)
    #                     template_service = {
    #                         "doctor_id": 0,
    #                         "hospital": {
    #                             "name": "",
    #                             "id": "",
    #
    #                         },
    #                         "designation": "",
    #                         "appointmentMinute": "",
    #                         "consultingCharge": "",
    #                         "time_type": "",
    #                         "time": {
    #
    #                         }
    #                     }
    #
    #                     template_service["doctor_id"] = int(doctor_id)
    #                     template_service["hospital"]["id"] = int(hospital_id)
    #                     org_single = OrganisationName.objects.get(id=int(hospital_id))
    #                     template_service["hospital"]["name"] = org_single.name
    #                     template_service["designation"] = designation
    #                     #template_service["appointmentMinute"] = int(app_minutes)
    #                     try:
    #                         template_service["appointmentMinute"] = int(app_minutes)
    #                     except:
    #                         template_service["appointmentMinute"] = 15
    #                     template_service["consultingCharge"] = float(consultation_charges)
    #                     template_service["did"] = live_schedule_did
    #                     template_service["extension"] = live_schedule_extension
    #
    #                     template_service["time_type"] = time_type
    #                     template_service["time"] = kkk
    #
    #                     global authToken
    #                     template_service['authToken'] = authToken
    #
    #                     global hostname
    #                     global port
    #                     url_p3 = "/api/v2/doctor/add_work_schedule/"
    #                     urlc = hostname + port + url_p3
    #                     # print urlc
    #                     import requests
    #                     url = urlc
    #                     try:
    #                         r = requests.post(url, json=template_service)
    #                         # tempresp = json.dumps(r.text)
    #                         # print r.text
    #                         # print type(r.text)
    #                         resp = json.loads(r.text)
    #                         # print type(resp)
    #                         # print resp
    #
    #                         if r.status_code == 200 or r.status_code == '200':
    #
    #                             if resp['statusCode'] == 200 or resp['statusCode'] == '200':
    #                                 messages.success(request, "Successfully Updated Schedule")
    #                                 return redirect(reverse('live_doctor_listing_edit', args=[int(doctor_id)]) + "?tab=5")
    #
    #                             else:
    #                                 messages.error(request, resp['statusMessage'])
    #                                 messages.success(request, "Updated Schedule But Problem with timing and time_obj")
    #                                 return redirect(reverse('live_doctor_listing_edit', args=[int(doctor_id)]) + "?tab=5")
    #
    #                         else:
    #                             messages.error(request, resp['statusMessage'])
    #                             messages.success(request, "Updated Schedule But Problem with timing and time_obj")
    #                             return redirect(reverse('live_doctor_listing_edit', args=[int(doctor_id)]) + "?tab=5")
    #
    #                     except Exception as e:
    #                         messages.error(request, e)
    #                         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    #
    #                     # messages.success(request, "Successfully Updated Schedule")
    #                     # return redirect(reverse('live_doctor_listing_edit', args=[int(doctor_id)])+"?tab=5")
    #             else:
    #                 messages.error(request, "Schedule Already exists for the given doctor and organisation pair")
    #                 return redirect(reverse('live_doctor_listing_edit', args=[int(doctor_id)]) + "?tab=5")
            # TAB 5----END-------------------------------------------------


            # TAB 6----START-----------------------------------------------

            if tab == '6' and request.method == 'GET':
                return render(request, 'global_search/livedoctor/view_live_doctor_data.html', {
                    'tab_listing': 'live_doctor_listing', 'tab': tab,
                    'live_doctor': live_doctor, 'doctor_id': doctor_id,
                    'live_doc_exp_list': live_doc_exp_list, 'live_doc_rewardrecog_list': live_doc_rewardrecog_list,
                    'live_doc_memb_list': live_doc_memb_list, 'live_doc_education_list': live_doc_education_list,
                    'year_list': year_list,
                    'reviewer_user_data': reviewer_user_data,
                    'publisher_user_data': publisher_user_data,
                    'user_data_complete': user_data_complete,'valid_choice': valid_choice,
                    'category_obj': category_obj,
                    'curent_cat': curent_cat, 'current_seroff': current_seroff,
                    'current_specialities': current_specialities,
                    'speciality': speciality, 'serviceOffered': serviceOffered,'zone_obj': zone_obj,
                    'current_zone': current_zone, 'current_zone_location': current_zone_location,
                    'zone_based_locations': zone_based_locations,
                    'appointment_minutes': appointment_minutes,'list_of_schedules':list_of_schedules,
                    'qualification': qualification,'talk_to_doc':talk_to_doc,'talk_fee':talk_fee,
                    'country_obj': country_obj, 'state_obj': state_obj,
                    'city': city, 'locality': locality,'asso_obj':asso_obj,
                    'emer_localities_list': emer_localities_list,'hostport':hostport,
                    'gallery_image_obj_list':gallery_image_obj_list,'country_obj':country_obj,'state_obj':state_obj,
                    'locality':locality,'all_departments':all_departments,'org_with_current_dep':org_with_current_dep
                })
            # if tab == '6' and request.method == 'POST':
            #     rewardrecog = None
            #     try:
            #         rewardrecog = request.POST['name']
            #     except:
            #         rewardrecog = None
            #
            #     year = request.POST['year']
            #
            #     if rewardrecog and year :
            #         import datetime
            #         now = datetime.datetime.now()
            #         new_rewardrecog = Live_Doctor_Rewardrecog(doctor_id=doctor_id, name=rewardrecog,year=int(year),
            #                                                   createdAt=now)
            #         new_rewardrecog.save()
            #         messages.success(request, "Successfully Added Reward Recognition Entry")
            #         return redirect(reverse('live_doctor_listing_edit', args=[doctor_id]) + '?tab=6')
            #     else:
            #         messages.error(request, "Please provide All Values")
            #         return redirect(reverse('live_doctor_listing_edit', args=[doctor_id]) + '?tab=6')
            # TAB 6----End-----------------------------------------------



            # TAB 7----START-----------------------------------------------
            if tab == '7' and request.method == 'GET':
                return render(request, 'global_search/livedoctor/view_live_doctor_data.html', {
                    'tab_listing': 'live_doctor_listing', 'tab': tab,
                    'live_doctor': live_doctor, 'doctor_id': doctor_id,
                    'live_doc_exp_list': live_doc_exp_list, 'live_doc_rewardrecog_list': live_doc_rewardrecog_list,
                    'live_doc_memb_list': live_doc_memb_list, 'live_doc_education_list': live_doc_education_list,
                    'year_list': year_list,
                    'reviewer_user_data': reviewer_user_data,
                    'publisher_user_data': publisher_user_data,
                    'user_data_complete': user_data_complete,'valid_choice': valid_choice,
                    'category_obj': category_obj,
                    'curent_cat': curent_cat, 'current_seroff': current_seroff,
                    'current_specialities': current_specialities,
                    'speciality': speciality, 'serviceOffered': serviceOffered,'zone_obj': zone_obj,
                    'current_zone': current_zone, 'current_zone_location': current_zone_location,
                    'zone_based_locations': zone_based_locations,
                    'appointment_minutes': appointment_minutes,'list_of_schedules':list_of_schedules,
                    'qualification': qualification,'talk_to_doc':talk_to_doc,'talk_fee':talk_fee,
                    'country_obj': country_obj, 'state_obj': state_obj,
                    'city': city, 'locality': locality,'asso_obj':asso_obj,
                    'emer_localities_list': emer_localities_list,'hostport':hostport,
                    'gallery_image_obj_list':gallery_image_obj_list,'country_obj':country_obj,'state_obj':state_obj,
                    'locality':locality,'all_departments':all_departments,'org_with_current_dep':org_with_current_dep
                })
            # if tab == '7' and request.method == 'POST':
            #     membership = None
            #     try:
            #         membership = request.POST['membership']
            #     except:
            #         membership = None
            #     if membership:
            #         import datetime
            #         now = datetime.datetime.now()
            #         new_membership = Live_Doctor_Membership(doctor_id=doctor_id, name=membership,
            #                                                 createdAt=now)
            #         new_membership.save()
            #         messages.success(request, "Successfully Added Membership Entry")
            #         return redirect(reverse('live_doctor_listing_edit', args=[doctor_id]) + '?tab=7')


            # TAB 7----END-------------------------------------------------

            # TAB 8----START-----------------------------------------------

            if tab == '8' and request.method == 'GET':
                #print live_doctor
                return render(request, 'global_search/livedoctor/view_live_doctor_data.html', {
                    'tab_listing': 'live_doctor_listing', 'tab': tab,
                    'live_doctor': live_doctor, 'doctor_id': doctor_id,
                    'live_doc_exp_list': live_doc_exp_list, 'live_doc_rewardrecog_list': live_doc_rewardrecog_list,
                    'live_doc_memb_list': live_doc_memb_list, 'live_doc_education_list': live_doc_education_list,
                    'year_list': year_list,
                    'reviewer_user_data': reviewer_user_data,
                    'publisher_user_data': publisher_user_data,
                    'user_data_complete': user_data_complete,'valid_choice': valid_choice,
                    'category_obj': category_obj,
                    'curent_cat': curent_cat, 'current_seroff': current_seroff,
                    'current_specialities': current_specialities,
                    'speciality': speciality, 'serviceOffered': serviceOffered,'zone_obj': zone_obj,
                    'current_zone': current_zone, 'current_zone_location': current_zone_location,
                    'zone_based_locations': zone_based_locations,
                    'appointment_minutes': appointment_minutes,'list_of_schedules':list_of_schedules,
                    'qualification': qualification,'talk_to_doc':talk_to_doc,'talk_fee':talk_fee,
                    'country_obj': country_obj, 'state_obj': state_obj,
                    'city': city, 'locality': locality,'asso_obj':asso_obj,
                    'emer_localities_list': emer_localities_list,'hostport':hostport,
                    'gallery_image_obj_list':gallery_image_obj_list,'country_obj':country_obj,'state_obj':state_obj,
                    'locality':locality,'all_departments':all_departments,'org_with_current_dep':org_with_current_dep
                })
                # TAB 8----END-------------------------------------------------


                # TAB 9----START-----------------------------------------------

            if tab == '9' and request.method == 'GET':
                # print live_doctor
                return render(request, 'global_search/livedoctor/view_live_doctor_data.html', {
                    'tab_listing': 'live_doctor_listing', 'tab': tab,
                    'live_doctor': live_doctor, 'doctor_id': doctor_id,
                    'live_doc_exp_list': live_doc_exp_list, 'live_doc_rewardrecog_list': live_doc_rewardrecog_list,
                    'live_doc_memb_list': live_doc_memb_list, 'live_doc_education_list': live_doc_education_list,
                    'year_list': year_list,
                    'reviewer_user_data': reviewer_user_data,
                    'publisher_user_data': publisher_user_data,
                    'user_data_complete': user_data_complete, 'valid_choice': valid_choice,
                    'category_obj': category_obj,
                    'curent_cat': curent_cat, 'current_seroff': current_seroff,
                    'current_specialities': current_specialities,
                    'speciality': speciality, 'serviceOffered': serviceOffered, 'zone_obj': zone_obj,
                    'current_zone': current_zone, 'current_zone_location': current_zone_location,
                    'zone_based_locations': zone_based_locations,
                    'appointment_minutes': appointment_minutes, 'list_of_schedules': list_of_schedules,
                    'qualification': qualification,'talk_to_doc':talk_to_doc,'talk_fee':talk_fee,
                    'country_obj': country_obj, 'state_obj': state_obj,
                    'city': city, 'locality': locality,'asso_obj':asso_obj,
                    'emer_localities_list': emer_localities_list,'hostport':hostport,
                    'gallery_image_obj_list':gallery_image_obj_list,'country_obj':country_obj,'state_obj':state_obj,
                    'locality':locality,'all_departments':all_departments,'org_with_current_dep':org_with_current_dep
                })
                    # TAB 9----END-------------------------------------------------

        else:
            return HttpResponseRedirect(reverse('live-doctor-type'))

    except Exception as e:
        #print e
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    raise Http404


####################################################################
# Name - user_activity_data_date_selection                         #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def user_activity_data_date_selection(request):
    try:
        return render(request, 'admin/user_activity/select_dates.html',{'tab':'user_activity'})
            # CODE THIS TO FETCH DATA FROM KANHAIYA API VIA  In JSON: {"regesterDate": "dt", lastLoginDt: "dt"}
            # AND THEN RENDER TEMPLATE WITH Out JSON: list of users, along with fields listed in the attached UI.
    except Exception as e:
        messages.error(request,e)
        return redirect(request.META('HTTP_REFERER'))
        raise Http404


####################################################################
# Name - show_activity_list                                        #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def show_activity_list(request):
    try:
        if request.method == 'POST':
            reg_date = request.POST['register_date']
            Login_date = request.POST['Login_date']

            tmp = reg_date.split('/')
            reg_date = tmp[1]+'/'+tmp[0]+'/'+tmp[2]
            tmp = Login_date.split('/')
            Login_date = tmp[1] + '/' + tmp[0] + '/' + tmp[2]

            template_service = {
                "authToken": "",
                "regesterDate": "",
                "lastLoginDt": "",
                "page": 1,
                "count":50
            }
            global authToken
            template_service['authToken'] = authToken
            template_service['regesterDate'] = reg_date
            template_service['lastLoginDt'] = Login_date

            # global hostname
            # global port
            # url_p3 = "??????????????"
            # urlc = hostname + port + url_p3
            # # print urlc
            # import requests
            # url = urlc
            # try:
            #     r = requests.post(url, json=template_service)
            #     # tempresp = json.dumps(r.text)
            #     # print r.text
            #     # print type(r.text)
            #     resp = json.loads(r.text)
            #     # print type(resp)
            #     # print resp
            #
            #     if r.status_code == 200 or r.status_code == '200':
            #
            #         if resp['statusCode'] == 200 or resp['statusCode'] == '200':
            #             messages.success(request, "Successfully Updated Schedule")
            #             return redirect(reverse('live_doctor_listing_edit', args=[int(doctor_id)]) + "?tab=5")
            #
            #         else:
            #             messages.error(request, resp['statusMessage'])
            #             messages.success(request, "Updated Schedule But Problem with timing and time_obj")
            #             return redirect(reverse('live_doctor_listing_edit', args=[int(doctor_id)]) + "?tab=5")
            #
            #     else:
            #         messages.error(request, resp['statusMessage'])
            #         messages.success(request, "Updated Schedule But Problem with timing and time_obj")
            #         return redirect(reverse('live_doctor_listing_edit', args=[int(doctor_id)]) + "?tab=5")
            #
            # except Exception as e:
            #     messages.error(request, e)
            #     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            # CODE THIS TO FETCH DATA FROM KANHAIYA API VIA  In JSON: {"regesterDate": "dt", lastLoginDt: "dt"}
            # AND THEN RENDER TEMPLATE WITH Out JSON: list of users, along with fields listed in the attached UI.

            # current_page  1 #from inside json
            # rec_from  =  ((current_page -1)*50)+1
            # rec_to = rec_from +49

            return render(request, 'admin/user_activity/activity_list.html',{'tab':'user_activity','rec_from': '',
                          'rec_to' : ''})

        else:
            pass
    except Exception as e:
        messages.error(request,e)
        return redirect(request.META('HTTP_REFERER'))
        raise Http404

####################################################################
# Name - live_doctor_update_totalexperience                             #
# BY - Ashutosh                                              #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@require_POST
def live_doctor_update_totalexperience(request, doctor_id=None):
    try:
        if doctor_id:
            try:
                asso_obj = Live_Doctor_Associated_Data.objects.get(doctor_id = doctor_id)
                totalexperience = request.POST['totalexperience']
                asso_obj.totalexperience = totalexperience
                asso_obj.save()
                get_notice = Live_Doctor_Notification.objects.all().order_by("-id")[0]
                get_notice.update_Type = 'Total Years Exp. Updated'
                get_notice.save()
                messages.success(request, "Total Year Of Experience has been Successfully saved")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            except Exception as E:
                messages.error(request, "Object Not found")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, "Doctor ID Not Provided")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    except Exception as e:
        raise Http404

# ####################################################################
# # Name - publish_any_new_master                                    #
## Owner - Ashutosh                                                 #
# ####################################################################
@login_required(login_url='/')
@require_POST
@csrf_exempt
def publish_unpublish_any_master_two(request):
    response_data = {
        "Message": "Internal Server Error"
    }
    response = False
    try:
        action = request.POST.get('action')
        master_type = request.POST.get('type')
        id = request.POST.get('checkedValues').split(',')

        if master_type == "country" and id:

            if action == "publish":
                for id in id:
                    try:
                        country_obj = Country.objects.get(id=id)
                    except:
                        pass
                    if country_obj.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = country_obj.id
                        response_data_dict['name'] = country_obj.name
                        response_data_dict['country_code'] = country_obj.country_code
                        response = elasticsearch_client.index_data('master', 'country', id, response_data_dict)
                    else:
                        pass
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully published"
            elif action == "un-publish":
                for id in id:
                    response = elasticsearch_client.delete_document('master', 'country', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    response_data['Message'] = "Data has been sucessfully unpublished"


        if master_type == "state" and id:
            if action == "publish":
                for id in id:
                   try:
                       state_obj = State.objects.get(id=id)
                   except:
                       pass
                   if state_obj.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = state_obj.id
                        response_data_dict['name'] = state_obj.name
                        response_data_dict['state_code'] = state_obj.state_code
                        response_data_dict['country_id'] = state_obj.country.id
                        response_data_dict['country_name'] = state_obj.country.name
                        response = elasticsearch_client.index_data('master', 'state', id, response_data_dict)
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully published"
            elif action == "un-publish":
                for id in id:
                    response = elasticsearch_client.delete_document('master', 'state', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    response_data['Message'] = "Data has been sucessfully unpublished"

        if master_type == "city" and id:
            if action == "publish":
                for id in id:
                    try:
                        city_obj = City.objects.get(id=id)
                    except:
                        pass
                    if city_obj.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = city_obj.id
                        response_data_dict['name'] = city_obj.name
                        response_data_dict['city_code'] = city_obj.city_code
                        response_data_dict['state_id'] = city_obj.state.id
                        response_data_dict['state_name'] = city_obj.state.name
                        response = elasticsearch_client.index_data('master', 'city', id, response_data_dict)
                    else:
                        pass
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully published"
            elif action == "un-publish":
                for id in id:
                    response = elasticsearch_client.delete_document('master', 'city', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    response_data['Message'] = "Data has been sucessfully unpublished"


        if master_type == "locality" and id:
            if action == "publish":
                for id in id:
                    try:
                        locality_obj = Locality.objects.get(id=id)
                    except:
                        pass
                    if locality_obj.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = locality_obj.id
                        response_data_dict['name'] = locality_obj.name
                        response_data_dict['latitude'] = locality_obj.latitude
                        response_data_dict['longitude'] = locality_obj.longitude
                        response_data_dict['city_id'] = locality_obj.city.id
                        response_data_dict['city_name'] = locality_obj.city.name
                        response = elasticsearch_client.index_data('master', 'locality', id, response_data_dict)
                        if response:
                            # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                            response_data['Message'] = "Data has been sucessfully published"
                    else:
                        pass
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    response_data['Message'] = "Data has been sucessfully published"
            elif action == "un-publish":
                for id in id:
                    response = elasticsearch_client.delete_document('master', 'locality', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    response_data['Message'] = "Data has been sucessfully unpublished"


        if master_type == "category" and id:
            if action == "publish":
                for id in id:
                    try:
                        category_obj = Category.objects.get(id=id)
                    except:
                        pass
                    if category_obj.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = category_obj.id
                        response_data_dict['name'] = category_obj.name
                        # response = elasticsearch_client.index_data('master', 'category', id, response_data_dict)
                        response = elasticsearch_client.index_data('globalmaster', 'category', id, response_data_dict)
                    else:
                        pass
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully published"
            elif action == "un-publish":
                # response = elasticsearch_client.delete_document('master', 'category', id)
                for id in id:
                    response = elasticsearch_client.delete_document('globalmaster', 'category', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    response_data['Message'] = "Data has been sucessfully unpublished"


        if master_type == "speciality" and id:
            if action == "publish":
                for id in id :
                    try:
                        speciality_obj = Speciality.objects.get(id=id)
                    except:
                        pass
                    if speciality_obj.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = speciality_obj.id
                        response_data_dict['name'] = speciality_obj.name
                        response_data_dict['category_id'] = speciality_obj.category.id
                        response_data_dict['category_name'] = speciality_obj.category.name
                        response_data_dict['name_with_category'] = ''
                        # response = elasticsearch_client.index_data('master', 'speciality', id, response_data_dict)
                        response = elasticsearch_client.index_data('globalmaster', 'speciality', id, response_data_dict)
                        response = elasticsearch_client.index_data('master', 'speciality', id, response_data_dict)
                    else:
                        pass
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully published"
            elif action == "un-publish":
                # response = elasticsearch_client.delete_document('master', 'speciality', id)
                for id in id:
                    response = elasticsearch_client.delete_document('globalmaster', 'speciality', id)
                    response = elasticsearch_client.delete_document('master', 'speciality', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    response_data['Message'] = "Data has been sucessfully unpublished"

        if master_type == "Doctor_Speciality_New" and id:
            if action == "publish":
                for id in id :
                    response = None
                    try:
                        speciality_obj = Doctor_Speciality_New.objects.get(id=id,deleete=False)

                        if speciality_obj.deleete == False:
                            response_data_dict = {}
                            response_data_dict['id'] = speciality_obj.id
                            response_data_dict['name'] = speciality_obj.name
                            #response_data_dict['category_id'] = 0
                            #response_data_dict['category_name'] = ''
                            #response_data_dict['name_with_category'] = ''
                            # response = elasticsearch_client.index_data('master', 'speciality', id, response_data_dict)
                            response = elasticsearch_client.index_data('globalmaster', 'speciality_new', id, response_data_dict)
                            response = elasticsearch_client.index_data('master', 'speciality_new', id, response_data_dict)
                        else:
                            pass
                    except:
                        pass
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully published"
            elif action == "un-publish":
                # response = elasticsearch_client.delete_document('master', 'speciality', id)
                for id in id:
                    response = elasticsearch_client.delete_document('globalmaster', 'speciality_new', id)
                    response = elasticsearch_client.delete_document('master', 'speciality_new', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    response_data['Message'] = "Data has been sucessfully unpublished"




        if master_type == "service_offered" and id:
            if action == "publish":
                for id in id:
                    try:
                        service_offered_obj = Service_Offred.objects.get(id=id)
                    except:
                        pass
                    if service_offered_obj.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = service_offered_obj.id
                        response_data_dict['name'] = service_offered_obj.name
                        response_data_dict['category_id'] = service_offered_obj.category.id
                        response_data_dict['category_name'] = service_offered_obj.category.name
                        response_data_dict['name_with_category'] = ''
                        # response = elasticsearch_client.index_data('master', 'service_offered', id, response_data_dict)
                        response = elasticsearch_client.index_data('globalmaster', 'service_offered', id, response_data_dict)
                        response = elasticsearch_client.index_data('master', 'service_offered', id, response_data_dict)
                    else:
                        pass
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully published"
            elif action == "un-publish":
                # response = elasticsearch_client.delete_document('master', 'service_offered', id)
                for id in id:
                    response = elasticsearch_client.delete_document('globalmaster', 'service_offered', id)
                    response = elasticsearch_client.delete_document('master', 'service_offered', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    response_data['Message'] = "Data has been sucessfully unpublished"

        if master_type == "Doctor_ServiceOffered_New" and id:
            if action == "publish":
                for id in id:
                    response = None
                    try:
                        service_offered_obj = Doctor_ServiceOffered_New.objects.get(id=id)

                        if service_offered_obj.deleete == False:
                            response_data_dict = {}
                            response_data_dict['id'] = service_offered_obj.id
                            response_data_dict['name'] = service_offered_obj.name
                            #response_data_dict['category_id'] = 0
                            #response_data_dict['category_name'] = ''
                            #response_data_dict['name_with_category'] = ''
                            # response = elasticsearch_client.index_data('master', 'service_offered', id, response_data_dict)
                            response = elasticsearch_client.index_data('globalmaster', 'service_offered_new', id, response_data_dict)
                            response = elasticsearch_client.index_data('master', 'service_offered_new', id, response_data_dict)
                        else:
                            pass
                    except:
                        pass
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully published"
            elif action == "un-publish":
                # response = elasticsearch_client.delete_document('master', 'service_offered', id)
                for id in id:
                    response = elasticsearch_client.delete_document('globalmaster', 'service_offered_new', id)
                    response = elasticsearch_client.delete_document('master', 'service_offered_new', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    response_data['Message'] = "Data has been sucessfully unpublished"

        if master_type == "Cat_SO_SPE_Assocaition_Final" and id:
            if action == "publish":
                for id in id:
                    response = None
                    try:
                        CSSAF = Doc_Cat_SO_Speciality_Association_Final.objects.get(id=id)
                        category_name = Category.objects.get(id=CSSAF.category).name

                        soss = []
                        if CSSAF.ServiceOffered and CSSAF.ServiceOffered != '' and CSSAF.ServiceOffered != ' ':
                            soss = CSSAF.ServiceOffered.strip().split(',')
                            soss = [{'id': int(ccc), 'name': Doctor_ServiceOffered_New.objects.get(id=int(ccc)).name} for ccc in soss]

                        spess = []
                        if CSSAF.Specialities and CSSAF.Specialities != '' and CSSAF.Specialities != ' ':
                            spess = CSSAF.Specialities.strip().split(',')
                            spess =  [{'id':int(ccc), 'name': Doctor_Speciality_New.objects.get(id=int(ccc)).name} for ccc in spess]

                        response_data_dict = {}
                        response_data_dict['id'] = CSSAF.id
                        response_data_dict['category_id'] = CSSAF.category
                        response_data_dict['category_name'] = category_name
                        response_data_dict['service_offered'] = soss
                        response_data_dict['speciality'] = spess

                        # response = elasticsearch_client.index_data('master', 'service_offered', id, response_data_dict)
                        response = elasticsearch_client.index_data('globalmaster', 'cat_so_spe_association', id, response_data_dict)
                        response = elasticsearch_client.index_data('master', 'cat_so_spe_association', id, response_data_dict)

                    except Exception as e:
                        print e
                        pass
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully published"
            elif action == "un-publish":
                # response = elasticsearch_client.delete_document('master', 'service_offered', id)
                for id in id:
                    response = elasticsearch_client.delete_document('globalmaster', 'cat_so_spe_association', id)
                    response = elasticsearch_client.delete_document('master', 'cat_so_spe_association', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    response_data['Message'] = "Data has been sucessfully unpublished"


        if master_type == "labservices" and id:
            if action == "publish":
                for id in id:
                    try:
                        labservices_obj = Lab_services_master.objects.get(id=id)
                    except:
                        pass
                    if labservices_obj.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = labservices_obj.id
                        response_data_dict['name'] = labservices_obj.name
                        # response = elasticsearch_client.index_data('master', 'labservices', id, response_data_dict)
                        response = elasticsearch_client.index_data('globalmaster', 'labservices', id, response_data_dict)
                    else:
                        pass
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully published"
            elif action == "un-publish":
                # response = elasticsearch_client.delete_document('master', 'labservices', id)
                for id in id:
                    response = elasticsearch_client.delete_document('globalmaster', 'labservices', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    response_data['Message'] = "Data has been sucessfully unpublished"


        if master_type == "labtest" and id:
            if action == "publish":
                for id in id :
                    try:
                        labtest_obj = Lab_test_master.objects.get(id=id)
                    except:
                        pass
                    if labtest_obj.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = labtest_obj.id
                        response_data_dict['name'] = labtest_obj.name
                        # response = elasticsearch_client.index_data('master', 'labtest', id, response_data_dict)
                        response = elasticsearch_client.index_data('globalmaster', 'labtest', id, response_data_dict)
                    else:
                        pass
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully published"
            elif action == "un-publish":
                # response = elasticsearch_client.delete_document('master', 'labtest', id)
                for id in id:
                    response = elasticsearch_client.delete_document('globalmaster', 'labtest', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    response_data['Message'] = "Data has been sucessfully unpublished"


        if master_type == "pharmacytype" and id:
            if action == "publish":
                for id in id:
                    try:
                        pharmacytype_obj = MedicalPharmacyStoreType.objects.get(id=id)
                    except:
                        pass
                    if pharmacytype_obj.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = pharmacytype_obj.id
                        response_data_dict['name'] = pharmacytype_obj.name
                        response = elasticsearch_client.index_data('master', 'pharmacytype', id, response_data_dict)
                    else:
                        pass
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully published"
            elif action == "un-publish":
                for id in id:
                    response = elasticsearch_client.delete_document('master', 'pharmacytype', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    response_data['Message'] = "Data has been sucessfully unpublished"


        if master_type == "pharmacyServices" and id:
            if action == "publish":
                for id in id:
                    try:
                        pharmacyServices_obj = MedicalPharmacyStoreServices.objects.get(id=id)
                    except:
                        pass
                    if pharmacyServices_obj.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = pharmacyServices_obj.id
                        response_data_dict['name'] = pharmacyServices_obj.name
                        response = elasticsearch_client.index_data('master', 'pharmacyServices', id, response_data_dict)
                    else:
                        pass
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully published"
                else:
                    pass
            elif action == "un-publish":
                for id in id:
                    response = elasticsearch_client.delete_document('master', 'pharmacyServices', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    response_data['Message'] = "Data has been sucessfully unpublished"


        if master_type == "facility" and id:
            if action == "publish":
                for id in id:
                    try:
                        facility_obj = Facility.objects.get(id=id)
                    except:
                        pass
                    if facility_obj.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = facility_obj.id
                        response_data_dict['name'] = facility_obj.name
                        response = elasticsearch_client.index_data('master', 'facility', id, response_data_dict)
                        response = elasticsearch_client.index_data('globalmaster', 'facility', id, response_data_dict)
                    else:
                        pass
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully published"
                else:
                    pass
            elif action == "un-publish":
                # response = elasticsearch_client.delete_document('master', 'facility', id)
                for id in id:
                    response = elasticsearch_client.delete_document('globalmaster', 'facility', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    response_data['Message'] = "Data has been sucessfully published"


        if master_type == "department" and id:
            if action == "publish":
                for id in id:
                    try:
                        department_obj = Department.objects.get(id=id)
                    except:
                        pass
                    if department_obj.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = department_obj.id
                        response_data_dict['name'] = department_obj.name
                        # response = elasticsearch_client.index_data('master', 'department', id, response_data_dict)
                        response = elasticsearch_client.index_data('globalmaster', 'department', id, response_data_dict)
                    else:
                        pass
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully published"
                else:
                    pass
            elif action == "un-publish":
                # response = elasticsearch_client.delete_document('master', 'department', id)
                for id in id:
                    response = elasticsearch_client.delete_document('globalmaster', 'department', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    response_data['Message'] = "Data has been sucessfully unpublished"


        if master_type == 'countrymaster':
            if action=="publish":
                for id in id:
                    try:
                        countrymaster = Countrymaster.objects.get(id=id)
                    except:
                        pass
                    if countrymaster.deletee == False:
                        response_data_dict = {}
                        response_data_dict['id'] = countrymaster.id
                        response_data_dict['name'] = countrymaster.name
                        response = elasticsearch_client.index_data('nonsearchmaster', 'countrymaster', id, response_data_dict)
                    else:
                        pass
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully published"
            if action=="un-publish":
                for id in id:
                    response = elasticsearch_client.delete_document('nonsearchmaster', 'countrymaster', id)

                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully published"


        if master_type == 'statemaster' and id:
            if action == "publish":
                for id in id:
                    try:
                        statemaster = Statemaster.objects.get(id=id)
                    except:
                        pass
                    if statemaster.deletee == False:
                        response_data_dict = {}
                        response_data_dict['id'] = statemaster.id
                        response_data_dict['name'] = statemaster.name
                        response_data_dict['country_id'] = statemaster.countrymaster.id
                        response = elasticsearch_client.index_data('nonsearchmaster', 'statemaster', id, response_data_dict)
                    else:
                        pass
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully published"
                else:
                    pass
            if action=="un-publish":
                for id in id:
                    response = elasticsearch_client.delete_document('nonsearchmaster', 'statemaster', id)
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully unpublished"


        if master_type == 'citymaster' and id:

            if action=="publish":
                for id in id:
                    try:
                        citymaster = Citymaster.objects.get(id=id)
                    except:
                        pass
                    if citymaster.deletee == False:
                        response_data_dict = {}
                        response_data_dict['id'] = citymaster.id
                        response_data_dict['name'] = citymaster.name
                        response_data_dict['state_id'] = citymaster.statemaster.id
                        response = elasticsearch_client.index_data('nonsearchmaster', 'citymaster', id, response_data_dict)
                    else:
                        pass
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully published"
            if action=="un-publish":
                for id in id:
                    response = elasticsearch_client.delete_document('nonsearchmaster', 'citymaster', id)
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully published"


        if master_type == 'localitymaster' and id:
            if action=="publish":
                for id in id:
                    try:
                        localitymaster = Localitymaster.objects.get(id=id, deletee=False)
                    except:
                        pass
                    if localitymaster.deletee == False:
                        response_data_dict = {}
                        response_data_dict['id'] = localitymaster.id
                        response_data_dict['name'] = localitymaster.name
                        response_data_dict['city_id'] = localitymaster.citymaster.id
                        response = elasticsearch_client.index_data('nonsearchmaster', 'localitymaster', id, response_data_dict)
                    else:
                        pass
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully published"

            if action=="un-publish":
                for id in id:
                    response = elasticsearch_client.delete_document('nonsearchmaster', 'localitymaster', id)
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully unpublished"

        if master_type == 'diseasesearchmaster' and id:
            if action=="publish":
                for id in id:
                    try:
                        disease_search_master = Disease_search_master.objects.get(id=id, delete=False)
                    except Exception as e:
                        #print e
                        pass
                    if disease_search_master.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = disease_search_master.id
                        response_data_dict['name'] = disease_search_master.name
                        response = elasticsearch_client.index_data('globalmaster', 'disease', id, response_data_dict)
                    else:
                        pass
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully published"
            if action=="un-publish":
                for id in id:
                    response = elasticsearch_client.delete_document('globalmaster', 'disease', id)
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully unpublished"

        if master_type == 'organisation_types' and id:
            if action=="publish":
                for id in id:
                    try:
                        organisation_types = Organisation_types.objects.get(id=id, delete=False)
                    except Exception as e:
                        #print e
                        pass
                    if organisation_types.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = organisation_types.id
                        response_data_dict['name'] = organisation_types.type_name
                        response = elasticsearch_client.index_data('globalmaster', 'organisationtypes', id, response_data_dict)
                    else:
                        pass
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully published"
            if action=="un-publish":
                for id in id:
                    response = elasticsearch_client.delete_document('globalmaster', 'organisationtypes', id)
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully unpublished"

        if master_type == 'labdepartment' and id:
            if action == "publish":
                for id in id:
                    try:
                        lab_department_master = Lab_department_master.objects.get(id=id, delete=False)
                    except Exception as e:
                        #print e
                        pass
                    if lab_department_master.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = lab_department_master.id
                        response_data_dict['name'] = lab_department_master.name
                        response = elasticsearch_client.index_data('globalmaster', 'labdepartments', id, response_data_dict)
                    else:
                        pass
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully published"
            if action=="un-publish":
                for id in id:
                    response = elasticsearch_client.delete_document('globalmaster', 'labdepartments', id)
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully unpublished"

        if master_type == 'symptomssearch' and id:
            if action == "publish":
                for id in id:
                    try:
                        symptoms_search_master = Symptoms_search_master.objects.get(id=id, delete=False)
                    except Exception as e:
                        #print e
                        pass
                    if symptoms_search_master.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = symptoms_search_master.id
                        response_data_dict['name'] = symptoms_search_master.name
                        response = elasticsearch_client.index_data('globalmaster', 'symptom', id, response_data_dict)
                    else:
                        pass
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully published"
            if action=="un-publish":
                for id in id:
                    response = elasticsearch_client.delete_document('globalmaster', 'symptom', id)
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully unpublished"

        if master_type == 'labaccrediton' and id:
            if action == "publish":
                for id in id:
                    try:
                        lab_accreditation = Lab_accreditation_body_master.objects.get(id=id, delete=False)
                    except Exception as e:
                        #print e
                        pass
                    if lab_accreditation.delete == False:
                        response_data_dict = {}
                        response_data_dict['address'] = lab_accreditation.address
                        response_data_dict['pincode'] = lab_accreditation.pincode
                        response_data_dict['telephone'] = lab_accreditation.telephone
                        response_data_dict['id'] = lab_accreditation.id
                        response_data_dict['name'] = lab_accreditation.name
                        response = elasticsearch_client.index_data('globalmaster', 'labaccreditation', id, response_data_dict)
                    else:
                        pass
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully published"
            if action=="un-publish":
                for id in id:
                    response = elasticsearch_client.delete_document('globalmaster', 'labaccreditation', id)
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully unpublished"

        if master_type == 'healthoholictype' and id:
            if action == "publish":
                for id in id:
                    try:
                        healthoholic_subtype = Healthoholic_subtype_master.objects.get(id=id, delete=False)
                    except Exception as e:
                        #print e
                        pass
                    if healthoholic_subtype.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = healthoholic_subtype.id
                        response_data_dict['name'] = healthoholic_subtype.name
                        response = elasticsearch_client.index_data('master', 'healthoholic', id, response_data_dict)
                    else:
                        pass
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully published"
            if action=="un-publish":
                for id in id:
                    response = elasticsearch_client.delete_document('master', 'healthoholic', id)
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully unpublished"

        if master_type == 'labType' and id:
            if action == "publish":
                for id in id:
                    try:
                        lab_type_master = Lab_type_master.objects.get(id=id, delete=False)
                    except Exception as e:
                        #print e
                        pass
                    if lab_type_master.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = lab_type_master.id
                        response_data_dict['name'] = lab_type_master.name
                        response = elasticsearch_client.index_data('master', 'labtypes', id, response_data_dict)
                    else:
                        pass
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully published"
            if action=="un-publish":
                for id in id:
                    response = elasticsearch_client.delete_document('master', 'labtypes', id)
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    response_data['Message'] = "Data has been sucessfully unpublished"
        else:
            if response == False:
                response_data['Message'] = "Cannot  publish or Unpublish"


    except Exception as e:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    response_data = json.dumps(response_data)
    return HttpResponse(response_data)

####################################################################
# Name - delete_live_doc_private_images                             #
# BY - Ashutosh kesharvani                                          #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def delete_live_doc_private_images(request, doctor_id=None):
    try:
        if doctor_id:
            try:
                doc_obj = Live_Doctor.objects.get(id=int(doctor_id))
                test = doc_obj.privateimagepath.split(',')
                path_list = request.POST.getlist('Images')
                newpath = ""
                if path_list != []:
                    for path in test:
                        #print path
                        path = str(path)
                        if path not in path_list:
                            if newpath != "":
                                newpath = newpath + ',' + str(path)
                            else:
                                newpath = str(path)
                    doc_obj.privateimagepath = str(newpath)
                    doc_obj.save()
                    get_notice = Live_Doctor_Notification.objects.all().order_by("-id")[0]
                    get_notice.update_Type = 'Private Image(s) Deleted'
                    get_notice.save()

                    messages.success(request, "Image has been deleted")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                else:
                    messages.error(request, "No Image to be deleted")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except Exception as e:
                messages.error(request, "Something Bad had happened")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        raise Http404

####################################################################
# Name - upload_privateimage                                        #
# BY - Ashutosh kesharvani                                          #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def upload_privateimage(request, doctor_id=None):
    try:
        if doctor_id and request.method == 'POST':
            try:
                doc_obj = Live_Doctor.objects.get(id=int(doctor_id))
                all_doc_obj = Live_Doctor.objects.all()

                if len(request.FILES) == 1:
                    image = request.FILES['privateimage']
                    imagename = request.FILES['privateimage'].name
                    iname = ""
                    for i in imagename:
                        if i == ' ' or i == '-' or i == '(' or i == ')' or i == ',':
                            iname = iname + '_'
                        else:
                            iname = iname + i
                    file_name = '/static/images/livedocpvtimg' + '/' + iname
                    file_name11 = '/static/images/livedocpvtimg' + '/' + iname

                    test = []
                    flag = 0
                    i = 1
                    for single_doc_obj in all_doc_obj:
                        if single_doc_obj.privateimagepath:
                            test = single_doc_obj.privateimagepath.split(',')
                            for privateimage in test:
                                if privateimage == file_name:
                                    i = i + 1
                                    file_name = file_name11
                                    file_name = file_name.split('.')
                                    file_name = file_name[0] + '_' + str(i) + '.' + file_name[1]
                                    flag = 1
                        else:
                            pass
                    if flag == 1:
                        iname = iname.split('.')
                        iname = iname[0] + '_' + str(i) + '.' + iname[1]
                        file_name = '/static/images/livedocpvtimg' + '/' + iname
                    import os
                    from django.conf import settings
                    filepath = os.path.join(settings.BASE_DIR,
                                            'hfu_cms/static/images/livedocpvtimg') + '/' + iname
                    # filepath = os.path.join(settings.BASE_DIR, 'hfu_cms/staticforimage/images/livedocpvtimg') + '/' + iname
                    # filepath='/home/jaguar/17June-CMSV1/cms/cms-v1/hfu_cms/static/images/livedocpvtimg' + '/' + iname
                    # filepath = '/17June-CMSV1/cms/cms-v1/hfu_cms/static/images/livedocpvtimg'+ '/' + iname
                    # filepath = '/home/jaguar/17June-CMSV1/cms/cms-v1/media/livedocprivateimage' + '/' + iname
                    fh = open(filepath, "wb")
                    fh.write(image.read())
                    fh.close()
                    b = ""
                    if doc_obj.privateimagepath:
                        b = doc_obj.privateimagepath + "," + file_name
                    else:
                        b = file_name
                    doc_obj.privateimagepath = b
                    doc_obj.save()
                    get_notice = Live_Doctor_Notification.objects.all().order_by("-id")[0]
                    get_notice.update_Type = 'Private Image Added'
                    get_notice.save()

                    messages.success(request, "Image Uploaded")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                else:
                    messages.error(request, "No Image to upload")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except Exception as e:
                raise Http404
        else:
            messages.error(request, "Something bad had happened")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        raise Http404




####################################################################
# Name - delete_live_doc_private_images                             #
# BY - Ashutosh kesharvani                                          #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def markascomplete(request):
    try:
        if request.method == "POST":
            try:
                xx = request.POST['xx']
            except:
                xx = 'lab'
            all_validation = ValidateByChoice.objects.all()

            if xx == 'lab':
                all_publisher = UserManagement.objects.filter(is_publisher=True)
                all_reviewwer = UserManagement.objects.filter(is_reviewer = True,is_path_reviewer=True)
                all_caller = UserManagement.objects.filter(is_caller=True,is_path_caller=True)
            if xx == 'doctor' or xx == 'livedoctor' or xx == 'organisation':
                all_publisher = UserManagement.objects.filter(is_publisher=True)
                all_reviewwer = UserManagement.objects.filter(is_reviewer = True,is_doctor_reviewer=True)
                all_caller = UserManagement.objects.filter(is_caller=True,is_doctor_caller=True)
            if xx == 'ambulance':
                all_publisher = UserManagement.objects.filter(is_publisher=True)
                all_reviewwer = UserManagement.objects.filter(is_reviewer = True,is_ambulance_reviewer=True)
                all_caller = UserManagement.objects.filter(is_caller=True,is_ambulance_caller=True)
            if xx == 'pharmacy':
                all_publisher = UserManagement.objects.filter(is_publisher=True)
                all_reviewwer = UserManagement.objects.filter(is_reviewer = True,is_phar_reviewer=True)
                all_caller = UserManagement.objects.filter(is_caller=True,is_phar_caller=True)
            if xx == 'rehab':
                all_publisher = UserManagement.objects.filter(is_publisher=True)
                all_reviewwer = UserManagement.objects.filter(is_reviewer = True,is_physio_rehab_reviewer=True)
                all_caller = UserManagement.objects.filter(is_caller=True,is_physio_rehab_caller=True)
            if xx == 'bloodbank':
                all_publisher = UserManagement.objects.filter(is_publisher=True)
                all_reviewwer = UserManagement.objects.filter(is_reviewer = True,is_blood_reviewer=True)
                all_caller = UserManagement.objects.filter(is_caller=True,is_blood_caller=True)
            if xx == 'dietitian':
                all_publisher = UserManagement.objects.filter(is_publisher=True)
                all_reviewwer = UserManagement.objects.filter(is_reviewer = True,is_dietitian_reviewer=True)
                all_caller = UserManagement.objects.filter(is_caller=True,is_dietitian_caller=True)
            if xx == 'disease':
                all_publisher = UserManagement.objects.filter(is_publisher=True)
                all_reviewwer = UserManagement.objects.filter(is_reviewer = True,is_disease_reviewer=True)
                all_caller = UserManagement.objects.filter(is_caller=True,is_disease_caller=True)
            if xx == 'drug':
                all_publisher = UserManagement.objects.filter(is_publisher=True)
                all_reviewwer = UserManagement.objects.filter(is_reviewer = True,is_disease_reviewer=True)
                all_caller = UserManagement.objects.filter(is_caller=True,is_disease_caller=True)
            if xx == 'nursebureau':
                all_publisher = UserManagement.objects.filter(is_publisher=True)
                all_reviewwer = UserManagement.objects.filter(is_reviewer = True,is_nurse_bureau_reviewer=True)
                all_caller = UserManagement.objects.filter(is_caller=True,is_nurse_bureau_caller=True)
            if xx == 'therapist':
                all_publisher = UserManagement.objects.filter(is_publisher=True)
                all_reviewwer = UserManagement.objects.filter(is_reviewer = True,is_therapist_reviewer=True)
                all_caller = UserManagement.objects.filter(is_caller=True,is_therapist_caller=True)
            if xx == 'therapist':
                all_publisher = UserManagement.objects.filter(is_publisher=True)
                all_reviewwer = UserManagement.objects.filter(is_reviewer = True,is_therapist_reviewer=True)
                all_caller = UserManagement.objects.filter(is_caller=True,is_therapist_caller=True)
            if xx == 'wellnessnews' or xx =='globalnews' or xx =='healthnews' or xx=='doctorsfeed':
                all_publisher = UserManagement.objects.filter(is_publisher=True)
                all_reviewwer = UserManagement.objects.filter(is_news_reviewer=True)
                all_caller = UserManagement.objects.filter(is_news=True)
            if xx == 'homeplan' or xx =='lifeplan' or xx =='enterpriseplan':
                all_publisher = UserManagement.objects.filter(is_publisher=True)
                all_reviewwer = UserManagement.objects.filter(is_service_reviewer=True)
                all_caller = UserManagement.objects.filter(is_service_plan=True)

            dj = []
            data = []
            for d in all_publisher:
                if d.user.is_active:
                    dict = {}
                    dict['id'] = d.user.id
                    dict['name'] = d.user.username
                    dj.append(dict)
            data.append(dj)

            dj = []
            for d in all_reviewwer:
                if d.user.is_active:
                    dict = {}
                    dict['id'] = d.user.id
                    dict['name'] = d.user.username
                    dj.append(dict)
            data.append(dj)

            dj = []
            for d in all_caller:
                if d.user.is_active:
                    dict = {}
                    dict['id'] = d.user.id
                    dict['name'] = d.user.username
                    dj.append(dict)
            data.append(dj)

            dj = []
            for d in all_validation:
                dict = {}
                dict['id'] = d.id
                dict['name'] = d.name
                dj.append(dict)
            data.append(dj)

            # data.append(reviewer_user_data)
            #
            # data.append(publisher_user_data)

            # data.append(valid_choice)
            #
            # data.append(user_data_complete)

            #print data
            if data:
                data = json.dumps(data)

    except Exception as e:
        raise Http404
    return HttpResponse(data)


####################################################################
# Name - reverse_to_any_user for publisher listing                  #
# BY - Ashutosh kesharvani                                          #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def reverse_to_any_user(request):
    respons = {}
    try:
        if request.method == "POST":
            u = request.user
            uid = u.id
            all_user = UserManagement.objects.all()
            for us in all_user:
                if us.user.id == uid:
                    if us.is_caller == True:
                        user_type = 'caller'
                        break
                    if us.is_reviewer == True:
                        user_type = 'reviewer'
                        break
                    if us.is_publisher == True:
                        user_type = 'publisher'
                        break
                    if us.is_news == True:
                        user_type = 'news_caller'
                        break
            if request.user.is_superuser:
                user_type = 'Admin'
            typ = request.POST['typ']
            ids = request.POST['checkedValues'].split(',')
            try:
                xx = request.POST['xx']
            except:
                xx ='lab'
            if xx == 'lab':
                model = Labs
                if user_type == 'publisher':
                    url ='/publisher/lab/listing/'
                else:
                    url ='/lab/listing/'
            if xx == 'doctor':
                model = Doctor
                if user_type == 'publisher':
                    url ='/publisher/doctor/listing/'
                else:
                    url ='/doctor/listing/'
            if xx == 'livedoctor':
                model = Live_Doctor
                if user_type == 'publisher':
                    url ='/publisher/live-doctor/listing/'
                else:
                    url ='/live-doctor/listing/new-registrations/'
            if xx == 'organisation':
                model = OrganisationName
                if user_type == 'publisher':
                    url ='/publisher/organisation/listing/'
                else:
                    url ='/organisation/listing/'
            if xx == 'ambulance':
                model = Ambulance
                if user_type == 'publisher':
                    url ='/publisher/ambulance/listing/'
                else:
                    url ='/ambulance/listing/'
            if xx == 'bloodbank':
                model = BloodBank
                if user_type == 'publisher':
                    url ='/publisher/blood-bank/listing/'
                else:
                    url ='/blood-bank/listing/'

            if xx == 'nursebureau':
                model = Nurse_Bureau
                if user_type == 'publisher':
                    url ='/publisher/nurse_bureau/listing/'
                else:
                    url ='/nurse_bureau/listing/'
            if xx == 'dietitian':
                model = Dietitian
                if user_type == 'publisher':
                    url ='/publisher/dietitian/listing/'
                else:
                    url ='/dietitian/listing/'
            if xx == 'disease':
                model = Disease
                if user_type == 'publisher':
                    url ='/publisher/disease/listing/'
                else:
                    url ='/disease/listing/'
            if xx == 'pharmacy':
                model = MedicalPharmacyStore
                if user_type == 'publisher':
                    url ='/publisher/pharmacy/listing/'
                else:
                    url ='/pharmacy/listing/'
            if xx == 'rehab':
                model = RehabCenter
                if user_type == 'publisher':
                    url ='/publisher/rehab/listing/'
                else:
                    url ='/rehab/listing/'
            if xx == 'therapist':
                model = Therapist
                if user_type == 'publisher':
                    url ='/publisher/therapist/listing/'
                else:
                    url ='/therapist/listing/'
            if xx == 'drug':
                model = Drug
                if user_type == 'publisher':
                    url ='/publisher/drug/listing/'
                else:
                    url ='/drug/listing/'
            if xx == 'symptoms':
                model = Symptoms
                if user_type == 'publisher':
                    url ='/publisher/symptoms/listing/'
                else:
                    url ='/symptoms/listing/'
            if xx == 'wellnessnews':
                model = NewsFeed
                if user_type == 'publisher':
                    url ='/news-feed/publish/get/wellness/'
                else:
                    url ='/news-feed/wellness/listing/'
            if xx == 'healthnews':
                model = NewsFeed
                if user_type == 'publisher':
                    url ='/news-feed/publish/get/health/'
                else:
                    url ='/news-feed/health/listing/'
            if xx == 'globalnews':
                model = NewsFeed
                if user_type == 'publisher':
                    url ='/news-feed/publish/get/global/'
                else:
                    url ='/news-feed/global/listing/'
            if xx == 'homeplan':
                model = ServicePlan
                if user_type == 'publisher':
                    url ='/service/publisher/home/plan/listing/'
                else:
                    url ='service/home/plan/listing/'
            if xx == 'lifeplan':
                model = ServicePlan
                if user_type == 'publisher':
                    url ='/service/publisher/life/plan/listing/'
                else:
                    url ='/service/life/plan/listing/'
            if xx == 'enterpriseplan':
                model = ServicePlan
                if user_type == 'publisher':
                    url ='/service/publisher/enterprise/plan/listing/'
                else:
                    url ='/service/enterprise/plan/listing/'
            if xx == 'doctorsfeed':
                model = Doctorsfeed
                if user_type == 'Admin':
                    url ='/news-feed/management/doctor/'
                else:
                    url ='/service/enterprise/plan/listing/'

            if user_type == 'Admin':
                if typ == 'caller':
                    try:
                        free_text = request.POST['acfreetext']
                        curr_user = request.POST['callername_admin']
                    except:
                        free_text = None
                        curr_user = None
                    if curr_user != None:
                        for id in ids:
                            obj = model.objects.get(id=id)
                            #print obj.stage_id
                            if obj.stage_id != 5:
                                pre_user = obj.current_user.id
                                obj.previous_user = pre_user
                                obj.current_user_id = int(curr_user)
                                obj.free_text = free_text
                                obj.stage_id = 2
                                obj.save()
                                respons['Message'] = "Data has been moved successfully"
                            else:
                                respons['Message'] = "Published data cannot move"
                elif typ == 'rev':
                    try:
                        free_text = request.POST['arfreetext']
                        curr_user = request.POST['reviewerrname_admin']
                    except:
                        free_text = None
                        curr_user = None
                    if curr_user != None:
                        for id in ids:
                            obj = model.objects.get(id=id)
                            #print obj.stage_id
                            if obj.stage_id != 5:
                                pre_user = obj.current_user.id
                                obj.previous_user = pre_user
                                obj.current_user_id = int(curr_user)
                                obj.free_text = free_text
                                obj.stage_id = 3
                                obj.save()
                                respons['Message'] = "Data has been moved successfully"
                            else:
                                respons['Message'] = "Published data cannot move"
                elif typ == 'publisher':
                    try:
                        curr_user = request.POST['publishername_admin']
                        free_text = request.POST['apfreetext']
                        # v_choice = ValidateByChoice.objects.get(id=v)
                    except Exception as e:
                        curr_user = None
                        free_text = None
                    if curr_user != None:
                        for id in ids:
                            obj = model.objects.get(id=id)
                            #print obj.stage_id
                            if obj.stage_id != 5:
                                pre_user = obj.current_user.id
                                obj.previous_user = pre_user
                                obj.current_user_id = int(curr_user)
                                obj.free_text = free_text
                                obj.stage_id = 4
                                obj.save()
                                respons['Message'] = "Data has been moved successfully"
                            else:
                                respons['Message'] = "Published data cannot move"

            if user_type == 'publisher':
                if typ == 'caller':
                    try:
                        free_text = request.POST['pcfreetext']
                        curr_user = request.POST['caller_name']
                    except:
                        free_text = None
                        curr_user = None
                    if curr_user != None:
                        for id in ids:
                            obj = model.objects.get(id=id)
                            #print obj.stage_id
                            if obj.stage_id != 5:
                                pre_user = obj.current_user.id
                                obj.previous_user = pre_user
                                obj.current_user_id = int(curr_user)
                                obj.free_text = free_text
                                obj.stage_id = 2
                                obj.save()
                                respons['Message'] = "Data has been moved successfully"
                            else:
                                respons['Message'] = "Published data cannot move"
                elif typ == 'reviewer':
                    try:
                        free_text = request.POST['prfreetext']
                        curr_user = request.POST['reviewer_name']
                    except:
                        free_text = None
                        curr_user = None
                    if curr_user != None:
                        for id in ids:
                            obj = model.objects.get(id=id)
                            #print obj.stage_id
                            if obj.stage_id != 5:
                                pre_user = obj.current_user.id
                                obj.previous_user = pre_user
                                obj.current_user_id = int(curr_user)
                                obj.free_text = free_text
                                obj.stage_id = 3
                                obj.save()
                                respons['Message'] = "Data has been moved successfully"
                            else:
                                respons['Message'] = "Published data cannot move"
            if user_type =='reviewer':
                if typ == 'caller':
                    try:
                        free_text = request.POST['rcfreetext']
                        curr_user = request.POST['callername_reviewer']
                    except Exception as e:
                        free_text = None
                        curr_user = None
                    if curr_user != None:
                        for id in ids:
                            obj = model.objects.get(id=id)
                            #print obj.stage_id
                            if obj.stage_id != 5:
                                pre_user = obj.current_user.id
                                obj.previous_user = pre_user
                                obj.current_user_id = int(curr_user)
                                obj.free_text = free_text
                                obj.stage_id = 2
                                obj.save()
                                respons['Message'] = "Data has been moved successfully"
                            else:
                                respons['Message'] = "Published data cannot move"

                if typ == 'publisher':
                    try:
                        curr_user = request.POST['publishername_revi']
                        v = request.POST['validchoices_reviewer']
                        v_choice = ValidateByChoice.objects.get(id=v)
                    except Exception as e:
                        curr_user = None
                        v_choice = None
                    if curr_user != None:
                        for id in ids:
                            obj = model.objects.get(id=id)
                            #print obj.stage_id
                            if obj.stage_id != 5:
                                pre_user = obj.current_user.id
                                obj.previous_user = pre_user
                                obj.current_user_id = int(curr_user)
                                obj.resource_validate = v_choice
                                obj.stage_id = 4
                                obj.save()
                                respons['Message'] = "Data has been moved successfully"
                            else:
                                respons['Message'] = "Published data cannot move"
            if user_type == 'caller':
                try:
                    curr_usr = request.POST['reviewerrname_caller']
                    v = request.POST['validchoices_caller']
                    valid_choices = ValidateByChoice.objects.get(id=v)
                except:
                    reviewer_name = None
                    valid_choices = None
                if curr_usr != None:
                    for id in ids:
                        obj = model.objects.get(id=id)
                        #print obj.stage_id
                        if obj.stage_id != 5:
                            pre_user = obj.current_user.id
                            obj.previous_user = pre_user
                            obj.current_user_id = int(curr_usr)
                            obj.resource_validate = valid_choices
                            obj.stage_id = 3
                            obj.save()
                            respons['Message'] = "Data has been moved successfully"
                        else:
                            respons['Message'] = "Published data cannot move"
        respons['RedirectUrl'] = url
        respons['Redirect'] = True
        response_data = json.dumps(respons)

        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        raise 404
    try:
        return HttpResponse(response_data)

    except Exception as e:
        #print 1
        pass
####################################################################################
# name : For merging crawled doctor into livedoctor                                #
# owner : Dhrumil Shah                                                             #
####################################################################################
@login_required(login_url='/')
@csrf_exempt
def merge_duplicates(request, merge_id=None, doctor_id=None):
    try:
        if merge_id and doctor_id:
            try:
                live_doctor_obj = Live_Doctor.objects.get(id=int(doctor_id))
                merge_doctor_obj = Doctor.objects.get(id=int(merge_id))
                live_merge_records = live_doctor_obj.merge_fields
            except:
                live_doctor_obj = None
                merge_doctor_obj= None
            merge_records = []
            count = 0
            flagg = 0
            from datetime import datetime
            d= datetime.now()
            merge_records.append({"Date Of Merging":str(d)})
            merge_records.append({"MERGE_DOC_ID":str(merge_doctor_obj.id).strip()})
            if live_doctor_obj.category == None or live_doctor_obj.category == '':
                if merge_doctor_obj.category != None and merge_doctor_obj.category != '':
                    live_doctor_obj.category = int(merge_doctor_obj.category_id)
                    flagg=1
                    c_id = int(merge_doctor_obj.category_id)
                    cat = Category.objects.get(id=c_id)
                    c_name = cat.name
                    merge_records.append({"CATEGORY":str(c_name).strip()})
                    count = 1
            else:
                if live_doctor_obj.category == merge_doctor_obj.category.id:
                    flagg =1

            if live_doctor_obj.dob == None or live_doctor_obj.dob == '':
                if merge_doctor_obj.dob != None and merge_doctor_obj.dob != '':
                    dr_dob = str(merge_doctor_obj.dob).strip()
                    dob = dr_dob.split('-')
                    live_dob = dob[2] + '/' + dob[1] + '/' + dob[0]
                    live_doctor_obj.dob = live_dob
                    merge_records.append({"DOB":str(live_dob).strip()})
                    count = 1

            if live_doctor_obj.speciality == None or live_doctor_obj.speciality == []:
                if flagg == 1:
                    if merge_doctor_obj.speciality != None and merge_doctor_obj.speciality != '':
                        speciality = []
                        spe_name = []
                        json_list_spe = []
                        speciality_data = str(merge_doctor_obj.speciality).strip()
                        speciality = speciality_data.split(',')
                        for i in speciality:
                            obj = Speciality.objects.get(id=int(i))
                            json_list_spe.append({"id": int(i), "name": obj.name})
                            spe_name.append(str(obj.name).strip())
                        live_doctor_obj.speciality = json_list_spe
                        merge_records.append({"SPECIALITY":spe_name})
                        count = 1

            if live_doctor_obj.serviceOffered == None or live_doctor_obj.serviceOffered == []:
                if flagg ==1:
                    if merge_doctor_obj.service_offered != None and merge_doctor_obj.service_offered != '':
                        service = []
                        ser_name = []
                        json_list_so = []
                        so_data = str(merge_doctor_obj.service_offered).strip()
                        service = so_data.split(',')

                        for i in service:
                            obj = Service_Offred.objects.get(id=int(i))
                            json_list_so.append({"id": int(i), "name": obj.name})
                            ser_name.append(str(obj.name).strip())
                        live_doctor_obj.serviceOffered = json_list_so
                        merge_records.append({"SERVICES_OFFERED":ser_name})
                        count = 1

            if live_doctor_obj.phoneNo == None or live_doctor_obj.phoneNo == '':
                if merge_doctor_obj.phone != None and merge_doctor_obj.phone != '':
                    live_doctor_obj.phoneNo = merge_doctor_obj.phone
                    merge_records.append({"PHONE_NO":str(merge_doctor_obj.phone).strip()})
                    count = 1

            if live_doctor_obj.alternateEmail == None or live_doctor_obj.alternateEmail == '':
                if merge_doctor_obj.email != None and merge_doctor_obj.email != '':
                    live_doctor_obj.alternateEmail = merge_doctor_obj.email
                    merge_records.append({"ALTERNATE_EMAIL":str(merge_doctor_obj.email).strip()})
                    count = 1
            try:
                if merge_doctor_obj.registration_data != None and merge_doctor_obj.registration_data != '':
                    regis_details = str(merge_doctor_obj.registration_data).strip()
                    regis_no = ''
                    regis_board = ''
                    regis_yr = ''
                    temp = ''
                    i = 0
                    for num in regis_details:
                        if num != ' ':
                            temp = temp + num
                            i = i + 1
                        elif num == ' ':
                            regis_no = temp
                            temp = ''
                            snum = i + 1
                            temp = regis_details[snum:len(regis_details)]

                            break
                    temp2 = str(temp).strip()
                    temp = ''
                    if temp2 != '':
                        for i in temp2:
                            if i != ',':
                                temp = temp + i
                            elif i == ',':
                                regis_board = temp
                                temp = ''
                        regis_yr = temp
                    try:
                        if live_doctor_obj.mciRegistrationNo == None or live_doctor_obj.mciRegistrationNo == '':
                            if regis_no != '':
                                live_doctor_obj.mciRegistrationNo = regis_no
                                merge_records.append({"MCI_NO":str(regis_no).strip()})
                                count = 1
                        if live_doctor_obj.registrationBoard == None or live_doctor_obj.registrationBoard == '':
                            if regis_board != '':
                                live_doctor_obj.registrationBoard = str(regis_board).strip()
                                merge_records.append({"MCI_BOARD":str(regis_board).strip()})
                                count = 1
                        if not live_doctor_obj.registrationYear:
                            if regis_yr != '':
                                live_doctor_obj.registrationYear = int(regis_yr)
                                merge_records.append({"MCI_YEAR":str(regis_yr).strip()})
                                count = 1
                    except Exception as e:
                        #print e
                        pass
            except Exception as e:
                #print e
                pass
            live_doc_exp_obj = Live_Doctor_Experience.objects.filter(doctor_id=doctor_id)
            if not live_doc_exp_obj:
                doc_exp_obj = Doctor_Experience.objects.filter(doctor_id=merge_id)
                if doc_exp_obj:
                    count = count + 1
                    import datetime
                    merge_exp = []
                    for d in doc_exp_obj:
                        merge_exp_details = []
                        temp = (d.experience_data).strip()
                        fromyr = 0
                        toyr = 0
                        exp_name = ''
                        desig = ''
                        city = ''
                        doc_id = doctor_id
                        i = len(temp)
                        if temp[0].isdigit() and temp[3].isdigit():
                            if temp.lower().find('-') != -1:
                                if temp.lower().find('present') != -1:
                                    j = temp.lower().index('-')
                                    temp2 = str(temp[0:j]).strip()
                                    k = temp.lower().index('present')
                                    temp3 = str(temp[k + 7:i]).strip()
                                    fromyr = int(temp2)
                                    toyr = datetime.datetime.now().year
                                    other_stng = temp3
                                else:
                                    j = temp.lower().index('-')
                                    temp2 = str(temp[0:j]).strip()
                                    temp3 = str(temp[j + 1:i]).strip()
                                    if temp3[0].isdigit():
                                        temp4 = str(temp3[0:4]).strip()
                                        temp5 = str(temp3[5:i]).strip()
                                        fromyr = int(temp2)
                                        toyr = int(temp4)
                                        other_stng = temp5
                                    else:
                                        toyr = int(temp2)
                                        other_stng = temp3
                            else:
                                temp2 = str(temp[0:4]).strip()
                                temp3 = str(temp[5:i]).strip()
                                toyr = int(temp2)
                                other_stng = temp3
                        else:
                            other_stng = temp
                        if other_stng.lower().find('at') != -1:
                            j = other_stng.lower().index('at')
                            temp2 = str(other_stng[0:j]).strip()
                            temp3 = str(other_stng[j + 2:i]).strip()
                            desig = temp2
                            other_stng = temp3
                        if other_stng.lower().find(',') != -1:
                            k = len(other_stng)
                            if other_stng[k - 1] != ',':
                                for l in reversed(other_stng):
                                    if l == ',':
                                        temp2 = str(other_stng[k + 1:len(other_stng)]).strip()
                                        temp3 = str(other_stng[0:k - 1]).strip()
                                        break
                                    else:
                                        k = k - 1
                                city = temp2
                                other_stng = temp3
                        if other_stng:
                            hosp = other_stng
                        if fromyr != 0 and toyr != 0:
                            new_live_doctor_exp = Live_Doctor_Experience(doctor_id=doc_id, name=hosp, designation=desig,
                                                                         city=city, fromYear=int(fromyr),
                                                                         toYear=int(toyr))
                            new_live_doctor_exp.save()
                        elif fromyr == 0 and toyr != 0:
                            new_live_doctor_exp = Live_Doctor_Experience(doctor_id=doc_id, name=hosp, designation=desig,
                                                                         city=city, toYear=int(toyr))
                            new_live_doctor_exp.save()
                        elif fromyr == 0 and toyr == 0:
                            new_live_doctor_exp = Live_Doctor_Experience(doctor_id=doc_id, name=hosp, designation=desig,
                                                                         city=city)
                            new_live_doctor_exp.save()
                        if hosp != None and hosp != '':
                            merge_exp_details.append({"Exp_Name":hosp})
                        if desig != None and desig != '':
                            merge_exp_details.append({"Exp_Designation":desig})
                        if city != None and city != '':
                            merge_exp_details.append({"Exp_City":city})
                        if fromyr != 0:
                            merge_exp_details.append({"Exp_From_Year":str(fromyr).strip()})
                        if toyr != 0:
                            merge_exp_details.append({"Exp_To_Year":str(toyr).strip()})
                        merge_exp.append(merge_exp_details)
                    merge_records.append({"EXPERIENCE":merge_exp})
                    count = 1
            if count == 1:
                live_merge_records.append(merge_records)
                live_doctor_obj.merge_fields = live_merge_records
            live_doctor_obj.save()
        else:
            messages.success(request, "Data is incorrect")
            return HttpResponseRedirect(reverse('view_duplicates', args=[doctor_id]))

        messages.success(request, "Data has been merged successfully")
        return HttpResponseRedirect(reverse('view_duplicates', args=[doctor_id]))
    except Exception as e:
        #print e
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - notify_doctorforarticle                                    #
# BY - Ashutosh kesharvani                                          #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def notify_doctorforarticle(request):
    try:
        id = request.POST.get('id')
        typ = request.POST.get('type')
        if typ == 'caller':
            print 1
    except Exception as e:
        #print e
        pass
####################################################################
# Name - live_organisation_data_manage                             #
# Owner - Visnu Badal                                              #
# Review by - ?                                                    #
#                                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def live_organisation_data_manage(request):
    try:
        return render(request, 'admin/admin_live_organisation/live_organisation_management.html',
                      {'tab': 'data', 'crosal': 'organisationmanage'})
    except:
        raise Http404




####################################################################
# Name - live_organisation_listing                                 #
# Owner - Ashutosh Kesharvani                                      #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def live_organisation_listing(request):
    try:
        if request.method == "GET":
            state_filter = False
            city_filter = False
            locality_filter = False
            state_data_obj = State.objects.all().order_by('name')
            user_data = User.objects.all()
            usmo = UserManagement.objects.get(user_id = request.user)
            usmo = UserManagement.objects.get(user_id = request.user.id)

            try:
                filter_name = str(request.GET['x'].strip())
            except:
                filter_name = None
            if filter_name == 'live_organisation_filter':
                state_data = request.GET['state_id'].strip()
                if state_data:
                    state_filter = int(state_data)
                city_data = request.GET['city_id'].strip()
                if city_data and state_filter:
                    city_filter = int(city_data)
                    city_obj = City.objects.filter(state_id=state_filter).order_by('name')
                else:
                    city_obj = []
                locality_data = request.GET['locality_id'].strip()
                if locality_data:
                    locality_filter = int(locality_data)

                try:
                    status_data = request.GET['status_data'].strip()
                    if status_data == '':
                        status_data = None
                except:
                    status_data = None

                if state_data:
                    if city_data and locality_data:
                        if status_data:
                            if status_data == 'active':
                                organisation_data_obj = OrganisationName.objects.filter(Q(is_live_org=True),
                                                                                        Q(state=state_data),
                                                                                        Q(city=city_data),
                                                                                        Q(locality=locality_data),
                                                                                        Q(current_user_id=request.user.id),Q(is_disable=False)).order_by('name')
                            if status_data == 'inactive':
                                organisation_data_obj = OrganisationName.objects.filter(Q(is_live_org=True),
                                                                                        Q(state=state_data),
                                                                                        Q(city=city_data),
                                                                                        Q(locality=locality_data),
                                                                                        Q(current_user_id=request.user.id),
                                                                                        Q(is_disable=True)).order_by('name')
                        else:
                            organisation_data_obj = OrganisationName.objects.filter(Q(is_live_org=True),
                                                                                    Q(state=state_data),
                                                                                    Q(city=city_data),
                                                                                    Q(locality=locality_data),
                                                                                    Q(current_user_id=request.user.id),
                                                                                    Q(is_disable=False)).order_by('name')

                        locality_obj = Locality.objects.filter(city_id=city_filter).order_by('name')
                        paginator = Paginator(organisation_data_obj, 100)
                        page = request.GET.get('page')
                        try:
                            organisation_data_obj = paginator.page(page)
                        except PageNotAnInteger:
                            # If page is not an integer, deliver first page.
                            organisation_data_obj = paginator.page(1)
                        except EmptyPage:
                            # If page is out of range (e.g. 9999), deliver last page of results.
                            organisation_data_obj = paginator.page(paginator.num_pages)
                        return render(request, 'data_management/live_organisation_data/live_organisation_listing.html',
                                      {'tab_listing': 'organisation_listing',
                                       'organisation_data_obj': organisation_data_obj, 'state_data_obj': state_data_obj,
                                       'state_filter': state_filter, 'locality_filter': locality_filter,
                                       'city_filter': city_filter, 'city_obj': city_obj, 'locality_obj': locality_obj,
                                       'user_data': user_data,'status_data':status_data})
                    elif city_data:
                        if status_data:
                            if status_data == 'active':
                                organisation_data_obj = OrganisationName.objects.filter(Q(is_live_org=True),Q(state=state_data),Q(is_disable=False),
                                                                                        Q(city=city_data), Q(current_user_id=request.user.id)).order_by('name')
                            if status_data == 'inactive':
                                organisation_data_obj = OrganisationName.objects.filter(Q(is_live_org=True),Q(state=state_data),Q(is_disable=True),
                                                                                        Q(city=city_data), Q(current_user_id=request.user.id)).order_by('name')

                        else:
                            organisation_data_obj = OrganisationName.objects.filter(Q(is_live_org=True),Q(state=state_data),Q(is_disable=False),
                                                                                Q(city=city_data),Q(current_user_id=request.user.id)).order_by('name')
                    else:
                        if status_data:
                            if status_data == 'active':
                                organisation_data_obj = OrganisationName.objects.filter(Q(is_live_org=True),Q(state=state_data),Q(is_disable=False),
                                                                                Q(current_user_id=request.user.id)).order_by('name')
                            if status_data == 'inactive':
                                organisation_data_obj = OrganisationName.objects.filter(Q(is_live_org=True),Q(state=state_data),Q(is_disable=True),
                                                                                        Q(current_user_id=request.user.id)).order_by('name')
                        else:
                            organisation_data_obj = OrganisationName.objects.filter(Q(is_live_org=True),Q(is_disable=False),Q(state=state_data),Q(current_user_id=request.user.id)).order_by('name')

                    paginator = Paginator(organisation_data_obj, 100)
                    page = request.GET.get('page')
                    try:
                        organisation_data_obj = paginator.page(page)
                    except PageNotAnInteger:
                        # If page is not an integer, deliver first page.
                        organisation_data_obj = paginator.page(1)
                    except EmptyPage:
                        # If page is out of range (e.g. 9999), deliver last page of results.
                        organisation_data_obj = paginator.page(paginator.num_pages)

                    return render(request, 'data_management/live_organisation_data/live_organisation_listing.html',
                                  {'tab_listing': 'organisation_listing',
                                   'organisation_data_obj': organisation_data_obj, 'state_data_obj': state_data_obj,
                                   'state_filter': state_filter, 'locality_filter': locality_filter,
                                   'city_filter': city_filter, 'city_obj': city_obj, 'user_data': user_data,'status_data':status_data})

                elif status_data and not state_data:
                    if status_data == 'active':
                        organisation_data_obj = OrganisationName.objects.filter(Q(is_live_org=True),Q(current_user_id=request.user.id),Q(is_disable=False)).order_by('name')
                    if status_data == 'inactive':
                            organisation_data_obj = OrganisationName.objects.filter(Q(is_live_org=True),Q(current_user_id=request.user.id), Q(is_disable=True)).order_by('name')

                else:
                    organisation_data_obj = OrganisationName.objects.filter(Q(current_user_id=request.user.id),
                                                                            Q(is_disable=False),
                                                                            Q(is_live_org=True)).order_by('name')

            else:

                status_data = None
                organisation_data_obj = OrganisationName.objects.filter(Q(current_user_id=request.user.id),Q(is_disable=False),Q(is_live_org=True)).order_by('name')

            paginator = Paginator(organisation_data_obj, 100)
            page = request.GET.get('page')
            try:
                organisation_data_obj = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                organisation_data_obj = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                organisation_data_obj = paginator.page(paginator.num_pages)
            return render(request, 'data_management/live_organisation_data/live_organisation_listing.html',
                          {'tab_listing': 'organisation_listing',
                           'organisation_data_obj': organisation_data_obj, 'state_data_obj': state_data_obj,
                           'state_filter': state_filter, 'city_filter': city_filter, 'user_data': user_data,'status_data':status_data})
    except Exception as e:
        raise Http404

####################################################################
# Name - live_organisation_data_by_users                           #
# Owner - Ashutosh kesaharvani                                     #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def live_organisation_data_by_users(request):
    try:
        search_data=None
        search_data = request.GET.get('search_data')
        if search_data :
            user_data_obj = UserManagement.objects.all()
            organisation_all_data = OrganisationName.objects.filter(Q(current_user_id=search_data),Q(is_live_org=True)).order_by('name')
            paginator = Paginator(organisation_all_data, 100)
            page = request.GET.get('page')
            try:
                organisation_all_data = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                organisation_all_data = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                organisation_all_data = paginator.page(paginator.num_pages)
            return render(request, 'admin/admin_live_organisation/live_organisation_by_user.html',
                      {'tab': 'data', 'crosal': 'organisationbymanage', 'organisation_all_data': organisation_all_data,
                       'user_data_obj': user_data_obj,'search_data':search_data})

        search_data_two = None
        search_data_two = request.GET.get('search_data_two')
        if search_data_two:
            user_data_obj = UserManagement.objects.all()
            organisation_all_data = OrganisationName.objects.filter(Q(name__icontains=search_data_two),Q(is_live_org=True)).order_by('name')
            paginator = Paginator(organisation_all_data, 100)
            page = request.GET.get('page')
            try:
                organisation_all_data = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                organisation_all_data = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                organisation_all_data = paginator.page(paginator.num_pages)
            return render(request, 'admin/admin_live_organisation/live_organisation_by_user.html',
                          {'tab': 'data', 'crosal': 'organisationbymanage',
                           'organisation_all_data': organisation_all_data,
                           'user_data_obj': user_data_obj, 'search_data_two': search_data_two})




        user_data_obj = UserManagement.objects.all()
        organisation_all_data = OrganisationName.objects.filter(is_live_org=True).order_by('name')
        #print organisation_all_data
        paginator = Paginator(organisation_all_data, 100)
        page = request.GET.get('page')
        try:
            organisation_all_data = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            organisation_all_data = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            organisation_all_data = paginator.page(paginator.num_pages)

        return render(request, 'admin/admin_live_organisation/live_organisation_by_user.html',
                      {'tab': 'data', 'crosal': 'organisationbymanage', 'organisation_all_data': organisation_all_data,
                       'user_data_obj': user_data_obj})
    except Exception as e:
        raise Http404

####################################################################
# Name - live_organisation_data_by_stages                          #
# Owner - Ashutsoh Kesharvani                                      #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def live_organisation_data_by_stages(request):
    try:
        stage_id = request.GET.get('stage_id')
        if stage_id:
            organisation_all_data = OrganisationName.objects.filter(Q(stage_id=stage_id),Q(is_live_org=True)).order_by('name')
        else:
            organisation_all_data = OrganisationName.objects.filter(is_live_org=True).order_by('name')
            stage_id=None
        stage_data = Stage.objects.all()[:5]

        paginator = Paginator(organisation_all_data, 100)
        page = request.GET.get('page')
        try:
            organisation_all_data = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            organisation_all_data = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            organisation_all_data = paginator.page(paginator.num_pages)
        return render(request, 'admin/admin_live_organisation/live_organisation_by_stages.html',
                      {'tab': 'data', 'crosal': 'organisationbymanage', 'organisation_all_data': organisation_all_data,
                       'stage_data': stage_data,'stage_no':stage_id})
    except Exception as e:
        #print e
        raise Http404


####################################################################
# Name - Live_organisation_assignment                                   #
# Owner - Ashutosh Kesharvani                                      #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
@csrf_exempt
def live_organisation_assignment(request):
    try:
        stage_filter = False
        user_filter = False
        state_filter = False
        city_filter = False
        locality_filter = False
        stage_data = Stage.objects.all()[:4]
        state_data_obj = State.objects.all().order_by('name')
        user_data = User.objects.all().order_by('username')



        search_data=None
        search_data = request.GET.get('search_data')
        if search_data :
            organisation_data_obj = OrganisationName.objects.filter(Q(name__icontains=search_data),Q(is_live_org=True)).order_by('name')

            #disabled on 25 APR 2017 TO DISPLAY ALL RECORDS SINCE NEW Pune records arte to come
            paginator = Paginator(organisation_data_obj, 100)
            page = request.GET.get('page')
            try:
                organisation_data_obj = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                organisation_data_obj = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                organisation_data_obj = paginator.page(paginator.num_pages)
            return render(request, 'admin/admin_live_organisation/live_organisation_assign.html',
                          {'tab': 'data', 'crosal': 'organisationbymanage', 'stage_data': stage_data,
                           'organisation_data_obj': organisation_data_obj, 'state_data_obj': state_data_obj,
                           'user_data': user_data, 'user_filter': user_filter,'search_data':search_data})

        try:
            filter_name = str(request.GET['x'].strip())
        except:
            filter_name = None
        if filter_name == 'live_organisation_filter':

            try:
                stage_id_data = request.GET['stage_da'].strip()
            except:
                stage_id_data = None
            try:
                user_id_data = request.GET['user_da'].strip()
            except:
                user_id_data = None
            if stage_id_data:
                stage_filter = int(stage_id_data)
            if user_id_data:
                user_filter = int(user_id_data)
            state_data = request.GET['state_id'].strip()
            if state_data:
                state_filter = int(state_data)
            city_data = request.GET['city_id'].strip()
            if city_data:
                city_filter = int(city_data)
                city_obj = City.objects.filter(state_id=state_filter).order_by('name')
            else:
                city_obj = []
            locality_data = request.GET['locality_id'].strip()
            if locality_data:
                locality_filter = int(locality_data)
            if state_data:

                if city_data and locality_data:
                    locality_obj = Locality.objects.filter(city_id=city_filter).order_by('name')

                    if stage_id_data and user_id_data:
                        organisation_data_obj = OrganisationName.objects.filter(Q(state=state_data),
                                                                                Q(city=city_data),
                                                                                Q(locality=locality_data),
                                                                                Q(stage=stage_id_data),
                                                                                Q(is_live_org=True),
                                                                                Q(current_user=user_id_data)).order_by(
                            'name')

                        # disabled on 25 APR 2017 TO DISPLAY ALL RECORDS SINCE NEW Pune records arte to come
                        paginator = Paginator(organisation_data_obj, 100)
                        page = request.GET.get('page')
                        try:
                            organisation_data_obj = paginator.page(page)
                        except PageNotAnInteger:
                            # If page is not an integer, deliver first page.
                            organisation_data_obj = paginator.page(1)
                        except EmptyPage:
                            # If page is out of range (e.g. 9999), deliver last page of results.
                            organisation_data_obj = paginator.page(paginator.num_pages)
                        return render(request, 'admin/admin_live_organisation/live_organisation_assign.html',
                                      {'tab': 'data', 'crosal': 'organisationbymanage', 'stage_data': stage_data,
                                       'organisation_data_obj': organisation_data_obj, 'state_data_obj': state_data_obj,
                                       'city_obj': city_obj, 'locality_obj': locality_obj,
                                       'locality_filter': locality_filter, 'city_filter': city_filter,
                                       'state_filter': state_filter, 'user_data': user_data, 'user_filter': user_filter,
                                       'stage_filter': stage_filter,
                                       'filter_name':filter_name,'state_data':state_data,'city_data':city_data,
                                       'user_id_data':user_id_data,'locality_data':locality_data,'stage_id_data':stage_id_data  })
                    elif stage_id_data:
                        organisation_data_obj = OrganisationName.objects.filter(Q(state=state_data),
                                                                                Q(city=city_data),
                                                                                Q(is_live_org=True),
                                                                                Q(locality=locality_data),
                                                                                Q(stage=stage_id_data)).order_by(
                            'name')
                    elif user_id_data:
                        organisation_data_obj = OrganisationName.objects.filter(Q(state=state_data),
                                                                                Q(city=city_data),
                                                                                Q(is_live_org=True),
                                                                                Q(locality=locality_data),
                                                                                Q(current_user=user_id_data)).order_by(
                            'name')

                    else:
                        organisation_data_obj = OrganisationName.objects.filter(Q(state=state_data),
                                                                                Q(city=city_data),
                                                                                Q(is_live_org=True),
                                                                                Q(locality=locality_data)).order_by(
                            'name')

                    # disabled on 25 APR 2017 TO DISPLAY ALL RECORDS SINCE NEW Pune records arte to come
                    paginator = Paginator(organisation_data_obj, 100)
                    page = request.GET.get('page')
                    try:
                        organisation_data_obj = paginator.page(page)
                    except PageNotAnInteger:
                        # If page is not an integer, deliver first page.
                        organisation_data_obj = paginator.page(1)
                    except EmptyPage:
                        # If page is out of range (e.g. 9999), deliver last page of results.
                        organisation_data_obj = paginator.page(paginator.num_pages)
                    return render(request, 'admin/admin_live_organisation/live_organisation_assign.html',
                                  {'tab': 'data', 'crosal': 'organisationbymanage', 'stage_data': stage_data,
                                   'organisation_data_obj': organisation_data_obj, 'state_data_obj': state_data_obj,
                                   'city_obj': city_obj, 'locality_obj': locality_obj,
                                   'locality_filter': locality_filter, 'city_filter': city_filter,
                                   'state_filter': state_filter, 'user_data': user_data, 'user_filter': user_filter,
                                   'stage_filter': stage_filter,
                                   'filter_name':filter_name,'state_data':state_data,'city_data':city_data,
                                    'user_id_data':user_id_data,'locality_data':locality_data,'stage_id_data':stage_id_data  })
                elif city_data:
                    if stage_id_data and user_id_data:
                        organisation_data_obj = OrganisationName.objects.filter(Q(state=state_data),
                                                                                Q(city=city_data),
                                                                                Q(is_live_org=True),
                                                                                Q(stage=stage_id_data),
                                                                                Q(current_user=user_id_data)).order_by(
                            'name')

                        # disabled on 25 APR 2017 TO DISPLAY ALL RECORDS SINCE NEW Pune records arte to come
                        paginator = Paginator(organisation_data_obj, 100)
                        page = request.GET.get('page')
                        try:
                            organisation_data_obj = paginator.page(page)
                        except PageNotAnInteger:
                            # If page is not an integer, deliver first page.
                            organisation_data_obj = paginator.page(1)
                        except EmptyPage:
                            # If page is out of range (e.g. 9999), deliver last page of results.
                            organisation_data_obj = paginator.page(paginator.num_pages)
                        return render(request, 'admin/admin_live_organisation/live_organisation_assign.html',
                                      {'tab': 'data', 'crosal': 'organisationbymanage', 'stage_data': stage_data,
                                       'organisation_data_obj': organisation_data_obj, 'state_data_obj': state_data_obj,
                                       'city_obj': city_obj,
                                       'locality_filter': locality_filter, 'city_filter': city_filter,
                                       'state_filter': state_filter, 'user_data': user_data, 'user_filter': user_filter,
                                       'stage_filter': stage_filter,
                                       'filter_name':filter_name,'state_data':state_data,'city_data':city_data,
                                       'user_id_data':user_id_data,'locality_data':locality_data,'stage_id_data':stage_id_data  })


                    elif stage_id_data:
                        organisation_data_obj = OrganisationName.objects.filter(Q(state=state_data),
                                                                                Q(city=city_data),
                                                                                Q(is_live_org=True),
                                                                                Q(stage=stage_id_data)).order_by(
                            'name')
                    elif user_id_data:
                        organisation_data_obj = OrganisationName.objects.filter(Q(state=state_data),
                                                                                Q(city=city_data),
                                                                                Q(is_live_org=True),
                                                                                Q(current_user=user_id_data)).order_by(
                            'name')
                    else:
                        organisation_data_obj = OrganisationName.objects.filter(state=state_data,
                                                                                is_live_org=True,
                                                                                city=city_data).order_by(
                            'name')
                else:
                    if stage_id_data and user_id_data:
                        organisation_data_obj = OrganisationName.objects.filter(Q(state=state_data),
                                                                                Q(stage=stage_id_data),
                                                                                Q(is_live_org=True),
                                                                                Q(current_user=user_id_data)).order_by(
                            'name')
                        # disabled on 25 APR 2017 TO DISPLAY ALL RECORDS SINCE NEW Pune records arte to come
                        paginator = Paginator(organisation_data_obj, 100)
                        page = request.GET.get('page')
                        try:
                            organisation_data_obj = paginator.page(page)
                        except PageNotAnInteger:
                            # If page is not an integer, deliver first page.
                            organisation_data_obj = paginator.page(1)
                        except EmptyPage:
                            # If page is out of range (e.g. 9999), deliver last page of results.
                            organisation_data_obj = paginator.page(paginator.num_pages)
                        return render(request, 'admin/admin_live_organisation/live_organisation_assign.html',
                                      {'tab': 'data', 'crosal': 'organisationbymanage', 'stage_data': stage_data,
                                       'organisation_data_obj': organisation_data_obj, 'state_data_obj': state_data_obj,
                                       'city_obj': city_obj,
                                       'locality_filter': locality_filter, 'city_filter': city_filter,
                                       'state_filter': state_filter, 'user_data': user_data, 'user_filter': user_filter,
                                       'stage_filter': stage_filter,
                                       'filter_name':filter_name,'state_data':state_data,'city_data':city_data,
                                       'user_id_data':user_id_data,'locality_data':locality_data,'stage_id_data':stage_id_data  })

                    elif stage_id_data:
                        organisation_data_obj = OrganisationName.objects.filter(Q(state=state_data),
                                                                                Q(is_live_org=True),
                                                                                Q(stage=stage_id_data)).order_by(
                            'name')
                    elif user_id_data:
                        organisation_data_obj = OrganisationName.objects.filter(Q(state=state_data),
                                                                                Q(is_live_org=True),
                                                                                Q(current_user=user_id_data)).order_by(
                            'name')
                    else:

                        organisation_data_obj = OrganisationName.objects.filter(state=state_data,is_live_org=True).order_by('name')
                    # disabled on 25 APR 2017 TO DISPLAY ALL RECORDS SINCE NEW Pune records arte to come
                    paginator = Paginator(organisation_data_obj, 100)
                    page = request.GET.get('page')
                    try:
                        organisation_data_obj = paginator.page(page)
                    except PageNotAnInteger:
                        # If page is not an integer, deliver first page.
                        organisation_data_obj = paginator.page(1)
                    except EmptyPage:
                        # If page is out of range (e.g. 9999), deliver last page of results.
                        organisation_data_obj = paginator.page(paginator.num_pages)

                    return render(request, 'admin/admin_live_organisation/live_organisation_assign.html',
                                  {'tab': 'data', 'crosal': 'organisationbymanage', 'stage_data': stage_data,
                                   'organisation_data_obj': organisation_data_obj, 'state_data_obj': state_data_obj,
                                   'state_filter': state_filter, 'locality_filter': locality_filter,
                                   'city_filter': city_filter, 'city_obj': city_obj, 'user_data': user_data,
                                   'user_filter': user_filter,
                                       'filter_name':filter_name,'state_data':state_data,'city_data':city_data,
                                       'user_id_data':user_id_data,'locality_data':locality_data,'stage_id_data':stage_id_data  })

            #No satte so no city etc
            elif stage_id_data and user_id_data:
                organisation_data_obj = OrganisationName.objects.filter(Q(stage=stage_id_data),
                                                                        Q(is_live_org=True),
                                                                        Q(current_user=user_id_data)).order_by('name')
                # disabled on 25 APR 2017 TO DISPLAY ALL RECORDS SINCE NEW Pune records arte to come
                paginator = Paginator(organisation_data_obj, 100)
                page = request.GET.get('page')
                try:
                    organisation_data_obj = paginator.page(page)
                except PageNotAnInteger:
                    # If page is not an integer, deliver first page.
                    organisation_data_obj = paginator.page(1)
                except EmptyPage:
                    # If page is out of range (e.g. 9999), deliver last page of results.
                    organisation_data_obj = paginator.page(paginator.num_pages)

                return render(request, 'admin/admin_live_organisation/live_organisation_assign.html',
                              {'tab': 'data', 'crosal': 'organisationbymanage', 'stage_data': stage_data,
                               'organisation_data_obj': organisation_data_obj, 'state_data_obj': state_data_obj,
                               'state_filter': state_filter, 'locality_filter': locality_filter,
                               'city_filter': city_filter, 'city_obj': city_obj, 'user_data': user_data,
                               'user_filter': user_filter, 'stage_filter': stage_filter,
                               'filter_name':filter_name,'state_data':state_data,'city_data':city_data,
                               'user_id_data':user_id_data,'locality_data':locality_data,'stage_id_data':stage_id_data  })



            #only stage
            elif stage_id_data:
                organisation_data_obj = OrganisationName.objects.filter(Q(stage=stage_id_data),Q(is_live_org=True)).order_by('name')

            #only user id
            elif user_id_data:
                organisation_data_obj = OrganisationName.objects.filter(Q(current_user=user_id_data),Q(is_live_org=True)).order_by('name')
            #No filter data received send all objects to template
            else:
                organisation_data_obj = OrganisationName.objects.filter(is_live_org=True).order_by('name')

            # disabled on 25 APR 2017 TO DISPLAY ALL RECORDS SINCE NEW Pune records arte to come
            paginator = Paginator(organisation_data_obj, 100)
            page = request.GET.get('page')
            try:
                organisation_data_obj = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                organisation_data_obj = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                organisation_data_obj = paginator.page(paginator.num_pages)
            return render(request, 'admin/admin_live_organisation/live_organisation_assign.html',
                          {'tab': 'data', 'crosal': 'organisationbymanage', 'stage_data': stage_data,
                           'organisation_data_obj': organisation_data_obj, 'state_data_obj': state_data_obj,
                           'user_data': user_data, 'user_filter': user_filter,
                           'filter_name':filter_name,'state_data':state_data,'city_data':city_data,
                           'user_id_data':user_id_data,'locality_data':locality_data,'stage_id_data':stage_id_data  })
        else:

            filter_name = None
            state_data = None
            city_data = None
            user_id_data = None
            locality_data =None
            stage_id_data =None


            # No filter send all objects
            # organisation_data_obj = OrganisationName.objects.all().order_by('name')
            organisation_data_obj = OrganisationName.objects.filter(is_live_org=True).order_by('name')

            # disabled on 25 APR 2017 TO DISPLAY ALL RECORDS SINCE NEW Pune records arte to come
            paginator = Paginator(organisation_data_obj, 100)
            page = request.GET.get('page')
            try:
                organisation_data_obj = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                organisation_data_obj = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                organisation_data_obj = paginator.page(paginator.num_pages)
            return render(request, 'admin/admin_live_organisation/live_organisation_assign.html',
                          {'tab': 'data', 'crosal': 'organisationbymanage', 'stage_data': stage_data,
                           'organisation_data_obj': organisation_data_obj, 'state_data_obj': state_data_obj,
                           'user_data': user_data, 'user_filter': user_filter,
                           'filter_name':filter_name,'state_data':state_data,'city_data':city_data,
                           'user_id_data':user_id_data,'locality_data':locality_data,'stage_id_data':stage_id_data  })
    except Exception as e:
        raise Http404


###################################################################
# Name - view duplicate organisation                              #
# BY - Ashutosh kesharvani                                        #
###################################################################
@login_required(login_url='/')
@csrf_exempt
def view_duplicates_organisation(request, organisation_id=None):
    try:
        org_match_list = []
        if organisation_id:
            org_obj = OrganisationName.objects.get(id= int(organisation_id))
            # if org_obj.merge_field !=[]:
            #     messages.error(request, "This organisation has been already been merged")
            #     return HttpResponseRedirect(reverse('live-organisation-by-users'))
            finali = org_obj.finalise
            #if live_doctor_obj.mciRegistrationNo != None and live_doctor_obj.mciRegistrationNo != '':
            org_list = OrganisationName.objects.all().exclude(id = int(organisation_id))
            if list(org_list) != []:
                for i in org_list:
                    if org_obj.name !='' and org_obj.name != None:
                        if i.name !='' and i.name != None:
                            if org_obj.name.strip() == i.name.strip():
                                if i not in org_match_list:
                                    org_match_list.append(i)

                    if org_obj.mobile_no != '' and org_obj.mobile_no != None:
                        if i.mobile_no != '' and i.mobile_no != None:
                            if org_obj.mobile_no.strip() == i.mobile_no.strip():
                                if i not in org_match_list:
                                    org_match_list.append(i)

                    if org_obj.phone != '' and org_obj.phone != None:
                        if i.phone != '' and i.phone != None:
                            if org_obj.phone.strip() == i.phone.strip():
                                if i not in org_match_list:
                                    org_match_list.append(i)

                    if org_obj.email != '' and org_obj.email != None:
                        if i.email != '' and i.email != None:
                            if org_obj.email.strip() == i.email.strip():
                                if i not in org_match_list:
                                    org_match_list.append(i)
                #print org_match_list
            else:
                pass
            return render(request,'data_management/live_organisation_data/live_organisation_duplicates.html',
                          {'org_match_list':org_match_list,'organisation_id':organisation_id,'org_obj':org_obj,'fin':finali}
                          )

        else:
            messages.error(request, "Organsiation ID Not Provided")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    except Exception as e:
        messages.error(request,e)
        HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - Merge Functionality for Clinic                            #
# BY - Dhrumil Shah                                                #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def merge_duplicate_organisation(request, old_clinic_id=None, new_clinic_id=None):
    try:
        if old_clinic_id and new_clinic_id:
            try:
                global hostname
                global port
                url_p3 = "/api/v2/clinic/merge_organisation/"
                global authToken
                old_clinic_id = int(old_clinic_id)
                new_clinic_id = int(new_clinic_id)

                urlc = hostname + port + url_p3
                import requests
                url = urlc
                obj = {'authToken':authToken, 'to_organisation_id':old_clinic_id, 'from_organisation_id':new_clinic_id}
                s = json.dumps(obj)
                try:
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
                    r = requests.post(url, s)
                    if r.status_code == 200 or r.status_code == '200':
                        messages.success(request, "Successfully Merged Organisation")
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                    else:
                        messages.error(request, "Organisation Not Merged")
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                except Exception as e:
                    messages.error(request, e)
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            except Exception as e:
                messages.error(request, e)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            messages.error(request, "Data is incorrect")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        #print e
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - organisation                                              #
# Owner - Visnu Badal                                              #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def assign_live_organisation(request):
    try:
        if request.method == "POST":
            response1 = {}
            try:
                assign_user = int(request.POST['telecaller'].strip())
            except:
                assign_user = 0
            try:
                change_stage = int(request.POST['stage'].strip())
            except:
                change_stage = 0
            checkedValues = request.POST.getlist('checkedValues[]')
            if assign_user and change_stage and checkedValues:
                if checkedValues[0] == 'on':
                    try:
                        checkedValues = checkedValues[1:]
                    except:
                        response1['Message'] = "Something Bad happened"
                nbslist = []
                nbflist = []
                for i in range(0, len(checkedValues)):
                    try:
                        assign_obj = OrganisationName.objects.filter(id=checkedValues[i],is_live_org=True).update(
                            current_user_id=assign_user,
                            stage_id=change_stage)
                        nbslist.append(checkedValues[i])
                    except:
                        nbflist.append(checkedValues[i])
                        continue
                # my_send_mail(request, 'organisation', nbslist, nbflist, 'Hospital Assignment', 'Assigned')
                response1['Redirect'] = True
                response1['RedirectUrl'] = '/live_organisation/assignment/users/'
                response1['Message'] = "Assign Complete"
            else:
                response1['Message'] = "Please select Stage and User "
            response = json.dumps(response1)
            return HttpResponse(response)
    except Exception as e:
        raise Http404

####################################################################
# Name - disable Live organisation_data                            #
# Owner - Ashutosh kesharvani                                      #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@require_GET
def disable_live_organisation_data(request, organisation_id=None):
    try:
        if organisation_id is not None:
            OrganisationName.objects.filter(id=organisation_id).update(is_disable=True)
            messages.success(request, 'Successfully Deactivated')
        else:
            messages.error(request, 'Try again')
    except Exception as e:
        messages.error(request, 'Something Bad Happened')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - activate_live_organisation                                  #
# Owner - Ashutosh kesharvani                                        #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@require_GET
def activate_live_organisation(request, organisation_id=None):
    try:
        if organisation_id is not None:
            OrganisationName.objects.filter(id=organisation_id).update(is_disable=False)
            messages.success(request, 'Successfully Activated')
        else:
            messages.error(request, 'Try again')
    except Exception as e:
        messages.error(request, 'Something Bad Happened')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



####################################################################
# Name - live_organisation_delete_schedule                         #
# Owner - Ashutosh kesharvani                                      #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def live_organisation_delete_schedule(request, organisation_id=None):
    try:
        if request.method == "GET" and organisation_id:
            id_data = request.GET['id']
            if id_data:
                schedule_data_obj = OrganisationName.objects.filter(schedule_data__contains=[{'id': id_data}])
                update_data = list(schedule_data_obj[0].schedule_data)
                # update_data = _.without(update_data, _.findWhere(update_data, {'id': id_data}))
                # schedule_data_obj.update(schedule_data=update_data)
                for i in update_data:
                    if i['id'] == id_data:
                        update_data.remove(i)
                schedule_data_obj.update(schedule_data=update_data)
                messages.success(request, 'Deleted')
            else:
                messages.error(request, 'Something Bad happened')
        else:
            messages.error(request, 'Something Bad happened')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        raise Http404

####################################################################
# Name - live_org_upload_image                                     #
# Owner - Ashutosh kesharvani                                      #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def live_org_upload_image(request, organisation_id=None):
    try:
        check_action = request.POST.get("check_action")
        if organisation_id and check_action != 'on':
            image_type = request.POST.get('ii')
            if image_type =='profileImage':
                try:
                    org_obj = OrganisationName.objects.get(id=int(organisation_id))
                    if len(request.FILES) == 1:
                        file = request.FILES['profile_image']
                        file_name = request.FILES['profile_image'].name

                        global hostname
                        global port
                        url_p3 = "/api/v2/clinic/add_profile_picture/"
                        global authToken
                        org_id = str(organisation_id) + '/'

                        urlc =hostname + port + url_p3 + authToken + '/' + org_id
                        import requests
                        url = urlc
                        #print settings.DOC_PROFILE
                        from django.core.files.storage import FileSystemStorage
                        filepath = settings.DOC_PROFILE + '/' + file_name
                        fs = FileSystemStorage()
                        # filename = fs.save(settings.DOC_REG, file)
                        filename = fs.save(filepath, file)
                        uploaded_file_url = fs.url(filename)
                        #print uploaded_file_url

                        try:
                            headers = {
                                'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
                            with open(filepath, "rb") as image_file:
                                # print ">>>>>>>>>   ", type(image_file), "   <<<<<<<<<<<<<<<<<"
                                files = {'uploadFile': image_file}

                                # cookie = {cookiename: token.value}
                                # r = requests.post(url,headers=headers ,files=files)
                                r = requests.post(url, files=files)
                                # print r.request.headers
                                # print r.status_code
                                # print r.text

                                if r.status_code == 200 or r.status_code == '200':
                                        messages.success(request, "Successfully Uploaded Profile Image")
                                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                                else:
                                    messages.success(request, "Profile Image Upload Failed")
                                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


                        except Exception as e:
                            messages.error(request, e)
                            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

                except Exception as e:
                    # print e
                    messages.error(request, e)
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            if image_type == 'logo':
                try:
                    org_obj = OrganisationName.objects.get(id=int(organisation_id))
                    if len(request.FILES) == 1:
                        file = request.FILES['logo']
                        file_name = request.FILES['logo'].name

                        global hostname
                        global port
                        url_p3 = "/api/v2/clinic/add_clinic_logo/"
                        global authToken
                        org_id = str(organisation_id) + '/'

                        urlc = hostname + port + url_p3 + authToken + '/' + org_id
                        import requests
                        url = urlc
                        #print settings.DOC_PROFILE
                        from django.core.files.storage import FileSystemStorage
                        filepath = settings.DOC_PROFILE + '/' + file_name
                        fs = FileSystemStorage()
                        # filename = fs.save(settings.DOC_REG, file)
                        filename = fs.save(filepath, file)
                        uploaded_file_url = fs.url(filename)
                        #print uploaded_file_url

                        try:
                            headers = {
                                'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
                            with open(filepath, "rb") as image_file:
                                # print ">>>>>>>>>   ", type(image_file), "   <<<<<<<<<<<<<<<<<"
                                files = {'uploadFile': image_file}

                                # cookie = {cookiename: token.value}
                                # r = requests.post(url,headers=headers ,files=files)
                                r = requests.post(url, files=files)
                                # print r.request.headers
                                # print r.status_code
                                # print r.text

                                if r.status_code == 200 or r.status_code == '200':
                                    messages.success(request, "Successfully Uploaded Profile Image")
                                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                                else:
                                    messages.success(request, "Profile Image Upload Failed")
                                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


                        except Exception as e:
                            messages.error(request, e)
                            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

                except Exception as e:
                    # print e
                    messages.error(request, e)
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            if image_type == 'stamp':
                try:
                    org_obj = OrganisationName.objects.get(id=int(organisation_id))
                    if len(request.FILES) == 1:
                        file = request.FILES['stamp']
                        file_name = request.FILES['stamp'].name

                        global hostname
                        global port
                        url_p3 = "/api/v2/clinic/add_clinic_stamp/"
                        global authToken
                        org_id = str(organisation_id) + '/'

                        urlc = hostname + port + url_p3 + authToken + '/' + org_id
                        import requests
                        url = urlc
                        #print settings.DOC_PROFILE
                        from django.core.files.storage import FileSystemStorage
                        filepath = settings.DOC_PROFILE + '/' + file_name
                        fs = FileSystemStorage()
                        # filename = fs.save(settings.DOC_REG, file)
                        filename = fs.save(filepath, file)
                        uploaded_file_url = fs.url(filename)
                        #print uploaded_file_url

                        try:
                            headers = {
                                'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
                            with open(filepath, "rb") as image_file:
                                # print ">>>>>>>>>   ", type(image_file), "   <<<<<<<<<<<<<<<<<"
                                files = {'uploadFile': image_file}

                                # cookie = {cookiename: token.value}
                                # r = requests.post(url,headers=headers ,files=files)
                                r = requests.post(url, files=files)
                                # print r.request.headers
                                # print r.status_code
                                # print r.text

                                if r.status_code == 200 or r.status_code == '200':
                                    messages.success(request, "Successfully Uploaded Profile Image")
                                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                                else:
                                    messages.success(request, "Profile Image Upload Failed")
                                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


                        except Exception as e:
                            messages.error(request, e)
                            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

                except Exception as e:
                    # print e
                    messages.error(request, e)
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            if image_type == 'registration':
                try:
                    org_obj = OrganisationName.objects.get(id=int(organisation_id))
                    if len(request.FILES) == 1:
                        file = request.FILES['registration']
                        file_name = request.FILES['registration'].name

                        global hostname
                        global port
                        url_p3 = "/api/v2/clinic/add_registration_image/"
                        global authToken
                        org_id = str(organisation_id) + '/'

                        urlc = hostname + port + url_p3 + authToken + '/' + org_id
                        import requests
                        url = urlc
                        #print settings.DOC_PROFILE
                        from django.core.files.storage import FileSystemStorage
                        filepath = settings.DOC_PROFILE + '/' + file_name
                        fs = FileSystemStorage()
                        # filename = fs.save(settings.DOC_REG, file)
                        filename = fs.save(filepath, file)
                        uploaded_file_url = fs.url(filename)
                        #print uploaded_file_url

                        try:
                            headers = {
                                'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
                            with open(filepath, "rb") as image_file:
                                # print ">>>>>>>>>   ", type(image_file), "   <<<<<<<<<<<<<<<<<"
                                files = {'uploadFile': image_file}

                                # cookie = {cookiename: token.value}
                                # r = requests.post(url,headers=headers ,files=files)
                                r = requests.post(url, files=files)
                                # print r.request.headers
                                # print r.status_code
                                # print r.text

                                if r.status_code == 200 or r.status_code == '200':
                                    messages.success(request, "Successfully Uploaded Profile Image")
                                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                                else:
                                    messages.success(request, "Profile Image Upload Failed")
                                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


                        except Exception as e:
                            messages.error(request, e)
                            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

                except Exception as e:
                    # print e
                    messages.error(request, e)
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            if image_type == 'gallery_image':
                try:
                    org_obj = OrganisationName.objects.get(id=int(organisation_id))
                    if len(request.FILES) == 1:
                        file = request.FILES['gallery_image']
                        file_name = request.FILES['gallery_image'].name

                        global hostname
                        global port
                        url_p3 = "/api/v2/clinic/add_gallery_image/"
                        global authToken
                        org_id = str(organisation_id) + '/'

                        urlc = hostname + port + url_p3 + authToken + '/' + org_id
                        import requests
                        url = urlc
                        #print settings.DOC_PROFILE
                        from django.core.files.storage import FileSystemStorage
                        filepath = settings.DOC_PROFILE + '/' + file_name
                        fs = FileSystemStorage()
                        # filename = fs.save(settings.DOC_REG, file)
                        filename = fs.save(filepath, file)
                        uploaded_file_url = fs.url(filename)
                        #print uploaded_file_url

                        try:
                            headers = {
                                'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
                            with open(filepath, "rb") as image_file:
                                # print ">>>>>>>>>   ", type(image_file), "   <<<<<<<<<<<<<<<<<"
                                files = {'uploadFile': image_file}

                                # cookie = {cookiename: token.value}
                                # r = requests.post(url,headers=headers ,files=files)
                                r = requests.post(url, files=files)
                                # print r.request.headers
                                # print r.status_code
                                # print r.text

                                if r.status_code == 200 or r.status_code == '200':
                                    messages.success(request, "Successfully Uploaded Profile Image")
                                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                                else:
                                    messages.success(request, "Profile Image Upload Failed")
                                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


                        except Exception as e:
                            messages.error(request, e)
                            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

                except Exception as e:
                    # print e
                    messages.error(request, e)
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                    check_action = request.POST.get("check_action")
        elif organisation_id and check_action == 'on':
            image_type = request.POST.get('ii')
            if image_type == 'profileImage':
                org_obj = OrganisationName.objects.get(id=int(organisation_id))
                if len(request.FILES) == 1:
                    file = request.FILES['profile_image']
                    file_name = request.FILES['profile_image'].name

                    global hostname
                    global port
                    url_p3 = "/api/v2/clinic/add_profile_picture/"
                    global authToken
                    org_id = str(organisation_id) + '/'

                    urlc = hostname + port + url_p3 + authToken + '/' + org_id
                    import requests
                    url = urlc
                    #print settings.DOC_PROFILE
                    from django.core.files.storage import FileSystemStorage
                    filepath = settings.DOC_PROFILE + '/' + file_name
                    fs = FileSystemStorage()
                    # filename = fs.save(settings.DOC_REG, file)
                    filename = fs.save(filepath, file)
                    uploaded_file_url = fs.url(filename)
                    #print uploaded_file_url

                    try:
                        headers = {
                            'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
                        with open(filepath, "rb") as image_file:
                            # print ">>>>>>>>>   ", type(image_file), "   <<<<<<<<<<<<<<<<<"
                            files = {'uploadFile': image_file}

                            # cookie = {cookiename: token.value}
                            # r = requests.post(url,headers=headers ,files=files)
                            r = requests.post(url, files=files)
                            # print r.request.headers
                            # print r.status_code
                            # print r.text

                            if r.status_code == 200 or r.status_code == '200':
                                messages.success(request, "Successfully Uploaded Profile Image")
                                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                            else:
                                messages.success(request, "Profile Image Upload Failed")
                                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                    except Exception as e:
                        messages.error(request, e)
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        # print e
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



####################################################################
# name live_organisation_publisher_listing                         #
# owner Ashutosh kesharvani                                        #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@require_GET
def live_organisation_publisher_listing(request):
    try:
        stage_data = Stage.objects.all()[3:5]
        #print stage_data
        state_data_obj = State.objects.all().order_by('name')
        try:
            filter_name = str(request.GET['x'].strip())
        except:
            filter_name = None
        if filter_name == 'organisation_filter':
            stage_filter = False
            user_filter = False
            state_filter = False
            city_filter = False
            locality_filter = False
            user_data= None
            try:
                stage_id_data = request.GET['stage_id'].strip()
            except:
                stage_id_data = None
            try:
                user_id_data = request.GET['user_da'].strip()
            except:
                user_id_data = None
            if stage_id_data:
                stage_filter = int(stage_id_data)
            if user_id_data:
                user_filter = int(user_id_data)
            state_data = request.GET['state_id'].strip()
            if state_data:
                state_filter = int(state_data)
            city_data = request.GET['city_id'].strip()
            if city_data:
                city_filter = int(city_data)
                city_obj = City.objects.filter(state_id=state_filter).order_by('name')
            else:
                city_obj = []
            locality_data = request.GET['locality_id'].strip()
            if locality_data:
                locality_filter = int(locality_data)
            if state_data:

                if city_data and locality_data:
                    locality_obj = Locality.objects.filter(city_id=city_filter).order_by('name')
                    if stage_id_data:
                        organisation_data_obj = OrganisationName.objects.filter(Q(is_live_org=True),
                                                                                Q(state=state_data),
                                                                                Q(city=city_data),
                                                                                Q(locality=locality_data),
                                                                                Q(stage=stage_id_data),
                                                                                Q(current_user_id=request.user.id),Q(is_disable=False)).order_by('name')
                    else:
                        organisation_data_obj = OrganisationName.objects.filter(Q(is_live_org=True),
                                                                                Q(state=state_data),
                                                                                Q(city=city_data),
                                                                                Q(locality=locality_data),
                                                                                Q(current_user_id=request.user.id),Q(is_disable=False)).order_by(
                            'name')

                    # disabled on 25 APR 2017 TO DISPLAY ALL RECORDS SINCE NEW Pune records arte to come
                    paginator = Paginator(organisation_data_obj, 100)
                    page = request.GET.get('page')
                    try:
                        organisation_data_obj = paginator.page(page)
                    except PageNotAnInteger:
                        # If page is not an integer, deliver first page.
                        organisation_data_obj = paginator.page(1)
                    except EmptyPage:
                        # If page is out of range (e.g. 9999), deliver last page of results.
                        organisation_data_obj = paginator.page(paginator.num_pages)
                    return render(request, 'publisher/live_organisation/live_organisation_listing_publisher.html',
                                  {'tab': 'data', 'crosal': 'organisationbymanage', 'stage_data': stage_data,
                                   'organisation': organisation_data_obj, 'state_data_obj': state_data_obj,
                                   'city_obj': city_obj, 'locality_obj': locality_obj,
                                   'locality_filter': locality_filter, 'city_filter': city_filter,
                                   'state_filter': state_filter, 'user_data': user_data, 'user_filter': user_filter,
                                   'stage_filter': stage_filter,
                                   'filter_name':filter_name,'state_data':state_data,'city_data':city_data,
                                    'user_id_data':user_id_data,'locality_data':locality_data,'stage_id_data':stage_id_data  })
                elif city_data:
                    if stage_id_data:
                        organisation_data_obj = OrganisationName.objects.filter(Q(is_live_org=True),
                                                                                Q(state=state_data),
                                                                                Q(city=city_data),
                                                                                Q(stage=stage_id_data),
                                                                                Q(current_user_id=request.user.id),Q(is_disable=False)).order_by(
                            'name')
                    else:
                        organisation_data_obj = OrganisationName.objects.filter(is_live_org=True,
                                                                                state=state_data,
                                                                                city=city_data,
                                                                                current_user_id=request.user.id,is_disable=False).order_by('name')

                    paginator = Paginator(organisation_data_obj, 100)
                    page = request.GET.get('page')
                    try:
                        organisation_data_obj = paginator.page(page)
                    except PageNotAnInteger:
                        # If page is not an integer, deliver first page.
                        organisation_data_obj = paginator.page(1)
                    except EmptyPage:
                        # If page is out of range (e.g. 9999), deliver last page of results.
                        organisation_data_obj = paginator.page(paginator.num_pages)

                    return render(request, 'publisher/live_organisation/live_organisation_listing_publisher.html',
                                  {'tab': 'data', 'crosal': 'organisationbymanage', 'stage_data': stage_data,
                                   'organisation': organisation_data_obj, 'state_data_obj': state_data_obj,
                                   'state_filter': state_filter, 'locality_filter': locality_filter,
                                   'city_filter': city_filter, 'city_obj': city_obj, 'user_data': user_data,
                                   'user_filter': user_filter,
                                   'filter_name': filter_name, 'state_data': state_data, 'city_data': city_data,
                                   'user_id_data': user_id_data, 'locality_data': locality_data,
                                   'stage_id_data': stage_id_data})
                else:
                    if stage_id_data:
                        organisation_data_obj = OrganisationName.objects.filter(Q(is_live_org=True),
                                                                                Q(state=state_data),
                                                                                Q(stage=stage_id_data,
                                                                                  current_user_id=request.user.id),Q(is_disable=False)).order_by(
                            'name')
                    else:

                        organisation_data_obj = OrganisationName.objects.filter(is_live_org=True,state=state_data,current_user_id=request.user.id,is_disable=False).order_by('name')
                    # disabled on 25 APR 2017 TO DISPLAY ALL RECORDS SINCE NEW Pune records arte to come
                    paginator = Paginator(organisation_data_obj, 100)
                    page = request.GET.get('page')
                    try:
                        organisation_data_obj = paginator.page(page)
                    except PageNotAnInteger:
                        # If page is not an integer, deliver first page.
                        organisation_data_obj = paginator.page(1)
                    except EmptyPage:
                        # If page is out of range (e.g. 9999), deliver last page of results.
                        organisation_data_obj = paginator.page(paginator.num_pages)

                    return render(request, 'publisher/live_organisation/live_organisation_listing_publisher.html',
                                  {'tab': 'data', 'crosal': 'organisationbymanage', 'stage_data': stage_data,
                                   'organisation': organisation_data_obj, 'state_data_obj': state_data_obj,
                                   'state_filter': state_filter, 'locality_filter': locality_filter,
                                   'city_filter': city_filter, 'city_obj': city_obj, 'user_data': user_data,
                                   'user_filter': user_filter,
                                       'filter_name':filter_name,'state_data':state_data,'city_data':city_data,
                                       'user_id_data':user_id_data,'locality_data':locality_data,'stage_id_data':stage_id_data  })
            #only stage
            if stage_id_data:
                organisation_data_obj = OrganisationName.objects.filter(Q(is_live_org=True),Q(stage=stage_id_data,current_user_id=request.user.id,is_disable=False)).order_by('name')
            else:
                organisation_data_obj = OrganisationName.objects.filter(is_live_org=True,current_user_id=request.user.id,is_disable=False).order_by('name')

            # disabled on 25 APR 2017 TO DISPLAY ALL RECORDS SINCE NEW Pune records arte to come
            paginator = Paginator(organisation_data_obj, 100)
            page = request.GET.get('page')
            try:
                organisation_data_obj = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                organisation_data_obj = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                organisation_data_obj = paginator.page(paginator.num_pages)
            return render(request, 'publisher/live_organisation/live_organisation_listing_publisher.html',
                          {'tab': 'data', 'crosal': 'organisationbymanage', 'stage_data': stage_data,
                           'organisation': organisation_data_obj, 'state_data_obj': state_data_obj,
                           'user_data': user_data, 'user_filter': user_filter,
                           'filter_name':filter_name,'state_data':state_data,'city_data':city_data,
                           'user_id_data':user_id_data,'locality_data':locality_data,'stage_id_data':stage_id_data  })

        try:
            search_name = request.GET['search_name']
        except:
            search_name = None
        try:
            stage_id = request.GET['stage_id']
        except:
            stage_id = None
        assign_id = UserManagement.objects.get(user_id=request.user.id)
        category_data = Category.objects.all().order_by('name')
        category_filter = False
        try:
            category_id = request.GET['category']
        except:
            category_id = None
        if assign_id.is_publisher is True:
            publisher_id = request.user.id
        else:
            publisher_id = 0
        if stage_id and publisher_id:
            organisation_obj = OrganisationName.objects.filter(is_live_org=True,stage_id=int(stage_id), current_user_id=request.user.id,is_disable=False).order_by('name')
        elif search_name and publisher_id:
            organisation_obj = OrganisationName.objects.filter(is_live_org=True,name__icontains=search_name, current_user_id=request.user.id,is_disable=False).order_by('name')
        elif publisher_id != None and stage_id == None and search_name == None :
            if category_id:
                organisation_obj = OrganisationName.objects.filter(Q(is_live_org=True),
                                                                   Q(category_id=category_id),
                                                                   Q(current_user_id=request.user.id),Q(is_disable=False)).order_by('name')
                category_filter = int(category_id)
            else:
                organisation_obj = OrganisationName.objects.filter(Q(is_live_org=True),
                                                                   Q(current_user_id=request.user.id),Q(is_disable=False)).order_by('name')
                #print len(organisation_obj)
        if len(organisation_obj) == 0:
            messages.error(request, "No organization found")
            return render(request, 'publisher/live_organisation/live_organisation_listing_publisher.html',
                          {'tab_listing': 'organisation-listing', 'tab': 'publish_organisation_data',
                           'stage_data': stage_data,
                           'category_obj': category_data, 'category_filter': category_filter,'stage_id':stage_id,
                           'search_name':search_name})
        else:
            paginator = Paginator(organisation_obj, 100)
            page = request.GET.get('page')
            try:
                organisation_obj = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                organisation_obj = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                organisation_obj = paginator.page(paginator.num_pages)
            return render(request, 'publisher/live_organisation/live_organisation_listing_publisher.html',
                          dict(organisation=organisation_obj, tab_listing='organisation-listing',
                               tab='publish_organisation_data',
                               stage_data=stage_data,state_data_obj=state_data_obj,
                               category_obj=category_data, category_filter=category_filter,stage_id=stage_id,
                               search_name=search_name,stage_id_data=None))
        # else:
        #     return HttpResponseRedirect(reverse('users-logout'))
    except Exception as e:
        raise Http404


####################################################################
# name live_organisation_publisher_listing                         #
# owner Ashutosh kesharvani                                        #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def finalise_live_organisatioin(request, organisation_id=None):
    try:
        org_obj = OrganisationName.objects.get(id=organisation_id)
        global host
        global port
        global authToken
        s = True
        obj = {'organisation_id': int(organisation_id), 'activation': s, 'user_id': org_obj.user_id,
               'authToken': authToken}
        oo = json.dumps(obj)
        url_p3 = "/api/v2/clinic/activate_deactivate_clinic/"
        urlc = hostname + port + url_p3
        import requests
        url = urlc
        try:
            r = requests.post(url, oo)

            if (r.status_code == 200 or r.status_code == '200'):
                tempresp = json.dumps(r.text)
                resp = json.loads(r.text)
                if resp['statusCode'] == 200 or resp['statusCode'] == '200':
                    org_obj.finalise = True
                    org_obj.activation = True
                    org_obj.save()
                    messages.success(request, "Operation successfull...!!!")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                else:
                    messages.error(request, resp['statusMessage'])
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                messages.error(request, "Something bad happend...!!!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        except Exception as e:
            messages.error(request, "Exception")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


####################################################################
# name associate disassociate live organisation                    #
# owner Ashutosh kesharvani                                        #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def associate_disassociate_live_organisation(request, organisation_id=None,doctor_id=None):
    try:
        org_id =organisation_id
        disassocaitedoctor = request.POST.get('disassocaitedoctor')
        removedoctor = request.POST.get('removedoctor')
        try:
            flag = request.GET['flag']
        except:
            flag = None
        #print flag

        schedule_obj = Live_Doctor_Commonworkschedule.objects.get(clinic_id=organisation_id,doctor_id=doctor_id)
        # associated_by_clinic = Live_Doctor_Commonworkschedule.objects.get(clinic_id=organisation_id,associated_by='clinic')

        if flag == '1':
            ''' flag == 1 is for association only '''
            schedule_obj.associated_by = 'clinic'
            schedule_obj.associateWithClinic = True
            schedule_obj.save()
            messages.success(request, 'Doctor has been associated Successfully ')

        else:
            schedule_obj.associated_by = ''
            schedule_obj.associateWithClinic = False
            schedule_obj.save()
            messages.success(request, 'Doctor has been disassociated Successfully ')
        return HttpResponseRedirect('/live_organisation/edit/' + str(org_id) + '/?tab=3')
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        messages.error(request,e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


####################################################################
# Name - create user Account for live organisatio                  #
# BY - Ashutosh                                                    #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def create_user_account_for_live_organisation(request, organisation_id=None):
    try:
        if organisation_id:
            try:

                organisation_obj = OrganisationName.objects.get(id=int(organisation_id))
                if organisation_obj:
                    #print request
                    inputJSON = {}
                    email = organisation_obj.email
                    #gender = request.POST['gender']
                    password = request.POST['setp']
                    cPassword = request.POST['confpa']
                    currPassword = request.POST['curr']
                    # mobileNo = organisation_obj.mobile_no
                    # firstName = request.POST['firstName']
                    # lastName = request.POST['lastName']
                    global authToken
                    global host
                    global port
                    inputJSON.update({'organisation_id': int(organisation_id)})
                    inputJSON.update({'userType': "clinic"})
                    inputJSON.update({'emailOrMob': email.strip()})
                    #inputJSON.update({'gender': gender.strip()})
                    inputJSON.update({'password': currPassword.strip()})
                    inputJSON.update({'newPassword': password.strip()})
                    inputJSON.update({'cPassword': cPassword.strip()})
                    # inputJSON.update({'mobileNo': mobileNo.strip()})
                    #inputJSON.update({'firstName': firstName.strip()})
                    #inputJSON.update({'lastName': lastName.strip()})
                    inputJSON.update({'terms_condition': True})
                    inputJSON.update({'authToken': authToken})
                    temp = json.dumps(inputJSON)
                    inputJSON = json.loads(temp)
                    global hostname
                    global port
                    url_p3 = "/api/v2/user/reset_password/"
                    urlc = hostname + port + url_p3
                    #print urlc
                    import requests
                    url = urlc

                    try:
                        r = requests.post(url, json=inputJSON)
                        tempresp = json.dumps(r.text)
                        #print r.text
                        #print type(r.text)
                        resp = json.loads(r.text)
                        #print type(resp)
                        #print resp
                        if (r.status_code == 200 or r.status_code == '200'):
                            if resp['statusCode'] == 200 or resp['statusCode'] == '200':
                                messages.success(request, "Password changed successfully...!!!")
                                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                            else:
                                messages.error(request, resp['statusMessage'])
                                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                        else:
                            messages.error(request, "Something bad happend...!!!")
                            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

                    except Exception as e:
                        messages.error(request, "Exception")
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            except Exception as e:
                #print e
                messages.error(request, e)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, "Doctor ID Not Provided")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    except Exception as e:
        raise Http404

####################################################################
# name live organisation disable enable branches                   #
# owner Ashutosh kesharvani                                        #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def live_org_disable_enable_branches(request, organisation_id=None):
    try:
        org_obj = OrganisationName.objects.get(id = organisation_id)
        global host
        global posrt
        global authToken
        ff= ''
        f = request.GET['f']
        if f == '1':
            s = True
        elif f == '0':
            s = False
        obj ={'organisation_id':int(organisation_id),'activation':s,'user_id':org_obj.user_id,'authToken':authToken}
        oo = json.dumps(obj)
        url_p3 = "/api/v2/clinic/activate_deactivate_clinic/"
        urlc = hostname + port + url_p3
        import requests
        url = urlc
        try:
            r = requests.post(url, oo)

            if (r.status_code == 200 or r.status_code == '200'):
                tempresp = json.dumps(r.text)
                resp = json.loads(r.text)
                if resp['statusCode'] == 200 or resp['statusCode'] == '200':
                    messages.success(request, "Operation successfull...!!!")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                else:
                    messages.error(request, resp['statusMessage'])
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                messages.error(request, "Something bad happend...!!!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        except Exception as e:
            messages.error(request, "Exception")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        messages.error(request,e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# name live organisation disable enable branches                   #
# owner Ashutosh kesharvani                                        #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def live_doc_notification(request):
    try:
        tab = 1
        live_doc_notifications = Live_Doctor_Notification.objects.all().order_by('-notification_creation_date')
        paginator = Paginator(live_doc_notifications, 100)
        page = request.GET.get('page')
        try:
            live_doc_notifications = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            live_doc_notifications = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            live_doc_notifications = paginator.page(paginator.num_pages)
        return render(request, 'admin/live_doctor_management/live_doctor_notification_tab.html',{'tab':tab,
                                                                  'live_doc_notifications':live_doc_notifications,'back_button':'no'})
    except Exception as e:
        messages.error(request,e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


####################################################################
# name live_doc_schedule_delete_notification                       #
# owner Nishank                                                    #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def live_doc_schedule_delete_notification(request):
    try:
        tab = 1
        live_doc_schedule_notifications = Live_Doctor_Schedule_Delete_Notification.objects.all().order_by('-notification_creation_date')
        paginator = Paginator(live_doc_schedule_notifications, 100)
        page = request.GET.get('page')
        try:
            live_doc_schedule_notifications = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            live_doc_schedule_notifications = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            live_doc_schedule_notifications = paginator.page(paginator.num_pages)
        return render(request, 'admin/live_doctor_management/live_doc_schedule_delete_notification.html',{'tab':tab,
                                                                  'live_doc_schedule_notifications':live_doc_schedule_notifications,'back_button':'no'})
    except Exception as e:
        messages.error(request,e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# name live_doc_schedule_stopdate_notification                     #
# owner Nishank                                                    #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def live_doc_schedule_stopdate_notification(request):
    try:
        tab = 1
        live_doc_schedule_notifications = Live_Doctor_Schedule_Stopdate_Notification.objects.all().order_by(
            '-notification_creation_date')
        paginator = Paginator(live_doc_schedule_notifications, 100)
        page = request.GET.get('page')
        try:
            live_doc_schedule_notifications = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            live_doc_schedule_notifications = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            live_doc_schedule_notifications = paginator.page(paginator.num_pages)
        return render(request, 'admin/live_doctor_management/live_doc_schedule_stopdate_notification.html',
                      {'tab': tab,
                       'live_doc_schedule_notifications': live_doc_schedule_notifications, 'back_button': 'no'})
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



####################################################################
# name live organisation delete reward recognisation               #
# owner Ashutosh kesharvani                                        #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def live_org_delete_rewrecog(request, rewrecog_id=None):
    try:
        try:
            org_obj = organisation_Rewardrecog.objects.get(id=rewrecog_id).delete()
            messages.success(request,"Data has been deleted successfully")
        except Exception as e:
            messages.error(request, "Exception")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        messages.error(request,e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


####################################################################
# name live_doctor_notification_bydate                             #
# owner Ashutosh kesharvani                                        #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def live_doctor_notification_bydate(request):
    try:

        tab = 1
        if request.method == 'POST':
            try:
                fd = request.POST.get('from_date').split('/')
                if fd == ['']:
                    fd = None
            except:
                fd = None
            try:
                td = request.POST.get('to_date').split('/')
                if td == ['']:
                    td = None
            except:
                td = None
            try:
                doc_name = request.POST.get('doc_name')
                if doc_name == None:
                    doc_name = ''
            except:
                doc_name = ''
        else:
            try:
                fd = request.GET.get('from_date').split('/')
                if fd == ['']:
                    fd = None
            except:
                fd = None
            try:
                td = request.GET.get('to_date').split('/')
                if td == ['']:
                    td = None
            except:
                td = None
            try:
                doc_name = request.POST.get('doc_name')
                if doc_name == None:
                    doc_name = ''
            except:
                doc_name = ''


        if fd == None and td != None:
            fd = td
        elif td == None and fd != None:
            td = fd
        elif td == None and fd == None:
            td = ['1800','1','1']
            fd = ['1800', '1', '1']

        fd = [int(item) for item in fd]
        td = [int(item) for item in td]

        if (fd != [1800,1,1] or td != [1800,1,1]) and doc_name == '':
            if datetime.date(fd[0],fd[1],fd[2]) > datetime.date(td[0],td[1],td[2]) :
                messages.error(request, 'FromDate Date should be smaller than  ToDate')
                return render(request, 'admin/live_doctor_management/live_doctor_notification_tab.html',{'tab': tab})
            elif datetime.date(fd[0],fd[1],fd[2]) == datetime.date(td[0],td[1],td[2]) :
                live_doc_notifications = Live_Doctor_Notification.objects.filter(notification_creation_date__date=datetime.date(fd[0],fd[1],fd[2])).order_by('-notification_creation_date')
            elif datetime.date(fd[0],fd[1],fd[2]) < datetime.date(td[0],td[1],td[2]) :
                live_doc_notifications = Live_Doctor_Notification.objects.filter(notification_creation_date__range=(datetime.date(fd[0],fd[1],fd[2]), datetime.date(td[0],td[1],td[2]))).order_by('-notification_creation_date')
        elif fd == [1800,1,1] and td == [1800,1,1] and doc_name != '':
            live_doc_notifications = Live_Doctor_Notification.objects.filter(livedoctorName__icontains=doc_name).order_by('-notification_creation_date')
        elif (fd != [1800,1,1] or td != [1800,1,1]) and doc_name != '':
            if datetime.date(fd[0],fd[1],fd[2]) > datetime.date(td[0],td[1],td[2]) :
                messages.error(request, 'FromDate Date should be smaller than  ToDate')
                return render(request, 'admin/live_doctor_management/live_doctor_notification_tab.html',{'tab': tab})
            elif datetime.date(fd[0],fd[1],fd[2]) == datetime.date(td[0],td[1],td[2]) :
                live_doc_notifications = Live_Doctor_Notification.objects.filter(notification_creation_date__date=datetime.date(fd[0],fd[1],fd[2])).filter(livedoctorName__icontains=doc_name).order_by('-notification_creation_date')
            elif datetime.date(fd[0],fd[1],fd[2]) < datetime.date(td[0],td[1],td[2]) :
                live_doc_notifications = Live_Doctor_Notification.objects.filter(notification_creation_date__range=(datetime.date(fd[0],fd[1],fd[2]), datetime.date(td[0],td[1],td[2]))).filter(livedoctorName__icontains=doc_name).order_by('-notification_creation_date')

        elif fd == [1800, 1, 1] and td == [1800, 1, 1] and doc_name == '':
            messages.success(request, 'No Data Provided by user')
            return render(request, 'admin/live_doctor_management/live_doctor_notification_tab.html',
                          {'tab': tab, 'back_button': 'yes'})

       # For template   live_docs[0].updatedAt.strftime('%d/%m/%Y - %H:%M:%S')
       # For template   live_docs[0].updatedAt.strftime('%d/%m/%Y')

        paginator = Paginator(live_doc_notifications, 100)
        page = request.GET.get('page')
        try:
            live_doc_notifications = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            live_doc_notifications = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            live_doc_notifications = paginator.page(paginator.num_pages)

        sendfd = "/".join([str(item) for item in fd])
        sendtd = "/".join([str(item) for item in td])
        return render(request, 'admin/live_doctor_management/live_doctor_notification_tab.html',
                      {'tab': tab, 'live_doc_notifications': live_doc_notifications,'from_date': sendfd,
                       'to_date': sendtd,'doc_name':doc_name,'back_button':'yes',
                       })
    except Exception as e:
        messages.error(request,e)
        return render(request, 'admin/live_doctor_management/live_doctor_notification_tab.html', {'tab': tab,'back_button':'yes'})


####################################################################
# name live_doctor_schedule_notification_bydate                    #
# By Nishank Gupta                                                 #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def live_doctor_schedule_notification_bydate(request):
    try:

        tab = 1
        if request.method == 'POST':
            try:
                fd = request.POST.get('from_date').split('/')
                if fd == ['']:
                    fd = None
            except:
                fd = None
            try:
                td = request.POST.get('to_date').split('/')
                if td == ['']:
                    td = None
            except:
                td = None
            try:
                doc_name = request.POST.get('doc_name')
                if doc_name == None:
                    doc_name = ''
            except:
                doc_name = ''
        else:
            try:
                fd = request.GET.get('from_date').split('/')
                if fd == ['']:
                    fd = None
            except:
                fd = None
            try:
                td = request.GET.get('to_date').split('/')
                if td == ['']:
                    td = None
            except:
                td = None
            try:
                doc_name = request.POST.get('doc_name')
                if doc_name == None:
                    doc_name = ''
            except:
                doc_name = ''


        if fd == None and td != None:
            fd = td
        elif td == None and fd != None:
            td = fd
        elif td == None and fd == None:
            td = ['1800','1','1']
            fd = ['1800', '1', '1']

        fd = [int(item) for item in fd]
        td = [int(item) for item in td]
        live_doc_schedule_notifications = []
        if (fd != [1800,1,1] or td != [1800,1,1]) and doc_name == '':
            if datetime.date(fd[0],fd[1],fd[2]) > datetime.date(td[0],td[1],td[2]) :
                messages.error(request, 'FromDate Date should be smaller than  ToDate')
                return render(request, 'admin/live_doctor_management/live_doc_schedule_delete_notification.html',
                              {'tab': tab,'live_doc_schedule_notifications': live_doc_schedule_notifications, 'back_button': 'no'})

            elif datetime.date(fd[0],fd[1],fd[2]) == datetime.date(td[0],td[1],td[2]) :
                live_doc_schedule_notifications = Live_Doctor_Schedule_Delete_Notification.objects.filter(notification_creation_date__date=datetime.date(fd[0],fd[1],fd[2])).order_by('-notification_creation_date')
            elif datetime.date(fd[0],fd[1],fd[2]) < datetime.date(td[0],td[1],td[2]) :
                live_doc_schedule_notifications = Live_Doctor_Schedule_Delete_Notification.objects.filter(notification_creation_date__range=(datetime.date(fd[0],fd[1],fd[2]), datetime.date(td[0],td[1],td[2]))).order_by('-notification_creation_date')
        elif fd == [1800,1,1] and td == [1800,1,1] and doc_name != '':
            live_doc_schedule_notifications = Live_Doctor_Schedule_Delete_Notification.objects.filter(livedoctorName__icontains=doc_name).order_by('-notification_creation_date')
        elif (fd != [1800,1,1] or td != [1800,1,1]) and doc_name != '':
            if datetime.date(fd[0],fd[1],fd[2]) > datetime.date(td[0],td[1],td[2]) :
                messages.error(request, 'FromDate Date should be smaller than  ToDate')
                return render(request, 'admin/live_doctor_management/live_doc_schedule_delete_notification.html',
                              {'tab': tab, 'live_doc_schedule_notifications': live_doc_schedule_notifications,
                               'back_button': 'no'})

            elif datetime.date(fd[0],fd[1],fd[2]) == datetime.date(td[0],td[1],td[2]) :
                live_doc_schedule_notifications = Live_Doctor_Schedule_Delete_Notification.objects.filter(notification_creation_date__date=datetime.date(fd[0],fd[1],fd[2])).filter(livedoctorName__icontains=doc_name).order_by('-notification_creation_date')
            elif datetime.date(fd[0],fd[1],fd[2]) < datetime.date(td[0],td[1],td[2]) :
                live_doc_schedule_notifications = Live_Doctor_Schedule_Delete_Notification.objects.filter(notification_creation_date__range=(datetime.date(fd[0],fd[1],fd[2]), datetime.date(td[0],td[1],td[2]))).filter(livedoctorName__icontains=doc_name).order_by('-notification_creation_date')

        elif fd == [1800, 1, 1] and td == [1800, 1, 1] and doc_name == '':
            messages.success(request, 'No Data Provided by user')
            return render(request, 'admin/live_doctor_management/live_doc_schedule_delete_notification.html',
                              {'tab': tab,'live_doc_schedule_notifications': live_doc_schedule_notifications, 'back_button': 'yes'})

       # For template   live_docs[0].updatedAt.strftime('%d/%m/%Y - %H:%M:%S')
       # For template   live_docs[0].updatedAt.strftime('%d/%m/%Y')

        paginator = Paginator(live_doc_schedule_notifications, 100)
        page = request.GET.get('page')
        try:
            live_doc_schedule_notifications = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            live_doc_schedule_notifications = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            live_doc_schedule_notifications = paginator.page(paginator.num_pages)

        sendfd = "/".join([str(item) for item in fd])
        sendtd = "/".join([str(item) for item in td])
        return render(request, 'admin/live_doctor_management/live_doc_schedule_delete_notification.html',
                      {'tab': tab, 'live_doc_schedule_notifications': live_doc_schedule_notifications,'from_date': sendfd,
                       'to_date': sendtd,'doc_name':doc_name,'back_button':'yes',
                       })
    except Exception as e:
        messages.error(request,e)
        return render(request, 'admin/live_doctor_management/live_doc_schedule_delete_notification.html',
                      {'tab': tab, 'live_doc_schedule_notifications': live_doc_schedule_notifications,
                       'back_button': 'yes'})




####################################################################
# name live_organisation_notification                              #
# owner Ashutosh kesharvani                                        #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def live_organisation_notification(request):
    try:
        tab = 1
        return render(request, 'admin/admin_live_organisation/live_organisation_notification_tab.html', {'tab': tab})
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


####################################################################
# name live_organisation_notification_bydate                       #
# owner Ashutosh kesharvani                                        #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def live_organisation_notification_bydate(request):
    try:
        tab = 1
        from_date = request.POST.get('from_date').replace('/','-')
        to_date = request.POST.get('to_date').replace('/','-')
        f_date = from_date.split('-')
        t_date = to_date.split('-')
        from datetime import datetime
        if datetime(int(f_date[0]),int(f_date[1]),int(f_date[2])) < datetime(int(t_date[0]),int(t_date[1]),int(t_date[2])):
            pass
        else:
            messages.error(request, 'FromDate Date should be smaller than  ToDate')
            return render(request, 'admin/admin_live_organisation/live_organisation_notification_tab.html',{'tab': tab})
        live_organisation = OrganisationName.objects.filter(is_live_org=True,updatedAt__range = [from_date,to_date])
        return render(request, 'admin/admin_live_organisation/live_organisation_notification_tab.html', {'tab': tab,'live_organisation':live_organisation})
    except Exception as e:
        messages.error(request,e)
        return render(request, 'admin/admin_live_organisation/live_organisation_notification_tab.html', {'tab': tab})


####################################################################
# name livedoctor_delete_older_than_fifteen_days                   #
# BY Nishank                                                       #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def livedoctor_delete_older_than_fifteen_days(request):
    try:
         tab = 1
         import datetime
         time_deltta = datetime.timedelta(days=15)
         now  = datetime.datetime.now()
         delete_from = now - time_deltta
         #delete_from = datetime.datetime(delete_from.year, delete_from.month, delete_from.day)
         live_doc_notifications = Live_Doctor_Notification.objects.filter(
             notification_creation_date__date__lte=delete_from)
         for iittem in live_doc_notifications:
             iittem.delete()
         from datetime import datetime
         live_doc_notifications = Live_Doctor_Notification.objects.all().order_by('-notification_creation_date')
         messages.success(request, 'Successfully deleted notifications')
         return redirect('live_doc_notification')
    except Exception as e:
        messages.error(request,e)
        live_doc_notifications = Live_Doctor_Notification.objects.all().order_by('-notification_creation_date')
        return redirect('live_doc_notification', {'tab': tab, 'live_doc_notifications': live_doc_notifications})


# ####################################################################
# # name live_doctor_notification_byname                             #
# # BY Nishank                                                       #
# ####################################################################
# @login_required(login_url='/')
# @csrf_exempt
# def live_doctor_notification_byname(request):
#     try:
#         tab = 1
#         if request.method == 'POST':
#             try:
#                 doc_name = request.POST.get('doc_name')
#             except:
#                 doc_name = ''
#
#             if doc_name != '':
#                 live_doc_notifications = Live_Doctor_Notification.objects.filter(livedoctorName__icontains = doc_name).order_by('-notification_creation_date')
#             else:
#                 live_doc_notifications = Live_Doctor_Notification.objects.all().order_by('-notification_creation_date')
#         else:
#             try:
#                 doc_name = request.GET.get('doc_name')
#             except:
#                 doc_name = ''
#             if doc_name != '':
#                 live_doc_notifications = Live_Doctor_Notification.objects.filter(livedoctorName__icontains = doc_name).order_by('-notification_creation_date')
#             else:
#                 live_doc_notifications = Live_Doctor_Notification.objects.all().order_by('-notification_creation_date')
#
#         paginator = Paginator(live_doc_notifications, 100)
#         page = request.GET.get('page')
#         try:
#             live_doc_notifications = paginator.page(page)
#         except PageNotAnInteger:
#             # If page is not an integer, deliver first page.
#             live_doc_notifications = paginator.page(1)
#         except EmptyPage:
#             # If page is out of range (e.g. 9999), deliver last page of results.
#             live_doc_notifications = paginator.page(paginator.num_pages)
#
#
#         return render(request, 'admin/live_doctor_management/live_doctor_notification_tab.html', {'tab': tab,
#                                                                     'live_doc_notifications':live_doc_notifications,
#                                                                     'doc_name':doc_name})
#     except Exception as e:
#         messages.error(request,e)
#         return render(request, 'admin/live_doctor_management/live_doctor_notification_tab.html', {'tab': tab})


####################################################################
# Name - live_doc_mark_for_search_results                          #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def live_doc_mark_for_search_results(request):
    try:
        country_data = Country.objects.filter(delete=False)
        state_master_obj = State.objects.filter(delete=False)
        category_obj = Category.objects.filter(delete=False).order_by('name')

        return render(request, 'admin/live_doctor_management/live_doc_mark_for_search_results.html',
                      {'tab': 'data', 'tab_listing': 'live_doctor_listing','country':country_data,
                       'state':state_master_obj,'category_obj': category_obj,
                       'live_doctors':None})



    except Exception as e:
        raise Http404


####################################################################
# Name - get_live_docs_for_search_results                          #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def get_live_docs_for_search_results(request):
    try:
        country_id = request.POST.get('formDATA[country_id]')
        test =  request.POST.get('formDATA[country_id]')
        state_id = request.POST.get('formDATA[state_id]')
        city_id = request.POST.get('formDATA[city_id]')
        locality_id = request.POST.get('formDATA[locality_id]')
        category_id = request.POST.get('formDATA[category_id]')

        # country_data = Country.objects.filter(delete=False)
        # state_master_obj = State.objects.filter(delete=False)
        # category_obj = Category.objects.filter(delete=False).order_by('name')
        orgs_id_list = []
        livedocs_id_list = []
        schedules_list = []
        send_list = []
        Locality_selected = 'NA'
        occupied_values_subs = None
        occupied_values_spons = None
        if country_id != '' and state_id != '' and city_id != '' and category_id != '':

            Key_CC_RANK = None
            Key_CLC_RANK = None

            if locality_id == '':
                orgs_id_list = OrganisationName.objects.filter(country_id=int(country_id),state_id=int(state_id),city_id=int(city_id)).values_list('id',flat=True)
                livedocs_id_list = Live_Doctor.objects.filter(category=int(category_id)).values_list('id',flat=True)
                schedules_list = Live_Doctor_Commonworkschedule.objects.filter(doctor_id__in = livedocs_id_list,clinic_id__in=orgs_id_list)
                for schs in schedules_list:
                    if schs.status.lower() != 'delete':
                    #if True:
                        ldoc = Live_Doctor.objects.get(id=schs.doctor_id)
                        Org = OrganisationName.objects.get(id = schs.clinic_id)
                        Key_CC_RANK =  str(Org.city_id)+'-'+str(ldoc.category)
                        if send_list != []:
                            temp_map = map(lambda x: x[0],send_list)
                            if ldoc not in temp_map:
                                send_list.append([ldoc,Org,schs.id,[ldoc.sponsored_rank['CC_RANK_list'].get(Key_CC_RANK,''),ldoc.subscribed_rank['CC_RANK_list'].get(Key_CC_RANK,''),ldoc.trial_rank],ldoc.firstName,ldoc.sponsored_start_dates.get(Key_CC_RANK,'NA'),ldoc.sponsored_end_dates.get(Key_CC_RANK,'NA')])
                        else:
                            send_list.append([ldoc,Org,schs.id,[ldoc.sponsored_rank['CC_RANK_list'].get(Key_CC_RANK,''),ldoc.subscribed_rank['CC_RANK_list'].get(Key_CC_RANK,''),ldoc.trial_rank],ldoc.firstName,ldoc.sponsored_start_dates.get(Key_CC_RANK,'NA'),ldoc.sponsored_end_dates.get(Key_CC_RANK,'NA')])
                send_list.sort(key=lambda x: x[4])
                Locality_selected = False
                try:
                    occupied_values_subs = subs_occupied_cc_ranks.objects.get(key=Key_CC_RANK).ranklist
                    if occupied_values_subs == []:
                        occupied_values_subs= ''
                    elif occupied_values_subs != None and occupied_values_subs != []:
                        occupied_values_subs = ",".join([str(iii) for iii in occupied_values_subs])
                except Exception as e:
                    occupied_values_subs = ''

                try:
                    occupied_values_spons = spons_occupied_cc_ranks.objects.get(key=Key_CC_RANK).ranklist
                    if occupied_values_spons == []:
                        occupied_values_spons = ''
                    elif occupied_values_spons != None and occupied_values_spons != []:
                        occupied_values_spons = ",".join([str(iii) for iii in occupied_values_spons])
                except Exception as e:
                    occupied_values_spons = ''


            elif locality_id != '' :
                orgs_id_list = OrganisationName.objects.filter(country_id=int(country_id), state_id=int(state_id),
                                                               city_id=int(city_id),locality_id=int(locality_id)).values_list('id', flat=True)
                livedocs_id_list = Live_Doctor.objects.filter(category=int(category_id)).values_list('id', flat=True)
                schedules_list = Live_Doctor_Commonworkschedule.objects.filter(doctor_id__in=livedocs_id_list,
                                                                               clinic_id__in=orgs_id_list)
                for schs in schedules_list:
                    if schs.status.lower() != 'delete':
                    #if True:
                        ldoc = Live_Doctor.objects.get(id=schs.doctor_id)
                        Org = OrganisationName.objects.get(id=schs.clinic_id)
                        Key_CLC_RANK = str(Org.city_id) + '-' + str(Org.locality_id) + '-' + str(ldoc.category)
                        if send_list != []:
                            temp_map = map(lambda x: x[0],send_list)
                            if ldoc not in temp_map:
                                send_list.append([ldoc, Org, schs.id,[ldoc.sponsored_rank['CLC_RANK_list'].get(Key_CLC_RANK,''),ldoc.subscribed_rank['CLC_RANK_list'].get(Key_CLC_RANK,''),ldoc.trial_rank],ldoc.firstName,ldoc.sponsored_start_dates.get(Key_CLC_RANK,'NA'),ldoc.sponsored_end_dates.get(Key_CLC_RANK,'NA')])
                        else:
                            send_list.append([ldoc,Org,schs.id,[ldoc.sponsored_rank['CLC_RANK_list'].get(Key_CLC_RANK,''),ldoc.subscribed_rank['CLC_RANK_list'].get(Key_CLC_RANK,''),ldoc.trial_rank],ldoc.firstName,ldoc.sponsored_start_dates.get(Key_CLC_RANK,'NA'),ldoc.sponsored_end_dates.get(Key_CLC_RANK,'NA')])
                send_list.sort(key=lambda x: x[4])
                Locality_selected = True
                try:
                    occupied_values_subs = subs_occupied_clc_ranks.objects.get(key=Key_CLC_RANK).ranklist
                    if occupied_values_subs == []:
                        occupied_values_subs = ''
                    elif occupied_values_subs != None and occupied_values_subs != []:
                        occupied_values_subs = ",".join([str(iii) for iii in occupied_values_subs])
                except Exception as e:
                    occupied_values_subs = ''
                try:
                    occupied_values_spons = spons_occupied_clc_ranks.objects.get(key=Key_CLC_RANK).ranklist
                    if occupied_values_spons == []:
                        occupied_values_spons = ''
                    elif occupied_values_spons != None and occupied_values_spons != []:
                        occupied_values_spons = ",".join([str(iii) for iii in occupied_values_spons])
                except Exception as e:
                    occupied_values_spons = ''

            if locality_id != '':
                tyyype = 'CLC'
                kkeeyy = Key_CLC_RANK
            else:
                tyyype = 'CC'
                kkeeyy = Key_CC_RANK
            occupied_values_obj = {'type':tyyype,'key':kkeeyy,'occupied_values_subs':occupied_values_subs,
                                   'occupied_values_spons':occupied_values_spons}


        else:
            messages.error(request,"City and Category are required")
            response = {"Message":"City and Category are required","Redirect":False}
            return HttpResponse(json.dumps(response))

        html = render_to_string('admin/live_doctor_management/get_live_doctor_for_search_results.html',
                                {'send_list':send_list,'Locality_selected':Locality_selected,'occupied_values_obj':occupied_values_obj})

        return HttpResponse(html)

    except Exception as e:
        raise Http404


####################################################################
# Name - save_live_doctor_rank                                     #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def save_live_doctor_rank(request):
    try:
        formDATA = request.POST.get('formDATA')
        type = request.POST.get('formDATA[TYPE]')
        checkedValues = request.POST.get('formDATA[checkedValues]')
        checkedValues = checkedValues.split(',')

        if type == 'CC':
            Spon_CC_RANK_list = request.POST.get('formDATA[Spon_CC_RANK_list]')
            Spon_CC_RANK_list = Spon_CC_RANK_list.split(',')

            Spon_CC_RANK_StartDate = request.POST.get('formDATA[Spon_CC_RANK_StartDate]')
            Spon_CC_RANK_StartDate = Spon_CC_RANK_StartDate.split(',')
            Spon_CC_RANK_EndDate = request.POST.get('formDATA[Spon_CC_RANK_EndDate]')
            Spon_CC_RANK_EndDate = Spon_CC_RANK_EndDate.split(",")

            Subs_CC_RANK_list = request.POST.get('formDATA[Subs_CC_RANK_list]')
            Subs_CC_RANK_list = Subs_CC_RANK_list.split(',')

            #Trial_CC_RANK_list = request.POST.get('formDATA[Trial_CC_RANK_list]')
            #Trial_CC_RANK_list = Trial_CC_RANK_list.split(',')

        elif type == 'CLC':
            Spon_CLC_RANK_list = request.POST.get('formDATA[Spon_CLC_RANK_list]')
            Spon_CLC_RANK_list = Spon_CLC_RANK_list.split(',')

            Spon_CLC_RANK_StartDate = request.POST.get('formDATA[Spon_CLC_RANK_StartDate]')
            Spon_CLC_RANK_StartDate = Spon_CLC_RANK_StartDate.split(",")
            Spon_CLC_RANK_EndDate = request.POST.get('formDATA[Spon_CLC_RANK_EndDate]')
            Spon_CLC_RANK_EndDate = Spon_CLC_RANK_EndDate.split(",")

            Subs_CLC_RANK_list = request.POST.get('formDATA[Subs_CLC_RANK_list]')
            Subs_CLC_RANK_list = Subs_CLC_RANK_list.split(',')

            #Trial_CLC_RANK_list = request.POST.get('formDATA[Trial_CLC_RANK_list]')
            #Trial_CLC_RANK_list = Trial_CLC_RANK_list.split(',')

        spons_json= {}
        subs_json= {}
        #trial_json= {}
        cat_id = city_id = None
        key = None
        error_msg=[]
        sponsored_keys = None
        subscribed_keys = None
        #trial_keys = None

        if type == 'CC':
            if Spon_CC_RANK_list != [''] and Subs_CC_RANK_list != [''] and len(Spon_CC_RANK_list) == len(Subs_CC_RANK_list) == len(checkedValues):
                for i in range(0,len(checkedValues)):
                    livedoc = Live_Doctor.objects.get(id= Live_Doctor_Commonworkschedule.objects.get(id=int(checkedValues[i])).doctor_id)
                    cat_id = livedoc.category
                    city_id = OrganisationName.objects.get(id = Live_Doctor_Commonworkschedule.objects.get(id=int(checkedValues[i])).clinic_id).city_id
                    key = str(city_id)+'-'+str(cat_id)

                    livedoc.sponsored_start_dates[key] = Spon_CC_RANK_StartDate[i]
                    livedoc.sponsored_end_dates[key] = Spon_CC_RANK_EndDate[i]

                    #occu_ranks = Occupied_ranks.objects.all()
                    # if list(occu_ranks) == []:
                    #     Occupied_ranks.objects.create()
                    #     occu_ranks = Occupied_ranks.objects.all()
                    #sponsored_keys = occu_ranks[0].doctor['CC']['Sponsored'].keys()
                    #subscribed_keys = occu_ranks[0].doctor['CC']['Subscribed'].keys()

                    #trial_keys = occu_ranks[0].doctor['CC']['trial'].keys()

                    ################ SPONSORED CHECK ################################
                    spon_cc_occu_list = None
                    try:
                        spon_cc_occu_obj = spons_occupied_cc_ranks.objects.get(key=key)
                        spon_cc_occu_list = spon_cc_occu_obj.ranklist
                        spon_cc_occu_list.sort()
                    except:
                        spon_cc_occu_list = 'DoesNotExist'
                    #occupied_values = None
                    #if key in sponsored_keys:
                    if spon_cc_occu_list != 'DoesNotExist' and spon_cc_occu_list != None:
                        #occupied_values = occu_ranks[0].doctor['CC']['Sponsored'][key]
                        current_value = livedoc.sponsored_rank['CC_RANK_list'].get(key,'Notfound')
                        if current_value != int(Spon_CC_RANK_list[i]):
                            #if int(Spon_CC_RANK_list[i]) in occupied_values:
                            if int(Spon_CC_RANK_list[i]) in spon_cc_occu_list:
                                msg = "CC Sponsored Rank " + Spon_CC_RANK_list[
                                    i] + " Already Occupied (Now set to 9999) - Tried For Dr." + livedoc.firstName + ' '+ livedoc.lastName + "\n"
                                error_msg.append(msg)
                                msg = None

                                # since system is itself setting the rank of doc to 9999, we will
                                # make the system delete the current rank from occupied ranks too
                                # if it exists there
                                while (current_value in spon_cc_occu_list):
                                    spon_cc_occu_list.remove(current_value)
                                spon_cc_occu_list.sort()
                                spon_cc_occu_obj.ranklist = spon_cc_occu_list
                                spon_cc_occu_obj.save()

                                # Mark the rank as 9999 showing Not set
                                livedoc.sponsored_rank['CC_RANK_list'][key] = 9999
                                # Do not save in accupied ranks

                            elif int(Spon_CC_RANK_list[i]) == 9999 or int(Spon_CC_RANK_list[i]) == 0:
                                # Mark the rank as 9999 showing Not set or as 0 showing no rank
                                # Do not save in accupied ranks
                                livedoc.sponsored_rank['CC_RANK_list'][key] = int(Spon_CC_RANK_list[i])

                                if current_value != 'Notfound':
                                    # Delete from occupied ranks
                                    while current_value in spon_cc_occu_list:
                                        spon_cc_occu_list.remove(current_value)
                                    spon_cc_occu_list.sort()
                                    spon_cc_occu_obj.ranklist = spon_cc_occu_list
                                    spon_cc_occu_obj.save()
                            else:
                                if current_value != 'Notfound':
                                    # Delete from occupied ranks
                                    while current_value in spon_cc_occu_list:
                                        spon_cc_occu_list.remove(current_value)
                                    spon_cc_occu_list.sort()
                                # Save the rank
                                livedoc.sponsored_rank['CC_RANK_list'][key] = int(Spon_CC_RANK_list[i])
                                #occu_ranks[0].doctor['CC']['Sponsored'][key].append(int(Spon_CC_RANK_list[i]))
                                #occu_ranks[0].save()
                                spon_cc_occu_list.append(int(Spon_CC_RANK_list[i]))
                                spon_cc_occu_list.sort()
                                spon_cc_occu_obj.ranklist = spon_cc_occu_list
                                spon_cc_occu_obj.save()
                        else:
                            if current_value != 9999 and current_value != 0:
                                if current_value not in spon_cc_occu_list:
                                    spon_cc_occu_list.append(current_value)
                                    spon_cc_occu_list.sort()
                                    spon_cc_occu_obj.ranklist = spon_cc_occu_list
                                    spon_cc_occu_obj.save()
                    else:
                        # EVEN if rank value is 9999 or 0, we assign this rank value to doctor's  Spon >  cc rank
                        livedoc.sponsored_rank['CC_RANK_list'][key] = int(Spon_CC_RANK_list[i])
                        # BUT IF value isd 9999 or 0 we don't add it to the accupied ranks
                        if int(Spon_CC_RANK_list[i]) != 9999 and int(Spon_CC_RANK_list[i]) != 0:
                            #occu_ranks[0].doctor['CC']['Sponsored'][key] = [int(Spon_CC_RANK_list[i])]
                            #ccu_ranks[0].save()
                            new_spon_cc_occu_obj = spons_occupied_cc_ranks.objects.create(key=key,ranklist=[int(Spon_CC_RANK_list[i])])

                    ###########################SUBSCRIBED CHECK ###################
                    if livedoc.is_subscribed == True:
                        subs_cc_occu_ranks = None
                        try:
                            subs_cc_occu_obj = subs_occupied_cc_ranks.objects.get(key=key)
                            subs_cc_occu_list = subs_cc_occu_obj.ranklist
                            subs_cc_occu_list.sort()
                        except:
                            subs_cc_occu_list = 'DoesNotExist'
                        #occupied_values = None
                        #if key in subscribed_keys:
                        if subs_cc_occu_list != 'DoesNotExist' and subs_cc_occu_list != None:
                            #occupied_values = occu_ranks[0].doctor['CC']['Subscribed'][key]
                            current_value = livedoc.subscribed_rank['CC_RANK_list'].get(key,'Notfound')
                            if current_value != int(Subs_CC_RANK_list[i]):
                                if int(Subs_CC_RANK_list[i]) in subs_cc_occu_list:
                                    msg = "CC Subscribed Rank " + Subs_CC_RANK_list[
                                        i] + " Already Occupied (Now set to 9999) - Tried For Dr."+ livedoc.firstName + ' '+ livedoc.lastName + "\n"
                                    error_msg.append(msg)
                                    msg = None

                                    # since system is itself setting the rank of doc to 9999, we will
                                    # make the system delete the current rank from occupied ranks too
                                    # if it exists there
                                    while (current_value in subs_cc_occu_list):
                                        subs_cc_occu_list.remove(current_value)
                                    subs_cc_occu_list.sort()
                                    subs_cc_occu_obj.ranklist = subs_cc_occu_list
                                    subs_cc_occu_obj.save()

                                    # Mark the rank as 9999 showing Not set
                                    livedoc.subscribed_rank['CC_RANK_list'][key] = 9999
                                    # Do not save in accupied ranks

                                elif int(Subs_CC_RANK_list[i]) == 9999 or int(Subs_CC_RANK_list[i]) == 0:
                                    # Mark the rank as 9999 showing Not set or as 0 showing no rank
                                    # Do not save in accupied ranks
                                    livedoc.subscribed_rank['CC_RANK_list'][key] = int(Subs_CC_RANK_list[i])

                                    if current_value != 'Notfound':
                                        # Delete from occupied ranks
                                        while current_value in subs_cc_occu_list:
                                            subs_cc_occu_list.remove(current_value)
                                        subs_cc_occu_list.sort()
                                        subs_cc_occu_obj.ranklist = subs_cc_occu_list
                                        subs_cc_occu_obj.save()
                                else:
                                    if current_value != 'Notfound':
                                        # Delete from occupied ranks
                                        while current_value in subs_cc_occu_list:
                                            subs_cc_occu_list.remove(current_value)
                                        subs_cc_occu_list.sort()
                                    # Save the rank
                                    livedoc.subscribed_rank['CC_RANK_list'][key] = int(Subs_CC_RANK_list[i])
                                    #occu_ranks[0].doctor['CC']['Subscribed'][key].append(int(Subs_CC_RANK_list[i]))
                                    #occu_ranks[0].save()
                                    subs_cc_occu_list.append(int(Subs_CC_RANK_list[i]))
                                    subs_cc_occu_list.sort()
                                    subs_cc_occu_obj.ranklist = subs_cc_occu_list
                                    subs_cc_occu_obj.save()
                            else:
                                if current_value != 9999 and current_value != 0:
                                    if current_value not in subs_cc_occu_list:
                                        subs_cc_occu_list.append(current_value)
                                        subs_cc_occu_list.sort()
                                        subs_cc_occu_obj.ranklist = subs_cc_occu_list
                                        subs_cc_occu_obj.save()
                        else:
                            # EVEN if rank value is 9999 or 0, we assign this rank value to doctor's  Spon >  cc rank
                            livedoc.subscribed_rank['CC_RANK_list'][key] = int(Subs_CC_RANK_list[i])
                            # BUT IF value isd 9999 or 0 we don't add it to the accupied ranks
                            if int(Subs_CC_RANK_list[i]) != 9999 and int(Subs_CC_RANK_list[i]) != 0:
                                #occu_ranks[0].doctor['CC']['Subscribed'][key] = [int(Subs_CC_RANK_list[i])]
                                #occu_ranks[0].save()
                                new_subs_cc_occu_obj = subs_occupied_cc_ranks.objects.create(key=key, ranklist=[int(Subs_CC_RANK_list[i])])

                    # ##########################TRIAL CHECK #########################
                    #
                    # occupied_values = None
                    # if key in trial_keys:
                    #     occupied_values = occu_ranks[0].doctor['CC']['trial'][key]
                    #     current_value = livedoc.trial_rank['CC_RANK_list'].get(key, 'Notfound')
                    #     if current_value != int(Trial_CC_RANK_list[i]):
                    #         if int(Trial_CC_RANK_list[i]) in occupied_values:
                    #             msg = "CC Trial Rank " + Trial_CC_RANK_list[
                    #                 i] + " Already Occupied (Now set to 9999) - Tried For Dr." + livedoc.firstName + ' '+ livedoc.lastName + "\n"
                    #             error_msg.append(msg)
                    #             msg = None
                    #             # Mark the rank as 9999 showing Not set
                    #             livedoc.trial_rank['CC_RANK_list'][key] = 9999
                    #             # Do not save in accupied ranks
                    #
                    #         elif int(Trial_CC_RANK_list[i]) == 9999 or int(Trial_CC_RANK_list[i]) == 0:
                    #             # Mark the rank as 9999 showing Not set or as 0 showing no rank
                    #             livedoc.trial_rank['CC_RANK_list'][key] = int(Trial_CC_RANK_list[i])
                    #             # Do not save in accupied ranks
                    #         else:
                    #             # Save the rank
                    #             livedoc.trial_rank['CC_RANK_list'][key] = int(Trial_CC_RANK_list[i])
                    #             occu_ranks[0].doctor['CC']['trial'][key].append(int(Trial_CC_RANK_list[i]))
                    #             occu_ranks[0].save()
                    # else:
                    #     # EVEN if rank value is 9999 or 0, we assign this rank value to doctor's  Spon >  cc rank
                    #     livedoc.trial_rank['CC_RANK_list'][key] = int(Trial_CC_RANK_list[i])
                    #     # BUT IF value isd 9999 or 0 we don't add it to the accupied ranks
                    #     if int(Trial_CC_RANK_list[i]) != 9999 and int(Trial_CC_RANK_list[i]) != 0:
                    #         occu_ranks[0].doctor['CC']['trial'][key] = [int(Trial_CC_RANK_list[i])]
                    #         occu_ranks[0].save()

                    ##############################################

                   # SAVE THE DOCTOR. WHAT EVER THE RANK VALUES BE, THESE HAVE BEEN SAVED INSIDE THE DOCTOR,TO
                   # BE PUBLISHED WITH THE DOCTOR
                    livedoc.save()
                if error_msg == [] :
                    Messagee = 'Successfully Updated CC Ranks'
                else:
                    Messagee =  " --- ".join(error_msg)
                return HttpResponse(json.dumps({"Redirect": False, "Message": Messagee}))

            else:
                #messages.error(request, "Missing Rank Values in Checked Rows")
                #return reverse('live-doc-mark-for-search-results')
                return HttpResponse(json.dumps({"Redirect": False, "Message": "Missing Rank Values in Checked Rows"}))

        elif type == 'CLC':
            if Spon_CLC_RANK_list != [''] and Subs_CLC_RANK_list != [''] and len(Spon_CLC_RANK_list) == len(Subs_CLC_RANK_list) == len(checkedValues):
                for i in range(0,len(checkedValues)):
                    livedoc = Live_Doctor.objects.get(id=Live_Doctor_Commonworkschedule.objects.get(id=int(checkedValues[i])).doctor_id)
                    cat_id = livedoc.category
                    city_id = OrganisationName.objects.get(id=Live_Doctor_Commonworkschedule.objects.get(id=int(checkedValues[i])).clinic_id).city_id
                    locality_id = OrganisationName.objects.get(id=Live_Doctor_Commonworkschedule.objects.get(id=int(checkedValues[i])).clinic_id).locality_id
                    key = str(city_id) + '-' +str(locality_id) +'-'+ str(cat_id)

                    livedoc.sponsored_start_dates[key] = Spon_CLC_RANK_StartDate[i]
                    livedoc.sponsored_end_dates[key] = Spon_CLC_RANK_EndDate[i]

                    # occu_ranks = Occupied_ranks.objects.all()
                    # if list(occu_ranks) == []:
                    #     Occupied_ranks.objects.create()
                    #     occu_ranks = Occupied_ranks.objects.all()

                    #sponsored_keys = occu_ranks[0].doctor['CLC']['Sponsored'].keys()
                    #subscribed_keys = occu_ranks[0].doctor['CLC']['Subscribed'].keys()

                    #trial_keys = occu_ranks[0].doctor['CLC']['trial'].keys()

                    ################ SPONSORED CHECK ################################
                    spon_clc_occu_list = None
                    try:
                        spon_clc_occu_obj = spons_occupied_clc_ranks.objects.get(key=key)
                        spon_clc_occu_list = spon_clc_occu_obj.ranklist
                        spon_clc_occu_list.sort()
                    except:
                        spon_clc_occu_list = 'DoesNotExist'


                    #occupied_values = None
                    #if key in spon_clc_occu_list:
                    if spon_clc_occu_list != 'DoesNotExist' and spon_clc_occu_list != None:
                        #occupied_values = occu_ranks[0].doctor['CLC']['Sponsored'][key]
                        current_value = livedoc.sponsored_rank['CLC_RANK_list'].get(key, 'Notfound')
                        if current_value != int(Spon_CLC_RANK_list[i]):
                            #if int(Spon_CLC_RANK_list[i]) in occupied_values:
                            if int(Spon_CLC_RANK_list[i]) in spon_clc_occu_list:
                                msg = "CLC Sponsored Rank " + Spon_CLC_RANK_list[
                                    i] + " Already Occupied (Now set to 9999) - Tried For Dr." + livedoc.firstName + ' '+ livedoc.lastName + "\n"
                                error_msg.append(msg)
                                msg = None

                                # since system is itself setting the rank of doc to 9999, we will
                                # make the system delete the current rank from occupied ranks too
                                # if it exists there
                                while(current_value in spon_clc_occu_list):
                                    spon_clc_occu_list.remove(current_value)
                                spon_clc_occu_list.sort()
                                spon_clc_occu_obj.ranklist = spon_clc_occu_list
                                spon_clc_occu_obj.save()

                                # Mark the rank as 9999 showing Not set
                                livedoc.sponsored_rank['CLC_RANK_list'][key] = 9999
                                # Do not save in accupied ranks

                            elif int(Spon_CLC_RANK_list[i]) == 9999 or int(Spon_CLC_RANK_list[i]) == 0:
                                # Mark the rank as 9999 showing Not set or as 0 showing no rank
                                # Do not save in accupied ranks
                                livedoc.sponsored_rank['CLC_RANK_list'][key] = int(Spon_CLC_RANK_list[i])

                                if current_value != 'Notfound':
                                    # Delete from occupied ranks
                                    while current_value in spon_clc_occu_list:
                                        spon_clc_occu_list.remove(current_value)
                                    spon_clc_occu_list.sort()
                                    spon_clc_occu_obj.ranklist = spon_clc_occu_list
                                    spon_clc_occu_obj.save()
                            else:
                                if current_value != 'Notfound':
                                    # Delete from occupied ranks
                                    while current_value in spon_clc_occu_list:
                                        spon_clc_occu_list.remove(current_value)
                                    spon_clc_occu_list.sort()
                                # Save the rank
                                livedoc.sponsored_rank['CLC_RANK_list'][key] = int(Spon_CLC_RANK_list[i])
                                #occu_ranks[0].doctor['CLC']['Sponsored'][key].append(int(Spon_CLC_RANK_list[i]))
                                #occu_ranks[0].save()
                                spon_clc_occu_list.append(int(Spon_CLC_RANK_list[i]))
                                spon_clc_occu_list.sort()
                                spon_clc_occu_obj.ranklist = spon_clc_occu_list
                                spon_clc_occu_obj.save()
                        else:
                            if current_value != 9999 and current_value != 0:
                                if current_value not in spon_clc_occu_list:
                                    spon_clc_occu_list.append(current_value)
                                    spon_clc_occu_list.sort()
                                    spon_clc_occu_obj.ranklist = spon_clc_occu_list
                                    spon_clc_occu_obj.save()
                    else:
                        # EVEN if rank value is 9999 or 0, we assign this rank value to doctor's  Spon >  clc rank
                        livedoc.sponsored_rank['CLC_RANK_list'][key] = int(Spon_CLC_RANK_list[i])
                        # BUT IF value isd 9999 or 0 we don't add it to the accupied ranks
                        if int(Spon_CLC_RANK_list[i]) != 9999 and int(Spon_CLC_RANK_list[i]) != 0:
                            #occu_ranks[0].doctor['CLC']['Sponsored'][key] = [int(Spon_CLC_RANK_list[i])]
                            #occu_ranks[0].save()
                            new_spons_clc_occu_obj = spons_occupied_clc_ranks.objects.create(key=key, ranklist=[int(Spon_CLC_RANK_list[i])])

                    ###########################SUBSCRIBED CHECK ###################

                    if livedoc.is_subscribed == True:
                        try:
                            subs_clc_occu_obj = subs_occupied_clc_ranks.objects.get(key=key)
                            subs_clc_occu_list = subs_clc_occu_obj.ranklist
                            subs_clc_occu_list.sort()
                        except:
                            subs_clc_occu_list = 'DoesNotExist'
                        #occupied_values = None
                        #if key in subs_clc_occu_list:
                        if subs_clc_occu_list != 'DoesNotExist' and subs_clc_occu_list != None:
                            #occupied_values = occu_ranks[0].doctor['CLC']['Subscribed'][key]
                            current_value = livedoc.subscribed_rank['CLC_RANK_list'].get(key, 'Notfound')
                            if current_value != int(Subs_CLC_RANK_list[i]):
                                if int(Subs_CLC_RANK_list[i]) in subs_clc_occu_list:
                                    msg = "CLC Subscribed Rank " + Subs_CLC_RANK_list[
                                        i] + " Already Occupied (Now set to 9999) - Tried For Dr." + livedoc.firstName + ' '+ livedoc.lastName + "\n"
                                    error_msg.append(msg)
                                    msg = None

                                    # since system is itself setting the rank of doc to 9999, we will
                                    # make the system delete the current rank from occupied ranks too
                                    # if it exists there
                                    while (current_value in subs_clc_occu_list):
                                        subs_clc_occu_list.remove(current_value)
                                    subs_clc_occu_list.sort()
                                    subs_clc_occu_obj.ranklist = subs_clc_occu_list
                                    subs_clc_occu_obj.save()

                                    # Mark the rank as 9999 showing Not set
                                    livedoc.subscribed_rank['CLC_RANK_list'][key] = 9999
                                    # Do not save in accupied ranks

                                elif int(Subs_CLC_RANK_list[i]) == 9999 or int(Subs_CLC_RANK_list[i]) == 0:
                                    # Mark the rank as 9999 showing Not set or as 0 showing no rank
                                    # Do not save in accupied ranks
                                    livedoc.subscribed_rank['CLC_RANK_list'][key] = int(Subs_CLC_RANK_list[i])

                                    if current_value != 'Notfound':
                                        # Delete from occupied ranks
                                        while current_value in subs_clc_occu_list:
                                            subs_clc_occu_list.remove(current_value)
                                        subs_clc_occu_list.sort()
                                        subs_clc_occu_obj.ranklist = subs_clc_occu_list
                                        subs_clc_occu_obj.save()
                                else:
                                    if current_value != 'Notfound':
                                        # Delete from occupied ranks
                                        while current_value in subs_clc_occu_list:
                                            subs_clc_occu_list.remove(current_value)
                                        subs_clc_occu_list.sort()
                                    # Save the rank
                                    livedoc.subscribed_rank['CLC_RANK_list'][key] = int(Subs_CLC_RANK_list[i])
                                    #occu_ranks[0].doctor['CLC']['Subscribed'][key].append(int(Subs_CLC_RANK_list[i]))
                                    #occu_ranks[0].save()
                                    subs_clc_occu_list.append(int(Subs_CLC_RANK_list[i]))
                                    subs_clc_occu_list.sort()
                                    subs_clc_occu_obj.ranklist = subs_clc_occu_list
                                    subs_clc_occu_obj.save()
                            else:
                                if current_value != 9999 and current_value != 0:
                                    if current_value not in subs_clc_occu_list:
                                        subs_clc_occu_list.append(current_value)
                                        subs_clc_occu_list.sort()
                                        subs_clc_occu_obj.ranklist = subs_clc_occu_list
                                        subs_clc_occu_obj.save()
                        else:
                            # EVEN if rank value is 9999 or 0, we assign this rank value to doctor's  Spon >  cc rank
                            livedoc.subscribed_rank['CLC_RANK_list'][key] = int(Subs_CLC_RANK_list[i])
                            # BUT IF value isd 9999 or 0 we don't add it to the accupied ranks
                            if int(Subs_CLC_RANK_list[i]) != 9999 and int(Subs_CLC_RANK_list[i]) != 0:
                                #occu_ranks[0].doctor['CLC']['Subscribed'][key] = [int(Subs_CLC_RANK_list[i])]
                                #occu_ranks[0].save()
                                new_subs_clc_occu_obj = subs_occupied_clc_ranks.objects.create(key=key, ranklist=[int(Subs_CLC_RANK_list[i])])

                    # ##########################TRIAL CHECK #########################
                    #
                    # occupied_values = None
                    # if key in trial_keys:
                    #     occupied_values = occu_ranks[0].doctor['CLC']['trial'][key]
                    #     current_value =  livedoc.trial_rank['CLC_RANK_list'].get(key, 'Notfound')
                    #     if current_value != int(Trial_CLC_RANK_list[i]):
                    #         if int(Trial_CLC_RANK_list[i]) in occupied_values:
                    #             msg = "CLC Trial Rank " + Trial_CLC_RANK_list[
                    #                 i] + " Already Occupied (Now set to 9999) - Tried For Dr." + livedoc.firstName + ' '+ livedoc.lastName + "\n"
                    #             error_msg.append(msg)
                    #             msg = None
                    #             # Mark the rank as 9999 showing Not set
                    #             livedoc.trial_rank['CLC_RANK_list'][key] = 9999
                    #             # Do not save in accupied ranks
                    #
                    #         elif int(Trial_CLC_RANK_list[i]) == 9999 or int(Trial_CLC_RANK_list[i]) == 0:
                    #             # Mark the rank as 9999 showing Not set or as 0 showing no rank
                    #             livedoc.trial_rank['CLC_RANK_list'][key] = int(Trial_CLC_RANK_list[i])
                    #             # Do not save in accupied ranks
                    #         else:
                    #             # Save the rank
                    #             livedoc.trial_rank['CLC_RANK_list'][key] = int(Trial_CLC_RANK_list[i])
                    #             occu_ranks[0].doctor['CLC']['trial'][key].append(int(Trial_CLC_RANK_list[i]))
                    #             occu_ranks[0].save()
                    # else:
                    #     # EVEN if rank value is 9999 or 0, we assign this rank value to doctor's  Spon >  cc rank
                    #     livedoc.trial_rank['CLC_RANK_list'][key] = int(Trial_CLC_RANK_list[i])
                    #     # BUT IF value isd 9999 or 0 we don't add it to the accupied ranks
                    #     if int(Trial_CLC_RANK_list[i]) != 9999 and int(Trial_CLC_RANK_list[i]) != 0:
                    #         occu_ranks[0].doctor['CLC']['trial'][key] = [int(Trial_CLC_RANK_list[i])]
                    #         occu_ranks[0].save()

                    ##############################################

                    # SAVE THE DOCTOR. WHAT EVER THE RANK VALUES BE, THESE HAVE BEEN SAVED INSIDE THE DOCTOR,TO
                    # BE PUBLISHED WITH THE DOCTOR
                    livedoc.save()

                if error_msg == [] :
                    Messagee = 'Successfully Updated CLC Ranks'
                else:
                    Messagee =  " --- ".join(error_msg)
                return HttpResponse(json.dumps({"Redirect": False, "Message": Messagee}))
            else:
                #messages.error(request, "Missing Rank Values in Checked Rows")
                #return reverse('live-doc-mark-for-search-results')
                return HttpResponse(json.dumps({"Redirect": False, "Message": "Missing Rank Values in Checked Rows"}))
        else:
            #messages.error(request, "No Rank Values Provided")
            MYMSG = json.dumps({"Redirect":False,"Message":"No Rank Values Provided"})
            return  HttpResponse(MYMSG)
        #return  {"Redirect": False, "Message": "Rank Data Successfully Saved"}


    except Exception as e:
        raise Http404



#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
####################################################################
# Name - reset_livedoctor_sponsranks_deleted_schedules             #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def reset_livedoctor_sponsranks_deleted_schedules(request):
    try:
        formDATA = request.POST.get('formDATA')
        checkedValues = request.POST.get('formDATA[checkedValues]')
        checkedValues = checkedValues.split(',')

        Spon_CC_RANK_list = request.POST.get('formDATA[Spon_CC_RANK_list]')
        Spon_CC_RANK_list = Spon_CC_RANK_list.split(',')
        Spon_CLC_RANK_list = request.POST.get('formDATA[Spon_CLC_RANK_list]')
        Spon_CLC_RANK_list = Spon_CLC_RANK_list.split(',')

        Spon_CC_KEY_list = request.POST.get('formDATA[Spon_CC_KEY_list]')
        Spon_CC_KEY_list = Spon_CC_KEY_list.split(',')
        Spon_CLC_KEY_list = request.POST.get('formDATA[Spon_CLC_KEY_list]')
        Spon_CLC_KEY_list = Spon_CLC_KEY_list.split(',')
        error_msg=None
        #if Spon_CLC_RANK_list != [''] and Subs_CLC_RANK_list != [''] and len(Spon_CLC_RANK_list) == len(Subs_CLC_RANK_list) == len(checkedValues):

        try:
            for i in range(0,len(checkedValues)):
                livedoc = Live_Doctor.objects.get(id=int(checkedValues[i]))
                if Spon_CC_KEY_list[i].lower() != "novalue" and Spon_CC_RANK_list[i].lower() != "novalue":
                    current_value_cc_rank = livedoc.sponsored_rank['CC_RANK_list'].get(Spon_CC_KEY_list[i],None)
                    tt = None
                    tt = Spon_CC_RANK_list[i]
                    if tt.isdigit() and int(Spon_CC_RANK_list[i]) == 0:
                        livedoc.sponsored_rank['CC_RANK_list'][Spon_CC_KEY_list[i]] = int(Spon_CC_RANK_list[i])
                        spon_cc_occu_list = None
                        try:
                            spon_cc_occu_obj = spons_occupied_cc_ranks.objects.get(key=Spon_CC_KEY_list[i])
                            spon_cc_occu_list = spon_cc_occu_obj.ranklist
                            spon_cc_occu_list.sort()
                        except:
                            spon_cc_occu_list = 'DoesNotExist'
                        if spon_cc_occu_list != 'DoesNotExist' and spon_cc_occu_list != None:
                            while(current_value_cc_rank in spon_cc_occu_list):
                                spon_cc_occu_list.remove(current_value_cc_rank)
                            spon_cc_occu_list.sort()
                            spon_cc_occu_obj.ranklist = spon_cc_occu_list
                            spon_cc_occu_obj.save()

                if Spon_CLC_KEY_list[i].lower() != "novalue" and Spon_CLC_RANK_list[i].lower() != "novalue":
                    current_value_clc_rank = livedoc.sponsored_rank['CLC_RANK_list'].get(Spon_CLC_KEY_list[i],None)
                    tt = None
                    tt = Spon_CLC_RANK_list[i]
                    if tt.isdigit() and int(Spon_CLC_RANK_list[i]) == 0:
                        livedoc.sponsored_rank['CLC_RANK_list'][Spon_CLC_KEY_list[i]] = int(Spon_CLC_RANK_list[i])
                        spon_clc_occu_list = None
                        try:
                            spon_clc_occu_obj = spons_occupied_clc_ranks.objects.get(key=Spon_CLC_KEY_list[i])
                            spon_clc_occu_list = spon_clc_occu_obj.ranklist
                            spon_clc_occu_list.sort()
                        except:
                            spon_clc_occu_list = 'DoesNotExist'
                        if spon_clc_occu_list != 'DoesNotExist' and spon_clc_occu_list != None:
                            while(current_value_clc_rank in spon_clc_occu_list):
                                spon_clc_occu_list.remove(current_value_clc_rank)
                            spon_clc_occu_list.sort()
                            spon_clc_occu_obj.ranklist = spon_clc_occu_list
                            spon_clc_occu_obj.save()
                livedoc.save()
        except Exception as e:
            error_msg = e
        if error_msg == None :
            error_msg = 'Successfully Updated Sponsored Ranks'
        return HttpResponse(json.dumps({"Redirect": False, "Message": error_msg}))
    except Exception as e:
        return HttpResponse(json.dumps({"Redirect": False, "Message": e}))


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%






####################################################################
# Name - doctor_mark_for_search_results                            #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def doctor_mark_for_search_results(request):
    try:
        country_data = Country.objects.filter(delete=False)
        state_master_obj = State.objects.filter(delete=False)
        category_obj = Category.objects.filter(delete=False).order_by('name')

        return render(request, 'admin/doctor_management/doctor_mark_for_search_results.html',
            {'tab': 'data', 'tab_listing': 'doctor_listing','country':country_data,
            'state':state_master_obj,'category_obj': category_obj,
            'doctors':None})

    except Exception as e:
        raise Http404

####################################################################
# Name - get_doctors_for_search_results                            #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def get_doctors_for_search_results(request):
    try:
        country_id = request.POST.get('formDATA[country_id]')
        test =  request.POST.get('formDATA[country_id]')
        state_id = request.POST.get('formDATA[state_id]')
        city_id = request.POST.get('formDATA[city_id]')
        locality_id = request.POST.get('formDATA[locality_id]')
        category_id = request.POST.get('formDATA[category_id]')

        # country_data = Country.objects.filter(delete=False)
        # state_master_obj = State.objects.filter(delete=False)
        # category_obj = Category.objects.filter(delete=False).order_by('name')
        orgs_id_list = []
        docs_id_list = []
        schedules_list = []
        send_list = []
        Locality_selected = 'NA'
        if country_id != '' and state_id != '' and city_id != '' and category_id != '':

            if locality_id == '' :
                orgs_id_list = OrganisationName.objects.filter(country_id=int(country_id),state_id=int(state_id),city_id=int(city_id)).values_list('id',flat=True)
                docs_id_list = Doctor.objects.filter(category=int(category_id)).values_list('id',flat=True)
                schedules_list = AttachWithDoctor.objects.filter(doctor_id__in = docs_id_list,organisation_id__in=orgs_id_list)
                Key_CC_RANK = city_id + '-' + category_id
                for schs in schedules_list:
                    ddoctors = Doctor.objects.get(id=schs.doctor_id)
                    Org = OrganisationName.objects.get(id = schs.organisation_id)
                    Key_CC_RANK =  str(Org.city_id)+'-'+str(ddoctors.category_id)
                    if send_list != []:
                        temp_map = map(lambda x: x[0],send_list)
                        if ddoctors not in temp_map:
                            #send_list.append([ddoctors,Org,schs.id,[ddoctors.sponsored_rank['CC_RANK_list'].get(Key_CC_RANK,''),ddoctors.subscribed_rank['CC_RANK_list'].get(Key_CC_RANK,''),ddoctors.trial_rank['CC_RANK_list'].get(Key_CC_RANK,'')],ddoctors.name])
                            send_list.append([ddoctors,Org,schs.id,[ddoctors.sponsored_rank['CC_RANK_list'].get(Key_CC_RANK,'')],ddoctors.name,ddoctors.sponsored_start_dates.get(Key_CC_RANK,'NA'),ddoctors.sponsored_end_dates.get(Key_CC_RANK,'NA')])
                    else:
                        #send_list.append([ddoctors,Org,schs.id,[ddoctors.sponsored_rank['CC_RANK_list'].get(Key_CC_RANK,''),ddoctors.subscribed_rank['CC_RANK_list'].get(Key_CC_RANK,''),ddoctors.trial_rank['CC_RANK_list'].get(Key_CC_RANK,'')],ddoctors.name])
                        send_list.append([ddoctors,Org,schs.id,[ddoctors.sponsored_rank['CC_RANK_list'].get(Key_CC_RANK,'')],ddoctors.name,ddoctors.sponsored_start_dates.get(Key_CC_RANK,'NA'),ddoctors.sponsored_end_dates.get(Key_CC_RANK,'NA')])
                send_list.sort(key=lambda x: x[4])
                Locality_selected = False
                try:
                    occupied_values_spons = spons_occupied_cc_ranks.objects.get(key=Key_CC_RANK).ranklist
                    if occupied_values_spons == []:
                        occupied_values_spons = ''
                    elif occupied_values_spons != None and occupied_values_spons != []:
                        occupied_values_spons = ",".join([str(iii) for iii in occupied_values_spons])
                except Exception as e:
                    occupied_values_spons = ''


            elif locality_id != '' :
                orgs_id_list = OrganisationName.objects.filter(country_id=int(country_id), state_id=int(state_id),
                                                               city_id=int(city_id),locality_id=int(locality_id)).values_list('id', flat=True)
                docs_id_list = Doctor.objects.filter(category=int(category_id)).values_list('id', flat=True)
                schedules_list = AttachWithDoctor.objects.filter(doctor_id__in=docs_id_list,
                                                                 organisation_id__in=orgs_id_list)
                Key_CLC_RANK = city_id + '-' + locality_id + '-' + category_id
                for schs in schedules_list:
                    ddoctors = Doctor.objects.get(id=schs.doctor_id)
                    Org = OrganisationName.objects.get(id=schs.organisation_id)
                    Key_CLC_RANK = str(Org.city_id) + '-' + str(Org.locality_id) + '-' + str(ddoctors.category_id)
                    if send_list != []:
                        temp_map = map(lambda x: x[0],send_list)
                        if ddoctors not in temp_map:
                            #send_list.append([ddoctors, Org, schs.id,[ddoctors.sponsored_rank['CLC_RANK_list'].get(Key_CLC_RANK,''),ddoctors.subscribed_rank['CLC_RANK_list'].get(Key_CLC_RANK,''),ddoctors.trial_rank['CLC_RANK_list'].get(Key_CLC_RANK,'')],ddoctors.name])
                            send_list.append([ddoctors, Org, schs.id,[ddoctors.sponsored_rank['CLC_RANK_list'].get(Key_CLC_RANK,'')],ddoctors.name,ddoctors.sponsored_start_dates.get(Key_CLC_RANK,'NA'),ddoctors.sponsored_end_dates.get(Key_CLC_RANK,'NA')])
                    else:
                        #send_list.append([ddoctors,Org,schs.id,[ddoctors.sponsored_rank['CLC_RANK_list'].get(Key_CLC_RANK,''),ddoctors.subscribed_rank['CLC_RANK_list'].get(Key_CLC_RANK,''),ddoctors.trial_rank['CLC_RANK_list'].get(Key_CLC_RANK,'')],ddoctors.name])
                        send_list.append([ddoctors,Org,schs.id,[ddoctors.sponsored_rank['CLC_RANK_list'].get(Key_CLC_RANK,'')],ddoctors.name,ddoctors.sponsored_start_dates.get(Key_CLC_RANK,'NA'),ddoctors.sponsored_end_dates.get(Key_CLC_RANK,'NA')])
                send_list.sort(key=lambda x: x[4])
                Locality_selected = True
                try:
                    occupied_values_spons = spons_occupied_clc_ranks.objects.get(key=Key_CLC_RANK).ranklist
                    if occupied_values_spons == []:
                        occupied_values_spons = ''
                    elif occupied_values_spons != None and occupied_values_spons != []:
                        occupied_values_spons = ",".join([str(iii) for iii in occupied_values_spons])
                except Exception as e:
                    occupied_values_spons = ''

            if locality_id != '':
                tyyype = 'CLC'
                kkeeyy = Key_CLC_RANK
            else:
                tyyype = 'CC'
                kkeeyy = Key_CC_RANK
            occupied_values_obj = {'type': tyyype, 'key': kkeeyy, 'occupied_values_spons': occupied_values_spons}


        else:
            messages.error(request,"City and Category are required")
            response = {"Message":"City and Category are required","Redirect":False}
            return HttpResponse(json.dumps(response))

        html = render_to_string('admin/doctor_management/get_doctor_for_search_results.html',
                                {'send_list':send_list,'Locality_selected':Locality_selected,'occupied_values_obj':occupied_values_obj})

        return HttpResponse(html)

    except Exception as e:
        raise Http404


####################################################################
# Name - save_doctor_rank                                          #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def save_doctor_rank(request):
     try:
        formDATA = request.POST.get('formDATA')
        type = request.POST.get('formDATA[TYPE]')
        checkedValues = request.POST.get('formDATA[checkedValues]')
        checkedValues = checkedValues.split(',')

        if type == 'CC':
            Spon_CC_RANK_list = request.POST.get('formDATA[Spon_CC_RANK_list]')
            Spon_CC_RANK_list = Spon_CC_RANK_list.split(',')

            Spon_CC_RANK_StartDate = request.POST.get('formDATA[Spon_CC_RANK_StartDate]')
            Spon_CC_RANK_StartDate = Spon_CC_RANK_StartDate.split(',')
            Spon_CC_RANK_EndDate = request.POST.get('formDATA[Spon_CC_RANK_EndDate]')
            Spon_CC_RANK_EndDate = Spon_CC_RANK_EndDate.split(",")

            #Subs_CC_RANK_list = request.POST.get('formDATA[Subs_CC_RANK_list]')
            #Subs_CC_RANK_list = Subs_CC_RANK_list.split(',')


        elif type == 'CLC':
            Spon_CLC_RANK_list = request.POST.get('formDATA[Spon_CLC_RANK_list]')
            Spon_CLC_RANK_list = Spon_CLC_RANK_list.split(',')

            Spon_CLC_RANK_StartDate = request.POST.get('formDATA[Spon_CLC_RANK_StartDate]')
            Spon_CLC_RANK_StartDate = Spon_CLC_RANK_StartDate.split(',')
            Spon_CLC_RANK_EndDate = request.POST.get('formDATA[Spon_CLC_RANK_EndDate]')
            Spon_CLC_RANK_EndDate = Spon_CLC_RANK_EndDate.split(",")

            #Subs_CLC_RANK_list = request.POST.get('formDATA[Subs_CLC_RANK_list]')
            #Subs_CLC_RANK_list = Subs_CLC_RANK_list.split(',')


        spons_json= {}
        #subs_json= {}
        cat_id = city_id = None
        key = None
        error_msg=[]
        sponsored_keys = None
        #subscribed_keys = None

        if type == 'CC':
            #if Spon_CC_RANK_list != [''] and Subs_CC_RANK_list != [''] and (len(Spon_CC_RANK_list) == len(Subs_CC_RANK_list) == len(checkedValues)):
            if Spon_CC_RANK_list != [''] and (len(Spon_CC_RANK_list) == len(checkedValues)):
                for i in range(0,len(checkedValues)):
                    ddoc = Doctor.objects.get(id= AttachWithDoctor.objects.get(id=int(checkedValues[i])).doctor_id)
                    cat_id = ddoc.category_id
                    city_id = OrganisationName.objects.get(id = AttachWithDoctor.objects.get(id=int(checkedValues[i])).organisation_id).city_id
                    key = str(city_id)+'-'+str(cat_id)
                    ddoc.sponsored_start_dates[key] = Spon_CC_RANK_StartDate[i]
                    ddoc.sponsored_end_dates[key] = Spon_CC_RANK_EndDate[i]

                    # occu_ranks = Occupied_ranks.objects.all()
                    # if list(occu_ranks) == []:
                    #     Occupied_ranks.objects.create()
                    #     occu_ranks = Occupied_ranks.objects.all()
                    #
                    # sponsored_keys = occu_ranks[0].doctor['CC']['Sponsored'].keys()
                    #subscribed_keys = occu_ranks[0].doctor['CC']['Subscribed'].keys()

                    ################ SPONSORED CHECK ################################
                    spon_cc_occu_list = None
                    try:
                        spon_cc_occu_obj = spons_occupied_cc_ranks.objects.get(key=key)
                        spon_cc_occu_list = spon_cc_occu_obj.ranklist
                        spon_cc_occu_list.sort()
                    except:
                        spon_cc_occu_list = 'DoesNotExist'
                    #occupied_values = None
                    #if key in sponsored_keys:
                    if spon_cc_occu_list != 'DoesNotExist' and spon_cc_occu_list != None:
                        #occupied_values = occu_ranks[0].doctor['CC']['Sponsored'][key]
                        current_value =  ddoc.sponsored_rank['CC_RANK_list'].get(key, 'Notfound')
                        if current_value != int(Spon_CC_RANK_list[i]):
                            #if int(Spon_CC_RANK_list[i]) in occupied_values :
                            if int(Spon_CC_RANK_list[i]) in spon_cc_occu_list:
                                msg = "CC Sponsored Rank "+Spon_CC_RANK_list[i]+" Already Occupied (Now set to 9999) - Tried For Dr."+ ddoc.name+"\n"
                                error_msg.append(msg)

                                # since system is itself setting the rank of doc to 9999, we will
                                # make the system delete the current rank from occupied ranks too
                                # if it exists there
                                while (current_value in spon_cc_occu_list):
                                    spon_cc_occu_list.remove(current_value)
                                spon_cc_occu_list.sort()
                                spon_cc_occu_obj.ranklist = spon_cc_occu_list
                                spon_cc_occu_obj.save()

                                msg = None
                                # Mark the rank as 9999 showing Not set
                                ddoc.sponsored_rank['CC_RANK_list'][key] = 9999
                                # Do not save in accupied ranks

                            elif int(Spon_CC_RANK_list[i]) == 9999 or int(Spon_CC_RANK_list[i]) == 0:
                                # Mark the rank as 9999 showing Not set or as 0 showing no rank
                                # Do not save in accupied ranks
                                ddoc.sponsored_rank['CC_RANK_list'][key] = int(Spon_CC_RANK_list[i])
                                if current_value != 'Notfound':
                                    # Delete from occupied ranks
                                    while current_value in spon_cc_occu_list:
                                        spon_cc_occu_list.remove(current_value)
                                    spon_cc_occu_list.sort()
                                    spon_cc_occu_obj.ranklist = spon_cc_occu_list
                                    spon_cc_occu_obj.save()
                            else:
                                if current_value != 'Notfound':
                                    # Delete from occupied ranks
                                    while current_value in spon_cc_occu_list:
                                        spon_cc_occu_list.remove(current_value)
                                    spon_cc_occu_list.sort()
                                # Save the rank
                                ddoc.sponsored_rank['CC_RANK_list'][key] = int(Spon_CC_RANK_list[i])
                                #occu_ranks[0].doctor['CC']['Sponsored'][key].append(int(Spon_CC_RANK_list[i]))
                                #occu_ranks[0].save()
                                spon_cc_occu_list.append(int(Spon_CC_RANK_list[i]))
                                spon_cc_occu_list.sort()
                                spon_cc_occu_obj.ranklist = spon_cc_occu_list
                                spon_cc_occu_obj.save()
                        else:
                            if current_value != 9999 and current_value != 0:
                                if current_value not in spon_cc_occu_list:
                                    spon_cc_occu_list.append(current_value)
                                    spon_cc_occu_list.sort()
                                    spon_cc_occu_obj.ranklist = spon_cc_occu_list
                                    spon_cc_occu_obj.save()
                    else:
                        #EVEN if rank value is 9999 or 0, we assign this rank value to doctor's  Spon >  cc rank
                        ddoc.sponsored_rank['CC_RANK_list'][key] = int(Spon_CC_RANK_list[i])
                        #BUT IF value isd 9999 or 0 we don't add it to the accupied ranks
                        if int(Spon_CC_RANK_list[i])!= 9999 and int(Spon_CC_RANK_list[i]) != 0 :
                            #occu_ranks[0].doctor['CC']['Sponsored'][key]=[int(Spon_CC_RANK_list[i])]
                            #occu_ranks[0].save()
                            new_spon_cc_occu_obj = spons_occupied_cc_ranks.objects.create(key=key, ranklist=[int(Spon_CC_RANK_list[i])])

                    ###########################SUBSCRIBED CHECK ###################
                    #
                    # occupied_values = None
                    # if key in subscribed_keys:
                    #     occupied_values = occu_ranks[0].doctor['CC']['Subscribed'][key]
                    #     current_value =   ddoc.subscribed_rank['CC_RANK_list'].get(key, 'Notfound')
                    #     if current_value != int(Subs_CC_RANK_list[i]):
                    #         if int(Subs_CC_RANK_list[i]) in occupied_values:
                    #             msg = "CC Subscribed Rank " + Subs_CC_RANK_list[
                    #                 i] + " Already Occupied (Now set to 9999) - Tried For Dr." + ddoc.name + "\n"
                    #             error_msg.append(msg)
                    #             msg = None
                    #             # Mark the rank as 9999 showing Not set
                    #             ddoc.subscribed_rank['CC_RANK_list'][key] = 9999
                    #             # Do not save in accupied ranks
                    #
                    #         elif int(Subs_CC_RANK_list[i]) == 9999 or int(Subs_CC_RANK_list[i]) == 0:
                    #             # Mark the rank as 9999 showing Not set or as 0 showing no rank
                    #             ddoc.subscribed_rank['CC_RANK_list'][key] = int(Subs_CC_RANK_list[i])
                    #             # Do not save in accupied ranks
                    #         else:
                    #             # Save the rank
                    #             ddoc.subscribed_rank['CC_RANK_list'][key] = int(Subs_CC_RANK_list[i])
                    #             occu_ranks[0].doctor['CC']['Subscribed'][key].append(int(Subs_CC_RANK_list[i]))
                    #             occu_ranks[0].save()
                    # else:
                    #     # EVEN if rank value is 9999 or 0, we assign this rank value to doctor's  Spon >  cc rank
                    #     ddoc.subscribed_rank['CC_RANK_list'][key] = int(Subs_CC_RANK_list[i])
                    #     # BUT IF value isd 9999 or 0 we don't add it to the accupied ranks
                    #     if int(Subs_CC_RANK_list[i]) != 9999 and int(Subs_CC_RANK_list[i]) != 0:
                    #         occu_ranks[0].doctor['CC']['Subscribed'][key] = [int(Subs_CC_RANK_list[i])]
                    #         occu_ranks[0].save()


                    ##############################################

                    # SAVE THE DOCTOR. WHAT EVER THE RANK VALUES BE, THESE HAVE BEEN SAVED INSIDE THE DOCTOR,TO
                    # BE PUBLISHED WITH THE DOCTOR
                    ddoc.save()

                if error_msg == [] :
                    Messagee = 'Successfully Updated CC Ranks'
                else:
                    Messagee =  " --- ".join(error_msg)
                return HttpResponse(json.dumps({"Redirect": False, "Message": Messagee}))

            else:
                #messages.error(request, "Missing Rank Values in Checked Rows")
                #return reverse('live-doc-mark-for-search-results')
                return HttpResponse(json.dumps({"Redirect": False, "Message": "Missing Rank Values in Checked Rows"}))

        elif type == 'CLC':
            #if Spon_CLC_RANK_list != [''] and Subs_CLC_RANK_list != [''] and (len(Spon_CLC_RANK_list) == len(Subs_CLC_RANK_list) == len(checkedValues)):
            if Spon_CLC_RANK_list != [''] and (len(Spon_CLC_RANK_list) == len(checkedValues)):
                for i in range(0,len(checkedValues)):
                    ddoc = Doctor.objects.get(id=AttachWithDoctor.objects.get(id=int(checkedValues[i])).doctor_id)
                    cat_id = ddoc.category_id
                    city_id = OrganisationName.objects.get(id=AttachWithDoctor.objects.get(id=int(checkedValues[i])).organisation_id).city_id
                    locality_id = OrganisationName.objects.get(id=AttachWithDoctor.objects.get(id=int(checkedValues[i])).organisation_id).locality_id
                    key = str(city_id) + '-' +str(locality_id) +'-'+ str(cat_id)
                    ddoc.sponsored_start_dates[key] = Spon_CLC_RANK_StartDate[i]
                    ddoc.sponsored_end_dates[key] = Spon_CLC_RANK_EndDate[i]

                    # occu_ranks = Occupied_ranks.objects.all()
                    # if list(occu_ranks) == []:
                    #     Occupied_ranks.objects.create()
                    #     occu_ranks = Occupied_ranks.objects.all()
                    #
                    # sponsored_keys = occu_ranks[0].doctor['CLC']['Sponsored'].keys()
                    # subscribed_keys = occu_ranks[0].doctor['CLC']['Subscribed'].keys()

                    ################ SPONSORED CHECK ################################
                    spon_clc_occu_list = None
                    try:
                        spon_clc_occu_obj = spons_occupied_clc_ranks.objects.get(key=key)
                        spon_clc_occu_list = spon_clc_occu_obj.ranklist
                        spon_clc_occu_list.sort()
                    except:
                        spon_clc_occu_list = 'DoesNotExist'

                    #occupied_values = None
                    #if key in sponsored_keys:
                    if spon_clc_occu_list != 'DoesNotExist' and spon_clc_occu_list != None:
                        #occupied_values = occu_ranks[0].doctor['CLC']['Sponsored'][key]
                        current_value =  ddoc.sponsored_rank['CLC_RANK_list'].get(key, 'Notfound')
                        if current_value != int(Spon_CLC_RANK_list[i]):
                            #if int(Spon_CLC_RANK_list[i]) in occupied_values:
                            if int(Spon_CLC_RANK_list[i]) in spon_clc_occu_list:
                                msg = "CLC Sponsored Rank " + Spon_CLC_RANK_list[
                                    i] + " Already Occupied (Now set to 9999) - Tried For Dr." + ddoc.name + "\n"
                                error_msg.append(msg)

                                # since system is itself setting the rank of doc to 9999, we will
                                # make the system delete the current rank from occupied ranks too
                                # if it exists there
                                while (current_value in spon_clc_occu_list):
                                    spon_clc_occu_list.remove(current_value)
                                    spon_clc_occu_list.sort()
                                spon_clc_occu_obj.ranklist = spon_clc_occu_list
                                spon_clc_occu_obj.save()

                                msg = None
                                # Mark the rank as 9999 showing Not set
                                ddoc.sponsored_rank['CLC_RANK_list'][key] = 9999
                                # Do not save in accupied ranks

                            elif int(Spon_CLC_RANK_list[i]) == 9999 or int(Spon_CLC_RANK_list[i]) == 0:
                                # Mark the rank as 9999 showing Not set or as 0 showing no rank
                                # Do not save in accupied ranks
                                ddoc.sponsored_rank['CLC_RANK_list'][key] = int(Spon_CLC_RANK_list[i])
                                if current_value != 'Notfound':
                                    # Delete from occupied ranks
                                    while current_value in spon_clc_occu_list:
                                        spon_clc_occu_list.remove(current_value)
                                    spon_clc_occu_list.sort()
                                    spon_clc_occu_obj.ranklist = spon_clc_occu_list
                                    spon_clc_occu_obj.save()

                            else:
                                if current_value != 'Notfound':
                                    # Delete from occupied ranks
                                    while current_value in spon_clc_occu_list:
                                        spon_clc_occu_list.remove(current_value)
                                    spon_clc_occu_list.sort()
                                # Save the rank
                                ddoc.sponsored_rank['CLC_RANK_list'][key] = int(Spon_CLC_RANK_list[i])
                                # occu_ranks[0].doctor['CLC']['Sponsored'][key].append(int(Spon_CLC_RANK_list[i]))
                                # occu_ranks[0].save()
                                spon_clc_occu_list.append(int(Spon_CLC_RANK_list[i]))
                                spon_clc_occu_list.sort()
                                spon_clc_occu_obj.ranklist = spon_clc_occu_list
                                spon_clc_occu_obj.save()
                        else:
                            if current_value != 9999 and current_value != 0:
                                if current_value not in spon_clc_occu_list:
                                    spon_clc_occu_list.append(current_value)
                                    spon_clc_occu_list.sort()
                                    spon_clc_occu_obj.ranklist = spon_clc_occu_list
                                    spon_clc_occu_obj.save()

                    else:
                        # EVEN if rank value is 9999 or 0, we assign this rank value to doctor's  Spon >  clc rank
                        ddoc.sponsored_rank['CLC_RANK_list'][key] = int(Spon_CLC_RANK_list[i])
                        # BUT IF value isd 9999 or 0 we don't add it to the accupied ranks
                        if int(Spon_CLC_RANK_list[i]) != 9999 and int(Spon_CLC_RANK_list[i]) != 0:
                            #occu_ranks[0].doctor['CLC']['Sponsored'][key] = [int(Spon_CLC_RANK_list[i])]
                            #occu_ranks[0].save()
                            new_spons_clc_occu_obj = spons_occupied_clc_ranks.objects.create(key=key, ranklist=[int(Spon_CLC_RANK_list[i])])

                    ###########################SUBSCRIBED CHECK ###################
                    #
                    # occupied_values = None
                    # if key in subscribed_keys:
                    #     occupied_values = occu_ranks[0].doctor['CLC']['Subscribed'][key]
                    #     current_value =  ddoc.subscribed_rank['CLC_RANK_list'].get(key, 'Notfound')
                    #     if current_value != int(Subs_CLC_RANK_list[i]):
                    #         if int(Subs_CLC_RANK_list[i]) in occupied_values:
                    #             msg = "CLC Subscribed Rank " + Subs_CLC_RANK_list[
                    #                 i] + " Already Occupied (Now set to 9999) - Tried For Dr." + ddoc.name + "\n"
                    #             error_msg.append(msg)
                    #             msg = None
                    #             # Mark the rank as 9999 showing Not set
                    #             ddoc.subscribed_rank['CLC_RANK_list'][key] = 9999
                    #             # Do not save in accupied ranks
                    #
                    #         elif int(Subs_CLC_RANK_list[i]) == 9999 or int(Subs_CLC_RANK_list[i]) == 0:
                    #             # Mark the rank as 9999 showing Not set or as 0 showing no rank
                    #             ddoc.subscribed_rank['CLC_RANK_list'][key] = int(Subs_CLC_RANK_list[i])
                    #             # Do not save in accupied ranks
                    #         else:
                    #             # Save the rank
                    #             ddoc.subscribed_rank['CLC_RANK_list'][key] = int(Subs_CLC_RANK_list[i])
                    #             occu_ranks[0].doctor['CLC']['Subscribed'][key].append(int(Subs_CLC_RANK_list[i]))
                    #             occu_ranks[0].save()
                    # else:
                    #     # EVEN if rank value is 9999 or 0, we assign this rank value to doctor's  Spon >  cc rank
                    #     ddoc.subscribed_rank['CLC_RANK_list'][key] = int(Subs_CLC_RANK_list[i])
                    #     # BUT IF value isd 9999 or 0 we don't add it to the accupied ranks
                    #     if int(Subs_CLC_RANK_list[i]) != 9999 and int(Subs_CLC_RANK_list[i]) != 0:
                    #         occu_ranks[0].doctor['CLC']['Subscribed'][key] = [int(Subs_CLC_RANK_list[i])]
                    #         occu_ranks[0].save()
                    #
                    ##############################################

                    # SAVE THE DOCTOR. WHAT EVER THE RANK VALUES BE, THESE HAVE BEEN SAVED INSIDE THE DOCTOR,TO
                    # BE PUBLISHED WITH THE DOCTOR
                    ddoc.save()
                if error_msg == [] :
                    Messagee = 'Successfully Updated CLC Ranks'
                else:
                    Messagee =  " --- ".join(error_msg)
                return HttpResponse(json.dumps({"Redirect": False, "Message": Messagee}))
            else:
                #messages.error(request, "Missing Rank Values in Checked Rows")
                #return reverse('live-doc-mark-for-search-results')
                return HttpResponse(json.dumps({"Redirect": False, "Message": "Missing Rank Values in Checked Rows"}))
        else:
            #messages.error(request, "No Rank Values Provided")
            MYMSG = json.dumps({"Redirect":False,"Message":"No Rank Values Provided"})
            return  HttpResponse(MYMSG)
        #return  {"Redirect": False, "Message": "Rank Data Successfully Saved"}


     except Exception as e:
        raise Http404

####################################################################
# Name - organisation_profile_image                                #
# Owner - Dhrumil Shah                                             #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def organisation_profile_image(request, org_id=None):
    try:
        if org_id:
            try:
                org_obj = OrganisationName.objects.get(id=int(org_id))
                if len(request.FILES) == 1:
                    file = request.FILES['OrgProfileImage']
                    file_name = request.FILES['OrgProfileImage'].name
                    global hostname
                    global port
                    url_p3 = "/api/v2/clinic/add_profile_picture/"
                    global authToken
                    org_id = str(org_id) + '/'

                    urlc = hostname + port + url_p3 + authToken + '/' + org_id
                    import requests
                    url = urlc
                    from django.core.files.storage import FileSystemStorage
                    filepath = settings.DOC_PROFILE + '/' + file_name
                    fs = FileSystemStorage()
                    filename = fs.save(filepath, file)
                    uploaded_file_url = fs.url(filename)
                    print uploaded_file_url

                    try:
                        headers = {
                            'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0',
                            'hit_from': 'CMS'}
                        with open(filepath, "rb") as image_file:
                            # print ">>>>>>>>>   ", type(image_file), "   <<<<<<<<<<<<<<<<<"
                            files = {'uploadFile': image_file}
                            r = requests.post(url, data={'hit_from': 'CMS'}, files=files)
                            if r.status_code == 200 or r.status_code == '200':
                                messages.success(request, "Successfully Uploaded Profile Image")
                                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                            else:
                                messages.error(request, "Profile Image Upload Failed")
                                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                    except Exception as e:
                        messages.error(request, e)
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except Exception as e:
                messages.error(request, e)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, "Organisation ID Not Provided")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




####################################################################
# Name - set_live_doctor_subscribed_ranks                          #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def set_live_doctor_subscribed_ranks(request,doctor_id=None):
     try:
        if doctor_id != None:
            try:
                live_doc_objj = Live_Doctor.objects.get(id = doctor_id)
            except:
                messages.error(request, "Doctor Not Found in DB")
                return redirect('live_doctor_assignment')
            if live_doc_objj and live_doc_objj.category != None and live_doc_objj.category != '':
                chkbbxk = request.POST.get('Subschkbox')
                if chkbbxk == None:
                    chkbbxk = 'OFFF'
                if chkbbxk == 'ONNN' and live_doc_objj.is_subscribed == True:
                    messages.error(request, "Already checked, Please uncheck first, save, recheck and save again to set new ranks")
                    return redirect( reverse('live_doctor_listing_edit',args=[int(doctor_id)])+'?tab=8')
                elif chkbbxk == 'ONNN' and live_doc_objj.is_subscribed == False:
                    schedules_list = Live_Doctor_Commonworkschedule.objects.filter(doctor_id=doctor_id)
                    ccset= []
                    clcset =[]
                    chk_all_status_delete = []
                    chk_all_status_delete = [ x.status.lower() for x in schedules_list if x.status.lower() != 'delete']

                    if list(schedules_list) != [] and chk_all_status_delete != []:
                        for schs in schedules_list:
                            if schs.status.lower() != 'delete':
                                Org = OrganisationName.objects.get(id=schs.clinic_id)
                                Key_CC_RANK = str(Org.city_id) + '-' + str(live_doc_objj.category)
                                key_CLC_RANK = str(Org.city_id) + '-' + str(Org.locality_id)+'-'+ str(live_doc_objj.category)
                                if Key_CC_RANK not in ccset:
                                    ccset.append(Key_CC_RANK)
                                    try:
                                        cc_occu_obj = subs_occupied_cc_ranks.objects.get(key=Key_CC_RANK)
                                    except:
                                        cc_occu_obj = subs_occupied_cc_ranks.objects.create(key=Key_CC_RANK, ranklist=[])
                                    cc_occu_list = cc_occu_obj.ranklist
                                    if cc_occu_list == None or cc_occu_list =='':
                                        cc_occu_list = list()
                                    if cc_occu_list != []:
                                        cc_occu_list.sort()
                                        rrank = cc_occu_list[-1] + 1
                                        cc_occu_list.append(rrank)
                                    else:
                                        rrank = 1
                                        cc_occu_list.append(rrank)
                                    cc_occu_obj.ranklist = cc_occu_list
                                    cc_occu_obj.save()
                                    live_doc_objj.subscribed_rank['CC_RANK_list'][Key_CC_RANK] = rrank
                                    rrank = None
                                if key_CLC_RANK not in clcset:
                                    clcset.append(key_CLC_RANK)
                                    try:
                                        clc_occu_obj = subs_occupied_clc_ranks.objects.get(key=key_CLC_RANK)
                                    except:
                                        clc_occu_obj = subs_occupied_clc_ranks.objects.create(key=key_CLC_RANK, ranklist=[])
                                    clc_occu_list = clc_occu_obj.ranklist
                                    if clc_occu_list == None or clc_occu_list == '':
                                        clc_occu_list = list()
                                    if clc_occu_list != []:
                                        clc_occu_list.sort()
                                        rrank = clc_occu_list[-1] + 1
                                        clc_occu_list.append(rrank)
                                    else:
                                        rrank = 1
                                        clc_occu_list.append(rrank)
                                    clc_occu_obj.ranklist = clc_occu_list
                                    clc_occu_obj.save()
                                    live_doc_objj.subscribed_rank['CLC_RANK_list'][key_CLC_RANK] = rrank
                                    rrank = None
                        live_doc_objj.is_subscribed = True
                        live_doc_objj.save()
                        messages.success(request, "Successfully set Subscribed ranks")
                        return redirect(reverse('live_doctor_listing_edit', args=[int(doctor_id)]) + '?tab=8')
                    else:
                        # live_doc_objj.is_subscribed = True
                        # live_doc_objj.save()
                        messages.error(request, "Doctor Not Marked as Subscribed - No Schedule Found")
                        return redirect(reverse('live_doctor_listing_edit', args=[int(doctor_id)]) + '?tab=8')
                elif chkbbxk == 'OFFF' and live_doc_objj.is_subscribed == False:
                    messages.error(request,"Doctor Already Un-Subscribed")
                    return redirect(reverse('live_doctor_listing_edit', args=[int(doctor_id)]) + '?tab=8')
                elif chkbbxk == 'OFFF' and live_doc_objj.is_subscribed == True:
                    schedules_list = Live_Doctor_Commonworkschedule.objects.filter(doctor_id=doctor_id)
                    ccset = []
                    clcset = []
                    if schedules_list != []:
                        for schs in schedules_list:
                            if schs.status.lower() != 'delete':
                                Org = OrganisationName.objects.get(id=schs.clinic_id)
                                Key_CC_RANK = str(Org.city_id) + '-' + str(live_doc_objj.category)
                                key_CLC_RANK = str(Org.city_id) + '-' + str(Org.locality_id) + '-' + str(live_doc_objj.category)

                                if Key_CC_RANK not in ccset:
                                    ccset.append(Key_CC_RANK)
                                    delccrank = live_doc_objj.subscribed_rank['CC_RANK_list'].get(Key_CC_RANK,None)
                                    if delccrank != None:
                                        del live_doc_objj.subscribed_rank['CC_RANK_list'][Key_CC_RANK]
                                        cc_occu_obj = subs_occupied_cc_ranks.objects.get(key=Key_CC_RANK)
                                        cc_occu_list = cc_occu_obj.ranklist
                                        if delccrank in cc_occu_list:
                                            cc_occu_list.remove(delccrank)
                                        cc_occu_list.sort()
                                        cc_occu_obj.ranklist = cc_occu_list
                                        cc_occu_obj.save()
                                    delccrank = None
                                if key_CLC_RANK not in clcset:
                                    clcset.append(key_CLC_RANK)
                                    delclcrank = live_doc_objj.subscribed_rank['CLC_RANK_list'].get(key_CLC_RANK, None)
                                    if delclcrank != None:
                                        del live_doc_objj.subscribed_rank['CLC_RANK_list'][key_CLC_RANK]
                                        clc_occu_obj = subs_occupied_clc_ranks.objects.get(key=key_CLC_RANK)
                                        clc_occu_list = clc_occu_obj.ranklist
                                        if delclcrank in clc_occu_list:
                                            clc_occu_list.remove(delclcrank)
                                        clc_occu_list.sort()
                                        clc_occu_obj.ranklist = clc_occu_list
                                        clc_occu_obj.save()
                                    delclcrank = None
                        live_doc_objj.is_subscribed = False
                        live_doc_objj.save()
                        messages.success(request, "Successfully Un-Subscribed ranks")
                        return redirect(reverse('live_doctor_listing_edit', args=[int(doctor_id)]) + '?tab=8')
                    else:
                        live_doc_objj.is_subscribed = False
                        live_doc_objj.save()
                        messages.success(request, "Doctor Marked as Un-Subscribed")
                        messages.error(request, "But No Schedule Found")
                        return redirect(reverse('live_doctor_listing_edit', args=[int(doctor_id)]) + '?tab=8')
            else:
                messages.error(request, "Doctor Category Missing")
                return redirect(reverse('live_doctor_listing_edit', args=[int(doctor_id)]) + '?tab=8')
        else:
            messages.error(request,"Doctor ID Not Provided")
            return redirect('live_doctor_assignment')
     except Exception as e:
        messages.error(request, e)
        return redirect(reverse('live_doctor_listing_edit', args=[int(doctor_id)]) + '?tab=8')



####################################################################
# Name - update_occupied_ranks                                     #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def update_occupied_ranks(request):
    try:
        if request.method == 'POST':
            occupied_values_subs = request.POST["formDATA[occupied_values_subs]"]
            occupied_values_spons = request.POST["formDATA[occupied_values_spons]"]
            typpe = request.POST.get('formDATA[type]')
            key = request.POST.get('formDATA[key]')
            message = None
            if key == None or key == '' or key == ' ':
                message = "Valid "+typpe+" Key required"
                return HttpResponse(json.dumps({"ssuccess":"No","message":message}))

            if typpe == 'CC':
                if occupied_values_subs == [] or occupied_values_subs == '' or occupied_values_subs == None:
                    occupied_values_subs = []
                else:
                    occupied_values_subs = occupied_values_subs.split(',')
                    occupied_values_subs = set(occupied_values_subs)
                    occupied_values_subs = list(occupied_values_subs)
                    occupied_values_subs = [int(elem) for elem in occupied_values_subs]
                    if 0 in occupied_values_subs:
                        occupied_values_subs.remove(0)
                    if 9999 in  occupied_values_subs:
                        occupied_values_subs.remove(9999)
                    occupied_values_subs.sort()
                try:
                    subs_obj = subs_occupied_cc_ranks.objects.get(key=key)
                    subs_obj.ranklist = occupied_values_subs
                    subs_obj.save()
                    message = "Subscribed Ranks Successfully Updated "
                except:
                    message = "Subscribed Rank Object not Found"
                    #return HttpResponse(json.dumps({"ssuccess": "No", "message": message}))

                if occupied_values_spons == [] or occupied_values_spons == '' or occupied_values_spons == None:
                    occupied_values_spons = []
                else:
                    occupied_values_spons =  occupied_values_spons.split(',')
                    occupied_values_spons =  set(occupied_values_spons)
                    occupied_values_spons =  list(occupied_values_spons)
                    occupied_values_spons =  [int(elem) for elem in occupied_values_spons]
                    if 0 in occupied_values_spons:
                        occupied_values_spons.remove(0)
                    if 9999 in occupied_values_spons:
                        occupied_values_spons.remove(9999)
                    occupied_values_spons.sort()
                try:
                    spons_obj = spons_occupied_cc_ranks.objects.get(key=key)
                    spons_obj.ranklist = occupied_values_spons
                    spons_obj.save()
                    message = message + "Sponsored Ranks Successfully Updated "
                    return HttpResponse(json.dumps({"ssuccess": "Yes", "message": message}))
                except:
                    message =  message + "Sponsored Rank Object not Found"
                    return HttpResponse(json.dumps({"ssuccess": "No", "message": message}))
            elif typpe == 'CLC':
                if occupied_values_subs == [] or occupied_values_subs == '' or occupied_values_subs == None:
                    occupied_values_subs = []
                else:
                    occupied_values_subs =  occupied_values_subs.split(',')
                    occupied_values_subs =  set(occupied_values_subs)
                    occupied_values_subs =  list(occupied_values_subs)
                    occupied_values_subs =  [int(elem) for elem in occupied_values_subs]
                    while 0 in occupied_values_subs:
                        occupied_values_subs.remove(0)
                    while 9999 in occupied_values_subs:
                        occupied_values_subs.remove(9999)
                    occupied_values_subs.sort()
                try:
                    subs_obj = subs_occupied_clc_ranks.objects.get(key=key)
                    subs_obj.ranklist = occupied_values_subs
                    subs_obj.save()
                    message = "Subscribed Ranks Successfully Updated "
                except:
                    message = "Subscribed Rank Object not Found"
                    #return HttpResponse(json.dumps({"ssuccess": "No", "message": message}))

                if occupied_values_spons == [] or occupied_values_spons == '' or occupied_values_spons == None:
                    occupied_values_spons = []
                else:
                    occupied_values_spons =  occupied_values_spons.split(',')
                    occupied_values_spons =  set(occupied_values_spons)
                    occupied_values_spons =  list(occupied_values_spons)
                    occupied_values_spons =  [int(elem) for elem in occupied_values_spons]
                    while 0 in occupied_values_spons:
                        occupied_values_spons.remove(0)
                    while 9999 in occupied_values_spons:
                        occupied_values_spons.remove(9999)
                    occupied_values_spons.sort()
                try:
                    spons_obj = spons_occupied_clc_ranks.objects.get(key=key)
                    spons_obj.ranklist = occupied_values_spons
                    spons_obj.save()
                    message = message + "Sponsored Ranks Successfully Updated "
                    return HttpResponse(json.dumps({"ssuccess": "Yes", "message": message}))
                except:
                    message =  message + "Sponsored Rank Object not Found"
                    return HttpResponse(json.dumps({"ssuccess": "No", "message": message}))
        else:
            message = request.mothod+ " method not allowed"
            return HttpResponse({"ssuccess": "No", "Message": message})
    except Exception as e:
        message = e
        return HttpResponse({"ssuccess": "No", "Message": message})


####################################################################
# Name - update_doctor_occupied_ranks                              #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def update_doctor_occupied_ranks(request):
    try:
        if request.method == 'POST':
            #occupied_values_subs = request.POST["formDATA[occupied_values_subs]"]
            occupied_values_spons = request.POST["formDATA[occupied_values_spons]"]
            typpe = request.POST.get('formDATA[type]')
            key = request.POST.get('formDATA[key]')
            message = None
            if key == None or key == '' or key == ' ':
                message = "Valid "+typpe+" Key required"
                return HttpResponse(json.dumps({"ssuccess":"No","message":message}))

            if typpe == 'CC':
                # if occupied_values_subs == [] or occupied_values_subs == '' or occupied_values_subs == None:
                #     occupied_values_subs = []
                # else:
                #     occupied_values_subs = occupied_values_subs.split(',')
                #     occupied_values_subs = set(occupied_values_subs)
                #     occupied_values_subs = list(occupied_values_subs)
                #     occupied_values_subs = [int(elem) for elem in occupied_values_subs]
                #     if 0 in occupied_values_subs:
                #         occupied_values_subs.remove(0)
                #     if 9999 in  occupied_values_subs:
                #         occupied_values_subs.remove(9999)
                #     occupied_values_subs.sort()
                # try:
                #     subs_obj = subs_occupied_cc_ranks.objects.get(key=key)
                #     subs_obj.ranklist = occupied_values_subs
                #     subs_obj.save()
                #     message = "Subscribed Ranks Successfully Updated "
                # except:
                #     message = "Subscribed Rank Object not Found"
                #     return HttpResponse(json.dumps({"ssuccess": "No", "message": message}))

                if occupied_values_spons == [] or occupied_values_spons == '' or occupied_values_spons == None:
                    occupied_values_spons = []
                else:
                    occupied_values_spons =  occupied_values_spons.split(',')
                    occupied_values_spons =  set(occupied_values_spons)
                    occupied_values_spons =  list(occupied_values_spons)
                    occupied_values_spons =  [int(elem) for elem in occupied_values_spons]
                    if 0 in occupied_values_spons:
                        occupied_values_spons.remove(0)
                    if 9999 in occupied_values_spons:
                        occupied_values_spons.remove(9999)
                    occupied_values_spons.sort()
                try:
                    spons_obj = spons_occupied_cc_ranks.objects.get(key=key)
                    spons_obj.ranklist = occupied_values_spons
                    spons_obj.save()
                    message = "Sponsored Ranks Successfully Updated "
                    return HttpResponse(json.dumps({"ssuccess": "Yes", "message": message}))
                except:
                    message = "Sponsored Rank Object not Found"
                    return HttpResponse(json.dumps({"ssuccess": "No", "message": message}))
            elif typpe == 'CLC':
                # if occupied_values_subs == [] or occupied_values_subs == '' or occupied_values_subs == None:
                #     occupied_values_subs = []
                # else:
                #     occupied_values_subs =  occupied_values_subs.split(',')
                #     occupied_values_subs =  set(occupied_values_subs)
                #     occupied_values_subs =  list(occupied_values_subs)
                #     occupied_values_subs =  [int(elem) for elem in occupied_values_subs]
                #     while 0 in occupied_values_subs:
                #         occupied_values_subs.remove(0)
                #     while 9999 in occupied_values_subs:
                #         occupied_values_subs.remove(9999)
                #     occupied_values_subs.sort()
                # try:
                #     subs_obj = subs_occupied_clc_ranks.objects.get(key=key)
                #     subs_obj.ranklist = occupied_values_subs
                #     subs_obj.save()
                #     message = "Subscribed Ranks Successfully Updated "
                # except:
                #     message = "Subscribed Rank Object not Found"
                #     return HttpResponse(json.dumps({"ssuccess": "No", "message": message}))

                if occupied_values_spons == [] or occupied_values_spons == '' or occupied_values_spons == None:
                    occupied_values_spons = []
                else:
                    occupied_values_spons =  occupied_values_spons.split(',')
                    occupied_values_spons =  set(occupied_values_spons)
                    occupied_values_spons =  list(occupied_values_spons)
                    occupied_values_spons =  [int(elem) for elem in occupied_values_spons]
                    while 0 in occupied_values_spons:
                        occupied_values_spons.remove(0)
                    while 9999 in occupied_values_spons:
                        occupied_values_spons.remove(9999)
                    occupied_values_spons.sort()
                try:
                    spons_obj = spons_occupied_clc_ranks.objects.get(key=key)
                    spons_obj.ranklist = occupied_values_spons
                    spons_obj.save()
                    message = "Sponsored Ranks Successfully Updated "
                    return HttpResponse(json.dumps({"ssuccess": "Yes", "message": message}))
                except:
                    message = "Sponsored Rank Object not Found"
                    return HttpResponse(json.dumps({"ssuccess": "No", "message": message}))
        else:
            message = request.mothod+ " method not allowed"
            return HttpResponse({"ssuccess": "No", "Message": message})
    except Exception as e:
        message = e
        return HttpResponse({"ssuccess": "No", "Message": message})

####################################################################
# Name - get_cities_list                                           #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def get_cities_list(request):
    data = []
    try:
        if request.method == "POST":
            city_id = request.POST.get('city_id')
            city_location_obj = Locality.objects.filter(city_id=city_id,delete=False)
            for i in city_location_obj:
                data_json = {}
                data_json['id'] = i.id
                data_json['name'] = i.name
                data.append(data_json)
            if data:
                data = json.dumps(data)
    except Exception as e:
        raise Http404
    return HttpResponse(data)

####################################################################
# Name - live_doctor_data_manage                                   #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def doctor_rank_module(request):
    try:
        # return render(request, 'admin/rank_notifications/rank_notifications.html',
        #               {'tab': 'doctor_rank_notifications', 'crosal': 'livedoctormanage'})

        return render(request, 'admin/rank_module.html',
                       {'tab': 'doctor_rank_module', 'crosal': 'livedoctormanage'})
    except Exception as e:
        raise Http404


####################################################################
# Name - live_doctor_data_manage                                   #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def old_doctor_rank_module(request):
    try:
        # return render(request, 'admin/rank_notifications/rank_notifications.html',
        #               {'tab': 'doctor_rank_notifications', 'crosal': 'livedoctormanage'})

        return render(request, 'admin/old_doctor_rank_module.html',
                       {'tab': 'doctor_rank_module', 'crosal': 'livedoctormanage'})
    except Exception as e:
        raise Http404

    live_doctor_rank_module
####################################################################
# Name - live_doctor_rank_module                                   #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def live_doctor_rank_module(request):
    try:
        # return render(request, 'admin/rank_notifications/rank_notifications.html',
        #               {'tab': 'doctor_rank_notifications', 'crosal': 'livedoctormanage'})

        return render(request, 'admin/live_doctor_rank_module.html',
                       {'tab': 'doctor_rank_module', 'crosal': 'livedoctormanage'})
    except Exception as e:
        raise Http404


#@^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
####################################################################
# Name - sponsored_ranks_report                                    #
# By Nishank                                                       #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
#@require_GET
def sponsored_ranks_report(request):
    try:
        doccategory = None
        lldoc = None
        report_list = []

        city_filter = False
        stage_filter = False
        user_filter = False
        city_location_filter_length = False
        category_filter = False
        #stage_data = Stage.objects.all()[:4]
        stage_data = Stage.objects.all()
        user_data = User.objects.all().order_by('username')
        city_obj = City.objects.filter(delete=False).order_by('name')
        city_location_obj = {}
        category_obj = Category.objects.filter(delete=False).order_by('name')
        search_data=None
        search_data = request.GET.get('search_data')
        mpty = []
        del_sch_mainlist = []
        # if search_data :
        #     doctor_data_obj = Live_Doctor.objects.all()
        #     mpty =[]
        #     for ld in doctor_data_obj:
        #         fulln = ''
        #         fulln = ld.firstName + ' ' +ld.lastName
        #         if search_data.lower() in fulln.lower():
        #             mpty.append(ld)
        #     mpty = [x.id for x in mpty]
        #     all_deleted_Schedules = Live_Doctor_Commonworkschedule.objects.filter(status__iexact='delete',doctor_id__in=mpty)
        #
        #     for sscchh in all_deleted_Schedules:
        #         lldoc = Live_Doctor.objects.get(id=sscchh.doctor_id)
        #         try:
        #             doccategory = Category.objects.get(id=lldoc.category).name
        #         except:
        #             doccategory = None
        #
        #         try:
        #             oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
        #         except:
        #             oorg = None
        #         if oorg != None and doccategory != None:
        #             Key_CC_RANK = oorg.city_id.__str__() + '-' + lldoc.category.__str__()
        #             key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + lldoc.category.__str__()
        #             Spon_cc =  lldoc.sponsored_rank['CC_RANK_list'].get(Key_CC_RANK,'DoesNotExist')
        #             Spon_clc = lldoc.sponsored_rank['CLC_RANK_list'].get(key_CLC_RANK,'DoesNotExist')
        #             Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(id=lldoc.category).name
        #             key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(id=lldoc.category).name
        #             if Spon_cc == 'DoesNotExist' and Spon_clc == 'DoesNotExist':
        #                 pass
        #             else:
        #                 if Spon_cc == 'DoesNotExist':
        #                     Spon_cc = None
        #                 if Spon_clc == 'DoesNotExist':
        #                     Spon_clc = None
        #                 del_sch_mainlist.append([lldoc,doccategory,oorg,Spon_cc,Spon_clc,Key_CC_RANK,key_CLC_RANK,lldoc.firstName,
        #                                          Key_CC_RANK_lable,key_CLC_RANK_label])
        #     if report_list != []:
        #         report_list.sort(key=lambda x: x[1])
        #
        #     paginator = Paginator(report_list, 100)
        #     page = request.GET.get('page')
        #     try:
        #         report_list = paginator.page(page)
        #     except PageNotAnInteger:
        #         # If page is not an integer, deliver first page.
        #         report_list = paginator.page(1)
        #     except EmptyPage:
        #         # If page is out of range (e.g. 9999), deliver last page of results.
        #         report_list = paginator.page(paginator.num_pages)
        #     return render(request, 'admin/live_doctor_management/sponsored_rank_report.html',
        #                   {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
        #                    'city_filter': city_filter,
        #                    'category_obj': category_obj, 'report_list': report_list,
        #                    'city_obj': city_obj, 'city_location_filter_length': city_location_filter_length,
        #                    'category_filter': category_filter, 'city_location_obj': city_location_obj,
        #                    'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
        #                    'search_data':search_data})
        try:
            filter_name = str(request.GET['x'].strip())
        except:
            filter_name = None
        if filter_name == 'filter':
            city_data = request.GET['city'].strip()
            if city_data:
                city_filter = city_data
            try:
                city_location_data = request.GET['city_location'].strip()
            except:
                city_location_data = 0
            try:
                stage_id_data = request.GET['stage_da'].strip()
            except:
                stage_id_data = 0
            try:
                user_id_data = request.GET['user_da'].strip()
            except:
                user_id_data = 0
            if stage_id_data:
                stage_filter = int(stage_id_data)
            if user_id_data:
                user_filter = int(user_id_data)
            if city_location_data:
                city_location_filter_length = int(city_location_data)
                city_location_obj = Locality.objects.filter(delete=False)

            category_data = request.GET['category'].strip()
            if category_data:
                category_filter = int(category_data)
            if city_data and category_data:
                if city_location_data and stage_id_data and user_id_data:
                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),stage=int(stage_id_data),category=int(category_data),current_user=int(user_id_data)).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),locality_id= int(city_location_data)).values_list('id',flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                    if report_list != []:
                        report_list.sort(key=lambda x: x[1])

                    # paginator = Paginator(report_list, 100)
                    # page = request.GET.get('page')
                    # try:
                    #     report_list = paginator.page(page)
                    # except PageNotAnInteger:
                    #     # If page is not an integer, deliver first page.
                    #     report_list = paginator.page(1)
                    # except EmptyPage:
                    #     # If page is out of range (e.g. 9999), deliver last page of results.
                        report_list = paginator.page(paginator.num_pages)
                    return render(request, 'admin/live_doctor_management/sponsored_rank_report.html',
                                  {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                                   'city_filter': city_filter,
                                   'category_obj': category_obj, 'report_list': report_list,
                                   'city_obj': city_obj,
                                   'city_location_filter_length': city_location_filter_length,
                                   'category_filter': category_filter, 'city_location_obj': city_location_obj,
                                   'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })


                elif city_location_data and stage_id_data:
                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data), category=int(category_data)).order_by(
                        'id')
                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),locality_id= int(city_location_data)).values_list('id',flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])


                elif city_location_data and user_id_data:
                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        category=int(category_data), current_user=int(user_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),
                                                                      locality_id=int(city_location_data)).values_list('id',
                                                                                                                  flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,
                                                                                      clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                elif stage_id_data and user_id_data:

                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data), category=int(category_data), current_user=int(user_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data)).values_list('id',flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,
                                                                                      clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                    if report_list != []:
                        report_list.sort(key=lambda x: x[1])

                    # paginator = Paginator(report_list, 100)
                    # page = request.GET.get('page')
                    # try:
                    #     report_list = paginator.page(page)
                    # except PageNotAnInteger:
                    #     # If page is not an integer, deliver first page.
                    #     report_list = paginator.page(1)
                    # except EmptyPage:
                    #     # If page is out of range (e.g. 9999), deliver last page of results.
                    #     report_list = paginator.page(paginator.num_pages)
                    return render(request, 'admin/live_doctor_management/sponsored_rank_report.html',
                                  {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                                   'city_filter': city_filter,
                                   'category_obj': category_obj, 'report_list': report_list,
                                   'city_obj': city_obj,
                                   'city_location_filter_length': city_location_filter_length,
                                   'category_filter': category_filter, 'city_location_obj': city_location_obj,
                                   'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

                elif stage_id_data:
                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data), category=int(category_data)).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data)).values_list('id', flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,
                                                                                      clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                elif city_location_data:
                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                         category=int(category_data)).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),locality_id= int(city_location_data)).values_list('id', flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,
                                                                                      clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])



                elif user_id_data:
                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                         category=int(category_data), current_user=int(user_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data)).values_list('id',flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,
                                                                                      clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                else:
                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        category=int(category_data)).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data)).values_list('id',flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,
                                                                                      clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])
                if report_list != []:
                    report_list.sort(key=lambda x: x[1])


                # paginator = Paginator(report_list, 100)
                # page = request.GET.get('page')
                # try:
                #     report_list = paginator.page(page)
                # except PageNotAnInteger:
                #     # If page is not an integer, deliver first page.
                #     report_list = paginator.page(1)
                # except EmptyPage:
                #     # If page is out of range (e.g. 9999), deliver last page of results.
                #     report_list = paginator.page(paginator.num_pages)
                return render(request, 'admin/live_doctor_management/sponsored_rank_report.html',
                              {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                               'city_filter': city_filter,
                               'category_obj': category_obj, 'report_list': report_list,
                               'city_obj': city_obj, 'city_location_filter_length': city_location_filter_length,
                               'category_filter': category_filter, 'city_location_obj': city_location_obj,
                               'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })
            elif category_data:
                if stage_id_data and user_id_data:

                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data), category=int(category_data), current_user=int(user_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        # filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),
                        #                                               locality_id=int(city_location_data)).values('id',
                        #                                                                                           flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id)

                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])


                    if report_list != []:
                        report_list.sort(key=lambda x: x[1])
                    # paginator = Paginator(report_list, 100)
                    # page = request.GET.get('page')
                    # try:
                    #     report_list = paginator.page(page)
                    # except PageNotAnInteger:
                    #     # If page is not an integer, deliver first page.
                    #     report_list = paginator.page(1)
                    # except EmptyPage:
                    #     # If page is out of range (e.g. 9999), deliver last page of results.
                    #     report_list = paginator.page(paginator.num_pages)
                    return render(request, 'admin/live_doctor_management/sponsored_rank_report.html',
                                  {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                                   'city_filter': city_filter,
                                   'category_obj': category_obj, 'report_list': report_list,
                                   'city_obj': city_obj,
                                   'city_location_filter_length': city_location_filter_length,
                                   'category_filter': category_filter, 'city_location_obj': city_location_obj,
                                   'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

                elif stage_id_data:
                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data), category=int(category_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []


                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                elif user_id_data:
                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        category=int(category_data), current_user=int(user_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])


                else:
                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        category=int(category_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])


                if report_list != []:
                    report_list.sort(key=lambda x: x[1])

                # paginator = Paginator(report_list, 100)
                # page = request.GET.get('page')
                # try:
                #     report_list = paginator.page(page)
                # except PageNotAnInteger:
                #     # If page is not an integer, deliver first page.
                #     report_list = paginator.page(1)
                # except EmptyPage:
                #     # If page is out of range (e.g. 9999), deliver last page of results.
                #     report_list = paginator.page(paginator.num_pages)
                return render(request, 'admin/live_doctor_management/sponsored_rank_report.html',
                              {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                               'city_filter': city_filter,
                               'category_obj': category_obj, 'report_list': report_list,
                               'city_obj': city_obj,
                               'city_location_filter_length': city_location_filter_length,
                               'category_filter': category_filter, 'city_location_obj': city_location_obj,
                               'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

            elif city_data and city_location_data:
                if stage_id_data and user_id_data:

                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data),current_user=int(user_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),
                                                                      locality_id=int(city_location_data)).values_list('id',
                                                                                                                  flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,
                                                                                      clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])


                    if report_list != []:
                        report_list.sort(key=lambda x: x[1])

                    # paginator = Paginator(report_list, 100)
                    # page = request.GET.get('page')
                    # try:
                    #     report_list = paginator.page(page)
                    # except PageNotAnInteger:
                    #     # If page is not an integer, deliver first page.
                    #     report_list = paginator.page(1)
                    # except EmptyPage:
                    #     # If page is out of range (e.g. 9999), deliver last page of results.
                    #     report_list = paginator.page(paginator.num_pages)
                    return render(request, 'admin/live_doctor_management/sponsored_rank_report.html',
                                  {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                                   'city_filter': city_filter,
                                   'category_obj': category_obj, 'report_list': report_list,
                                   'city_obj': city_obj,
                                   'city_location_filter_length': city_location_filter_length,
                                   'category_filter': category_filter, 'city_location_obj': city_location_obj,
                                   'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

                elif stage_id_data:
                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),
                                                                      locality_id=int(city_location_data)).values_list('id',
                                                                                                                  flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,
                                                                                      clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                elif user_id_data:

                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                         current_user=int(user_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),
                                                                      locality_id=int(city_location_data)).values_list('id',
                                                                                                                  flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,
                                                                                      clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                else:

                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={})).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),
                                                                      locality_id=int(city_location_data)).values_list('id',
                                                                                                                  flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,
                                                                                      clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                if report_list != []:
                    report_list.sort(key=lambda x: x[1])

                # paginator = Paginator(report_list, 100)
                # page = request.GET.get('page')
                # try:
                #     report_list = paginator.page(page)
                # except PageNotAnInteger:
                #     # If page is not an integer, deliver first page.
                #     report_list = paginator.page(1)
                # except EmptyPage:
                #     # If page is out of range (e.g. 9999), deliver last page of results.
                #     report_list = paginator.page(paginator.num_pages)
                return render(request, 'admin/live_doctor_management/sponsored_rank_report.html',
                              {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                               'city_filter': city_filter,
                               'category_obj': category_obj, 'report_list': report_list,
                               'city_obj': city_obj, 'city_location_filter_length': city_location_filter_length,
                               'category_filter': category_filter, 'city_location_obj': city_location_obj,
                               'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                               'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                               'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

            elif city_data:
                if stage_id_data and user_id_data:

                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data), current_user=int(user_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data)).values_list('id',flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,
                                                                                      clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                    if report_list != []:
                        report_list.sort(key=lambda x: x[1])


                    # paginator = Paginator(report_list, 100)
                    # page = request.GET.get('page')
                    # try:
                    #     report_list = paginator.page(page)
                    # except PageNotAnInteger:
                    #     # If page is not an integer, deliver first page.
                    #     report_list = paginator.page(1)
                    # except EmptyPage:
                    #     # If page is out of range (e.g. 9999), deliver last page of results.
                    #     report_list = paginator.page(paginator.num_pages)
                    return render(request, 'admin/live_doctor_management/sponsored_rank_report.html',
                                  {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                                   'city_filter': city_filter,
                                   'category_obj': category_obj, 'report_list': report_list,
                                   'city_obj': city_obj,
                                   'city_location_filter_length': city_location_filter_length,
                                   'category_filter': category_filter, 'city_location_obj': city_location_obj,
                                   'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

                elif stage_id_data:

                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data)).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),).values_list('id',flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,
                                                                                      clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                elif user_id_data:

                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                         current_user=int(user_id_data)).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data)).values_list('id',flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,
                                                                                      clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                else:
                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={})).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data)).values_list('id',flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,
                                                                                      clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])


                if report_list != []:
                    report_list.sort(key=lambda x: x[1])

                # paginator = Paginator(report_list, 100)
                # page = request.GET.get('page')
                # try:
                #     report_list = paginator.page(page)
                # except PageNotAnInteger:
                #     # If page is not an integer, deliver first page.
                #     report_list = paginator.page(1)
                # except EmptyPage:
                #     # If page is out of range (e.g. 9999), deliver last page of results.
                #     report_list = paginator.page(paginator.num_pages)
                return render(request, 'admin/live_doctor_management/sponsored_rank_report.html',
                              {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                               'city_filter': city_filter,
                               'category_obj': category_obj, 'report_list': report_list,
                               'city_obj': city_obj, 'city_location_filter_length': city_location_filter_length,
                               'category_filter': category_filter, 'city_location_obj': city_location_obj,
                               'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                               'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                               'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

            elif stage_id_data or user_id_data:
                if stage_id_data and user_id_data:

                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data), current_user=int(user_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                    if report_list != []:
                        report_list.sort(key=lambda x: x[1])

                    # paginator = Paginator(report_list, 100)
                    # page = request.GET.get('page')
                    # try:
                    #     report_list = paginator.page(page)
                    # except PageNotAnInteger:
                    #     # If page is not an integer, deliver first page.
                    #     report_list = paginator.page(1)
                    # except EmptyPage:
                    #     # If page is out of range (e.g. 9999), deliver last page of results.
                    #     report_list = paginator.page(paginator.num_pages)
                    return render(request, 'admin/live_doctor_management/sponsored_rank_report.html',
                                  {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                                   'city_filter': city_filter,
                                   'category_obj': category_obj, 'report_list': report_list,
                                   'city_obj': city_obj,
                                   'city_location_filter_length': city_location_filter_length,
                                   'category_filter': category_filter, 'city_location_obj': city_location_obj,
                                   'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

                elif stage_id_data:

                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data)).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                elif user_id_data:

                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        current_user=int(user_id_data)).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                # else:
                #     pass
            else:
                doctor_liist = Live_Doctor.objects.filter(
                    ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={})).order_by('id')
                for dddoc in doctor_liist:
                    cc_add_list = []
                    cc_add_list_write = []
                    clc_add_list = []
                    clc_add_list_write = []
                    city_list = []
                    locality_list = []
                    all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                  doctor_id=dddoc.id)
                    if all_Schedules != []:
                        for sscchh in all_Schedules:
                            key_CLC_RANK_label = Key_CC_RANK_lable = None
                            try:
                                doccategory = Category.objects.get(id=dddoc.category).name
                            except:
                                doccategory = None

                            try:
                                oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                            except:
                                oorg = None
                            if oorg != None and doccategory != None:
                                Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                    if Key_CC_RANK not in cc_add_list:
                                        cc_add_list.append(Key_CC_RANK)
                                        Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                            id=dddoc.category).name + '_' + str(
                                            dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                        cc_add_list_write.append(Key_CC_RANK_lable)
                                        if oorg.city.name not in city_list:
                                            city_list.append(oorg.city.name)

                                if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                    if key_CLC_RANK not in clc_add_list:
                                        clc_add_list.append(key_CLC_RANK)
                                        key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                            id=dddoc.category).name + '_' + str(
                                            dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                        clc_add_list_write.append(key_CLC_RANK_label)
                                        if oorg.city.name not in city_list:
                                            city_list.append(oorg.city.name)
                                        if oorg.locality.name not in locality_list:
                                            locality_list.append(oorg.locality.name)
                        if cc_add_list_write != [] or clc_add_list_write != []:
                            try:
                                doccategory = Category.objects.get(id=dddoc.category).name
                            except:
                                doccategory = 'NA'
                            city_list = ",".join(city_list)
                            locality_list = ",".join(locality_list)
                            if cc_add_list_write == []:
                                cc_add_list_write = 'NA'
                            else:
                                cc_add_list_write = ",".join(cc_add_list_write)
                            if clc_add_list_write == []:
                                clc_add_list_write = 'NA'
                            else:
                                clc_add_list_write = ",".join(clc_add_list_write)
                            if dddoc.stage:
                                stage_name = dddoc.stage.stage_name
                            else:
                                stage_name = 'NA'
                            if dddoc.current_user:
                                cu_name = dddoc.current_user.username
                            else:
                                stage_name = 'NA'
                            doc_name = dddoc.firstName + ' ' + dddoc.lastName

                            report_list.append(
                                [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                 clc_add_list_write, stage_name, cu_name])

            if report_list != []:
                report_list.sort(key=lambda x: x[1])


            # paginator = Paginator(report_list, 100)
            # page = request.GET.get('page')
            # try:
            #     report_list = paginator.page(page)
            # except PageNotAnInteger:
            #     # If page is not an integer, deliver first page.
            #     report_list = paginator.page(1)
            # except EmptyPage:
            #     # If page is out of range (e.g. 9999), deliver last page of results.
            #     report_list = paginator.page(paginator.num_pages)
            return render(request, 'admin/live_doctor_management/sponsored_rank_report.html',
                          {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                           'city_filter': city_filter,
                           'category_obj': category_obj, 'report_list': report_list,
                           'city_obj': city_obj, 'city_location_filter_length': city_location_filter_length,
                           'category_filter': category_filter, 'city_location_obj': city_location_obj,
                           'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                           'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                           'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

        else:

            filter_name = None
            city_data = None
            city_location_data = None
            category_data = None
            stage_id_data = None
            user_id_data= None
            report_list = []

            doctor_liist = Live_Doctor.objects.filter(~Q(sponsored_rank__CC_RANK_list={})|~Q(sponsored_rank__CLC_RANK_list={})).order_by('id')
            for dddoc in doctor_liist:
                cc_add_list = []
                cc_add_list_write = []
                clc_add_list = []
                clc_add_list_write = []
                city_list = []
                locality_list = []
                all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),doctor_id=dddoc.id)
                if all_Schedules != []:
                    for sscchh in all_Schedules:
                        key_CLC_RANK_label =  Key_CC_RANK_lable = None
                        try:
                            doccategory = Category.objects.get(id=dddoc.category).name
                        except:
                            doccategory = None

                        try:
                            oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                        except:
                            oorg = None
                        if oorg != None and doccategory != None:
                            Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                            key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                            if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                if Key_CC_RANK not in cc_add_list:
                                    cc_add_list.append(Key_CC_RANK)
                                    Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(id=dddoc.category).name+'_'+str(dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                    cc_add_list_write.append(Key_CC_RANK_lable)
                                    if oorg.city.name not in city_list:
                                        city_list.append(oorg.city.name)

                            if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                if key_CLC_RANK not in clc_add_list:
                                    clc_add_list.append(key_CLC_RANK)
                                    key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                        id=dddoc.category).name +'_'+str(dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                    clc_add_list_write.append(key_CLC_RANK_label)
                                    if oorg.city.name not in city_list:
                                        city_list.append(oorg.city.name)
                                    if oorg.locality.name not in locality_list:
                                        locality_list.append(oorg.locality.name)
                    if cc_add_list_write != [] or clc_add_list_write != []:
                        try:
                            doccategory = Category.objects.get(id=dddoc.category).name
                        except:
                            doccategory = 'NA'
                        city_list = ",".join(city_list)
                        locality_list = ",".join(locality_list)
                        if cc_add_list_write == []:
                            cc_add_list_write ='NA'
                        else:
                            cc_add_list_write = ",".join(cc_add_list_write)
                        if clc_add_list_write ==[]:
                            clc_add_list_write= 'NA'
                        else:
                            clc_add_list_write = ",".join(clc_add_list_write)
                        if dddoc.stage:
                            stage_name = dddoc.stage.stage_name
                        else:
                            stage_name = 'NA'
                        if dddoc.current_user:
                            cu_name = dddoc.current_user.username
                        else:
                            stage_name = 'NA'
                        doc_name = dddoc.firstName+' '+dddoc.lastName

                        report_list.append([dddoc.id,doc_name,city_list,locality_list,doccategory,cc_add_list_write,clc_add_list_write,stage_name,cu_name])

            if report_list != []:
                report_list.sort(key=lambda x: x[1])
            #paginator = Paginator(doctor_data_obj, 100)
            # paginator = Paginator(report_list, 100)
            # page = request.GET.get('page')
            # try:
            #     report_list = paginator.page(page)
            # except PageNotAnInteger:
            #     # If page is not an integer, deliver first page.
            #     report_list = paginator.page(1)
            # except EmptyPage:
            #     # If page is out of range (e.g. 9999), deliver last page of results.
            #     report_list = paginator.page(paginator.num_pages)
            return render(request, 'admin/live_doctor_management/sponsored_rank_report.html',
                          {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                           'city_filter': city_filter,'doctor_data_obj':None,
                           'category_obj': category_obj, 'report_list': report_list,
                           'city_obj': city_obj, 'city_location_filter_length': city_location_filter_length,
                           'category_filter': category_filter, 'city_location_obj': city_location_obj,
                           'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                           'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                           'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

    except Exception as e:
        raise Http404

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^






#@^^^^^^^^^^^^^^^^^^^^^^^^########^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
####################################################################
# Name - subscribed_ranks_report                                   #
# By Nishank                                                       #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
#@require_GET
def subscribed_ranks_report(request):
    try:
        doccategory = None
        lldoc = None
        report_list = []

        city_filter = False
        stage_filter = False
        user_filter = False
        city_location_filter_length = False
        category_filter = False
        #stage_data = Stage.objects.all()[:4]
        stage_data = Stage.objects.all()
        user_data = User.objects.all().order_by('username')
        city_obj = City.objects.filter(delete=False).order_by('name')
        city_location_obj = {}
        category_obj = Category.objects.filter(delete=False).order_by('name')
        search_data=None
        search_data = request.GET.get('search_data')
        mpty = []
        del_sch_mainlist = []
        # if search_data :
        #     doctor_data_obj = Live_Doctor.objects.all()
        #     mpty =[]
        #     for ld in doctor_data_obj:
        #         fulln = ''
        #         fulln = ld.firstName + ' ' +ld.lastName
        #         if search_data.lower() in fulln.lower():
        #             mpty.append(ld)
        #     mpty = [x.id for x in mpty]
        #     all_deleted_Schedules = Live_Doctor_Commonworkschedule.objects.filter(status__iexact='delete',doctor_id__in=mpty)
        #
        #     for sscchh in all_deleted_Schedules:
        #         lldoc = Live_Doctor.objects.get(id=sscchh.doctor_id)
        #         try:
        #             doccategory = Category.objects.get(id=lldoc.category).name
        #         except:
        #             doccategory = None
        #
        #         try:
        #             oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
        #         except:
        #             oorg = None
        #         if oorg != None and doccategory != None:
        #             Key_CC_RANK = oorg.city_id.__str__() + '-' + lldoc.category.__str__()
        #             key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + lldoc.category.__str__()
        #             Spon_cc =  lldoc.sponsored_rank['CC_RANK_list'].get(Key_CC_RANK,'DoesNotExist')
        #             Spon_clc = lldoc.sponsored_rank['CLC_RANK_list'].get(key_CLC_RANK,'DoesNotExist')
        #             Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(id=lldoc.category).name
        #             key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(id=lldoc.category).name
        #             if Spon_cc == 'DoesNotExist' and Spon_clc == 'DoesNotExist':
        #                 pass
        #             else:
        #                 if Spon_cc == 'DoesNotExist':
        #                     Spon_cc = None
        #                 if Spon_clc == 'DoesNotExist':
        #                     Spon_clc = None
        #                 del_sch_mainlist.append([lldoc,doccategory,oorg,Spon_cc,Spon_clc,Key_CC_RANK,key_CLC_RANK,lldoc.firstName,
        #                                          Key_CC_RANK_lable,key_CLC_RANK_label])
        #     if report_list != []:
        #         report_list.sort(key=lambda x: x[1])
        #
        #     paginator = Paginator(report_list, 100)
        #     page = request.GET.get('page')
        #     try:
        #         report_list = paginator.page(page)
        #     except PageNotAnInteger:
        #         # If page is not an integer, deliver first page.
        #         report_list = paginator.page(1)
        #     except EmptyPage:
        #         # If page is out of range (e.g. 9999), deliver last page of results.
        #         report_list = paginator.page(paginator.num_pages)
        #     return render(request, 'admin/live_doctor_management/sponsored_rank_report.html',
        #                   {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
        #                    'city_filter': city_filter,
        #                    'category_obj': category_obj, 'report_list': report_list,
        #                    'city_obj': city_obj, 'city_location_filter_length': city_location_filter_length,
        #                    'category_filter': category_filter, 'city_location_obj': city_location_obj,
        #                    'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
        #                    'search_data':search_data})
        try:
            filter_name = str(request.GET['x'].strip())
        except:
            filter_name = None
        if filter_name == 'filter':
            city_data = request.GET['city'].strip()
            if city_data:
                city_filter = city_data
            try:
                city_location_data = request.GET['city_location'].strip()
            except:
                city_location_data = 0
            try:
                stage_id_data = request.GET['stage_da'].strip()
            except:
                stage_id_data = 0
            try:
                user_id_data = request.GET['user_da'].strip()
            except:
                user_id_data = 0
            if stage_id_data:
                stage_filter = int(stage_id_data)
            if user_id_data:
                user_filter = int(user_id_data)
            if city_location_data:
                city_location_filter_length = int(city_location_data)
                city_location_obj = Locality.objects.filter(delete=False)

            category_data = request.GET['category'].strip()
            if category_data:
                category_filter = int(category_data)
            if city_data and category_data:
                if city_location_data and stage_id_data and user_id_data:
                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(subscribed_rank__CC_RANK_list={}) | ~Q(subscribed_rank__CLC_RANK_list={}),stage=int(stage_id_data),category=int(category_data),current_user=int(user_id_data)).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),locality_id= int(city_location_data)).values_list('id',flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.subscribed_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.subscribed_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                    if report_list != []:
                        report_list.sort(key=lambda x: x[1])

                    # paginator = Paginator(report_list, 100)
                    # page = request.GET.get('page')
                    # try:
                    #     report_list = paginator.page(page)
                    # except PageNotAnInteger:
                    #     # If page is not an integer, deliver first page.
                    #     report_list = paginator.page(1)
                    # except EmptyPage:
                    #     # If page is out of range (e.g. 9999), deliver last page of results.
                    #     report_list = paginator.page(paginator.num_pages)
                    return render(request, 'admin/live_doctor_management/subscribed_ranks_report.html',
                                  {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                                   'city_filter': city_filter,
                                   'category_obj': category_obj, 'report_list': report_list,
                                   'city_obj': city_obj,
                                   'city_location_filter_length': city_location_filter_length,
                                   'category_filter': category_filter, 'city_location_obj': city_location_obj,
                                   'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })


                elif city_location_data and stage_id_data:
                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(subscribed_rank__CC_RANK_list={}) | ~Q(subscribed_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data), category=int(category_data)).order_by(
                        'id')
                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),locality_id= int(city_location_data)).values_list('id',flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.subscribed_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.subscribed_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])


                elif city_location_data and user_id_data:
                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(subscribed_rank__CC_RANK_list={}) | ~Q(subscribed_rank__CLC_RANK_list={}),
                        category=int(category_data), current_user=int(user_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),
                                                                      locality_id=int(city_location_data)).values_list('id',
                                                                                                                  flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,
                                                                                      clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.subscribed_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.subscribed_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                elif stage_id_data and user_id_data:

                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(subscribed_rank__CC_RANK_list={}) | ~Q(subscribed_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data), category=int(category_data), current_user=int(user_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data)).values_list('id',flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,
                                                                                      clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.subscribed_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.subscribed_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                    if report_list != []:
                        report_list.sort(key=lambda x: x[1])

                    # paginator = Paginator(report_list, 100)
                    # page = request.GET.get('page')
                    # try:
                    #     report_list = paginator.page(page)
                    # except PageNotAnInteger:
                    #     # If page is not an integer, deliver first page.
                    #     report_list = paginator.page(1)
                    # except EmptyPage:
                    #     # If page is out of range (e.g. 9999), deliver last page of results.
                    #     report_list = paginator.page(paginator.num_pages)
                    return render(request, 'admin/live_doctor_management/subscribed_ranks_report.html',
                                  {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                                   'city_filter': city_filter,
                                   'category_obj': category_obj, 'report_list': report_list,
                                   'city_obj': city_obj,
                                   'city_location_filter_length': city_location_filter_length,
                                   'category_filter': category_filter, 'city_location_obj': city_location_obj,
                                   'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

                elif stage_id_data:
                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(subscribed_rank__CC_RANK_list={}) | ~Q(subscribed_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data), category=int(category_data)).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data)).values_list('id', flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,
                                                                                      clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.subscribed_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.subscribed_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                elif city_location_data:
                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(subscribed_rank__CC_RANK_list={}) | ~Q(subscribed_rank__CLC_RANK_list={}),
                         category=int(category_data)).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),locality_id= int(city_location_data)).values_list('id', flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,
                                                                                      clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.subscribed_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.subscribed_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])



                elif user_id_data:
                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(subscribed_rank__CC_RANK_list={}) | ~Q(subscribed_rank__CLC_RANK_list={}),
                         category=int(category_data), current_user=int(user_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data)).values_list('id',flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,
                                                                                      clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.subscribed_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.subscribed_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                else:
                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(subscribed_rank__CC_RANK_list={}) | ~Q(subscribed_rank__CLC_RANK_list={}),
                        category=int(category_data)).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data)).values_list('id',flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,
                                                                                      clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.subscribed_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.subscribed_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])
                if report_list != []:
                    report_list.sort(key=lambda x: x[1])


                # paginator = Paginator(report_list, 100)
                # page = request.GET.get('page')
                # try:
                #     report_list = paginator.page(page)
                # except PageNotAnInteger:
                #     # If page is not an integer, deliver first page.
                #     report_list = paginator.page(1)
                # except EmptyPage:
                #     # If page is out of range (e.g. 9999), deliver last page of results.
                #     report_list = paginator.page(paginator.num_pages)
                return render(request, 'admin/live_doctor_management/subscribed_ranks_report.html',
                              {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                               'city_filter': city_filter,
                               'category_obj': category_obj, 'report_list': report_list,
                               'city_obj': city_obj, 'city_location_filter_length': city_location_filter_length,
                               'category_filter': category_filter, 'city_location_obj': city_location_obj,
                               'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })
            elif category_data:
                if stage_id_data and user_id_data:

                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(subscribed_rank__CC_RANK_list={}) | ~Q(subscribed_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data), category=int(category_data), current_user=int(user_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        # filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),
                        #                                               locality_id=int(city_location_data)).values('id',
                        #                                                                                           flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id)

                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.subscribed_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.subscribed_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])


                    if report_list != []:
                        report_list.sort(key=lambda x: x[1])
                    # paginator = Paginator(report_list, 100)
                    # page = request.GET.get('page')
                    # try:
                    #     report_list = paginator.page(page)
                    # except PageNotAnInteger:
                    #     # If page is not an integer, deliver first page.
                    #     report_list = paginator.page(1)
                    # except EmptyPage:
                    #     # If page is out of range (e.g. 9999), deliver last page of results.
                    #     report_list = paginator.page(paginator.num_pages)
                    return render(request, 'admin/live_doctor_management/subscribed_ranks_report.html',
                                  {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                                   'city_filter': city_filter,
                                   'category_obj': category_obj, 'report_list': report_list,
                                   'city_obj': city_obj,
                                   'city_location_filter_length': city_location_filter_length,
                                   'category_filter': category_filter, 'city_location_obj': city_location_obj,
                                   'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

                elif stage_id_data:
                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(subscribed_rank__CC_RANK_list={}) | ~Q(subscribed_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data), category=int(category_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []


                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.subscribed_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.subscribed_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                elif user_id_data:
                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(subscribed_rank__CC_RANK_list={}) | ~Q(subscribed_rank__CLC_RANK_list={}),
                        category=int(category_data), current_user=int(user_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.subscribed_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.subscribed_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])


                else:
                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(subscribed_rank__CC_RANK_list={}) | ~Q(subscribed_rank__CLC_RANK_list={}),
                        category=int(category_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.subscribed_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.subscribed_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])


                if report_list != []:
                    report_list.sort(key=lambda x: x[1])

                # paginator = Paginator(report_list, 100)
                # page = request.GET.get('page')
                # try:
                #     report_list = paginator.page(page)
                # except PageNotAnInteger:
                #     # If page is not an integer, deliver first page.
                #     report_list = paginator.page(1)
                # except EmptyPage:
                #     # If page is out of range (e.g. 9999), deliver last page of results.
                #     report_list = paginator.page(paginator.num_pages)
                return render(request, 'admin/live_doctor_management/subscribed_ranks_report.html',
                              {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                               'city_filter': city_filter,
                               'category_obj': category_obj, 'report_list': report_list,
                               'city_obj': city_obj,
                               'city_location_filter_length': city_location_filter_length,
                               'category_filter': category_filter, 'city_location_obj': city_location_obj,
                               'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

            elif city_data and city_location_data:
                if stage_id_data and user_id_data:

                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(subscribed_rank__CC_RANK_list={}) | ~Q(subscribed_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data),current_user=int(user_id_data)).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),
                                                                      locality_id=int(city_location_data)).values_list('id',
                                                                                                                  flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,
                                                                                      clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.subscribed_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.subscribed_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])


                    if report_list != []:
                        report_list.sort(key=lambda x: x[1])

                    # paginator = Paginator(report_list, 100)
                    # page = request.GET.get('page')
                    # try:
                    #     report_list = paginator.page(page)
                    # except PageNotAnInteger:
                    #     # If page is not an integer, deliver first page.
                    #     report_list = paginator.page(1)
                    # except EmptyPage:
                    #     # If page is out of range (e.g. 9999), deliver last page of results.
                    #     report_list = paginator.page(paginator.num_pages)
                    return render(request, 'admin/live_doctor_management/subscribed_ranks_report.html',
                                  {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                                   'city_filter': city_filter,
                                   'category_obj': category_obj, 'report_list': report_list,
                                   'city_obj': city_obj,
                                   'city_location_filter_length': city_location_filter_length,
                                   'category_filter': category_filter, 'city_location_obj': city_location_obj,
                                   'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

                elif stage_id_data:
                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(subscribed_rank__CC_RANK_list={}) | ~Q(subscribed_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),
                                                                      locality_id=int(city_location_data)).values_list('id',
                                                                                                                  flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,
                                                                                      clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.subscribed_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.subscribed_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                elif user_id_data:

                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(subscribed_rank__CC_RANK_list={}) | ~Q(subscribed_rank__CLC_RANK_list={}),
                         current_user=int(user_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),
                                                                      locality_id=int(city_location_data)).values_list('id',
                                                                                                                  flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,
                                                                                      clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.subscribed_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.subscribed_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                else:

                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(subscribed_rank__CC_RANK_list={}) | ~Q(subscribed_rank__CLC_RANK_list={})).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),
                                                                      locality_id=int(city_location_data)).values_list('id',
                                                                                                                  flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,
                                                                                      clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.subscribed_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.subscribed_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                if report_list != []:
                    report_list.sort(key=lambda x: x[1])

                # paginator = Paginator(report_list, 100)
                # page = request.GET.get('page')
                # try:
                #     report_list = paginator.page(page)
                # except PageNotAnInteger:
                #     # If page is not an integer, deliver first page.
                #     report_list = paginator.page(1)
                # except EmptyPage:
                #     # If page is out of range (e.g. 9999), deliver last page of results.
                #     report_list = paginator.page(paginator.num_pages)
                return render(request, 'admin/live_doctor_management/subscribed_ranks_report.html',
                              {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                               'city_filter': city_filter,
                               'category_obj': category_obj, 'report_list': report_list,
                               'city_obj': city_obj, 'city_location_filter_length': city_location_filter_length,
                               'category_filter': category_filter, 'city_location_obj': city_location_obj,
                               'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                               'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                               'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

            elif city_data:
                if stage_id_data and user_id_data:

                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(subscribed_rank__CC_RANK_list={}) | ~Q(subscribed_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data), current_user=int(user_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data)).values_list('id',flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,
                                                                                      clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.subscribed_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.subscribed_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                    if report_list != []:
                        report_list.sort(key=lambda x: x[1])


                    # paginator = Paginator(report_list, 100)
                    # page = request.GET.get('page')
                    # try:
                    #     report_list = paginator.page(page)
                    # except PageNotAnInteger:
                    #     # If page is not an integer, deliver first page.
                    #     report_list = paginator.page(1)
                    # except EmptyPage:
                    #     # If page is out of range (e.g. 9999), deliver last page of results.
                    #     report_list = paginator.page(paginator.num_pages)
                    return render(request, 'admin/live_doctor_management/subscribed_ranks_report.html',
                                  {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                                   'city_filter': city_filter,
                                   'category_obj': category_obj, 'report_list': report_list,
                                   'city_obj': city_obj,
                                   'city_location_filter_length': city_location_filter_length,
                                   'category_filter': category_filter, 'city_location_obj': city_location_obj,
                                   'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

                elif stage_id_data:

                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(subscribed_rank__CC_RANK_list={}) | ~Q(subscribed_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data)).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),).values_list('id',flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,
                                                                                      clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.subscribed_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.subscribed_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                elif user_id_data:

                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(subscribed_rank__CC_RANK_list={}) | ~Q(subscribed_rank__CLC_RANK_list={}),
                         current_user=int(user_id_data)).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data)).values_list('id',flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,
                                                                                      clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.subscribed_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.subscribed_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                else:
                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(subscribed_rank__CC_RANK_list={}) | ~Q(subscribed_rank__CLC_RANK_list={})).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data)).values_list('id',flat=True)

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id,
                                                                                      clinic_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.subscribed_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.subscribed_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])


                if report_list != []:
                    report_list.sort(key=lambda x: x[1])

                # paginator = Paginator(report_list, 100)
                # page = request.GET.get('page')
                # try:
                #     report_list = paginator.page(page)
                # except PageNotAnInteger:
                #     # If page is not an integer, deliver first page.
                #     report_list = paginator.page(1)
                # except EmptyPage:
                #     # If page is out of range (e.g. 9999), deliver last page of results.
                #     report_list = paginator.page(paginator.num_pages)
                return render(request, 'admin/live_doctor_management/subscribed_ranks_report.html',
                              {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                               'city_filter': city_filter,
                               'category_obj': category_obj, 'report_list': report_list,
                               'city_obj': city_obj, 'city_location_filter_length': city_location_filter_length,
                               'category_filter': category_filter, 'city_location_obj': city_location_obj,
                               'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                               'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                               'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

            elif stage_id_data or user_id_data:
                if stage_id_data and user_id_data:

                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(subscribed_rank__CC_RANK_list={}) | ~Q(subscribed_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data), current_user=int(user_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.subscribed_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.subscribed_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                    if report_list != []:
                        report_list.sort(key=lambda x: x[1])

                    # paginator = Paginator(report_list, 100)
                    # page = request.GET.get('page')
                    # try:
                    #     report_list = paginator.page(page)
                    # except PageNotAnInteger:
                    #     # If page is not an integer, deliver first page.
                    #     report_list = paginator.page(1)
                    # except EmptyPage:
                    #     # If page is out of range (e.g. 9999), deliver last page of results.
                    #     report_list = paginator.page(paginator.num_pages)
                    return render(request, 'admin/live_doctor_management/subscribed_ranks_report.html',
                                  {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                                   'city_filter': city_filter,
                                   'category_obj': category_obj, 'report_list': report_list,
                                   'city_obj': city_obj,
                                   'city_location_filter_length': city_location_filter_length,
                                   'category_filter': category_filter, 'city_location_obj': city_location_obj,
                                   'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

                elif stage_id_data:

                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(subscribed_rank__CC_RANK_list={}) | ~Q(subscribed_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data)).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.subscribed_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.subscribed_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                elif user_id_data:

                    doctor_liist = Live_Doctor.objects.filter(
                        ~Q(subscribed_rank__CC_RANK_list={}) | ~Q(subscribed_rank__CLC_RANK_list={}),
                        current_user=int(user_id_data)).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []

                        all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                      doctor_id=dddoc.id)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                    if Key_CC_RANK in dddoc.subscribed_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.subscribed_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category).name + '_' + str(
                                                dddoc.subscribed_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.firstName + ' ' + dddoc.lastName

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                # else:
                #     pass
            else:
                doctor_liist = Live_Doctor.objects.filter(
                    ~Q(subscribed_rank__CC_RANK_list={}) | ~Q(subscribed_rank__CLC_RANK_list={})).order_by('id')
                for dddoc in doctor_liist:
                    cc_add_list = []
                    cc_add_list_write = []
                    clc_add_list = []
                    clc_add_list_write = []
                    city_list = []
                    locality_list = []
                    all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),
                                                                                  doctor_id=dddoc.id)
                    if all_Schedules != []:
                        for sscchh in all_Schedules:
                            key_CLC_RANK_label = Key_CC_RANK_lable = None
                            try:
                                doccategory = Category.objects.get(id=dddoc.category).name
                            except:
                                doccategory = None

                            try:
                                oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                            except:
                                oorg = None
                            if oorg != None and doccategory != None:
                                Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                                key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                                if Key_CC_RANK in dddoc.subscribed_rank['CC_RANK_list']:
                                    if Key_CC_RANK not in cc_add_list:
                                        cc_add_list.append(Key_CC_RANK)
                                        Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                            id=dddoc.category).name + '_' + str(
                                            dddoc.subscribed_rank['CC_RANK_list'][Key_CC_RANK])
                                        cc_add_list_write.append(Key_CC_RANK_lable)
                                        if oorg.city.name not in city_list:
                                            city_list.append(oorg.city.name)

                                if key_CLC_RANK in dddoc.subscribed_rank['CLC_RANK_list']:
                                    if key_CLC_RANK not in clc_add_list:
                                        clc_add_list.append(key_CLC_RANK)
                                        key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                            id=dddoc.category).name + '_' + str(
                                            dddoc.subscribed_rank['CLC_RANK_list'][key_CLC_RANK])
                                        clc_add_list_write.append(key_CLC_RANK_label)
                                        if oorg.city.name not in city_list:
                                            city_list.append(oorg.city.name)
                                        if oorg.locality.name not in locality_list:
                                            locality_list.append(oorg.locality.name)
                        if cc_add_list_write != [] or clc_add_list_write != []:
                            try:
                                doccategory = Category.objects.get(id=dddoc.category).name
                            except:
                                doccategory = 'NA'
                            city_list = ",".join(city_list)
                            locality_list = ",".join(locality_list)
                            if cc_add_list_write == []:
                                cc_add_list_write = 'NA'
                            else:
                                cc_add_list_write = ",".join(cc_add_list_write)
                            if clc_add_list_write == []:
                                clc_add_list_write = 'NA'
                            else:
                                clc_add_list_write = ",".join(clc_add_list_write)
                            if dddoc.stage:
                                stage_name = dddoc.stage.stage_name
                            else:
                                stage_name = 'NA'
                            if dddoc.current_user:
                                cu_name = dddoc.current_user.username
                            else:
                                stage_name = 'NA'
                            doc_name = dddoc.firstName + ' ' + dddoc.lastName

                            report_list.append(
                                [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                 clc_add_list_write, stage_name, cu_name])

            if report_list != []:
                report_list.sort(key=lambda x: x[1])


            # paginator = Paginator(report_list, 100)
            # page = request.GET.get('page')
            # try:
            #     report_list = paginator.page(page)
            # except PageNotAnInteger:
            #     # If page is not an integer, deliver first page.
            #     report_list = paginator.page(1)
            # except EmptyPage:
            #     # If page is out of range (e.g. 9999), deliver last page of results.
            #     report_list = paginator.page(paginator.num_pages)
            return render(request, 'admin/live_doctor_management/subscribed_ranks_report.html',
                          {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                           'city_filter': city_filter,
                           'category_obj': category_obj, 'report_list': report_list,
                           'city_obj': city_obj, 'city_location_filter_length': city_location_filter_length,
                           'category_filter': category_filter, 'city_location_obj': city_location_obj,
                           'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                           'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                           'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

        else:

            filter_name = None
            city_data = None
            city_location_data = None
            category_data = None
            stage_id_data = None
            user_id_data= None
            report_list = []

            doctor_liist = Live_Doctor.objects.filter(~Q(subscribed_rank__CC_RANK_list={})|~Q(subscribed_rank__CLC_RANK_list={})).order_by('id')
            for dddoc in doctor_liist:
                cc_add_list = []
                cc_add_list_write = []
                clc_add_list = []
                clc_add_list_write = []
                city_list = []
                locality_list = []
                all_Schedules = Live_Doctor_Commonworkschedule.objects.filter(~Q(status__iexact='delete'),doctor_id=dddoc.id)
                if all_Schedules != []:
                    for sscchh in all_Schedules:
                        key_CLC_RANK_label =  Key_CC_RANK_lable = None
                        try:
                            doccategory = Category.objects.get(id=dddoc.category).name
                        except:
                            doccategory = None

                        try:
                            oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                        except:
                            oorg = None
                        if oorg != None and doccategory != None:
                            Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category.__str__()
                            key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category.__str__()

                            if Key_CC_RANK in dddoc.subscribed_rank['CC_RANK_list']:
                                if Key_CC_RANK not in cc_add_list:
                                    cc_add_list.append(Key_CC_RANK)
                                    Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(id=dddoc.category).name+'_'+str(dddoc.subscribed_rank['CC_RANK_list'][Key_CC_RANK])
                                    cc_add_list_write.append(Key_CC_RANK_lable)
                                    if oorg.city.name not in city_list:
                                        city_list.append(oorg.city.name)

                            if key_CLC_RANK in dddoc.subscribed_rank['CLC_RANK_list']:
                                if key_CLC_RANK not in clc_add_list:
                                    clc_add_list.append(key_CLC_RANK)
                                    key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                        id=dddoc.category).name +'_'+str(dddoc.subscribed_rank['CLC_RANK_list'][key_CLC_RANK])
                                    clc_add_list_write.append(key_CLC_RANK_label)
                                    if oorg.city.name not in city_list:
                                        city_list.append(oorg.city.name)
                                    if oorg.locality.name not in locality_list:
                                        locality_list.append(oorg.locality.name)
                    if cc_add_list_write != [] or clc_add_list_write != []:
                        try:
                            doccategory = Category.objects.get(id=dddoc.category).name
                        except:
                            doccategory = 'NA'
                        city_list = ",".join(city_list)
                        locality_list = ",".join(locality_list)
                        if cc_add_list_write == []:
                            cc_add_list_write ='NA'
                        else:
                            cc_add_list_write = ",".join(cc_add_list_write)
                        if clc_add_list_write ==[]:
                            clc_add_list_write= 'NA'
                        else:
                            clc_add_list_write = ",".join(clc_add_list_write)
                        if dddoc.stage:
                            stage_name = dddoc.stage.stage_name
                        else:
                            stage_name = 'NA'
                        if dddoc.current_user:
                            cu_name = dddoc.current_user.username
                        else:
                            stage_name = 'NA'
                        doc_name = dddoc.firstName+' '+dddoc.lastName

                        report_list.append([dddoc.id,doc_name,city_list,locality_list,doccategory,cc_add_list_write,clc_add_list_write,stage_name,cu_name])

            if report_list != []:
                report_list.sort(key=lambda x: x[1])
            #paginator = Paginator(doctor_data_obj, 100)
            # paginator = Paginator(report_list, 100)
            # page = request.GET.get('page')
            # try:
            #     report_list = paginator.page(page)
            # except PageNotAnInteger:
            #     # If page is not an integer, deliver first page.
            #     report_list = paginator.page(1)
            # except EmptyPage:
            #     # If page is out of range (e.g. 9999), deliver last page of results.
            #     report_list = paginator.page(paginator.num_pages)
            return render(request, 'admin/live_doctor_management/subscribed_ranks_report.html',
                          {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                           'city_filter': city_filter,'doctor_data_obj':None,
                           'category_obj': category_obj, 'report_list': report_list,
                           'city_obj': city_obj, 'city_location_filter_length': city_location_filter_length,
                           'category_filter': category_filter, 'city_location_obj': city_location_obj,
                           'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                           'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                           'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

    except Exception as e:
        raise Http404

#^^^^^^^^^^^^^^^^^^^^^^##########^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^





#@^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^$$$$$$^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
####################################################################
# Name - doctor_sponsored_ranks_report                             #
# By Nishank                                                       #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
#@require_GET
def doctor_sponsored_ranks_report(request):
    try:
        doccategory = None
        lldoc = None
        report_list = []

        city_filter = False
        stage_filter = False
        user_filter = False
        city_location_filter_length = False
        category_filter = False
        #stage_data = Stage.objects.all()[:4]
        stage_data = Stage.objects.all()
        user_data = User.objects.all().order_by('username')
        city_obj = City.objects.filter(delete=False).order_by('name')
        city_location_obj = {}
        category_obj = Category.objects.filter(delete=False).order_by('name')
        search_data=None
        search_data = request.GET.get('search_data')
        mpty = []
        del_sch_mainlist = []
        # if search_data :
        #     doctor_data_obj = Live_Doctor.objects.all()
        #     mpty =[]
        #     for ld in doctor_data_obj:
        #         fulln = ''
        #         fulln = ld.firstName + ' ' +ld.lastName
        #         if search_data.lower() in fulln.lower():
        #             mpty.append(ld)
        #     mpty = [x.id for x in mpty]
        #     all_deleted_Schedules = Live_Doctor_Commonworkschedule.objects.filter(status__iexact='delete',doctor_id__in=mpty)
        #
        #     for sscchh in all_deleted_Schedules:
        #         lldoc = Live_Doctor.objects.get(id=sscchh.doctor_id)
        #         try:
        #             doccategory = Category.objects.get(id=lldoc.category).name
        #         except:
        #             doccategory = None
        #
        #         try:
        #             oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
        #         except:
        #             oorg = None
        #         if oorg != None and doccategory != None:
        #             Key_CC_RANK = oorg.city_id.__str__() + '-' + lldoc.category.__str__()
        #             key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + lldoc.category.__str__()
        #             Spon_cc =  lldoc.sponsored_rank['CC_RANK_list'].get(Key_CC_RANK,'DoesNotExist')
        #             Spon_clc = lldoc.sponsored_rank['CLC_RANK_list'].get(key_CLC_RANK,'DoesNotExist')
        #             Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(id=lldoc.category).name
        #             key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(id=lldoc.category).name
        #             if Spon_cc == 'DoesNotExist' and Spon_clc == 'DoesNotExist':
        #                 pass
        #             else:
        #                 if Spon_cc == 'DoesNotExist':
        #                     Spon_cc = None
        #                 if Spon_clc == 'DoesNotExist':
        #                     Spon_clc = None
        #                 del_sch_mainlist.append([lldoc,doccategory,oorg,Spon_cc,Spon_clc,Key_CC_RANK,key_CLC_RANK,lldoc.firstName,
        #                                          Key_CC_RANK_lable,key_CLC_RANK_label])
        #     if report_list != []:
        #         report_list.sort(key=lambda x: x[1])
        #
        #     paginator = Paginator(report_list, 100)
        #     page = request.GET.get('page')
        #     try:
        #         report_list = paginator.page(page)
        #     except PageNotAnInteger:
        #         # If page is not an integer, deliver first page.
        #         report_list = paginator.page(1)
        #     except EmptyPage:
        #         # If page is out of range (e.g. 9999), deliver last page of results.
        #         report_list = paginator.page(paginator.num_pages)
        #     return render(request, 'admin/live_doctor_management/sponsored_rank_report.html',
        #                   {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
        #                    'city_filter': city_filter,
        #                    'category_obj': category_obj, 'report_list': report_list,
        #                    'city_obj': city_obj, 'city_location_filter_length': city_location_filter_length,
        #                    'category_filter': category_filter, 'city_location_obj': city_location_obj,
        #                    'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
        #                    'search_data':search_data})
        try:
            filter_name = str(request.GET['x'].strip())
        except:
            filter_name = None
        if filter_name == 'filter':
            city_data = request.GET['city'].strip()
            if city_data:
                city_filter = city_data
            try:
                city_location_data = request.GET['city_location'].strip()
            except:
                city_location_data = 0
            try:
                stage_id_data = request.GET['stage_da'].strip()
            except:
                stage_id_data = 0
            try:
                user_id_data = request.GET['user_da'].strip()
            except:
                user_id_data = 0
            if stage_id_data:
                stage_filter = int(stage_id_data)
            if user_id_data:
                user_filter = int(user_id_data)
            if city_location_data:
                city_location_filter_length = int(city_location_data)
                city_location_obj = Locality.objects.filter(delete=False)

            category_data = request.GET['category'].strip()
            if category_data:
                category_filter = int(category_data)
            if city_data and category_data:
                if city_location_data and stage_id_data and user_id_data:
                    doctor_liist = Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),stage=int(stage_id_data),category=int(category_data),current_user=int(user_id_data)).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),locality_id= int(city_location_data)).values_list('id',flat=True)

                        all_Schedules = AttachWithDoctor.objects.filter(doctor_id=dddoc.id,organisation_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.organisation_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category_id.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category_id.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.name

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                    if report_list != []:
                        report_list.sort(key=lambda x: x[1])

                    # paginator = Paginator(report_list, 100)
                    # page = request.GET.get('page')
                    # try:
                    #     report_list = paginator.page(page)
                    # except PageNotAnInteger:
                    #     # If page is not an integer, deliver first page.
                    #     report_list = paginator.page(1)
                    # except EmptyPage:
                    #     # If page is out of range (e.g. 9999), deliver last page of results.
                    #     report_list = paginator.page(paginator.num_pages)
                    return render(request, 'admin/doctor_management/sponsored_rank_report.html',
                                  {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                                   'city_filter': city_filter,
                                   'category_obj': category_obj, 'report_list': report_list,
                                   'city_obj': city_obj,
                                   'city_location_filter_length': city_location_filter_length,
                                   'category_filter': category_filter, 'city_location_obj': city_location_obj,
                                   'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })


                elif city_location_data and stage_id_data:
                    doctor_liist = Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data), category=int(category_data)).order_by(
                        'id')
                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),locality_id= int(city_location_data)).values_list('id',flat=True)

                        all_Schedules = AttachWithDoctor.objects.filter(doctor_id=dddoc.id,organisation_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.organisation_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category_id.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category_id.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.name

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])


                elif city_location_data and user_id_data:
                    doctor_liist = Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        category=int(category_data), current_user=int(user_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),
                                                                      locality_id=int(city_location_data)).values_list('id',
                                                                                                                  flat=True)

                        all_Schedules = AttachWithDoctor.objects.filter(doctor_id=dddoc.id,
                                                                        organisation_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.organisation_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category_id.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category_id.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.categoryv).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.name

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                elif stage_id_data and user_id_data:

                    doctor_liist = Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data), category=int(category_data), current_user=int(user_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data)).values_list('id',flat=True)

                        all_Schedules = AttachWithDoctor.objects.filter(doctor_id=dddoc.id,
                                                                        organisation_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.organisation_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category_id.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category_id.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.name

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                    if report_list != []:
                        report_list.sort(key=lambda x: x[1])

                    # paginator = Paginator(report_list, 100)
                    # page = request.GET.get('page')
                    # try:
                    #     report_list = paginator.page(page)
                    # except PageNotAnInteger:
                    #     # If page is not an integer, deliver first page.
                    #     report_list = paginator.page(1)
                    # except EmptyPage:
                    #     # If page is out of range (e.g. 9999), deliver last page of results.
                    #     report_list = paginator.page(paginator.num_pages)
                    return render(request, 'admin/doctor_management/sponsored_rank_report.html',
                                  {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                                   'city_filter': city_filter,
                                   'category_obj': category_obj, 'report_list': report_list,
                                   'city_obj': city_obj,
                                   'city_location_filter_length': city_location_filter_length,
                                   'category_filter': category_filter, 'city_location_obj': city_location_obj,
                                   'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

                elif stage_id_data:
                    doctor_liist = Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data), category=int(category_data)).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data)).values_list('id', flat=True)

                        all_Schedules = AttachWithDoctor.objects.filter(doctor_id=dddoc.id,
                                                                        organisation_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.organisation_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category_id.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category_id.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.name

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                elif city_location_data:
                    doctor_liist = Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                         category=int(category_data)).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),locality_id= int(city_location_data)).values_list('id', flat=True)

                        all_Schedules = AttachWithDoctor.objects.filter(doctor_id=dddoc.id,
                                                                        organisation_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.organisation_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category_id.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category_id.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.name

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])



                elif user_id_data:
                    doctor_liist = Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                         category=int(category_data), current_user=int(user_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data)).values_list('id',flat=True)

                        all_Schedules = AttachWithDoctor.objects.filter(doctor_id=dddoc.id,
                                                                        organisation_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.organisation_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category_id.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category_id.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.name

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                else:
                    doctor_liist = Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        category=int(category_data)).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data)).values_list('id',flat=True)

                        all_Schedules = AttachWithDoctor.objects.filter(doctor_id=dddoc.id,
                                                                        organisation_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.organisation_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category_id.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category_id.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.name

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])
                if report_list != []:
                    report_list.sort(key=lambda x: x[1])


                # paginator = Paginator(report_list, 100)
                # page = request.GET.get('page')
                # try:
                #     report_list = paginator.page(page)
                # except PageNotAnInteger:
                #     # If page is not an integer, deliver first page.
                #     report_list = paginator.page(1)
                # except EmptyPage:
                #     # If page is out of range (e.g. 9999), deliver last page of results.
                #     report_list = paginator.page(paginator.num_pages)
                return render(request, 'admin/doctor_management/sponsored_rank_report.html',
                              {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                               'city_filter': city_filter,
                               'category_obj': category_obj, 'report_list': report_list,
                               'city_obj': city_obj, 'city_location_filter_length': city_location_filter_length,
                               'category_filter': category_filter, 'city_location_obj': city_location_obj,
                               'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })
            elif category_data:
                if stage_id_data and user_id_data:

                    doctor_liist = Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data), category=int(category_data), current_user=int(user_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        # filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),
                        #                                               locality_id=int(city_location_data)).values('id',
                        #                                                                                           flat=True)

                        all_Schedules = AttachWithDoctor.objects.filter(doctor_id=dddoc.id)

                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.organisation_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category_id.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category_id.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.name

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])


                    if report_list != []:
                        report_list.sort(key=lambda x: x[1])
                    # paginator = Paginator(report_list, 100)
                    # page = request.GET.get('page')
                    # try:
                    #     report_list = paginator.page(page)
                    # except PageNotAnInteger:
                    #     # If page is not an integer, deliver first page.
                    #     report_list = paginator.page(1)
                    # except EmptyPage:
                    #     # If page is out of range (e.g. 9999), deliver last page of results.
                    #     report_list = paginator.page(paginator.num_pages)
                    return render(request, 'admin/doctor_management/sponsored_rank_report.html',
                                  {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                                   'city_filter': city_filter,
                                   'category_obj': category_obj, 'report_list': report_list,
                                   'city_obj': city_obj,
                                   'city_location_filter_length': city_location_filter_length,
                                   'category_filter': category_filter, 'city_location_obj': city_location_obj,
                                   'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

                elif stage_id_data:
                    doctor_liist = Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data), category=int(category_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []


                        all_Schedules = AttachWithDoctor.objects.filter(doctor_id=dddoc.id)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.organisation_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category_id.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category_id.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.name

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                elif user_id_data:
                    doctor_liist = Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        category=int(category_data), current_user=int(user_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []

                        all_Schedules = AttachWithDoctor.objects.filter(doctor_id=dddoc.id)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.organisation_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category_id.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category_id.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.name

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])


                else:
                    doctor_liist = Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        category=int(category_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []

                        all_Schedules = AttachWithDoctor.objects.filter(doctor_id=dddoc.id)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.organisation_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category_id.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category_id.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.name

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])


                if report_list != []:
                    report_list.sort(key=lambda x: x[1])

                # paginator = Paginator(report_list, 100)
                # page = request.GET.get('page')
                # try:
                #     report_list = paginator.page(page)
                # except PageNotAnInteger:
                #     # If page is not an integer, deliver first page.
                #     report_list = paginator.page(1)
                # except EmptyPage:
                #     # If page is out of range (e.g. 9999), deliver last page of results.
                #     report_list = paginator.page(paginator.num_pages)
                return render(request, 'admin/doctor_management/sponsored_rank_report.html',
                              {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                               'city_filter': city_filter,
                               'category_obj': category_obj, 'report_list': report_list,
                               'city_obj': city_obj,
                               'city_location_filter_length': city_location_filter_length,
                               'category_filter': category_filter, 'city_location_obj': city_location_obj,
                               'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

            elif city_data and city_location_data:
                if stage_id_data and user_id_data:

                    doctor_liist = Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data),current_user=int(user_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),
                                                                      locality_id=int(city_location_data)).values_list('id',
                                                                                                                  flat=True)

                        all_Schedules = AttachWithDoctor.objects.filter(doctor_id=dddoc.id,
                                                                        organisation_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.organisation_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category_id.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category_id.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.name

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])


                    if report_list != []:
                        report_list.sort(key=lambda x: x[1])

                    # paginator = Paginator(report_list, 100)
                    # page = request.GET.get('page')
                    # try:
                    #     report_list = paginator.page(page)
                    # except PageNotAnInteger:
                    #     # If page is not an integer, deliver first page.
                    #     report_list = paginator.page(1)
                    # except EmptyPage:
                    #     # If page is out of range (e.g. 9999), deliver last page of results.
                    #     report_list = paginator.page(paginator.num_pages)
                    return render(request, 'admin/doctor_management/sponsored_rank_report.html',
                                  {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                                   'city_filter': city_filter,
                                   'category_obj': category_obj, 'report_list': report_list,
                                   'city_obj': city_obj,
                                   'city_location_filter_length': city_location_filter_length,
                                   'category_filter': category_filter, 'city_location_obj': city_location_obj,
                                   'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

                elif stage_id_data:
                    doctor_liist = Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),
                                                                      locality_id=int(city_location_data)).values_list('id',
                                                                                                                  flat=True)

                        all_Schedules = AttachWithDoctor.objects.filter(doctor_id=dddoc.id,
                                                                        organisation_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.organisation_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category_id.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category_id.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.name

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                elif user_id_data:

                    doctor_liist = Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                         current_user=int(user_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),
                                                                      locality_id=int(city_location_data)).values_list('id',
                                                                                                                  flat=True)

                        all_Schedules = AttachWithDoctor.objects.filter(doctor_id=dddoc.id,
                                                                        organisation_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.organisation_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category_id.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category_id.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.name

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                else:

                    doctor_liist = Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={})).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),
                                                                      locality_id=int(city_location_data)).values_list('id',
                                                                                                                  flat=True)

                        all_Schedules = AttachWithDoctor.objects.filter(doctor_id=dddoc.id,
                                                                        organisation_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.organisation_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category_id.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category_id.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.name

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                if report_list != []:
                    report_list.sort(key=lambda x: x[1])

                # paginator = Paginator(report_list, 100)
                # page = request.GET.get('page')
                # try:
                #     report_list = paginator.page(page)
                # except PageNotAnInteger:
                #     # If page is not an integer, deliver first page.
                #     report_list = paginator.page(1)
                # except EmptyPage:
                #     # If page is out of range (e.g. 9999), deliver last page of results.
                #     report_list = paginator.page(paginator.num_pages)
                return render(request, 'admin/doctor_management/sponsored_rank_report.html',
                              {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                               'city_filter': city_filter,
                               'category_obj': category_obj, 'report_list': report_list,
                               'city_obj': city_obj, 'city_location_filter_length': city_location_filter_length,
                               'category_filter': category_filter, 'city_location_obj': city_location_obj,
                               'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                               'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                               'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

            elif city_data:
                if stage_id_data and user_id_data:

                    doctor_liist = Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data), current_user=int(user_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data)).values_list('id',flat=True)

                        all_Schedules = AttachWithDoctor.objects.filter(doctor_id=dddoc.id,
                                                                        organisation_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.organisation_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category_id.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category_id.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.name

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                    if report_list != []:
                        report_list.sort(key=lambda x: x[1])


                    # paginator = Paginator(report_list, 100)
                    # page = request.GET.get('page')
                    # try:
                    #     report_list = paginator.page(page)
                    # except PageNotAnInteger:
                    #     # If page is not an integer, deliver first page.
                    #     report_list = paginator.page(1)
                    # except EmptyPage:
                    #     # If page is out of range (e.g. 9999), deliver last page of results.
                    #     report_list = paginator.page(paginator.num_pages)
                    return render(request, 'admin/doctor_management/sponsored_rank_report.html',
                                  {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                                   'city_filter': city_filter,
                                   'category_obj': category_obj, 'report_list': report_list,
                                   'city_obj': city_obj,
                                   'city_location_filter_length': city_location_filter_length,
                                   'category_filter': category_filter, 'city_location_obj': city_location_obj,
                                   'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

                elif stage_id_data:

                    doctor_liist = Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data)).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data),).values_list('id',flat=True)

                        all_Schedules = AttachWithDoctor.objects.filter(doctor_id=dddoc.id,
                                                                        organisation_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.organisation_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category_id.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category_id.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.name

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                elif user_id_data:

                    doctor_liist = Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                         current_user=int(user_id_data)).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data)).values_list('id',flat=True)

                        all_Schedules = AttachWithDoctor.objects.filter(doctor_id=dddoc.id,
                                                                        organisation_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.organisation_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category_id.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category_id.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.name

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                else:
                    doctor_liist = Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={})).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []
                        filter_orgs = OrganisationName.objects.filter(city_id=int(city_data)).values_list('id',flat=True)

                        all_Schedules = AttachWithDoctor.objects.filter(doctor_id=dddoc.id,
                                                                        organisation_id__in=filter_orgs)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.organisation_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category_id.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category_id.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.name

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])


                if report_list != []:
                    report_list.sort(key=lambda x: x[1])

                # paginator = Paginator(report_list, 100)
                # page = request.GET.get('page')
                # try:
                #     report_list = paginator.page(page)
                # except PageNotAnInteger:
                #     # If page is not an integer, deliver first page.
                #     report_list = paginator.page(1)
                # except EmptyPage:
                #     # If page is out of range (e.g. 9999), deliver last page of results.
                #     report_list = paginator.page(paginator.num_pages)
                return render(request, 'admin/doctor_management/sponsored_rank_report.html',
                              {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                               'city_filter': city_filter,
                               'category_obj': category_obj, 'report_list': report_list,
                               'city_obj': city_obj, 'city_location_filter_length': city_location_filter_length,
                               'category_filter': category_filter, 'city_location_obj': city_location_obj,
                               'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                               'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                               'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

            elif stage_id_data or user_id_data:
                if stage_id_data and user_id_data:

                    doctor_liist = Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data), current_user=int(user_id_data)).order_by(
                        'id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []

                        all_Schedules = AttachWithDoctor.objects.filter(doctor_id=dddoc.id)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.organisation_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category_id.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category_id.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.name

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                    if report_list != []:
                        report_list.sort(key=lambda x: x[1])

                    # paginator = Paginator(report_list, 100)
                    # page = request.GET.get('page')
                    # try:
                    #     report_list = paginator.page(page)
                    # except PageNotAnInteger:
                    #     # If page is not an integer, deliver first page.
                    #     report_list = paginator.page(1)
                    # except EmptyPage:
                    #     # If page is out of range (e.g. 9999), deliver last page of results.
                    #     report_list = paginator.page(paginator.num_pages)
                    return render(request, 'admin/doctor_management/sponsored_rank_report.html',
                                  {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                                   'city_filter': city_filter,
                                   'category_obj': category_obj, 'report_list': report_list,
                                   'city_obj': city_obj,
                                   'city_location_filter_length': city_location_filter_length,
                                   'category_filter': category_filter, 'city_location_obj': city_location_obj,
                                   'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

                elif stage_id_data:

                    doctor_liist = Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        stage=int(stage_id_data)).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []

                        all_Schedules = AttachWithDoctor.objects.filter(doctor_id=dddoc.id)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.organisation_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category_id.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category_id.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.name

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                elif user_id_data:

                    doctor_liist = Doctor.objects.filter(
                        ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={}),
                        current_user=int(user_id_data)).order_by('id')

                    for dddoc in doctor_liist:
                        cc_add_list = []
                        cc_add_list_write = []
                        clc_add_list = []
                        clc_add_list_write = []
                        city_list = []
                        locality_list = []

                        all_Schedules = AttachWithDoctor.objects.filter(doctor_id=dddoc.id)
                        if all_Schedules != []:
                            for sscchh in all_Schedules:
                                key_CLC_RANK_label = Key_CC_RANK_lable = None
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = None

                                try:
                                    oorg = OrganisationName.objects.get(id=sscchh.organisation_id)
                                except:
                                    oorg = None
                                if oorg != None and doccategory != None:
                                    Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category_id.__str__()
                                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category_id.__str__()

                                    if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                        if Key_CC_RANK not in cc_add_list:
                                            cc_add_list.append(Key_CC_RANK)
                                            Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                            cc_add_list_write.append(Key_CC_RANK_lable)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)

                                    if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                        if key_CLC_RANK not in clc_add_list:
                                            clc_add_list.append(key_CLC_RANK)
                                            key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                                id=dddoc.category_id).name + '_' + str(
                                                dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                            clc_add_list_write.append(key_CLC_RANK_label)
                                            if oorg.city.name not in city_list:
                                                city_list.append(oorg.city.name)
                                            if oorg.locality.name not in locality_list:
                                                locality_list.append(oorg.locality.name)
                            if cc_add_list_write != [] or clc_add_list_write != []:
                                try:
                                    doccategory = Category.objects.get(id=dddoc.category_id).name
                                except:
                                    doccategory = 'NA'
                                city_list = ",".join(city_list)
                                locality_list = ",".join(locality_list)
                                if cc_add_list_write == []:
                                    cc_add_list_write = 'NA'
                                else:
                                    cc_add_list_write = ",".join(cc_add_list_write)
                                if clc_add_list_write == []:
                                    clc_add_list_write = 'NA'
                                else:
                                    clc_add_list_write = ",".join(clc_add_list_write)
                                if dddoc.stage:
                                    stage_name = dddoc.stage.stage_name
                                else:
                                    stage_name = 'NA'
                                if dddoc.current_user:
                                    cu_name = dddoc.current_user.username
                                else:
                                    stage_name = 'NA'
                                doc_name = dddoc.name

                                report_list.append(
                                    [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                     clc_add_list_write, stage_name, cu_name])

                # else:
                #     pass
            else:
                doctor_liist = Doctor.objects.filter(
                    ~Q(sponsored_rank__CC_RANK_list={}) | ~Q(sponsored_rank__CLC_RANK_list={})).order_by('id')
                for dddoc in doctor_liist:
                    cc_add_list = []
                    cc_add_list_write = []
                    clc_add_list = []
                    clc_add_list_write = []
                    city_list = []
                    locality_list = []
                    all_Schedules = AttachWithDoctor.objects.filter(doctor_id=dddoc.id)
                    if all_Schedules != []:
                        for sscchh in all_Schedules:
                            key_CLC_RANK_label = Key_CC_RANK_lable = None
                            try:
                                doccategory = Category.objects.get(id=dddoc.category_id).name
                            except:
                                doccategory = None

                            try:
                                oorg = OrganisationName.objects.get(id=sscchh.organisation_id)
                            except:
                                oorg = None
                            if oorg != None and doccategory != None:
                                Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category_id.__str__()
                                key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category_id.__str__()

                                if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                    if Key_CC_RANK not in cc_add_list:
                                        cc_add_list.append(Key_CC_RANK)
                                        Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(
                                            id=dddoc.category_id).name + '_' + str(
                                            dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                        cc_add_list_write.append(Key_CC_RANK_lable)
                                        if oorg.city.name not in city_list:
                                            city_list.append(oorg.city.name)

                                if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                    if key_CLC_RANK not in clc_add_list:
                                        clc_add_list.append(key_CLC_RANK)
                                        key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                            id=dddoc.category_id).name + '_' + str(
                                            dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                        clc_add_list_write.append(key_CLC_RANK_label)
                                        if oorg.city.name not in city_list:
                                            city_list.append(oorg.city.name)
                                        if oorg.locality.name not in locality_list:
                                            locality_list.append(oorg.locality.name)
                        if cc_add_list_write != [] or clc_add_list_write != []:
                            try:
                                doccategory = Category.objects.get(id=dddoc.category_id).name
                            except:
                                doccategory = 'NA'
                            city_list = ",".join(city_list)
                            locality_list = ",".join(locality_list)
                            if cc_add_list_write == []:
                                cc_add_list_write = 'NA'
                            else:
                                cc_add_list_write = ",".join(cc_add_list_write)
                            if clc_add_list_write == []:
                                clc_add_list_write = 'NA'
                            else:
                                clc_add_list_write = ",".join(clc_add_list_write)
                            if dddoc.stage:
                                stage_name = dddoc.stage.stage_name
                            else:
                                stage_name = 'NA'
                            if dddoc.current_user:
                                cu_name = dddoc.current_user.username
                            else:
                                stage_name = 'NA'
                            doc_name = dddoc.name

                            report_list.append(
                                [dddoc.id, doc_name, city_list, locality_list, doccategory, cc_add_list_write,
                                 clc_add_list_write, stage_name, cu_name])

            if report_list != []:
                report_list.sort(key=lambda x: x[1])


            # paginator = Paginator(report_list, 100)
            # page = request.GET.get('page')
            # try:
            #     report_list = paginator.page(page)
            # except PageNotAnInteger:
            #     # If page is not an integer, deliver first page.
            #     report_list = paginator.page(1)
            # except EmptyPage:
            #     # If page is out of range (e.g. 9999), deliver last page of results.
            #     report_list = paginator.page(paginator.num_pages)
            return render(request, 'admin/doctor_management/sponsored_rank_report.html',
                          {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                           'city_filter': city_filter,
                           'category_obj': category_obj, 'report_list': report_list,
                           'city_obj': city_obj, 'city_location_filter_length': city_location_filter_length,
                           'category_filter': category_filter, 'city_location_obj': city_location_obj,
                           'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                           'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                           'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

        else:

            filter_name = None
            city_data = None
            city_location_data = None
            category_data = None
            stage_id_data = None
            user_id_data= None
            report_list = []

            doctor_liist = Doctor.objects.filter(~Q(sponsored_rank__CC_RANK_list={})|~Q(sponsored_rank__CLC_RANK_list={})).order_by('id')
            for dddoc in doctor_liist:
                cc_add_list = []
                cc_add_list_write = []
                clc_add_list = []
                clc_add_list_write = []
                city_list = []
                locality_list = []
                all_Schedules = AttachWithDoctor.objects.filter(doctor_id=dddoc.id)
                if all_Schedules != []:
                    for sscchh in all_Schedules:
                        key_CLC_RANK_label =  Key_CC_RANK_lable = None
                        try:
                            doccategory = Category.objects.get(id=dddoc.category_id).name
                        except:
                            doccategory = None

                        try:
                            oorg = OrganisationName.objects.get(id=sscchh.organisation_id)
                        except:
                            oorg = None
                        if oorg != None and doccategory != None:
                            Key_CC_RANK = oorg.city_id.__str__() + '-' + dddoc.category_id.__str__()
                            key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + dddoc.category_id.__str__()

                            if Key_CC_RANK in dddoc.sponsored_rank['CC_RANK_list']:
                                if Key_CC_RANK not in cc_add_list:
                                    cc_add_list.append(Key_CC_RANK)
                                    Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(id=dddoc.category_id).name+'_'+str(dddoc.sponsored_rank['CC_RANK_list'][Key_CC_RANK])
                                    cc_add_list_write.append(Key_CC_RANK_lable)
                                    if oorg.city.name not in city_list:
                                        city_list.append(oorg.city.name)

                            if key_CLC_RANK in dddoc.sponsored_rank['CLC_RANK_list']:
                                if key_CLC_RANK not in clc_add_list:
                                    clc_add_list.append(key_CLC_RANK)
                                    key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                                        id=dddoc.category_id).name +'_'+str(dddoc.sponsored_rank['CLC_RANK_list'][key_CLC_RANK])
                                    clc_add_list_write.append(key_CLC_RANK_label)
                                    if oorg.city.name not in city_list:
                                        city_list.append(oorg.city.name)
                                    if oorg.locality.name not in locality_list:
                                        locality_list.append(oorg.locality.name)
                    if cc_add_list_write != [] or clc_add_list_write != []:
                        try:
                            doccategory = Category.objects.get(id=dddoc.category_id).name
                        except:
                            doccategory = 'NA'
                        city_list = ",".join(city_list)
                        locality_list = ",".join(locality_list)
                        if cc_add_list_write == []:
                            cc_add_list_write ='NA'
                        else:
                            cc_add_list_write = ",".join(cc_add_list_write)
                        if clc_add_list_write ==[]:
                            clc_add_list_write= 'NA'
                        else:
                            clc_add_list_write = ",".join(clc_add_list_write)
                        if dddoc.stage:
                            stage_name = dddoc.stage.stage_name
                        else:
                            stage_name = 'NA'
                        if dddoc.current_user:
                            cu_name = dddoc.current_user.username
                        else:
                            stage_name = 'NA'
                        doc_name = dddoc.name

                        report_list.append([dddoc.id,doc_name,city_list,locality_list,doccategory,cc_add_list_write,clc_add_list_write,stage_name,cu_name])

            if report_list != []:
                report_list.sort(key=lambda x: x[1])
            #paginator = Paginator(doctor_data_obj, 100)
            # paginator = Paginator(report_list, 100)
            # page = request.GET.get('page')
            # try:
            #     report_list = paginator.page(page)
            # except PageNotAnInteger:
            #     # If page is not an integer, deliver first page.
            #     report_list = paginator.page(1)
            # except EmptyPage:
            #     # If page is out of range (e.g. 9999), deliver last page of results.
            #     report_list = paginator.page(paginator.num_pages)
            return render(request, 'admin/doctor_management/sponsored_rank_report.html',
                          {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                           'city_filter': city_filter,'doctor_data_obj':None,
                           'category_obj': category_obj, 'report_list': report_list,
                           'city_obj': city_obj, 'city_location_filter_length': city_location_filter_length,
                           'category_filter': category_filter, 'city_location_obj': city_location_obj,
                           'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                           'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                           'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

    except Exception as e:
        raise Http404


####################################################################
# name doc_schedule_stopdate_notification                          #
# owner Nishank                                                    #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def doc_schedule_stopdate_notification(request):
    try:
        tab = 1
        doc_schedule_notifications = Doctor_Schedule_Stopdate_Notification.objects.all().order_by(
            '-notification_creation_date')
        paginator = Paginator(doc_schedule_notifications, 100)
        page = request.GET.get('page')
        try:
            doc_schedule_notifications = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            doc_schedule_notifications = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            doc_schedule_notifications = paginator.page(paginator.num_pages)
        return render(request, 'admin/doctor_management/doc_schedule_stopdate_notification.html',
                      {'tab': tab,
                       'doc_schedule_notifications': doc_schedule_notifications, 'back_button': 'no'})
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



#@^^^^^^^^^^^^^^^^^^^^^^^^^^^^^$%$%$$%^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
####################################################################
# Name - doctor_sponsored_ranks_deleted_schedules                  #
# By Nishank                                                       #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
#@require_GET
def doctor_sponsored_ranks_deleted_schedules(request):
    try:
        city_filter = False
        stage_filter = False
        user_filter = False
        city_location_filter_length = False
        category_filter = False
        #stage_data = Stage.objects.all()[:4]
        stage_data = Stage.objects.all()
        user_data = User.objects.all().order_by('username')
        city_obj = City.objects.filter(delete=False).order_by('name')
        city_location_obj = {}
        category_obj = Category.objects.filter(delete=False).order_by('name')
        search_data=None
        search_data = request.GET.get('search_data')
        mpty = []
        del_sch_mainlist = []
        if search_data :
            del_sch_mainlist = Doctor_Schedule_Delete_Notification.objects.filter(doctorName__icontains=search_data)

            if del_sch_mainlist != []:
                del_sch_mainlist = list(del_sch_mainlist)
                del_sch_mainlist.sort(key=lambda x: x.doctorName)

            paginator = Paginator(del_sch_mainlist, 100)
            page = request.GET.get('page')
            try:
                del_sch_mainlist = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                del_sch_mainlist = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                del_sch_mainlist = paginator.page(paginator.num_pages)
            return render(request, 'admin/doctor_management/doctor_sponsored_rank_deleted_schedules.html',
                          {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                           'city_filter': city_filter,
                           'category_obj': category_obj, 'del_sch_mainlist': del_sch_mainlist,
                           'city_obj': city_obj, 'city_location_filter_length': city_location_filter_length,
                           'category_filter': category_filter, 'city_location_obj': city_location_obj,
                           'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                           'search_data':search_data})
        try:
            filter_name = str(request.GET['x'].strip())
        except:
            filter_name = None
        if filter_name == 'filter':
            city_data = request.GET['city'].strip()
            if city_data:
                city_filter = city_data
            try:
                city_location_data = request.GET['city_location'].strip()
            except:
                city_location_data = 0
            try:
                stage_id_data = request.GET['stage_da'].strip()
            except:
                stage_id_data = 0
            try:
                user_id_data = request.GET['user_da'].strip()
            except:
                user_id_data = 0
            if stage_id_data:
                stage_filter = int(stage_id_data)
            if user_id_data:
                user_filter = int(user_id_data)
            if city_location_data:
                city_location_filter_length = int(city_location_data)
                city_location_obj = Locality.objects.filter(delete=False)

            category_data = request.GET['category'].strip()
            if category_data:
                category_filter = int(category_data)
            if city_data and category_data:
                if city_location_data and stage_id_data and user_id_data:
                    del_sch_mainlist = Doctor_Schedule_Delete_Notification.objects.filter(doctor__category_id=int(category_data),
                                                                                          clinic__city_id=int(city_data),
                                                                                          doctor__stage_id=int(stage_id_data),
                                                                                          doctor__current_user_id=int(user_id_data),
                                                                                          clinic__locality_id=int(city_location_data),
                                                                                          )

                    if del_sch_mainlist != []:
                        del_sch_mainlist = list(del_sch_mainlist)
                        del_sch_mainlist.sort(key=lambda x: x.doctorName)

                    paginator = Paginator(del_sch_mainlist, 100)
                    page = request.GET.get('page')
                    try:
                        del_sch_mainlist = paginator.page(page)
                    except PageNotAnInteger:
                        # If page is not an integer, deliver first page.
                        del_sch_mainlist = paginator.page(1)
                    except EmptyPage:
                        # If page is out of range (e.g. 9999), deliver last page of results.
                        del_sch_mainlist = paginator.page(paginator.num_pages)
                    return render(request, 'admin/doctor_management/doctor_sponsored_rank_deleted_schedules.html',
                                  {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                                   'city_filter': city_filter,
                                   'category_obj': category_obj, 'del_sch_mainlist': del_sch_mainlist,
                                   'city_obj': city_obj,
                                   'city_location_filter_length': city_location_filter_length,
                                   'category_filter': category_filter, 'city_location_obj': city_location_obj,
                                   'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })


                elif city_location_data and stage_id_data:
                    del_sch_mainlist = Doctor_Schedule_Delete_Notification.objects.filter(
                        doctor__category_id=int(category_data),
                        clinic__city_id=int(city_data),
                        doctor__stage_id=int(stage_id_data),
                        clinic__locality_id=int(city_location_data),
                        )

                    if del_sch_mainlist != []:
                        del_sch_mainlist = list(del_sch_mainlist)
                        del_sch_mainlist.sort(key=lambda x: x.doctorName)

                elif city_location_data and user_id_data:
                    del_sch_mainlist = Doctor_Schedule_Delete_Notification.objects.filter(
                        doctor__category_id=int(category_data),
                        clinic__city_id=int(city_data),
                        doctor__current_user_id=int(user_id_data),
                        clinic__locality_id=int(city_location_data),
                        )

                    if del_sch_mainlist != []:
                        del_sch_mainlist = list(del_sch_mainlist)
                        del_sch_mainlist.sort(key=lambda x: x.doctorName)

                elif stage_id_data and user_id_data:
                    del_sch_mainlist = Doctor_Schedule_Delete_Notification.objects.filter(
                        doctor__category_id=int(category_data),
                        clinic__city_id=int(city_data),
                        doctor__stage_id=int(stage_id_data),
                        doctor__current_user_id=int(user_id_data)
                        )

                    if del_sch_mainlist != []:
                        del_sch_mainlist = list(del_sch_mainlist)
                        del_sch_mainlist.sort(key=lambda x: x.doctorName)

                    paginator = Paginator(del_sch_mainlist, 100)
                    page = request.GET.get('page')
                    try:
                        del_sch_mainlist = paginator.page(page)
                    except PageNotAnInteger:
                        # If page is not an integer, deliver first page.
                        del_sch_mainlist = paginator.page(1)
                    except EmptyPage:
                        # If page is out of range (e.g. 9999), deliver last page of results.
                        del_sch_mainlist = paginator.page(paginator.num_pages)
                    return render(request, 'admin/doctor_management/doctor_sponsored_rank_deleted_schedules.html',
                                  {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                                   'city_filter': city_filter,
                                   'category_obj': category_obj, 'del_sch_mainlist': del_sch_mainlist,
                                   'city_obj': city_obj,
                                   'city_location_filter_length': city_location_filter_length,
                                   'category_filter': category_filter, 'city_location_obj': city_location_obj,
                                   'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

                elif stage_id_data:
                    del_sch_mainlist = Doctor_Schedule_Delete_Notification.objects.filter(
                        doctor__category_id=int(category_data),
                        clinic__city_id=int(city_data),
                        doctor__stage_id=int(stage_id_data)
                        )

                    if del_sch_mainlist != []:
                        del_sch_mainlist = list(del_sch_mainlist)
                        del_sch_mainlist.sort(key=lambda x: x.doctorName)

                elif city_location_data:
                    del_sch_mainlist = Doctor_Schedule_Delete_Notification.objects.filter(
                        doctor__category_id=int(category_data),
                        clinic__city_id=int(city_data),
                        clinic__locality_id=int(city_location_data)
                        )

                    if del_sch_mainlist != []:
                        del_sch_mainlist = list(del_sch_mainlist)
                        del_sch_mainlist.sort(key=lambda x: x.doctorName)


                elif user_id_data:
                    del_sch_mainlist = Doctor_Schedule_Delete_Notification.objects.filter(
                        doctor__category_id=int(category_data),
                        clinic__city_id=int(city_data),
                        doctor__current_user_id=int(user_id_data)
                        )

                    if del_sch_mainlist != []:
                        del_sch_mainlist = list(del_sch_mainlist)
                        del_sch_mainlist.sort(key=lambda x: x.doctorName)

                else:
                    del_sch_mainlist = Doctor_Schedule_Delete_Notification.objects.filter(
                        doctor__category_id=int(category_data),
                        clinic__city_id=int(city_data)
                        )

                    if del_sch_mainlist != []:
                        del_sch_mainlist = list(del_sch_mainlist)
                        del_sch_mainlist.sort(key=lambda x: x.doctorName)

                paginator = Paginator(del_sch_mainlist, 100)
                page = request.GET.get('page')
                try:
                    del_sch_mainlist = paginator.page(page)
                except PageNotAnInteger:
                    # If page is not an integer, deliver first page.
                    del_sch_mainlist = paginator.page(1)
                except EmptyPage:
                    # If page is out of range (e.g. 9999), deliver last page of results.
                    del_sch_mainlist = paginator.page(paginator.num_pages)
                return render(request, 'admin/doctor_management/doctor_sponsored_rank_deleted_schedules.html',
                              {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                               'city_filter': city_filter,
                               'category_obj': category_obj, 'del_sch_mainlist': del_sch_mainlist,
                               'city_obj': city_obj, 'city_location_filter_length': city_location_filter_length,
                               'category_filter': category_filter, 'city_location_obj': city_location_obj,
                               'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })
            elif category_data:
                if stage_id_data and user_id_data:

                    del_sch_mainlist = Doctor_Schedule_Delete_Notification.objects.filter(
                        doctor__category_id=int(category_data),
                        doctor__stage_id=int(stage_id_data),
                        doctor__current_user_id=int(user_id_data)
                        )

                    if del_sch_mainlist != []:
                        del_sch_mainlist = list(del_sch_mainlist)
                        del_sch_mainlist.sort(key=lambda x: x.doctorName)

                    paginator = Paginator(del_sch_mainlist, 100)
                    page = request.GET.get('page')
                    try:
                        del_sch_mainlist = paginator.page(page)
                    except PageNotAnInteger:
                        # If page is not an integer, deliver first page.
                        del_sch_mainlist = paginator.page(1)
                    except EmptyPage:
                        # If page is out of range (e.g. 9999), deliver last page of results.
                        del_sch_mainlist = paginator.page(paginator.num_pages)
                    return render(request, 'admin/doctor_management/doctor_sponsored_rank_deleted_schedules.html',
                                  {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                                   'city_filter': city_filter,
                                   'category_obj': category_obj, 'del_sch_mainlist': del_sch_mainlist,
                                   'city_obj': city_obj,
                                   'city_location_filter_length': city_location_filter_length,
                                   'category_filter': category_filter, 'city_location_obj': city_location_obj,
                                   'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

                elif stage_id_data:
                    del_sch_mainlist = Doctor_Schedule_Delete_Notification.objects.filter(
                        doctor__category_id=int(category_data),
                        doctor__stage_id=int(stage_id_data)
                        )

                    if del_sch_mainlist != []:
                        del_sch_mainlist = list(del_sch_mainlist)
                        del_sch_mainlist.sort(key=lambda x: x.doctorName)

                elif user_id_data:
                    del_sch_mainlist = Doctor_Schedule_Delete_Notification.objects.filter(
                        doctor__category_id=int(category_data),
                        doctor__current_user_id=int(user_id_data)
                        )

                    if del_sch_mainlist != []:
                        del_sch_mainlist = list(del_sch_mainlist)
                        del_sch_mainlist.sort(key=lambda x: x.doctorName)

                else:
                    del_sch_mainlist = Doctor_Schedule_Delete_Notification.objects.filter(
                        doctor__category_id=int(category_data)
                        )

                    if del_sch_mainlist != []:
                        del_sch_mainlist = list(del_sch_mainlist)
                        del_sch_mainlist.sort(key=lambda x: x.doctorName)


                paginator = Paginator(del_sch_mainlist, 100)
                page = request.GET.get('page')
                try:
                    del_sch_mainlist = paginator.page(page)
                except PageNotAnInteger:
                    # If page is not an integer, deliver first page.
                    del_sch_mainlist = paginator.page(1)
                except EmptyPage:
                    # If page is out of range (e.g. 9999), deliver last page of results.
                    del_sch_mainlist = paginator.page(paginator.num_pages)
                return render(request, 'admin/doctor_management/doctor_sponsored_rank_deleted_schedules.html',
                              {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                               'city_filter': city_filter,
                               'category_obj': category_obj, 'del_sch_mainlist': del_sch_mainlist,
                               'city_obj': city_obj,
                               'city_location_filter_length': city_location_filter_length,
                               'category_filter': category_filter, 'city_location_obj': city_location_obj,
                               'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

            elif city_data and city_location_data:
                if stage_id_data and user_id_data:
                    del_sch_mainlist = Doctor_Schedule_Delete_Notification.objects.filter(
                        clinic__city_id=int(city_data),
                        doctor__stage_id=int(stage_id_data),
                        doctor__current_user_id=int(user_id_data),
                        clinic__locality_id=int(city_location_data),
                        )

                    if del_sch_mainlist != []:
                        del_sch_mainlist = list(del_sch_mainlist)
                        del_sch_mainlist.sort(key=lambda x: x.doctorName)

                    paginator = Paginator(del_sch_mainlist, 100)
                    page = request.GET.get('page')
                    try:
                        del_sch_mainlist = paginator.page(page)
                    except PageNotAnInteger:
                        # If page is not an integer, deliver first page.
                        del_sch_mainlist = paginator.page(1)
                    except EmptyPage:
                        # If page is out of range (e.g. 9999), deliver last page of results.
                        del_sch_mainlist = paginator.page(paginator.num_pages)
                    return render(request, 'admin/doctor_management/doctor_sponsored_rank_deleted_schedules.html',
                                  {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                                   'city_filter': city_filter,
                                   'category_obj': category_obj, 'del_sch_mainlist': del_sch_mainlist,
                                   'city_obj': city_obj,
                                   'city_location_filter_length': city_location_filter_length,
                                   'category_filter': category_filter, 'city_location_obj': city_location_obj,
                                   'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

                elif stage_id_data:
                    del_sch_mainlist = Doctor_Schedule_Delete_Notification.objects.filter(
                        clinic__city_id=int(city_data),
                        doctor__stage_id=int(stage_id_data),
                        clinic__locality_id=int(city_location_data)
                        )

                    if del_sch_mainlist != []:
                        del_sch_mainlist = list(del_sch_mainlist)
                        del_sch_mainlist.sort(key=lambda x: x.doctorName)

                elif user_id_data:
                    del_sch_mainlist = Doctor_Schedule_Delete_Notification.objects.filter(
                        clinic__city_id=int(city_data),
                        doctor__current_user_id=int(user_id_data),
                        clinic__locality_id=int(city_location_data)
                        )

                    if del_sch_mainlist != []:
                        del_sch_mainlist = list(del_sch_mainlist)
                        del_sch_mainlist.sort(key=lambda x: x.doctorName)
                else:
                    del_sch_mainlist = Doctor_Schedule_Delete_Notification.objects.filter(
                        clinic__city_id=int(city_data),
                        clinic__locality_id=int(city_location_data)
                        )

                    if del_sch_mainlist != []:
                        del_sch_mainlist = list(del_sch_mainlist)
                        del_sch_mainlist.sort(key=lambda x: x.doctorName)


                paginator = Paginator(del_sch_mainlist, 100)
                page = request.GET.get('page')
                try:
                    del_sch_mainlist = paginator.page(page)
                except PageNotAnInteger:
                    # If page is not an integer, deliver first page.
                    del_sch_mainlist = paginator.page(1)
                except EmptyPage:
                    # If page is out of range (e.g. 9999), deliver last page of results.
                    del_sch_mainlist = paginator.page(paginator.num_pages)
                return render(request, 'admin/doctor_management/doctor_sponsored_rank_deleted_schedules.html',
                              {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                               'city_filter': city_filter,
                               'category_obj': category_obj, 'del_sch_mainlist': del_sch_mainlist,
                               'city_obj': city_obj, 'city_location_filter_length': city_location_filter_length,
                               'category_filter': category_filter, 'city_location_obj': city_location_obj,
                               'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                               'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                               'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

            elif city_data:
                if stage_id_data and user_id_data:
                    del_sch_mainlist = Doctor_Schedule_Delete_Notification.objects.filter(
                        clinic__city_id=int(city_data),
                        doctor__stage_id=int(stage_id_data),
                        doctor__current_user_id=int(user_id_data)
                        )

                    if del_sch_mainlist != []:
                        del_sch_mainlist = list(del_sch_mainlist)
                        del_sch_mainlist.sort(key=lambda x: x.doctorName)


                    paginator = Paginator(del_sch_mainlist, 100)
                    page = request.GET.get('page')
                    try:
                        del_sch_mainlist = paginator.page(page)
                    except PageNotAnInteger:
                        # If page is not an integer, deliver first page.
                        del_sch_mainlist = paginator.page(1)
                    except EmptyPage:
                        # If page is out of range (e.g. 9999), deliver last page of results.
                        del_sch_mainlist = paginator.page(paginator.num_pages)
                    return render(request, 'admin/doctor_management/doctor_sponsored_rank_deleted_schedules.html',
                                  {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                                   'city_filter': city_filter,
                                   'category_obj': category_obj, 'del_sch_mainlist': del_sch_mainlist,
                                   'city_obj': city_obj,
                                   'city_location_filter_length': city_location_filter_length,
                                   'category_filter': category_filter, 'city_location_obj': city_location_obj,
                                   'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

                elif stage_id_data:
                    del_sch_mainlist = Doctor_Schedule_Delete_Notification.objects.filter(
                        clinic__city_id=int(city_data),
                        doctor__stage_id=int(stage_id_data)
                    )

                    if del_sch_mainlist != []:
                        del_sch_mainlist = list(del_sch_mainlist)
                        del_sch_mainlist.sort(key=lambda x: x.doctorName)

                elif user_id_data:
                    del_sch_mainlist = Doctor_Schedule_Delete_Notification.objects.filter(
                        clinic__city_id=int(city_data),
                        doctor__current_user_id=int(user_id_data)
                    )

                    if del_sch_mainlist != []:
                        del_sch_mainlist = list(del_sch_mainlist)
                        del_sch_mainlist.sort(key=lambda x: x.doctorName)
                else:
                    del_sch_mainlist = Doctor_Schedule_Delete_Notification.objects.filter(
                        clinic__city_id=int(city_data)
                        )

                    if del_sch_mainlist != []:
                        del_sch_mainlist = list(del_sch_mainlist)
                        del_sch_mainlist.sort(key=lambda x: x.doctorName)

                paginator = Paginator(del_sch_mainlist, 100)
                page = request.GET.get('page')
                try:
                    del_sch_mainlist = paginator.page(page)
                except PageNotAnInteger:
                    # If page is not an integer, deliver first page.
                    del_sch_mainlist = paginator.page(1)
                except EmptyPage:
                    # If page is out of range (e.g. 9999), deliver last page of results.
                    del_sch_mainlist = paginator.page(paginator.num_pages)
                return render(request, 'admin/doctor_management/doctor_sponsored_rank_deleted_schedules.html',
                              {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                               'city_filter': city_filter,
                               'category_obj': category_obj, 'del_sch_mainlist': del_sch_mainlist,
                               'city_obj': city_obj, 'city_location_filter_length': city_location_filter_length,
                               'category_filter': category_filter, 'city_location_obj': city_location_obj,
                               'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                               'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                               'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

            elif stage_id_data or user_id_data:
                if stage_id_data and user_id_data:
                    del_sch_mainlist = Doctor_Schedule_Delete_Notification.objects.filter(
                        doctor__stage_id=int(stage_id_data),
                        doctor__current_user_id=int(user_id_data)
                        )

                    if del_sch_mainlist != []:
                        del_sch_mainlist = list(del_sch_mainlist)
                        del_sch_mainlist.sort(key=lambda x: x.doctorName)

                    paginator = Paginator(del_sch_mainlist, 100)
                    page = request.GET.get('page')
                    try:
                        del_sch_mainlist = paginator.page(page)
                    except PageNotAnInteger:
                        # If page is not an integer, deliver first page.
                        del_sch_mainlist = paginator.page(1)
                    except EmptyPage:
                        # If page is out of range (e.g. 9999), deliver last page of results.
                        del_sch_mainlist = paginator.page(paginator.num_pages)
                    return render(request, 'admin/doctor_management/doctor_sponsored_rank_deleted_schedules.html',
                                  {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                                   'city_filter': city_filter,
                                   'category_obj': category_obj, 'del_sch_mainlist': del_sch_mainlist,
                                   'city_obj': city_obj,
                                   'city_location_filter_length': city_location_filter_length,
                                   'category_filter': category_filter, 'city_location_obj': city_location_obj,
                                   'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                                   'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                                   'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

                elif stage_id_data:
                    del_sch_mainlist = Doctor_Schedule_Delete_Notification.objects.filter(
                        doctor__stage_id=int(stage_id_data)
                        )

                    if del_sch_mainlist != []:
                        del_sch_mainlist = list(del_sch_mainlist)
                        del_sch_mainlist.sort(key=lambda x: x.doctorName)
                elif user_id_data:
                    del_sch_mainlist = Doctor_Schedule_Delete_Notification.objects.filter(
                        doctor__current_user_id=int(user_id_data)
                        )

                    if del_sch_mainlist != []:
                        del_sch_mainlist = list(del_sch_mainlist)
                        del_sch_mainlist.sort(key=lambda x: x.doctorName)

                else:
                    del_sch_mainlist = Doctor_Schedule_Delete_Notification.objects.all()

                    if del_sch_mainlist != []:
                        del_sch_mainlist = list(del_sch_mainlist)
                        del_sch_mainlist.sort(key=lambda x: x.doctorName)
            else:
                del_sch_mainlist = Doctor_Schedule_Delete_Notification.objects.all()

                if del_sch_mainlist != []:
                    del_sch_mainlist = list(del_sch_mainlist)
                    del_sch_mainlist.sort(key=lambda x: x.doctorName)


            paginator = Paginator(del_sch_mainlist, 100)
            page = request.GET.get('page')
            try:
                del_sch_mainlist = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                del_sch_mainlist = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                del_sch_mainlist = paginator.page(paginator.num_pages)
            return render(request, 'admin/doctor_management/doctor_sponsored_rank_deleted_schedules.html',
                          {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                           'city_filter': city_filter,
                           'category_obj': category_obj, 'del_sch_mainlist': del_sch_mainlist,
                           'city_obj': city_obj, 'city_location_filter_length': city_location_filter_length,
                           'category_filter': category_filter, 'city_location_obj': city_location_obj,
                           'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                           'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                           'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

        else:
            del_sch_mainlist = []
            filter_name = None
            city_data = None
            city_location_data = None
            category_data = None
            stage_id_data = None
            user_id_data= None
            #doctor_data_obj = Live_Doctor.objects.all().order_by('-createdAt')
            del_sch_mainlist = Doctor_Schedule_Delete_Notification.objects.all()

            if del_sch_mainlist != []:
                del_sch_mainlist = list(del_sch_mainlist)
                del_sch_mainlist.sort(key=lambda x: x.doctorName)
            #paginator = Paginator(doctor_data_obj, 100)
            paginator = Paginator(del_sch_mainlist, 100)
            page = request.GET.get('page')
            try:
                del_sch_mainlist = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                del_sch_mainlist = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                del_sch_mainlist = paginator.page(paginator.num_pages)
            return render(request, 'admin/doctor_management/doctor_sponsored_rank_deleted_schedules.html',
                          {'tab': 'data', 'crosal': 'doctorbymanage', 'stage_data': stage_data,
                           'city_filter': city_filter,'doctor_data_obj':None,
                           'category_obj': category_obj, 'del_sch_mainlist': del_sch_mainlist,
                           'city_obj': city_obj, 'city_location_filter_length': city_location_filter_length,
                           'category_filter': category_filter, 'city_location_obj': city_location_obj,
                           'stage_filter': stage_filter, 'user_filter': user_filter, 'user_data': user_data,
                           'filter_name':filter_name, 'city_data':city_data,'city_location_data':city_location_data,
                           'category_data':category_data,'stage_id_data':stage_id_data,'user_id_data':user_id_data })

    except Exception as e:
        raise Http404

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
####################################################################
# Name - reset_doctor_sponsranks_deleted_schedules                 #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def reset_doctor_sponsranks_deleted_schedules(request):
    try:
        formDATA = request.POST.get('formDATA')
        checkedValues = request.POST.get('formDATA[checkedValues]')
        checkedValues = checkedValues.split(',')

        Spon_CC_RANK_list = request.POST.get('formDATA[Spon_CC_RANK_list]')
        Spon_CC_RANK_list = Spon_CC_RANK_list.split(',')
        Spon_CLC_RANK_list = request.POST.get('formDATA[Spon_CLC_RANK_list]')
        Spon_CLC_RANK_list = Spon_CLC_RANK_list.split(',')

        Spon_CC_KEY_list = request.POST.get('formDATA[Spon_CC_KEY_list]')
        Spon_CC_KEY_list = Spon_CC_KEY_list.split(',')

        Spon_CLC_KEY_list = request.POST.get('formDATA[Spon_CLC_KEY_list]')
        Spon_CLC_KEY_list = Spon_CLC_KEY_list.split(',')

        Notice_id_list = request.POST.get('formDATA[Notice_id_list]')
        Notice_id_list = Notice_id_list.split(',')

        error_msg=None
        #if Spon_CLC_RANK_list != [''] and Subs_CLC_RANK_list != [''] and len(Spon_CLC_RANK_list) == len(Subs_CLC_RANK_list) == len(checkedValues):

        try:
            for i in range(0,len(checkedValues)):
                doc = Doctor.objects.get(id=int(checkedValues[i]))
                if Spon_CC_KEY_list[i].lower() != "novalue" and Spon_CC_RANK_list[i].lower() != "novalue":
                    current_value_cc_rank = doc.sponsored_rank['CC_RANK_list'].get(Spon_CC_KEY_list[i],None)
                    tt = None
                    tt = Spon_CC_RANK_list[i]
                    if tt.isdigit() and int(Spon_CC_RANK_list[i]) == 0:
                        doc.sponsored_rank['CC_RANK_list'][Spon_CC_KEY_list[i]] = int(Spon_CC_RANK_list[i])
                        spon_cc_occu_list = None
                        try:
                            spon_cc_occu_obj = spons_occupied_cc_ranks.objects.get(key=Spon_CC_KEY_list[i])
                            spon_cc_occu_list = spon_cc_occu_obj.ranklist
                            spon_cc_occu_list.sort()
                        except:
                            spon_cc_occu_list = 'DoesNotExist'
                        if spon_cc_occu_list != 'DoesNotExist' and spon_cc_occu_list != None:
                            while(current_value_cc_rank in spon_cc_occu_list):
                                spon_cc_occu_list.remove(current_value_cc_rank)
                            spon_cc_occu_list.sort()
                            spon_cc_occu_obj.ranklist = spon_cc_occu_list
                            spon_cc_occu_obj.save()
                        if Notice_id_list[i].lower() != "novalue":
                            notice_obj = Doctor_Schedule_Delete_Notification.objects.get(id=int(Notice_id_list[i]))
                            notice_obj.spon_cc_rank = 0
                            notice_obj.save()

                if Spon_CLC_KEY_list[i].lower() != "novalue" and Spon_CLC_RANK_list[i].lower() != "novalue":
                    current_value_clc_rank = doc.sponsored_rank['CLC_RANK_list'].get(Spon_CLC_KEY_list[i],None)
                    tt = None
                    tt = Spon_CLC_RANK_list[i]
                    if tt.isdigit() and int(Spon_CLC_RANK_list[i]) == 0:
                        doc.sponsored_rank['CLC_RANK_list'][Spon_CLC_KEY_list[i]] = int(Spon_CLC_RANK_list[i])
                        spon_clc_occu_list = None
                        try:
                            spon_clc_occu_obj = spons_occupied_clc_ranks.objects.get(key=Spon_CLC_KEY_list[i])
                            spon_clc_occu_list = spon_clc_occu_obj.ranklist
                            spon_clc_occu_list.sort()
                        except:
                            spon_clc_occu_list = 'DoesNotExist'
                        if spon_clc_occu_list != 'DoesNotExist' and spon_clc_occu_list != None:
                            while(current_value_clc_rank in spon_clc_occu_list):
                                spon_clc_occu_list.remove(current_value_clc_rank)
                            spon_clc_occu_list.sort()
                            spon_clc_occu_obj.ranklist = spon_clc_occu_list
                            spon_clc_occu_obj.save()

                        if Notice_id_list[i].lower() != "novalue":
                            notice_obj = Doctor_Schedule_Delete_Notification.objects.get(id=int(Notice_id_list[i]))
                            notice_obj.spon_clc_rank = 0
                            notice_obj.save()
                doc.save()
        except Exception as e:
            error_msg = e
        if error_msg == None :
            error_msg = 'Successfully Updated Sponsored Ranks'
        return HttpResponse(json.dumps({"Redirect": False, "Message": error_msg}))
    except Exception as e:
        return HttpResponse(json.dumps({"Redirect": False, "Message": e}))