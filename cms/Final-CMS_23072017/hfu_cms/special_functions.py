from django.http.response import HttpResponse, HttpResponseRedirect, Http404
from hfu_cms.models import *
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.core.urlresolvers import reverse
import elasticsearch_client
from hfu_cms.data_publisher import __doctor_data_creation,__organisation_data_creation
from django.shortcuts import redirect,render

####################################################################
# Name - doctor_set_unpublish                                      #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
#@user_passes_test(lambda u: u.is_superuser)
def doctor_set_unpublish(request):
    try:
       doc_list = Doctor.objects.filter(publish=True,current_user_id=request.user.id)
       for doc in doc_list:
           doc.publish = False
           doc.stage_id = 4
           doc.save()
       messages.success(request,'stage to 4 and publish to False - for DOCTOR DONE' )
       return HttpResponseRedirect(reverse('users-dashboard'))
    except Exception as e:
        #print e
        messages.error(request, "Model Not Provided")
        return HttpResponseRedirect(reverse('users-dashboard'))

####################################################################
# Name - organisation_set_unpublish                                #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
# @user_passes_test(lambda u: u.is_superuser)
def organisation_set_unpublish(request):
    try:
        OrganisationName.objects.filter(current_user_id=request.user.id,publish=True).update(stage_id=4,publish=False)
        messages.success(request, 'stage to 4 and publish to False - for ORGANISATION DONE')
        return HttpResponseRedirect(reverse('users-dashboard'))
    except Exception as e:
        #print e
        messages.error(request, "Model Not Provided")
        return HttpResponseRedirect(reverse('users-dashboard'))

####################################################################
# Name - ambulance_set_unpublish                                   #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
#@user_passes_test(lambda u: u.is_superuser)
def ambulance_set_unpublish(request):
    try:
       a_list = Ambulance.objects.filter(publish=True,current_user_id=request.user.id)
       for a in a_list:
           a.publish = False
           a.stage_id = 4
           a.save()
       messages.success(request,'stage to 4 and publish to False - for AMBULANCE DONE' )
       return HttpResponseRedirect(reverse('users-dashboard'))
    except Exception as e:
        #print e
        messages.error(request, "Model Not Provided")
        return HttpResponseRedirect(reverse('users-dashboard'))

####################################################################
# Name - dietitian_set_unpublish                                   #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
#@user_passes_test(lambda u: u.is_superuser)
def dietitian_set_unpublish(request):
    try:
       a_list = Dietitian.objects.filter(publish=True,current_user_id=request.user.id)
       for a in a_list:
           a.publish = False
           a.stage_id = 4
           a.save()
       messages.success(request,'stage to 4 and publish to False - for Dietitian DONE' )
       return HttpResponseRedirect(reverse('users-dashboard'))
    except Exception as e:
        #print e
        messages.error(request, "Model Not Provided")
        return HttpResponseRedirect(reverse('users-dashboard'))

####################################################################
# Name - Publish Locality master                                   #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def publish_locality_master(request):
    try:
        Locality_obj = Locality.objects.filter(delete=False)
        for locality in Locality_obj:
            data = {}
            data['id'] = locality.id
            data['name'] = locality.name
            data['name'].strip()
            data['city_id'] = locality.city_id
            response = elasticsearch_client.index_data('master', 'locality', locality.id, data)
            if response:
                pass
            else:
                messages.error(request, "Error while Publishing Locality master")
                return HttpResponseRedirect(reverse('users-dashboard'))
        messages.success(request,'SUCCESSFULLY Published Locality master' )
        return HttpResponseRedirect(reverse('users-dashboard'))
    except Exception as e:
        #print e
        messages.error(request, "Error while Publishing Locality master")
        return HttpResponseRedirect(reverse('users-dashboard'))

####################################################################
# Name - Publish Speciality master                                 #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def publish_speciality_master(request):
    try:
        Speciality_obj = Speciality.objects.filter(delete=False)
        for speciality in Speciality_obj:
            data = {}
            data['id'] = speciality.id
            data['category_id'] = speciality.category_id
            data['name'] = speciality.name
            data['name'].strip()
            response = elasticsearch_client.index_data('master', 'speciality', speciality.id, data)
            if response:
                pass
            else:
                print "Error while Publishing Speciality master" , speciality.id
                messages.error(request, "Error while Publishing Speciality master")
                return HttpResponseRedirect(reverse('users-dashboard'))
        messages.success(request,'SUCCESSFULLY Published Speciality master' )
        return HttpResponseRedirect(reverse('users-dashboard'))
    except Exception as e:
        #print e
        messages.error(request, "Error while Publishing Speciality master")
        return HttpResponseRedirect(reverse('users-dashboard'))

####################################################################
# Name - unpublish_organisation_for_publisher                      #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def unpublish_organisation_for_publisher(request):
    try:
        user_management_obj =  UserManagement.objects.get(user_id = request.user.id)
        if user_management_obj.is_publisher == True:
            org_obj = OrganisationName.objects.filter(is_disable=False,current_user_id=request.user.id,stage_id=5)
            for org in org_obj:
                id = org.id
                response = elasticsearch_client.delete_document('global','organisation', id)
                if response:
                    org.publish=False
                    org.stage_id=4
                    org.save()
                else:
                    print "Error while Un-Publishing Organisation" , org.id
                    messages.error(request, "Error while Un-Publishing Organisations"+str(org.id))
                    return HttpResponseRedirect(reverse('users-dashboard'))
            messages.success(request,'SUCCESSFULLY Un-Published Organisations' )
            return HttpResponseRedirect(reverse('users-dashboard'))
        else:
            messages.error(request,"Current user is NOT PUBLISHER")
            return HttpResponseRedirect(reverse('users-dashboard'))
    except Exception as e:
        #print e
        messages.error(request, e)
        return HttpResponseRedirect(reverse('users-dashboard'))

####################################################################
# Name - unpublish_doctor_for_publisher                            #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def unpublish_doctor_for_publisher(request):
    try:
        user_management_obj =  UserManagement.objects.get(user_id = request.user.id)
        if user_management_obj.is_publisher == True:
            doc_obj = Doctor.objects.filter(is_disable=False,current_user_id=request.user.id,stage_id=5)
            for doc in doc_obj:
                id = doc.id
                response = elasticsearch_client.delete_document('global', 'doctor', id)
                if response:
                    doc.publish=False
                    doc.stage_id=4
                    doc.save()
                else:
                    print "Error while Un-Publishing Doctor" , doc.id
                    messages.error(request, "Error while Un-Publishing Doctors"+str(doc.id))
                    return HttpResponseRedirect(reverse('users-dashboard'))
            messages.success(request,'SUCCESSFULLY Un-Published Doctors' )
            return HttpResponseRedirect(reverse('users-dashboard'))
        else:
            messages.error(request,"Current user is NOT PUBLISHER")
            return HttpResponseRedirect(reverse('users-dashboard'))
    except Exception as e:
        #print e
        messages.error(request, e)
        return HttpResponseRedirect(reverse('users-dashboard'))

####################################################################
# Name - publish_for_publisher                                     #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def publish_for_publisher(request):
    try:
        user_management_obj =  UserManagement.objects.get(user_id = request.user.id)
        if user_management_obj.is_publisher == True:
            doc_obj = Doctor.objects.filter(is_disable=False,current_user_id=request.user.id,stage_id=4)
            for doc in doc_obj :
                if doc.is_disable == False:
                    data = __doctor_data_creation(doc.id)
                    response = elasticsearch_client.index_data("global", 'doctor', doc.id, data)
                    if response:
                        doc.publish=True,
                        doc.stage_id=5
                        doc.save()
                        #print(" is indexed: " + str(doc.id))
                    else:
                        #print("Failed To" + ": " + str(doc.id))
                        pass

            org_obj = OrganisationName.objects.filter(is_disable=False, current_user_id=request.user.id, stage_id=4)
            for org in org_obj:
                if org.is_disable == False:
                    data = __organisation_data_creation(org.id)
                    response = elasticsearch_client.index_data("global", 'organisation', org.id, data)
                    if response:
                        org.publish = True,
                        org.stage_id = 5
                        org.save()
                        #print(" is indexed: " + str(org.id))
                    else:
                        #print("Failed To " + ": " + str(org.id))
                        pass

            messages.success(request,'SUCCESSFULLY Published Doctors and Organisation' )
            return HttpResponseRedirect(reverse('users-dashboard'))
        else:
            messages.error(request,"Current user is NOT PUBLISHER")
            return HttpResponseRedirect(reverse('users-dashboard'))
    except Exception as e:
        #print e
        messages.error(request, e)
        return HttpResponseRedirect(reverse('users-dashboard'))

import json
####################################################################
# Name - publish_SO_master                                         #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def publish_SO_master(request):
    try:
        user =  User.objects.get(id = request.user.id)
        if user.is_superuser == True:
            Service_Offred_obj = Service_Offred.objects.filter(delete=False)
            for service_offer in Service_Offred_obj:
                data = {}
                data['id'] = service_offer.id
                data['category_id'] = service_offer.category_id
                data['name'] = service_offer.name
                data['name'].strip()
                data['name_with_category'] = service_offer.name.strip() + "(" + service_offer.category.name.strip() + ")"
                response = elasticsearch_client.index_data('globalmaster', 'service_offered', service_offer.id, data)
                response = elasticsearch_client.index_data('master', 'service_offered', service_offer.id, data)
                if response:
                    pass
                    #print(" is indexed: " + str(data['id']))
                    #print json.dumps(data)
                else:
                    pass
                    #print("Failed To : " + str(data['id']))

            messages.success(request,'SUCCESSFULLY Published SO MASTER' )
            return HttpResponseRedirect(reverse('users-dashboard'))
        else:
            messages.error(request,"Current user is NOT ADMIN")
            return HttpResponseRedirect(reverse('users-dashboard'))
    except Exception as e:
        #print e
        messages.error(request, e)
        return HttpResponseRedirect(reverse('users-dashboard'))

####################################################################
# Name - publish_SPE_master                                        #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def publish_SPE_master(request):
    try:
        user =  User.objects.get(id = request.user.id)
        if user.is_superuser == True:
            Speciality_obj = Speciality.objects.filter(delete=False)
            for speciality in Speciality_obj:
                data = {}
                data['id'] = speciality.id
                data['category_id'] = speciality.category_id
                data['name'] = speciality.name
                data['name'].strip()
                data['name_with_category'] = speciality.name.strip() + "(" + speciality.category.name.strip() + ")"
                response = elasticsearch_client.index_data('globalmaster', 'speciality', speciality.id, data)
                response = elasticsearch_client.index_data('master', 'speciality', speciality.id, data)
                if response:
                    pass
                    #print(" is indexed: " + str(data['id']))
                else:
                    pass
                    #print("Failed To "  + str(data['id']))

            messages.success(request,'SUCCESSFULLY Published SO MASTER' )
            return HttpResponseRedirect(reverse('users-dashboard'))
        else:
            messages.error(request,"Current user is NOT ADMIN")
            return HttpResponseRedirect(reverse('users-dashboard'))
    except Exception as e:
        #print e
        messages.error(request, e)
        return HttpResponseRedirect(reverse('users-dashboard'))

####################################################################
# Name - disease_search_master_attach_disease_with_doctors         #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def disease_search_master_attach_disease_with_doctors(request):
    try:
        errorlist = []
        disease_search_master_all  = Disease_search_master.objects.all().order_by('id')
        for disease in disease_search_master_all:
            categories_doc = disease.doctor_categories.strip()
            #print categories_doc," >>  ",disease.id
            if categories_doc != None and categories_doc != [] and categories_doc != '':
                cat_list = categories_doc.strip()
                cat_list = cat_list.split(',')

                for i in cat_list:
                    if i and i != '' and i != ' ':
                        category = Category.objects.get(id=int(i))
                        print 'associating disease ',disease.name, ' id = ', disease.id,' with Category ',  category.name, ' id = ', category.id

                        cat_doc_list = Doctor.objects.filter(category_id=int(i.strip()))  # TODO 2 is_disable = False
                        #print cat_doc_list.count(),int(i.strip())
                        for j in cat_doc_list:
                            try:
                                if j.associated_diseases == '' or j.associated_diseases == None or j.associated_diseases == []:
                                    j.associated_diseases = str(disease.id)
                                else:
                                    check = j.associated_diseases.strip()
                                    check_list = check.split(',')
                                    if str(disease.id) not in check_list:
                                        j.associated_diseases = j.associated_diseases + ',' + str(disease.id)
                                j.save()
                                #print "saved ",j.id
                                print "disease id = " , disease.id,"DISEASE NAME = ", disease.name
                            except:
                                errorlist.append([disease.name,disease.id,category.name,category.id,j.name,j.id])
                    else:
                        pass
                        #print"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
                        #print "disease id= ",disease.id
                        #print"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
        print errorlist
        messages.success(request, "Disease Associated with Doctors (Via Category) Successfully")
        return redirect('disease_search_master_data_page')
    except Exception as e:
        messages.error(request, e)
        return redirect('disease_search_master_data_page')


