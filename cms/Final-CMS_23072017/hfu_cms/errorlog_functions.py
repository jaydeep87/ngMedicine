from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from hfu_cms.models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse


####################################################################
# Name - doctor_error_logs                                         #
# By- Nishank                                                      #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@require_GET
def doctor_error_logs(request):
    try:
        log_list = None
        log_list = pub_unpub_error_log.objects.filter(model_type='doctor').order_by('date_n_time')
        if len(log_list) == 0:
            messages.error(request, "No Error Log For Doctors found")
            return render(request, 'publisher/doctor/doctor-error-logs.html',
                          {'tab_listing': 'doctor-listing', 'tab': 'doctor-listing',
                           'log_list':None})
        else:
            paginator = Paginator(log_list, 50)
            page = request.GET.get('page')
            try:
                log_list = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                log_list = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                log_list = paginator.page(paginator.num_pages)
            return render(request, 'publisher/doctor/doctor-error-logs.html',
                          {'tab_listing': 'doctor-listing', 'tab': 'doctor-listing',
                           'log_list': log_list})
    except Exception as e:
        #print e
        raise Http404

####################################################################
# Name - organisation_error_logs                                   #
# By- Nishank                                                      #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@require_GET
def organisation_error_logs(request):
    try:
        log_list = None
        log_list = pub_unpub_error_log.objects.filter(model_type='organisation').order_by('date_n_time')

        if len(log_list) == 0:
            messages.error(request, "No Error Log For Organisation found")
            return render(request, 'publisher/organisation/organisation-error-logs.html',
                          {'tab_listing': 'organisation-listing', 'tab': 'organisation-listing',
                           'log_list': None})

        else:
            paginator = Paginator(log_list, 50)
            page = request.GET.get('page')
            try:
                log_list = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                log_list = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                log_list = paginator.page(paginator.num_pages)
            return render(request, 'publisher/organisation/organisation-error-logs.html',
                          {'tab_listing': 'organisation-listing', 'tab': 'organisation-listing',
                           'log_list': log_list})
    except Exception as e:
        #print e
        raise Http404

####################################################################
# Name - lab_error_logs                                            #
# By- Nishank                                                      #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@require_GET
def lab_error_logs(request):
    try:
        log_list = None
        log_list = pub_unpub_error_log.objects.filter(model_type='lab').order_by('date_n_time')

        if len(log_list) == 0:
            messages.error(request, "No Error Log For Lab found")
            return render(request, 'publisher/lab/lab-error-logs.html',
                          {'tab_listing': 'lab-listing', 'tab': 'lab-listing',
                           'log_list': None})
        else:
            paginator = Paginator(log_list, 50)
            page = request.GET.get('page')
            try:
                log_list = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                log_list = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                log_list = paginator.page(paginator.num_pages)
            return render(request, 'publisher/lab/lab-error-logs.html',
                          {'tab_listing': 'lab-listing', 'tab': 'lab-listing',
                           'log_list': log_list})
    except Exception as e:
        #print e
        raise Http404

####################################################################
# Name - bloodbank_error_logs                                      #
# By- Nishank                                                      #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@require_GET
def bloodbank_error_logs(request):
    try:
        log_list = None
        log_list = pub_unpub_error_log.objects.filter(model_type='bloodbank').order_by('date_n_time')

        if len(log_list) == 0:
            messages.error(request, "No Error Log For bloodbank found")
            return render(request, 'publisher/bloodbank/bloodbank-error-logs.html',
                          {'tab_listing': 'bloodbank-listing', 'tab': 'bloodbank-listing',
                           'log_list': None})
        else:
            paginator = Paginator(log_list, 50)
            page = request.GET.get('page')
            try:
                log_list = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                log_list = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                log_list = paginator.page(paginator.num_pages)
            return render(request, 'publisher/bloodbank/bloodbank-error-logs.html',
                          {'tab_listing': 'bloodbank-listing', 'tab': 'bloodbank-listing',
                           'log_list': log_list})
    except Exception as e:
        #print e
        raise Http404

####################################################################
# Name - ambulance_error_logs                                      #
# By- Nishank                                                      #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@require_GET
def ambulance_error_logs(request):
    try:
        log_list = None
        log_list = pub_unpub_error_log.objects.filter(model_type='ambulance').order_by('date_n_time')

        if len(log_list) == 0:
            messages.error(request, "No Error Log For ambulance found")
            return render(request, 'publisher/ambulance/ambulance-error-logs.html',
                          {'tab_listing': 'ambulance-listing', 'tab': 'ambulance-listing',
                           'log_list': None})
        else:
            paginator = Paginator(log_list, 50)
            page = request.GET.get('page')
            try:
                log_list = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                log_list = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                log_list = paginator.page(paginator.num_pages)
            return render(request, 'publisher/ambulance/ambulance-error-logs.html',
                          {'tab_listing': 'ambulance-listing', 'tab': 'ambulance-listing',
                           'log_list': log_list})
    except Exception as e:
        #print e
        raise Http404

####################################################################
# Name - pharmacy_error_logs                                       #
# By- Nishank                                                      #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@require_GET
def pharmacy_error_logs(request):
    try:
        log_list = None
        log_list = pub_unpub_error_log.objects.filter(model_type='pharmacy').order_by('date_n_time')
        if len(log_list) == 0:
            messages.error(request, "No Error Log For pharmacy found")
            return render(request, 'publisher/pharmacy/pharmacy-error-logs.html',
                          {'tab_listing': 'pharmacy-listing', 'tab': 'pharmacy-listing',
                           'log_list': None})
        else:
            paginator = Paginator(log_list, 50)
            page = request.GET.get('page')
            try:
                log_list = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                log_list = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                log_list = paginator.page(paginator.num_pages)
            return render(request, 'publisher/pharmacy/pharmacy-error-logs.html',
                          {'tab_listing': 'pharmacy-listing', 'tab': 'pharmacy-listing',
                           'log_list': log_list})
    except Exception as e:
        #print e
        raise Http404

