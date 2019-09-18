# import here
from django.core.checks import messages

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token

from news.models import NewsFeed
from providers.models import ServicePlan
from .models import *
# from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect, Http404
from django.template.loader import render_to_string
# from views import paginate
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from hfu_cms.views import paginate
from django.core.urlresolvers import reverse
from django.shortcuts import render

####################################################################
# Name - search_doctor_caller                                      #
# Owner - Visnu Badal                                              #
# Review by - jitendra dixit
#                                                                  #
# comment : good
# change : assignment before   results                             #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_doctor_caller(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            usm = UserManagement.objects.get(user_id=request.user.id)
            if user_id and q is not None:
                if usm.is_reviewer and usm.is_doctor_reviewer:
                    results = Doctor.objects.filter(current_user_id=user_id, name__icontains=q).order_by('name')
                else:
                    results = Doctor.objects.filter(current_user_id=user_id, name__icontains=q,is_disable=False).order_by('name')
            elif user_id:
                if usm.is_reviewer and usm.is_doctor_reviewer:
                    results = Doctor.objects.filter(current_user_id=user_id).order_by('name')
                else:
                    results = Doctor.objects.filter(current_user_id=user_id, is_disable=False).order_by('name')
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
            html = render_to_string('data_management/search_data/search_doctor.html',
                                    {'doctor': results, 'tab_listing': 'doctor_listing','request':request})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_care_doctor                                        #
# By : Nishank                                                     #
####################################################################