####################################################################
# Name - symptoms_search_master_attach_symptoms_with_doctors       #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def symptoms_search_master_attach_symptoms_with_doctors(request):
    try:
        errorlist = []
        symptom_search_master_all  = Symptoms_search_master.objects.all().order_by('id')
        for symptom in symptom_search_master_all:
            categories_doc = symptom.doctor_categories.strip()
            #print categories_doc," >>  ",disease.id
            if categories_doc != None and categories_doc != [] and categories_doc != '':
                cat_list = categories_doc.strip()
                cat_list = cat_list.split(',')

                for i in cat_list:
                    if i and i != '' and i != ' ':
                        category = Category.objects.get(id=int(i))
                        print 'associating ', symptom.name, ' id = ', symptom.id, ' with ', category.name, ' id = ', category.id
                        cat_doc_list = Doctor.objects.filter(category_id=int(i.strip()))  # TODO 2 is_disable = False
                        #print cat_doc_list.count(),int(i.strip())
                        for j in cat_doc_list:
                            try:
                                if j.associated_symptoms == '' or j.associated_symptoms == None or j.associated_symptoms == []:
                                    j.associated_symptoms = str(symptom.id)
                                else:
                                    check = j.associated_symptoms.strip()
                                    check_list = check.split(',')
                                    if str(symptom.id) not in check_list:
                                        j.associated_symptoms = j.associated_symptoms + ',' + str(symptom.id)
                                j.save()
                                #print "saved ",j.id
                                print "symptom id = " , symptom.id, "symptom name = ",symptom.name
                            except:
                                errorlist.append([symptom.name,symptom.id,category.name,category.id,j.name,j.id])
                    else:
                        pass
                        #print"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
                        #print "disease id= ",symptom.id
                        #print"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
        print errorlist
        messages.success(request, "Symptoms Associated with Doctors (Via Category) Successfully")
        return redirect('symptoms_search_master_data_page')
    except Exception as e:
        messages.error(request, e)
        return redirect('symptoms_search_master_data_page')

######################################################################
# Name - symptoms_search_master_attach_symptoms_with_doctors_in part #
# By - Nishank                                                       #
######################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def symptoms_search_master_attach_symptoms_with_doctors_in_part(request):
    try:
        errorlist = []
        symptom_search_master_all = Symptoms_search_master.objects.all()[:50]
        for symptom in symptom_search_master_all:
            categories_doc = symptom.doctor_categories.strip()
            print categories_doc," >>  ",symptom.id
            print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
            if categories_doc != None and categories_doc != [] and categories_doc != '':
                cat_list = categories_doc.strip()
                cat_list = cat_list.split(',')

                for i in cat_list:
                    if i and i != '' and i != ' ':
                        category = Category.objects.get(id=int(i))
                        print 'associating ', symptom.name, ' id = ', symptom.id, ' with ', category.name, ' id = ', category.id
                        cat_doc_list = Doctor.objects.filter(
                            category_id=int(i.strip()))  # TODO 2 is_disable = False
                        # print cat_doc_list.count(),int(i.strip())
                        for j in cat_doc_list:
                            try:
                                if j.associated_symptoms == '' or j.associated_symptoms == None or j.associated_symptoms == []:
                                    j.associated_symptoms = str(symptom.id)
                                else:
                                    check = j.associated_symptoms.strip()
                                    check_list = check.split(',')
                                    if str(symptom.id) not in check_list:
                                        j.associated_symptoms = j.associated_symptoms + ',' + str(symptom.id)
                                j.save()
                                # print "saved ",j.id
                                print "symptom id = ", symptom.id, "symptom name = ", symptom.name
                            except:
                                errorlist.append(
                                    [symptom.name, symptom.id, category.name, category.id, j.name, j.id])
                    else:
                        pass
                        # print"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
                        # print "disease id= ",symptom.id
                        # print"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
        print errorlist
        messages.success(request, "Symptoms Associated with Doctors (Via Category) Successfully")
        return redirect('symptoms_search_master_data_page')
    except Exception as e:
        messages.error(request, e)
        return redirect('symptoms_search_master_data_page')


####################################################################
# Name - rem_decimal_disease_search_master                         #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def rem_decimal_disease_search_master(request):
    disease_search_master_all  = Disease_search_master.objects.all()
    for disease in disease_search_master_all:
        if len(disease.doctor_categories) == 3 or len(disease.doctor_categories) == 4:
            if '.' in disease.doctor_categories:
                #print "then = ", disease.doctor_categories
                temp11 = disease.doctor_categories.split('.')
                for i in temp11:
                    if i != '0':
                        disease.doctor_categories = i
                        disease.save()
                #print "now = ", disease.doctor_categories
                #print "----------------------------------"
        else:
            pass

    messages.success(request, "Decimal Successfully removed From disease search master ")
    return redirect('disease_search_master_data_page')


####################################################################
# Name - rem_decimal_symptoms_search_master                        #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def rem_decimal_symptoms_search_master(request):
    symptoms_search_master_all  = Symptoms_search_master.objects.all()
    for symptoms in symptoms_search_master_all:
        if len(symptoms.doctor_categories) == 3 or len(symptoms.doctor_categories) == 4:
            if '.' in symptoms.doctor_categories:
                #print "then = ", symptoms.doctor_categories
                temp11 = symptoms.doctor_categories.split('.')
                for i in temp11:
                    if i != '0':
                        symptoms.doctor_categories = i
                        symptoms.save()
                #print "now = ", symptoms.doctor_categories
                #print "----------------------------------"
        else:
            pass

    messages.success(request, "Decimal Successfully removed From symptoms search master")
    return redirect('symptoms_search_master_data_page')


####################################################################
# Name - publish_diease_search_master                              #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def publish_diease_search_master(request):
    try:
        user =  User.objects.get(id = request.user.id)
        if user.is_superuser == True:
            diseases = Disease_search_master.objects.filter(delete=False)
            for dis in diseases:
                data = {}
                data['id'] = dis.id
                data['name'] = dis.name
                data['name'].strip()
                # if dis.doctor_categories and dis.doctor_categories != '' and dis.doctor_categories != []:
                #     mptylist = []
                #     alist =  []
                #     alist = dis.doctor_categories.split(',')
                #     for i in alist:
                #         if i != '' and i != ' ':
                #             getcat = Category.objects.get(id = int(i ))
                #             mptylist.append({"id":int(i),"name":getcat.name.strip()})
                #     data['doctor_categories'] = mptylist
                # else:
                #     data['doctor_categories'] = []
                response = elasticsearch_client.index_data('globalmaster', 'disease', dis.id, data)
                response = elasticsearch_client.index_data('master', 'disease', dis.id, data)
                if response:
                    pass
                    #print(" is indexed: " + str(data['id']))
                else:
                    pass
                    #print("Failed To "  + str(data['id']))

            messages.success(request,'SUCCESSFULLY Published Disease Search Master' )
            return HttpResponseRedirect(reverse('users-dashboard'))
        else:
            messages.error(request,"Current user is NOT ADMIN")
            return HttpResponseRedirect(reverse('users-dashboard'))
    except Exception as e:
        #print e
        messages.error(request, e)
        return HttpResponseRedirect(reverse('users-dashboard'))

####################################################################
# Name - publish_symptom_search_master                             #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def publish_symptom_search_master(request):
    try:
        user =  User.objects.get(id = request.user.id)
        if user.is_superuser == True:
            symps = Symptoms_search_master.objects.filter(delete=False)
            for sy in symps:
                data = {}
                data['id'] = sy.id
                data['name'] = sy.name
                data['name'].strip()

                response = elasticsearch_client.index_data('globalmaster', 'symptom', sy.id, data)
                response = elasticsearch_client.index_data('master', 'symptom', sy.id, data)
                if response:
                    pass
                    #print(" is indexed: " + str(data['id']))
                else:
                    pass
                    #print("Failed To "  + str(data['id']))

            messages.success(request,'SUCCESSFULLY Published Symptom Search Master' )
            return HttpResponseRedirect(reverse('users-dashboard'))
        else:
            messages.error(request,"Current user is NOT ADMIN")
            return HttpResponseRedirect(reverse('users-dashboard'))
    except Exception as e:
        #print e
        messages.error(request, e)
        return HttpResponseRedirect(reverse('users-dashboard'))
####################################################################
# Name - unpublish_xyz                                             #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def unpublish_xyz(request):
    try:
        response1 = elasticsearch_client.delete_document('globalmaster', 'labdepartments', 8)
        response2 = elasticsearch_client.delete_document('master', 'labdepartments', 8)
        print response1,"   ",response2
        if response1 and response2:
           print "Unpublished"
           messages.success(request, "Unpublished")
           return HttpResponseRedirect(reverse('users-dashboard'))
        else:
            print "Error while Un-Publishing"
            messages.error(request,'"Error while Un-Publishing"')
            return HttpResponseRedirect(reverse('users-dashboard'))

    except Exception as e:
        #print e
        messages.error(request, e)
        return HttpResponseRedirect(reverse('users-dashboard'))

####################################################################
# Name - abasedir                                                  #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def abasedir(request):
    from django.conf import settings
    return HttpResponse(settings.BASE_DIR)

####################################################################
# Name - makeFirstLetterCapital                                    #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def makeFirstLetterCapital(request,model=None):
    try:
        name = None
        if model:
            count = 0
            if model.lower() == 'category':
                object_list = Category.objects.all()
                for i in object_list:
                    name = i.name
                    name = name.title()
                    i.name = name
                    i.save()
                    count += 1
                    #print i.name
                #print count
                messages.success(request, "Title function applied to"+' '+str(count)+" name entries for model"+" "+model )
                return HttpResponseRedirect(reverse('users-dashboard'))
        else:
            messages.error(request,"Model Not Provided")
            return HttpResponseRedirect(reverse('users-dashboard'))
    except Exception as e:
        #print e
        messages.error(request, "Model Not Provided")
        return HttpResponseRedirect(reverse('users-dashboard'))




####################################################################
# Name - test_disease_user_change                                  #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def test_disease_user_change(request):
    try:
        d_obj = None
        d_obj = Disease.objects.get(current_user_id=12,id=449 )
        if d_obj:
            d_obj.current_user_id = 113
            d_obj.save()
            messages.success(request, "Assigned Disease 449" )
            return HttpResponseRedirect(reverse('users-dashboard'))
        else:
            messages.error(request, "Obj Not found")
            return HttpResponseRedirect(reverse('users-dashboard'))

    except Exception as e:
        #print e
        messages.error(request, "Not assigned")
        return HttpResponseRedirect(reverse('users-dashboard'))

####################################################################
# Name - assign_all_disease_to_mrinalini                           #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def assign_all_disease_to_mrinalini(request):
    try:
        d_obj = None
        d_obj = Disease.objects.filter(current_user_id=12)
        if d_obj:
            d_obj.update(current_user_id = 113)
            messages.success(request, "All transferred successfully")
            return HttpResponseRedirect(reverse('users-dashboard'))
        else:
            messages.error(request, "Objects Not found")
            return HttpResponseRedirect(reverse('users-dashboard'))

    except Exception as e:
        #print e
        messages.error(request, "Not Transferred")
        return HttpResponseRedirect(reverse('users-dashboard'))

