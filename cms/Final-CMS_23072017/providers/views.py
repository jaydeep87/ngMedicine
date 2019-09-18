from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template.loader import render_to_string
from django.views.decorators.http import require_GET, require_POST

from hfu_cms.models import *
from models import *
from hfu_cms.views import paginate
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from pyPdf import PdfFileReader
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
import json
""" Import News Module """
from news.deco import providers_permission

""" End News Module Import """
from hfu_cms.data_publisher import my_send_mail

bussiness_obj = BusinessType.objects.all()


# Create your views here.

@require_GET
def add_plan_home(request):
    bussiness_obj = BusinessType.objects.all()
    return render(request, 'plan_provider/service_provider.html',
                  {'tab': 'provide_data', 'bussiness_type': bussiness_obj})


""" Service Provider Admin Dashboard """


####################################################################
# Name - service_provider_home                                     #
# Owner - Visnu Badal                                              #
####################################################################
@login_required(login_url='/')
@require_GET
def service_provider_home(request):
    return render(request, "admin_template/plan_provider/plan_provider_dashboard.html", {'tab': 'provide_data'})

####################################################################
# Name - service_provider_home                                     #
# Owner - Visnu Badal                                              #
####################################################################
@login_required(login_url='/')
@require_GET
def listing_home_provider(request):
    providers_obj = ServiceProvider.objects.all()
    providers_obj = paginate(providers_obj, 30)
    return render(request, 'plan_provider/service_provider.html',
                  {'tab': 'provide_data', 'providers_obj': providers_obj})

####################################################################
# Name - add_provider                                              #
# Owner - Visnu Badal                                              #
####################################################################
"""Note This Function has caller, reviewer and Super User access If you want to change than go providers_permission"""
@login_required(login_url='/')
@csrf_exempt
@providers_permission
def add_provider(request):
    if request.method == 'GET':
        bussiness_obj = BusinessType.objects.all()
        return render(request, 'plan_provider/add_provider.html',
                      {'tab': 'provide_data', 'bussiness_type': bussiness_obj})
    elif request.method == 'POST':
        try:
            home_is = request.POST['home_is']
            if home_is:
                home_is = True
            hs_list = request.POST['hs_list']
        except:
            home_is = False
            hs_list = None
        try:
            life_is = request.POST['life_is']
            if life_is:
                life_is = True
            ls_list = request.POST['ls_list']
        except:
            life_is = False
            ls_list = None
        try:
            enter_is = request.POST['enter_is']
            if enter_is:
                enter_is = True
            es_list = request.POST['es_list']
        except:
            enter_is = False
            es_list = None
        if home_is and hs_list is not None or life_is and ls_list is not None or enter_is and es_list is not None:
            business_type = request.POST['business_type']
            organisation_name = request.POST['organisation_name']
            ownerName = request.POST['ownerName']
            years_in_service = request.POST['years_in_service']
            qualityCertification = request.POST['qualityCertification']
            website = request.POST['website']
            c_validity = request.POST['c_validity']
            p_location = request.POST['p_location']
            tat = request.POST['tat']
            remarks = request.POST['remarks']
            person_name = request.POST['person_name']
            mobile = request.POST['mobile']
            email_id = request.POST['email_id']
            r_house_door_bldg = request.POST['r_house_door_bldg']
            c_house_door_bldg = request.POST['c_house_door_bldg']
            r_street = request.POST['r_street']
            c_street = request.POST['c_street']
            r_location = request.POST['r_location']
            c_location = request.POST['c_location']
            r_city = request.POST['r_city']
            c_city = request.POST['c_city']
            r_state = request.POST['r_state']
            c_state = request.POST['c_state']
            r_zip_code = request.POST['r_zip_code']
            r_phone_number = request.POST['r_phone_number']
            c_zip_code = request.POST['c_zip_code']
            c_phone_number = request.POST['c_phone_number']
            beneficiary_name = request.POST['beneficiary_name']
            bank_name = request.POST['bank_name']
            branch_name = request.POST['branch_name']
            account_no = request.POST['account_no']
            ifsc_code = request.POST['ifsc_code']
            try:
                home_rate = request.FILES['home_rate']
                if not home_rate.content_type == 'application/pdf':
                    home_rate = None
            except:
                home_rate = None
            try:
                life_rate = request.FILES['life_rate']
                if not life_rate.content_type == 'application/pdf':
                    life_rate = None
            except:
                life_rate = None
            try:
                enterprise_rate = request.FILES['enterprise_rate']
                if not enterprise_rate.content_type == 'application/pdf':
                    enterprise_rate = None
            except:
                enterprise_rate = None
            if business_type and organisation_name and ownerName and years_in_service and person_name and mobile and email_id and r_city and c_city and r_state and c_state and r_zip_code and r_phone_number and c_zip_code and c_phone_number and beneficiary_name and bank_name and branch_name and account_no and ifsc_code:
                try:
                    service_obj = ServiceProvider(business_type_id=business_type, enterprise_service_provider=enter_is,
                                                  home_service_provider=home_is, life_service_provider=life_is,
                                                  organisation_name=organisation_name, owner_name=ownerName,
                                                  years_in_service=years_in_service, person_name=person_name,
                                                  mobile=mobile, email=email_id,
                                                  quality_certification=qualityCertification,
                                                  website=website, certification_validity=c_validity,
                                                  preferred_location=p_location, tat=tat, remarks=remarks,
                                                  hs_list=hs_list,
                                                  ls_list=ls_list, es_list=es_list, home_rate_card=home_rate,
                                                  life_rate_card=life_rate,
                                                  enterprise_rate_card=enterprise_rate,
                                                  r_house_door_bldg_no=r_house_door_bldg, r_street=r_street,
                                                  c_house_door_bldg_no=c_house_door_bldg, c_street=c_street,
                                                  r_location=r_location, c_location=c_location, r_city=r_city,
                                                  c_city=c_city, r_state=r_state, c_state=c_state,
                                                  r_zip_code=r_zip_code, r_phone_number=r_phone_number,
                                                  c_zip_code=c_zip_code, c_phone_number=c_phone_number,
                                                  beneficiary_name=beneficiary_name,
                                                  bank_name=bank_name, branch_name=branch_name, account_no=account_no,
                                                  ifsc_code=ifsc_code,stage_id=2)
                    service_obj.save()
                    messages.success(request, 'Sccessfully Created Provider Information')

                    return redirect('home-service-providers')
                except Exception as e:
                    messages.error(request, "Something Bad Happened.Please Try Again")

        else:
            messages.error(request, "Please Enter required Field")
        return render(request, 'plan_provider/add_provider.html',
                      {'tab': 'provide_data', 'bussiness_type': bussiness_obj})
        # except Exception as e:
        #     print e


####################################################################
# Name - edit_provider                                             #
# Owner - Visnu Badal                                              #
####################################################################
# This Function is under process
@login_required(login_url='/')
@csrf_exempt
@providers_permission
def edit_providers(request, providers_id=None):
    provide_data_obj = ServiceProvider.objects.filter(id=providers_id)
    if request.method == 'GET':
        if providers_id is not None:
            # provide_data_obj = ServiceProvider.objects.filter(id=providers_id)
            return render(request, 'plan_provider/edit_provider.html',
                          {'provide_data_obj': provide_data_obj, 'tab': 'provide_data',
                           'bussiness_type': bussiness_obj})
    elif request.method == 'POST':
        try:
            home_is = request.POST['home_is']
            if home_is:
                home_is = True
            hs_list = request.POST['hs_list']
        except:
            home_is = False
            hs_list = None
        try:
            life_is = request.POST['life_is']
            if life_is:
                life_is = True
            ls_list = request.POST['ls_list']
        except:
            life_is = False
            ls_list = None
        try:
            enter_is = request.POST['enter_is']
            if enter_is:
                enter_is = True
            es_list = request.POST['es_list']
        except:
            enter_is = False
            es_list = None
        if home_is and hs_list is not None or life_is and ls_list is not None or enter_is and es_list is not None:
            business_type = request.POST['business_type']
            organisation_name = request.POST['organisation_name']
            ownerName = request.POST['ownerName']
            years_in_service = request.POST['years_in_service']
            qualityCertification = request.POST['qualityCertification']
            website = request.POST['website']
            c_validity = request.POST['c_validity']
            p_location = request.POST['p_location']
            tat = request.POST['tat']
            remarks = request.POST['remarks']
            person_name = request.POST['person_name']
            mobile = request.POST['mobile']
            email_id = request.POST['email_id']
            r_house_door_bldg = request.POST['r_house_door_bldg']
            c_house_door_bldg = request.POST['c_house_door_bldg']
            r_street = request.POST['r_street']
            c_street = request.POST['c_street']
            r_location = request.POST['r_location']
            c_location = request.POST['c_location']
            r_city = request.POST['r_city']
            c_city = request.POST['c_city']
            r_state = request.POST['r_state']
            c_state = request.POST['c_state']
            r_zip_code = request.POST['r_zip_code']
            r_phone_number = request.POST['r_phone_number']
            c_zip_code = request.POST['c_zip_code']
            c_phone_number = request.POST['c_phone_number']
            beneficiary_name = request.POST['beneficiary_name']
            bank_name = request.POST['bank_name']
            branch_name = request.POST['branch_name']
            account_no = request.POST['account_no']
            ifsc_code = request.POST['ifsc_code']
            try:
                home_rate = request.FILES['home_rate']
                if not home_rate.content_type == 'application/pdf':
                    home_rate = None
            except:
                home_rate = None
            try:
                life_rate = request.FILES['life_rate']
                if not life_rate.content_type == 'application/pdf':
                    life_rate = None
            except:
                life_rate = None
            try:
                enterprise_rate = request.FILES['enterprise_rate']
                if not enterprise_rate.content_type == 'application/pdf':
                    enterprise_rate = None
            except:
                enterprise_rate = None
            if business_type and organisation_name and ownerName and years_in_service and person_name and mobile and email_id and r_city and c_city and r_state and c_state and r_zip_code and r_phone_number and c_zip_code and c_phone_number and beneficiary_name and bank_name and branch_name and account_no and ifsc_code:
                provide_data_obj.update(business_type_id=business_type, enterprise_service_provider=enter_is,
                                        home_service_provider=home_is, life_service_provider=life_is,
                                        organisation_name=organisation_name,
                                        owner_name=ownerName,
                                        years_in_service=years_in_service, person_name=person_name,
                                        mobile=mobile, email=email_id,
                                        quality_certification=qualityCertification,
                                        website=website, certification_validity=c_validity,
                                        preferred_location=p_location, tat=tat, remarks=remarks,
                                        hs_list=hs_list,
                                        ls_list=ls_list, es_list=es_list,
                                        r_house_door_bldg_no=r_house_door_bldg, r_street=r_street,
                                        c_house_door_bldg_no=c_house_door_bldg, c_street=c_street,
                                        r_location=r_location, c_location=c_location, r_city=r_city,
                                        c_city=c_city, r_state=r_state, c_state=c_state,
                                        r_zip_code=r_zip_code, r_phone_number=r_phone_number,
                                        c_zip_code=c_zip_code, c_phone_number=c_phone_number,
                                        beneficiary_name=beneficiary_name,
                                        bank_name=bank_name, branch_name=branch_name, account_no=account_no,
                                        ifsc_code=ifsc_code)
                file_obj = ServiceProvider.objects.get(id=providers_id)
                file_obj.home_rate_card.delete()
                messages.success(request, "Successfully Updated Provider Information")
                return redirect('home-service-providers')

        else:
            messages.error(request, 'Please Select Which type service Provider and require Fields')
            return HttpResponseRedirect('/service/home-service/edit/providers/' + providers_id + '/')

####################################################################
# Name - listing_life_provider                                     #
# Owner - Visnu Badal                                              #
####################################################################
@login_required(login_url='/')
@require_GET
def listing_life_provider(request):
    return HttpResponse("This is Life provider listing ")

####################################################################
# Name - listing_life_provider                                     #
# Owner - Visnu Badal                                              #
####################################################################
@login_required(login_url='/')
@require_GET
def listing_enterprise_provider(request):
    return HttpResponse("This is enterprise provider listing ")

# -----------Service Plan Views Start------------- #

####################################################################
# Name - listing_home_service_plan                                 #
# Owner - Visnu Badal                                              #
####################################################################
@login_required(login_url='/')
@require_GET
def listing_home_service_plan(request):
    try :
        home_list = ServicePlan.objects.filter(is_home_service=True,current_user_id=request.user.id,activation_status=True).order_by('plan_name')

        results = []
        try:
            page = request.GET.get('page')
            paginator = Paginator(home_list, 50)
            results = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            paginator = Paginator(home_list, 50)
            results = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            paginator = Paginator(home_list, 50)
            results = paginator.page(paginator.num_pages)
        except :
            # If page is out of range (e.g. 9999), deliver last page of results.
            paginator = Paginator(home_list, 50)
            results = paginator.page(1)

        return render(request, 'service_plan/home_service_plan_listing.html',{'tab_listing': 'home_listing', 'plan_list': results,
                       'plan_type': 'Home'})
    except Exception as e:
        raise Http404

####################################################################
# Name - listing_life_service_plan                                 #
# Owner - Visnu Badal                                              #
####################################################################
@login_required(login_url='/')
@require_GET
def listing_life_service_plan(request):
    life_list = ServicePlan.objects.filter(is_life_service=True,current_user_id=request.user.id,activation_status=True).order_by('plan_name')
    results = []

    try:
        page = request.GET.get('page')
        paginator = Paginator(life_list, 50)
        results = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginator = Paginator(life_list, 50)
        results = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginator = Paginator(life_list, 50)
        results = paginator.page(paginator.num_pages)
    except :
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginator = Paginator(life_list, 50)
        results = paginator.page(1)
    return render(request, 'service_plan/life_service_plan_listing.html',
                  {'tab_listing': 'life_listing', 'plan_list': results,
                   'plan_type': 'Life'})

####################################################################
# Name - listing_enterprise_service_plan                           #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@require_GET
def listing_enterprise_service_plan(request):
    enterprise_list = ServicePlan.objects.filter(is_enterprise_service=True,current_user_id=request.user.id,activation_status=True).order_by('plan_name')
    results = []
    try:
        page = request.GET.get('page')
        paginator = Paginator(enterprise_list, 50)
        results = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginator = Paginator(enterprise_list, 50)
        results = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginator = Paginator(enterprise_list, 50)
        results = paginator.page(paginator.num_pages)

    except :
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginator = Paginator(enterprise_list, 50)
        results = paginator.page(1)
    return render(request, 'service_plan/enterprise_service_plan_listing.html',
                  {'tab_listing': 'enterprise_listing', 'plan_list': results,
                   'plan_type': 'Enterprise'})

####################################################################
# Name - service_plan_home                                         #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def service_plan_home(request):
    if request.method == 'GET':
        try:
            return render(request, 'admin_template/service_plan/service_plan_dashboard.html', {'tab': 'service-plan'})
        except Exception as e:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            messages.error(request, "Something Bad Happened")