@login_required(login_url='/')
@csrf_exempt
def search_care_doctor(request):
    try:
        if request.method == 'POST':
            q = None
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = Doctor.objects.filter(is_disable=False,provides_home_care=True,name__icontains =q).order_by('name')
            elif user_id:
                results = []
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
            html = render_to_string('data_management/search_data/care/search_care_doctor.html',
                                    {'doctor': results, 'tab_listing': 'doctor_listing','search_data': q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_doctor_caller                                      #
# Owner - Visnu Badal                                              #
# Review by - jitendra dixit
#                                                                  #
# comment : good
#                                                                  #
####################################################################


@login_required(login_url='/')
@csrf_exempt
def search_organisation_caller(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            usmo = UserManagement.objects.get(user_id = request.user.id)
            if user_id and q is not None:
                if usmo.is_reviewer and usmo.is_doctor_reviewer:
                    results = OrganisationName.objects.filter(current_user_id=user_id, name__icontains=q,is_live_org=False).order_by('name')
                else:
                    results = OrganisationName.objects.filter(current_user_id=user_id, name__icontains=q,
                                                          is_disable=False,is_live_org=False).order_by('name')
            elif user_id:
                results = OrganisationName.objects.filter(current_user_id=user_id,is_live_org=False, is_disable=False).order_by('name')
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
            html = render_to_string('data_management/search_data/search_organisation.html',
                                    {'organisation_data_obj': results,'request':request})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_lab_caller                                         #
# Owner - Jaydeep                                                  #
# Review by -                                                      #
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################

@login_required(login_url='/')
@csrf_exempt
def search_lab_caller(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = Labs.objects.filter(current_user_id=user_id, name__icontains=q,
                                                  is_disable=False).order_by('name')
            elif user_id:
                results = Labs.objects.filter(current_user_id=user_id, is_disable=False).order_by(
                        'name')
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
            html = render_to_string('data_management/search_data/search_lab.html',
                                    {'lab': results})
            return HttpResponse(html)
    except Exception as e:
        raise Http404



####################################################################
# Name - search_doctor_admin                                       #
# Owner - Visnu Badal                                              #
# Review by - jitendra dixit
#                                                                  #
# comment : good
#                                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_doctor_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Doctor.objects.filter(name__icontains=q)
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
            html = render_to_string('admin/doctor_management/search_admin_doctor.html',
                                    {'tab': 'data', 'crosal': 'doctorbymanage', 'doctor_all_data': results})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_doctor by user for association                     #
# Owner - Jaydeep                                                  #
# Review by -
#                                                                  #
# comment :
#                                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_doctor_association_by_user(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Doctor.objects.filter(name__icontains=q, stage__gte=2, is_disable=False)
            else:
                results = []
            try:
                results= paginate(results, 50)
                html = render_to_string('data_management/search_data/search_doctor_for_association.html',
                                        {'tab': 'data', 'crosal': 'doctorbymanage', 'doctor_data_obj': results})
            except Exception as e:

                html = "Bad Happened"
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_doctor_admin                                       #
# Owner - Visnu Badal                                              #
# Review by - jitendra dixit
#                                                                  #
# comment : good
#                                                                   #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_doctor_assign_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:

                results = Doctor.objects.filter(name__icontains=q)
            else:
                results = Doctor.objects.all()
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
            html = render_to_string('admin/doctor_management/search_admin_doctor.html',
                                    {'tab': 'data', 'crosal': 'doctorbymanage', 'doctor_data_obj': results,
                                     'search_data':q})
            return HttpResponse(html)
    except Exception as e:

        raise Http404

####################################################################
# Name - search_doctor_admin_on_stage and user                     #
# Owner - Jaydeep verma                                            #
#  Review by -                                                     #
# comment :
#                                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_doctor_admin_on_stage_user(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Doctor.objects.filter(name__icontains=q)
            else:
                results = Doctor.objects.all()
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
            html = render_to_string('admin/doctor_management/search_doctor_by_stages_user.html',
                                    {'tab': 'data', 'crosal': 'doctorbymanage', 'doctor_all_data': results,
                                     'search_data_two':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_organisation_admin                                 #
# Owner - Visnu Badal                                              #
# Review by - jitendra dixit
#                                                                  #
# comment : good
#                                                                  #
####################################################################

@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_organisation_assign_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = OrganisationName.objects.filter(name__icontains=q,is_live_org=False).order_by('name')
            else:
                results = OrganisationName.objects.filter(is_live_org=False).order_by('name')
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
            html = render_to_string('admin/admin_organisation/search_organisation_assign.html',
                                    {'tab': 'data', 'crosal': 'doctorbymanage', 'organisation_data_obj': results,
                                     'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        #print e
        raise Http404

####################################################################
# Name - search_lab_admin                                       #
# Owner - Jaydeep verma                                         #
# Review by -
#                                                                  #
# comment :
#                                                                   #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_lab_assign_admin(request):
    try:
        if request.method == 'POST':
            city_list = City.objects.all().order_by('name')
            locality_list = Locality.objects.all().order_by('name')
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Labs.objects.filter(name__icontains=q)
            else:
                results = Labs.objects.all()
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
            html = render_to_string('admin/lab_management/search_admin_lab.html',
                                    {'tab': 'data', 'crosal': 'labbymanage', 'lab': results,
                                     'search_data':q,'city_list':city_list,'locality_list':locality_list})
            return HttpResponse(html)
    except Exception as e:

        raise Http404

####################################################################
# Name - search_lab_by stage and user                              #
# Owner - Jaydeep verma                                            #
# Review by -
#                                                                  #
# comment :                                                        #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_lab_admin_on_stage_user(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Labs.objects.filter(name__icontains=q)
            else:
                results = Labs.objects.all()
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
            html = render_to_string('admin/lab_management/search_lab_by_stage_user.html',
                                    {'tab': 'data', 'crosal': 'labbymanage', 'lab_all_data': results,
                                     'search_data_two':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_doctor_by_users_by_admin                           #
# Owner - Visnu Badal                                              #
# Review by - jitendra dixit
#                                                                  #
# comment : good                                                   #
#                                                                  #
####################################################################

@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_doctor_by_users_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Doctor.objects.filter(current_user_id=q).order_by('name')
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
            html = render_to_string('admin/doctor_management/search_doctor_by_users.html',
                                    {'tab': 'data', 'crosal': 'doctorbymanage', 'doctor_all_data': results,
                                     'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_organisation_by_satages_by_admin                   #
# Owner - Visnu Badal                                              #
# Review by - jitendra dixit
#                                                                  #
# comment : good                                                   #
#                                                                  #
####################################################################

@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_doctor_by_stages_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Doctor.objects.filter(stage_id=q).order_by('name')
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
            html = render_to_string('admin/doctor_management/search_doctor_by_stages_user.html',
                                    {'tab': 'data', 'crosal': 'doctorbymanage', 'doctor_all_data': results,
                                     'stage_no':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404



####################################################################
# Name - search_ambulance_by_users_by_admin                        #
# Owner - Visnu Badal                                              #
# Review by - Nishank
#                                                                  #
# comment : good                                                   #
#                                                                  #
####################################################################

@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_ambulance_by_users_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Ambulance.objects.filter(current_user_id=q).order_by('name')
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
            html = render_to_string('admin/ambulance_management/search_ambulance_by_users.html',
                                    {'tab': 'data', 'crosal': 'ambulancebymanage', 'ambulance_all_data': results,
                                     'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404



####################################################################
# Name - search_organisation_admin                                 #
# Owner - Visnu Badal                                              #
# Review by - jitendra dixit                                       #
#                                                                  #
# comment : good                                                   #
#                                                                  #
####################################################################


@login_required(login_url='/')
@csrf_exempt
def search_organisation_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = OrganisationName.objects.filter(is_live_org=False,name__icontains=q).order_by('name')
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
            html = render_to_string('admin/admin_organisation/search_organisaton_admin.html',
                                    {'tab': 'data', 'crosal': 'organisationbymanage', 'organisation_all_data': results,
                                     'search_data_two':q})
            return HttpResponse(html)
    except Exception as e:
        #print e
        raise Http404


####################################################################
# Name - search_organisation_by_stages_by_admin                    #
# Owner - Visnu Badal                                              #
# Review by - jitendra dixit                                       #
#                                                                  #
# comment : good                                                   #
#                                                                  #
####################################################################

@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_organisation_by_stages_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = OrganisationName.objects.filter(is_live_org=False,stage_id=q).order_by('name')
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
            html = render_to_string('admin/admin_organisation/search_organisation_stages.html',
                                    {'tab': 'data', 'crosal': 'organisationbymanage', 'organisation_all_data': results,
                                     'stage_no':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_organisation_by_users_by_admin                     #
# Owner - Visnu Badal                                              #
# Review by - jitendra dixit
#                                                                  #
# comment : good                                                   #
#                                                                  #
####################################################################


@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_organisation_by_users_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = OrganisationName.objects.filter(is_live_org=False,current_user_id=q).order_by('name')
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
            html = render_to_string('admin/admin_organisation/search_by_user_admin.html',
                                    {'tab': 'data', 'crosal': 'organisationbymanage', 'organisation_all_data': results,
                                     'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_Lab_by_users_by_admin                              #
# Owner - Jaydeep                                                  #
# Review by -
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################


@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_lab_by_users_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Labs.objects.filter(current_user_id=q).order_by('name')
            paginator = Paginator(results, 3)
            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('admin/lab_management/search_by_user_admin.html',
                                    {'tab': 'data', 'crosal': 'labbymanage',
                                     'lab_all_data': results,'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_Lab_by_stages_by_admin                              #
# Owner - Jaydeep  verma                                            #
# Review by -
#                                                                  #
# comment :                                                       #
#                                                                  #
####################################################################


@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_lab_by_stages_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Labs.objects.filter(stage_id=q).order_by('name')
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
            html = render_to_string('admin/lab_management/search_lab_by_stage_user.html',
                                    {'tab': 'data', 'crosal': 'labbymanage', 'lab_all_data': results,
                                     'stage_no':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404



####################################################################
# Name - search_doctor_by_stages_by_publisher                      #
# Owner - Visnu Badal                                              #
# Review by - jitendra dixit
#                                                                  #
# comment : good                                                   #
#                                                                  #
####################################################################

@login_required(login_url='/')
@csrf_exempt
def search_doctor_by_stages_by_publisher(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            category_filter = False
            if q is not None:
                results = Doctor.objects.filter(stage_id=q,current_user_id=request.user.id,is_disable=False).order_by('name')
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
            html = render_to_string('publisher/doctor/search_doctor_by_stage_by_publisher.html',
                                    {'tab': 'publish_doctor_data', 'crosal': 'doctorbymanagebypublisher',
                                     'doctor': results,
                                     'category_filter': category_filter,'stage_id':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_lab_by_stages_by_publisher                         #
# Owner - Visnu Badal                                              #
# Review by - jitendra dixit
#                                                                  #
# comment : good                                                   #
#                                                                  #
####################################################################

@login_required(login_url='/')
@csrf_exempt
def search_lab_by_stages_by_publisher(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            category_filter = False
            if q is not None:
                results = Labs.objects.filter(stage_id=q,current_user_id=request.user.id,is_disable=False ).order_by('name')
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
            html = render_to_string('publisher/lab/search_lab_by_stage_by_publisher.html',
                                    {'tab': 'publish_lab_data', 'crosal': 'labbymanagebypublisher',
                                     'lab': results,
                                     'category_filter': category_filter,'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_question_by_type_admin                             #
# By - Ni    shank                                                 #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_question_by_type_admin(request):
    try:
        if request.method == 'POST':
            cat_list = Category.objects.all()
            q = request.POST['formDATA[q]']
            results = []
            #category_filter = False
            live_docs = Live_Doctor.objects.filter(is_disable=False)
            live_doc_list = []
            for i in live_docs:
                try:
                    Associated_Data = Live_Doctor_Associated_Data.objects.get(doctor_id=i.id)
                except:
                    Associated_Data = None
                if Associated_Data != None:
                    if i.activate == True or Associated_Data.talk_to_doc == True:
                        live_doc_list.append(i)
                    else:
                        pass
                else:
                    if i.activate == True:
                        live_doc_list.append(i)
                    else:
                        pass
            print live_doc_list
            if q is not None:
                if q == '1':
                    results = patienttoaskquestion.objects.filter(doctor_id__isnull=False,free='true').order_by('-createdAt')
                elif q == '2':
                    results = patienttoaskquestion.objects.filter(doctor_id__isnull=True,free='true').order_by('-createdAt')
                else:
                    results =  []
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
            html = render_to_string('admin/questions_management/search_question_by_type_admin.html',
                                    {'tab_listing': 'questions_listing','question_obj': results,
                                     'live_doc_list': live_doc_list,'cat_list':cat_list},request=request)
                                     #'category_filter': category_filter, 'search_data': q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404




#`````
####################################################################
# Name - feedback_by_status_admin                                  #
# By - Ni    shank                                                 #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def feedback_by_status_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            #category_filter = False
            if q is not None:
                if q == '1':
                    results = patienttodoctorfeedback.objects.filter(verified=True)
                elif q == '2':
                    results = patienttodoctorfeedback.objects.filter(verified=False)
                else:
                    results =  []


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
            html = render_to_string('admin/feedback_management/search_feedback_by_status_admin.html',
                                    {'tab_listing': 'feedback_listing','feedback_obj': results,
                                     })
                                     #'category_filter': category_filter, 'search_data': q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404



####################################################################
# Name - search_blood_bank_by_stages_by_publisher                  #
# Addd by Nishank                                                  #
#
#                                                                  #
# comment : good                                                   #
#                                                                  #
####################################################################

@login_required(login_url='/')
@csrf_exempt
def search_blood_bank_by_stages_by_publisher(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            category_filter = False
            if q is not None:
                results = BloodBank.objects.filter(stage_id=q,current_user_id=request.user.id,is_disable=False ).order_by('name')
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
            html = render_to_string('publisher/bloodbank/search_blood_bank_by_stage_by_publisher.html',
                                    {'tab': 'publish_blood_bank_data', 'crosal': 'blood_bankbymanagebypublisher',
                                     'bloodbank': results,
                                     'category_filter': category_filter,'stage_id':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404



####################################################################
# Name - search_ambulance_by_stages_by_publisher                   #
# Addd by Nishank                                                  #
#
#                                                                  #
# comment : good                                                   #
#                                                                  #
####################################################################

@login_required(login_url='/')
@csrf_exempt
def search_ambulance_by_stages_by_publisher(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            category_filter = False
            if q is not None:
                results = Ambulance.objects.filter(stage_id=q,current_user_id=request.user.id,is_disable=False ).order_by('name')
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
            html = render_to_string('publisher/ambulance/search_ambulance_by_stage_by_publisher.html',
                                    {'tab': 'publish_ambulance_data', 'crosal': 'ambulancebymanagebypublisher',
                                     'ambulance': results,
                                     'category_filter': category_filter,
                                      'stage_id':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_pharmacy_by_stages_by_publisher                    #
# Addd by Nishank                                                  #
#
#                                                                  #
# comment : good                                                   #
#                                                                  #
####################################################################

@login_required(login_url='/')
@csrf_exempt
def search_pharmacy_by_stages_by_publisher(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            category_filter = False
            if q is not None:
                results = MedicalPharmacyStore.objects.filter(stage_id=q,current_user_id=request.user.id,is_disable=False ).order_by('name')
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
            html = render_to_string('publisher/pharmacy/search_pharmacy_by_stage_by_publisher.html',
                                    {'tab': 'publish_pharmacy_data', 'crosal': 'pharmacybymanagebypublisher',
                                     'pharmacy': results, 'stage_id':q })
            return HttpResponse(html)
    except Exception as e:

        raise Http404



####################################################################
# Name - search_doctor_by_stages_by_publisher                      #
# Owner - Visnu Badal                                              #
# Review by - jitendra dixit
#                                                                  #
# comment : good                                                   #
#                                                                  #
####################################################################

@login_required(login_url='/')
@csrf_exempt
def search_organisation_by_stages_by_publisher(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            category_filter = False
            if q is not None:
                results = OrganisationName.objects.filter(stage_id=q,current_user_id=request.user.id,is_disable=False).order_by('name')
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
            html = render_to_string('publisher/organisation/search_organisation_by_stage_by_publisher.html',
                                    {'tab': 'publish_organisation_data',
                                     'organisation': results,
                                     'category_filter': category_filter,'stage_id':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

"""Bloodbank search added by Nishank"""


####################################################################
# Name - search_bloodbank_by_users_by_admin                        #
# Owner - Nishank                                                  #
# Review by - jitendra dixit
#                                                                  #
# comment : good                                                   #
#                                                                  #
####################################################################

@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_bloodbank_by_users_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = BloodBank.objects.filter(current_user_id=q).order_by('name')
            paginator = Paginator(results, 4)
            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('admin/bloodbank_management/search_bloodbank_by_users.html',
                                    {'tab_listing': 'bloodbank_listing', 'crosal': 'bloodbankbymanage', 'bloodbank_all_data': results,
                                     'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_bloodbank_admin_on_stage_user(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']

            results = []
            if q is not None:
                results = BloodBank.objects.filter(name__icontains=q)
            else:
                results = BloodBank.objects.all()
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
            html = render_to_string('admin/bloodbank_management/search_bloodbank_by_stage_user.html',
                                    {'tab': 'data', 'crosal': 'bloofbankbymanage', 'bloodbank_all_data': results,
                                     'search_data_two':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_bloodbank_assign_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = BloodBank.objects.filter(name__icontains=q)
            else:
                results = BloodBank.objects.all()
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
            html = render_to_string('admin/bloodbank_management/search_admin_bloodbank.html',
                                    {'tab': 'data', 'crosal': 'labbymanage', 'bloodbank': results,
                                     'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_bloodbank_by_stages_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = BloodBank.objects.filter(stage_id=q).order_by('name')
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
            html = render_to_string('admin/bloodbank_management/search_by_user_admin.html',
                                    {'tab': 'data', 'crosal': 'labbymanage', 'bloodbank_all_data': results,
                                     'stage_no':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404



####################################################################
# Name - search_bloodbank_caller                                   #
# Owner - Nishank                                                  #
# Review by -                                                      #
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################

@login_required(login_url='/')
@csrf_exempt
def search_bloodbank_caller(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = BloodBank.objects.filter(current_user_id=user_id, name__icontains=q,
                                                          is_disable=False).order_by('name')
            elif user_id:
                results = BloodBank.objects.filter(current_user_id=user_id, is_disable=False).order_by(
                    'name')
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
            html = render_to_string('data_management/search_data/search_bloodbank.html',
                                    {'bloodbank': results})
            return HttpResponse(html)
    except Exception as e:
        raise Http404




"""Ambulance search added by Nishank"""

@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_ambulance_admin_on_stage_user(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Ambulance.objects.filter(name__icontains=q)
            else:
                results = Ambulance.objects.all()
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
            html = render_to_string('admin/ambulance_management/search_ambulance_by_stage_user.html',
                                    {'tab': 'data', 'crosal': 'labbymanage', 'ambulance_all_data': results,
                                     'search_data_two':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_ambulance_assign_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Ambulance.objects.filter(name__icontains=q)
            else:
                results = Ambulance.objects.all()
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
            html = render_to_string('admin/ambulance_management/search_admin_ambulance.html',
                                    {'tab': 'data', 'crosal': 'labbymanage', 'ambulance': results,
                                     'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404




@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_ambulance_by_stages_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Ambulance.objects.filter(stage_id=q).order_by('name')
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
            html = render_to_string('admin/ambulance_management/search_by_user_admin.html',
                                    {'tab': 'data', 'crosal': 'labbymanage', 'ambulance_all_data': results,
                                     'stage_no':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_ambulance_caller                                   #
# Owner - Nishank                                                  #
# Review by -                                                      #
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################

@login_required(login_url='/')
@csrf_exempt
def search_ambulance_caller(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = Ambulance.objects.filter(current_user_id=user_id, name__icontains=q,
                                                          is_disable=False).order_by('name')
            elif user_id:
                results = Ambulance.objects.filter(current_user_id=user_id, is_disable=False).order_by(
                    'name')
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
            html = render_to_string('data_management/search_data/search_ambulance.html',
                                    {'ambulance': results})
            return HttpResponse(html)
    except Exception as e:
        #print e
        raise Http404

""" Pharmacy Functions Start"""

####################################################################
# Name - search_pharmacy_by_users_by_admin                         #
# Owner - Nishank                                                  #
# Review by -
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################


@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_pharmacy_by_users_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = MedicalPharmacyStore.objects.filter(current_user_id=q).order_by('name')
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
            html = render_to_string('admin/pharmacy_management/search_by_user_admin.html',
                                    {'tab': 'data', 'crosal': 'pharmacybymanage',
                                     'pharmacy_all_data': results,'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_pharmacy_by stage and user                         #
# Owner - Jaydeep verma                                            #
# Review by -
#                                                                  #
# comment :                                                        #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_pharmacy_admin_on_stage_user(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = MedicalPharmacyStore.objects.filter(name__icontains=q)
            else:
                results = MedicalPharmacyStore.objects.all()
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
            html = render_to_string('admin/pharmacy_management/search_pharmacy_by_stage_user.html',
                                    {'tab': 'data', 'crosal': 'pharmacybymanage', 'pharmacy_all_data': results,
                                     'search_data_two':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_Pharmacy_by_stages_by_admin                        #
# Owner - Jaydeep  verma                                           #
# Review by -
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################


@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_pharmacy_by_stages_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = MedicalPharmacyStore.objects.filter(stage_id=q).order_by('name')
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
            html = render_to_string('admin/pharmacy_management/search_pharmacy_by_stage_user.html',
                                    {'tab': 'data', 'crosal': 'pharmacybymanage', 'pharmacy_all_data': results,
                                     'stage_no':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_pharmacy_admin                                       #
# Owner - Jaydeep verma                                         #
# Review by -
#                                                                  #
# comment :
#                                                                   #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_pharmacy_assign_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = MedicalPharmacyStore.objects.filter(name__icontains=q)
            else:
                results = MedicalPharmacyStore.objects.all()
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
            html = render_to_string('admin/pharmacy_management/search_admin_pharmacy.html',
                                    {'tab': 'data', 'crosal': 'pharmacybymanage', 'pharmacy': results,
                                     'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_pharmacy_caller                                    #
# Owner - Jaydeep                                                  #
# Review by -                                                      #
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################

@login_required(login_url='/')
@csrf_exempt
def search_pharmacy_caller(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = MedicalPharmacyStore.objects.filter(current_user_id=user_id, name__icontains=q,
                                                  is_disable=False).order_by('name')
            elif user_id:
                results = MedicalPharmacyStore.objects.filter(current_user_id=user_id, is_disable=False).order_by(
                        'name')
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
            html = render_to_string('data_management/search_data/search_pharmacy.html',
                                    {'pharmacy': results})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_disease_by stage and user                         #
# Owner - Jaydeep verma                                            #
# Review by -
#                                                                  #
# comment :                                                        #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_disease_admin_on_stage_user(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Disease.objects.filter(tag_string__icontains=q).order_by('tag_string')
            else:
                results = Disease.objects.all()
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
            html = render_to_string('admin/disease_management/search_disease_by_stage_user.html',
                                    {'tab': 'disease_symptom_drug_data', 'crosal': 'diseasebymanage', 'disease_all_data': results,
                                    'search_data_two':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_disease_by_stages_by_admin                         #
# Owner - Jaydeep  verma                                           #
# Review by -
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################


@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_disease_by_stages_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                #results = Disease.objects.filter(stage_id=q)
                results = Disease.objects.filter(stage_id=q)
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
            html = render_to_string('admin/disease_management/search_disease_by_stage_user.html',
                                    {'tab': 'disease_symptom_drug_data', 'crosal': 'diseasebymanage', 'disease_all_data': results,
                                     'stage_no':q})
            return HttpResponse(html)
    except Exception as e:

        raise Http404

####################################################################
# Name - search_disease_admin                                       #
# Owner - Jaydeep verma                                             #
# Review by -
#                                                                  #
# comment :
#                                                                   #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_disease_assign_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Disease.objects.filter(tag_string__icontains=q)
            else:
                results = Disease.objects.all()
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
            html = render_to_string('admin/disease_management/search_admin_disease.html',
                                    {'tab': 'disease_symptom_drug_data', 'crosal': 'diseasebymanage', 'disease_all_data': results,
                                     'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404



####################################################################
# Name - search_disease_caller                                     #
# Owner - Jaydeep                                                  #
# Review by -                                                      #
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################

@login_required(login_url='/')
@csrf_exempt
def search_disease_caller(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = Disease.objects.filter(current_user_id=user_id, topic_title__icontains=q,
                                                  is_disable=False).order_by('topic_title')
            elif user_id:
                results = Disease.objects.filter(current_user_id=user_id, is_disable=False).order_by(
                        'name')
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
            html = render_to_string('data_management/search_data/search_disease.html',
                                    {'disease': results})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_disease_by_users_by_admin                          #
# Owner - Nishank                                                  #
# Review by -
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################


@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_disease_by_users_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Disease.objects.filter(current_user_id=q).order_by('tag_string')
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
            html = render_to_string('admin/disease_management/search_by_user_admin.html',
                                    {'tab': 'data', 'crosal': 'diseasebymanage',
                                     'disease_all_data': results,'search_data':q})
            return HttpResponse(html)
    except Exception as e:

        raise Http404

"""Drug functions"""


####################################################################
# Name - search_drug_by_users_by_admin                             #
# Owner - Nishank                                                  #
# Review by -
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################


@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_drug_by_users_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Drug.objects.filter(current_user_id=q).order_by('name')
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
            html = render_to_string('admin/drug_management/search_by_user_admin.html',
                                    {'tab': 'data', 'crosal': 'drugbymanage',
                                     'drug_all_data': results,'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_drug_by stage and user                             #
# Owner - Jaydeep verma                                            #
# Review by -
#                                                                  #
# comment :                                                        #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_drug_admin_on_stage_user(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Drug.objects.filter(name__icontains=q).order_by('name')
            else:
                results = Drug.objects.all().order_by('name')
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
            html = render_to_string('admin/drug_management/search_drug_by_stage_user.html',
                                    {'tab': 'drug_symptom_drug_data', 'crosal': 'drugbymanage', 'drug_all_data': results,
                                     'search_data_two':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_drug_by_stages_by_admin                            #
# Owner - Jaydeep  verma                                           #
# Review by -
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################


@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_drug_by_stages_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Drug.objects.filter(stage_id=q).order_by('name')
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
            html = render_to_string('admin/drug_management/search_by_user_admin.html',
                                    {'tab': 'disease_symptom_drug_data', 'crosal': 'drugbymanage', 'drug_all_data': results,
                                     'stage_no':q})
            return HttpResponse(html)
    except Exception as e:

        raise Http404

####################################################################
# Name - search_drug_caller                                        #
# Owner - Jaydeep                                                  #
# Review by -                                                      #
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################

@login_required(login_url='/')
@csrf_exempt
def search_drug_caller(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = Drug.objects.filter(current_user_id=user_id, name__icontains=q,
                                                  is_disable=False).order_by('name')
            elif user_id:
                results = Drug.objects.filter(current_user_id=user_id, is_disable=False).order_by(
                        'name')
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
            html = render_to_string('data_management/search_data/search_drug.html',
                                    {'drug': results})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_drug_admin                                         #
# Owner - Nishank                                                  #
# Review by -
#                                                                  #
# comment :
#                                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_drug_assign_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Drug.objects.filter(name__icontains=q)
            else:
                results = Drug.objects.all()
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
            html = render_to_string('admin/drug_management/search_admin_drug.html',
                                    {'tab': 'drug_symptom_drug_data', 'crosal': 'drugbymanage', 'drug_all_data': results,
                                     'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404



"""Symptom functions"""

####################################################################
# Name - search_symptoms_by stage and user                         #
# Owner - Nishank                                                  #
# Review by -
#                                                                  #
# comment :                                                        #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_symptoms_admin_on_stage_user(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Symptoms.objects.filter(topic_title__icontains=q).order_by('topic_title')
            else:
                results = Symptoms.objects.all()
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
            html = render_to_string('admin/symptoms_management/search_symptoms_by_stage_user.html',
                                    {'tab': 'disease_symptom_drug_data', 'crosal': 'symptomsbymanage', 'symptoms_all_data': results,
                                     'search_data': q,'search_data_two':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_symptoms_by_stages_by_admin                        #
# Owner - Jaydeep  verma                                           #
# Review by -
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################


@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_symptoms_by_stages_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Symptoms.objects.filter(stage_id=q)
            paginator = Paginator(results,100)
            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('admin/symptoms_management/search_by_user_admin.html',
                                    {'tab': 'symptoms_symptom_drug_data', 'crosal': 'symptomsbymanage', 'symptoms_all_data': results,
                                     'stage_no':q})
            return HttpResponse(html)
    except Exception as e:

        raise Http404

####################################################################
# Name - search_symptoms_admin                                      #
# Owner - Jaydeep verma                                             #
# Review by -
#                                                                   #
# comment :
#                                                                   #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_symptoms_assign_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Symptoms.objects.filter(topic_title__icontains=q)
            else:
                results = Symptoms.objects.all()
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
            html = render_to_string('admin/symptoms_management/search_admin_symptoms.html',
                                    {'tab': 'disease_symptom_drug_data', 'crosal': 'symptomsbymanage', 'symptoms_all_data': results,
                                     'search_data':q})
            return HttpResponse(html)
    except Exception as e:

        raise Http404

####################################################################
# Name - search_symptoms_caller                                    #
# Owner - Nishank                                                  #
# Review by -                                                      #
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################

@login_required(login_url='/')
@csrf_exempt
def search_symptoms_caller(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = Symptoms.objects.filter(current_user_id=user_id, topic_title__icontains=q,
                                                  is_disable=False)
            elif user_id:
                results = Symptoms.objects.filter(current_user_id=user_id, is_disable=False)
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
            html = render_to_string('data_management/search_data/search_symptoms.html',
                                    {'symptoms': results})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name: search_disease_by_stages_by_publisher                      #
#Added by Nishank                                                  #
#                                                                  #
####################################################################


@login_required(login_url='/')
@csrf_exempt
def search_disease_by_stages_by_publisher(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            category_filter = False
            if q is not None:
                results = Disease.objects.filter(stage_id=q,current_user_id=request.user.id,is_disable=False ).order_by('topic_title')
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
            html = render_to_string('publisher/disease/search_disease_by_stage_by_publisher.html',
                                    {'tab': 'publish_disease_data', 'crosal': 'diseasebymanagebypublisher',
                                     'disease': results,
                                     'category_filter': category_filter})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name: search_symptoms_by_stages_by_publisher                     #
#Added by Nishank                                                  #
#                                                                  #
####################################################################


@login_required(login_url='/')
@csrf_exempt
def search_symptoms_by_stages_by_publisher(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            category_filter = False
            if q is not None:
                results = Symptoms.objects.filter(stage_id=q,current_user_id=request.user.id,is_disable=False ).order_by('topic_title')
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
            html = render_to_string('publisher/symptoms/search_symptoms_by_stage_by_publisher.html',
                                    {'tab': 'publish_symptoms_data', 'crosal': 'symptomsbymanagebypublisher',
                                     'symptoms': results,
                                     'category_filter': category_filter})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


    ####################################################################
# Name: search_drug_by_stages_by_publisher                         #
#Added by Nishank                                                  #
#                                                                  #
####################################################################


@login_required(login_url='/')
@csrf_exempt
def search_drug_by_stages_by_publisher(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            category_filter = False
            if q is not None:
                results = Drug.objects.filter(stage_id=q,current_user_id=request.user.id,is_disable=False ).order_by('name')
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
            html = render_to_string('publisher/drug/search_drug_by_stage_by_publisher.html',
                                    {'tab': 'publish_drug_data', 'crosal': 'drugbymanagebypublisher',
                                     'drug': results,
                                     'category_filter': category_filter})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_symptoms_by_users_by_admin                          #
# Owner - Nishank                                                  #
# Review by -
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################


@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_symptoms_by_users_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Symptoms.objects.filter(current_user_id=q).order_by('topic_title')
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
            html = render_to_string('admin/symptoms_management/search_by_user_admin.html',
                                    {'tab': 'data', 'crosal': 'symptomsbymanage',
                                     'symptoms_all_data': results,'search_data':q})
            return HttpResponse(html)
    except Exception as e:

        raise Http404

####################################################################
# Name - search_global_caller                                      #
# Owner - Nishank                                                  #
# Review by -                                                      #
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################

@login_required(login_url='/')
@csrf_exempt
def search_global_caller(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = NewsFeed.objects.filter(current_user_id=user_id, topic_title__icontains=q,
                                                  activation_status=True,news_type=1).order_by('topic_title')
            elif user_id:
                results = NewsFeed.objects.filter(current_user_id=user_id,
                                                  activation_status=True,news_type=1).order_by('topic_title')
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
            html = render_to_string('data_management/search_data/search_global.html',
                                    {'global_news': results})
            return HttpResponse(html)
    except Exception as e:
        #print e
        raise Http404

####################################################################
# Name - search_health_caller                                      #
# Owner - Nishank                                                  #
# Review by -                                                      #
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_health_caller(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = NewsFeed.objects.filter(current_user_id=user_id, topic_title__icontains=q,
                                                  activation_status=True, news_type=3).order_by('topic_title')
            elif user_id:
                results = NewsFeed.objects.filter(current_user_id=user_id,
                                                  activation_status=True, news_type=3).order_by('topic_title')
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
            html = render_to_string('data_management/search_data/search_health.html',
                                    {'health_news': results})
            return HttpResponse(html)
    except Exception as e:
        #print e
        raise Http404


####################################################################
# Name - search_wellness_caller                                    #
# Owner - Nishank                                                  #
# Review by -                                                      #
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################

@login_required(login_url='/')
@csrf_exempt
def search_wellness_caller(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = NewsFeed.objects.filter(current_user_id=user_id, topic_title__icontains=q,
                                                  activation_status=True,news_type=2).order_by('topic_title')
            elif user_id:
                results = NewsFeed.objects.filter(current_user_id=user_id,
                                                  activation_status=True,news_type=2).order_by('topic_title')
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
            html = render_to_string('data_management/search_data/search_wellness.html',
                                    {'wellness_news': results})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_home_plan_caller                                   #
# Owner - Nishank                                                  #
# Review by -                                                      #
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################

@login_required(login_url='/')
@csrf_exempt
def search_home_plan_caller(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = ServicePlan.objects.filter(current_user_id=user_id, plan_name__icontains=q,
                                                  activation_status=True,is_home_service=True).order_by('plan_name')
            elif user_id:
                results = ServicePlan.objects.filter(current_user_id=user_id,
                                                  activation_status=True,is_home_service=True).order_by('plan_name')
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
            html = render_to_string('data_management/search_data/search_home_plan.html',
                                    {'plan_list': results})
            return HttpResponse(html)
    except Exception as e:
        #print e
        raise Http404

####################################################################
# Name - search_life_plan_caller                                   #
# Owner - Nishank                                                  #
# Review by -                                                      #
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################

@login_required(login_url='/')
@csrf_exempt
def search_life_plan_caller(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = ServicePlan.objects.filter(current_user_id=user_id, plan_name__icontains=q,
                                                  activation_status=True,is_life_service=True).order_by('plan_name')
            elif user_id:
                results = ServicePlan.objects.filter(current_user_id=user_id,
                                                  activation_status=True,is_life_service=True).order_by('plan_name')
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
            html = render_to_string('data_management/search_data/search_life_plan.html',
                                    {'plan_list': results})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_enterprise_plan_caller                             #
# Owner - Nishank                                                  #
# Review by -                                                      #
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################

@login_required(login_url='/')
@csrf_exempt
def search_enterprise_plan_caller(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = ServicePlan.objects.filter(current_user_id=user_id, plan_name__icontains=q,
                                                  activation_status=True,is_enterprise_service=True).order_by('plan_name')
            elif user_id:
                results = ServicePlan.objects.filter(current_user_id=user_id,
                                                  activation_status=True,is_enterprise_service=True).order_by('plan_name')
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
            html = render_to_string('data_management/search_data/search_enterprise_plan.html',
                                    {'plan_list': results})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_serviceoffered_by_category_admin                   #
# By - Nishank                                                     #
#                                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_serviceoffered_by_category_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            category_obj = Category.objects.all().order_by('name')
            if q is not None:
                results = Service_Offred.objects.filter(category_id=q).order_by('name')

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
            html = render_to_string('admin/master_data_management/search_serviceoffered_by_category_admin.html',
                                    {'tab': 'data', 'crosal': 'serviceofferedbymanage', 'service_offered_obj': results,
                                     'search_data':q,'category_obj':category_obj})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_speciality_by_category_admin                       #
# By - Nishank                                                     #
#
#                                                                  #
#                                                                  #
#                                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_speciality_by_category_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Speciality.objects.filter(category_id=q).order_by('name')
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
            html = render_to_string('admin/master_data_management/search_speciality_by_category_admin.html',
                                    {'tab': 'data', 'crosal': 'specialitybymanage', 'speciality_obj': results,
                                     'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_user_by_name_admin                                 #
# By - Nishank                                                     #
#
#                                                                  #
#                                                                  #
#                                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_user_by_name_admin(request):
    try:
        caller_user_data = None
        reviewer_user_data= None
        publisher_user_data = None
        news_user_data = None
        service_user_data = None
        admin_user_data = None

        umo = results = None
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            q2 = request.POST['formDATA[q2]']
            results = []
            if q is not None  and  q2 is not None:
                if q2 == 'caller':
                    umo = UserManagement.objects.filter(is_caller=True).values('user_id')
                    results = User.objects.filter(username__icontains=q,id__in=umo).order_by('username')

                    paginator = Paginator(results, 10)
                    page = request.GET.get('page')
                    try:
                        results = paginator.page(page)
                    except PageNotAnInteger:
                        # If page is not an integer, deliver first page.
                        results = paginator.page(1)
                    except EmptyPage:
                        # If page is out of range (e.g. 9999), deliver last page of results.
                        results = paginator.page(paginator.num_pages)
                    caller_user_data = results
                    html = render_to_string('admin/user_table_search.html',
                                            {'tab': 'data', 'crosal': 'userbybymanage','caller_user_data':caller_user_data,'reviewer_user_data':reviewer_user_data,
                                            'publisher_user_data':publisher_user_data, 'news_user_data':news_user_data,'service_user_data':service_user_data,
                                            'search_data':q,'user_type':q2,'admin_user_data':admin_user_data})
                    return HttpResponse(html)


                elif q2 == 'reviewer':
                    umo = UserManagement.objects.filter(is_reviewer=True).values('user_id')
                    results = User.objects.filter(username__icontains=q,id__in=umo).order_by('username')

                    paginator = Paginator(results, 10)
                    page = request.GET.get('page')
                    try:
                        results = paginator.page(page)
                    except PageNotAnInteger:
                        # If page is not an integer, deliver first page.
                        results = paginator.page(1)
                    except EmptyPage:
                        # If page is out of range (e.g. 9999), deliver last page of results.
                        results = paginator.page(paginator.num_pages)
                    reviewer_user_data = results
                    #print reviewer_user_data
                    for i in reviewer_user_data:
                        #print i.username,i.id
                        pass
                    html = render_to_string('admin/user_table_search.html',
                                            {'tab': 'data', 'crosal': 'userbybymanage','caller_user_data':caller_user_data,'reviewer_user_data':reviewer_user_data,
                                            'publisher_user_data':publisher_user_data, 'news_user_data':news_user_data,'service_user_data':service_user_data,
                                            'search_data':q,'user_type':q2,'admin_user_data':admin_user_data})
                    return HttpResponse(html)

                elif q2 == 'publisher':
                    umo = UserManagement.objects.filter(is_publisher=True).values('user_id')
                    results = User.objects.filter(username__icontains=q,id__in=umo).order_by('username')

                    paginator = Paginator(results, 10)
                    page = request.GET.get('page')
                    try:
                        results = paginator.page(page)
                    except PageNotAnInteger:
                        # If page is not an integer, deliver first page.
                        results = paginator.page(1)
                    except EmptyPage:
                        # If page is out of range (e.g. 9999), deliver last page of results.
                        results = paginator.page(paginator.num_pages)
                    publisher_user_data = results
                    html = render_to_string('admin/user_table_search.html',
                                            {'tab': 'data', 'crosal': 'userbybymanage','caller_user_data':caller_user_data,'reviewer_user_data':reviewer_user_data,
                                            'publisher_user_data':publisher_user_data, 'news_user_data':news_user_data,'service_user_data':service_user_data,
                                            'search_data':q,'user_type':q2,'admin_user_data':admin_user_data})
                    return HttpResponse(html)

                elif q2 == 'admin':
                    results = User.objects.filter(username__icontains=q, is_superuser=True).order_by('username')
                    admin_user_data = results
                    paginator = Paginator(results, 10)
                    page = request.GET.get('page')
                    try:
                        results = paginator.page(page)
                    except PageNotAnInteger:
                        # If page is not an integer, deliver first page.
                        results = paginator.page(1)
                    except EmptyPage:
                        # If page is out of range (e.g. 9999), deliver last page of results.
                        results = paginator.page(paginator.num_pages)
                    admin_user_data = results
                    html = render_to_string('admin/user_table_search.html',
                                            {'tab': 'data', 'crosal': 'userbybymanage','caller_user_data':caller_user_data,'reviewer_user_data':reviewer_user_data,
                                            'publisher_user_data':publisher_user_data, 'news_user_data':news_user_data,'service_user_data':service_user_data,
                                            'admin_user_data':admin_user_data,'search_data':q,'user_type':q2,'admin_user_data':admin_user_data})
                    return HttpResponse(html)


                elif q2 == 'service':
                    umo = UserManagement.objects.filter(is_service_plan=True).values('user_id')
                    results = User.objects.filter(username__icontains=q,id__in=umo).order_by('username')

                    paginator = Paginator(results, 10)
                    page = request.GET.get('page')
                    try:
                        results = paginator.page(page)
                    except PageNotAnInteger:
                        # If page is not an integer, deliver first page.
                        results = paginator.page(1)
                    except EmptyPage:
                        # If page is out of range (e.g. 9999), deliver last page of results.
                        results = paginator.page(paginator.num_pages)
                    service_user_data = results
                    html = render_to_string('admin/user_table_search.html',
                                            {'tab': 'data', 'crosal': 'userbybymanage','caller_user_data':caller_user_data,'reviewer_user_data':reviewer_user_data,
                                            'publisher_user_data':publisher_user_data, 'news_user_data':news_user_data,'service_user_data':service_user_data,
                                            'search_data':q,'user_type':q2,'admin_user_data':admin_user_data})
                    return HttpResponse(html)

                elif q2 == 'news':
                    umo = UserManagement.objects.filter(is_news=True).values('user_id')
                    results = User.objects.filter(username__icontains=q,id__in=umo).order_by('username')

                    paginator = Paginator(results, 10)
                    page = request.GET.get('page')
                    try:
                        results = paginator.page(page)
                    except PageNotAnInteger:
                        # If page is not an integer, deliver first page.
                        results = paginator.page(1)
                    except EmptyPage:
                        # If page is out of range (e.g. 9999), deliver last page of results.
                        results = paginator.page(paginator.num_pages)
                    news_user_data = results
                    html = render_to_string('admin/user_table_search.html',
                                            {'tab': 'data', 'crosal': 'userbybymanage','caller_user_data':caller_user_data,'reviewer_user_data':reviewer_user_data,
                                            'publisher_user_data':publisher_user_data, 'news_user_data':news_user_data,'service_user_data':service_user_data,
                                            'search_data':q,'user_type':q2,'admin_user_data':admin_user_data})
                    return HttpResponse(html)

                else:
                    messages.error('Something Bad Happened')
                    return redirect(request.META.HTTP_REFERER)

    except Exception as e:
        #print e
        raise Http404


####################################################################
# Name - search_Locality_by_name_admin                             #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_locality_by_name_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            if q is not None :
                try :
                    results = Locality.objects.filter(name__icontains=q).order_by('id')
                except:
                    results= None
                if results :
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

                    html = render_to_string('admin/master_data_management/locality_search_by_name.html',
                                            {'tab': 'data', 'crosal': 'localitybymanage',
                                            'search_data':q,'locality_obj':results})
                    return HttpResponse(html)

                html = "<div class=table-responsive table_modify_for_all>No Locality Found</div>"
                return HttpResponse(html)

            messages.error(request,"Invalid data")
            return redirect(request.META.HTTP_REFERER)

    except:

        messages.error(request,"Method not allowed")
        return redirect(request.META.HTTP_REFERER)


####################################################################
# Name - search_ZoneLocation_by_name_admin                         #
# By - Nishank                                                     #
#
#                                                                  #
#                                                                  #
#                                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_zonelocation_by_name_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            if q is not None :
                try :
                    results = ZoneLocation.objects.filter(name__icontains=q).order_by('name')
                except:
                    results= None
                if results :
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

                    html = render_to_string('admin/master_data_management/zonelocation_search_by_name.html',
                                            {'tab': 'data', 'crosal': 'localitybymanage',
                                            'search_data':q,'zone_location_obj':results})
                    return HttpResponse(html)

                html = "<div class=table-responsive table_modify_for_all>No Zone Location Found</div>"
                return HttpResponse(html)

            messages.error(request,"Invalid data")
            return redirect(request.META.HTTP_REFERER)

    except:

        messages.error(request,"Method not allowed")
        return redirect(request.META.HTTP_REFERER)

####################################################################
# Name - search_rehab_caller                                       #
# BY :  Nishank                                                    #
# Review by -                                                      #
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################

@login_required(login_url='/')
@csrf_exempt
def search_rehab_caller(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:

                if request.user.is_superuser :
                    results = RehabCenter.objects.filter(current_user_id=user_id, clinic_name__icontains=q,
                                                  ).order_by('clinic_name')
                else:
                    results = RehabCenter.objects.filter(current_user_id=user_id, clinic_name__icontains=q,
                                                         is_disable=False).order_by('clinic_name')
            elif user_id:
                if request.user.is_superuser:
                    results = RehabCenter.objects.filter(current_user_id=user_id).order_by(
                        'clinic_name')
                else:
                    results = RehabCenter.objects.filter(current_user_id=user_id, is_disable=False).order_by(
                        'clinic_name')

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
            html = render_to_string('data_management/search_data/search_rehab.html',
                                    {'rehab': results})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_rehab_by_stages_by_publisher                       #
# Owner - Visnu Badal                                              #
# Review by - jitendra dixit
#                                                                  #
# comment : good                                                   #
#                                                                  #
####################################################################

@login_required(login_url='/')
@csrf_exempt
def search_rehab_by_stages_by_publisher(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            category_filter = False
            if q is not None:
                results = RehabCenter.objects.filter(stage_id=q,current_user_id=request.user.id,is_disable=False ).order_by('clinic_name')
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
            html = render_to_string('publisher/rehab/search_rehab_by_stage_by_publisher.html',
                                    {'tab': 'publish_rehab_data', 'crosal': 'rehab_bymanagebypublisher',
                                     'rehab': results,
                                     'category_filter': category_filter,'stage_id':q})
            return HttpResponse(html)
    except Exception as e:
        #print e
        raise Http404
####################################################################
# Name - search_rehab_by_users_by_admin                            #
# BY : NISHANK                                                     #
# Review by -
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################


@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_rehab_by_users_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = RehabCenter.objects.filter(current_user_id=q).order_by('clinic_name')
            paginator = Paginator(results, 3)
            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('admin/rehab_management/search_by_user_admin.html',
                                    {'tab': 'data', 'crosal': 'rehabbymanage',
                                     'rehab_all_data': results,'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404



####################################################################
# Name - search_rehab_by stage and user                            #
# BY : Nishank                                                     #
# Review by -
#                                                                  #
# comment :                                                        #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_rehab_admin_on_stage_user(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = RehabCenter.objects.filter(name__icontains=q).order_by('clinic_name')
            else:
                results = RehabCenter.objects.all().order_by('clinic_name')
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
            html = render_to_string('admin/rehab_management/search_rehab_by_stage_user.html',
                                    {'tab': 'data', 'crosal': 'rehabbymanage', 'rehab_all_data': results,
                                     'search_data_two':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_Rehab_by_stages_by_admin                           #
# Owner - Jaydeep  verma                                           #
# Review by -
#                                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_rehab_by_stages_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = RehabCenter.objects.filter(stage_id=q).order_by('clinic_name')
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
            html = render_to_string('admin/rehab_management/search_rehab_by_stage_user.html',
                                    {'tab': 'data', 'crosal': 'rehabbymanage', 'rehab_all_data': results,
                                     'stage_no':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404
###################################################################
# Name - search_rehab_admin                                       #
# Owner - Jaydeep verma                                           #
# Review by -
#                                                                 #
# comment :
#                                                                 #
###################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_rehab_assign_admin(request):
    try:
        if request.method == 'POST':
            city_list = City.objects.all().order_by('name')
            locality_list = Locality.objects.all().order_by('name')
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = RehabCenter.objects.filter(clinic_name__icontains=q).order_by('clinic_name')
            else:
                results = RehabCenter.objects.all().order_by('clinic_name')
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
            html = render_to_string('admin/rehab_management/search_admin_rehab.html',
                                    {'tab': 'data', 'crosal': 'rehabbymanage', 'rehab': results,
                                     'search_data':q,'city_list':city_list,'locality_list':locality_list})
            return HttpResponse(html)
    except Exception as e:

        raise Http404


####################################################################
# Name - search_ambulance_service_by_name_admin                    #
# By - Nishank                                                     #
#
#                                                                  #
#                                                                  #
#                                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_ambulance_service_by_name_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            if q is not None :
                try :
                    results = AmbulanceServices.objects.filter(name__icontains=q).order_by('name')
                except:
                    results= None
                if results :
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

                    html = render_to_string('admin/master_data_management/ambulance_service_search_by_name.html',
                                            {'tab': 'data', 'crosal': 'ambulanceservicebymanage',
                                            'search_data':q,'ambulance_service_obj':results})
                    return HttpResponse(html)

                html = "<div class=table-responsive table_modify_for_all>No Ambulance Service Found</div>"
                return HttpResponse(html)

            messages.error(request,"Invalid data")
            return redirect(request.META.HTTP_REFERER)

    except:

        messages.error(request,"Method not allowed")
        return redirect(request.META.HTTP_REFERER)




####################################################################
# Name - search_ambulance_type_by_name_admin                       #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_ambulance_type_by_name_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            if q is not None :
                try :
                    results = Ambulance_type_master.objects.filter(name__icontains=q).order_by('name')
                except:
                    results= None
                if results :
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

                    html = render_to_string('admin/master_data_management/ambulance_type_search_by_name.html',
                                            {'tab': 'data', 'crosal': 'ambulancetypebymanage',
                                            'search_data':q,'ambulance_type_obj':results})
                    return HttpResponse(html)

                html = "<div class=table-responsive table_modify_for_all>No Ambulance Service Found</div>"
                return HttpResponse(html)

            messages.error(request,"Invalid data")
            return redirect(request.META.HTTP_REFERER)

    except:

        messages.error(request,"Method not allowed")
        return redirect(request.META.HTTP_REFERER)

####################################################################
# Name - search_nurse_bureau_caller                                #
# BY :  Nishank                                                    #
# Review by -                                                      #
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_nurse_bureau_caller(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:

                if request.user.is_superuser :
                    results = Nurse_Bureau.objects.filter(current_user_id=user_id, name__icontains=q,
                                                  ).order_by('name')
                else:
                    results = Nurse_Bureau.objects.filter(current_user_id=user_id, name__icontains=q,
                                                         is_disable=False).order_by('name')
            elif user_id:
                if request.user.is_superuser:
                    results = Nurse_Bureau.objects.filter(current_user_id=user_id).order_by(
                        'name')
                else:
                    results = Nurse_Bureau.objects.filter(current_user_id=user_id, is_disable=False).order_by(
                        'name')

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
            html = render_to_string('data_management/search_data/search_nurse_bureau.html',
                                    {'nurse_bureau': results})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_nurse_bureau_by_stages_by_publisher                #
# Owner -                                                          #
# Review by -
#                                                                  #
# comment : good                                                   #
#                                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_nurse_bureau_by_stages_by_publisher(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            category_filter = False
            if q is not None:
                results = Nurse_Bureau.objects.filter(stage_id=q,current_user_id=request.user.id,is_disable=False ).order_by('name')
            else:
                results = []
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
            html = render_to_string('publisher/nurse_bureau/search_nurse_bureau_by_stage_by_publisher.html',
                                    {'tab': 'publish_nurse_bureau_data', 'crosal': 'nurse_bureau_bymanagebypublisher',
                                     'nurse_bureau': results,
                                     'category_filter': category_filter,'stage_id':q})
            return HttpResponse(html)
    except Exception as e:
        #print e
        raise Http404


####################################################################
# Name - search_nurse_bureau_by_users_by_admin                     #
# BY : NISHANK                                                     #
# Review by -
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_nurse_bureau_by_users_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Nurse_Bureau.objects.filter(current_user_id=q).order_by('name')
            paginator = Paginator(results,100)
            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('admin/nurse_bureau_management/search_by_user_admin.html',
                                    {'tab': 'data', 'crosal': 'nurse_bureaubymanage',
                                     'nurse_bureau_all_data': results,'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_nurse_bureau_by stage and user                     #
# BY : Nishank                                                     #
# Review by -
#                                                                  #
# comment :                                                        #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_nurse_bureau_admin_on_stage_user(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Nurse_Bureau.objects.filter(name__icontains=q).order_by('name')
            else:
                results = Nurse_Bureau.objects.all().order_by('name')
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
            html = render_to_string('admin/nurse_bureau_management/search_nurse_bureau_by_stage_user.html',
                                    {'tab': 'data', 'crosal': 'nurse_bureaubymanage', 'nurse_bureau_all_data': results,
                                     'search_data_two':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_Nurse_Bureau_by_stages_by_admin                    #
# Owner - Jaydeep  verma                                           #
# Review by -
#                                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_nurse_bureau_by_stages_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Nurse_Bureau.objects.filter(stage_id=q).order_by('name')
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
            html = render_to_string('admin/nurse_bureau_management/search_nurse_bureau_by_stage_user.html',
                                    {'tab': 'data', 'crosal': 'nurse_bureaubymanage', 'nurse_bureau_all_data': results,
                                     'stage_no':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


###################################################################
# Name - search_nurse_bureau_admin                                #
# Owner - Jaydeep verma                                           #
# Review by -
#                                                                 #
# comment :
#                                                                 #
###################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_nurse_bureau_assign_admin(request):
    try:
        if request.method == 'POST':
            city_list = City.objects.all().order_by('name')
            locality_list = Locality.objects.all().order_by('name')
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Nurse_Bureau.objects.filter(name__icontains=q).order_by('name')
            else:
                results = Nurse_Bureau.objects.all().order_by('name')
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
            html = render_to_string('admin/nurse_bureau_management/search_admin_nurse_bureau.html',
                                    {'tab': 'data', 'crosal': 'nurse_bureaubymanage', 'nurse_bureau': results,
                                     'search_data':q,'city_list':city_list,'locality_list':locality_list})
            return HttpResponse(html)
    except Exception as e:

        raise Http404



####################################################################
# Name - search_dietitian_caller                                   #
# BY :  Nishank                                                    #
# Review by -                                                      #
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_dietitian_caller(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:

                if request.user.is_superuser :
                    results = Dietitian.objects.filter(current_user_id=user_id, name__icontains=q,
                                                  ).order_by('name')
                else:
                    results = Dietitian.objects.filter(current_user_id=user_id, name__icontains=q,
                                                         is_disable=False).order_by('name')
            elif user_id:
                if request.user.is_superuser:
                    results = Dietitian.objects.filter(current_user_id=user_id).order_by(
                        'name')
                else:
                    results = Dietitian.objects.filter(current_user_id=user_id, is_disable=False).order_by(
                        'name')

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
            html = render_to_string('data_management/search_data/search_dietitian.html',
                                    {'dietitian': results})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_dietitian_by_stages_by_publisher                   #
# Owner -                                                          #
# Review by -
#                                                                  #
# comment : good                                                   #
#                                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_dietitian_by_stages_by_publisher(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            category_filter = False
            if q is not None:
                results = Dietitian.objects.filter(stage_id=q,current_user_id=request.user.id,is_disable=False ).order_by('name')
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
            html = render_to_string('publisher/dietitian/search_dietitian_by_stage_by_publisher.html',
                                    {'tab': 'publish_dietitian_data', 'crosal': 'dietitian_bymanagebypublisher',
                                     'dietitian': results,
                                     'category_filter': category_filter,
                                     'stage_data_pub':q})
            return HttpResponse(html)
    except Exception as e:
        #print e
        raise Http404

####################################################################
# Name - search_dietitian_by_users_by_admin                        #
# BY : NISHANK                                                     #
# Review by -
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_dietitian_by_users_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Dietitian.objects.filter(current_user_id=q).order_by('name')
            paginator = Paginator(results,100)
            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('admin/dietitian_management/search_by_user_admin.html',
                                    {'tab': 'data', 'crosal': 'dietitianbymanage',
                                     'dietitian_all_data': results,'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_dietitian_by stage and user                        #
# BY : Nishank                                                     #
# Review by -
#                                                                  #
# comment :                                                        #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_dietitian_admin_on_stage_user(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Dietitian.objects.filter(name__icontains=q).order_by('name')
            else:
                results = Dietitian.objects.all().order_by('name')
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
            html = render_to_string('admin/dietitian_management/search_dietitian_by_stage_user.html',
                                    {'tab': 'data', 'crosal': 'dietitianbymanage', 'dietitian_all_data': results,
                                     'search_data_two':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_Dietitian_by_stages_by_admin                       #
# Owner - Jaydeep  verma                                           #
# Review by -
#                                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_dietitian_by_stages_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Dietitian.objects.filter(stage_id=q).order_by('name')
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
            html = render_to_string('admin/dietitian_management/search_dietitian_by_stage_user.html',
                                    {'tab': 'data', 'crosal': 'dietitianbymanage', 'dietitian_all_data': results,
                                     'stage_no':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

###################################################################
# Name - search_dietitian_admin                                   #
# Owner - Jaydeep verma                                           #
# Review by -
#                                                                 #
# comment :
#                                                                 #
###################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_dietitian_assign_admin(request):
    try:
        if request.method == 'POST':
            city_list = City.objects.all().order_by('name')
            locality_list = Locality.objects.all().order_by('name')
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Dietitian.objects.filter(name__icontains=q).order_by('name')
            else:
                results = Dietitian.objects.all().order_by('name')
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
            html = render_to_string('admin/dietitian_management/search_admin_dietitian.html',
                                    {'tab': 'data', 'crosal': 'dietitianbymanage', 'dietitian': results,
                                     'search_data':q,'city_list':city_list,'locality_list':locality_list})
            return HttpResponse(html)
    except Exception as e:
        #print e
        raise Http404


# ########## THERAPIST START ####################

####################################################################
# Name - search_therapist_caller                                   #
# BY :  Nishank                                                    #
# Review by -                                                      #
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_therapist_caller(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:

                if request.user.is_superuser :
                    results = Therapist.objects.filter(current_user_id=user_id, name__icontains=q,
                                                  ).order_by('name')
                else:
                    results = Therapist.objects.filter(current_user_id=user_id, name__icontains=q,
                                                         is_disable=False).order_by('name')
            elif user_id:
                if request.user.is_superuser:
                    results = Therapist.objects.filter(current_user_id=user_id).order_by(
                        'name')
                else:
                    results = Therapist.objects.filter(current_user_id=user_id, is_disable=False).order_by(
                        'name')

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
            html = render_to_string('data_management/search_data/search_therapist.html',
                                    {'therapist': results,'therapist_search_data':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_therapist_by_stages_by_publisher                   #
# Owner -                                                          #
# Review by -
#                                                                  #
# comment : good                                                   #
#                                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_therapist_by_stages_by_publisher(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            category_filter = False
            if q is not None:
                results = Therapist.objects.filter(stage_id=q,current_user_id=request.user.id,is_disable=False ).order_by('name')
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
            html = render_to_string('publisher/therapist/search_therapist_by_stage_by_publisher.html',
                                    {'tab': 'publish_therapist_data', 'crosal': 'therapist_bymanagebypublisher',
                                     'therapist': results,
                                     'category_filter': category_filter,
                                     'stage_data_pub':q})
            return HttpResponse(html)
    except Exception as e:
        #print e
        raise Http404

####################################################################
# Name - search_therapist_by_users_by_admin                        #
# BY : NISHANK                                                     #
# Review by -
#                                                                  #
# comment :                                                        #
#                                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_therapist_by_users_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Therapist.objects.filter(current_user_id=q).order_by('name')
            paginator = Paginator(results,100)
            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('admin/therapist_management/search_by_user_admin.html',
                                    {'tab': 'data', 'crosal': 'therapistbymanage',
                                     'therapist_all_data': results,'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_therapist_by stage and user                        #
# BY : Nishank                                                     #
# Review by -
#                                                                  #
# comment :                                                        #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_therapist_admin_on_stage_user(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Therapist.objects.filter(name__icontains=q).order_by('name')
            else:
                results = Therapist.objects.all().order_by('name')
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
            html = render_to_string('admin/therapist_management/search_therapist_by_stage_user.html',
                                    {'tab': 'data', 'crosal': 'therapistbymanage', 'therapist_all_data': results,
                                     'search_data_two':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_Therapist_by_stages_by_admin                       #
# Owner - Jaydeep  verma                                           #
# Review by -
#                                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_therapist_by_stages_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Therapist.objects.filter(stage_id=q).order_by('name')
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
            html = render_to_string('admin/therapist_management/search_therapist_by_stage_user.html',
                                    {'tab': 'data', 'crosal': 'therapistbymanage', 'therapist_all_data': results,
                                     'stage_no':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

###################################################################
# Name - search_therapist_admin                                   #
# Owner - Jaydeep verma                                           #
# Review by -
#                                                                 #
# comment :
#                                                                 #
###################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_therapist_assign_admin(request):
    try:
        if request.method == 'POST':
            city_list = City.objects.all().order_by('name')
            locality_list = Locality.objects.all().order_by('name')
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Therapist.objects.filter(name__icontains=q).order_by('name')
            else:
                results = Therapist.objects.all().order_by('name')
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
            html = render_to_string('admin/therapist_management/search_admin_therapist.html',
                                    {'tab': 'data', 'crosal': 'therapistbymanage', 'therapist': results,
                                     'search_data':q,'city_list':city_list,'locality_list':locality_list})
            return HttpResponse(html)
    except Exception as e:
        #print e
        raise Http404

####################################################################
# Name - search_doctor_publisher                                   #
# By Nishank                                                       #

####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_doctor_for_publisher(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = Doctor.objects.filter(current_user_id=user_id, name__icontains=q,is_disable=False).order_by('name')
            elif user_id:
                #results = Doctor.objects.filter(current_user_id=user_id, is_disable=False).order_by('name')
                results = []
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
            html = render_to_string('publisher/doctor/search_doctor_by_name.html',
                                    {'doctor': results, 'tab_listing': 'doctor_listing','search_name':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_organisation_publisher                             #
# By Nishank                                                       #

####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_organisation_for_publisher(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = OrganisationName.objects.filter(current_user_id=user_id,is_live_org=False, name__icontains=q,is_disable=False).order_by('name')
            elif user_id:
                #results = Doctor.objects.filter(current_user_id=user_id, is_disable=False).order_by('name')
                results = []
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
            html = render_to_string('publisher/organisation/search_organisation_by_name.html',
                                    {'organisation': results, 'tab_listing': 'organisation_listing','search_name':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_pharmacy_publisher                                 #
# By Nishank                                                       #

####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_pharmacy_for_publisher(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = MedicalPharmacyStore.objects.filter(current_user_id=user_id, name__icontains=q,
                                                is_disable=False).order_by('name')
            elif user_id:
                #results = Doctor.objects.filter(current_user_id=user_id, is_disable=False).order_by('name')
                results = []
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
            html = render_to_string('publisher/pharmacy/search_pharmacy_by_name.html',
                                    {'pharmacy': results, 'tab_listing': 'pharmacy_listing','search_name':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_lab_publisher                                 #
# By Nishank                                                       #

####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_lab_for_publisher(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = Labs.objects.filter(current_user_id=user_id, name__icontains=q,
                                                is_disable=False).order_by('name')
            elif user_id:
                #results = Doctor.objects.filter(current_user_id=user_id, is_disable=False).order_by('name')
                results = []
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
            html = render_to_string('publisher/lab/search_lab_by_name.html',
                                    {'lab': results, 'tab_listing': 'lab_listing','search_name':q})
            return HttpResponse(html)
    except Exception as e:
        #print e
        raise Http404

####################################################################
# Name - search_bloodbank_publisher                                 #
# By Nishank                                                       #

####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_bloodbank_for_publisher(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = BloodBank.objects.filter(current_user_id=user_id, name__icontains=q,
                                                is_disable=False).order_by('name')
            elif user_id:
                #results = Doctor.objects.filter(current_user_id=user_id, is_disable=False).order_by('name')
                results = []
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
            html = render_to_string('publisher/bloodbank/search_bloodbank_by_name.html',
                                    {'bloodbank': results, 'tab_listing': 'bloodbank_listing','search_name':q})
            return HttpResponse(html)
    except Exception as e:
        #print e
        raise Http404

####################################################################
# Name - search_therapist_publisher                                 #
# By Nishank                                                       #

####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_therapist_for_publisher(request):
    try:
        if request.method == 'POST':
            search_name =  None
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = Therapist.objects.filter(current_user_id=user_id, name__icontains=q,
                                                is_disable=False).order_by('name')
            elif user_id:
                #results = Doctor.objects.filter(current_user_id=user_id, is_disable=False).order_by('name')
                results = []
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
            html = render_to_string('publisher/therapist/search_therapist_by_name.html',
                                    {'therapist_obj': results, 'tab_listing': 'therapist_listing','search_name':q})
            return HttpResponse(html)
    except Exception as e:
        #print e
        raise Http404

####################################################################
# Name - search_ambulance_publisher                                 #
# By Nishank                                                       #

####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_ambulance_for_publisher(request):
    try:
        if request.method == 'POST':
            search_name =  None
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = Ambulance.objects.filter(current_user_id=user_id, name__icontains=q,
                                                is_disable=False).order_by('name')
            elif user_id:
                #results = Doctor.objects.filter(current_user_id=user_id, is_disable=False).order_by('name')
                results = []
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
            html = render_to_string('publisher/ambulance/search_ambulance_by_name.html',
                                    {'ambulance': results, 'tab_listing': 'ambulance_listing','search_name':q})
            return HttpResponse(html)
    except Exception as e:
        #print e
        raise Http404


####################################################################
# Name - search_rehab_publisher                                #
# By Nishank                                                       #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_rehab_for_publisher(request):
    try:
        if request.method == 'POST':
            search_name =  None
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = RehabCenter.objects.filter(current_user_id=user_id, clinic_name__icontains=q,
                                                is_disable=False).order_by('clinic_name')
            elif user_id:
                #results = Doctor.objects.filter(current_user_id=user_id, is_disable=False).order_by('name')
                results = []
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
            html = render_to_string('publisher/rehab/search_rehab_by_name.html',
                                    {'rehab_obj': results, 'tab_listing': 'rehab_listing','search_name':q})
            return HttpResponse(html)
    except Exception as e:
        #print e
        raise Http404

####################################################################
# Name - search_nurse_bureau_publisher                             #
# By Nishank                                                       #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_nurse_bureau_for_publisher(request):
    try:
        if request.method == 'POST':
            search_name =  None
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = Nurse_Bureau.objects.filter(current_user_id=user_id, name__icontains=q,
                                                is_disable=False).order_by('name')
            elif user_id:
                #results = Doctor.objects.filter(current_user_id=user_id, is_disable=False).order_by('name')
                results = []
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
            html = render_to_string('publisher/nurse_bureau/search_nurse_bureau_by_name.html',
                                    {'nurse_bureau_obj': results, 'tab_listing': 'rehab_listing','search_name':q})
            return HttpResponse(html)
    except Exception as e:
        #print e
        raise Http404



####################################################################
# Name - global_search_for_all_users                               #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def global_search_for_all_users(request):
    try:
        if request.method == 'GET':
            try:
                data_found = request.GET['data_found']
                value = request.GET['value']
                type = request.GET['type']
            except:
                data_found = False
                value = None
                type = None

            if data_found and value and type:
                try :
                    if type == 'Doctor':
                        results = Doctor.objects.filter(name__icontains=value).order_by('name')
                    elif type == 'Organisation':
                        results = OrganisationName.objects.filter(name__icontains=value,is_live_org=False).order_by('name')
                    elif type == 'BloodBank':
                        results = BloodBank.objects.filter(name__icontains=value).order_by('name')
                    elif type == 'Lab':
                        results = Labs.objects.filter(name__icontains=value).order_by('name')
                    elif type == 'Pharmacy':
                        results = MedicalPharmacyStore.objects.filter(name__icontains=value).order_by('name')
                    elif type == 'Rehab':
                        results = RehabCenter.objects.filter(clinic_name__icontains=value).order_by('clinic_name')
                    elif type == 'Ambulance':
                        results = Ambulance.objects.filter(name__icontains=value).order_by('name')
                    elif type == 'Disease Article':
                        results = Disease.objects.filter(topic_title__icontains=value).order_by('topic_title')
                    elif type == 'Symptom Article':
                        results = Symptoms.objects.filter(topic_title__icontains=value).order_by('topic_title')
                    elif type == 'News Feed':
                        results = NewsFeed.objects.filter(topic_title__icontains=value).order_by('topic_title')
                    elif type == 'Service Plans':
                        results = ServicePlan.objects.filter(plan_name__icontains=value).order_by('plan_name')
                    elif type == 'Therapist':
                        results = Therapist.objects.filter(name__icontains=value).order_by('name')
                    elif type == 'NB':
                        results = Nurse_Bureau.objects.filter(name__icontains=value).order_by('name')
                    elif type == 'Dietitian':
                        results = Dietitian.objects.filter(name__icontains=value).order_by('name')
                    elif type == 'BloodBank':
                        results = BloodBank.objects.filter(name__icontains=value).order_by('name')
                    elif type == 'Live-Doctor':
                        l_alls = Live_Doctor.objects.all()
                        results = []
                        for ldoc in l_alls:
                            fname=''
                            fname = ldoc.firstName+' '+ldoc.lastName
                            if value.lower() in fname.lower():
                                results.append(ldoc)


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

                    return render(request, 'global_search_for_all_users.html',
                                  {'tab': 'global_search_for_all', 'type': type, 'value': value, 'results': results,
                                   'data_found': data_found})
                except:
                    results= []
            else:
                results = []


            return render(request, 'global_search_for_all_users.html',
                          {'tab': 'global_search_for_all','type':None,'value':None,'results':results,'data_found':None })

        elif request.method == 'POST':
            type = request.POST['formDATA[type]']
            value = request.POST['formDATA[value]']
            if type and value:
                try :
                    if type == 'Doctor':
                        results = Doctor.objects.filter(name__icontains=value).order_by('name')
                    elif type == 'Organisation':
                        results = OrganisationName.objects.filter(name__icontains=value,is_live_org=False).order_by('name')
                    elif type == 'BloodBank':
                        results = BloodBank.objects.filter(name__icontains=value).order_by('name')
                    elif type == 'Lab':
                        results = Labs.objects.filter(name__icontains=value).order_by('name')
                    elif type == 'Pharmacy':
                        results = MedicalPharmacyStore.objects.filter(name__icontains=value).order_by('name')
                    elif type == 'Rehab':
                        results = RehabCenter.objects.filter(clinic_name__icontains=value).order_by('clinic_name')
                    elif type == 'Ambulance':
                        results = Ambulance.objects.filter(name__icontains=value).order_by('name')
                    elif type == 'Disease Article':
                        results = Disease.objects.filter(topic_title__icontains=value).order_by('topic_title')
                    elif type == 'Symptom Article':
                        results = Symptoms.objects.filter(topic_title__icontains=value).order_by('topic_title')
                    elif type == 'News Feed':
                        results = NewsFeed.objects.filter(topic_title__icontains=value).order_by('topic_title')
                    elif type == 'Service Plans':
                        results = ServicePlan.objects.filter(plan_name__icontains=value).order_by('plan_name')
                    elif type == 'Therapist':
                        results = Therapist.objects.filter(name__icontains=value).order_by('name')
                    elif type == 'NB':
                        results = Nurse_Bureau.objects.filter(name__icontains=value).order_by('name')
                    elif type == 'Dietitian':
                        results = Dietitian.objects.filter(name__icontains=value).order_by('name')
                    elif type == 'Live-Doctor':
                        l_alls = Live_Doctor.objects.all()
                        results = []
                        for ldoc in l_alls:
                            fname = ''
                            fname = ldoc.firstName + ' ' + ldoc.lastName
                            if value.lower() in fname.lower():
                                results.append(ldoc)


                except:
                    results= []
                if results :
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

                    html = render_to_string('global_search_results.html',
                                            {'tab': 'global_search_for_all', 'type':type,'value':value,'results':results,'data_found':True})
                    return HttpResponse(html)

                html = "<div class=table-responsive table_modify_for_all>No DATA Found</div>"
                return HttpResponse(html)

            messages.error(request,"Invalid data")
            return redirect(request.META.HTTP_REFERER)

    except Exception as e   :
        #print e
        messages.error(request,"Method not allowed")
        return redirect(request.META.HTTP_REFERER)


####################################################################
# Name - search_disease_by_name_publisher                          #
# By Nishank                                                       #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_disease_by_name_publisher(request):
    try:
        if request.method == 'POST':
            search_name =  None
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = Disease.objects.filter(current_user_id=user_id, topic_title__icontains=q,is_disable=False).order_by('topic_title')
            elif user_id:
                #results = Doctor.objects.filter(current_user_id=user_id, is_disable=False).order_by('name')
                results = []
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
            html = render_to_string('publisher/disease/search_disease_by_name_publisher.html',
                                    {'publisher_data': results, 'search_data':q,'tab_listing': 'global_listing',
                                     'tab': 'news_data'})
            return HttpResponse(html)
    except Exception as e:
        #print e
        raise Http404

# LIve doctor search views Start
#-------------------------------

####################################################################
# Name - search_live_doctor_by_users_by_admin                      #
# By : Nishank                                                     #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_live_doctor_by_users_by_admin(request):
    try:
        if request.method == 'POST':
            all_categories = Category.objects.filter(delete=False)
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Live_Doctor.objects.filter(current_user_id=q).order_by('-createdAt')
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
            html = render_to_string('admin/live_doctor_management/search_live_doctor_by_users.html',
                                    {'tab': 'data', 'crosal': 'doctorbymanage', 'doctor_all_data': results,
                                     'search_data': q,'all_categories':all_categories})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_live_doctor_by_name_on_by_stage_page               #
# By : Nishank                                                     #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_live_doctor_by_name_on_by_stage_page(request):
    try:
        if request.method == 'POST':
            all_categories = Category.objects.filter(delete=False)
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                ttemp = []
                results = Live_Doctor.objects.all().order_by('-createdAt')  #filter(name__icontains=q)
                for i in results:
                    fullNAme = ''
                    fullNAme = i.firstName+ ' '+i.lastName
                    if q.lower() in fullNAme.lower():
                        ttemp.append(i)
                results = ttemp
            else:
                results = []
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
            html = render_to_string('admin/live_doctor_management/search_live_doctor_by_stages_user.html',
                                    {'tab': 'data', 'crosal': 'doctorbymanage', 'doctor_all_data': results,
                                     'search_data_two': q,'all_categories':all_categories})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_live_doctor_by_stages_by_admin                     #
# By : Nishank                                                     #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_live_doctor_by_stages_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Live_Doctor.objects.filter(stage_id=q).order_by('-createdAt')
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
            html = render_to_string('admin/live_doctor_management/search_live_doctor_by_stages_user.html',
                                    {'tab': 'data', 'crosal': 'doctorbymanage', 'doctor_all_data': results,
                                     'stage_no': q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_live_doctor_assign_admin                           #
# Owner - Visnu Badal                                              #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_live_doctor_assign_admin(request):
    try:
        if request.method == 'POST':
            all_category = Category.objects.filter(delete=False).order_by('name')
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Live_Doctor.objects.all().order_by('-createdAt') #filter(name__icontains=q)
                mpty = []
                for i in results:
                    fulln = ''
                    fulln =  i.firstName + ' '+ i.lastName
                    if q.lower() in fulln.lower():
                        mpty.append(i)
                results= mpty
            else:
                results = Live_Doctor.objects.all().order_by('-createdAt')
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
            html = render_to_string('admin/live_doctor_management/search_admin_live_doctor.html',
                                    {'tab': 'data', 'crosal': 'doctorbymanage', 'doctor_data_obj': results,
                                     'search_data': q,'all_category':all_category})
            return HttpResponse(html)
    except Exception as e:

        raise Http404


####################################################################
# Name - deleted_schedules_with_sponsored_ranks                    #
# Owner - Nishank Gupta                                           #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def deleted_schedules_with_sponsored_ranks(request):
    try:
        mpty= []
        del_sch_mainlist = []
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                doctors = Live_Doctor.objects.all()
                mpty = []
                for i in doctors:
                    fulln = ''
                    fulln =  i.firstName + ' '+ i.lastName
                    if q.lower() in fulln.lower():
                        mpty.append(i)
                mpty = [x.id for x in mpty]
                all_deleted_Schedules = Live_Doctor_Commonworkschedule.objects.filter(status__iexact='delete',doctor_id__in=mpty)
            else:
                all_deleted_Schedules = []


            for sscchh in all_deleted_Schedules:
                lldoc = Live_Doctor.objects.get(id=sscchh.doctor_id)
                try:
                    doccategory = Category.objects.get(id=lldoc.category).name
                except:
                    doccategory = None

                try:
                    oorg = OrganisationName.objects.get(id=sscchh.clinic_id)
                except:
                    oorg = None
                if oorg != None and doccategory != None:
                    Key_CC_RANK = oorg.city_id.__str__() + '-' + lldoc.category.__str__()
                    key_CLC_RANK = oorg.city_id.__str__() + '-' + oorg.locality_id.__str__() + '-' + lldoc.category.__str__()
                    Spon_cc =  lldoc.sponsored_rank['CC_RANK_list'].get(Key_CC_RANK,'DoesNotExist')
                    Spon_clc = lldoc.sponsored_rank['CLC_RANK_list'].get(key_CLC_RANK,'DoesNotExist')
                    Key_CC_RANK_lable = oorg.city.name + '-' + Category.objects.get(id=lldoc.category).name
                    key_CLC_RANK_label = oorg.city.name + '-' + oorg.locality.name + '-' + Category.objects.get(
                        id=lldoc.category).name
                    if Spon_cc == 'DoesNotExist' and Spon_clc == 'DoesNotExist':
                        pass
                    else:
                        if Spon_cc == 'DoesNotExist':
                            Spon_cc = None
                        if Spon_clc == 'DoesNotExist':
                            Spon_clc = None
                        del_sch_mainlist.append([lldoc,doccategory,oorg,Spon_cc,Spon_clc,Key_CC_RANK,key_CLC_RANK,lldoc.firstName,
                                                 Key_CC_RANK_lable,key_CLC_RANK_label])
            if del_sch_mainlist != []:
                del_sch_mainlist.sort(key=lambda x: x[7])
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
            html = render_to_string('admin/live_doctor_management/deleted_schedules_with_sponsored_ranks.html',
                                    {'tab': 'data', 'crosal': 'doctorbymanage', 'del_sch_mainlist': del_sch_mainlist,
                                     'search_data': q,})
            return HttpResponse(html)
    except Exception as e:

        raise Http404


####################################################################
# Name - search_live_doctor_for_publisher                          #
# By Nishank                                                       #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_live_doctor_for_publisher(request):
    try:
        all_categories = Category.objects.filter(delete=False)
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None and q != '':
                results = Live_Doctor.objects.filter(current_user_id=user_id).order_by('-createdAt')
                templist =[]
                if list(results) != []:
                    for i in results:
                        fn = ''
                        fn = i.firstName+' '+i.lastName
                        if q.lower() in fn.lower():
                            templist.append(i)
                results = templist

            elif user_id:
                # results = Doctor.objects.filter(current_user_id=user_id, is_disable=False).order_by('name')
                results = Live_Doctor.objects.filter(current_user_id=user_id).order_by('-createdAt')
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
            html = render_to_string('publisher/live_doctor/search_live_doctor_by_name.html',
                                    {'doctor': results, 'tab_listing': 'doctor_listing', 'search_name': q,
                                     'all_categories':all_categories})
            return HttpResponse(html)
    except Exception as e:
        raise Http404
#-------------------------------
# LIve doctor search views end


####################################################################
# Name - search_symptom_by_name_publisher                          #
# By Nishank                                                       #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_symptom_by_name_publisher(request):
    try:
        if request.method == 'POST':
            search_name =  None
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = Symptoms.objects.filter(current_user_id=user_id, topic_title__icontains=q,is_disable=False).order_by('topic_title')
            elif user_id:
                #results = Doctor.objects.filter(current_user_id=user_id, is_disable=False).order_by('name')
                results = []
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
            html = render_to_string('publisher/symptoms/search_symptoms_by_name_publisher.html',
                                    {'publisher_data': results, 'search_data':q,'tab_listing': 'global_listing',
                                     'tab': 'news_data'})
            return HttpResponse(html)
    except Exception as e:
        #print e
        raise Http404

####################################################################
# Name - search_service_offered                                    #
# Owner - Ashutosh KEsharvani                                      #
#  Review by -                                                     #
# comment :                                                        #
#                                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_service_offered(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Service_Offred.objects.filter(name__icontains=q)
            else:
                results = Service_Offred.objects.all()
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
            html = render_to_string('admin/master_data_management/search_service_offered_data_management.html',
                                    {'tab': 'data', 'crosal': 'doctorbymanage','service_offered_obj': results,
                                     'search_data_two':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - localitymaster_admin                                       #
# By - AShutosh                                                     #
#
#                                                                  #
#                                                                  #
#                                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_locality_master(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            if q is not None :
                try :
                    results = Localitymaster.objects.filter(name__icontains=q).order_by('id')
                except:
                    results= None
                if results :
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

                    html = render_to_string('admin/master_data_management/manage_country_state_city_location_master/Search_localitymaster.html',
                                            {'tab': 'data', 'crosal': 'localitybymanage',
                                            'search_data':q,'locality_obj':results})
                    return HttpResponse(html)

                html = "<div class=table-responsive table_modify_for_all>No Locality Found</div>"
                return HttpResponse(html)

            messages.error(request,"Invalid data")
            return redirect(request.META.HTTP_REFERER)

    except:

        messages.error(request,"Method not allowed")
        return redirect(request.META.HTTP_REFERER)


####################################################################
# Name - search_city_master                                        #
# By - Ashutosh                                                    #
#
#                                                                  #
#                                                                  #
#                                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_city_master(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            if q is not None :
                try :
                    results = Citymaster.objects.filter(name__icontains=q).order_by('id')
                except:
                    results= None
                if results :
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

                    html = render_to_string('admin/master_data_management/manage_country_state_city_location_master/Search_citymaster.html',
                                            {'tab': 'data',
                                            'search_data':q,'city_obj':results,'request':request})
                    return HttpResponse(html)

                html = "<div class=table-responsive table_modify_for_all> No City Found </div>"
                return HttpResponse(html)


            return redirect(request.META.HTTP_REFERER)

    except Exception as e:
        return redirect(request.META.HTTP_REFERER)


####################################################################
# Name - search_localitybycity                                     #
# Owner - ASHUTOSH                                                 #
####################################################################

@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def filter_localitybycity(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Localitymaster.objects.filter(citymaster=q).order_by('name')
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
            html = render_to_string('admin/master_data_management/manage_country_state_city_location_master/search_localitybycity.html',
                                    {'tab': 'data', 'crosal': '', 'locality_obj': results,
                                     'stage_no':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - filter_citybystate                                        #
# Owner - ASHUTOSH                                                 #
####################################################################

@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def filter_citybystate(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = Citymaster.objects.filter(statemaster=q)
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
            html = render_to_string('admin/master_data_management/manage_country_state_city_location_master/search_citybystate.html',
                                    {'tab': 'data', 'crosal': '', 'city_obj': results,
                                     'stage_no':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404



####################################################################
# Name - search_state_master                                        #
# By - Ashutosh                                                    #
#
#                                                                  #
#                                                                  #
#                                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_state_master(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            if q is not None :
                try :
                    results = Statemaster.objects.filter(name__icontains=q).order_by('id')
                except:
                    results= None
                if results :
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

                    html = render_to_string('admin/master_data_management/manage_country_state_city_location_master/search_state_master.html',
                                            {'tab': 'data',
                                            'search_data':q,'state_obj':results,'request':request})
                    return HttpResponse(html)

                html = "<div class=table-responsive table_modify_for_all> No State Found </div>"
                return HttpResponse(html)


            return redirect(request.META.HTTP_REFERER)

    except Exception as e:
        return redirect(request.META.HTTP_REFERER)



####################################################################
# Name - search_categorymaster_byname                              #
# By - Ashutosh                                                    #
#
#                                                                  #
#                                                                  #
#                                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_categorymaster_byname(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            if q is not None :
                try :
                    results = Category.objects.filter(name__icontains=q).order_by('id')
                except:
                    results= None
                html = render_to_string('admin/master_data_management/masters_search/search_categorymaster_byname.html',
                                        {'tab': 'data',
                                        'search_data':q,'category_obj':results,'request':request})
                return HttpResponse(html)


            return redirect(request.META.HTTP_REFERER)

    except Exception as e:
        return redirect(request.META.HTTP_REFERER)

####################################################################
# Name - search_specialitymaster_byname                            #
# By - Ashutosh                                                    #
#                                                                  #
#                                                                  #
#                                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_specialitymaster_byname(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            if q is not None :
                try :
                    results = Speciality.objects.filter(name__icontains=q).order_by('id')
                except:
                    results= None
                if results :
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

                    html = render_to_string(
                        'admin/master_data_management/masters_search/search_specialitymaster_byname.html',
                        {'tab': 'data','search_dataa': q, 'speciality_obj': results, 'request': request})
                    return HttpResponse(html)

                html = "<div class=table-responsive table_modify_for_all> No State Found </div>"
                return HttpResponse(html)

            return redirect(request.META.HTTP_REFERER)

    except Exception as e:
        return redirect(request.META.HTTP_REFERER)

####################################################################
# Name - search_facility_byname                                    #
# By - Ashutosh                                                    #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_facility_byname(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            if q is not None :
                try :
                    results = Facility.objects.filter(name__icontains=q).order_by('id')
                except:
                    results= None
                html = render_to_string('admin/master_data_management/masters_search/search_facility_byname.html',
                                        {'tab': 'data',
                                        'search_data':q,'facility_obj':results,'request':request})
                return HttpResponse(html)
            return redirect(request.META.HTTP_REFERER)

    except Exception as e:
        return redirect(request.META.HTTP_REFERER)

####################################################################
# Name - search_disease_byname                                        #
# By - Ashutosh                                                    #
#
#                                                                  #
#                                                                  #
#                                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_disease_byname(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            if q is not None :
                try :
                    results = Disease_Category_search_mapping.objects.filter(disease_name__icontains=q).order_by('id')
                except:
                    results= None
                if results :
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

                    html = render_to_string('admin/master_data_management/masters_search/search_disease_byname.html',
                                            {'tab': 'data','search_data': q, 'disease_category': results, 'request': request})
                    return HttpResponse(html)

                html = "<div class=table-responsive table_modify_for_all> No State Found </div>"
                return HttpResponse(html)

    except Exception as e:
        return redirect(request.META.HTTP_REFERER)

####################################################################
# Name - search_labtest_byname                                        #
# By - Ashutosh                                                    #
#
#                                                                  #
#                                                                  #
#                                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_labtest_byname(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            if q is not None :
                try :
                    results = Lab_test_master.objects.filter(name__icontains=q).order_by('id')
                except:
                    results= None
                if results :
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

                    html = render_to_string('admin/master_data_management/masters_search/search_labtest_byname.html',
                                            {'tab': 'data','search_data': q, 'lab_test_master': results, 'request': request})
                    return HttpResponse(html)

                html = "<div class=table-responsive table_modify_for_all> No State Found </div>"
                return HttpResponse(html)

            return redirect(request.META.HTTP_REFERER)

    except Exception as e:
        return redirect(request.META.HTTP_REFERER)

####################################################################
# Name - search_diseasemaster_byname                                        #
# By - Ashutosh                                                    #
#
#                                                                  #
#                                                                  #
#                                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_diseasemaster_byname(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            if q is not None :
                try :
                    results = Disease_search_master.objects.filter(name__icontains=q).order_by('id')
                except:
                    results= None
                if results:
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

                    html = render_to_string('admin/master_data_management/masters_search/search_diseasemaster_byname.html',
                                            {'tab': 'data',
                                            'search_data': q, 'disease_search_master': results, 'request': request})
                    return HttpResponse(html)

                html = "<div class=table-responsive table_modify_for_all> No State Found </div>"
                return HttpResponse(html)
            return redirect(request.META.HTTP_REFERER)

    except Exception as e:
        return redirect(request.META.HTTP_REFERER)


####################################################################
# Name - search_symptommaster_byname                                        #
# By - Ashutosh                                                    #
#
#                                                                  #
#                                                                  #
#                                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_symptommaster_byname(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            if q is not None :
                try :
                    results = Symptoms_search_master.objects.filter(name__icontains=q).order_by('id')
                except:
                    results= None
                if results:
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

                    html = render_to_string(
                        'admin/master_data_management/masters_search/search_symptommaster_byname.html',
                        {'tab': 'data',
                         'search_data': q, 'symptoms_search_master': results, 'request': request})
                    return HttpResponse(html)

                html = "<div class=table-responsive table_modify_for_all> No State Found </div>"
                return HttpResponse(html)
            return redirect(request.META.HTTP_REFERER)

    except Exception as e:
        return redirect(request.META.HTTP_REFERER)


####################################################################
# Name - search_organisation_by_users_by_admin                     #
# Owner - Visnu Badal                                              #
# Review by - jitendra dixit
#                                                                  #
# comment : good                                                   #
#                                                                  #
####################################################################


@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def filter_live_organisation_by_users(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = OrganisationName.objects.filter(current_user_id=q, is_live_org=True).order_by('name')
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
            html = render_to_string('admin/admin_live_organisation/search_by_user_admin.html',
                                    {'tab': 'data', 'crosal': 'organisationbymanage', 'organisation_all_data': results,
                                     'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        print e
        raise Http404

####################################################################
# Name - search_organisation_by_stages_by_admin                    #
# Owner - Visnu Badal                                              #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def filter_live_organisation_by_stages(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = OrganisationName.objects.filter(stage_id=q, is_live_org=True).order_by('name')
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
            html = render_to_string('admin/admin_live_organisation/search_live_organisation_stages.html',
                                    {'tab': 'data', 'crosal': 'organisationbymanage', 'organisation_all_data': results,
                                     'stage_no':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404


####################################################################
# Name - search_whole_live_organisation                            #
# Owner - Dhrumil Shah                                             #
####################################################################

@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_whole_live_organisation(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = OrganisationName.objects.filter(name__icontains=q, is_live_org=True).order_by('name')
            else:
                results = OrganisationName.objects.filter(is_live_org=True).order_by('name')
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
            html = render_to_string('admin/admin_live_organisation/search_live_organisation_assign.html',
                                    {'tab': 'data', 'crosal': 'doctorbymanage', 'organisation_data_obj': results,
                                     'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        print e
        raise Http404


@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_organisation_assign_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = OrganisationName.objects.filter(name__icontains=q,is_live_org=False).order_by('name')
            else:
                results = OrganisationName.objects.filter(is_live_org=False).order_by('name')
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
            html = render_to_string('admin/admin_organisation/search_organisation_assign.html',
                                    {'tab': 'data', 'crosal': 'doctorbymanage', 'organisation_data_obj': results,
                                     'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        print e
        raise Http404


####################################################################
# Name - search_live_organisation_by_publisher                     #
# Owner - Dhrumil Shah                                             #
####################################################################

@login_required(login_url='/')
@csrf_exempt
def search_live_organisation_by_publisher(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            category_filter = False
            if q is not None:
                results = OrganisationName.objects.filter(is_live_org=True,stage_id=q,current_user_id=request.user.id,is_disable=False).order_by('name')
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
            html = render_to_string('publisher/live_organisation/search_live_organisation_by_stage_by_publisher.html',
                                    {'tab': 'publish_live_organisation_data',
                                     'live_organisation': results,
                                     'category_filter': category_filter,'stage_id':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_live_doctor_caller                                 #
# Owner - Dhrumil Shah                                             #
####################################################################


@login_required(login_url='/')
@csrf_exempt
def search_live_organisation_caller(request):
    try:
        if request.method == 'POST':
            user_data = User.objects.all()
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            usmo = UserManagement.objects.get(user_id = request.user.id)
            if user_id and q is not None:
                if usmo.is_reviewer and usmo.is_doctor_reviewer:
                    results = OrganisationName.objects.filter(current_user_id=user_id, is_live_org=True, name__icontains=q, is_disable=False).order_by('name')
                else:
                    results = OrganisationName.objects.filter(current_user_id=user_id, is_live_org=True, name__icontains=q,
                                                          is_disable=False).order_by('name')
            elif user_id:
                results = OrganisationName.objects.filter(current_user_id=user_id, is_live_org=True, is_disable=False).order_by('name')
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
            html = render_to_string('data_management/search_data/search_live_organisation.html',
                                    {'user_data': user_data,'organisation_data_obj': results,'request':request})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_live_organisation_publisher                             #
# By Dhrumil Shah                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def search_live_organisation_for_publisher(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = OrganisationName.objects.filter(current_user_id=user_id, is_live_org=True, name__icontains=q,is_disable=False).order_by('name')
            elif user_id:
                #results = Doctor.objects.filter(current_user_id=user_id, is_disable=False).order_by('name')
                results = []
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
            html = render_to_string('publisher/live_organisation/search_live_organisation_by_name.html',
                                    {'organisation': results, 'tab_listing': 'organisation_listing','search_name':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_live_organisation_by_stage_admin                   #
# Owner - Dhrumil Shah                                             #
####################################################################


@login_required(login_url='/')
@csrf_exempt
def search_live_organisation_by_stage_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = OrganisationName.objects.filter(is_live_org=True, name__icontains=q).order_by('name')
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
            html = render_to_string('admin/admin_live_organisation/search_live_organisaton_admin.html',
                                    {'tab': 'data', 'crosal': 'organisationbymanage', 'organisation_all_data': results,
                                     'search_data_two':q})
            return HttpResponse(html)
    except Exception as e:
        #print e
        raise Http404


####################################################################
# Name - search_DoctorNewSO_by_name_admin                          #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_DoctorNewSO_by_name_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            if q is not None :
                try :
                    results = Doctor_ServiceOffered_New.objects.filter(WorL__iexact='winner',name__icontains=q).order_by('name')
                except:
                    results= None
                if results :
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

                    html = render_to_string('admin/master_data_management/DoctorNewSO_search_by_name.html',
                                            {'tab': 'data', 'crosal': 'DoctorNewSO',
                                            'search_data':q,'DoctorNewSO_obj':results})
                    return HttpResponse(html)

                html = "<div class=table-responsive table_modify_for_all>No Service Offered Found</div>"
                return HttpResponse(html)

            messages.error(request,"Invalid data")
            return redirect(request.META.HTTP_REFERER)

    except:

        messages.error(request,"Method not allowed")
        return redirect(request.META.HTTP_REFERER)

####################################################################
# Name - search_DoctorNewSOLooser_by_name_admin                    #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_DoctorNewSOLooser_by_name_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            if q is not None:
                try:
                    results = Doctor_ServiceOffered_New.objects.filter(WorL__iexact='looser',
                                                                       name__icontains=q).order_by('name')
                except:
                    results = None
                if results:
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

                    html = render_to_string('admin/master_data_management/DoctorNewSOLooser_search_by_name.html',
                                            {'tab': 'data', 'crosal': 'DoctorNewSO',
                                             'search_data': q, 'DoctorNewSOLooser_obj': results})
                    return HttpResponse(html)

                html = "<div class=table-responsive table_modify_for_all>No Service Offered Looser Found with this name</div>"
                return HttpResponse(html)

            messages.error(request, "Looser ID Not Provided")
            return redirect(request.META.HTTP_REFERER)
        else:
            messages.error(request, "Method Not Allowed")
            return redirect(request.META.HTTP_REFERER)

    except Exception as e:
        messages.error(request, e)
        return redirect(request.META.HTTP_REFERER)


####################################################################
# Name - search_DoctorNewSPE_by_name_admin                         #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_DoctorNewSPE_by_name_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            if q is not None :
                try :
                    results = Doctor_Speciality_New.objects.filter(WorL__iexact='winner',name__icontains=q).order_by('name')
                except:
                    results= None
                if results :
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

                    html = render_to_string('admin/master_data_management/DoctorNewSPE_search_by_name.html',
                                            {'tab': 'data', 'crosal': 'DoctorNewSPE',
                                            'search_data':q,'DoctorNewSPE_obj':results})
                    return HttpResponse(html)

                html = "<div class=table-responsive table_modify_for_all>No Speciality Found</div>"
                return HttpResponse(html)

            messages.error(request,"Invalid data")
            return redirect(request.META.HTTP_REFERER)

    except:

        messages.error(request,"Method not allowed")
        return redirect(request.META.HTTP_REFERER)


####################################################################
# Name - deleted_schedules_with_sponsored_ranks                    #
# Owner - Nishank Gupta                                           #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def doctor_deleted_schedules_with_sponsored_ranks(request):
    try:

        del_sch_mainlist = []
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                del_sch_mainlist = Doctor_Schedule_Delete_Notification.objects.filter(
                    doctor__name__icontains=q
                )

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
            html = render_to_string('admin/doctor_management/deleted_schedules_with_sponsored_ranks.html',
                                    {'tab': 'data', 'crosal': 'doctorbymanage', 'del_sch_mainlist': del_sch_mainlist,
                                     'search_data': q,})
            return HttpResponse(html)
    except Exception as e:

        raise Http404