####################################################################
# Name - copy_department_associate_to_attach                       #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def copy_department_associate_to_attach(request):
    try:
        attach = AttachWithDoctor.objects.all().order_by('id')
        rerec = 0
        for i in attach:
            f = AssociateDoctorWithOrganization.objects.filter(organisation_id = i.organisation_id, doctor_id = i.doctor_id)
            if len(f) > 0:
                rerec += 1

                strjoin = ''
                count = 0
                for j in f:
                    count += 1
                    if count == 1:
                        strjoin =  str(j.department_id)
                    else:
                        strjoin = strjoin + ',' + str(j.department_id)
                if i.department == None or i.department == '' or i.department == ' ':
                    i.department = strjoin
                else:
                    buffer__list = []
                    pre_list = i.department.split(',')
                    new_list = strjoin.split(',')
                    buffer__list = pre_list
                    for el in new_list:
                        if el not in buffer__list:
                            if el != '' and el !=  ' ':
                                buffer__list.append(el)
                    i.department = ','.join(buffer__list)
                i.save()
                print "Row------SAVED----> ", rerec
        messages.success(request, "Done")
        return HttpResponseRedirect(reverse('users-dashboard'))
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(reverse('users-dashboard'))


####################################################################
# Name - unpublish_live_docs                                       #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def unpublish_live_docs(request):
    try:
        for ldoc in range(200000,200102):
            try:
                response = elasticsearch_client.delete_document('global', "doctor", ldoc)
                if response:
                    print ldoc, " Successfully Un-Published"
            except:
                print ldoc ," NOT UNPUBLISHED"
        messages.success(request, "Done")
        return HttpResponseRedirect(reverse('users-dashboard'))
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(reverse('users-dashboard'))


####################################################################
# Name - truncate                                                  #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def truncate(request):
    try:
        ldcws = Live_Doctor_Commonworkschedule.objects.all()
        for sch in ldcws:
            sch.delete()
        ld = Live_Doctor.objects.all()
        for lidoc in ld:
            lidoc.delete()
        ldedu = Live_Doctor_Education.objects.all()
        for edu in ldedu:
            edu.delete()
        ldexp = Live_Doctor_Experience.objects.all()
        for exp in ldexp:
            exp.delete()
        ldimage= Live_Doctor_Imagegallery.objects.all()
        for gall in ldimage:
            gall.delete()
        ldmem = Live_Doctor_Membership.objects.all()
        for mem in ldmem:
            mem.delete()
        rewrec = Live_Doctor_Rewardrecog.objects.all()
        for rr in rewrec:
            rr.delete()
        ldasso = Live_Doctor_Associated_Data.objects.all()
        for asso in ldasso:
            asso.delete()
        ldquest = patienttoaskquestion.objects.all()
        for qs in ldquest:
            qs.delete()
        ldfeed = patienttodoctorfeedback.objects.all()
        for feed in ldfeed:
            feed.delete()

        messages.success(request, "Done")
        return HttpResponseRedirect(reverse('users-dashboard'))
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(reverse('users-dashboard'))


####################################################################
# Name - show_mailer                                               #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
#@user_passes_test(lambda u: u.is_superuser)
def show_mailer(request):
    try:
        return render(request,'mailer.html')

    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(reverse('users-dashboard'))


####################################################################
# Name - to_del_del                                                #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def to_del_del(request):
    try:
        # smita = Live_Doctor_Commonworkschedule.objects.get(doctor_id= 200130)
        # smita.clinic_id = str(16226)
        # smita.save()
        #
        # darpana = Live_Doctor_Commonworkschedule.objects.filter(doctor_id=200124)
        # darpana.update(clinic_id = str(16223))

        kunal_aher = Live_Doctor_Commonworkschedule.objects.filter(doctor_id=200115)
        kunal_aher.update(clinic_id=16223)

        messages.success("Done")
        return HttpResponseRedirect(reverse('users-dashboard'))

    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(reverse('users-dashboard'))

############MASTER WORK CAT SERV SPECIAL################


####################################################################
# Name - copy_Speciality                                           #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def copy_Speciality(request):
    try:
        counter=0
        for i in range(1 , 1936):
            try:
                spl = Speciality.objects.get(id=i)  # 1935
                counter += 1
                try:
                    add_new_cat = Doctor_Speciality_New(id=counter,name=spl.name.strip())
                    add_new_cat.save()
                except Exception as e :
                    counter -= 1
                    print e, "   ", counter
            except Exception as e:
                print "  ", e, "  :- ", i
        messages.success(request,"Done Copying Speciality")
        return HttpResponseRedirect(reverse('users-dashboard'))

    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(reverse('users-dashboard'))
####################################################################
# Name - copy_serviceoffered                                       #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def copy_serviceoffered(request):
    try:
        counter=0
        for i in range(1, 21328):
            try:
                spl = Service_Offred.objects.get(id=i) #21327
                counter += 1
                try:
                    add_new_so = Doctor_ServiceOffered_New(id=counter,name=spl.name.strip())
                    add_new_so.save()
                except Exception as e :
                    counter -= 1
                    print e,"   ",counter
            except Exception as e:
                print "  ", e, "  :- ", i

        messages.success(request,"Done Copying Service Offered")
        return HttpResponseRedirect(reverse('users-dashboard'))

    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(reverse('users-dashboard'))

####################################################################
# Name - copy_serviceoffered_7872                                  #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def copy_serviceoffered_7872(request):
    try:
        counter = 0
        for i in range(1,7873):
            try:
                spl = Service_Offred.objects.get(id=i)
                counter += 1
                try:
                    add_new_so = DelServiceOfferedNew_7872(id=counter, name=spl.name.strip())
                    add_new_so.save()

                    print ">>>>>>>>>>>>>>>>>CREATED ", spl.name.strip()
                except:
                    counter -= 1;
                    print "NOT CREATED ", spl.name.strip()
            except Exception as e:
                print "  ",e,"  :- ",i

        messages.success(request,"Done Copying Service Offered 7872")
        return HttpResponseRedirect(reverse('users-dashboard'))

    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(reverse('users-dashboard'))


####################################################################
# Name - publish_for_ashutosh                                      #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def publish_for_ashutosh(request):
    try:
        locality = Localitymaster.objects.get(id=1)
        data = {}
        data['id'] = locality.id
        data['name'] = locality.name
        data['name'].strip()
        response = elasticsearch_client.index_data('nonsearchmaster', 'localitymaster', locality.id, data)
        if response:
            pass
        else:
            messages.error(request, "Error while Publishing Locality master")
            return HttpResponseRedirect(reverse('users-dashboard'))

        city = Citymaster.objects.get(id=1)
        data = {}
        data['id'] = city.id
        data['name'] = city.name
        data['name'].strip()
        response = elasticsearch_client.index_data('nonsearchmaster', 'citymaster', city.id, data)
        if response:
            pass
        else:
            messages.error(request, "Error while Publishing City master")
            return HttpResponseRedirect(reverse('users-dashboard'))

        state = Statemaster.objects.get(id=1)
        data = {}
        data['id'] = state.id
        data['name'] = state.name
        data['name'].strip()
        response = elasticsearch_client.index_data('nonsearchmaster', 'statemaster', state.id, data)
        if response:
            pass
        else:
            messages.error(request, "Error while Publishing State master")
            return HttpResponseRedirect(reverse('users-dashboard'))

        country = Countrymaster.objects.get(id=1)
        data = {}
        data['id'] = country.id
        data['name'] = country.name
        data['name'].strip()
        response = elasticsearch_client.index_data('nonsearchmaster', 'countrymaster', country.id, data)
        if response:
            pass
        else:
            messages.error(request, "Error while Publishing Country master")
            return HttpResponseRedirect(reverse('users-dashboard'))

        messages.success(request,'SUCCESSFULLY Published All' )
        return HttpResponseRedirect(reverse('users-dashboard'))
    except Exception as e:
        #print e
        messages.error(request, "Error ")
        return HttpResponseRedirect(reverse('users-dashboard'))


####################################################################
# Name - traverse                                                  #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def traverse(request):
    try:

        from hfu_cms.models import Doctor_ServiceOffered_New, Service_Offred
        soold = Service_Offred.objects.all()
        sonew = Doctor_ServiceOffered_New.objects.all()

        for i in sonew:
            llist = []
            print i.id, " >>>>>>>>>>>>> ", i.name
            for j in soold:
                if j.name.strip().lower() == i.name.lower():
                    docs = Doctor.objects.filter(service_offered__icontains= str(j.id))
                    for doctor in docs:
                        llist = []
                        if doctor.service_offered_NAYIFIELD != '' and doctor.service_offered_NAYIFIELD != ' ':
                            llist = doctor.service_offered_NAYIFIELD.split(',')
                            llist.remove(str(j.id))
                            llist.append(str(i.id))
                            doctor.service_offered_NAYIFIELD = ",".join(llist)
                        else:
                            doctor.service_offered_NAYIFIELD = str(i.id)
                        doctor.save()

        messages.success(request,'SUCCESSFULLY Published All' )
        return HttpResponseRedirect(reverse('users-dashboard'))
    except Exception as e:
        print e
        messages.error(request, "Error ")
        return HttpResponseRedirect(reverse('users-dashboard'))



#######################
#Written By - Nishank #
#######################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
def temp_doctor_derviceoffered_new(request):
    try:
        new_so_records = Doctor_ServiceOffered_New.objects.all().order_by('id')
        count =0
        if len(new_so_records):
            so_old_all = Service_Offred.objects.all().order_by('id')
            for i in new_so_records:
                count += 1
                catlist = []
                idlist = []
                cll= ''
                ill = ''
                for j in so_old_all:
                    if j.name.lower().strip() == i.name.lower().strip():
                        catlist.append(j.category.name)
                        idlist.append(str(j.category.id))

                cll = ",".join(catlist)
                ill = ",".join(idlist)
                i.tempcat = cll
                i.tempcatIDS  = ill
                i.save()
                print "-------",i.id,"  ",i.name,"-------",count

        return HttpResponse("COMPLETE")
    except Exception as e:
        print "%% OUTER %%%%%%%%%%%%%%%%%%%%%%%"
        print e
        return HttpResponse("IN - COMPLETE")

# >>>>>>>>>>>>>   Special functions 29Nv17  Start <<<<<<<<<<<<<<<<<<<<

# FOR SERVICE OFFERED

# Populate ttteempp_for_association_so_2  using  ttteempp_for_association_so