####################################################################
# Name - add_home_service_plan                                     #
# Owner - Nishank                                                  #
####################################################################
# This Function like edit_providers does not have @plan_permission decorator
# Write Separate Function to each
@login_required(login_url='/')
@csrf_exempt
def add_home_service_plan(request, plan_type=None):
    try :
        if request.method == 'GET':
            plan_category_list = PlanCategory.objects.all()
            provider_list = ServiceProvider.objects.all()
            plan_list= ServicePlan.objects.filter(is_home_service = True)
            caresidense_plan_types = CaResidense_subtype_master.objects.filter(delete=False)
            return render(request, 'service_plan/add_home_service_plan.html',
                      {'tab_listing': 'home_listing', 'plan_type': plan_type,
                       'plan_category_list': plan_category_list,
                       'provider_list': provider_list,'plan_list':plan_list,
                       'caresidense_plan_types':caresidense_plan_types})
        elif request.method == 'POST':

            caresidense_plans = request.POST.getlist('caresidense_plans')

            if caresidense_plans != []:
                tempstr = ''
                counter = 0
                for i in caresidense_plans:
                    i = i.strip()
                    counter += 1
                    if counter == 1:
                        tempstr = tempstr + i
                    else:
                        tempstr = tempstr + ',' + i
                        caresidense_plans = tempstr
            else:
                caresidense_plans = ''

            plan_name = request.POST['package_name']

            provider_id = request.POST['provider_name']

            instructions = request.POST['instructions']

            package_description = request.POST['package_description']

            investigation = request.POST.getlist('investigations')

            others = request.POST.getlist('others')

            consultation = request.POST.getlist('consultations')

            imaging = request.POST.getlist('imaging')

            plan_price = float(request.POST['package_rates'])

            timings = request.POST['timings']

            plan_validity = request.POST['validity']
            type = request.POST['type']

            dict_in = {}
            for i in range(0, len(investigation)) :
                if investigation[i] != '':
                    dict_in.update({i: investigation[i]})

            dict_co= {}
            for i in range(0, len(consultation)) :
                if consultation[i] != '':
                    dict_co.update({i: consultation[i]})

            dict_im = {}
            for i in range(0, len(imaging)) :
                if imaging[i] != '':
                    dict_im.update({i: imaging[i]})

            dict_bb = {}
            for i in range(0, len(others)) :
                if others[i] != '':
                    dict_bb.update({i: others[i]})

            investigationj = dict_in
            consultationj = dict_co
            imagingj = dict_im
            othersj = dict_bb
            #investigationj = [{i: investigation[i]} for i in  range(0, len(investigation))]
            #consultationj = [{i: consultation[i]} for i in range(0, len(consultation))]
            #imagingj = [{i: imaging[i]} for i in range(0, len(imaging))]
            #blood_bankj = [{i: blood_bank[i]} for i in range(0, len(blood_bank))]
            if plan_name and provider_id:
                home_plan_obj=  ServicePlan(plan_name=plan_name,provider_id=provider_id, instructions= instructions,
                           package_description =package_description , investigation=investigationj,
                           others = othersj,consultation=consultationj,imaging =imagingj ,
                           plan_price=plan_price, timings=timings,plan_validity=plan_validity,
                           stage_id= 2, current_user_id = request.user.id,is_home_service =True,
                           free_text='',type=type,caresidense_plan_type = caresidense_plans)

                home_plan_obj.save()
                messages.success(request, "Successfully added Home Service Plan")
                return HttpResponseRedirect(reverse('home-service-plan-listing'))
            else:
                messages.error(request, "Please provide Provider and Plan name")
                return HttpResponseRedirect(reverse('home-service-plan-listing'))
    except Exception as e:
        #print e
        messages.error(request, "Something Bad Happened")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - add_life_service_plan                                     #
# Owner - Nishank                                                  #
####################################################################
# This Function like edit_providers does not have @plan_permission decorator
# Write Separate Function to each
@login_required(login_url='/')
@csrf_exempt
def add_life_service_plan(request, plan_type=None):
    try :
        if request.method == 'GET':
            plan_category_list = PlanCategory.objects.all()
            provider_list = ServiceProvider.objects.all()
            plan_list= ServicePlan.objects.filter(is_home_service = True)
            kurable_plan_types = Kurable_subtype_master.objects.filter(delete=False)
            return render(request, 'service_plan/add_life_service_plan.html',
                      {'tab_listing': 'life_listing', 'plan_type': plan_type,
                       'plan_category_list': plan_category_list,
                       'provider_list': provider_list,'plan_list':plan_list,
                       'kurable_plan_types':kurable_plan_types})
        elif request.method == 'POST':

            kurable_plans = request.POST.getlist('kurable_plans')

            if kurable_plans != [] :
                tempstr = ''
                counter = 0
                for i in kurable_plans :
                    i = i.strip()
                    counter += 1
                    if counter == 1:
                        tempstr = tempstr + i
                    else:
                        tempstr = tempstr + ',' + i
                kurable_plans = tempstr
            else:
                kurable_plans = ''

            plan_name = request.POST['package_name']
            provider_id = request.POST['provider_name']
            instructions = request.POST['instructions']
            package_description = request.POST['package_description']
            investigation = request.POST.getlist('investigations')
            others = request.POST.getlist('others')
            consultation = request.POST.getlist('consultations')
            imaging = request.POST.getlist('imaging')
            plan_price = float(request.POST['package_rates'])
            timings = request.POST['timings']
            plan_validity = request.POST['validity']
            type = request.POST['type']
            dict_in = {}
            for i in range(0, len(investigation)) :
                if investigation[i] != '':
                    dict_in.update({i: investigation[i]})

            dict_co= {}
            for i in range(0, len(consultation)) :
                if consultation[i] != '':
                    dict_co.update({i: consultation[i]})

            dict_im = {}
            for i in range(0, len(imaging)) :
                if imaging[i] != '':
                    dict_im.update({i: imaging[i]})

            dict_bb = {}
            for i in range(0, len(others)) :
                if others[i] != '':
                    dict_bb.update({i: others[i]})

            investigationj = dict_in
            consultationj = dict_co
            imagingj = dict_im
            othersj = dict_bb
            #investigationj = [{i: investigation[i]} for i in  range(0, len(investigation))]
            #consultationj = [{i: consultation[i]} for i in range(0, len(consultation))]
            #imagingj = [{i: imaging[i]} for i in range(0, len(imaging))]
            #blood_bankj = [{i: blood_bank[i]} for i in range(0, len(blood_bank))]
            if plan_name and provider_id:
                home_plan_obj=  ServicePlan(plan_name=plan_name,provider_id=provider_id, instructions= instructions,
                           package_description =package_description , investigation=investigationj,
                           others = othersj,consultation=consultationj,imaging =imagingj ,
                           plan_price=plan_price, timings=timings,plan_validity=plan_validity,
                           stage_id= 2, current_user_id = request.user.id,is_life_service =True,
                           free_text='',type=type,kurable_plan_type = kurable_plans)

                home_plan_obj.save()
                messages.success(request, "Successfully added Life Service Plan")
                return HttpResponseRedirect(reverse('life-service-plan-listing'))
            else:
                messages.error(request, "Please provide Provider and Plan name")
                return HttpResponseRedirect(reverse('life-service-plan-listing'))
    except Exception as e:
        messages.error(request, "Something Bad Happened")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - add_enterprise_service_plan                               #
# Owner - Nishank                                                  #
####################################################################
# This Function like edit_providers does not have @plan_permission decorator
# Write Separate Function to each
@login_required(login_url='/')
@csrf_exempt
def add_enterprise_service_plan(request, plan_type=None):
    try :
        if request.method == 'GET':
            plan_category_list = PlanCategory.objects.all()
            provider_list = ServiceProvider.objects.all()
            plan_list= ServicePlan.objects.filter(is_home_service = True)
            healthoholic_plan_types = Healthoholic_subtype_master.objects.filter(delete=False)
            return render(request, 'service_plan/add_enterprise_service_plan.html',
                      {'tab_listing': 'enterprise_listing', 'plan_type': plan_type,
                       'plan_category_list': plan_category_list,
                       'provider_list': provider_list,'plan_list':plan_list,
                       'healthoholic_plan_types':healthoholic_plan_types})
        elif request.method == 'POST':
            healthoholic_plans = request.POST.getlist('healthoholic_plans')
            if healthoholic_plans != []:
                tempstr = ''
                counter = 0
                for i in healthoholic_plans:
                    i = i.strip()
                    counter += 1
                    if counter == 1:
                        tempstr = tempstr + i
                    else:
                        tempstr = tempstr + ',' + i
                healthoholic_plans = tempstr
            else:
                healthoholic_plans = ''

            plan_name = request.POST['package_name']
            provider_id = request.POST['provider_name']
            instructions = request.POST['instructions']
            package_description = request.POST['package_description']
            investigation = request.POST.getlist('investigations')
            others = request.POST.getlist('others')
            consultation = request.POST.getlist('consultations')
            imaging = request.POST.getlist('imaging')
            try:
                plan_price = float(request.POST['package_rates'])
            except:
                plan_price = 0
            timings = request.POST['timings']
            plan_validity = request.POST['validity']
            type = request.POST['type']

            dict_in = {}
            for i in range(0, len(investigation)) :
                if investigation[i] != '':
                    dict_in.update({i: investigation[i]})

            dict_co= {}
            for i in range(0, len(consultation)) :
                if consultation[i] != '':
                    dict_co.update({i: consultation[i]})

            dict_im = {}
            for i in range(0, len(imaging)) :
                if imaging[i] != '':
                    dict_im.update({i: imaging[i]})

            dict_bb = {}
            for i in range(0, len(others)) :
                if others[i] != '':
                    dict_bb.update({i: others[i]})

            investigationj = dict_in
            consultationj = dict_co
            imagingj = dict_im
            othersj = dict_bb
            #investigationj = [{i: investigation[i]} for i in  range(0, len(investigation))]
            #consultationj = [{i: consultation[i]} for i in range(0, len(consultation))]
            #imagingj = [{i: imaging[i]} for i in range(0, len(imaging))]
            #blood_bankj = [{i: blood_bank[i]} for i in range(0, len(blood_bank))]
            if plan_name and provider_id:
                home_plan_obj=  ServicePlan(plan_name=plan_name,provider_id=provider_id, instructions= instructions,
                           package_description =package_description , investigation=investigationj,
                           others = othersj,consultation=consultationj,imaging =imagingj ,
                           plan_price=plan_price, timings=timings,plan_validity=plan_validity,
                           stage_id= 2, current_user_id = request.user.id,is_enterprise_service =True,
                           free_text='',type=type,healthoholic_plan_type=healthoholic_plans)

                home_plan_obj.save()
                messages.success(request, "Successfully added Enterprise Service Plan")
                return HttpResponseRedirect(reverse('enterprise-service-plan-listing'))
            else:
                messages.error(request, "Please provide Provider and Plan name")
                return HttpResponseRedirect(reverse('enterprise-service-plan-listing'))
    except Exception as e:

        messages.error(request, "Something Bad Happened")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - edit_home_service_plan                                    #
# Owner - Nishank                                                  #
####################################################################
from datetime import datetime
# This Function like edit_providers does not have @plan_permission decorator
# Added by Nishank 27-9
@login_required(login_url='/')
@csrf_exempt
def edit_home_service_plan(request, plan_type=None, plan_id=None):
    try :
        if request.method == 'GET':
            plan_category_list = PlanCategory.objects.all()
            provider_list = ServiceProvider.objects.all()
            publisher_user_data = UserManagement.objects.filter(is_publisher=True, user__is_active=True)
            reviewer_user_data = UserManagement.objects.filter(is_reviewer=True, user__is_active=True,is_service_reviewer=True)
            caller_user_data = UserManagement.objects.filter(user__is_active=True,is_service_plan=True)
            #Have not put is_caller = True for the sake of old users
            valid_choice = ValidateByChoice.objects.all()
            caresidense_plan_types = CaResidense_subtype_master.objects.filter(delete=False)

            if plan_id:
                package_obj = ServicePlan.objects.get(id= plan_id)
                current_provider = ServiceProvider.objects.get(id=package_obj.provider_id)
                investigation_list = package_obj.investigation
                consultation_list = package_obj.consultation
                imaging_list = package_obj.imaging
                others_list = package_obj.others
                if package_obj.caresidense_plan_type :
                    crp =  package_obj.caresidense_plan_type
                    caresidense_current_plans = crp.split(',')
                else:
                    caresidense_current_plans = []
                user_is_publisher = None
                is_publisher = UserManagement.objects.filter(user_id=request.user.id, is_publisher=True)
                if len(is_publisher):
                    user_is_publisher = True
                return render(request, 'service_plan/edit_home_service_plan.html',
                      {'tab_listing': 'home_listing', 'plan_type': plan_type,
                       'plan_category_list': plan_category_list,
                       'provider_list': provider_list, 'package_obj' :package_obj,
                       'investigation_list':investigation_list,'consultation_list':consultation_list,
                       'imaging_list':imaging_list,'others_list':others_list,
                       'publisher_user_data':publisher_user_data, 'reviewer_user_data':reviewer_user_data,
                       'caller_user_data':caller_user_data,'valid_choice':valid_choice,
                       'user_is_publisher': user_is_publisher,
                       'caresidense_current_plans': caresidense_current_plans,
                       'caresidense_plan_types': caresidense_plan_types,
                       'current_provider':current_provider
                       })
            else:
                messages.error(request, "Something Bad Happened")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        elif request.method == 'POST' and plan_id:
            caresidense_plans = request.POST.getlist('caresidense_plans')
            if caresidense_plans != []:
                tempstr = ''
                counter = 0
                for i in caresidense_plans:
                    i = i.strip()
                    counter += 1
                    if counter == 1:
                        tempstr = tempstr + i
                    else:
                        tempstr = tempstr + ',' + i
                caresidense_plans = tempstr
            else:
                caresidense_plans = ''

            plan_name = request.POST['package_name']
            provider_id = request.POST['provider_name']
            instructions = request.POST['instructions']
            package_description = request.POST['package_description']
            investigation = request.POST.getlist('investigations')
            others = request.POST.getlist('others')
            consultation = request.POST.getlist('consultations')
            imaging = request.POST.getlist('imaging')
            plan_price = float(request.POST['package_rates'])
            timings = request.POST['timings']
            plan_validity = request.POST['validity']
            type = request.POST['type']

            dict_in = {}
            for i in range(0, len(investigation)) :
                if investigation[i] != '':
                    dict_in.update({i: investigation[i]})

            dict_co= {}
            for i in range(0, len(consultation)) :
                if consultation[i] != '':
                    dict_co.update({i: consultation[i]})

            dict_im = {}
            for i in range(0, len(imaging)) :
                if imaging[i] != '':
                    dict_im.update({i: imaging[i]})

            dict_bb = {}
            for i in range(0, len(others)) :
                if others[i] != '':
                    dict_bb.update({i: others[i]})

            investigationj = dict_in
            consultationj = dict_co
            imagingj = dict_im
            othersj = dict_bb
            if plan_name and provider_id :
                package_obj = ServicePlan.objects.get(id= plan_id )
                package_obj.plan_name=plan_name
                package_obj.provider_id=provider_id
                package_obj.instructions= instructions
                package_obj.package_description = package_description
                package_obj.investigation=investigationj
                package_obj.others = othersj
                package_obj.consultation=consultationj
                package_obj.imaging =imagingj
                package_obj.plan_price=plan_price
                package_obj.timings=timings
                package_obj.plan_validity=plan_validity
                package_obj.caresidense_plan_type = caresidense_plans
                package_obj.type=type
                package_obj.save()
                is_publisher = UserManagement.objects.filter(user_id= request.user.id,is_publisher=True)
                if request.user.is_superuser :
                    messages.success(request, "Successfully Edited Home Service Plan")
                    return HttpResponseRedirect(reverse('home-plan-management'))
                elif len(is_publisher):
                    messages.success(request, "Successfully Edited Home Service Plan")
                    return HttpResponseRedirect(reverse('publisher-homeplan-listing'))
                else:
                    messages.success(request, "Successfully Edited Home Service Plan")
                    return HttpResponseRedirect(reverse('home-service-plan-listing'))
            else:
                messages.error(request, "Please provide Provider and Plan name")
                return HttpResponseRedirect(reverse('home-service-plan-listing'))
    except Exception as e:
        #print e
        messages.error(request, "Something Bad Happened")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - edit_life_service_plan                                    #