####################################################################
# Name - rehab_error_logs                                          #
# By- Nishank                                                      #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@require_GET
def rehab_error_logs(request):
    try:
        log_list = None
        log_list = pub_unpub_error_log.objects.filter(model_type='rehabitation').order_by('date_n_time')

        if len(log_list) == 0:
            messages.error(request, "No Error Log For rehab found")
            return render(request, 'publisher/rehab/rehab-error-logs.html',
                          {'tab_listing': 'rehab-listing', 'tab': 'rehab-listing',
                           'log_list': None})
        else:
            paginator = Paginator(log_list, 50)
            page = request.GET.get('page')
            try:
                log_list = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                log_list = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                log_list = paginator.page(paginator.num_pages)
            return render(request, 'publisher/rehab/rehab-error-logs.html',
                          {'tab_listing': 'rehab-listing', 'tab': 'rehab-listing',
                           'log_list': log_list})
    except Exception as e:
        #print e
        raise Http404

####################################################################
# Name - disease_error_logs                                        #
# By- Nishank                                                      #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@require_GET
def disease_error_logs(request):
    try:
        log_list = None
        log_list = pub_unpub_error_log.objects.filter(model_type='disease').order_by('date_n_time')

        if len(log_list) == 0:
            messages.error(request, "No Error Log For disease found")
            return render(request, 'publisher/disease/disease-error-logs.html',
                          {'tab_listing': 'disease-listing', 'tab': 'disease-listing',
                           'log_list': None})
        else:
            paginator = Paginator(log_list, 50)
            page = request.GET.get('page')
            try:
                log_list = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                log_list = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                log_list = paginator.page(paginator.num_pages)
            return render(request, 'publisher/disease/disease-error-logs.html',
                          {'tab_listing': 'disease-listing', 'tab': 'disease-listing',
                           'log_list': log_list})
    except Exception as e:
        #print e
        raise Http404

####################################################################
# Name - symptoms_error_logs                                       #
# By- Nishank                                                      #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@require_GET
def symptoms_error_logs(request):
    try:
        log_list = None
        log_list = pub_unpub_error_log.objects.filter(model_type='symptom').order_by('date_n_time')

        if len(log_list) == 0:
            messages.error(request, "No Error Log For symptoms found")
            return render(request, 'publisher/symptoms/symptoms-error-logs.html',
                          {'tab_listing': 'symptoms-listing', 'tab': 'symptoms-listing',
                           'log_list': None})
        else:
            paginator = Paginator(log_list, 50)
            page = request.GET.get('page')
            try:
                log_list = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                log_list = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                log_list = paginator.page(paginator.num_pages)
            return render(request, 'publisher/symptoms/symptoms-error-logs.html',
                          {'tab_listing': 'symptoms-listing', 'tab': 'symptoms-listing',
                           'log_list': log_list})
    except Exception as e:
        #print e
        raise Http404

####################################################################
# Name - Serviceplan_error_logs                                    #
# By- Nishank                                                      #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@require_GET
def Serviceplan_error_logs(request):
    try:
        log_list = None
        log_list = pub_unpub_error_log.objects.filter(model_type='services').order_by('date_n_time')

        if len(log_list) == 0:
            messages.error(request, "No Error Log For Service Plan found")
            return render(request, 'publisher/homeplan/service-plan-common-error-logs.html',
                          {'tab_listing': 'serviceplan-listing', 'tab': 'serviceplan-listing',
                           'log_list': None})
        else:
            paginator = Paginator(log_list, 50)
            page = request.GET.get('page')
            try:
                log_list = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                log_list = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                log_list = paginator.page(paginator.num_pages)
            return render(request, 'publisher/homeplan/service-plan-common-error-logs.html',
                          {'tab_listing': 'serviceplan-listing', 'tab': 'serviceplan-listing',
                           'log_list': log_list})
    except Exception as e:
        #print e
        raise Http404

####################################################################
# Name - newsfeed_error_logs                                       #
# By- Nishank                                                      #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@require_GET
def newsfeed_error_logs(request):
    try:
        log_list = None
        log_list = pub_unpub_error_log.objects.filter(model_type='newsfeed').order_by('date_n_time')
        if len(log_list) == 0:
            messages.error(request, "No Error Log For newsfeed found")
            return render(request, 'news/publisher/newsfeed-error-logs.html',
                          {'tab_listing': 'newsfeed-listing', 'tab': 'newsfeed-listing',
                           'log_list': None})
        else:
            paginator = Paginator(log_list, 50)
            page = request.GET.get('page')
            try:
                log_list = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                log_list = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                log_list = paginator.page(paginator.num_pages)
            return render(request, 'news/publisher/newsfeed-error-logs.html',
                          {'tab_listing': 'newsfeed-listing', 'tab': 'newsfeed-listing',
                           'log_list': log_list})
    except Exception as e:
        #print e
        raise Http404

####################################################################
# Name - delete_error_log                                          #
# By- Nishank                                                      #
# Review by - ?                                                    #
# For Publisher view                                               #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@require_GET
def delete_error_log(request,log_id=None):
    try:
        if log_id:
            log = None
            log = pub_unpub_error_log.objects.get(id = int(log_id))
            if log:
                log.delete()
                messages.success(request, 'Error Log deleted successfully')
                return HttpResponseRedirect(request.META['HTTP_REFERER'])
            else:
                messages.error(request, 'Error Record could not be founs')
                return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request,'No id received')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    except Exception as e:
        #print e
        raise Http404