#######################
# Written By - Nishank #
#######################
# @login_required(login_url='/')
# @user_passes_test(lambda u: u.is_superuser)
# def fill_ttteempp_for_association_so_2(request):
#     try:
#         allimp = ttteempp_for_association_so.objects.all().order_by('id')
#         if(len(allimp)):
#             for ii in allimp:
#                 if ii.categories:
#                     cats = None
#                     cats = ii.categories.split(',')
#                     for catid in cats:
#                         if catid != '' :
#                             ttteempp_for_association_so_2.objects.create(soid=ii.soid,categoryid=int(catid.strip()))
#                             print " --------  ", ii.soid,'  ',catid
#                         else:
#                             pass
#                 else:
#                     ttteempp_for_association_so_2.objects.create(soid=ii.soid)
#                     print " --------  ", ii.id, '_____________^^____________________'
#
#         return HttpResponse("COMPLETE")
#     except Exception as e:
#         print "%% OUTER %%%%%%%%%%%%%%%%%%%%%%%  ",e
#         print e
#         return HttpResponse("IN - COMPLETE")
#
#
#
# # Populate ttteempp_for_association_so_3  using  ttteempp_for_association_so_2
#
# #######################
# # Written By - Nishank #
# #######################
# @login_required(login_url='/')
# @user_passes_test(lambda u: u.is_superuser)
# def fill_ttteempp_for_association_so_3(request):
#     try:
#         assoall = Doc_Cat_SO_Speciality_Association_Final.objects.all().order_by('id')
#         for rec in assoall:
#             sos = None
#             sos = ttteempp_for_association_so_2.objects.filter(categoryid=rec.category)
#             if len(sos):
#                 sos = [ str(k.soid) for k in sos]
#                 sos = ",".join(sos)
#                 cname= Category.objects.get(id=rec.category).name
#                 ttteempp_for_association_so_3.objects.create(categoryid=rec.category,categoryname=cname,soids=sos)
#
#
#         return HttpResponse("COMPLETE so_3")
#     except Exception as e:
#         print "%% OUTER %%%%%%%%%%%%%%%%%%%%%%%  ", e
#         print e
#         return HttpResponse("IN - COMPLETE")
#
# # Replace the content of the ServiceOffered field in Doc_Cat_SO_Speciality_Association_Final table  (for 38 active categories) with
# # the contents in the soids field of ttteempp_for_association_so_3  since ttteempp_for_association_so_3 has only 38 rows corresponsing to
# # 38 categories.
#
# ########################
# # Written By - Nishank #
# ########################
# @login_required(login_url='/')
# @user_passes_test(lambda u: u.is_superuser)
# def replace_so_in_Doc_Cat_SO_Speciality_Association_Final(request):
#     try:
#         ttemp3all = ttteempp_for_association_so_3.objects.all().order_by('id')
#         for rec in ttemp3all:
#             obbj = Doc_Cat_SO_Speciality_Association_Final.objects.get(category=rec.categoryid)
#             obbj.ServiceOffered = rec.soids
#             obbj.save()
#             print obbj.id, ' Updated Category is ',obbj.category
#
#         return HttpResponse("COMPLETE obbj.ServiceOffered = rec.soids")
#     except Exception as e:
#         print "%% OUTER %%%%%%%%%%%%%%%%%%%%%%%  ", e
#         print e
#         return HttpResponse("IN - COMPLETE")
#
#
# # Now we select all doctors containing each of the 38 categories one by one. [we find category using ttteempp_for_association_so_3]
# # Say we selected all doctors in category dental and we got 150 doctrs with category dental.
# # Now for each of these 150 doctors we will compare the comma seperated values contained in doctor's  new_service_offered_final
# # field with the comma separated values in ServiceOffered  field of Doc_Cat_SO_Speciality_Association_Final for that category  and
# # delete all values present in doctor's  new_service_offered_final  field but not present in ServiceOffered  field of
# # Doc_Cat_SO_Speciality_Association_Final
#
# ########################
# # Written By - Nishank #
# ########################
# @login_required(login_url='/')
# @user_passes_test(lambda u: u.is_superuser)
# def update_doctors_new_service_offered_final(request):
#     try:
#         ttemp3all = ttteempp_for_association_so_3.objects.all().order_by('id')
#         for rec in ttemp3all:
#             # Get the association for the category
#             obbj = Doc_Cat_SO_Speciality_Association_Final.objects.get(category=rec.categoryid)
#
#             #Get doctors belonging to that category
#             doclist = None
#             doclist = Doctor.objects.filter(category_id=rec.categoryid).order_by('id')
#
#             if(len(doclist)):
#                 #check each doctor's new_service_offered_final field and delete unnecessary/no permissible ids
#                 reference_values =  obbj.ServiceOffered.split(',')
#                 for ddoc in doclist:
#                     if ddoc.new_service_offered_final:
#                         doctor_values = ''
#                         doctor_values = ddoc.new_service_offered_final.split(',')
#                         replist = []
#                         for ittem in doctor_values:
#                             if ittem in reference_values:
#                                 replist.append(ittem)
#                         ddoc.new_service_offered_final = ",".join(replist)
#                         #print
#                         #print
#                         #print
#
#                         ddoc.save()
#                         print "Updated ----------        ",ddoc.id,"  ",ddoc.name
#                     else:
#                         print 'P   A    S   S   E   D   Doctors SO is None' , ddoc.id,"  ",ddoc.name
#             else:
#                 print "P   A    S   S   E   D    NO Doctor For category id  ", rec.categoryid
#
#
#         return HttpResponse("COMPLETE Updatiing doctor")
#     except Exception as e:
#         print "%% OUTER %%%%%%%%%%%%%%%%%%%%%%%  ", e
#         print e
#         return HttpResponse("IN - COMPLETE")



# FOR SPECILALITY

# Populate ttteempp_for_association_spe_2  using  ttteempp_for_association_spe

# ########################
# # Written By - Nishank #
# ########################
# @login_required(login_url='/')
# @user_passes_test(lambda u: u.is_superuser)
# def fill_ttteempp_for_association_spe_2(request):
#     try:
#         allimp = ttteempp_for_association_spe.objects.all().order_by('id')
#         if (len(allimp)):
#             for ii in allimp:
#                 if ii.categories:
#                     cats = None
#                     cats = ii.categories.split(',')
#                     for catid in cats:
#                         if catid != '':
#                             ttteempp_for_association_spe_2.objects.create(speid=ii.speid,
#                                                                           categoryid=int(catid.strip()))
#                             print " --------  ", ii.speid, '  ', catid
#                         else:
#                             pass
#                 else:
#                     ttteempp_for_association_spe_2.objects.create(speid=ii.speid)
#                     print " --------  ", ii.speid, '_____________^^____________________'
#
#         return HttpResponse("COMPLETE")
#     except Exception as e:
#         print "%% OUTER %%%%%%%%%%%%%%%%%%%%%%%  ", e
#         print e
#         return HttpResponse("IN - COMPLETE")
#
# # Populate ttteempp_for_association_spe_3  using  ttteempp_for_association_spe_2
#
# ########################
# # Written By - Nishank #
# ########################
# @login_required(login_url='/')
# @user_passes_test(lambda u: u.is_superuser)
# def fill_ttteempp_for_association_spe_3(request):
#     try:
#         assoall = Doc_Cat_SO_Speciality_Association_Final.objects.all().order_by('id')
#         for rec in assoall:
#             spes = None
#             spes = ttteempp_for_association_spe_2.objects.filter(categoryid=rec.category)
#             if len(spes):
#                 spes = [str(k.speid) for k in spes]
#                 spes = ",".join(spes)
#                 cname = Category.objects.get(id=rec.category).name
#                 ttteempp_for_association_spe_3.objects.create(categoryid=rec.category, categoryname=cname,
#                                                               speids=spes)
#
#         return HttpResponse("COMPLETE spe_3")
#     except Exception as e:
#         print "%% OUTER %%%%%%%%%%%%%%%%%%%%%%%  ", e
#         print e
#         return HttpResponse("IN - COMPLETE")
#
# # Replace the content of the ServiceOffered field in Doc_Cat_SO_Speciality_Association_Final table  (for 38 active categories) with
# # the contents in the soids field of ttteempp_for_association_so_3  since ttteempp_for_association_so_3 has only 38 rows corresponsing to
# # 38 categories.
#
# ########################
# # Written By - Nishank #
# ########################
# @login_required(login_url='/')
# @user_passes_test(lambda u: u.is_superuser)
# def replace_spe_in_Doc_Cat_SO_Speciality_Association_Final(request):
#     try:
#         ttemp3all = ttteempp_for_association_spe_3.objects.all().order_by('id')
#         for rec in ttemp3all:
#             obbj = Doc_Cat_SO_Speciality_Association_Final.objects.get(category=rec.categoryid)
#             obbj.Specialities = rec.speids
#             obbj.save()
#             print obbj.id, ' Updated Category is ', obbj.category
#
#         return HttpResponse("COMPLETE obbj.Specialities = rec.speids")
#     except Exception as e:
#         print "%% OUTER %%%%%%%%%%%%%%%%%%%%%%%  ", e
#         print e
#         return HttpResponse("IN - COMPLETE")
#
# # Now we select all doctors containing each of the 38 categories one by one. [we find category using ttteempp_for_association_so_3]
# # Say we selected all doctors in category dental and we got 150 doctrs with category dental.
# # Now for each of these 150 doctors we will compare the comma seperated values contained in doctor's  new_service_offered_final
# # field with the comma separated values in ServiceOffered  field of Doc_Cat_SO_Speciality_Association_Final for that category  and
# # delete all values present in doctor's  new_service_offered_final  field but not present in ServiceOffered  field of
# # Doc_Cat_SO_Speciality_Association_Final
#
# ########################
# # Written By - Nishank #
# ########################
# @login_required(login_url='/')
# @user_passes_test(lambda u: u.is_superuser)
# def update_doctors_new_speciality_final(request):
#     try:
#         ttemp3all = ttteempp_for_association_spe_3.objects.all().order_by('id')
#         for rec in ttemp3all:
#             # Get the association for the category
#             obbj = Doc_Cat_SO_Speciality_Association_Final.objects.get(category=rec.categoryid)
#
#             # Get doctors belonging to that category
#             doclist = None
#             doclist = Doctor.objects.filter(category_id=rec.categoryid).order_by('id')
#
#             if (len(doclist)):
#                 # check each doctor's new_service_offered_final field and delete unnecessary/no permissible ids
#                 reference_values = obbj.Specialities.split(',')
#                 for ddoc in doclist:
#                     if ddoc.new_speciality_final:
#                         doctor_values = ''
#                         doctor_values = ddoc.new_speciality_final.split(',')
#                         replist = []
#                         for ittem in doctor_values:
#                             if ittem in reference_values:
#                                 replist.append(ittem)
#                         ddoc.new_speciality_final = ",".join(replist)
#                         # print
#                         # print
#                         # print
#
#                         ddoc.save()
#                         print "Updated ----------        ", ddoc.id, "  ", ddoc.name
#                     else:
#                         print 'P   A    S   S   E   D   Doctors Speciality is None', ddoc.id, "  ", ddoc.name
#             else:
#                 print "P   A    S   S   E   D    NO Doctor For category id  ", rec.categoryid
#
#         return HttpResponse("COMPLETE Updatiing doctor")
#     except Exception as e:
#         print "%% OUTER %%%%%%%%%%%%%%%%%%%%%%%  ", e
#         print e
#         return HttpResponse("IN - COMPLETE")

# For 7 more categories we delete all specialities relatined to them by emptying the
# Specialities field of Doc_Cat_SO_Speciality_Association_Final for these 7 categories
########################
# Written By - Nishank #
########################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
def empty_spe_in_Doc_Cat_SO_Speciality_Association_Final_for7cats(request):
    try:
        dellist = [18, 20, 22, 29, 33, 35, 39]
        for rec in dellist:
            obbj = Doc_Cat_SO_Speciality_Association_Final.objects.get(category=rec)
            obbj.Specialities = ''
            obbj.save()
            print obbj.id, ' Updated Category is ', obbj.category

        return HttpResponse("COMPLETE obbj.Specialities = '' ")
    except Exception as e:
        print "%% OUTER %%%%%%%%%%%%%%%%%%%%%%%  ", e
        print e
        return HttpResponse("IN - COMPLETE")

########################
# Written By - Nishank #
########################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
def empty_doctors_new_speciality_final_for7cats(request):
    try:
        dellist = [18, 20, 22, 29, 33, 35, 39]
        for rec in dellist:
            # Get doctors belonging to that category
            doclist = None
            doclist = Doctor.objects.filter(category_id=rec).order_by('id')
            print 'Doctor Count for  Category Id ', rec, ' is ', doclist.count()

            if (len(doclist)):
                for ddoc in doclist:
                    ddoc.new_speciality_final = ""
                    ddoc.save()
                    print "deleted Specialities in doc ----------        ", ddoc.id, "  ", ddoc.name
            else:
                print "P   A    S   S   E   D    NO Doctor For category id  ", rec

        return HttpResponse("COMPLETE Updat5ing doctor")
    except Exception as e:
        print "%% OUTER %%%%%%%%%%%%%%%%%%%%%%%  ", e
        print e
        return HttpResponse("IN - COMPLETE")


        # >>>>>>>>>>>>>   Special functions 29Nv17  End <<<<<<<<<<<<<<<<<<<<


#######**########