# Owner - Nishank                                                  #
####################################################################
from datetime import datetime
# This Function like edit_providers does not have @plan_permission decorator
# Added by Nishank 27-9
@login_required(login_url='/')
@csrf_exempt
def edit_life_service_plan(request, plan_type=None, plan_id=None):
    try :
        if request.method == 'GET':
            plan_category_list = PlanCategory.objects.all()
            provider_list = ServiceProvider.objects.all()
            publisher_user_data = UserManagement.objects.filter(is_publisher=True, user__is_active=True)
            reviewer_user_data = UserManagement.objects.filter(is_reviewer=True, user__is_active=True,is_service_reviewer=True)
            caller_user_data = UserManagement.objects.filter(user__is_active=True,is_service_plan=True)
            #Have not put is_caller = True for the sake of old users
            valid_choice = ValidateByChoice.objects.all()
            kurable_plan_types = Kurable_subtype_master.objects.filter(delete=False)

            if plan_id:
                package_obj = ServicePlan.objects.get(id= plan_id)
                current_provider = ServiceProvider.objects.get(id=package_obj.provider_id)

                investigation_list = package_obj.investigation
                consultation_list = package_obj.consultation
                imaging_list = package_obj.imaging
                others_list = package_obj.others
                if package_obj.kurable_plan_type :
                    kcp =  package_obj.kurable_plan_type
                    kurable_current_plans = kcp.split(',')
                else:
                    kurable_current_plans = []
                user_is_publisher = None
                is_publisher = UserManagement.objects.filter(user_id=request.user.id, is_publisher=True)
                if len(is_publisher):
                    user_is_publisher = True
                return render(request, 'service_plan/edit_life_service_plan.html',
                      {'tab_listing': 'life_listing', 'plan_type': plan_type,
                       'plan_category_list': plan_category_list,
                       'provider_list': provider_list, 'package_obj' :package_obj,
                       'investigation_list':investigation_list,'consultation_list':consultation_list,
                       'imaging_list':imaging_list,'others_list':others_list,
                       'publisher_user_data':publisher_user_data, 'reviewer_user_data':reviewer_user_data,
                       'caller_user_data':caller_user_data,'valid_choice':valid_choice,
                       'user_is_publisher': user_is_publisher,'kurable_current_plans':kurable_current_plans,
                       'kurable_plan_types':kurable_plan_types,'current_provider':current_provider})
            else:
                messages.error(request, "Something Bad Happened")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        elif request.method == 'POST' and plan_id:
            kurable_plans = request.POST.getlist('kurable_plans')
            if kurable_plans != []:
                tempstr = ''
                counter = 0
                for i in kurable_plans:
                    i = i.strip()
                    counter += 1
                    if counter == 1:
                        tempstr = tempstr + i
                    else:
                        tempstr = tempstr + ',' + i
                kurable_plans = tempstr
            else:
                kurable_plans = ''

            plan_name = request.POST['package_name']
            provider_id = request.POST['provider_name']
            instructions = request.POST['instructions']
            package_description = request.POST['package_description']
            investigation = request.POST.getlist('investigations')
            others = request.POST.getlist('others')
            consultation = request.POST.getlist('consultations')
            imaging = request.POST.getlist('imaging')
            plan_price = float(request.POST['package_rates'])
            timings = request.POST['timings']
            plan_validity = request.POST['validity']
            type = request.POST['type']
            dict_in = {}
            for i in range(0, len(investigation)) :
                if investigation[i] != '':
                    dict_in.update({i: investigation[i]})

            dict_co= {}
            for i in range(0, len(consultation)) :
                if consultation[i] != '':
                    dict_co.update({i: consultation[i]})

            dict_im = {}
            for i in range(0, len(imaging)) :
                if imaging[i] != '':
                    dict_im.update({i: imaging[i]})

            dict_bb = {}
            for i in range(0, len(others)) :
                if others[i] != '':
                    dict_bb.update({i: others[i]})

            investigationj = dict_in
            consultationj = dict_co
            imagingj = dict_im
            othersj = dict_bb
            if plan_name and provider_id :
                package_obj = ServicePlan.objects.get(id= plan_id )
                package_obj.plan_name=plan_name
                package_obj.provider_id=provider_id
                package_obj.instructions= instructions
                package_obj.package_description = package_description
                package_obj.investigation=investigationj
                package_obj.others = othersj
                package_obj.consultation=consultationj
                package_obj.imaging =imagingj
                package_obj.plan_price=plan_price
                package_obj.timings=timings
                package_obj.plan_validity=plan_validity
                package_obj.kurable_plan_type = kurable_plans
                package_obj.type=type
                package_obj.save()
                is_publisher = UserManagement.objects.filter(user_id= request.user.id,is_publisher=True)

                if request.user.is_superuser :
                    messages.success(request, "Successfully Edited Life Service Plan")
                    return HttpResponseRedirect(reverse('life-plan-management'))
                elif len(is_publisher):
                    messages.success(request, "Successfully Edited Life Service Plan")
                    return HttpResponseRedirect(reverse('publisher-lifeplan-listing'))
                else:
                    messages.success(request, "Successfully Edited Life Service Plan")
                    return HttpResponseRedirect(reverse('life-service-plan-listing'))
            else:
                messages.error(request, "Please provide Provider and Plan name")
                return HttpResponseRedirect(reverse('life-service-plan-listing'))
    except Exception as e:
        messages.error(request, "Something Bad Happened")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - edit_enterprise_service_plan                              #
# Owner - Nishank                                                  #
####################################################################
from datetime import datetime
# This Function like edit_providers does not have @plan_permission decorator
# Added by Nishank 27-9
@login_required(login_url='/')
@csrf_exempt
def edit_enterprise_service_plan(request, plan_type=None, plan_id=None):
    try :
        if request.method == 'GET':
            plan_category_list = PlanCategory.objects.all()
            provider_list = ServiceProvider.objects.all()

            publisher_user_data = UserManagement.objects.filter(is_publisher=True, user__is_active=True)
            reviewer_user_data = UserManagement.objects.filter(is_reviewer=True, user__is_active=True,is_service_reviewer=True)
            caller_user_data = UserManagement.objects.filter( user__is_active=True,is_service_plan=True)
            #Have not put is_caller = True for the sake of old users
            valid_choice = ValidateByChoice.objects.all()
            healthoholic_plan_types = Healthoholic_subtype_master.objects.filter(delete=False)
            if plan_id:
                package_obj = ServicePlan.objects.get(id= plan_id)
                current_provider = ServiceProvider.objects.get(id=package_obj.provider_id)
                investigation_list = package_obj.investigation
                consultation_list = package_obj.consultation
                imaging_list = package_obj.imaging
                others_list = package_obj.others
                if package_obj.healthoholic_plan_type :
                    hcp =  package_obj.healthoholic_plan_type
                    healthoholic_current_plans = hcp.split(',')
                else:
                    healthoholic_current_plans = []
                user_is_publisher = None
                is_publisher = UserManagement.objects.filter(user_id=request.user.id, is_publisher=True)
                if len(is_publisher):
                    user_is_publisher = True
                return render(request, 'service_plan/edit_enterprise_service_plan.html',
                      {'tab_listing': 'enterprise_listing', 'plan_type': plan_type,
                       'plan_category_list': plan_category_list,
                       'provider_list': provider_list, 'package_obj' :package_obj,
                       'investigation_list':investigation_list,'consultation_list':consultation_list,
                       'imaging_list':imaging_list,'others_list':others_list,
                       'publisher_user_data':publisher_user_data, 'reviewer_user_data':reviewer_user_data,
                       'caller_user_data':caller_user_data,'valid_choice':valid_choice,
                       'user_is_publisher': user_is_publisher,'healthoholic_plan_types':healthoholic_plan_types,
                       'healthoholic_current_plans':healthoholic_current_plans,
                       'current_provider':current_provider})
            else:
                messages.error(request, "Something Bad Happened")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        elif request.method == 'POST' and plan_id:
            healthoholic_plans = request.POST.getlist('healthoholic_plans')
            if healthoholic_plans != []:
                tempstr = ''
                counter = 0
                for i in healthoholic_plans:
                    i = i.strip()
                    counter += 1
                    if counter == 1:
                        tempstr = tempstr + i
                    else:
                        tempstr = tempstr + ',' + i
                healthoholic_plans = tempstr
            else:
                healthoholic_plans = ''

            plan_name = request.POST['package_name']
            provider_id = request.POST['provider_name']
            instructions = request.POST['instructions']
            package_description = request.POST['package_description']
            investigation = request.POST.getlist('investigations')
            others = request.POST.getlist('others')
            consultation = request.POST.getlist('consultations')
            imaging = request.POST.getlist('imaging')
            plan_price = float(request.POST['package_rates'])
            timings = request.POST['timings']
            plan_validity = request.POST['validity']
            type = request.POST['type']
            dict_in = {}
            for i in range(0, len(investigation)) :
                if investigation[i] != '':
                    dict_in.update({i: investigation[i]})

            dict_co= {}
            for i in range(0, len(consultation)) :
                if consultation[i] != '':
                    dict_co.update({i: consultation[i]})

            dict_im = {}
            for i in range(0, len(imaging)) :
                if imaging[i] != '':
                    dict_im.update({i: imaging[i]})

            dict_bb = {}
            for i in range(0, len(others)) :
                if others[i] != '':
                    dict_bb.update({i: others[i]})

            investigationj = dict_in
            consultationj = dict_co
            imagingj = dict_im
            othersj = dict_bb
            if plan_name and provider_id :
                package_obj = ServicePlan.objects.get(id= plan_id )
                package_obj.plan_name=plan_name
                package_obj.provider_id=provider_id
                package_obj.instructions= instructions
                package_obj.package_description = package_description
                package_obj.investigation=investigationj
                package_obj.others = othersj
                package_obj.consultation=consultationj
                package_obj.imaging =imagingj
                package_obj.plan_price=plan_price
                package_obj.timings=timings
                package_obj.plan_validity=plan_validity
                package_obj.healthoholic_plan_type=healthoholic_plans
                package_obj.type=type
                package_obj.save()
                is_publisher = UserManagement.objects.filter(user_id= request.user.id,is_publisher=True)

                if request.user.is_superuser :
                    messages.success(request, "Successfully Edited Enterprise Service Plan")
                    return HttpResponseRedirect(reverse('enterprise-plan-management'))
                elif len(is_publisher):
                    messages.success(request, "Successfully Edited Enterprise Service Plan")
                    return HttpResponseRedirect(reverse('publisher-enterpriseplan-listing'))
                else:
                    messages.success(request, "Successfully Edited Enterprise Service Plan")
                    return HttpResponseRedirect(reverse('enterprise-service-plan-listing'))
            else:
                messages.error(request, "Please provide Provider and Plan name")
                return HttpResponseRedirect(reverse('enterprise-service-plan-listing'))
    except Exception as e:
        messages.error(request, "Something Bad Happened")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - home _plan_data_by_users                                  #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser, login_url='/')
@require_GET
def home_plan_data_manage(request):
    try:
        return render(request, 'admin_template/service_plan/home_plan_management/home_plan_management.html',
                      {'tab': 'home_manage', 'crosal': 'home _planmanage'})
    except Exception as e:
        raise Http404

####################################################################
# Name - life _plan_data_by_users                                  #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser, login_url='/')
@require_GET
def life_plan_data_manage(request):
    try:
        return render(request, 'admin_template/service_plan/life_plan_management/life_plan_management.html',
                      {'tab': 'life_manage', 'crosal': 'life _planmanage'})
    except Exception as e:
        raise Http404

####################################################################
# Name - enterprise _plan_data_by_users                            #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser, login_url='/')
@require_GET
def enterprise_plan_data_manage(request):
    try:
        return render(request, 'admin_template/service_plan/enterprise_plan_management/enterprise_plan_management.html',
                      {'tab': 'enterprise_manage', 'crosal': 'enterprise _planmanage'})
    except Exception as e:
        raise Http404

####################################################################
# Name - home_plan_data_by_users                                   #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def home_plan_data_by_users(request):
    try:
        user_data_obj = UserManagement.objects.all()
        search_data=None
        search_data = request.GET.get('search_data')
        if search_data :
            home_plan_all_data = ServicePlan.objects.filter(current_user_id=search_data,is_home_service=True).order_by('plan_name')
            paginator = Paginator(home_plan_all_data, 100)
            page = request.GET.get('page')
            try:
                home_plan_all_data = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                home_plan_all_data = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                home_plan_all_data = paginator.page(paginator.num_pages)

            return render(request, 'admin_template/service_plan/home_plan_management/home_plan_by_user.html',
                      {'tab': 'home_manage', 'crosal': 'home_planbymanage',
                       'home_plan_all_data': home_plan_all_data,
                       'user_data_obj': user_data_obj,'search_data':search_data})
        try:
            search_data_two = request.GET.get('search_data_two')
        except:
            search_data_two = None
        if search_data_two:
            user_data_obj = UserManagement.objects.all()
            home_plan_all_data = ServicePlan.objects.filter(news_header__icontains=search_data_two,is_home_service=True).order_by('plan_name')
            paginator = Paginator(home_plan_all_data, 3)
            page = request.GET.get('page')
            try:
                home_plan_all_data = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                home_plan_all_data = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                home_plan_all_data = paginator.page(paginator.num_pages)
            return render(request, 'admin_template/service_plan/home_plan_management/home_plan_by_user.html',
                          {'tab': 'home_manage', 'crosal': 'home_planbymanage',
                           'home_plan_all_data': home_plan_all_data,
                           'user_data_obj': user_data_obj, 'search_data_two': search_data_two})
        home_plan_all_data = ServicePlan.objects.filter(is_home_service=True).order_by('plan_name')
        user_data_obj = UserManagement.objects.all()
        paginator = Paginator(home_plan_all_data, 100)
        page = request.GET.get('page')
        try:
            home_plan_all_data = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            home_plan_all_data = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            home_plan_all_data = paginator.page(paginator.num_pages)
        return render(request, 'admin_template/service_plan/home_plan_management/home_plan_by_user.html',
                      {'tab': 'home_manage', 'crosal': 'home_planbymanage',
                       'home_plan_all_data': home_plan_all_data,
                       'user_data_obj': user_data_obj})
    except Exception as e:
        raise Http404