########################
# Written By - Nishank #
########################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
def publish_3_masters(request):
    try:
        import elasticsearch_client
        cat_id_list = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 14 , 15 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 33 , 34 , 35 , 36 , 37 , 39 , 40 , 41 , 42 , 45 ]
        cat_count = 0
        for idd in cat_id_list:
            category = Category.objects.get(id=idd)
            data = {}
            data['id'] = category.id
            data['name'] = category.name.strip()
            response = elasticsearch_client.index_data('globalmaster', 'category', category.id, data)
            response = elasticsearch_client.index_data('master', 'category', category.id, data)
            cat_count += 1
            print "Published Categories : "+' '+str(cat_count)



        speciality_obj_all = Doctor_Speciality_New.objects.filter(WorL__iexact='winner').order_by('name')
        print "-------------------------  ",speciality_obj_all.count()
        SPE_COUNT = 0
        for speciality_obj in speciality_obj_all:
            response_data_dict = {}
            response_data_dict['id'] = speciality_obj.id
            response_data_dict['name'] = speciality_obj.name

            response = elasticsearch_client.index_data('globalmaster', 'speciality_new', speciality_obj.id, response_data_dict)
            response = elasticsearch_client.index_data('master', 'speciality_new', speciality_obj.id, response_data_dict)
            SPE_COUNT += 1
            print "Published SPECIALITIERS  " + ' ' + str(SPE_COUNT)

        service_offered_obj_all = Doctor_ServiceOffered_New.objects.filter(WorL__iexact='winner').order_by('name')
        print "-------------------------  ",service_offered_obj_all.count()
        SO_COUNT = 0
        for service_offered_obj in service_offered_obj_all:
            if service_offered_obj.deleete == False:
                response_data_dict = {}
                response_data_dict['id'] = service_offered_obj.id
                response_data_dict['name'] = service_offered_obj.name

                response = elasticsearch_client.index_data('globalmaster', 'service_offered_new', service_offered_obj.id, response_data_dict)
                response = elasticsearch_client.index_data('master', 'service_offered_new', service_offered_obj.id, response_data_dict)
                SO_COUNT += 1
                print "Published SOS  " + ' ' + str(SO_COUNT)
        #
        CSSAF_all = Doc_Cat_SO_Speciality_Association_Final.objects.filter(category__in=cat_id_list)
        print "-------------------------  ",CSSAF_all.count()
        ASSO_COUNT =0
        for CSSAF in CSSAF_all :
            category_name = Category.objects.get(id=CSSAF.category).name

            soss = []
            if CSSAF.ServiceOffered and CSSAF.ServiceOffered != '' and CSSAF.ServiceOffered != ' ':
                soss = CSSAF.ServiceOffered.strip().split(',')
                soss = [{'id': int(ccc), 'name': Doctor_ServiceOffered_New.objects.get(id=int(ccc)).name} for ccc in soss if ccc != '']

            spess = []
            if CSSAF.Specialities and CSSAF.Specialities != '' and CSSAF.Specialities != ' ':
                spess = CSSAF.Specialities.strip().split(',')
                spess = [{'id': int(ccc), 'name': Doctor_Speciality_New.objects.get(id=int(ccc)).name} for ccc in spess if ccc != '']

            response_data_dict = {}
            response_data_dict['id'] = CSSAF.id
            response_data_dict['category_id'] = CSSAF.category
            response_data_dict['category_name'] = category_name
            response_data_dict['service_offered'] = soss
            response_data_dict['speciality'] = spess

            response = elasticsearch_client.index_data('globalmaster', 'cat_so_spe_association', CSSAF.id, response_data_dict)
            response = elasticsearch_client.index_data('master', 'cat_so_spe_association', CSSAF.id, response_data_dict)
            ASSO_COUNT += 1
            print "Published Associations  " + ' ' + str(ASSO_COUNT)


        return HttpResponse("PUblished all 3 Masters")
    except Exception as e:
        print "%% OUTER %%%%%%%%%%%%%%%%%%%%%%%  ", e
        print e
        return HttpResponse("IN - COMPLETE")


########################
# Written By - Nishank #
########################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
def org_update_lat_long(request):
    try:
        import json
        done_list = []
        left_list = []
        org_id_list = [ 131,326,694,916,1107,1386,1521,1567,1645,1662,2057,2211,2481,2550,2630,2723,2759,2800,2813,2853,2890,2912,2949,2976,2986,3033,3064,3065,3075,3102,3108,3141,3152,3206,3313,3324,3339,3442,3452,3474,3487,3499,3519,3522,3523,3547,3640,3657,3661,3704,3708,3729,3739,3945,3986,4162,4194,4225,4324,4359,4402,4467,4537,4627,4692,4693,4794,4842,4849,4929,5031,5059,5151,5221,5222,5287,5376,5435,5510,5513,5523,5856,5876,5891,5936,5990,6049,6060,6302,6420,6519,6573,6626,6710,6737,6760,6761,7104,7218,7331,7332,7396,7403,7674,7729,7775,7825,7835,7853,7934,7943,8044,8110,8115,8158,8193,8194,8208,8313,8423,8443,8557,8559,8586,8612,8617,8672,8674,8884,8886,8888,8889,8892,8894,8901,8902,8905,8906,8907,8908,8910,8912,8915,8916,8917,8920,8923,8927,8930,8931,8932,8934,8935,8937,8940,8942,8943,8944,8946,8947,8951,8955,8957,8960,8963,8965,8966,8967,8970,8971,8973,8977,8979,8980,8981,8984,8989,8990,8992,8995,8997,8998,8999,9000,9001,9002,9003,9004,9005,9006,9007,9009,9011,9012,9014,9015,9017,9018,9019,9020,9021,9022,9023,9024,9025,9027,9028,9030,9031,9032,9033,9034,9035,9036,9037,9038,9040,9042,9043,9044,9046,9047,9048,9049,9050,9051,9052,9053,9054,9055,9056,9057,9058,9059,9061,9062,9063,9064,9065,9066,9068,9069,9070,9071,9072,9073,9074,9075,9076,9077,9078,9079,9080,9081,9082,9083,9084,9085,9086,9087,9088,9089,9090,9091,9092,9093,9094,9095,9096,9097,9098,9099,9101,9102,9103,9104,9105,9106,9107,9108,9109,9110,9111,9112,9113,9114,9116,9117,9118,9119,9121,9122,9123,9124,9125,9126,9127,9128,9129,9130,9131,9132,9134,9135,9136,9137,9138,9139,9141,9143,9144,9145,9147,9148,9149,9151,9152,9153,9154,9158,9160,9162,9163,9165,9167,9168,9169,9170,9171,9173,9174,9175,9176,9177,9178,9181,9182,9183,9186,9187,9188,9189,9190,9191,9192,9193,9194,9195,9196,9197,9198,9199,9200,9201,9202,9203,9204,9205,9206,9207,9208,9209,9210,9211,9214,9216,9217,9218,9219,9220,9221,9222,9223,9224,9225,9226,9227,9228,9229,9230,9231,9233,9234,9235,9237,9239,9240,9241,9242,9243,9244,9245,9246,9247,9248,9249,9251,9252,9253,9254,9255,9257,9259,9260,9261,9263,9264,9266,9267,9268,9269,9270,9271,9272,9273,9274,9275,9276,9278,9279,9280,9281,9283,9284,9285,9286,9287,9288,9289,9291,9292,9293,9294,9295,9297,9298,9299,9300,9301,9302,9303,9304,9305,9307,9308,9310,9311,9312,9313,9314,9315,9316,9317,9318,9319,9320,9321,9322,9323,9325,9326,9327,9328,9329,9330,9331,9332,9333,9334,9335,9336,9337,9338,9339,9340,9341,9349,9350,9351,9352,9354,9356,9357,9358,9359,9360,9365,9367,9368,9369,9370,9372,9375,9376,9378,9380,9381,9382,9383,9385,9386,9393,9394,9395,9396,9397,9399,9400,9401,9402,9403,9404,9405,9406,9407,9408,9409,9410,9411,9412,9413,9414,9415,9416,9417,9418,9419,9420,9421,9422,9423,9424,9425,9427,9428,9430,9431,9432,9433,9434,9435,9436,9437,9438,9439,9440,9441,9442,9444,9445,9446,9447,9448,9449,9450,9451,9452,9453,9454,9455,9456,9457,9458,9459,9460,9462,9463,9464,9465,9466,9467,9468,9469,9470,9472,9474,9475,9476,9478,9479,9480,9481,9484,9487,9491,9492,9493,9494,9495,9496,9499,9501,9502,9503,9504,9506,9507,9510,9511,9513,9516,9518,9519,9520,9521,9522,9523,9524,9526,9527,9528,9532,9535,9536,9537,9538,9539,9540,9542,9543,9544,9545,9546,9550,9556,9557,9558,9559,9560,9561,9562,9563,9564,9565,9566,9567,9568,9569,9570,9571,9572,9573,9574,9575,9577,9579,9580,9581,9582,9583,9586,9587,9588,9589,9590,9591,9592,9593,9594,9595,9597,9598,9599,9600,9602,9604,9605,9606,9607,9608,9609,9610,9611,9612,9613,9614,9615,9616,9617,9618,9619,9620,9621,9622,9623,9624,9625,9626,9627,9628,9629,9630,9631,9632,9633,9634,9635,9636,9637,9638,9639,9640,9641,9642,9643,9644,9645,9646,9647,9648,9649,9650,9651,9652,9653,9654,9655,9656,9657,9658,9659,9660,9661,9662,9663,9664,9666,9667,9668,9669,9670,9671,9672,9673,9674,9675,9676,9677,9678,9679,9680,9681,9682,9683,9684,9685,9687,9688,9689,9690,9691,9692,9693,9694,9695,9696,9697,9698,9699,9700,9701,9702,9703,9704,9705,9706,9707,9708,9709,9711,9712,9713,9714,9715,9716,9717,9718,9719,9720,9721,9722,9723,9724,9725,9726,9727,9728,9729,9730,9731,9732,9733,9734,9735,9736,9737,9738,9739,9740,9741,9742,9743,9744,9745,9746,9747,9748,9749,9750,9751,9752,9753,9754,9755,9756,9757,9758,9759,9760,9761,9762,9763,9764,9765,9766,9767,9768,9769,9770,9771,9772,9773,9774,9775,9776,9777,9778,9779,9780,9781,9782,9783,9784,9785,9786,9787,9788,9789,9790,9791,9792,9793,9794,9795,9796,9797,9798,9799,9800,9801,9802,9803,9804,9805,9806,9807,9808,9809,9810,9811,9812,9813,9814,9815,9816,9817,9818,9819,9820,9821,9822,9823,9824,9825,9826,9827,9828,9829,9830,9831,9832,9834,9835,9837,9838,9839,9840,9841,9842,9843,9844,9845,9846,9847,9848,9849,9850,9851,9852,9853,9855,9856,9857,9858,9859,9860,9861,9862,9863,9864,9865,9866,9867,9868,9869,9870,9871,9872,9873,9874,9875,9876,9877,9878,9879,9880,9881,9882,9883,9884,9885,9886,9887,9888,9889,9890,9891,9892,9893,9894,9895,9896,9897,9898,9899,9900,9901,9902,9903,9904,9905,9906,9907,9908,9909,9910,9911,9912,9913,9914,9915,9916,9917,9918,9919,9920,9921,9922,9923,9924,9925,9926,9927,9928,9929,9930,9931,9932,9933,9934,9935,9936,9937,9938,9939,9940,9941,9942,9943,9944,9945,9946,9947,9948,9949,9950,9951,9952,9953,9954,9955,9956,9957,9958,9959,9960,9961,9962,9963,9964,9965,9966,9967,9968,9969,9970,9971,9972,9973,9974,9975,9976,9977,9978,9979,9980,9981,9982,9983,9984,9985,9986,9987,9988,9989,9990,9991,9992,9993,9994,9995,9996,9997,9998,9999,10000,10001,10002,10003,10004,10005,10006,10007,10008,10009,10010,10011,10012,10013,10014,10015,10016,10017,10018,10019,10020,10021,10022,10023,10024,10025,10026,10353,16188,16189,16190,16191,16192,16193,16194,16195,16196,16197,16198,16199,16202,16203,16205,16206,16207,16208,16209,16210,16211,16212,16213,16214,16215,16216,16217,16218,16219,16220,16221,16222,16223,16224,16225,16226,16227,16228,16229,16230,16231,16232,16233,16234,16235,16236,16237,16238,16239,16240,16241,16242,16243,16244,16245,16246,16247,16248,16249,16250,16251,16252,16253,16254,16256,16257,16258,16259,16260,16261,16262,16263,16264,16265,16266,16267,16268,16269,16270,16271,16272,16273,16274,16275,16276,16277,16278,16279,16280,16281,16282,16283,16284,16285,16286,16287,16288,16289,16290,16291,16292,16293,16294,16295,16296,16297,16298,16299,16300,16301,16302,16303,16304,16305,16306,16307,16308,16309,16310,16311,16312,16313,16314,16315,16316,16317,16318,16319,16320,16321,16322,16323,16324,16325,16326,16327,16328,16329,16330,16331,16332,16333,16334,16335,16336,16337,16338,16339,16340,16341,16342,16343,16344,16345,16346,16347,16348,16349,16350,16351,16352,16353,16354,16355,16356,16357,16358,16359,16360,16361,16362,16363,16364,16365,16366,16367,16368,16369,16370,16371,16372,16373,16374,16375,16376,16377,16378,16379,16380,16381,16382,16383,16384,16385,16386,16387,16388,16389,16390,16391,16392,16393,16394,16395,16396,16397,16398,16399,16400,16401,16402,16403,16404,16405,16406,16407,16408,16409,16410,16411,16412,16413,16414,16415,16416,16417,16418,16419,16420,16421,16422,16423,16424,16425,16426,16427,16428,16429,16430,16431,16432,16433,16434,16435,16436,16437,16438,16439,16440,16441,16442,16443,16444,16445,16446,16447,16448,16449,16450,16451,16452,16453,16455,16456,16457,16458,16459,16460,16461,16462,16463,16464,16465,16466,16467,16468,16469,16470,16472,16473,16474,16475,16476,16477,16478,16479,16480,16481,16482,16483,16484,16485,16486,16487,16488,16489,16490,16491,16492,16493,16494,16495,16496,16497,16498,16499,16500,16501,16502,16503,16504,16505,16506,16507,16508,16509,16510,16511,16512,16513,16514,16515,16516,16517,16518,16519,16520,16521,16522,16523,16524,16525,16526,16527,16528,16529,16530,16531,16532,16533,16534,16535,16536,16537,16538,16539,16540,16541,16542,16543,16544,16545,16546,16547,16548,16549,16550,16551,16552,16553,16554,16555,16556,16557,16558,16559,16560,16561,16562,16563,16564,16565,16566,16567,16568,16569,16570,16571,16572,16573,16574,16575,16577,16578,16579,16580,16582,16583,16584,16585,16586,16587,16588,16589,16590,16592,16593,16594,16595,16596,16597,16598,16599,16600,16601,16602,16603,16604,16605,16606,16607,16608,16609,16610,16611,16612,16613,16614,16615,16616,16617,16618,16619,16620,16621,16622,16623,16624,16625,16626,16627,16628,16629,16630,16631,16632,16633,16634,16635,16636,16637,16638,16639,16640,16641,16642,16643,16644,16645,16646,16647,16648,16649,16650,16651,16652,16653,16654,16655,16656,16657,16658,16659,16660,16661,16662,16663,16664,16665,16666,16667,16668,16669,16670,16671,16672,16673,16674,16675,16676,16677,16678,16679,16680,16681,16682,16683,16684,16685,16686,16687,16688,16689,16690,16691,16692,16693,16694,16695,16696,16697,16698,16699,16700,16701,16702,16703,16704,16705,16706,16707,16708,16709,16710,16711,16712,16713,16714,16715,16716,16717,16718,16719,16720,16721,16722,16723,16724,16725,16726,16727,16728,16729,16730,16731,16732,16733,16734,16735,16736,16737,16738,16739,16740,16741,16742,16743,16744,16745,16746,16747,16748,16749,16750,16751,16752,16753,16754,16755,16756,16757,16758,16759,16760,16761,16762,16763,16764,16765,16766,16767,16768,16769,16770,16771,16772,16773,16774,16775,16776,16777,16778,16779,16780,16781,16782,16783,16784,16785,16786,16787,16788,16789,16790,16791,16792,16793,16794,16795,16796,16797,16798,16799,16800,16801,16802,16803,16804,16805,16806,16807,16808,16809,16810,16811,16812,16813,16814,16815,16816,16817,16818,16819,16820,16821,16822,16823,16824,16825,16826,16827,16828,16829,16830,16831,16832,16833,16834,16835,16836,16837,16838,16839,16840,16841,16842,16843,16844,16845,16846,16847,16848,16849,16851,16852,16853,16854,16855,16856,16857,16858,16859,16860,16861,16862,16863,16864,16865,16866,16867,16868,16869,16870,16871,16872,16873,16874,16875,16876,16877,16878,16879,16880,16881,16882,16883,16884,16885,16886,16887,16888,16889,16890,16891,16892,16893,16894,16895,16896,16897,16898,16899,16900,16901,16902,16903,16904,16905,16906,16907,16908,16909,16910,16911,16912,16913,16914,16915,16916,16917,16918,16919,16920,16921,16922,16923,16924,16925,16926,16927,16928,16929,16930,16931,16932,16933,16934,16935,16936,16937,16938,16939,16940,16941,16942,16943,16944,16945,16946,16947,16948,16949,16950,16951,16952,16953,16954,16955,16956,16957,16958,16959,16960,16961,16962,16963,16964,16965,16966,16967,16968,16969,16970,16971,16972,16973,16974,16975,16976,16977,16978,16979,16980,16981,16982,16983,16984,16985,16986,16987,16988,16989,16990,16991,16992,16993,16994,16995,16996,16997,16998,16999,17000,17001,17002,17003,17004,17005,17006,17007,17008,17009,17010,17011,17012,17013,17014,17015,17016,17017,17018,17019,17020,17021,17022,17023,17024,17025,17026,17027,17028,17029,17030,17031,17032,17033,17034,17035,17036,17037,17038,17039,17040,17041,17042,17043,17044,17045,17046,17047,17048,17049,17050,17051,17052,17053,17054,17055,17056,17057,17058,17059,17060,17061,17062,17063,17064,17065,17066,17067,17068,17069,17070,17071,17072,17073,17074,17075,17076,17077,17078,17079,17080,17081,17082,17083,17084,17085,17086,17087,17088,17089,17090,17091,17092,17093,17094,17095,17096,17097,17098,17099,17100,17101,17102,17103,17104,17105,17106,17107,17108,17109,17110,17111,17112,17113,17114,17115,17116,17117,17118,17119,17120,17121,17122,17123,17124,17125,17126,17127,17128,17129,17130,17131,17132,17133,17134,17135,17136,17137,17138,17139,17140,17141,17142,17143,17144,17145,17146,17147,17148,17149,17150,17151,17152,17153,17154,17155,17156,17157,17158,17159,17160,17161,17162,17163,17164,17165,17166,17167,17168,17169,17170,17171,17172,17173,17174,17175,17176,17177,17178,17180,17181,17182,17183,17184,17185,17186,17187,17188,17189,17190,17191,17192,17193,17194,17195,17196,17197,17198,17199,17200,17201,17202,17203,17204,17205,17206,17207,17208,17209,17210,17211,17212,17213,17214,17215,17216,17217,17218,17219,17220,17221,17222,17223,17224,17225,17226,17227,17228,17229,17230,17231,17232,17233,17234,17235,17236,17237,17238,17239,17240,17241,17242,17243,17244,17245,17246,17247,17248,17249,17250,17251,17252,17253,17254,17255,17256,17257,17258,17259,17260,17261,17262,17263,17264,17265,17266,17267,17268,17269,17270,17271,17272,17273,17274,17275,17276,17277,17278,17279,17280,17281,17282,17283,17284,17285,17286,17287,17288,17289,17290,17291,17292,17293,17294,17295,17296,17297,17298,17299,17300,17301,17302,17303,17304,17305,17306,17307,17308,17309,17310,17311,17312,17313,17314,17315,17316,17317,17318,17319,17320,17321,17322,17323,17324,17325,17326,17327,17328,17329,17330,17331,17332,17333,17334,17335,17336,17337,17338,17339,17340,17341,17342,17343,17344,17345,17346,17347,17348,17349,17350,17351,17352,17353,17354,17355,17356,17357,17358,17359,17360,17361,17362,17363,17364,17365,17366,17367,17368,17369,17370,17371,17372,17373,17374,17375,17376,17377,17378,17380,17381,17382,17383,17384,17385,17386,17387,17388,17389,17390,17391,17392,17393,17394,17395,17397,17398,17399,17400,17401,17402,17403,17404,17405,17406,17407,17408,17409,17410,17411,17412,17413,17414,17415,17416,17417,17418,17419,17420,17421,17422,17423,17424,17425,17426,17427,17428,17429,17430,17431,17432,17433,17434,17435,17436,17437,17438,17439,17440,17441,17442,17443,17444,17445,17446,17447,17448,17449,17450,17451,17452,17453,17454,17455,17456,17457,17458,17459,17460,17461,17462,17463,17464,17465,17466,17467,17468,17469,17470,17471,17472,17473,17474,17475,17476,17477,17478,17479,17480,17481,17482,17483,17484,17485,17486,17487,17488,17489,17490,17491,17492,17493,17494,17495,17496,17497,17498,17499,17500,17501,17502,17503,17504,17505,17506,17507,17508,17509,17510,17511,17512,17513,17514,17515,17516,17517,17518,17519,17520,17521,17522,17523,17524,17525,17526,17527,17528,17529,17530,17531,17532,17533,17534,17535,17536,17537,17538,17539,17540,17541,17542,17543,17544,17545,17546,17547,17548,17549,17550,17551,17552,17553,17554,17555,17556,17557,17558,17559,17560,17561,17562,17563,17564,17565,17566,17568,17570,17571,17572,17573,17574,17575,17576,17577,17578,17579,17580,17581,17582,17583,17584,17585,17586,17587,17588,17589,17590,17591,17592,17593,17594,17595,17596,17597,17598,17599,17600,17601,17602,17603,17604,17605,17606,17607,17608,17609,17610,17611,17612,17613,17614,17615,17616,17617,17618,17619,17620,17621,17622,17623,17624,17625,17626,17627,17628,17629,17630,17631,17632,17633,17634,17635,17636,17637,17638,17639,17640,17641,17642,17643,17644,17645,17646,17647,17648,17649,17650,17651,17652,17653,17654,17655,17656,17657,17658,17659,17660,17661,17662,17663,17664,17665,17666,17667,17668,17669,17670,17671,17672,17673,17674,17675,17676,17677,17678,17679,17680,17681,17682,17683,17684,17685,17686,17687,17688,17689,17690,17691,17692,17693,17694,17695,17696,17697,17698,17699,17700,17701,17702,17703,17704,17705,17706,17707,17708,17709,17710,17711,17712,17713,17714,17715,17716,17717,17718,17719,17720,17721,17722,17723,17724,17725,17726,17727,17728,17729,17730,17731,17732,17733,17734,17735,17736,17737,17738,17739,17740,17741,17742,17743,17744,17745,17746,17747,17748,17749,17750,17751,17752,17753,17754,17755,17756,17757,17758,17759,17760,17761,17762,17763,17764,17765,17766,17767,17768,17769,17770,17771,17772,17773,17774,17775,17776,17777,17778,17779,17780,17781,17782,17783,17784,17785,17786,17787,17788,17789,17790,17791,17792,17793,17794,17795,17796,17797,17798,17799,17800,17801,17802,17803,17804,17805,17806,17807,17808,17809,17810,17811,17812,17813,17814,17815,17816,17817,17818,17819,17820,17821,17822,17823,17824,17825,17826,17827,17828,17829,17830,17831,17832,17833,17834,17835,17836,17837,17838,17839,17840,17841,17842,17843,17844,17845,17846,17847,17848,17849,17850,17851,17852,17853,17854,17855,17856,17857,17858,17859,17860,17861,17862,17863,17864,17865,17866,17867,17868,17869,17870,17871,17872,17873,17874,17875,17876,17877,17878,17879,17880,17881,17882,17883,17884,17885,17886,17887,17888,17889,17890,17891,17892,17893,17894,17895,17896,17897,17898,17899,17900,17901,17902,17903,17904,17905,17906,17907,17908,17909,17910,17911,17912,17913,17914,17915,17916,17917,17918,17919,17920,17921,17922,17923,17924,17925,17926,17927,17928,17929,17930,17931,17932,17933,17934,17935,17936,17937,17938,17939,17940,17941,17942,17943,17944,17945,17946,17947,17948,17949,17950,17951,17952,17953,17954,17955,17956,17957,17958,17959,17960,17961,17962,17963,17964,17965,17966,17967,17968,17969,17970,17971,17972,17973,17974,17975,17976,17977,17978,17979,17980,17981,17982,17983,17984,17985,17986,17987,17988,17989,17990,17991,17992,17993,17994,17995,17996,17997,17998,17999,18000,18001,18002,18003,18004,18005,18006,18007,18008,18009,18010,18011,18012,18013,18014,18015,18016,18017,18018,18019,18020,18021,18022,18023,18024,18025,18026,18027,18028,18029,18030,18031,18032,18033,18034,18035,18036,18037,18038,18039,18040,18041,18042,18043,18044,18045,18046,18047,18048,18049,18050,18051,18052,18053,18054,18055,18056,18057,18058,18059,18060,18061,18062,18063,18064,18065,18066,18067,18068,18069,18070,18071,18072,18073,18074,18075,18076,18077,18078,18079,18080,18081,18082,18083,18084,18085,18086,18087,18088,18089,18090,18091,18092,18093,18094,18095,18096,18097,18098,18099,18100,18101,18102,18103,18104,18105,18106,18107,18108,18109,18110,18111,18112,18113,18114,18115,18116,18117,18118,18119,18120,18121,18122,18123,18124,18125,18126,18127,18128,18129,18130,18131,18132,18133,18134,18135,18136,18137,18138,18139,18140,18141,18142,18143,18144,18145,18146,18147,18148,18149,18150,18151,18152,18153,18154,18155,18156,18157,18158,18159,18160,18161,18162,18163,18164,18165,18166,18167,18168,18169,18170,18171,18172,18173,18174,18175,18176,18177,18178,18179,18180,18181,18182,18183,18184,18185,18186,18187,18188,18189,18190,18191,18192,18193,18194,18195,18196,18197,18198,18199,18200,18201,18202,18203,18204,18205,18206,18207,18208,18209,18210,18211,18212,18213,18214,18215,18216,18217,18218,18219,18220,18221,18222,18223,18224,18225,18226,18227,18228,18229,18230,18231,18232,18233,18234,18235,18236,18237,18238,18239,18240,18241,18242,18243,18244,18245,18246,18247,18248,18249,18250,18251,18252,18253,18254,18255,18256,18257,18258,18259,18260,18261,18262,18263,18264,18265,18266,18267,18268,18269,18270,18271,18272,18273,18274,18275,18276,18277,18278,18279,18280,18281,18282,18283,18284,18285,18286,18287,18288,18289,18290,18291,18292,18293,18294,18295,18296,18297,18298,18299,18300,18301,18302,18303,18304,18305,18306,18307,18308,18309,18310,18311,18312,18313,18314,18315,18316,18317,18318,18319,18320,18321,18322,18323,18324,18325,18326,18327,18328,18329,18330,18342,18343,18344,18345,18346,18347,18348,18349,18350,18351,18352,18353,18354,18355,18356,18357,18358,18359,18360,18361,18362,18363,18364,18365,18366,18367,18368,18369,18370,18371,18372,18373,18374,18375,18376,18377,18378,18379,18380,18381,18382,18383,18384,18385,18386,18388,18389,18390,18391,18392,18393,18394,18395,18396,18397,18398,18399,18400,18401,18402,18403,18404,18405,18406,18407,18408,18409,18410,18411,18412,18413,18414,18415,18416,18417,18418,18419,18420,18421,18422,18423,18424,18425,18426,18427,18428,18429,18430,18431,18432,18433,18434,18435,18436,18437,18438,18439,18440,18441,18442,18443,18444,18445,18446,18447,18448,18449,18450,18451,18452,18453,18454,18455,18456,18457,18458,18459,18460,18461,18462,18463,18464,18465,18466,18467,18468,18469,18470,18471,18472,18473,18474,18475,18476,18477,18478,18479,18480,18481,18482,18483,18484,18485,18486,18487,18488,18489,18490,18491,18492,18493,18494,18495,18496,18497,18498,18499,18500,18501,18502,18503,18504,18505,18506,18507,18508,18509,18510,18511,18512,18513,18514,18515,18516,18517,18518,18520,18521,18522,18523,18524,18525,18526,18527,18528,18529,18530,18531,18532,18533,18534,18535,18536,18537,18538,18539,18540,18541,18542,18543,18544,18545,18546,18547,18548,18549,18550,18551,18552,18553,18554,18555,18556,18557,18558,18559,18560,18561,18562,18563,18564,18565,18566,18567,18568,18569,18570,18571,18572,18573,18574,18575,18576,18577,18578,18579,18580,18581,18582,18583,18584,18585,18586,18587,18588,18589,18590,18591,18592,18593,18594,18595,18596,18597,18598,18599,18600,18601,18602,18603,18604,18605,18606,18607,18608,18609,18610,18611,18612,18613,18614,18615,18616,18617,18618,18619,18620,18621,18622,18623,18624,18625,18626,18627,18628,18629,18630,18631,18632,18633,18634,18635,18636,18637,18638,18639,18640,18641,18642,18643,18644,18645,18646,18647,18648,18649,18650,18651,18653,18654,18655,18656,18657,18658,18659,18660,18661,18662,18663,18664,18665,18666,18667,18668,18669,18670,18671,18672,18673,18674,18675,18676,18677,18678,18679,18680,18681,18682,18683,18684,18685,18686,18687,18688,18689,18690,18691,18692,18693,18694,18695,18696,18697,18698,18699,18700,18701,18702,18703,18704,18705,18706,18707,18708,18709,18710,18711,18712,18713,18714,18715,18716,18717,18718,18719,18720,18721,18722,18723,18724,18725,18726,18727,18728,18729,18730,18731,18732,18733,18734,18735,18736,18737,18738,18739,18740,18741,18742,18743,18744,18745,18746,18747,18748,18749,18750,18751,18752,18753,18754,18755,18756,18757,18758,18759,18760,18761,18762,18763,18764,18765,18766,18767,18768,18769,18770,18771,18772,18773,18774,18775,18776,18778,18779,18780,18781,18782,18783,18784,18785,18786,18787,18788,18789,18790,18791,18792,18793,18794,18795,18796,18797,18798,18799,18800,18801,18802,18803,18804,18805,18806,18807,18808,18809,18810,18811,18812,18813,18814,18815,18816,18817,18818,18819,18820,18821,18822,18823,18824,18825,18826,18827,18828,18829,18830,18831,18832,18833,18834,18835,18836,18837,18838,18839,18840,18841,18842,18843,18844,18845,18846,18847,18848,18849,18850,18851,18852,18853,18854,18855,18856,18857,18858,18859,18860,18861,18862,18863,18864,18865,18866,18867,18868,18869,18870,18871,18872,18873,18874,18875,18876,18877,18878,18879,18880,18881,18882,18883,18884,18885,18886,18887,18888,18889,18890,18891,18892,18893,18894,18895,18896,18897,18898,18899,18900,18901,18902,18903,18904,18905,18906,18907,18908,18909,18910,18911,18912,18913,18914,18915,18916,18917,18918,18919,18920,18921,18922,18923,18924,18925,18926,18927,18928,18929,18930,18931,18932,18933,18934,18935,18937,18938,18939,18940,18941,18942,18943,18944,18945,18946,18947,18948,18949,18950,18951,18952,18953,18954,18955,18956,18957,18958,18959,18960,18961,18962,18963,18964,18965,18966,18967,18968,18969,18970,18971,64,80,98,145,184,194,204,293,295,334,410,418,428,445,454,455,484,543,545,558,579,672,688,712,734,738,743,747,748,753,764,767,768,772,773,774,775,777,778,782,785,786,788,789,791,793,795,797,798,800,805,807,827,828,831,832,855,863,874,877,888,889,891,894,895,904,905,911,912,925,954,964,967,968,969,985,987,988,991,992,994,1004,1005,1007,1009,1010,1022,1081,1116,1117,1201,1255,1300,1310,1337,1349,1391,1413,1422,1435,1447,1449,1451,1452,1453,1466,1467,1469,1474,1488,1489,1491,1495,1509,1514,1515,1530,1533,1534,1546,1547,1550,1551,1554,1565,1566,1570,1574,1591,1593,1605,1607,1608,1609,1624,1625,1626,1627,1628,1629,1640,1642,1643,1644,1646,1647,1648,1659,1660,1661,1664,1665,1666,1679,1684,1695,1698,1700,1707,1711,1712,1713,1714,1716,1718,1719,1720,1731,1732,1734,1736,1737,1758,1759,1760,1761,1763,1766,1777,1781,1784,1793,1795,1797,1798,1803,1808,1812,1814,1815,1816,1817,1819,1820,1821,1830,1832,1834,1835,1836,1837,1847,1848,1849,1850,1851,1852,1853,1854,1865,1939,1954,1980,2015,2016,2028,2076,2077,2102,2119,2133,2209,2234,2250,2261,2320,2333,2335,2343,2350,2353,2354,2360,2365,2386,2387,2388,2424,2444,2461,2466,2468,2483,2484,2485,2499,2501,2508,2514,2522,2525,2527,2528,2529,2530,2534,2535,2539,2540,2542,2543,2544,2547,2552,2555,2557,2558,2563,2574,2575,2576,2586,2592,2593,2595,2601,2612,2622,2623,2625,2629,2646,2647,2648,2650,2657,2659,2660,2661,2662,2663,2666,2667,2668,2670,2671,2672,2673,2676,2677,2680,2681,2682,2685,2687,2691,2692,2693,2698,2700,2701,2702,2704,2707,2708,2711,2713,2714,2717,2727,2743,2745,2748,2751,2764,2765,2776,2779,2782,2790,2791,2793,2794,2801,2804,2805,2806,2807,2810,2811,2812,2817,2818,2820,2821,2822,2824,2825,2827,2832,2833,2834,2835,2838,2842,2846,2857,2859,2860,2862,2865,2866,2869,2873,2874,2875,2879,2881,2882,2883,2888,2889,2891,2893,2900,2902,2905,2907,2909,2910,2911,2913,2914,2915,2917,2918,2919,2922,2923,2924,2932,2936,2940,2942,2946,2947,2952,2954,2956,2958,2960,2961,2962,2963,2972,2975,2980,2981,2987,2989,2990,2993,2994,2997,2999,3001,3002,3003,3006,3007,3009,3010,3013,3018,3021,3023,3026,3027,3029,3037,3039,3045,3047,3055,3057,3062,3063,3068,3073,3074,3076,3082,3084,3087,3088,3091,3092,3093,3095,3097,3100,3109,3110,3111,3113,3114,3117,3120,3121,3125,3126,3131,3132,3134,3135,3138,3143,3144,3145,3146,3147,3151,3154,3156,3161,3162,3167,3179,3180,3181,3183,3185,3186,3187,3200,3207,3208,3225,3226,3227,3228,3229,3230,3235,3238,3241,3242,3243,3245,3259,3261,3262,3263,3267,3268,3270,3276,3290,3293,3295,3296,3298,3299,3300,3304,3311,3312,3314,3315,3319,3323,3325,3327,3336,3338,3340,3341,3342,3343,3345,3350,3352,3356,3357,3360,3369,3370,3372,3374,3376,3378,3385,3387,3389,3390,3391,3392,3393,3394,3397,3398,3403,3404,3405,3406,3407,3416,3418,3419,3421,3429,3436,3438,3443,3446,3447,3456,3458,3464,3465,3468,3472,3473,3475,3478,3480,3481,3482,3484,3485,3490,3493,3494,3495,3498,3501,3502,3504,3505,3507,3508,3509,3510,3511,3512,3515,3517,3518,3526,3533,3535,3538,3540,3541,3543,3544,3546,3549,3550,3551,3552,3553,3556,3559,3560,3562,3564,3565,3566,3568,3572,3573,3575,3589,3596,3607,3614,3616,3619,3636,3647,3651,3658,3659,3663,3664,3665,3673,3674,3676,3678,3679,3682,3685,3691,3694,3696,3698,3700,3701,3705,3709,3711,3716,3720,3722,3723,3724,3725,3726,3727,3728,3731,3735,3740,3746,3750,3751,3752,3753,3754,3755,3756,3757,3760,3761,3762,3763,3764,3765,3766,3767,3768,3788,3789,3798,3799,3800,3811,3812,3813,3814,3815,3824,3825,3826,3827,3829,3830,3831,3832,3833,3834,3838,3848,3851,3855,3858,3859,3860,3861,3862,3865,3867,3869,3871,3873,3876,3878,3881,3895,3899,3900,3902,3904,3905,3906,3910,3917,3920,3921,3923,3927,3928,3930,3934,3941,3943,3944,3953,3954,3958,3960,3966,3974,3975,3977,3978,3987,3989,3998,4006,4009,4021,4023,4024,4025,4036,4037,4048,4055,4059,4069,4091,4116,4124,4125,4126,4146,4161,4172,4180,4181,4195,4196,4199,4206,4207,4218,4223,4231,4237,4248,4249,4251,4267,4268,4269,4287,4289,4290,4291,4305,4306,4307,4321,4322,4323,4325,4338,4342,4343,4353,4361,4376,4377,4378,4380,4393,4395,4413,4414,4416,4417,4433,4434,4435,4448,4449,4461,4466,4468,4469,4470,4471,4483,4484,4485,4503,4504,4505,4517,4518,4521,4538,4540,4542,4558,4559,4560,4585,4624,4629,4639,4642,4647,4690,4713,4721,4723,4726,4731,4732,4733,4756,4775,4787,4810,4819,4826,4837,4838,4843,4844,4855,4856,4866,4868,4874,4879,4891,4895,4896,4897,4899,4900,4903,4906,4909,4910,4912,4919,4928,4930,4944,4945,4946,4951,4954,4962,4969,4984,4988,5002,5003,5005,5029,5032,5033,5037,5044,5045,5058,5091,5108,5109,5136,5174,5177,5181,5183,5204,5205,5206,5214,5216,5225,5244,5265,5266,5272,5273,5276,5284,5297,5306,5307,5315,5317,5318,5319,5320,5322,5323,5326,5335,5338,5341,5349,5351,5356,5357,5361,5366,5370,5375,5378,5382,5383,5387,5393,5394,5395,5396,5399,5400,5401,5406,5407,5409,5430,5442,5445,5450,5451,5457,5459,5460,5467,5481,5494,5499,5502,5505,5507,5508,5536,5538,5543,5547,5562,5567,5571,5576,5578,5580,5581,5608,5609,5612,5613,5634,5647,5649,5692,5695,5714,5716,5717,5719,5734,5751,5753,5756,5759,5768,5780,5781,5782,5783,5784,5785,5794,5797,5798,5800,5809,5810,5812,5814,5823,5827,5852,5854,5858,5866,5867,5868,5870,5871,5872,5890,5892,5896,5898,5905,5908,5909,5932,5947,5949,5961,5970,5973,5993,6004,6015,6018,6035,6038,6039,6059,6072,6081,6083,6086,6093,6094,6100,6101,6112,6116,6130,6132,6133,6137,6149,6150,6151,6152,6153,6154,6167,6170,6175,6177,6181,6182,6187,6192,6193,6195,6203,6204,6209,6213,6223,6224,6235,6237,6238,6240,6241,6252,6254,6262,6270,6275,6278,6279,6284,6293,6294,6295,6327,6335,6341,6349,6350,6357,6365,6366,6397,6399,6418,6419,6455,6456,6466,6468,6496,6497,6500,6501,6508,6515,6521,6537,6546,6547,6548,6549,6553,6554,6564,6583,6586,6602,6603,6606,6614,6621,6624,6625,6631,6642,6645,6653,6660,6661,6662,6663,6664,6673,6680,6681,6683,6684,6697,6711,6712,6713,6715,6716,6721,6722,6723,6724,6725,6728,6729,6739,6758,6759,6763,6770,6776,6783,6787,6788,6789,6790,6792,6807,6809,6811,6828,6838,6843,6846,6847,6861,6863,6867,6870,6883,6892,6905,6920,6921,6922,6951,6960,6978,6979,7000,7013,7014,7036,7045,7048,7050,7062,7068,7069,7088,7091,7100,7117,7124,7157,7158,7159,7160,7161,7163,7171,7174,7175,7201,7233,7237,7238,7258,7277,7278,7280,7283,7298,7300,7301,7303,7304,7308,7314,7322,7327,7343,7344,7365,7370,7383,7389,7406,7407,7409,7411,7413,7415,7416,7417,7418,7420,7421,7422,7423,7447,7451,7456,7503,7505,7536,7581,7600,7629,7667,7670,7687,7699,7715,7716,7725,7726,7735,7749,7751,7752,7755,7756,7759,7762,7765,7771,7777,7779,7782,7783,7785,7798,7799,7802,7805,7809,7816,7820,7822,7824,7829,7832,7833,7838,7858,7862,7875,7890,7891,7892,7897,7901,7902,7903,7904,7905,7906,7907,7909,7910,7912,7914,7916,7917,7918,7919,7920,7921,7923,7924,7925,7927,7929,7931,7933,7937,7949,7958,7978,7980,7985,7989,7995,8014,8020,8029,8030,8038,8039,8042,8043,8064,8071,8077,8081,8083,8085,8089,8096,8100,8101,8102,8107,8109,8119,8128,8134,8137,8138,8145,8146,8148,8154,8156,8162,8163,8168,8169,8172,8182,8183,8184,8188,8195,8196,8198,8199,8202,8205,8206,8211,8212,8213,8218,8219,8220,8221,8222,8224,8225,8226,8229,8230,8231,8247,8251,8254,8285,8290,8314,8320,8324,8326,8327,8328,8340,8377,8381,8385,8386,8393,8394,8408,8411,8422,8435,8452,8474,8479,8487,8488,8489,8491,8495,8509,8513,8520,8523,8527,8535,8540,8541,8542,8552,8555,8556,8561,8564,8568,8570,8578,8580,8581,8589,8598,8599,8602,8603,8606,8607,8610,8611,8613,8614,8619,8621,8624,8636,8641,8648,8649,8652,8653,8657,8658,8796,8797,8807,8816,8821,8822,8826,8852,8853,8866,8877,8879,10367,10386,10407,10601,10694,10700,10753,10763,10764,10826,10829,10858,10861,10968,10975,11041,11072,11103,11160,11167,11181,11236,11248,11249,11269,11291,11314,11490,11591,11694,11695,11738,11813,11825,11905,11929,11937,12015,12035,12048,12068,12129,12153,12190,12285,12299,12322,12347,12351,12388,12390,12402,12431,12441,12520,12544,12592,12627,12731,12787,12865,12912,12940,13011,13014,13019,13028,13044,13046,13142,13148,13154,13169,13222,13286,13309,13312,13318,13324,13325,13326,13392,13397,13398,13404,13415,13468,13482,13484,13495,13496,13528,13532,13534,13554,13555,13561,13576,13580,13601,13652,13672,13686,13697,13713,13714,13717,13728,13734,13762,13766,13767,13768,13777,13778,13779,13797,13798,13800,13804,13816,13833,13875,13876,13879,13897,13905,13913,13919,13929,13930,13947,13960,13966,13968,13982,13993,14003,14009,14016,14018,14024,14025,14040,14056,14061,14078,14090,14095,14101,14106,14111,14135,14164,14180,14182,14186,14196,14201,14206,14207,14211,14216,14217,14222,14235,14237,14246,14248,14257,14264,14269,14311,14312,14319,14343,14358,14369,14371,14376,14379,14384,14394,14395,14398,14402,14408,14421,14430,14444,14445,14454,14459,14481,14491,14499,14509,14512,14516,14524,14526,14527,14528,14530,14532,14547,14548,14555,14558,14559,14560,14561,14562,14563,14564,14571,14573,14574,14575,14582,14584,14589,14591,14592,14593,14603,14604,14608,14609,14610,14611,14612,14613,14615,14618,14619,14621,14622,14623,14624,14625,14626,14631,14632,14636,14637,14638,14639,14642,14644,14646,14647,14648,14649,14650,14651,14654,14655,14656,14658,14661,14663,14682,14867,14874,14888,15095,15116,15235,15253,15258,15282,15300,15345,15392,15393,15396,15398,15411,15413,15437,15442,15450,15451,15453,15454,15467,15471,15472,15491,15513,15521,15524,15529,15530,15538,15544,15567,15578,15589,15604,15610,15643,15658,15684,15704,15705,15708,15735,15747,15749,15761,15764,15781,15793,15794,15816,15885,15987,16001,16029,16055,16063,16068,16098,16119,16121,16130,16138,16139,16179,16180,16183,16186 ]
        print "LENGTH OF LIST IS ", len(org_id_list)
        for org_id in org_id_list:
            org_object = OrganisationName.objects.get(id=org_id)

            try:
                mygoogleapibase = 'https://maps.googleapis.com/maps/api/geocode/json?address='
                mygoogleapikey = '&key=AIzaSyBSgwtACK4WPjYKy837g7fgaeYf6JDjxkM' # hfu key
                AddressForApi = org_object.name.strip() + ' ' + org_object.street.strip() + ' ' + org_object.city.name.strip()
                if AddressForApi and AddressForApi != '':
                    AddressForApi = AddressForApi.split(' ')
                    AddressForApi = [mm.strip() for mm in AddressForApi]
                    AddressForApi = "+".join(AddressForApi)
                mygoogleapiurl = mygoogleapibase + AddressForApi + mygoogleapikey
                import requests
                r = requests.post(mygoogleapiurl)

                rrcc = json.loads(r.content)
                if rrcc['status'] == 'ZERO_RESULTS':
                    #gformatted_address = 'ZERO_RESULTS'
                    glatitude = 'ZERO_RESULTS'
                    glongitude = 'ZERO_RESULTS'
                    left_list.append(org_id)

                if rrcc['status'] == 'OK':
                    resgoogle = rrcc['results'][0]
                    #gformatted_address = resgoogle['formatted_address']
                    glatitude = resgoogle['geometry']['location']['lat']
                    glongitude = resgoogle['geometry']['location']['lng']
                    org_object.latitude = str(glatitude).strip()
                    org_object.longitude = str(glongitude).strip()
                    org_object.save()
                    done_list.append(org_id)

            except:
                left_list.append(org_id)

            print ' -----------------------------  ', org_id

        print "Done List ", done_list
        print
        print "Left List ", left_list

        return HttpResponse("Updated Lat and Long")
    except Exception as e:
        print "%% OUTER %%%%%%%%%%%%%%%%%%%%%%%     ", e
        print e
        return HttpResponse("IN - COMPLETE")