####################################################################
# Name - search_home_plan_admin_on_stage_user                      #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_home_plan_admin_on_stage_user(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = ServicePlan.objects.filter(Q(plan_name__icontains=q) & Q(is_home_service=True)).order_by('plan_name')
            else:
                results = ServicePlan.objects.filter(is_home_service=True).order_by('plan_name')
            paginator = Paginator(results, 3)
            try:
                page = request.GET.get('page')
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('admin_template/service_plan/home_plan_management/search_home_plan_by_stage_user.html',
                                    {'tab': 'home_manage', 'crosal': 'homeplanbymanage', 'home_plan_all_data': results,
                                     'search_data_two':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - home_plan_data_by_stages                                  #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def home_plan_data_by_stages(request):
    try:
        stage_id = request.GET.get('stage_id')
        if stage_id:
            home_plan_all_data = ServicePlan.objects.filter(stage_id=stage_id,is_home_service=True).order_by('plan_name')
        else:
            home_plan_all_data = ServicePlan.objects.filter(is_home_service=True).order_by('plan_name')
            stage_id=None
        stage_data = Stage.objects.all()[:5]
        paginator = Paginator(home_plan_all_data, 100)
        page = request.GET.get('page')
        try:
            home_plan_all_data = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            home_plan_all_data = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            home_plan_all_data = paginator.page(paginator.num_pages)
        return render(request, 'admin_template/service_plan/home_plan_management/home_plan_by_stages.html',
                      {'tab': 'home_manage', 'crosal': 'home_planbymanage',
                       'home_plan_all_data': home_plan_all_data,
                       'stage_data': stage_data,'stage_no':stage_id  })
    except Exception as e:
        raise Http404

####################################################################
# Name - home_plan Assignment                                      #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
@csrf_exempt
def home_plan_assignment(request):
    try:
        stage_data = Stage.objects.all()[:4]
        state_data_obj = State.objects.all()
        search_data=None
        search_data = request.GET.get('search_data')
        if search_data :
            home_plan_obj =  ServicePlan.objects.filter(is_home_service= True,plan_name__icontains=search_data).order_by('plan_name')
            paginator = Paginator(home_plan_obj,100)
            page = request.GET.get('page')
            try:
                home_plan_obj = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                home_plan_obj = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                home_plan_obj = paginator.page(paginator.num_pages)
            return render(request, 'admin_template/service_plan/home_plan_management/home_plan_assign.html',
                          {'tab': 'home_manage', 'crosal': 'home_planbymanage', 'stage_data': stage_data,
                           'home_plan_all_data': home_plan_obj, 'state_data_obj': state_data_obj,'search_data':search_data})
        try:
            filter_name = str(request.GET['x'].strip())
        except:
            filter_name = None
        if filter_name == 'home_plan_filter':
            state_data = request.GET['state_id'].strip()
            if state_data:
                state_filter = int(state_data)
            city_data = request.GET['city_id'].strip()
            if city_data:
                city_filter = int(city_data)
                city_obj = City.objects.filter(state_id=state_filter)
            else:
                city_obj = []
            locality_data = request.GET['locality_id'].strip()
            if locality_data:
                locality_filter = int(locality_data)
            if state_data:
                if city_data and locality_data:
                    home_plan_obj = ServicePlan.objects.filter(is_home_service= True).order_by('plan_name')
                    locality_obj = Locality.objects.filter(city_id=city_filter).order_by('name')
                    paginator = Paginator(home_plan_obj, 100)
                    page = request.GET.get('page')
                    try:
                        home_plan_obj = paginator.page(page)
                    except PageNotAnInteger:
                        # If page is not an integer, deliver first page.
                        home_plan_obj = paginator.page(1)
                    except EmptyPage:
                        # If page is out of range (e.g. 9999), deliver last page of results.
                        home_plan_obj = paginator.page(paginator.num_pages)
                    return render(request, 'admin_template/service_plan/home_plan_management/home_plan_assign.html',
                                  {'tab': 'home_manage', 'crosal': 'home_planbymanage',
                                   'stage_data': stage_data,
                                   'home_plan_all_data': home_plan_obj, 'state_data_obj': state_data_obj,
                                   'city_obj': city_obj, 'locality_obj': locality_obj,
                                   'locality_filter': locality_filter, 'city_filter': city_filter,
                                   'state_filter': state_filter})
                elif city_data:
                    home_plan_obj = ServicePlan.objects.filter(is_home_service= True).order_by('plan_name')
                else:
                    home_plan_obj = ServicePlan.objects.filter(is_home_service= True).order_by('plan_name')
                paginator = Paginator(home_plan_obj, 100)
                page = request.GET.get('page')
                try:
                    home_plan_obj = paginator.page(page)
                except PageNotAnInteger:
                    # If page is not an integer, deliver first page.
                    home_plan_obj = paginator.page(1)
                except EmptyPage:
                    # If page is out of range (e.g. 9999), deliver last page of results.
                    home_plan_obj = paginator.page(paginator.num_pages)

                return render(request, 'admin_template/service_plan/home_plan_management/home_plan_assign.html',
                              {'tab': 'home_manage', 'crosal': 'home_planbymanage',
                               'stage_data': stage_data,
                               'home_plan_all_data': home_plan_obj, 'state_data_obj': state_data_obj,
                               'state_filter': state_filter, 'locality_filter': locality_filter,
                               'city_filter': city_filter, 'city_obj': city_obj})
            else:
                home_plan_obj = ServicePlan.objects.filter(is_home_service= True).order_by('plan_name')
            paginator = Paginator(home_plan_obj, 100)
            page = request.GET.get('page')
            try:
                home_plan_obj = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                home_plan_obj = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                home_plan_obj = paginator.page(paginator.num_pages)
            return render(request, 'admin_template/service_plan/home_plan_management/home_plan_assign.html',
                          {'tab': 'home_manage', 'crosal': 'home_planbymanage', 'stage_data': stage_data,
                           'home_plan_all_data': home_plan_obj, 'state_data_obj': state_data_obj
                           })
        else:
            home_plan_obj = ServicePlan.objects.filter(is_home_service= True).order_by('plan_name')
            paginator = Paginator(home_plan_obj, 100)
            page = request.GET.get('page')
            try:
                home_plan_obj = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                home_plan_obj = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                home_plan_obj = paginator.page(paginator.num_pages)
            return render(request, 'admin_template/service_plan/home_plan_management/home_plan_assign.html',
                          {'tab': 'home_manage', 'crosal': 'home_planbymanage', 'stage_data': stage_data,
                           'home_plan_all_data': home_plan_obj, 'state_data_obj': state_data_obj})
    except Exception as e:
        raise Http404

####################################################################
# Name - search_home_plan_by_stages_by_admin                       #
# Owner - Jaydeep  verma                                           #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_home_plan_by_stages_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = ServicePlan.objects.filter(stage_id=q).order_by('plan_name')
                results = results.filter(is_home_service= True)
            paginator = Paginator(results, 100)
            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('admin_template/service_plan/home_plan_management/search_by_user_admin.html',
                                    {'tab': 'home_manage', 'crosal': 'home_planbymanage', 'home_plan_all_data': results,
                                      'stage_no':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - assign HomePlan                                           #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def assign_homeplan(request):
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
                        assign_obj = ServicePlan.objects.filter(id=checkedValues[i]).update(
                            current_user_id=assign_user,
                            stage_id=change_stage)
                        nbslist.append(checkedValues[i])
                    except:
                        nbflist.append(checkedValues[i])
                        continue
                my_send_mail(request, 'homeplan', nbslist, nbflist, 'Homeplan Assignment', 'Assigned')

                response1['Redirect'] = True
                response1['RedirectUrl'] = '/service/assignment/home/plan/'
                response1['Message'] = "Assign Complete"
            else:
                response1['Message'] = "Please select Stage and User "
            response = json.dumps(response1)
            return HttpResponse(response)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_home_plan_admin                                    #
# Owner - Jaydeep verma                                            #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_home_plan_assign_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = ServicePlan.objects.filter(Q(plan_name__icontains=q) & Q(is_home_service=True)).order_by('plan_name')
            else:
                results = ServicePlan.objects.all(is_home_service = True).order_by('plan_name')
            paginator = Paginator(results, 100)
            try:
                page = request.GET.get('page')
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('admin_template/service_plan/home_plan_management/search_admin_home_plan.html',
                                    {'tab': 'home-manage', 'crosal': 'home_planbymanage', 'home_plan_all_data': results,
                                     'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - life_plan_data_by_users                                   #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def life_plan_data_by_users(request):
    try:
        search_data=None
        search_data = request.GET.get('search_data')
        if search_data :
            user_data_obj = UserManagement.objects.all()
            life_plan_all_data = ServicePlan.objects.filter(current_user_id=search_data,is_life_service=True).order_by('plan_name')
            paginator = Paginator(life_plan_all_data, 100)
            page = request.GET.get('page')
            try:
                life_plan_all_data = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                life_plan_all_data = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                life_plan_all_data = paginator.page(paginator.num_pages)
            return render(request, 'admin_template/service_plan/life_plan_management/life_plan_by_user.html',
                      {'tab': 'life_manage', 'crosal': 'life_planbymanage',
                       'life_plan_all_data': life_plan_all_data,
                       'user_data_obj': user_data_obj, 'search_data':search_data})
        life_plan_all_data = ServicePlan.objects.filter(is_life_service=True).order_by('plan_name')
        user_data_obj = UserManagement.objects.all()
        results = []
        paginator = Paginator(life_plan_all_data, 100)
        page = request.GET.get('page')
        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            results = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            results = paginator.page(paginator.num_pages)
        return render(request, 'admin_template/service_plan/life_plan_management/life_plan_by_user.html',
                      {'tab': 'life_manage', 'crosal': 'life_planbymanage',
                       'life_plan_all_data': results,
                       'user_data_obj': user_data_obj})
    except Exception as e:
        raise Http404

####################################################################
# Name - search_life_plan_admin_on_stage_user                      #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_life_plan_admin_on_stage_user(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = ServicePlan.objects.filter(Q(plan_name__icontains=q) & Q(is_life_service=True)).order_by('plan_name')
            else:
                results = ServicePlan.objects.filter(is_life_service=True).order_by('plan_name')
            paginator = Paginator(results, 100)
            try:
                page = request.GET.get('page')
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('admin_template/service_plan/life_plan_management/search_life_plan_by_stage_user.html',
                                    {'tab': 'life_manage', 'crosal': 'lifeplanbymanage', 'life_plan_all_data': results})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - life_plan_data_by_stages                                  #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def life_plan_data_by_stages(request):
    try:
        stage_id = request.GET.get('stage_id')
        if stage_id:
            life_plan_all_data = ServicePlan.objects.filter(stage_id=stage_id,is_life_service=True).order_by('plan_name')
        else:
            life_plan_all_data = ServicePlan.objects.filter(is_life_service=True).order_by('plan_name')
            stage_id=None
        stage_data = Stage.objects.all()[:5]
        paginator = Paginator(life_plan_all_data, 100)
        page = request.GET.get('page')
        try:
            life_plan_all_data = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            life_plan_all_data = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            life_plan_all_data = paginator.page(paginator.num_pages)
        return render(request, 'admin_template/service_plan/life_plan_management/life_plan_by_stages.html',
                      {'tab': 'life_manage', 'crosal': 'life_planbymanage',
                       'life_plan_all_data': life_plan_all_data,
                       'stage_data': stage_data,'stage_no':stage_id })
    except Exception as e:
        raise Http404

####################################################################
# Name - life_plan Assignment                                      #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
@csrf_exempt
def life_plan_assignment(request):
    try:
        state_filter = False
        city_filter = False
        locality_filter = False
        stage_data = Stage.objects.all()[:4]
        state_data_obj = State.objects.all()
        search_data=None
        search_data = request.GET.get('search_data')
        if search_data :
            life_plan_obj =  ServicePlan.objects.filter(is_life_service= True,plan_name__icontains=search_data).order_by('plan_name')
            paginator = Paginator(life_plan_obj,100)
            page = request.GET.get('page')
            try:
                life_plan_obj = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                life_plan_obj = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                life_plan_obj = paginator.page(paginator.num_pages)
            return render(request, 'admin_template/service_plan/life_plan_management/life_plan_assign.html',
                          {'tab': 'life_manage', 'crosal': 'life_planbymanage', 'stage_data': stage_data,
                           'life_plan_all_data': life_plan_obj, 'state_data_obj': state_data_obj,'search_data':search_data})

        try:
            filter_name = str(request.GET['x'].strip())
        except:
            filter_name = None
        if filter_name == 'life_plan_filter':
            state_data = request.GET['state_id'].strip()
            if state_data:
                state_filter = int(state_data)
            city_data = request.GET['city_id'].strip()
            if city_data:
                city_filter = int(city_data)
                city_obj = City.objects.filter(state_id=state_filter)
            else:
                city_obj = []
            locality_data = request.GET['locality_id'].strip()
            if locality_data:
                locality_filter = int(locality_data)
            if state_data:
                if city_data and locality_data:
                    life_plan_obj = ServicePlan.objects.filter(is_life_service= True).order_by('plan_name')
                    locality_obj = Locality.objects.filter(city_id=city_filter).order_by('name')
                    paginator = Paginator(life_plan_obj, 100)
                    page = request.GET.get('page')
                    try:
                        life_plan_obj = paginator.page(page)
                    except PageNotAnInteger:
                        # If page is not an integer, deliver first page.
                        life_plan_obj = paginator.page(1)
                    except EmptyPage:
                        # If page is out of range (e.g. 9999), deliver last page of results.
                        life_plan_obj = paginator.page(paginator.num_pages)
                    return render(request, 'admin_template/service_plan/life_plan_management/life_plan_assign.html',
                                  {'tab': 'life_manage', 'crosal': 'life_planbymanage',
                                   'stage_data': stage_data,
                                   'life_plan_all_data': life_plan_obj, 'state_data_obj': state_data_obj,
                                   'city_obj': city_obj, 'locality_obj': locality_obj,
                                   'locality_filter': locality_filter, 'city_filter': city_filter,
                                   'state_filter': state_filter})
                elif city_data:
                    life_plan_obj = ServicePlan.objects.filter(is_life_service= True).order_by('plan_name')
                else:
                    life_plan_obj = ServicePlan.objects.filter(is_life_service= True).order_by('plan_name')
                paginator = Paginator(life_plan_obj, 100)
                page = request.GET.get('page')
                try:
                    life_plan_obj = paginator.page(page)
                except PageNotAnInteger:
                    # If page is not an integer, deliver first page.
                    life_plan_obj = paginator.page(1)
                except EmptyPage:
                    # If page is out of range (e.g. 9999), deliver last page of results.
                    life_plan_obj = paginator.page(paginator.num_pages)

                return render(request, 'admin_template/service_plan/life_plan_management/life_plan_assign.html',
                              {'tab': 'life_manage', 'crosal': 'life_planbymanage',
                               'stage_data': stage_data,
                               'life_plan_all_data': life_plan_obj, 'state_data_obj': state_data_obj,
                               'state_filter': state_filter, 'locality_filter': locality_filter,
                               'city_filter': city_filter, 'city_obj': city_obj})
            else:
                life_plan_obj = ServicePlan.objects.filter(is_life_service= True).order_by('plan_name')
            paginator = Paginator(life_plan_obj, 100)
            page = request.GET.get('page')
            try:
                life_plan_obj = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                life_plan_obj = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                life_plan_obj = paginator.page(paginator.num_pages)
            return render(request, 'admin_template/service_plan/life_plan_management/life_plan_assign.html',
                          {'tab': 'life_manage', 'crosal': 'life_planbymanage', 'stage_data': stage_data,
                           'life_plan_all_data': life_plan_obj, 'state_data_obj': state_data_obj
                           })
        else:
            life_plan_obj = ServicePlan.objects.filter(is_life_service= True).order_by('plan_name')
            paginator = Paginator(life_plan_obj, 100)
            page = request.GET.get('page')
            try:
                life_plan_obj = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                life_plan_obj = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                life_plan_obj = paginator.page(paginator.num_pages)
            return render(request, 'admin_template/service_plan/life_plan_management/life_plan_assign.html',
                          {'tab': 'life_manage', 'crosal': 'life_planbymanage', 'stage_data': stage_data,
                           'life_plan_all_data': life_plan_obj, 'state_data_obj': state_data_obj})
    except Exception as e:
        raise Http404

####################################################################
# Name - search_life_plan_by_stages_by_admin                       #
# Owner - Jaydeep  verma                                           #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_life_plan_by_stages_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = ServicePlan.objects.filter(stage_id=q).order_by('plan_name')
                results = results.filter(is_life_service= True)
            paginator = Paginator(results, 100)
            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('admin_template/service_plan/life_plan_management/search_by_user_admin.html',
                                    {'tab': 'life_manage', 'crosal': 'life_planbymanage', 'life_plan_all_data': results,
                                     'stage_no':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - assign lifePlan                                           #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def assign_lifeplan(request):
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
                        assign_obj = ServicePlan.objects.filter(id=checkedValues[i]).update(
                            current_user_id=assign_user,
                            stage_id=change_stage)
                        nbslist.append(checkedValues[i])
                    except:
                        nbflist.append(checkedValues[i])
                        continue
                my_send_mail(request, 'lifeplan', nbslist, nbflist, 'Lifeplan Assignment', 'Assigned')
                response1['Redirect'] = True
                response1['RedirectUrl'] = '/service/assignment/life/plan/'
                response1['Message'] = "Assign Complete"
            else:
                response1['Message'] = "Please select Stage and User "
            response = json.dumps(response1)
            return HttpResponse(response)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_life_plan_admin                                    #
# Owner - Jaydeep verma                                            #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_life_plan_assign_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = ServicePlan.objects.filter(Q(plan_name__icontains=q) & Q(is_life_service=True)).order_by('plan_name')
            else:
                results = ServicePlan.objects.all(is_life_service = True).order_by('plan_name')
            paginator = Paginator(results, 100)
            try:
                page = request.GET.get('page')
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('admin_template/service_plan/life_plan_management/search_admin_life_plan.html',
                                    {'tab': 'life-manage', 'crosal': 'life_planbymanage', 'life_plan_all_data': results,
                                     'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - enterprise_plan_data_by_users                             #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def enterprise_plan_data_by_users(request):
    try:
        search_data=None
        search_data = request.GET.get('search_data')
        if search_data :
            user_data_obj = UserManagement.objects.all()
            enterprise_plan_all_data = ServicePlan.objects.filter(current_user_id=search_data,is_enterprise_service=True).order_by('plan_name')
            paginator = Paginator(enterprise_plan_all_data, 100)
            page = request.GET.get('page')
            try:
                enterprise_plan_all_data = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                enterprise_plan_all_data = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                enterprise_plan_all_data = paginator.page(paginator.num_pages)
            return render(request, 'admin_template/service_plan/enterprise_plan_management/enterprise_plan_by_user.html',
                      {'tab': 'enterprise_manage', 'crosal': 'enterprise_planbymanage',
                       'enterprise_plan_all_data': enterprise_plan_all_data,
                       'user_data_obj': user_data_obj, 'search_data':search_data})
        enterprise_plan_all_data = ServicePlan.objects.filter(is_enterprise_service=True).order_by('plan_name')
        user_data_obj = UserManagement.objects.all()
        paginator = Paginator(enterprise_plan_all_data, 100)
        page = request.GET.get('page')
        try:
            enterprise_plan_all_data = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            enterprise_plan_all_data = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            enterprise_plan_all_data = paginator.page(paginator.num_pages)
        return render(request, 'admin_template/service_plan/enterprise_plan_management/enterprise_plan_by_user.html',
                      {'tab': 'enterprise_manage', 'crosal': 'enterprise_planbymanage',
                       'enterprise_plan_all_data': enterprise_plan_all_data,
                       'user_data_obj': user_data_obj})
    except Exception as e:
        raise Http404

####################################################################
# Name - search_enterprise_plan_admin_on_stage_user                #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_enterprise_plan_admin_on_stage_user(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = ServicePlan.objects.filter(Q(plan_name__icontains=q) & Q(is_enterprise_service=True)).order_by('plan_name')
            else:
                results = ServicePlan.objects.filter(is_enterprise_service=True).order_by('plan_name')
            paginator = Paginator(results, 100)
            try:
                page = request.GET.get('page')
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('admin_template/service_plan/enterprise_plan_management/search_enterprise_plan_by_stage_user.html',
                                    {'tab': 'enterprise_manage', 'crosal': 'enterpriseplanbymanage', 'enterprise_plan_all_data': results})

            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - enterprise_plan_data_by_stages                            #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def enterprise_plan_data_by_stages(request):
    try:
        stage_id = request.GET.get('stage_id')
        if stage_id:
            enterprise_plan_all_data = ServicePlan.objects.filter(stage_id=stage_id,is_enterprise_service=True).order_by('plan_name')
        else:
            enterprise_plan_all_data = ServicePlan.objects.filter(is_enterprise_service=True).order_by('plan_name')
            stage_id=None
        stage_data = Stage.objects.all()[:5]
        paginator = Paginator(enterprise_plan_all_data, 100)
        page = request.GET.get('page')
        try:
            enterprise_plan_all_data = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            enterprise_plan_all_data = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            enterprise_plan_all_data = paginator.page(paginator.num_pages)
        return render(request, 'admin_template/service_plan/enterprise_plan_management/enterprise_plan_by_stages.html',
                      {'tab': 'enterprise_manage', 'crosal': 'enterprise_planbymanage',
                       'enterprise_plan_all_data': enterprise_plan_all_data,
                       'stage_data': stage_data,'stage_no':stage_id})
    except Exception as e:
        raise Http404

####################################################################
# Name - enterprise_plan Assignment                                #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
@csrf_exempt
def enterprise_plan_assignment(request):
    try:
        state_filter = False
        city_filter = False
        locality_filter = False
        stage_data = Stage.objects.all()[:4]
        state_data_obj = State.objects.all()
        search_data=None
        search_data = request.GET.get('search_data')
        if search_data :
            enterprise_plan_obj =  ServicePlan.objects.filter(is_enterprise_service= True,plan_name__icontains=search_data).order_by('plan_name')
            paginator = Paginator(enterprise_plan_obj,100)
            page = request.GET.get('page')
            try:
                enterprise_plan_obj = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                enterprise_plan_obj = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                enterprise_plan_obj = paginator.page(paginator.num_pages)
            return render(request, 'admin_template/service_plan/enterprise_plan_management/enterprise_plan_assign.html',
                          {'tab': 'enterprise_manage', 'crosal': 'enterprise_planbymanage', 'stage_data': stage_data,
                           'enterprise_plan_all_data': enterprise_plan_obj, 'state_data_obj': state_data_obj,
                           'search_data':search_data})
        try:
            filter_name = str(request.GET['x'].strip())
        except:
            filter_name = None
        if filter_name == 'enterprise_plan_filter':
            state_data = request.GET['state_id'].strip()
            if state_data:
                state_filter = int(state_data)
            city_data = request.GET['city_id'].strip()
            if city_data:
                city_filter = int(city_data)
                city_obj = City.objects.filter(state_id=state_filter)
            else:
                city_obj = []
            locality_data = request.GET['locality_id'].strip()
            if locality_data:
                locality_filter = int(locality_data)
            if state_data:
                if city_data and locality_data:
                    enterprise_plan_obj = ServicePlan.objects.filter(is_enterprise_service= True).order_by('plan_name')
                    locality_obj = Locality.objects.filter(city_id=city_filter).order_by('name')
                    paginator = Paginator(enterprise_plan_obj, 100)
                    page = request.GET.get('page')
                    try:
                        enterprise_plan_obj = paginator.page(page)
                    except PageNotAnInteger:
                        # If page is not an integer, deliver first page.
                        enterprise_plan_obj = paginator.page(1)
                    except EmptyPage:
                        # If page is out of range (e.g. 9999), deliver last page of results.
                        enterprise_plan_obj = paginator.page(paginator.num_pages)
                    return render(request, 'admin_template/service_plan/enterprise_plan_management/enterprise_plan_assign.html',
                                  {'tab': 'enterprise_manage', 'crosal': 'enterprise_planbymanage',
                                   'stage_data': stage_data,
                                   'enterprise_plan_all_data': enterprise_plan_obj, 'state_data_obj': state_data_obj,
                                   'city_obj': city_obj, 'locality_obj': locality_obj,
                                   'locality_filter': locality_filter, 'city_filter': city_filter,
                                   'state_filter': state_filter})
                elif city_data:
                    enterprise_plan_obj = ServicePlan.objects.filter(is_enterprise_service= True).order_by('plan_name')
                else:
                    enterprise_plan_obj = ServicePlan.objects.filter(is_enterprise_service= True).order_by('plan_name')
                paginator = Paginator(enterprise_plan_obj, 100)
                page = request.GET.get('page')
                try:
                    enterprise_plan_obj = paginator.page(page)
                except PageNotAnInteger:
                    # If page is not an integer, deliver first page.
                    enterprise_plan_obj = paginator.page(1)
                except EmptyPage:
                    # If page is out of range (e.g. 9999), deliver last page of results.
                    enterprise_plan_obj = paginator.page(paginator.num_pages)

                return render(request, 'admin_template/service_plan/enterprise_plan_management/enterprise_plan_assign.html',
                              {'tab': 'enterprise_manage', 'crosal': 'enterprise_planbymanage',
                               'stage_data': stage_data,
                               'enterprise_plan_all_data': enterprise_plan_obj, 'state_data_obj': state_data_obj,
                               'state_filter': state_filter, 'locality_filter': locality_filter,
                               'city_filter': city_filter, 'city_obj': city_obj})

            else:
                enterprise_plan_obj = ServicePlan.objects.filter(is_enterprise_service= True).order_by('plan_name')
            paginator = Paginator(enterprise_plan_obj, 100)
            page = request.GET.get('page')
            try:
                enterprise_plan_obj = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                enterprise_plan_obj = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                enterprise_plan_obj = paginator.page(paginator.num_pages)
            return render(request, 'admin_template/service_plan/enterprise_plan_management/enterprise_plan_assign.html',
                          {'tab': 'enterprise_manage', 'crosal': 'enterprise_planbymanage', 'stage_data': stage_data,
                           'enterprise_plan_all_data': enterprise_plan_obj, 'state_data_obj': state_data_obj
                           })
        else:
            enterprise_plan_obj = ServicePlan.objects.filter(is_enterprise_service= True).order_by('plan_name')
            paginator = Paginator(enterprise_plan_obj, 100)
            page = request.GET.get('page')
            try:
                enterprise_plan_obj = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                enterprise_plan_obj = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                enterprise_plan_obj = paginator.page(paginator.num_pages)
            return render(request, 'admin_template/service_plan/enterprise_plan_management/enterprise_plan_assign.html',
                          {'tab': 'enterprise_manage', 'crosal': 'enterprise_planbymanage', 'stage_data': stage_data,
                           'enterprise_plan_all_data': enterprise_plan_obj, 'state_data_obj': state_data_obj})
    except Exception as e:
        raise Http404

####################################################################
# Name - search_enterprise_plan_by_stages_by_admin                 #
# Owner - Jaydeep  verma                                           #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_enterprise_plan_by_stages_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = ServicePlan.objects.filter(stage_id=q).order_by('plan_name')
                results = results.filter(is_enterprise_service= True)
            paginator = Paginator(results, 100)
            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('admin_template/service_plan/enterprise_plan_management/search_by_user_admin.html',
                                    {'tab': 'enterprise_manage', 'crosal': 'enterprise_planbymanage', 'enterprise_plan_all_data': results,
                                     'stage_no':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - assign enterprisePlan                                     #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def assign_enterpriseplan(request):
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
                        assign_obj = ServicePlan.objects.filter(id=checkedValues[i]).update(
                        current_user_id=assign_user,
                        stage_id=change_stage)
                        nbslist.append(checkedValues[i])
                    except:
                        nbflist.append(checkedValues[i])
                        continue
                my_send_mail(request, 'enterpriseplan', nbslist, nbflist, 'Enterpriseplan Assignment', 'Assigned')

                response1['Redirect'] = True
                response1['RedirectUrl'] = '/service/assignment/enterprise/plan/'
                response1['Message'] = "Assign Complete"
            else:
                response1['Message'] = "Please select Stage and User "
            response = json.dumps(response1)
            return HttpResponse(response)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_enterprise_plan_admin                              #
# Owner - Jaydeep verma                                            #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_enterprise_plan_assign_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = ServicePlan.objects.filter(Q(plan_name__icontains=q) & Q(is_enterprise_service=True)).order_by('plan_name')
            else:
                results = ServicePlan.objects.all(is_enterprise_service = True).order_by('plan_name')
            paginator = Paginator(results, 100)
            try:
                page = request.GET.get('page')
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('admin_template/service_plan/enterprise_plan_management/search_admin_enterprise_plan.html',
                                    {'tab': 'enterprise-manage', 'crosal': 'enterprise_planbymanage', 'enterprise_plan_all_data': results,
                                     'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_Homeplan_by_users_by_admin                         #
# Owner - Nishank Gupta                                            #
####################################################################

@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_home_plan_by_users(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = ServicePlan.objects.filter(current_user_id=q,is_home_service=True).order_by('plan_name')
            paginator = Paginator(results, 3)
            page = request.GET.get('page')
            if q.isdigit():
                search_data = q
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)

            html = render_to_string( 'admin_template/service_plan/home_plan_management/search_home_plan_by_users.html',
                      {'tab': 'data', 'crosal': 'home_planbymanage','home_plan_all_data': results,
                       'search_data':q,'search_data_two':q})

            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_lifeplan_by_users_by_admin                         #
# Owner - Nishank Gupta                                            #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_life_plan_by_users(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = ServicePlan.objects.filter(current_user_id=q,is_life_service=True).order_by('plan_name')
            paginator = Paginator(results, 100)
            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)

            html = render_to_string( 'admin_template/service_plan/life_plan_management/search_life_plan_by_users.html',
                      {'tab': 'data', 'crosal': 'life_planbymanage','life_plan_all_data': results, 'search_data':q})

            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_enterpriseplan_by_users_by_admin                   #
# Owner - Nishank Gupta                                            #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_enterprise_plan_by_users(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = ServicePlan.objects.filter(current_user_id=q,is_enterprise_service=True).order_by('plan_name')

            paginator = Paginator(results, 100)
            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)

            html = render_to_string( 'admin_template/service_plan/enterprise_plan_management/search_enterprise_plan_by_users.html',
                      {'tab': 'data', 'crosal': 'enterprise_planbymanage','enterprise_plan_all_data': results,
                       'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

"""Publisher ViEWS"""

####################################################################
# Name - homeplan_publisher_listing                                #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@require_GET
def homeplan_publisher_listing(request):
    try:
        assign_id = UserManagement.objects.get(user_id=request.user.id)
        stage_data_obj = Stage.objects.all()[3:5]
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
        if publisher_id:
            if category_id:
                homeplan_obj = ServicePlan.objects.filter(Q(stage_id__gte=4),Q(category_id=category_id), Q(current_user_id =request.user.id),Q(is_home_service=True), Q(activation_status=True)).order_by('plan_name')
                category_filter = int(category_id)
            else:
                homeplan_obj = ServicePlan.objects.filter(stage_id__gte=4,current_user_id =request.user.id,is_home_service=True,activation_status=True).order_by('plan_name')
            if len(homeplan_obj) == 0:
                messages.error(request, "No homeplan found")
                return render(request, 'publisher/homeplan/homeplan_listing_publisher.html',
                              {'tab_listing': 'homeplan_listing', 'tab': 'publish_homeplan_data',
                               'stage_data': stage_data_obj,
                               'category_obj': category_data, 'category_filter': category_filter})

            paginator = Paginator(homeplan_obj, 50)
            page = request.GET.get('page')
            try:
                homeplan_obj = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                homeplan_obj = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                homeplan_obj = paginator.page(paginator.num_pages)
            return render(request, 'publisher/homeplan/homeplan_listing_publisher.html',
                          dict(homeplan=homeplan_obj, tab_listing='homeplan_listing', tab='publish_homeplan_data',
                               stage_data=stage_data_obj,
                               category_obj=category_data, category_filter=category_filter))
        else:
            return HttpResponseRedirect(reverse('users-logout'))
    except Exception as e:
        raise Http404

####################################################################
# Name - lifeplan_publisher_listing                                #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@require_GET
def lifeplan_publisher_listing(request):
    try:
        assign_id = UserManagement.objects.get(user_id=request.user.id)
        stage_data_obj = Stage.objects.all()[3:5]
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
        if publisher_id:
            if category_id:
                lifeplan_obj = ServicePlan.objects.filter(Q(stage_id__gte=4),Q(category_id=category_id), Q(current_user_id =request.user.id),Q(is_life_service=True), Q(activation_status=True)).order_by('plan_name')
                category_filter = int(category_id)
            else:
                lifeplan_obj = ServicePlan.objects.filter(stage_id__gte=4,current_user_id =request.user.id,is_life_service=True,activation_status=True).order_by('plan_name')
            if len(lifeplan_obj) == 0:
                messages.error(request, "No lifeplan found")
                return render(request, 'publisher/lifeplan/lifeplan_listing_publisher.html',
                              {'tab_listing': 'lifeplan_listing', 'tab': 'publish_lifeplan_data',
                               'stage_data': stage_data_obj,
                               'category_obj': category_data, 'category_filter': category_filter})
            paginator = Paginator(lifeplan_obj, 50)
            page = request.GET.get('page')
            try:
                lifeplan_obj = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                lifeplan_obj = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                lifeplan_obj = paginator.page(paginator.num_pages)
            return render(request, 'publisher/lifeplan/lifeplan_listing_publisher.html',
                          dict(lifeplan=lifeplan_obj, tab_listing='lifeplan_listing', tab='publish_lifeplan_data',
                               stage_data=stage_data_obj,
                               category_obj=category_data, category_filter=category_filter))
        else:
            return HttpResponseRedirect(reverse('users-logout'))
    except Exception as e:
        raise Http404

####################################################################
# Name - enterpriseplan_publisher_listing                          #
# Owner -  Nishank                                                 #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@require_GET
def enterpriseplan_publisher_listing(request):
    try:
        assign_id = UserManagement.objects.get(user_id=request.user.id)
        stage_data_obj = Stage.objects.all()[3:5]
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
        if publisher_id:
            if category_id:
                enterpriseplan_obj = ServicePlan.objects.filter(Q(stage_id__gte=4),Q(category_id=category_id), Q(current_user_id =request.user.id),Q(is_enterprise_service=True), Q(activation_status=True)).order_by('plan_name')
                category_filter = int(category_id)
            else:
                enterpriseplan_obj = ServicePlan.objects.filter(stage_id__gte=4,current_user_id =request.user.id,is_enterprise_service=True, activation_status=True).order_by('plan_name')
            if len(enterpriseplan_obj) == 0:
                messages.error(request, "No enterpriseplan found")
                return render(request, 'publisher/enterpriseplan/enterpriseplan_listing_publisher.html',
                              {'tab_listing': 'enterpriseplan_listing', 'tab': 'publish_enterpriseplan_data',
                               'stage_data': stage_data_obj,
                               'category_obj': category_data, 'category_filter': category_filter})

            paginator = Paginator(enterpriseplan_obj, 50)
            page = request.GET.get('page')
            try:
                enterpriseplan_obj = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                enterpriseplan_obj = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                enterpriseplan_obj = paginator.page(paginator.num_pages)
            return render(request, 'publisher/enterpriseplan/enterpriseplan_listing_publisher.html',
                          dict(enterpriseplan=enterpriseplan_obj, tab_listing='enterpriseplan_listing', tab='publish_enterpriseplan_data',
                               stage_data=stage_data_obj,
                               category_obj=category_data, category_filter=category_filter))
        else:
            return HttpResponseRedirect(reverse('users-logout'))
    except Exception as e:
        raise Http404

####################################################################
# Name - search_home_plan_by_publisher                             #
# Addd by Nishank                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_home_plan_by_publisher(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            category_filter = False
            if q is not None:
                results = ServicePlan.objects.filter(stage_id=q,current_user_id=request.user.id,activation_status=True,is_home_service=True ).order_by('plan_name')
            paginator = Paginator(results, 50)
            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('publisher/homeplan/search_home_plan_by_stage_by_publisher.html',
                                    {'tab': 'publish_home_plan_data', 'crosal': 'home_planbymanagebypublisher',
                                     'homeplan': results,
                                     'category_filter': category_filter})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_life_plan_by_publisher                             #
# Aded by Nishank                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_life_plan_by_publisher(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            category_filter = False
            if q is not None:
                results = ServicePlan.objects.filter(stage_id=q,current_user_id=request.user.id,activation_status=True,is_life_service=True ).order_by('plan_name')
            paginator = Paginator(results, 50)
            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('publisher/lifeplan/search_life_plan_by_stage_by_publisher.html',
                                    {'tab': 'publish_life_plan_data', 'crosal': 'life_planbymanagebypublisher',
                                     'lifeplan': results,
                                     'category_filter': category_filter})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name: search_enterprise_plan_by_publisher                        #
#Added by Nishank                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_enterprise_plan_by_publisher(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            category_filter = False
            if q is not None:
                results = ServicePlan.objects.filter(stage_id=q,current_user_id=request.user.id,activation_status=True,is_enterprise_service=True ).order_by('plan_name')
            paginator = Paginator(results, 50)
            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('publisher/enterpriseplan/search_enterprise_plan_by_stage_by_publisher.html',
                                    {'tab': 'publish_enterprise_plan_data', 'crosal': 'enterprise_planbymanagebypublisher',
                                     'enterpriseplan': results,
                                     'category_filter': category_filter})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - master_data                                               #
# Owner - Dhrumil Shah                                             #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def service_plans_masters(request):
    try:
        if request.method == "GET":
            count = PlanCat.objects.all().count()
            count1 = PlanSubCat.objects.all().count()
            count2 = PlanDetails.objects.all().count()
            count3 = PlanComponent.objects.all().count()
            count4 = PlanSubComponent.objects.all().count()
            return render(request, 'service_plan_masters/service_plan_masters.html',
                          {'count':count, 'count1':count1, 'count2':count2, 'count3':count3, 'count4':count4,})
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - Plan Category Listing                                     #
# Owner - Dhrumil Shah                                             #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def category_listing(request):
    try:
        category = PlanCat.objects.all().order_by('name')
        return render(request, 'service_plan_masters/plan_cat_listing.html', {'category':category})
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - Add Edit Plan Category                                    #
# Owner - Dhrumil Shah                                             #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def add_edit_plan_category(request, cat_id=None):
    try:
        if cat_id != None:
            admin_action = 'Edit'
            if request.method == 'GET':
                category = PlanCat.objects.get(id=cat_id)
                return render(request, 'service_plan_masters/add_edit_plan_category.html',
                              {'category': category, 'admin_action': admin_action})
            elif request.method == 'POST':
                name = request.POST['category_name'].strip()
                category = PlanCat.objects.get(id=cat_id)
                if name:
                    category_all = PlanCat.objects.all().exclude(id=cat_id)
                    for i in category_all:
                        if i.name.lower() == name.lower():
                            messages.error(request, "Plan Category already exist")
                            return HttpResponseRedirect(reverse('category_listing'))
                    category.name = name
                    category.save()
                    messages.success(request, 'Plan Category Changed Successfully')
                    return HttpResponseRedirect(reverse('category_listing'))
                else:
                    messages.error(request, 'Please provide name')
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            admin_action = 'Add'
            if request.method == 'GET':
                return render(request, 'service_plan_masters/add_edit_plan_category.html',
                              {'admin_action': admin_action})
            elif request.method == 'POST':
                name = request.POST['category_name'].strip()
                if name:
                    category_all = PlanCat.objects.all()
                    for i in category_all:
                        if i.name.lower() == name.lower():
                            messages.error(request, "Plan Category already exist")
                            return HttpResponseRedirect(reverse('category_listing'))
                    PlanCat(name=name).save()
                    messages.success(request, 'Plan Category Added Successfully')
                    return HttpResponseRedirect(reverse('category_listing'))
                else:
                    messages.error(request, 'Please provide name')
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - Plan Sub Category Listing                                 #
# Owner - Dhrumil Shah                                             #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def sub_category_listing(request):
    try:
        sub_category = PlanSubCat.objects.all().order_by('name')
        return render(request, 'service_plan_masters/plan_sub_cat_listing.html',
                      {'sub_category':sub_category})
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - Add Edit Plan Sub Category                                #
# Owner - Dhrumil Shah                                             #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def add_edit_plan_sub_category(request, subcat_id=None):
    try:
        category_all = PlanCat.objects.filter(delete=False)
        if subcat_id != None:
            admin_action = 'Edit'
            if request.method == 'GET':
                subcategory = PlanSubCat.objects.get(id=subcat_id)
                return render(request, 'service_plan_masters/add_edit_plan_sub_category.html',
                              {'category_all':category_all, 'subcategory': subcategory, 'admin_action': admin_action})
            elif request.method == 'POST':
                category = request.POST['category'].strip()
                subcategory_name = request.POST['sub_category_name'].strip()
                subcategory = PlanSubCat.objects.all().exclude(id=subcat_id)
                subcat_obj = PlanSubCat.objects.get(id=subcat_id)
                if subcategory_name and category:
                    category_obj = PlanCat.objects.get(id=category)
                    for i in subcategory:
                        if i.name.lower() == subcategory_name.lower():
                            messages.error(request, "Plan Sub Category already exist")
                            return HttpResponseRedirect(reverse('sub_category_listing'))
                    subcat_obj.name = subcategory_name
                    subcat_obj.category = category_obj
                    subcat_obj.save()
                    messages.success(request, 'Plan Category Changed Successfully')
                    return HttpResponseRedirect(reverse('sub_category_listing'))
                else:
                    messages.error(request, 'Please provide appropriate data...')
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            admin_action = 'Add'
            if request.method == 'GET':
                return render(request, 'service_plan_masters/add_edit_plan_sub_category.html',
                              {'category_all':category_all,'admin_action': admin_action})
            elif request.method == 'POST':
                category = request.POST['category'].strip()
                category_obj = PlanCat.objects.get(id=category)
                subcategory_name = request.POST['sub_category_name'].strip()
                subcategory = PlanSubCat.objects.all()
                if subcategory_name and category:
                    for i in subcategory:
                        if i.name.lower() == subcategory_name.lower():
                            messages.error(request, "Plan Sub Category already exist")
                            return HttpResponseRedirect(reverse('sub_category_listing'))
                    PlanSubCat(name=subcategory_name, category=category_obj).save()
                    messages.success(request, 'Plan Category Added Successfully')
                    return HttpResponseRedirect(reverse('sub_category_listing'))
                else:
                    messages.error(request, 'Please provide appropriate data...')
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - Plan Details Listing                                      #
# Owner - Dhrumil Shah                                             #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def plan_details_listing(request):
    try:
        plan_details = PlanDetails.objects.all().order_by('name')
        return render(request, 'service_plan_masters/plan_details_listing.html', {'plan_details':plan_details})
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - Add Edit Plan Details                                     #
# Owner - Dhrumil Shah                                             #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def add_edit_plan_details(request, detail_id=None):
    try:
        if detail_id != None:
            admin_action = 'Edit'
            if request.method == 'GET':
                plan_details = PlanDetails.objects.get(id=detail_id)
                return render(request, 'service_plan_masters/add_edit_plan_details.html',
                              {'plan_details': plan_details, 'admin_action': admin_action})
            elif request.method == 'POST':
                name = request.POST['detail_name'].strip()
                plan_details = PlanDetails.objects.get(id=detail_id)
                if name:
                    plan_detail_all = PlanDetails.objects.all().exclude(id=detail_id)
                    for i in plan_detail_all:
                        if i.name.lower() == name.lower():
                            messages.error(request, "Plan Detail already exist")
                            return HttpResponseRedirect(reverse('plan_details_listing'))
                    plan_details.name = name
                    plan_details.save()
                    messages.success(request, 'Plan Detail Changed Successfully')
                    return HttpResponseRedirect(reverse('plan_details_listing'))
                else:
                    messages.error(request, 'Please provide name')
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            admin_action = 'Add'
            if request.method == 'GET':
                return render(request, 'service_plan_masters/add_edit_plan_details.html',
                              {'admin_action': admin_action})
            elif request.method == 'POST':
                name = request.POST['detail_name'].strip()
                if name:
                    plan_detail_all = PlanDetails.objects.all()
                    for i in plan_detail_all:
                        if i.name.lower() == name.lower():
                            messages.error(request, "Plan Detail already exist")
                            return HttpResponseRedirect(reverse('plan_details_listing'))
                    PlanDetails(name=name).save()
                    messages.success(request, 'Plan Detail Added Successfully')
                    return HttpResponseRedirect(reverse('plan_details_listing'))
                else:
                    messages.error(request, 'Please provide name')
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - Plan Component Listing                                    #
# Owner - Dhrumil Shah                                             #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def component_listing(request):
    try:
        component = PlanComponent.objects.all().order_by('name')
        return render(request, 'service_plan_masters/plan_component_listing.html', {'component':component})
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - Add Edit Plan Component                                   #
# Owner - Dhrumil Shah                                             #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def add_edit_plan_component(request, component_id=None):
    try:
        if component_id != None:
            admin_action = 'Edit'
            if request.method == 'GET':
                component = PlanComponent.objects.get(id=component_id)
                plan_details = PlanDetails.objects.filter(delete=False)
                return render(request, 'service_plan_masters/add_edit_plan_components.html',
                              {'component': component, 'plan_details':plan_details, 'admin_action': admin_action})
            elif request.method == 'POST':
                name = request.POST['component_name'].strip()
                detail = request.POST['detail']
                component = PlanComponent.objects.get(id=component_id)
                if name and detail:
                    detail_obj = PlanDetails.objects.get(id=detail)
                    component_all = PlanComponent.objects.all().exclude(id=component_id)
                    for i in component_all:
                        if i.name.lower() == name.lower():
                            messages.error(request, "Plan Component already exist")
                            return HttpResponseRedirect(reverse('component_listing'))
                    component.name = name
                    component.plan_details = detail_obj
                    component.save()
                    messages.success(request, 'Plan Component Changed Successfully')
                    return HttpResponseRedirect(reverse('component_listing'))
                else:
                    messages.error(request, 'Please provide appropriate data...')
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            admin_action = 'Add'
            if request.method == 'GET':
                plan_details = PlanDetails.objects.filter(delete=False)
                return render(request, 'service_plan_masters/add_edit_plan_components.html',
                              {'plan_details':plan_details, 'admin_action': admin_action})
            elif request.method == 'POST':
                name = request.POST['component_name'].strip()
                details = request.POST['detail']
                details_obj = PlanDetails.objects.get(id=details)
                if name and details:
                    component_all = PlanComponent.objects.all()
                    for i in component_all:
                        if i.name.lower() == name.lower():
                            messages.error(request, "Plan Component already exist")
                            return HttpResponseRedirect(reverse('component_listing'))
                    PlanComponent(name=name, plan_details=details_obj).save()
                    messages.success(request, 'Plan Component Added Successfully')
                    return HttpResponseRedirect(reverse('component_listing'))
                else:
                    messages.error(request, 'Please provide appropriate data...')
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - Plan Sub Component Listing                                #
# Owner - Dhrumil Shah                                             #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def sub_component_listing(request):
    try:
        sub_component = PlanSubComponent.objects.all().order_by('name')
        return render(request, 'service_plan_masters/plan_sub_component_listing.html', {'sub_component':sub_component})
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - Add Edit Plan Sub Component                               #
# Owner - Dhrumil Shah                                             #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def add_edit_plan_sub_component(request, subcomponent_id=None):
    try:
        if subcomponent_id != None:
            admin_action = 'Edit'
            if request.method == 'GET':
                subcomponent = PlanSubComponent.objects.get(id=subcomponent_id)
                detail_all = PlanDetails.objects.filter(delete=False)
                component_all = PlanComponent.objects.filter(delete=False)
                return render(request, 'service_plan_masters/add_edit_plan_sub_components.html',
                              {'subcomponent': subcomponent, 'detail_all':detail_all, 'component_all':component_all, 'admin_action': admin_action})
            elif request.method == 'POST':
                name = request.POST['sub_component_name'].strip()
                details = request.POST['detail']
                try:
                    component = request.POST['component']
                except:
                    component = ''
                amount = request.POST['amount']
                if name and details and component:
                    detail_obj = PlanDetails.objects.get(id=details)
                    component_obj = PlanComponent.objects.get(id=component)
                    subcomponent = PlanSubComponent.objects.get(id=subcomponent_id)
                    subcomponent_all=PlanSubComponent.objects.all().exclude(id=subcomponent_id)
                    for i in subcomponent_all:
                        if i.name.lower() == name.lower():
                            messages.error(request, "Plan Sub Component already exist")
                            return HttpResponseRedirect(reverse('sub_component_listing'))
                    subcomponent.name = name
                    subcomponent.plan_detail = detail_obj
                    subcomponent.plan_component = component_obj
                    subcomponent.amount = int(amount)
                    subcomponent.save()
                    messages.success(request, 'Plan Sub Component Changed Successfully')
                    return HttpResponseRedirect(reverse('sub_component_listing'))
                else:
                    messages.error(request, 'Please provide appropriate data...')
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            admin_action = 'Add'
            if request.method == 'GET':
                detail_all = PlanDetails.objects.filter(delete=False)
                component_all = PlanComponent.objects.filter(delete=False)
                return render(request, 'service_plan_masters/add_edit_plan_sub_components.html',
                              {'detail_all':detail_all, 'component_all':component_all, 'admin_action': admin_action})
            elif request.method == 'POST':
                name = request.POST['sub_component_name'].strip()
                details = request.POST['detail']
                try:
                    component = request.POST['component']
                except:
                    component = ''
                amount = request.POST['amount']
                if name and details and component:
                    detail_obj = PlanDetails.objects.get(id=details)
                    component_obj = PlanComponent.objects.get(id=component)
                    subcomponent_all = PlanSubComponent.objects.all()
                    for i in subcomponent_all:
                        if i.name.lower() == name.lower():
                            messages.error(request, "Plan Sub Component already exist")
                            return HttpResponseRedirect(reverse('sub_component_listing'))
                    PlanSubComponent(name=name, plan_component=component_obj, plan_detail=detail_obj, amount=amount).save()
                    messages.success(request, 'Plan Sub Component Added Successfully')
                    return HttpResponseRedirect(reverse('sub_component_listing'))
                else:
                    messages.error(request, 'Please provide appropriate data...')
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    except Exception as e:
        print e
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - Service Plan Listing for admin                            #
# Owner - Dhrumil Shah                                             #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def service_plans_listing_admin(request):
    try:
        stage_data = Stage.objects.all()
        city_obj = Citymaster.objects.filter(deletee=False)
        provider_obj = ServiceProvider.objects.all()
        cat_obj = PlanCat.objects.filter(delete=False)
        sub_cat_obj = PlanSubCat.objects.filter(delete=False)
        try:
            plan_filter = request.GET['x']
        except:
            plan_filter = ''
        if plan_filter:
            city = request.GET['city_id']
            cat = request.GET['cat_id']
            subcat = request.GET['sub_cat_id']
            provider = request.GET['provider']
            if city:
                city = int(city)
                if cat:
                    cat = int(cat)
                    if subcat:
                        subcat = int(subcat)
                        if provider:
                            provider = int(provider)
                            plan = PlanNew.objects.filter(Q(city_id=city),
                                                          Q(plan_category_id=cat),
                                                          Q(plan_sub_category_id=subcat),
                                                          Q(provider_id=provider))
                            return render(request, 'service_plan/plan_listing.html',
                                    {'plan':plan, 'stage_data':stage_data, 'city_obj':city_obj, 'provider_obj':provider_obj,
                                     'cat_obj':cat_obj, 'sub_cat_obj':sub_cat_obj, 'city':city, 'cat':cat, 'subcat':subcat,
                                     'provider':provider})
                        plan = PlanNew.objects.filter(Q(city_id=city),
                                                      Q(plan_category_id=cat),
                                                      Q(plan_sub_category_id=subcat))
                        return render(request, 'service_plan/plan_listing.html',
                                {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj, 'provider_obj': provider_obj,
                                 'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj, 'city':city, 'cat':cat, 'subcat':subcat,
                                 'provider':provider})
                    elif provider:
                        provider = int(provider)
                        plan = PlanNew.objects.filter(Q(city_id=city),
                                                      Q(plan_category_id=cat),
                                                      Q(provider_id=provider))
                        return render(request, 'service_plan/plan_listing.html',
                                      {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj,
                                       'provider_obj': provider_obj,
                                       'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj, 'city': city, 'cat': cat,
                                       'subcat': subcat,
                                       'provider': provider})
                    plan = PlanNew.objects.filter(Q(city_id=city),
                                                  Q(plan_category_id=cat))
                    return render(request, 'service_plan/plan_listing.html',
                              {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj,'provider_obj': provider_obj,
                               'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj, 'city': city, 'cat': cat,'subcat': subcat,
                               'provider': provider})
                elif provider:
                    provider = int(provider)
                    plan = PlanNew.objects.filter(Q(city_id=city),
                                                  Q(provider_id=provider))
                    return render(request, 'service_plan/plan_listing.html',
                                  {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj, 'provider_obj': provider_obj,
                                   'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj, 'city': city, 'cat': cat, 'subcat': subcat,
                                   'provider': provider})
                elif subcat:
                    subcat = int(subcat)
                    plan = PlanNew.objects.filter(Q(city_id=city),
                                                  Q(plan_sub_category_id=subcat))
                    return render(request, 'service_plan/plan_listing.html',
                                  {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj, 'provider_obj': provider_obj,
                                   'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj, 'city': city, 'cat': cat, 'subcat': subcat,
                                   'provider': provider})
                plan = PlanNew.objects.filter(Q(city_id=city))
                return render(request, 'service_plan/plan_listing.html',
                              {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj, 'provider_obj': provider_obj,
                               'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj, 'city': city, 'cat': cat, 'subcat': subcat,
                               'provider': provider})
            elif cat:
                cat = int(cat)
                if subcat:
                    subcat = int(subcat)
                    if provider:
                        provider = int(provider)
                        plan = PlanNew.objects.filter(Q(plan_category_id=cat),
                                                      Q(plan_sub_category_id=subcat),
                                                      Q(provider_id=provider))
                        return render(request, 'service_plan/plan_listing.html',
                                      {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj,
                                       'provider_obj': provider_obj,
                                       'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj, 'city': city, 'cat': cat,
                                       'subcat': subcat,
                                       'provider': provider})
                    plan = PlanNew.objects.filter(Q(plan_category_id=cat),
                                                  Q(plan_sub_category_id=subcat))
                    return render(request, 'service_plan/plan_listing.html',
                                  {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj,
                                   'provider_obj': provider_obj,
                                   'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj, 'city': city, 'cat': cat,
                                   'subcat': subcat,
                                   'provider': provider})
                elif provider:
                    provider = int(provider)
                    plan = PlanNew.objects.filter(Q(plan_category_id=cat),
                                                  Q(provider_id=provider))
                    return render(request, 'service_plan/plan_listing.html',
                                  {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj,
                                   'provider_obj': provider_obj,
                                   'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj, 'city': city, 'cat': cat,
                                   'subcat': subcat,
                                   'provider': provider})
                plan = PlanNew.objects.filter(Q(plan_category_id=cat))
                return render(request, 'service_plan/plan_listing.html',
                              {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj,
                               'provider_obj': provider_obj,
                               'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj, 'city': city, 'cat': cat,
                               'subcat': subcat,
                               'provider': provider})
            elif provider:
                provider = int(provider)
                if subcat:
                    subcat = int(subcat)
                    plan = PlanNew.objects.filter(Q(provider_id=provider),
                                                  Q(plan_sub_category_id=subcat))
                    return render(request, 'service_plan/plan_listing.html',
                                  {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj,
                                   'provider_obj': provider_obj,
                                   'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj, 'city': city, 'cat': cat,
                                   'subcat': subcat,
                                   'provider': provider})
                plan = PlanNew.objects.filter(Q(provider_id=provider))
                return render(request, 'service_plan/plan_listing.html',
                              {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj,
                               'provider_obj': provider_obj,
                               'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj, 'city': city, 'cat': cat,
                               'subcat': subcat,
                               'provider': provider})
            elif subcat:
                subcat = int(subcat)
                plan = PlanNew.objects.filter(Q(plan_sub_category_id=subcat))
                return render(request, 'service_plan/plan_listing.html',
                              {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj,
                               'provider_obj': provider_obj,
                               'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj, 'city': city, 'cat': cat,
                               'subcat': subcat,
                               'provider': provider})
        plan = PlanNew.objects.all()
        return render(request, 'service_plan/plan_listing.html',
                      {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj,
                       'provider_obj': provider_obj,
                       'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj})
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - Service Plan Listing                                      #
# Owner - Dhrumil Shah                                             #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def service_plans_listing(request):
    try:
        stage_data = Stage.objects.all()
        city_obj = Citymaster.objects.filter(deletee=False)
        provider_obj = ServiceProvider.objects.all()
        cat_obj = PlanCat.objects.filter(delete=False)
        sub_cat_obj = PlanSubCat.objects.filter(delete=False)
        user = request.user
        try:
            plan_filter = request.GET['x']
        except:
            plan_filter = ''
        if plan_filter:
            city = request.GET['city_id']
            cat = request.GET['cat_id']
            subcat = request.GET['sub_cat_id']
            provider = request.GET['provider']
            if city:
                city = int(city)
                if cat:
                    cat = int(cat)
                    if subcat:
                        subcat = int(subcat)
                        if provider:
                            provider = int(provider)
                            plan = PlanNew.objects.filter(Q(current_user_id=user),
                                                          Q(city_id=city),
                                                          Q(plan_category_id=cat),
                                                          Q(plan_sub_category_id=subcat),
                                                          Q(provider_id=provider))
                            return render(request, 'service_plan/plan_listing.html',
                                          {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj,
                                           'provider_obj': provider_obj,
                                           'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj, 'city': city, 'cat': cat,
                                           'subcat': subcat,
                                           'provider': provider})
                        plan = PlanNew.objects.filter(Q(current_user_id=user),
                                                      Q(city_id=city),
                                                      Q(plan_category_id=cat),
                                                      Q(plan_sub_category_id=subcat))
                        return render(request, 'service_plan/plan_listing.html',
                                      {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj,
                                       'provider_obj': provider_obj,
                                       'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj, 'city': city, 'cat': cat,
                                       'subcat': subcat,
                                       'provider': provider})
                    elif provider:
                        provider = int(provider)
                        plan = PlanNew.objects.filter(Q(current_user_id=user),
                                                      Q(city_id=city),
                                                      Q(plan_category_id=cat),
                                                      Q(provider_id=provider))
                        return render(request, 'service_plan/plan_listing.html',
                                      {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj,
                                       'provider_obj': provider_obj,
                                       'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj, 'city': city, 'cat': cat,
                                       'subcat': subcat,
                                       'provider': provider})
                    plan = PlanNew.objects.filter(Q(current_user_id=user),
                                                  Q(city_id=city),
                                                  Q(plan_category_id=cat))
                    return render(request, 'service_plan/plan_listing.html',
                                  {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj,
                                   'provider_obj': provider_obj,
                                   'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj, 'city': city, 'cat': cat,
                                   'subcat': subcat,
                                   'provider': provider})
                elif provider:
                    provider = int(provider)
                    plan = PlanNew.objects.filter(Q(current_user_id=user),
                                                  Q(city_id=city),
                                                  Q(provider_id=provider))
                    return render(request, 'service_plan/plan_listing.html',
                                  {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj,
                                   'provider_obj': provider_obj,
                                   'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj, 'city': city, 'cat': cat,
                                   'subcat': subcat,
                                   'provider': provider})
                elif subcat:
                    subcat = int(subcat)
                    plan = PlanNew.objects.filter(Q(current_user_id=user),
                                                  Q(city_id=city),
                                                  Q(plan_sub_category_id=subcat))
                    return render(request, 'service_plan/plan_listing.html',
                                  {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj,
                                   'provider_obj': provider_obj,
                                   'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj, 'city': city, 'cat': cat,
                                   'subcat': subcat,
                                   'provider': provider})
                plan = PlanNew.objects.filter(Q(current_user_id=user),
                                              Q(city_id=city))
                return render(request, 'service_plan/plan_listing.html',
                              {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj,
                               'provider_obj': provider_obj,
                               'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj, 'city': city, 'cat': cat,
                               'subcat': subcat,
                               'provider': provider})
            elif cat:
                cat = int(cat)
                if subcat:
                    subcat = int(subcat)
                    if provider:
                        provider = int(provider)
                        plan = PlanNew.objects.filter(Q(current_user_id=user),
                                                      Q(plan_category_id=cat),
                                                      Q(plan_sub_category_id=subcat),
                                                      Q(provider_id=provider))
                        return render(request, 'service_plan/plan_listing.html',
                                      {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj,
                                       'provider_obj': provider_obj,
                                       'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj, 'city': city, 'cat': cat,
                                       'subcat': subcat,
                                       'provider': provider})
                    plan = PlanNew.objects.filter(Q(current_user_id=user),
                                                  Q(plan_category_id=cat),
                                                  Q(plan_sub_category_id=subcat))
                    return render(request, 'service_plan/plan_listing.html',
                                  {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj,
                                   'provider_obj': provider_obj,
                                   'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj, 'city': city, 'cat': cat,
                                   'subcat': subcat,
                                   'provider': provider})
                elif provider:
                    provider = int(provider)
                    plan = PlanNew.objects.filter(Q(current_user_id=user),
                                                  Q(plan_category_id=cat),
                                                  Q(provider_id=provider))
                    return render(request, 'service_plan/plan_listing.html',
                                  {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj,
                                   'provider_obj': provider_obj,
                                   'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj, 'city': city, 'cat': cat,
                                   'subcat': subcat,
                                   'provider': provider})
                plan = PlanNew.objects.filter(Q(current_user_id=user),
                                              Q(plan_category_id=cat))
                return render(request, 'service_plan/plan_listing.html',
                              {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj,
                               'provider_obj': provider_obj,
                               'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj, 'city': city, 'cat': cat,
                               'subcat': subcat,
                               'provider': provider})
            elif provider:
                provider = int(provider)
                if subcat:
                    subcat = int(subcat)
                    plan = PlanNew.objects.filter(Q(current_user_id=user),
                                                  Q(provider_id=provider),
                                                  Q(plan_sub_category_id=subcat))
                    return render(request, 'service_plan/plan_listing.html',
                                  {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj,
                                   'provider_obj': provider_obj,
                                   'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj, 'city': city, 'cat': cat,
                                   'subcat': subcat,
                                   'provider': provider})
                plan = PlanNew.objects.filter(Q(current_user_id=user),
                                              Q(provider_id=provider))
                return render(request, 'service_plan/plan_listing.html',
                              {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj,
                               'provider_obj': provider_obj,
                               'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj, 'city': city, 'cat': cat,
                               'subcat': subcat,
                               'provider': provider})
            elif subcat:
                subcat = int(subcat)
                plan = PlanNew.objects.filter(Q(current_user_id=user),
                                              Q(plan_sub_category_id=subcat))
                return render(request, 'service_plan/plan_listing.html',
                              {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj,
                               'provider_obj': provider_obj,
                               'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj, 'city': city, 'cat': cat,
                               'subcat': subcat,
                               'provider': provider})
        plan = PlanNew.objects.filter(Q(current_user_id=user))
        return render(request, 'service_plan/plan_listing.html',
                      {'plan': plan, 'stage_data': stage_data, 'city_obj': city_obj,
                       'provider_obj': provider_obj,
                       'cat_obj': cat_obj, 'sub_cat_obj': sub_cat_obj})
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - Cat_SubCat                                                #
# By Dhrumil Shah                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def cat_subcat(request):
    data = {}
    try:
        response1 = {}
        if request.method == "POST":
            plancategory_id = request.POST['id'].strip()
            if plancategory_id is not None:
                cat = PlanCat.objects.get(id=plancategory_id)
                subcat = PlanSubCat.objects.filter(category=cat, delete=False).values('id', 'name')
                if len(subcat):
                    response1['subcat'] = list(subcat)
                else:
                    response1['Message'] = "No Sub Category"
                    response1['subcat'] = []
            else:
                response1['Message'] = "Please select Plan category"
        data = json.dumps(response1)
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponse(data)

####################################################################
# Name - Detail Component                                          #
# By Dhrumil Shah                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def detail_component(request):
    data = {}
    try:
        response1 = {}
        if request.method == "POST":
            plandetail_id = request.POST['id'].strip()
            if plandetail_id is not None:
                detail = PlanDetails.objects.get(id=plandetail_id)
                component = PlanComponent.objects.filter(plan_details=detail, delete=False).values('id', 'name')
                if len(component):
                    response1['component'] = list(component)
                else:
                    response1['Message'] = "No Component"
                    response1['component'] = []
            else:
                response1['Message'] = "Please Select Plan Component"
        data = json.dumps(response1)
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponse(data)
####################################################################
# Name - Detail Component                                          #
# By Dhrumil Shah                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def component_subcomponent(request):

    data = {}
    try:
        response1 = {}
        if request.method == "POST":
            plancomponent_id = request.POST['id'].strip()
            if plancomponent_id is not None:
                component = PlanComponent.objects.get(id=plancomponent_id)
                subcomponent = PlanSubComponent.objects.filter(plan_component=component, delete=False).values('id', 'name')
                if len(subcomponent):
                    response1['subcomponent'] = list(subcomponent)
                else:
                    response1['Message'] = "No Sub Component"
                    response1['subcomponent'] = []
            else:
                response1['Message'] = "Please Select Plan Sub Component"
        data = json.dumps(response1)
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponse(data)

####################################################################
# Name - Add Service Plan                                          #
# Owner - Dhrumil Shah                                             #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def service_plan_add(request):
    try:
        if request.method == 'GET':
            city_obj = Citymaster.objects.filter(deletee=False)
            provider_name = ServiceProvider.objects.all()
            category = PlanCat.objects.filter(delete=False)
            sub_category = PlanSubCat.objects.filter(delete=False)
            return render(request, 'service_plan/add_plannew.html',
                          {'city_obj':city_obj, 'provider_name':provider_name, 'category':category, 'sub_category':sub_category})
        elif request.method == 'POST':
            user = request.user.id
            stage = Stage.objects.get(id=2)
            city = request.POST['city'].strip()
            city_obj = Citymaster.objects.get(id=city)
            provider = request.POST['provider']
            provider_obj = ServiceProvider.objects.get(id=provider)
            category = request.POST['plancat']
            category_obj = PlanCat.objects.get(id=category)
            subcategory = request.POST['plansubcat']
            subcategory_obj = PlanSubCat.objects.get(id=subcategory)
            plan_name = request.POST['planname'].strip()
            try:
                plan_duration = int(request.POST['duration'])
            except:
                plan_duration = ''
            try:
                min_emp = int(request.POST['no_of_emp'])
            except:
                min_emp = ''
            gender = request.POST['gender']
            try:
                from_age = int(request.POST['from_age'])
            except:
                from_age = ''
            try:
                to_age = int(request.POST['to_age'])
            except:
                to_age = ''
            try:
                short_desc = request.POST['short_desc'].strip()
            except:
                short_desc = ''
            try:
                desc = request.POST['desc'].strip()
            except:
                desc = ''
            try:
                instruction = request.POST['instructions'].strip()
            except:
                instruction = ''
            try:
                other_field = {'plan_name':plan_name, 'plan_duration':plan_duration, 'min_emp':min_emp, 'gender':gender, 'from_age':from_age,
                           'to_age':to_age, 'short_desc':short_desc, 'desc':desc, 'instruction':instruction}
            except Exception as e:
                other_field = {}
            new_plan = PlanNew(stage=stage, current_user_id=user, provider=provider_obj, plan_category=category_obj,
                    plan_sub_category=subcategory_obj, other_details=other_field, city=city_obj, test_details=[])
            new_plan.save()
            return redirect(reverse('plannew-edit', args=[new_plan.id]) + "?tab=1")
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - Add Edit Plan Sub Category                                #
# Owner - Dhrumil Shah                                             #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def service_plan_edit(request, plannew_id):
    try:
        tab = None
        try:
            tab = request.GET['tab']
        except:
            tab = None
        publisher_user_data = UserManagement.objects.filter(is_publisher=True, user__is_active=True)
        reviewer_user_data = UserManagement.objects.filter(is_reviewer=True, user__is_active=True,
                                                           is_service_reviewer=True)
        caller_user_data = UserManagement.objects.filter(user__is_active=True, is_service_plan=True)
        # Have not put is_caller = True for the sake of old users
        valid_choice = ValidateByChoice.objects.all()
        if plannew_id:
            city = Citymaster.objects.filter(deletee=False)
            provider_name = ServiceProvider.objects.all()
            category = PlanCat.objects.filter(delete=False)
            sub_category = PlanSubCat.objects.filter(delete=False)
            plan_detail = PlanDetails.objects.filter(delete=False)
            plan_component = PlanComponent.objects.filter(delete=False)
            plan_subcomponent = PlanSubComponent.objects.filter(delete=False)
            plan_obj = PlanNew.objects.get(id=plannew_id)
            if tab == '1' and request.method == 'GET':
                try:
                    return render(request, 'service_plan/edit_plan_new.html',
                              {'tab':tab, 'city':city, 'provider_name':provider_name, 'category':category,
                               'sub_category':sub_category, 'plan_detail':plan_detail, 'plan_component':plan_component,
                               'plan_subcomponent':plan_subcomponent, 'plan_obj':plan_obj, 'publisher_user_data':publisher_user_data,
                               'reviewer_user_data':reviewer_user_data, 'caller_user_data':caller_user_data, 'valid_choice':valid_choice})
                except Exception as e:
                    print e
                    messages.error(request, e)
            elif tab == '1' and request.method == 'POST':
                user = request.user.id
                plan_obj.current_user_id = user
                stage = Stage.objects.get(id=2)
                plan_obj.stage = stage
                city = request.POST['city'].strip()
                city_obj = Citymaster.objects.get(id=city)
                plan_obj.city = city_obj
                provider = request.POST['provider']
                provider_obj = ServiceProvider.objects.get(id=provider)
                plan_obj.provider = provider_obj
                category = request.POST['plancat']
                category_obj = PlanCat.objects.get(id=category)
                plan_obj.plan_category = category_obj
                subcategory = request.POST['plansubcat']
                subcategory_obj = PlanSubCat.objects.get(id=subcategory)
                plan_obj.plan_sub_category = subcategory_obj
                plan_name = request.POST['planname'].strip()
                plan_obj.other_details['plan_name'] = plan_name
                try:
                    plan_duration = request.POST['duration']
                    plan_obj.other_details['plan_duration'] = int(plan_duration)
                except:
                    plan_duration = ''
                try:
                    min_emp = request.POST['no_of_emp']
                    plan_obj.other_details['min_emp'] = int(min_emp)
                except:
                    min_emp = ''
                gender = request.POST['gender']
                plan_obj.other_details['gender'] = gender
                try:
                    from_age = request.POST['from_age']
                    plan_obj.other_details['from_age'] = int(from_age)
                except:
                    from_age = ''
                try:
                    to_age = request.POST['to_age']
                    plan_obj.other_details['to_age'] = int(to_age)
                except:
                    to_age = ''
                try:
                    short_desc = request.POST['short_desc'].strip()
                    plan_obj.other_details['short_desc'] = short_desc
                except:
                    short_desc = ''
                try:
                    desc = request.POST['desc'].strip()
                    plan_obj.other_details['desc'] = desc
                except:
                    desc = ''
                try:
                    instruction = request.POST['instructions'].strip()
                    plan_obj.other_details['instruction'] = instruction
                except:
                    instruction = ''
                plan_obj.save()
                return redirect(reverse('plannew-edit', args=[plan_obj.id]) + "?tab=1")
            elif tab == '2' and request.method == 'GET':
                try:
                    return render(request, 'service_plan/edit_plan_new.html',
                              {'tab':tab, 'city':city, 'provider_name':provider_name, 'category':category,
                               'sub_category':sub_category, 'plan_detail':plan_detail, 'plan_component':plan_component,
                               'plan_subcomponent':plan_subcomponent, 'plan_obj':plan_obj, 'publisher_user_data':publisher_user_data,
                               'reviewer_user_data':reviewer_user_data, 'caller_user_data':caller_user_data, 'valid_choice':valid_choice})
                except Exception as e:
                    messages.error(request, e)
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            elif tab == '2' and request.method == 'POST':
                try:
                    try:
                        dc = request.POST['dc']
                    except:
                        dc = ''
                    if dc == 'dc':
                        dis_prize = request.POST['dis_price']
                        try:
                            plan_obj.discounted_price = int(dis_prize)
                        except Exception as e:
                            messages.error(request, "Only Numbers please...")
                            return redirect(reverse('plannew-edit', args=[plan_obj.id]) + "?tab=2")
                        plan_obj.save()
                        messages.success(request, "Discounted Price added")
                        return HttpResponseRedirect(reverse('plannew-edit', args=[plan_obj.id]) + "?tab=2")
                    test_list = plan_obj.test_details
                    subcomponent_name = request.POST['subcomponent']
                    sub_comp = PlanSubComponent.objects.get(id=subcomponent_name)
                    detail_nm = sub_comp.plan_detail.name
                    component_nm = sub_comp.plan_component.name
                    subcomponent_nm = sub_comp.name
                    amount_nm = sub_comp.amount
                    count = request.POST['test_count']
                    if len(test_list) == 0:
                        detail_dict = {}
                        comp_dict = {}
                        subcomp_dict = {}
                        comp_list = []
                        subcomp_list = []
                        subcomp_dict['s_name'] = subcomponent_nm
                        subcomp_dict['s_count'] = int(count)
                        subcomp_dict['s_amount'] = int(amount_nm) * int(count)
                        plan_obj.total_price = int(subcomp_dict['s_amount'])
                        subcomp_list.append(subcomp_dict)
                        comp_dict['c_name'] = component_nm
                        comp_dict['c_subcomp'] = subcomp_list
                        comp_list.append(comp_dict)
                        detail_dict['d_name'] = detail_nm
                        detail_dict['d_comp'] = comp_list
                        test_list.append(detail_dict)
                        plan_obj.test_details = test_list
                        plan_obj.save()
                        messages.success(request, "Test Added Successfully")
                        return redirect(reverse('plannew-edit', args=[plan_obj.id]) + "?tab=2")
                    else:
                        total_cost = int(plan_obj.total_price)
                        detail_dict = {}
                        comp_dict = {}
                        subcomp_dict = {}
                        comp_list = []
                        subcomp_list = []
                        for i in test_list:
                            if i['d_name'] == detail_nm:
                                for j in i['d_comp']:
                                    if j['c_name'] == component_nm:
                                        for k in j['c_subcomp']:
                                            if k['s_name'] == subcomponent_nm:
                                                messages.error(request, "Test Already Exist")
                                                return redirect(reverse('plannew-edit', args=[plan_obj.id]) + "?tab=2")
                                        subcomp_dict['s_name'] = subcomponent_nm
                                        subcomp_dict['s_count'] = int(count)
                                        subcomp_dict['s_amount'] = int(amount_nm) * int(count)
                                        total_cost = int(total_cost) + int(subcomp_dict['s_amount'])
                                        plan_obj.total_price = int(total_cost)
                                        j['c_subcomp'].append(subcomp_dict)
                                        plan_obj.test_details = test_list
                                        plan_obj.save()
                                        messages.success(request, "Test Added Successfully")
                                        return redirect(reverse('plannew-edit', args=[plan_obj.id]) + "?tab=2")
                                subcomp_dict['s_name'] = subcomponent_nm
                                subcomp_dict['s_count'] = int(count)
                                subcomp_dict['s_amount'] = int(amount_nm) * int(count)
                                total_cost = int(total_cost) + int(subcomp_dict['s_amount'])
                                plan_obj.total_price = int(total_cost)
                                subcomp_list.append(subcomp_dict)
                                comp_dict['c_name'] = component_nm
                                comp_dict['c_subcomp'] = subcomp_list
                                i['d_comp'].append(comp_dict)
                                plan_obj.test_details = test_list
                                plan_obj.save()
                                messages.success(request, "Test Added Successfully")
                                return redirect(reverse('plannew-edit', args=[plan_obj.id]) + "?tab=2")
                        subcomp_dict['s_name'] = subcomponent_nm
                        subcomp_dict['s_count'] = int(count)
                        subcomp_dict['s_amount'] = int(amount_nm) * int(count)
                        total_cost = int(total_cost) + int(subcomp_dict['s_amount'])
                        plan_obj.total_price = int(total_cost)
                        subcomp_list.append(subcomp_dict)
                        comp_dict['c_name'] = component_nm
                        comp_dict['c_subcomp'] = subcomp_list
                        comp_list.append(comp_dict)
                        detail_dict['d_name'] = detail_nm
                        detail_dict['d_comp'] = comp_list
                        test_list.append(detail_dict)
                        plan_obj.test_details = test_list
                        plan_obj.save()
                        messages.success(request, "Test Added Successfully")
                        return redirect(reverse('plannew-edit', args=[plan_obj.id]) + "?tab=2")

                except Exception as e:
                    messages.error(request, e)
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        messages.error(request,e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


####################################################################
# Name - Delete Plan Test                                          #
# Owner - Dhrumil Shah                                             #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def delete_test(request, plannew_id):
    try:
        if request.method == "GET" and plannew_id:
            subcomp_name = request.GET['s_name']
            plan_obj = PlanNew.objects.get(id=plannew_id)
            test_list = plan_obj.test_details
            total_cost = int(plan_obj.total_price)
            for i in test_list:
                for j in i['d_comp']:
                    for k in j['c_subcomp']:
                        if k['s_name'] == subcomp_name:
                            total_cost = int(total_cost) - int(k['s_amount'])
                            j['c_subcomp'].remove(k)
                    if len(j['c_subcomp']) == 0:
                        i['d_comp'].remove(j)
                if len(i['d_comp']) == 0:
                    test_list.remove(i)
            plan_obj.test_details = test_list
            plan_obj.total_price = total_cost
            plan_obj.save()
            messages.success(request, "Test Deleted")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - mark_as_complete_caller_service_plan                      #
# Owner - Dhrumil Shah                                             #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def mark_as_complete_caller_service_plan(request):
    try:
        if request.method == 'POST':
            plannew_id = request.POST['plannew-id']
            reviewer_data_id = request.POST['reviewer_name']
            valid_choice_id = request.POST['validator_name']
            plan_obj = PlanNew.objects.get(id=plannew_id)

            if plan_obj and reviewer_data_id and valid_choice_id:
                try:
                    plan_obj.current_user = User.objects.get(id=reviewer_data_id)
                    plan_obj.previous_user = request.user.id
                    plan_obj.stage = Stage.objects.get(pk=3)
                    plan_obj.free_text = ''
                    plan_obj.resource_validate = ValidateByChoice(id=valid_choice_id)
                    plan_obj.save()
                    messages.success(request, 'Successfully moved to next Stage')
                    return HttpResponseRedirect(reverse('plan-name-listing'))
                except:
                    raise Http404

            else:
                messages.error(request, 'Select Reviewer and Validation Choice')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            messages.error(request, 'Other Method not allowed')
        return HttpResponseRedirect(reverse('plan-name-listing'))
    except Exception as e:
        return HttpResponse("Something Bad Happened")

####################################################################
# Name - mark_as_reverse_caller_service_plan                       #
# Owner - Dhrumil Shah                                            #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def mark_as_reverse_caller_service_plan(request):
    try:
        if request.method == 'POST':
            plannew_id = request.POST['plannew-id']
            caller_data_id = request.POST['caller_name']
            free_text = request.POST['free_text']
            plan_obj = PlanNew.objects.get(id=plannew_id)
            if plan_obj and caller_data_id and free_text:
                try:
                    plan_obj.current_user = User.objects.get(id=caller_data_id)
                    plan_obj.previous_user = request.user.id
                    plan_obj.stage = Stage.objects.get(pk=2)
                    plan_obj.free_text = free_text
                    plan_obj.save()
                    messages.success(request, 'Successfully moved to "Previous" Stage')
                    User_management_obj = UserManagement.objects.filter(user_id=request.user.id, is_publisher=True)
                    if (len(User_management_obj)):
                        return HttpResponseRedirect(reverse('publisher-serviceplan-listing'))
                    return HttpResponseRedirect(reverse('plan-name-listing'))
                except:
                    pass
            else:
                messages.error(request, 'Select Reviewer and Validation Choice')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            messages.error(request, 'Other Method not allowed')
        User_management_obj = UserManagement.objects.filter(user_id=request.user.id, is_publisher=True)
        if (len(User_management_obj)):
            return HttpResponseRedirect(reverse('publisher-serviceplan-listing'))
        return HttpResponseRedirect(reverse('plan-name-listing'))
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - mark_as_complete_reviewer_service_plan                    #
# Owner - Dhrumil Shah                                             #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def mark_as_complete_reviewer_service_plan(request):
    try:
        if request.method == 'POST':
            plannew_id = request.POST['plannew-id']
            publisher_data_id = request.POST['publisher_name']
            valid_choice_id = request.POST['validator_name']
            plan_obj = PlanNew.objects.get(id=plannew_id)

            if plan_obj and publisher_data_id and valid_choice_id:
                try:
                    plan_obj.current_user = User.objects.get(id=publisher_data_id)
                    plan_obj.previous_user = request.user.id
                    plan_obj.stage = Stage.objects.get(pk=4)
                    plan_obj.free_text = ''
                    plan_obj.resource_validate = ValidateByChoice(id=valid_choice_id)
                    plan_obj.save()
                    messages.success(request, 'Successfully moved to next Stage')
                    return HttpResponseRedirect(reverse('plan-name-listing'))

                except:

                    pass
            else:
                messages.error(request, 'Select Publisher and Validation Choice')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Other Method not allowed')
        return HttpResponseRedirect(reverse('plan-name-listing'))
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name -mark_as_reverse_reviewer_service_plan                      #
# Owner - Dhrumil Shah                                             #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def mark_as_reverse_reviewer_service_plan(request):
    try:
        if request.method == 'POST':
            plannew_id = request.POST['plannew-id']
            reviewer_data_id = request.POST['reviewer_name']
            free_text = request.POST['free_text']
            plan_obj = PlanNew.objects.get(id=plannew_id)

            if plan_obj and reviewer_data_id and free_text:
                try:
                    plan_obj.current_user = User.objects.get(id=reviewer_data_id)
                    plan_obj.previous_user = request.user.id
                    plan_obj.stage = Stage.objects.get(pk=3)
                    plan_obj.free_text = free_text
                    plan_obj.save()
                    messages.success(request, 'Successfully moved to "Previous" Stage')
                    return HttpResponseRedirect(reverse('publisher-serviceplan-listing'))
                except:
                    pass
            else:
                messages.error(request, 'Select Reviewer and Validation Choice')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Other Method not allowed')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - serviceplan_publisher_listing                             #
# Owner -  Dhrumil Shah                                            #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@require_GET
def serviceplan_publisher_listing(request):
    try:
        assign_id = UserManagement.objects.get(user_id=request.user.id)
        stage_data_obj = Stage.objects.all()[3:5]
        if assign_id.is_publisher is True:
            publisher_id = request.user.id
        else:
            publisher_id = 0
        if publisher_id:
            plan_obj = PlanNew.objects.filter(stage_id__gte=4,current_user_id =request.user.id, activation_status=True)
            if len(plan_obj) == 0:
                return render(request, 'publisher/serviceplan/servcieplan_listing_publisher.html',
                              {'tab_listing': 'service_listing', 'tab': 'publish_serviceplan_data',
                               'stage_data': stage_data_obj,})
            return render(request, 'publisher/serviceplan/servcieplan_listing_publisher.html',
                          dict(plan_obj=plan_obj, tab_listing='service_listing', tab='publish_serviceplan_data',
                               stage_data=stage_data_obj))
        else:
            return HttpResponseRedirect(reverse('users-logout'))
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name: search_service_plan_by_publisher                           #
#Added by Dhrumil                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_service_plan_by_publisher_stage(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = PlanNew.objects.filter(stage_id=q,current_user_id=request.user.id,activation_status=True)
            html = render_to_string('publisher/serviceplan/search_service_plan_by_stage_by_publisher.html',
                                    {'tab': 'publish_service_plan_data', 'crosal': 'service_planbymanagebypublisher',
                                     'plan_obj': results})
            return HttpResponse(html)
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - assign Service Plan                                       #
# Owner - Dhrumil                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def assign_serviceplan(request):
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
                        assign_obj = PlanNew.objects.filter(id=checkedValues[i]).update(
                        current_user_id=assign_user,
                        stage_id=change_stage)
                        nbslist.append(checkedValues[i])
                    except:
                        nbflist.append(checkedValues[i])
                        continue
                response1['Redirect'] = True
                response1['RedirectUrl'] = '/service/plan-new/service-plan/listing-admin/'
                response1['Message'] = "Assign Complete"
            else:
                response1['Message'] = "Please select Stage and User "
            response = json.dumps(response1)
            return HttpResponse(response)
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - Search Service Plan by Admin                              #
# Owner - Dhrumil                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def search_service_plan_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                pl_obj = PlanNew.objects.all()
                results = []
                for i in pl_obj:
                    name = i.other_details['plan_name'].lower()
                    q = q.lower()
                    if name.find(q) != -1:
                        results.append(i)
            else:
                results = PlanNew.objects.all()
            html = render_to_string('service_plan/search_service_plan.html',
                                    {'plan': results, 'user':'admin'})
            return HttpResponse(html)
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

####################################################################
# Name - Search Service Plan by Publisher                          #
# Owner - Dhrumil                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_service_plan_by_publisher(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                pl_obj = PlanNew.objects.filter(current_user_id=request.user)
                results = []
                for i in pl_obj:
                    name = i.other_details['plan_name'].lower()
                    q = q.lower()
                    if name.find(q) != -1:
                        results.append(i)
            else:
                results = PlanNew.objects.filter(current_user_id=request.user)
            html = render_to_string('publisher/serviceplan/search_service_plan_by_stage_by_publisher.html',
                                    {'tab': 'publish_service_plan_data', 'crosal': 'service_planbymanagebypublisher',
                                     'plan_obj': results})
            return HttpResponse(html)
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


####################################################################
# Name - Search Service Plan by user                               #
# Owner - Dhrumil                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_service_plan_by_user(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if q is not None:
                pl_obj = PlanNew.objects.filter(current_user_id=user_id)
                results = []
                for i in pl_obj:
                    name = i.other_details['plan_name'].lower()
                    q = q.lower()
                    if name.find(q) != -1:
                        results.append(i)
            else:
                results = PlanNew.objects.filter(current_user_id=user_id)
            html = render_to_string('service_plan/search_service_plan.html',
                                    {'plan': results, 'user':'user'})
            return HttpResponse(html)
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))