########################
# Written By - Nishank #
########################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
def publish_live_n_old_docs_7Feb2018(request):
    try:
        from hfu_cms.data_publisher import __live_doctor_data_creation, __doctor_data_creation
        live_doctor_listids= Live_Doctor.objects.filter(stage=5,publish=True).values_list('id',flat=True)
        type == "livedoctor"
        live_doc_success_list = []
        live_doc_fail_list = []
        for idd in live_doctor_listids:
            doc_obj = Live_Doctor.objects.get(id=idd)
            data = __live_doctor_data_creation(idd)
            response = elasticsearch_client.index_data("global", 'doctor', idd, data)
            if response:
                live_doc_success_list.append(idd)
                doctor_obj = Live_Doctor.objects.filter(id=idd)
                if doctor_obj:
                    doctor_obj.update(publish=True, stage=5)
            else:
                live_doc_fail_list.append(idd)
            print " -------------------------- "
        print "Live Doc Success List > ", live_doc_success_list
        print "Live Doc Fail list > ", live_doc_fail_list

        count = 0
        doctor_listids = Doctor.objects.filter(stage_id=5,publish=True).values_list('id',flat=True)
        type == "doctor"
        doc_success_list = []
        doc_fail_list = []
        for idd in doctor_listids:
            count += 1
            doc_obj = Doctor.objects.get(id=idd)
            if doc_obj.is_disable == False:
                data = __doctor_data_creation(idd)
                response = elasticsearch_client.index_data("global", 'doctor', idd, data)
                if response:
                    doc_success_list.append(idd)
                    doctor_obj = Doctor.objects.filter(id=idd)
                    if doctor_obj:
                        doctor_obj.update(publish=True, stage=5)
                else:
                    doc_fail_list.append(idd)
            print " --------------++-------------- count = ",count
        print "Doc Success List > ", doc_success_list
        print "Doc Fail list > ", doc_fail_list


    except Exception as e:
        print "%% OUTER %%%%%%%%%%%%%%%%%%%%%%%     ", e
        print e
        return HttpResponse("IN - COMPLETE")