# -*- coding:utf-8 -*-
# import csv
# from django.views.decorators.http import require_GET, require_POST
# from hfu_cms.models import *
# from django.http import HttpResponse

import csv
from django.views.decorators.http import require_GET, require_POST
from hfu_cms.models import *
from django.http.response import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q


# @login_required(login_url='/')
# @user_passes_test(lambda u: u.is_superuser)
# @require_GET
# def get_data(request):
#     objects = Doctor.objects.all()
#     attach_objects = AttachWithDoctor.objects.all()
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename=doctor.csv'
#     # with open('doctor.csv', 'w') as csvfile:
#     if len(objects):
#         fieldnames = ['Doctor Name', 'Category', 'Current User', 'Stage', 'Action', 'Organisation Name',
#                       'Address of Organisation', 'Locality', 'Current User Org', 'Stage of Org', 'Action Org']
#         writer = csv.DictWriter(response, fieldnames=fieldnames)
#
#         writer.writeheader()
#         for i in objects:
#             if i.current_user is not None:
#                 doctor_user = i.current_user.username
#             else:
#                 doctor_user = ''
#             doctor_name = u' '.join(i.name)
#
#             attach_hospital = attach_objects.filter(doctor_id=i.id)
#             if len(attach_hospital):
#                 for j in attach_hospital:
#                     if j.organisation.current_user is not None:
#                         organisation_username = j.organisation.current_user.username
#                 else:
#                     organisation_username = ''
#                 try:
#                     address = u' '.join(j.organisation.street)
#                 except Exception as e:
#                     address = ''
#                 org_name = u' '.join(j.organisation.name)
#                 try:
#                     writer.writerow({'Doctor Name': doctor_name.encode('utf-8'), 'Category': i.category.name,
#                                      'Current User': i.current_user.username, 'Stage': i.stage.stage_name,
#                                      'Action': i.is_disable, 'Organisation Name': org_name.encode('utf-8'),
#                                      'Address of Organisation': address.encode('utf-8'),
#                                      'Locality': j.organisation.locality,
#                                      'Current User Org': organisation_username,
#                                      'Stage of Org': j.organisation.stage.stage_name,
#                                      'Action Org': j.organisation.is_disable})
#                 except Exception as e:
#                     print e
#             else:
#
#                 try:
#                     writer.writerow(
#                         {'Doctor Name': doctor_name.encode('utf-8'), 'Category': i.category.name,
#                          'Current User': doctor_user,
#                          'Stage': i.stage.stage_name, 'Action': i.is_disable, 'Organisation Name': '',
#                          'Address of Organisation': '', 'Locality': '', 'Current User Org': '', 'Stage of Org': '',
#                          'Action Org': ''})
#                 except Exception as e:
#                     pass
#     return response




@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def get_data(request):
    objects = Doctor.objects.all()
    print objects.count()
    attach_objects = AttachWithDoctor.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=doctor.csv'
    # with open('doctor.csv', 'w') as csvfile:
    if len(objects):
        fieldnames = ['id','unique_id','resource_validate','Doctor Name', 'Category', 'Current User','Previous_user','Free_text','Speciality',
                      'Service Offered','Zone','Zone Location','DOB','Mobile_no','Phone','skype_id','Email','Secondary_email', 'Stage', 'Action',
                      'Organisation Name','Doctor_experience_year','Qualification_data','is_disable','Male_doctor','female_doctor','Publish','Registration_data','Address of Organisation',
                      'Locality', 'Current User Org', 'Stage of Org', 'Action Org']
        writer = csv.DictWriter(response, fieldnames=fieldnames)

        writer.writeheader()
        countrow = 0
        for i in objects:
            prevname = ''

            countrow += 1
            #print 'countrow =', countrow

            if i.current_user is not None:
                doctor_user = i.current_user.username
            else:
                doctor_user = ''
            doctor_name = u' '.join(i.name)

            attach_hospital = attach_objects.filter(doctor_id=i.id)
            if len(attach_hospital):
                for j in attach_hospital:
                    if j.organisation.current_user is not None:
                        organisation_username = j.organisation.current_user.username
                else:
                    organisation_username = ''
                try:
                    address = u' '.join(j.organisation.street)
                except Exception as e:
                    address = ''
                org_name = u' '.join(j.organisation.name)

                uu = User.objects.all()
                for unis in uu:
                    if unis.id == i.previous_user:
                        prevname = unis.username

                strspe=''
                cc=0
                spe_all = Speciality.objects.all()
                alspe = i.speciality.split(',')
                for iiidin in alspe:
                    for iiispe in  spe_all:
                        if iiispe.id == iiidin.strip() :
                            cc= cc+1
                            if cc== 1:
                                strspe = strspe+iiispe.name
                            else:
                                strspe = ','+ strspe + iiispe.name


                strspe2 = ''
                cc = 0
                ser_all = Service_Offred.objects.all()
                alser = i.speciality.split(',')
                for iiidin in alser:
                    for iiiser in ser_all:
                        if iiiser.id == iiidin.strip():
                            cc = cc + 1
                            if cc == 1:
                                strspe2 = strspe2 + iiiser.name
                            else:
                                strspe2 = ',' + strspe2 + iiiser.name

                zonename =''
                zonelist = Zone.objects.all()
                for iz in zonelist :
                    if iz.id == i.zone_id:
                        zonename = iz.name

                zonelocatname = ''
                zonelocatlist = ZoneLocation.objects.all()
                for izl in zonelocatlist:
                    if izl.id == i.zone_location_id:
                        zonelocatname = izl.name

                rvname = ''
                rvlist = ValidateByChoice.objects.all()
                for rv in rvlist:
                    if rv.id == i.resource_validate_id :
                        rvname = rv.name

                try:
                    writer.writerow({'id':i.id,'unique_id':i.unique_id,'resource_validate':rvname,'Doctor Name': doctor_name.encode('utf-8'),
                                     'Category': i.category.name,'Current User': i.current_user.username,'Previous_user': prevname,'Free_text':i.free_text,
                                     'Speciality':strspe,'Service Offered':strspe2,'Zone':zonename,'Zone Location':zonelocatname,'DOB':i.dob,'Mobile_no':i.mobile_no,
                                     'Phone':i.phone,'skype_id':i.skype_id,'Email':i.email,'Secondary_email':i.secondary_email,
                                     'Stage': i.stage.stage_name, 'Action': i.is_disable, 'Organisation Name': org_name.encode('utf-8'),
                                     'Doctor_experience_year':i.doctor_experience_year,'Qualification_data':i.qualification_data,
                                     'is_disable':i.is_disable,'Male_doctor':i.male_doctor,'female_doctor':i.female_doctor,'Publish':i.publish,
                                     'Registration_data':i.registration_data,
                                     'Address of Organisation': address.encode('utf-8'),'Locality': j.organisation.locality,'Current User Org': organisation_username,
                                     'Stage of Org': j.organisation.stage.stage_name,'Action Org': j.organisation.is_disable})
                except Exception as e:
                    #print e
                    pass
            else:

                try:

                    uu = User.objects.all()
                    for unis in uu:
                        if unis.id == i.previous_user:
                            prevname = unis.username

                    strspe = ''
                    cc = 0
                    spe_all = Speciality.objects.all()
                    alspe = i.speciality.split(',')
                    for iiidin in alspe:
                        for iiispe in spe_all:
                            if iiispe.id == iiidin.strip():
                                cc = cc + 1
                                if cc == 1:
                                    strspe = strspe + iiispe.name
                                else:
                                    strspe = ',' + strspe + iiispe.name

                    strspe2 = ''
                    cc = 0
                    ser_all = Service_Offred.objects.all()
                    alser = i.speciality.split(',')
                    for iiidin in alser:
                        for iiiser in ser_all:
                            if iiiser.id == iiidin.strip():
                                cc = cc + 1
                                if cc == 1:
                                    strspe2 = strspe2 + iiiser.name
                                else:
                                    strspe2 = ',' + strspe2 + iiiser.name

                    zonename = ''
                    zonelist = Zone.objects.all()
                    for iz in zonelist:
                        if iz.id == i.zone_id:
                            zonename = iz.name

                    zonelocatname = ''
                    zonelocatlist = ZoneLocation.objects.all()
                    for izl in zonelocatlist:
                        if izl.id == i.zone_location_id:
                            zonelocatname = izl.name

                    rvname = ''
                    rvlist = ValidateByChoice.objects.all()
                    for rv in rvlist:
                        if rv.id == i.resource_validate_id:
                            rvname = rv.name


                    writer.writerow(
                        {'id': i.id, 'unique_id': i.unique_id, 'resource_validate': rvname,
                         'Doctor Name': doctor_name.encode('utf-8'),
                         'Category': i.category.name, 'Current User': i.current_user.username,
                         'Previous_user': prevname, 'Free_text': i.free_text,
                         'Speciality': strspe, 'Service Offered': strspe2, 'Zone': zonename,
                         'Zone Location': zonelocatname, 'DOB': i.dob, 'Mobile_no': i.mobile_no,
                         'Phone': i.phone, 'skype_id': i.skype_id, 'Email': i.email,
                         'Secondary_email': i.secondary_email,
                         'Stage': i.stage.stage_name, 'Action': i.is_disable,
                         'Organisation Name': '',
                         'Doctor_experience_year': i.doctor_experience_year, 'Qualification_data': i.qualification_data,
                         'is_disable': i.is_disable, 'Male_doctor': i.male_doctor, 'female_doctor': i.female_doctor,
                         'Publish': i.publish,
                         'Registration_data': i.registration_data,
                         'Address of Organisation': '', 'Locality': '',
                         'Current User Org': '',
                         'Stage of Org': '', 'Action Org': ''})


                    # writer.writerow(
                    #     {'Doctor Name': doctor_name.encode('utf-8'), 'Category': i.category.name,
                    #      'Current User': doctor_user,
                    #      'Stage': i.stage.stage_name, 'Action': i.is_disable, 'Organisation Name': '',
                    #      'Address of Organisation': '', 'Locality': '', 'Current User Org': '', 'Stage of Org': '',
                    #      'Action Org': ''})
                except Exception as e:
                    #print e
                    pass
    return response



                    #
                    # @require_GET
                    # def get_data(request):
                    #     objects = Doctor.objects.all()
                    #     attach_objects = AttachWithDoctor.objects.all()
                    #     response = HttpResponse(content_type='text/csv')
                    #     response['Content-Disposition'] = 'attachment; filename=doctor.csv'
                    #     # with open('doctor.csv', 'w') as csvfile:
                    #     if len(objects):
                    #         fieldnames = ['Doctor Name', 'Category', 'Current User', 'Stage', 'Action', 'Organisation Name',
                    #                       'Address of Organisation', 'Locality', 'Current User Org', 'Stage of Org', 'Action Org']
                    #         writer = csv.DictWriter(response, fieldnames=fieldnames)
                    #
                    #         writer.writeheader()
                    #         for i in objects:
                    #             if i.current_user is not None:
                    #                 doctor_user = i.current_user.username
                    #             else:
                    #                 doctor_user = ''
                    #             attach_hospital = attach_objects.filter(doctor_id=i.id)
                    #             if len(attach_hospital):
                    #                 for j in attach_hospital:
                    #                     if j.organisation.current_user is not None:
                    #                         organisation_username = j.organisation.current_user.username
                    #                     else:
                    #                         organisation_username = ''
                    #                     try:
                    #                         address = u' '.join(j.organisation.street)
                    #                     except Exception as e:
                    #                         address = ''
                    #                     org_name = u' '.join(j.organisation.name)
                    #                     try:
                    #                         writer.writerow({'Doctor Name': i.name, 'Category': i.category.name,
                    #                                          'Current User': doctor_user, 'Stage': i.stage.stage_name,
                    #                                          'Action': i.is_disable, 'Organisation Name': org_name.encode('utf-8'),
                    #                                          'Address of Organisation': address.encode('utf-8'),
                    #                                          'Locality': j.organisation.locality,
                    #                                          'Current User Org': organisation_username,
                    #                                          'Stage of Org': j.organisation.stage.stage_name,
                    #                                          'Action Org': j.organisation.is_disable})
                    #                     except Exception as e:
                    #                         print e
                    #             else:
                    #
                    #                 try:
                    #                     writer.writerow(
                    #                         {'Doctor Name': i.name, 'Category': i.category.name, 'Current User': doctor_user,
                    #                          'Stage': i.stage.stage_name, 'Action': i.is_disable, 'Organisation Name': '',
                    #                          'Address of Organisation': '', 'Locality': '', 'Current User Org': '', 'Stage of Org': '',
                    #                          'Action Org': ''})
                    #                 except Exception as e:
                    #                     pass
                    #     return response


                    # @require_GET
                    # def get_data_organisation(request):
                    #     objects = Doctor.objects.all()
                    #     attach_objects = AttachWithDoctor.objects.all()
                    #     response = HttpResponse(content_type='text/csv')
                    #     response['Content-Disposition'] = 'attachment; filename=doctor.csv'
                    #     # with open('doctor.csv', 'w') as csvfile:
                    #     if len(objects):
                    #         fieldnames = ['Doctor Name', 'Category', 'Current User', 'Stage', 'Action', 'Organisation Name',
                    #                       'Address of Organisation', 'Locality', 'Current User Org', 'Stage of Org', 'Action Org']
                    #         writer = csv.DictWriter(response, fieldnames=fieldnames)
                    #
                    #         writer.writeheader()
                    #         for i in objects:
                    #             attach_hospital = attach_objects.filter(doctor_id=i.id)
                    #             if len(attach_hospital):
                    #                 for j in attach_hospital:
                    #                     try:
                    #                         writer.writerow({'Doctor Name': i.name, 'Category': i.category.name,
                    #                                          'Current User': i.current_user.username, 'Stage': i.stage.stage_name,
                    #                                          'Action': i.is_disable, 'Organisation Name': j.organisation.name,
                    #                                          'Address of Organisation': j.organisation.street,
                    #                                          'Locality': j.organisation.locality,
                    #                                          'Current User Org': j.organisation.current_user.username,
                    #                                          'Stage of Org': j.organisation.stage.stage_name,
                    #                                          'Action Org': j.organisation.is_disable})
                    #                     except Exception as e:
                    #                         print e
                    #             else:
                    #
                    #                 try:
                    #                     writer.writerow(
                    #                         {'Doctor Name': i.name, 'Category': i.category.name, 'Current User': i.current_user.username,
                    #                          'Stage': i.stage.stage_name, 'Action': i.is_disable, 'Organisation Name': '',
                    #                          'Address of Organisation': '', 'Locality': '', 'Current User Org': '', 'Stage of Org': '',
                    #                          'Action Org': ''})
                    #                 except Exception as e:
                    #                     pass
                    #     return response


@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def get_data_org(request):
    objects = OrganisationName.objects.all()
    #attach_objects = AttachWithDoctor.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Hospital.csv'
    # with open('doctor.csv', 'w') as csvfile:
    if len(objects):
        fieldnames = ['id','resource_validate','facility','Hospital Name', 'Category', 'Current User','Previous_user','Free_text',
                      'Service Offered','Zone','Zone Location','DOB','Mobile_no','Phone','skype_id','Email','Secondary_email', 'Stage', 'Action',
                      'Organisation Name','Doctor_experience_year','Qualification_data','is_disable','Male_doctor','female_doctor','Publish','Registration_data','Address of Organisation',
                      'Locality', 'Current User Org', 'Stage of Org', 'Action Org']
        writer = csv.DictWriter(response, fieldnames=fieldnames)

        writer.writeheader()
        countrow = 0
        for i in objects:
            prevname = ''

            countrow += 1
            #print 'countrow =', countrow

            if i.current_user is not None:
                hospital_user = i.current_user.username
            else:
                hospital_user = ''
            hospital_name = u' '.join(i.name)


            if i.facility != [] or i.facility != '' or i.facility != None :
                fac_str =''
                ava_facility = i.facility
                ava_facility_list = ava_facility.split(',')
                master_facility_list = Facility.objetcs.all()
                cf=0
                for afac in ava_facility_list :
                    for mfac in master_facility_list :
                        if afac.strip() == mfac.id:
                            cf += 1
                            if cf == 1:
                                fac_str = fac_str + mfac.name
                            else:
                                fac_str = ',' + fac_str + mfac.name



            uu = User.objects.all()
            for unis in uu:
                if unis.id == i.previous_user:
                    prevname = unis.username

            strspe=''
            cc=0
            spe_all = Speciality.objects.all()
            alspe = i.speciality.split(',')
            for iiidin in alspe:
                for iiispe in  spe_all:
                    if iiispe.id == iiidin.strip() :
                        cc= cc+1
                        if cc== 1:
                            strspe = strspe+iiispe.name
                        else:
                            strspe = ','+ strspe + iiispe.name


            strspe2 = ''
            cc = 0
            ser_all = Service_Offred.objects.all()
            alser = i.speciality.split(',')
            for iiidin in alser:
                for iiiser in ser_all:
                    if iiiser.id == iiidin.strip():
                        cc = cc + 1
                        if cc == 1:
                            strspe2 = strspe2 + iiiser.name
                        else:
                            strspe2 = ',' + strspe2 + iiiser.name

            zonename =''
            zonelist = Zone.objects.all()
            for iz in zonelist :
                if iz.id == i.zone_id:
                    zonename = iz.name

            zonelocatname = ''
            zonelocatlist = ZoneLocation.objects.all()
            for izl in zonelocatlist:
                if izl.id == i.zone_location_id:
                    zonelocatname = izl.name

            rvname = ''
            rvlist = ValidateByChoice.objects.all()
            for rv in rvlist:
                if rv.id == i.resource_validate_id :
                    rvname = rv.name

            try:
                writer.writerow({'id':i.id,'resource_validate':rvname,'facility':fac_str ,'Hospital Name': hospital_name.encode('utf-8'),
                                 'Category': i.category.name,'Current User': i.current_user.username,'Previous_user': prevname,'Free_text':i.free_text,
                                 'Service Offered':strspe2,'Zone':zonename,'Zone Location':zonelocatname,'DOB':i.dob,'Mobile_no':i.mobile_no,
                                 'Phone':i.phone,'skype_id':i.skype_id,'Email':i.email,'Secondary_email':i.secondary_email,
                                 'Stage': i.stage.stage_name, 'Action': i.is_disable, 'Organisation Name': hospital_name.encode('utf-8'),
                                 'Doctor_experience_year':i.doctor_experience_year,'Qualification_data':i.qualification_data,
                                 'is_disable':i.is_disable,'Male_doctor':i.male_doctor,'female_doctor':i.female_doctor,'Publish':i.publish,
                                 'Registration_data':i.registration_data,
                                 'Address of Organisation': address.encode('utf-8'),'Locality': j.organisation.locality,'Current User Org': organisation_username,
                                 'Stage of Org': j.organisation.stage.stage_name,'Action Org': j.organisation.is_disable})
            except Exception as e:
                #print e
                pass

    return response

#######################
#Written By - Nishank #
#######################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def get_docs_attached_with_orgs(request):
    attached_doc_records = AssociateDoctorWithOrganization.objects.all().order_by('id')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Org_n_attached_docs.csv'
    # with open('org_attached_docs.csv', 'w') as csvfile:

    if len(attached_doc_records):
        count = 0
        fieldnames = ['Organisation id','doctor_id','Organisation Name','Organisation City','Organisation Locality','Organisation Address','Organisation Phone','Organisation Mobile','Department Name',
                      'Doctor Name','Doctor Category','Doctor Speciality',
                      'Doctor current user','Doctor current stage']
        writer = csv.DictWriter(response, fieldnames=fieldnames)

        writer.writeheader()
        countrow = 0
        l = []
        for i in attached_doc_records:
            count += 1

            hospital_name = i.organisation.name
            department_name = i.department.name
            doctor_name = i.doctor.name
            org_city_name = i.organisation.city.name
            org_locality_name = i.organisation.locality.name
            org_address = i.organisation.street
            org_phone = i.organisation.phone
            org_mobile = i.organisation.mobile_no
            doc_category = i.doctor.category.name
            doc_speciality = i.doctor.speciality
            doc_currrent_user = i.doctor.current_user.username
            doc_currrent_stage = i.doctor.stage.stage_name

            try:
                writer.writerow({'Organisation id':i.organisation.id,'doctor_id':i.doctor.id,'Organisation Name': hospital_name.encode('utf-8'),'Organisation City':org_city_name.encode('utf-8'),
                                 'Organisation Locality':org_locality_name.encode('utf-8'),'Organisation Address':org_address.encode('utf-8'),
                                 'Organisation Phone':org_phone.encode('utf-8'),'Organisation Mobile':org_mobile.encode('utf-8'),
                                 'Department Name':department_name.encode('utf-8'),'Doctor Name':doctor_name.encode('utf-8'),
                                 'Doctor Category':doc_category.encode('utf-8'),'Doctor Speciality':doc_speciality.encode('utf-8'),
                                 'Doctor current user':doc_currrent_user.encode('utf-8'),'Doctor current stage':doc_currrent_stage.encode('utf-8')
                                 })
                #print count, i.id
            except Exception as e:
                #print "MISSSSSSSSSSSSSEDDDDDD",e,i.id
                l.append[i.id]
        #print l

    return response

#######################
#Written By - Nishank #
#######################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def docs_sch_missin_endtime(request):
    all_schedule_list = Schedule.objects.all().order_by('doctor_id')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=docs_sch_missin_endtime.csv'
    # with open('org_attached_docs.csv', 'w') as csvfile:
    if len(all_schedule_list):
        count = 0
        fieldnames = ['Doctor id', 'Doctor Name', 'Doctor Category', 'Doctor current user', 'Doctor current stage',
                      'Organisation id','Organisation Name', 'Times'
                      ]
        writer = csv.DictWriter(response, fieldnames=fieldnames)

        writer.writeheader()

        for schedule_single_object in all_schedule_list:
            sch = schedule_single_object.schedule_data
            overall_count = 0
            present = 'No'
            for i in sch:
                t = i['timing']
                for j in t:
                    if j['end_time'] == '' or j['end_time'] == ' ':
                        present = 'yes'
                        overall_count += 1

            if present == 'yes':
                doctor_id = schedule_single_object.doctor.id
                doctor_name = schedule_single_object.doctor.name
                doctor_category = schedule_single_object.doctor.category.name
                doctor_currentUser = schedule_single_object.doctor.current_user.username
                doctor_stage = schedule_single_object.doctor.stage.stage_name
                organisation_id = schedule_single_object.organisation.id
                organisation_name = schedule_single_object.organisation.name
                try:
                    writer.writerow({
                        'Doctor id': doctor_id, 'Doctor Name': doctor_name.encode('utf-8'),
                        'Doctor Category': doctor_category.encode('utf-8'),
                        'Doctor current user': doctor_currentUser.encode('utf-8'),
                        'Doctor current stage': doctor_stage.encode('utf-8'),
                        'Organisation id': organisation_id,
                        'Organisation Name': organisation_name.encode('utf-8'), 'Times': overall_count

                    })
                except Exception as e:
                    #print e
                    pass


    return response


#######################
#Written By - Nishank #
#######################
@login_required(login_url='/')
@require_GET
def org_without_attached_docs(request):
    Org_list = OrganisationName.objects.filter(current_user_id=request.user.id,is_disable=False)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=org_without_attached_docs.csv'
    # with open('org_attached_docs.csv', 'w') as csvfile:
    if len(Org_list):
        count = 0
        fieldnames = ['Organisation id', 'Organisation Name', 'Organisation current Stage', 'Organisation current Username' ,'PUBLISH']
        writer = csv.DictWriter(response, fieldnames=fieldnames)
        writer.writeheader()

        id_list_of_orgs_in_associatedocwithorg  = AssociateDoctorWithOrganization.objects.all().values('id')

        for org in Org_list:
            organisation_id = org.id
            if organisation_id not in id_list_of_orgs_in_associatedocwithorg :
                organisation_name = org.name
                organisation_current_stage = org.stage.stage_name
                organisation_current_user = org.current_user.username
                organisation_publish_status = org.publish
                count +=1
                print count
                try:
                    writer.writerow({
                        'Organisation id': organisation_id, 'Organisation Name': organisation_name.encode('utf-8'),
                        'Organisation current Stage': organisation_current_stage.encode('utf-8'),
                        'Organisation current Username': organisation_current_user.encode('utf-8'),
                        'PUBLISH': organisation_publish_status,

                    })
                except Exception as e:
                    #print organisation_id, organisation_name,
                    #print e
                    pass

    return response



#######################
#Written By - Nishank #
#######################
@require_GET
@login_required(login_url='/')
def org_without_emails(request):
    Org_list = OrganisationName.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=org_without_emails.csv'
    # with open('org_attached_docs.csv', 'w') as csvfile:
    if len(Org_list):
        count = 0
        fieldnames = ['Organisation id', 'Organisation Name', 'Organisation current Stage', 'Organisation current Username','PUBLISH']
        writer = csv.DictWriter(response, fieldnames=fieldnames)
        writer.writeheader()

        for org in Org_list:
            organisation_id = org.id
            if org.email == None or org.email == [] or org.email == '' or org.email == ' ':
                organisation_name = org.name
                organisation_current_stage = org.stage.stage_name
                organisation_current_user = org.current_user.username
                organisation_publish_status = org.publish
                count +=1

                try:
                    writer.writerow({
                        'Organisation id': organisation_id, 'Organisation Name': organisation_name.encode('utf-8'),
                        'Organisation current Stage': organisation_current_stage.encode('utf-8'),
                        'Organisation current Username': organisation_current_user.encode('utf-8'),
                        'PUBLISH': organisation_publish_status,

                    })
                except Exception as e:
                    #print organisation_id, organisation_name,
                    #print e
                    pass
        #print count
    return response



#######################
#Written By - Nishank #
#######################
@require_GET
@login_required(login_url='/')
def org_category_ayurveda(request):
    Org_list = OrganisationName.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=org_category_ayurveda.csv'
    # with open('org_attached_docs.csv', 'w') as csvfile:
    if len(Org_list):
        count = 0
        fieldnames = ['Organisation id', 'Organisation Name', 'Organisation current Stage', 'Organisation current Username','PUBLISH','IS_DISABLE','State','City','Locality','Street', 'Pincode', 'Phone']
        writer = csv.DictWriter(response, fieldnames=fieldnames)
        writer.writeheader()

        for org in Org_list:
            type_str = ''
            type_str = org.type
            if type_str != '' and type_str != ' ' and type_str != [] and type_str != None:
                type_str = type_str.strip()
                type_list = []
                type_list = type_str.split(',')

                if 'Ayurveda' in type_list :
                    organisation_id = org.id
                    organisation_name = org.name
                    organisation_current_stage = org.stage.stage_name
                    organisation_current_user = org.current_user.username
                    organisation_publish_status = org.publish
                    organisation_activation_status = org.is_disable
                    state = org.state.name
                    city = org.city.name
                    locality = org.locality.name
                    street = org.street
                    pincode = org.pincode
                    phone = org.phone

                    count +=1

                    try:
                        writer.writerow({
                            'Organisation id': organisation_id, 'Organisation Name': organisation_name.encode('utf-8'),
                            'Organisation current Stage': organisation_current_stage.encode('utf-8'),
                            'Organisation current Username': organisation_current_user.encode('utf-8'),
                            'PUBLISH': organisation_publish_status,
                            'IS_DISABLE': organisation_activation_status,
                            'State' : state.encode('utf-8'),
                            'City' : city.encode('utf-8'),
                            'Locality' : locality.encode('utf-8'),
                            'Street' : street.encode('utf-8'),
                            'Pincode' :pincode.encode('utf-8'),
                            'Phone' :phone.encode('utf-8'),

                        })
                    except Exception as e:
                        #print organisation_id, organisation_name,
                        #print e
                        pass
        #print count
    return response


#######################
#Written By - Nishank #    I HAVE CHANGED THIS TO INSTEAD EXPORT ALL DOCTORS IN 'Publisher' id = 12 user Login
#######################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def published_doc_mumbai(request):
    try:
        doc_records = Doctor.objects.filter(current_user_id=12).order_by('id')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=docs_Publisher_login.csv'
        # with open('org_attached_docs.csv', 'w') as csvfile:

        if len(doc_records):
            fieldnames = ['Doctor id','Doctor Name','Doctor Category','Doctor Mobile','Doctor Phone','Doctor Did','Doctor Extension','Doctor IsDisable',
                          'Attached Organisation id','Attached Organisation Name','Attached Organisation City','Attached Organisation Locality',
                          'Attached Organisation Did','Attached Organisation Extension','Attached Organisation Consultancy Fee',
                          'Attached Organisation Phone','Attached Organisation Mobile','Attached Organisation Current User'
                          ]
            writer = csv.DictWriter(response, fieldnames=fieldnames)

            writer.writeheader()

            for i in doc_records:
                attached_orgs = AttachWithDoctor.objects.filter(doctor_id =  i.id)
                if list(attached_orgs) != []:
                    for j in attached_orgs:
                        org =  OrganisationName.objects.get(id= j.organisation_id)
                        if org.state_id == 1 and org.city_id == 1:
                            doctor_id = i.id
                            doctor_name = i.name
                            doctor_category = i.category.name
                            doctor_mobile = i.mobile_no
                            doctor_phone = i.phone
                            doctor_did = i.did
                            doctor_extension = i.extension


                            attached_org_id = org.id
                            attached_org_name = org.name
                            attached_org_city_name = org.city.name
                            attached_org_locality_name = org.locality.name
                            attached_org_did = j.did
                            attached_org_extension = j.extension
                            attached_org_con_fee = j.consultancy_fee
                            attached_org_phone = org.phone
                            attached_org_mobile = org.mobile_no
                            attached_current_user = org.current_user.username

                            try:
                                writer.writerow({'Doctor id':doctor_id,'Doctor Name':doctor_name.encode('utf-8'),
                                                 'Doctor Category':doctor_category.encode('utf-8'),
                                                 'Doctor Mobile':doctor_mobile.encode('utf-8'),'Doctor Phone':doctor_phone.encode('utf-8'),
                                                 'Doctor Did':doctor_did.encode('utf-8'),'Doctor Extension':doctor_extension.encode('utf-8'),
                                                 'Doctor IsDisable': i.is_disable,
                                                 'Attached Organisation id': attached_org_id,'Attached Organisation Name':attached_org_name.encode('utf-8'),
                                                 'Attached Organisation City':attached_org_city_name.encode('utf-8'),
                                                 'Attached Organisation Locality':attached_org_locality_name.encode('utf-8'),
                                                 'Attached Organisation Did':attached_org_did.encode('utf-8'),
                                                 'Attached Organisation Extension':attached_org_extension.encode('utf-8'),
                                                 'Attached Organisation Consultancy Fee':attached_org_con_fee.encode('utf-8'),
                                                 'Attached Organisation Phone':attached_org_phone.encode('utf-8'),
                                                 'Attached Organisation Mobile':attached_org_mobile.encode('utf-8'),
                                                 'Attached Organisation Current User':attached_current_user.encode('utf-8')
                                                 })
                            except Exception as p:
                                print p

        return response
    except Exception as e:
        print e


#######################
#Written By - Nishank #
#######################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def orgs_without_attached_docs(request):
    try:
        org_records = OrganisationName.objects.filter(is_disable=False).order_by('id')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=orgs_without_attached_docs.csv'
        # with open('org_attached_docs.csv', 'w') as csvfile:

        if len(org_records):
            fieldnames = ['Organisation ID', 'Organisation Name', 'Organisation City', 'Organisation Locality',
                          'Organisation Stage','Organisation Current User'
                          ]
            writer = csv.DictWriter(response, fieldnames=fieldnames)

            writer.writeheader()

            for i in org_records:
                attached_docs = AssociateDoctorWithOrganization.objects.filter(organisation_id =  i.id)
                if list(attached_docs) == []:

                    try:
                        writer.writerow({'Organisation ID':i.id,'Organisation Name': i.name.encode('utf-8'),
                                         'Organisation City':i.city.name.encode('utf-8'),
                                         'Organisation Locality':i.locality.name.encode('utf-8'),
                                         'Organisation Stage': i.stage.stage_name.encode('utf-8'),
                                         'Organisation Current User':i.current_user.username.encode('utf-8')
                                         })
                    except Exception as p:
                        print p

        return response
    except Exception as e:
        print e
#######################
#Written By - Nishank #
#######################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def all_orgs_limited_field_export(request):
    try:
        org_records = OrganisationName.objects.all().order_by('id')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=all_organisations.csv'
        # with open('org_attached_docs.csv', 'w') as csvfile:

        if len(org_records):
            fieldnames = ['Organisation ID', 'Organisation Name', 'Organisation City', 'Organisation Locality',
                          'Organisation Address','Organisation Phone','Organisation Mobile',
                          'Organisation Stage','Organisation Current User','Publish','Is Disabled'
                          ]
            writer = csv.DictWriter(response, fieldnames=fieldnames)
            writer.writeheader()

            for i in org_records:
                try:
                    writer.writerow({'Organisation ID':i.id,'Organisation Name': i.name.encode('utf-8'),
                                     'Organisation City':i.city.name.encode('utf-8'),
                                     'Organisation Locality':i.locality.name.encode('utf-8'),
                                     'Organisation Address':i.street.encode('utf-8'),
                                     'Organisation Phone':i.phone.encode('utf-8'),
                                     'Organisation Mobile':i.mobile_no.encode('utf-8'),
                                     'Organisation Stage': i.stage.stage_name.encode('utf-8'),
                                     'Organisation Current User':i.current_user.username.encode('utf-8'),
                                     'Publish':i.publish,
                                     'Is Disabled': i.is_disable
                                     })

                except Exception as p:
                    print p

        return response
    except Exception as e:
        print e

#######################
#Written By - Nishank #
#######################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def all_labs_limited_field_export(request):
    try:
        lab_records = Labs.objects.all().order_by('id')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=all_labs.csv'
        # with open('org_attached_docs.csv', 'w') as csvfile:

        if len(lab_records):
            fieldnames = ['Lab ID', 'Lab Name', 'Lab City', 'Lab Locality',
                          'Lab Address','Lab Phone','Lab Mobile',
                          'Lab Stage','Lab Current User','Publish','Is Disabled'
                          ]
            writer = csv.DictWriter(response, fieldnames=fieldnames)
            writer.writeheader()

            for i in lab_records:
                try:
                    if i.telephone and i.telephone != '' and i.telephone != ' ':
                        tel= i.telephone.encode('utf-8')
                    else:
                        tel = ''
                    if i.lab_mobile and i.lab_mobile != '' and i.lab_mobile != ' ':
                        mob= i.lab_mobile.encode('utf-8')
                    else:
                        mob = ''
                    writer.writerow({'Lab ID':i.id,'Lab Name': i.name.encode('utf-8'),
                                     'Lab City':i.city.name.encode('utf-8'),
                                     'Lab Locality':i.locality.name.encode('utf-8'),
                                     'Lab Address':i.address.encode('utf-8'),
                                     'Lab Phone':tel,
                                     'Lab Mobile':mob,
                                     'Lab Stage': i.stage.stage_name.encode('utf-8'),
                                     'Lab Current User':i.current_user.username.encode('utf-8'),
                                     'Publish':i.publish,
                                     'Is Disabled': i.is_disable
                                     })

                except Exception as p:
                    print p

        return response
    except Exception as e:
        print e


#######################
#Written By - Nishank #
#######################
@login_required(login_url='/')
@require_GET
def attach_with_doctor_export(request):
    try:
        attach_list = AttachWithDoctor.objects.all().order_by('id')
        #attach_list = AttachWithDoctor.objects.filter(id=12305)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=attach_table_list.csv'

        if len(attach_list):
            count = 0
            fieldnames = ['Attach ID','Organisation ID', 'Organisation Name', 'Doctor ID', 'Doctor Name','DID','Extension' ]
            writer = csv.DictWriter(response, fieldnames=fieldnames)
            writer.writeheader()

            for aa in attach_list:
                count +=1
                #print "_"
                try:
                    writer.writerow({
                        'Attach ID':aa.id,
                        'Organisation ID':aa.organisation.id,
                        'Organisation Name':aa.organisation.name.encode('utf-8'),
                        'Doctor ID':aa.doctor.id,
                        'Doctor Name':aa.doctor.name.encode('utf-8'),
                        'DID':aa.did.encode('utf-8'),
                        'Extension':aa.extension.encode('utf-8')

                    })
                except Exception as e:
                    #print organisation_id, organisation_name,
                    #print  aa.id
                    pass

    except Exception as e:
        print e

    return response

#######################
#Written By - Nishank #
#######################
@login_required(login_url='/')
@require_GET
def doc_edit_missing_combination(request):
    """This function creates docx file where
       A particular combination of doc and org exiss in   AssociateDoctorWithOrganization
       but is missing in AttachWithDoctor
    """
    try:
        org_edit = AssociateDoctorWithOrganization.objects.all().order_by('id')


        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=doc_edit_missing_combination.csv'

        fieldnames = ['Attach Doc In Org ID','Organisation ID', 'Organisation Name','Organisation Current User', 'Doctor ID', 'Doctor Name','Department','Doctor Current User' ]
        writer = csv.DictWriter(response, fieldnames=fieldnames)
        writer.writeheader()

        for ooo in org_edit:
            ddd = []
            ddd = AttachWithDoctor.objects.filter(organisation_id = ooo.organisation_id,doctor_id=ooo.doctor_id)
            if len(list(ddd)) == 0:
                try:
                    writer.writerow({
                        'Attach Doc In Org ID':ooo.id,
                        'Organisation ID':ooo.organisation.id,
                        'Organisation Name':ooo.organisation.name.encode('utf-8'),
                        'Organisation Current User':ooo.organisation.current_user.username.encode('utf-8'),
                        'Doctor ID':ooo.doctor.id,
                        'Doctor Name':ooo.doctor.name.encode('utf-8'),
                        'Department':ooo.department.name.encode('utf-8'),
                        'Doctor Current User':ooo.doctor.current_user.username.encode('utf-8')

                    })
                except Exception as e:
                    #print organisation_id, organisation_name,
                    #print  aa.id
                    print "   IN <<< ", e
                    pass

    except Exception as e:
        print " OUT  >>> ",e

    return response



#######################
#Written By - Nishank #
#######################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def Jodhpur_attached_organisations(request):
    try:
        Attach_queryset = AttachWithDoctor.objects.filter(organisation__city_id=4).order_by('id')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Jodhpur_attached_organisations.csv'
        # with open('org_attached_docs.csv', 'w') as csvfile:

        if len(Attach_queryset):
            fieldnames = ['Doctor id','Doctor Name','Doctor Category','Doctor Mobile','Doctor Phone','Doctor Did','Doctor Extension','Doctor IsDisable','Doctor Current User',
                          'Attached Organisation id','Attached Organisation Name','Attached Organisation City','Attached Organisation Locality',
                          'Attached Organisation Did','Attached Organisation Extension','Attached Organisation Consultancy Fee',
                          'Attached Organisation Phone','Attached Organisation Mobile','Attached Organisation Current User','Attached Organisation IsDisable',
                          'Attached Organisation Publish']
            writer = csv.DictWriter(response, fieldnames=fieldnames)

            writer.writeheader()
            count = 0
            for i in Attach_queryset:
                count += 1
                doctor_id = i.doctor_id
                doctor_name = i.doctor.name
                doctor_category = i.doctor.category.name

                if i.doctor.mobile_no != None:
                    doctor_mobile = i.doctor.mobile_no
                else:
                    doctor_mobile = ''

                if i.doctor.phone != None:
                    doctor_phone = i.doctor.phone
                else:
                    doctor_phone = ''

                doctor_did = i.doctor.did
                doctor_extension = i.doctor.extension
                doctor_is_disable = i.doctor.is_disable
                doctor_current_user = i.doctor.current_user.username


                attached_org_id = i.organisation_id
                attached_org_name = i.organisation.name
                attached_org_city_name = i.organisation.city.name
                attached_org_locality_name = i.organisation.locality.name

                if i.did != None:
                    attached_org_did = i.did
                else:
                    attached_org_did = ''

                if i.extension != None:
                    attached_org_extension = i.extension
                else:
                    attached_org_extension = ''

                if i.consultancy_fee != None:
                    attached_org_con_fee = i.consultancy_fee
                else:
                    attached_org_con_fee = ''

                attached_org_phone = i.organisation.phone
                attached_org_mobile = i.organisation.mobile_no
                attached_current_user = i.organisation.current_user.username
                attached_is_disable = i.organisation.is_disable
                attached_org_publish = i.organisation.publish

                try:
                    writer.writerow({'Doctor id':doctor_id,'Doctor Name':doctor_name.encode('utf-8'),
                                     'Doctor Category':doctor_category.encode('utf-8'),
                                     'Doctor Mobile':doctor_mobile.encode('utf-8'),'Doctor Phone':doctor_phone.encode('utf-8'),
                                     'Doctor Did':doctor_did.encode('utf-8'),'Doctor Extension':doctor_extension.encode('utf-8'),
                                     'Doctor IsDisable':doctor_is_disable,'Doctor Current User':doctor_current_user.encode('utf-8'),
                                     'Attached Organisation id': attached_org_id,'Attached Organisation Name':attached_org_name.encode('utf-8'),
                                     'Attached Organisation City':attached_org_city_name.encode('utf-8'),
                                     'Attached Organisation Locality':attached_org_locality_name.encode('utf-8'),
                                     'Attached Organisation Did':attached_org_did.encode('utf-8'),
                                     'Attached Organisation Extension':attached_org_extension.encode('utf-8'),
                                     'Attached Organisation Consultancy Fee':attached_org_con_fee.encode('utf-8'),
                                     'Attached Organisation Phone':attached_org_phone.encode('utf-8'),
                                     'Attached Organisation Mobile':attached_org_mobile.encode('utf-8'),
                                     'Attached Organisation Current User':attached_current_user.encode('utf-8'),
                                     'Attached Organisation IsDisable':attached_is_disable,
                                     'Attached Organisation Publish':attached_org_publish,
                                     })
                except Exception as p:
                    print count,"  >>>  ",i.id
                    print p

        return response
    except Exception as e:
        print e


#######################
#Written By - Nishank #
#######################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def Pune_doctors(request):
    try:
        doc_records = Doctor.objects.filter(current_user_id=103).order_by('id')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Pune_doctors.csv'
        # with open('org_attached_docs.csv', 'w') as csvfile:

        if len(doc_records):
            fieldnames = ['Doctor id','Doctor Name','Doctor Category','Doctor Specilaity','Doctor Service offered','Zone','Zone Location','Current User',
                          'Doctor Registration','Attached Organisation id','Attached Organisation Name','Attached Organisation City','Attached Organisation Locality',
                          'Attached Organisation Address'
                          ]
            writer = csv.DictWriter(response, fieldnames=fieldnames)

            writer.writeheader()

            for i in doc_records:
                attached_orgs = AttachWithDoctor.objects.filter(doctor_id =  i.id)
                if list(attached_orgs) != []:
                    for j in attached_orgs:
                        org =  OrganisationName.objects.get(id= j.organisation_id)

                        doctor_id = i.id
                        doctor_name = i.name
                        if i.category != None and i.category != '' :
                            doctor_category = i.category.name
                        else:
                            doctor_category = ' '

                        if i.speciality != None and i.speciality != ' ' and i.speciality.strip() != '' :
                            doctor_speciality = i.speciality
                            strspe = ''
                            sp_l = doctor_speciality.split(',')
                            count = 0
                            for ss in sp_l:
                                count += 1
                                sp_obj = Speciality.objects.get(id =  int(ss))
                                if count == 1:
                                    strspe = strspe + sp_obj.name
                                else:
                                    strspe = strspe + ',' + sp_obj.name
                            doctor_speciality =  strspe
                        else:
                            doctor_speciality = ' '

                        if i.service_offered != None and i.service_offered != ' ' and i.service_offered != '' :
                            doctor_service_offered = i.service_offered
                            strspe = ''
                            sp_l = doctor_service_offered.split(',')
                            count = 0
                            for tt in sp_l:
                                count += 1
                                sp_obj = Service_Offred.objects.get(id=int(tt))
                                if count == 1:
                                    strspe = strspe + sp_obj.name
                                else:
                                    strspe = strspe + ',' + sp_obj.name
                            doctor_service_offered = strspe

                        else:
                            doctor_service_offered = ' '

                        doctor_zone = i.zone.name
                        doctor_zone_location = i.zone_location.name
                        doctor_current_user = i.current_user.username
                        doctor_registration = i.registration_data


                        attached_org_id = org.id
                        attached_org_name = org.name
                        attached_org_city_name = org.city.name
                        attached_org_locality_name = org.locality.name
                        attached_address = org.street


                        try:
                            writer.writerow({'Doctor id':doctor_id, 'Doctor Name':doctor_name.encode('utf-8'),
                                             'Doctor Category':doctor_category.encode('utf-8'), 'Doctor Specilaity':doctor_speciality.encode('utf-8'),
                                             'Doctor Service offered':doctor_service_offered.encode('utf-8'),
                                             'Zone':doctor_zone.encode('utf-8'), 'Zone Location':doctor_zone_location.encode('utf-8'),
                                             'Current User':doctor_current_user.encode('utf-8'),
                                             'Doctor Registration':doctor_registration.encode('utf-8'),
                                             'Attached Organisation id': attached_org_id,
                                             'Attached Organisation Name':attached_org_name.encode('utf-8'),
                                             'Attached Organisation City':attached_org_city_name.encode('utf-8'),
                                             'Attached Organisation Locality':attached_org_locality_name.encode('utf-8'),
                                             'Attached Organisation Address':attached_address.encode('utf-8'),
                                             })
                        except Exception as p:
                            print p,'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
                            pass
            return response
    except Exception as e:
        print e


#######################
#Written By - Nishank #
#######################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def Ahmedabad_doctors(request):
    try:
        doc_records = Doctor.objects.filter(current_user_id=114).order_by('id')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Ahmedabad_doctors.csv'
        # with open('org_attached_docs.csv', 'w') as csvfile:

        if len(doc_records):
            fieldnames = ['Doctor ID','Doctor Name','Doctor Category','Doctor Specilaity','Doctor Service offered','Zone','Zone Location','Current User',
                          'Doctor Registration','Attached Organisation ID','Attached Organisation Name','Attached Organisation City','Attached Organisation Locality',
                          'Attached Organisation Address'
                          ]
            writer = csv.DictWriter(response, fieldnames=fieldnames)

            writer.writeheader()

            for i in doc_records:
                attached_orgs = AttachWithDoctor.objects.filter(doctor_id =  i.id)
                if list(attached_orgs) != []:
                    for j in attached_orgs:
                        org =  OrganisationName.objects.get(id= j.organisation_id)

                        doctor_id = i.id
                        doctor_name = i.name
                        if i.category != None and i.category != '' :
                            doctor_category = i.category.name
                        else:
                            doctor_category = ' '

                        if i.speciality != None and i.speciality != ' ' and i.speciality.strip() != '' :
                            doctor_speciality = i.speciality
                            strspe = ''
                            sp_l = doctor_speciality.split(',')
                            count = 0
                            for ss in sp_l:
                                count += 1
                                sp_obj = Speciality.objects.get(id =  int(ss))
                                if count == 1:
                                    strspe = strspe + sp_obj.name
                                else:
                                    strspe = strspe + ',' + sp_obj.name
                            doctor_speciality =  strspe
                        else:
                            doctor_speciality = ' '

                        if i.service_offered != None and i.service_offered != ' ' and i.service_offered != '' :
                            doctor_service_offered = i.service_offered
                            strspe = ''
                            sp_l = doctor_service_offered.split(',')
                            count = 0
                            for tt in sp_l:
                                count += 1
                                sp_obj = Service_Offred.objects.get(id=int(tt))
                                if count == 1:
                                    strspe = strspe + sp_obj.name
                                else:
                                    strspe = strspe + ',' + sp_obj.name
                            doctor_service_offered = strspe

                        else:
                            doctor_service_offered = ' '

                        doctor_zone = i.zone.name
                        doctor_zone_location = i.zone_location.name
                        doctor_current_user = i.current_user.username
                        doctor_registration = i.registration_data


                        attached_org_id = org.id
                        attached_org_name = org.name
                        attached_org_city_name = org.city.name
                        attached_org_locality_name = org.locality.name
                        attached_address = org.street


                        try:
                            writer.writerow({'Doctor ID':doctor_id, 'Doctor Name':doctor_name.encode('utf-8'),
                                             'Doctor Category':doctor_category.encode('utf-8'), 'Doctor Specilaity':doctor_speciality.encode('utf-8'),
                                             'Doctor Service offered':doctor_service_offered.encode('utf-8'),
                                             'Zone':doctor_zone.encode('utf-8'), 'Zone Location':doctor_zone_location.encode('utf-8'),
                                             'Current User':doctor_current_user.encode('utf-8'),
                                             'Doctor Registration':doctor_registration.encode('utf-8'),
                                             'Attached Organisation ID': attached_org_id,
                                             'Attached Organisation Name':attached_org_name.encode('utf-8'),
                                             'Attached Organisation City':attached_org_city_name.encode('utf-8'),
                                             'Attached Organisation Locality':attached_org_locality_name.encode('utf-8'),
                                             'Attached Organisation Address':attached_address.encode('utf-8'),
                                             })
                        except Exception as p:
                            print p,'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
                            pass
            return response
    except Exception as e:
        print e

#!!!~!~!~!~!~!~!~!~!~!~!!~!~!~!~!~!

#######################
#Written By - Nishank #
#######################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def Mumbai_All_doctors(request):
    try:
        from hfu_cms.data_publisher import convert_time_str_array
        doc_records = Doctor.objects.filter(zone_id=1).order_by('id')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Mumbai_all_doctors.csv'
        # with open('org_attached_docs.csv', 'w') as csvfile:

        if len(doc_records):

            fieldnames = ['Doctor ID','Doctor Name','Doctor Qualification','Years of Experience','Doctor Category','Associated Organisation ID','Associated Organisation Name',
                          'Address of Organisation','Location of Organisation','Consultation Timings/days of doctor to attached organisation',
                          'Doctor Mobile','Doctor Telephone','Doctor Email','Organisation Mobile','Organisation Telephone','Organisation Email'
                          ]
            writer = csv.DictWriter(response, fieldnames=fieldnames)
            writer.writeheader()


            for i in doc_records:
                doctor_id = i.id
                doctor_name = i.name
                doctor_qualification = i.qualification_data
                doctor_experience = i.doctor_experience_year
                if i.category != None and i.category != '':
                    doctor_category = i.category.name
                else:
                    doctor_category = ' '
                doctor_mobile = i.mobile_no
                doctor_telephone = i.phone
                doctor_email = i.email

                attached_orgs = AttachWithDoctor.objects.filter(doctor_id =  i.id)
                if list(attached_orgs) != []:
                    for j in attached_orgs:
                        org =  OrganisationName.objects.get(id= j.organisation_id)

                        org_id = org.id
                        org_name = org.name
                        org_locality_name = org.locality.name
                        org_address = org.street
                        org_mobile = org.mobile_no
                        org_telephone = org.phone
                        org_email = org.email


                        try:
                            Schedule_obj = Schedule.objects.get(doctor_id=i.id, organisation_id=org.id)
                        except:
                            Schedule_obj = None

                        if Schedule_obj:
                            if Schedule_obj.by_appointment == False:
                                try:
                                    schedule_data = Schedule_obj.schedule_data
                                    timing_str = convert_time_str_array(schedule_data)
                                    timing_str = json.dumps(timing_str)
                                except:
                                    timing_str = ' '



                        try:
                            writer.writerow({'Doctor ID':doctor_id, 'Doctor Name':doctor_name.encode('utf-8'),
                                             'Doctor Qualification':doctor_qualification.encode('utf-8'),
                                             'Years of Experience':doctor_experience.encode('utf-8'),
                                             'Doctor Category':doctor_category.encode('utf-8'),
                                             'Associated Organisation ID':org_id,
                                             'Associated Organisation Name':org_name.encode('utf-8'),
                                             'Address of Organisation':org_address.encode('utf-8'),
                                             'Location of Organisation':org_locality_name.encode('utf-8'),
                                             'Consultation Timings/days of doctor to attached organisation':timing_str.encode('utf-8'),
                                             'Doctor Mobile':doctor_mobile.encode('utf-8'), 'Doctor Telephone':org_telephone.encode('utf-8'),
                                             'Doctor Email':org_email.encode('utf-8'), 'Organisation Mobile':org_mobile.encode('utf-8'),
                                             'Organisation Telephone':org_telephone.encode('utf-8'), 'Organisation Email':org_email.encode('utf-8')

                            })
                        except Exception as p:
                            print p,'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
                            pass
                else:
                    try:
                        writer.writerow({'Doctor ID': doctor_id, 'Doctor Name': doctor_name.encode('utf-8'),
                                         'Doctor Qualification': doctor_qualification.encode('utf-8'),
                                         'Years of Experience': doctor_experience.encode('utf-8'),
                                         'Doctor Category': doctor_category.encode('utf-8'),
                                         'Associated Organisation ID': 'N/A'.encode('utf-8'),
                                         'Associated Organisation Name': 'N/A'.encode('utf-8'),
                                         'Address of Organisation': 'N/A'.encode('utf-8'),
                                         'Location of Organisation': 'N/A'.encode('utf-8'),
                                         'Consultation Timings/days of doctor to attached organisation': 'N/A'.encode('utf-8'),
                                         'Doctor Mobile': doctor_mobile.encode('utf-8'),
                                         'Doctor Telephone': org_telephone.encode('utf-8'),
                                         'Doctor Email': org_email.encode('utf-8'),
                                         'Organisation Mobile': 'N/A'.encode('utf-8'),
                                         'Organisation Telephone': 'N/A'.encode('utf-8'),
                                         'Organisation Email': 'N/A'.encode('utf-8')

                                         })
                    except Exception as p:
                        print p, '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
                        pass

            return response
    except Exception as e:
        print e


####### NEW C, SO . SPl  exports
#######################
#Written By - Nishank #
#######################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def new_speciality_export(request):
    try:
        new_spl_records = Doctor_Speciality_New.objects.all().order_by('id')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=new_speciality_master.csv'
        # with open('org_attached_docs.csv', 'w') as csvfile:

        if len(new_spl_records):
            fieldnames = ['Speciality ID', 'Speciality Name', ]
            writer = csv.DictWriter(response, fieldnames=fieldnames)
            writer.writeheader()
            for i in new_spl_records:

                try:
                    writer.writerow({'Speciality ID':i.id,
                                     'Speciality Name':i.name.encode('utf-8'),
                                     })
                except Exception as p:
                    print p

        return response
    except Exception as e:
        print e

#######################
#Written By - Nishank #
#######################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def new_serviceoffered_export(request):
    try:
        import sys
        reload(sys)
        sys.setdefaultencoding('utf8')
        new_so_records = Doctor_ServiceOffered_New.objects.all().order_by('id')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=new_serviceoffered_master_NEW.csv'
        # with open('org_attached_docs.csv', 'w') as csvfile:

        if len(new_so_records):
            fieldnames = ['Service Offered ID', 'Service Offered Name', ]
            writer = csv.DictWriter(response, fieldnames=fieldnames)
            writer.writeheader()
            for i in new_so_records:

                try:
                    writer.writerow({'Service Offered ID':i.id,
                                     'Service Offered Name':i.name.encode('utf-8'),
                                     })
                except Exception as p:
                    print p

        return response
    except Exception as e:
        print e

#######**########
#######################
#Written By - Nishank #
#######################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def cats_mappedto_newunique_serviceoffered_mastervalues(request):
    try:
        import sys
        reload(sys)
        sys.setdefaultencoding('utf8')
        new_so_records = Doctor_ServiceOffered_New.objects.all().order_by('id')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=cats_mappedto_newunique_serviceoffered_mastervalues.csv'
        # with open('org_attached_docs.csv', 'w') as csvfile:

        if len(new_so_records):
            fieldnames = ['Service Offered ID','Service Offered name', 'Categories', ]
            writer = csv.DictWriter(response, fieldnames=fieldnames)
            writer.writeheader()

            for i in new_so_records:
                try:
                    writer.writerow({'Service Offered ID':i.id,
                                     'Service Offered name': i.name.encode('utf-8'),
                                     'Categories':i.tempcat.encode('utf-8'),
                                     })
                except Exception as p:
                    print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
                    print i.id,i.name
                    print p

        return response
    except Exception as e:
        print "%%%%%%%%%%%%%%%%%%%%%%%%%"
        print e
#######**########


#######################
#Written By - Nishank #
#######################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def new_serviceoffered_export_7872(request):
    try:
        import sys
        reload(sys)
        sys.setdefaultencoding('utf8')
        new_so_records = DelServiceOfferedNew_7872.objects.all().order_by('id')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=SO_Unique_Extract_1TO7872.csv'
        # with open('org_attached_docs.csv', 'w') as csvfile:

        if len(new_so_records):
            fieldnames = ['Servoce Offered ID', 'Servoce Offered Name', ]
            writer = csv.DictWriter(response, fieldnames=fieldnames)
            writer.writeheader()
            for i in new_so_records:

                try:
                    writer.writerow({'Servoce Offered ID':i.id,
                                     'Servoce Offered Name':i.name.encode('utf-8'),
                                     })
                except Exception as p:
                    print p

        return response
    except Exception as e:
        print e



# All service Offered mapped in all Doctors
#######################
#Written By - Nishank #
#######################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def all_so_all_docs_15June(request):
    try:
        from django.db.models import Q
        Docs = Doctor.objects.filter(Q(zone=1)|Q(zone=4)).order_by('id')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=all_so_all_docs_15June.csv'
        # with open('org_attached_docs.csv', 'w') as csvfile:

        if len(Docs):
            fieldnames = ['Doctor ID','Doctor Name','Doctor Zone', 'Zone Location','Doc User','Doc Stage', 'SO ID',
                          'SO Name', 'SO Cat ID', 'SO Cat Name' ]
            writer = csv.DictWriter(response, fieldnames=fieldnames)
            writer.writeheader()
            for d in Docs:
                name = d.name
                zone = d.zone.name
                zoneloc = d.zone_location.name
                docuse = d.current_user.username
                docstage = d.stage.stage_name
                if d.service_offered != None and d.service_offered != '' and d.service_offered != ' ':
                    so_list = d.service_offered.split(',')
                    for so in so_list:
                        try:
                            serv_of = Service_Offred.objects.get(id=so)
                        except:
                            serv_of = None
                        if serv_of != None:
                            soid = serv_of.id
                            soname = serv_of.name
                            cocat = serv_of.category.name
                            cocatid = serv_of.category.id
                            try:
                                writer.writerow({'Doctor ID':d.id,'Doctor Name':name.encode('utf-8'),'Doctor Zone':zone.encode('utf-8'),
                                                 'Zone Location':zoneloc.encode('utf-8'),'Doc User':docuse.encode('utf-8'),
                                                 'Doc Stage':docstage.encode('utf-8'), 'SO ID':soid,
                                                 'SO Name':soname.encode('utf-8'), 'SO Cat ID':cocatid, 'SO Cat Name':cocat.encode('utf-8'),

                                                 })
                                print "+++++++++++++++++++++"
                            except Exception as p:
                                print p
                        else:
                            pass
                else:
                    try:
                        writer.writerow({'Doctor ID': d.id, 'Doctor Name': name.encode('utf-8'),
                                         'Doctor Zone': zone.encode('utf-8'),
                                         'Zone Location': zoneloc.encode('utf-8'), 'Doc User': docuse.encode('utf-8'),
                                         'Doc Stage': docstage.encode('utf-8'), 'SO ID': "".encode('utf-8'),
                                         'SO Name': "".encode('utf-8'), 'SO Cat ID': "".encode('utf-8'),
                                         'SO Cat Name': "".encode('utf-8'),

                                         })
                        print "------------------------------------------"
                    except Exception as p:
                        print p

        return response
    except Exception as e:
        print e


#######################
#Written By - Nishank #
#######################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def all_Mumbai_docs_with_email(request):
    try:
        from django.db.models import Q
        Docs = Doctor.objects.filter(Q(zone=1) & ~Q(email = None) & ~Q(email = '') & ~Q(email = ' ' )).order_by('id')

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=all_Mumbai_docs_with_email.csv'
        # with open('org_attached_docs.csv', 'w') as csvfile:

        if len(Docs):
            fieldnames = ['ID','Name','Category', 'Email', 'Mobile','Zone', 'Zone Location' ]
            writer = csv.DictWriter(response, fieldnames=fieldnames)
            writer.writeheader()
            for d in Docs:
                name = d.name
                zone = d.zone.name
                try:
                    zoneloc = d.zone_location.name
                except:
                    zoneloc = 'Not Available'
                try:
                    cat = d.category.name
                except:
                    cat = 'Not Available'
                mail = d.email
                iid = d.id
                if d.mobile_no and d.mobile_no != ' ':
                    mmob = d.mobile_no
                else:
                    mmob = 'Not Available'
                try:
                    writer.writerow({'ID':iid,'Name':name.encode('utf-8'),
                                     'Category': cat.encode('utf-8'),
                                     'Email': mail.encode('utf-8'),
                                     'Mobile': mmob.encode('utf-8'),
                                     'Zone':zone.encode('utf-8'),
                                     'Zone Location':zoneloc.encode('utf-8'),
                                     })
                    print "+++++++++++++++++++++"
                except Exception as p:
                    print d.id," >>>> " ,p


        return response
    except Exception as e:
        print e


#######################
#Written By - Nishank #
#######################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def Mumbai_docs__zonelocations_3(request):
    try:
        from django.db.models import Q
        from hfu_cms.data_publisher import convert_time_str_array
        Docs_bhandup = Doctor.objects.filter(Q(zone_location=65)|Q(zone_location=66)|Q(zone_location=95)).order_by('id')
        Docs_mulundp = Doctor.objects.filter(Q(zone_location=110) | Q(zone_location=15) | Q(zone_location=2) ).order_by('id')
        Docs_thane = Doctor.objects.filter(Q(zone_location=169)|Q(zone_location=185)).order_by('id')

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=all_Mumbai_docs_with_email.csv'
        # with open('org_attached_docs.csv', 'w') as csvfile:


        fieldnames = ['Doctor ID', 'Doctor Zone','Zone Location','Doctor Name',
                                         'Doctor Category','Doctor Mail','Doctor Mobile',
                                         'Doctor Telepohone',
                                         'Doctor Qualification','Years of Experience',
                                          'Dcotor DOB',
                                         'Associated Organisation ID',
                                         'Associated Organisation Name', 'Address of Organisation',
                                         'Location of Organisation', 'Consultation Timings/days of doctor to attached organisation',
                                         'Consultation Fee','Organisation Mobile','Organisation Telephone',
                                         'Organisation Email' ]
        writer = csv.DictWriter(response, fieldnames=fieldnames)
        writer.writeheader()

        if len(Docs_bhandup):
            for d in Docs_bhandup:
                doctor_qualification = d.qualification_data
                doctor_experience = d.doctor_experience_year
                dob = str(d.dob)
                doc_tel = d.phone

                if doctor_qualification == None:
                    doctor_qualification = 'Not Available'
                if doctor_experience == None:
                    doctor_experience = 'Not Available'
                if dob == None or dob =='None':
                    dob = 'Not Available'
                if doc_tel == None:
                    doc_tel = 'Not Available'
                doctor_name = d.name
                zone = d.zone.name
                try:
                    zoneloc = d.zone_location.name
                except:
                    zoneloc = 'Not Available'
                try:
                    doctor_category = d.category.name
                except:
                    doctor_category = 'Not Available'
                mail = d.email
                if mail == None:
                    mail = 'Not Available'
                doctor_id = d.id
                if d.mobile_no and d.mobile_no != ' ':
                    mmob = d.mobile_no
                else:
                    mmob = 'Not Available'
                attached_orgs = AttachWithDoctor.objects.filter(doctor_id=d.id)
                if list(attached_orgs) != []:
                    for j in attached_orgs:
                        org = OrganisationName.objects.get(id=j.organisation_id)
                        org_id = org.id
                        org_name = org.name
                        org_locality_name = org.locality.name
                        org_address = org.street
                        org_mobile = org.mobile_no
                        org_telephone = org.phone
                        org_email = org.email

                        try:
                            Schedule_obj = Schedule.objects.get(doctor_id=d.id, organisation_id=org.id)
                        except:
                            Schedule_obj = None

                        if Schedule_obj:
                            if Schedule_obj.by_appointment == False:
                                try:
                                    schedule_data = Schedule_obj.schedule_data
                                    timing_str = convert_time_str_array(schedule_data)
                                    timing_str = json.dumps(timing_str)
                                except:
                                    timing_str = 'Not Available'

                                try:
                                    cfee = j.consultancy_fee
                                except:
                                    cfee = 'Not Available'
                        else:
                            timing_str = 'Not Available'
                            cfee ='Not Available'
                        if cfee == None:
                            cfee = 'Not Available'

                        try:
                            writer.writerow({'Doctor ID': doctor_id,  'Doctor Zone':zone.encode('utf-8'),
                                             'Zone Location':zoneloc.encode('utf-8'),
                                             'Doctor Name': doctor_name.encode('utf-8'),
                                             'Doctor Category': doctor_category.encode('utf-8'),
                                             'Doctor Mail':mail.encode('utf-8'), 'Doctor Mobile':mmob.encode('utf-8'),
                                             'Doctor Telepohone':doc_tel.encode('utf-8'),
                                             'Doctor Qualification':doctor_qualification.encode('utf-8'),
                                             'Years of Experience':doctor_experience.encode('utf-8'),
                                             'Dcotor DOB':dob.encode('utf-8'),
                                             'Associated Organisation ID': org_id,
                                             'Associated Organisation Name': org_name.encode('utf-8'),
                                             'Address of Organisation': org_address.encode('utf-8'),
                                             'Location of Organisation': org_locality_name.encode('utf-8'),
                                             'Consultation Timings/days of doctor to attached organisation': timing_str.encode(
                                                 'utf-8'),
                                             'Consultation Fee':cfee.encode('utf-8'),
                                             'Organisation Mobile': org_mobile.encode('utf-8'),
                                             'Organisation Telephone': org_telephone.encode('utf-8'),
                                             'Organisation Email': org_email.encode('utf-8')

                                             })
                        except Exception as p:
                            print p, '~~~~~~~',d.id,d.name,'~~~~~~~',org.id,org.name
                            pass

        if len(Docs_mulundp):
            for d in Docs_mulundp:
                if d.id == 8:
                    print 'asasas'
                doctor_qualification = d.qualification_data
                doctor_experience = d.doctor_experience_year
                dob = str(d.dob)
                doc_tel = d.phone

                if doctor_qualification == None:
                    doctor_qualification = 'Not Available'
                if doctor_experience == None:
                    doctor_experience = 'Not Available'
                if dob == None or dob =='None':
                    dob = 'Not Available'
                if doc_tel == None:
                    doc_tel = 'Not Available'
                doctor_name = d.name
                zone = d.zone.name
                try:
                    zoneloc = d.zone_location.name
                except:
                    zoneloc = 'Not Available'
                try:
                    doctor_category = d.category.name
                except:
                    doctor_category = 'Not Available'
                mail = d.email
                if mail == None:
                    mail = 'Not Available'
                doctor_id = d.id
                if d.mobile_no and d.mobile_no != ' ':
                    mmob = d.mobile_no
                else:
                    mmob = 'Not Available'
                attached_orgs = AttachWithDoctor.objects.filter(doctor_id=d.id)
                if list(attached_orgs) != []:
                    for j in attached_orgs:
                        org = OrganisationName.objects.get(id=j.organisation_id)
                        org_id = org.id
                        org_name = org.name
                        org_locality_name = org.locality.name
                        org_address = org.street
                        org_mobile = org.mobile_no
                        org_telephone = org.phone
                        org_email = org.email

                        try:
                            Schedule_obj = Schedule.objects.get(doctor_id=d.id, organisation_id=org.id)
                        except:
                            Schedule_obj = None

                        if Schedule_obj:
                            if Schedule_obj.by_appointment == False:
                                try:
                                    schedule_data = Schedule_obj.schedule_data
                                    timing_str = convert_time_str_array(schedule_data)
                                    timing_str = json.dumps(timing_str)
                                except:
                                    timing_str = 'Not Available'
                                try:
                                    cfee = j.consultancy_fee
                                except:
                                    cfee = 'Not Available'
                        else:
                            timing_str = 'Not Available'
                            cfee ='Not Available'
                        if cfee == None:
                            cfee = 'Not Available'

                        try:
                            writer.writerow({'Doctor ID': doctor_id,  'Doctor Zone':zone.encode('utf-8'),
                                             'Zone Location':zoneloc.encode('utf-8'),
                                             'Doctor Name': doctor_name.encode('utf-8'),
                                             'Doctor Category': doctor_category.encode('utf-8'),
                                             'Doctor Mail':mail.encode('utf-8'), 'Doctor Mobile':mmob.encode('utf-8'),
                                             'Doctor Telepohone':doc_tel.encode('utf-8'),
                                             'Doctor Qualification':doctor_qualification.encode('utf-8'),
                                             'Years of Experience':doctor_experience.encode('utf-8'),
                                             'Dcotor DOB':dob.encode('utf-8'),
                                             'Associated Organisation ID': org_id,
                                             'Associated Organisation Name': org_name.encode('utf-8'),
                                             'Address of Organisation': org_address.encode('utf-8'),
                                             'Location of Organisation': org_locality_name.encode('utf-8'),
                                             'Consultation Timings/days of doctor to attached organisation': timing_str.encode(
                                                 'utf-8'),
                                             'Consultation Fee':cfee.encode('utf-8'),
                                             'Organisation Mobile': org_mobile.encode('utf-8'),
                                             'Organisation Telephone': org_telephone.encode('utf-8'),
                                             'Organisation Email': org_email.encode('utf-8')

                                             })
                        except Exception as p:
                            print p, '~~~~~~~',d.id,d.name,'~~~~~~~',org.id,org.name
                            pass



        if len(Docs_thane):
            for d in Docs_thane:
                doctor_qualification = d.qualification_data
                doctor_experience = d.doctor_experience_year
                dob = str(d.dob)
                doc_tel = d.phone

                if doctor_qualification == None:
                    doctor_qualification = 'Not Available'
                if doctor_experience == None:
                    doctor_experience = 'Not Available'
                if dob == None or dob =='None':
                    dob = 'Not Available'
                if doc_tel == None:
                    doc_tel = 'Not Available'
                doctor_name = d.name
                zone = d.zone.name
                try:
                    zoneloc = d.zone_location.name
                except:
                    zoneloc = 'Not Available'
                try:
                    doctor_category = d.category.name
                except:
                    doctor_category = 'Not Available'
                mail = d.email
                if mail == None:
                    mail = 'Not Available'
                doctor_id = d.id
                if d.mobile_no and d.mobile_no != ' ':
                    mmob = d.mobile_no
                else:
                    mmob = 'Not Available'
                attached_orgs = AttachWithDoctor.objects.filter(doctor_id=d.id)
                if list(attached_orgs) != []:
                    for j in attached_orgs:
                        org = OrganisationName.objects.get(id=j.organisation_id)
                        org_id = org.id
                        org_name = org.name
                        org_locality_name = org.locality.name
                        org_address = org.street
                        org_mobile = org.mobile_no
                        org_telephone = org.phone
                        org_email = org.email

                        try:
                            Schedule_obj = Schedule.objects.get(doctor_id=d.id, organisation_id=org.id)
                        except:
                            Schedule_obj = None

                        if Schedule_obj:
                            if Schedule_obj.by_appointment == False:
                                try:
                                    schedule_data = Schedule_obj.schedule_data
                                    timing_str = convert_time_str_array(schedule_data)
                                    timing_str = json.dumps(timing_str)
                                except:
                                    timing_str = 'Not Available'
                                try:
                                    cfee = j.consultancy_fee
                                except:
                                    cfee = 'Not Available'
                        else:
                            timing_str = 'Not Available'
                            cfee ='Not Available'
                        if cfee == None:
                            cfee = 'Not Available'

                        try:
                            writer.writerow({'Doctor ID': doctor_id,  'Doctor Zone':zone.encode('utf-8'),
                                             'Zone Location':zoneloc.encode('utf-8'),
                                             'Doctor Name': doctor_name.encode('utf-8'),
                                             'Doctor Category': doctor_category.encode('utf-8'),
                                             'Doctor Mail':mail.encode('utf-8'), 'Doctor Mobile':mmob.encode('utf-8'),
                                             'Doctor Telepohone':doc_tel.encode('utf-8'),
                                             'Doctor Qualification':doctor_qualification.encode('utf-8'),
                                             'Years of Experience':doctor_experience.encode('utf-8'),
                                             'Dcotor DOB':dob.encode('utf-8'),
                                             'Associated Organisation ID': org_id,
                                             'Associated Organisation Name': org_name.encode('utf-8'),
                                             'Address of Organisation': org_address.encode('utf-8'),
                                             'Location of Organisation': org_locality_name.encode('utf-8'),
                                             'Consultation Timings/days of doctor to attached organisation': timing_str.encode(
                                                 'utf-8'),
                                             'Consultation Fee':cfee.encode('utf-8'),
                                             'Organisation Mobile': org_mobile.encode('utf-8'),
                                             'Organisation Telephone': org_telephone.encode('utf-8'),
                                             'Organisation Email': org_email.encode('utf-8')

                                             })
                        except Exception as p:
                            print p, '~~~~~~~',d.id,d.name,'~~~~~~~',org.id,org.name
                            pass

        return response
    except Exception as e:
        print e



#######################
#Written By - Nishank #
#######################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def all_orgs_lat_long(request):
    try:
        org_records = OrganisationName.objects.filter(id__lte=2000).order_by('id')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=all_organisations_lat_long.csv'
        # with open('org_attached_docs.csv', 'w') as csvfile:

        if len(org_records):
            fieldnames = ['Organisation ID', 'Organisation Name', 'Organisation City', 'Organisation Locality',
                          'Organisation Address','Organisation Address By Google','Organisation Current Lat','Organisation Lat By Google',
                          'Organisation Current Long', 'Organisation Long By Google',
                          ]
            writer = csv.DictWriter(response, fieldnames=fieldnames)
            writer.writeheader()

            for i in org_records:
                try:

                    try:
                        mygoogleapibase = 'https://maps.googleapis.com/maps/api/geocode/json?address='
                        mygoogleapikey = '&key=AIzaSyBSgwtACK4WPjYKy837g7fgaeYf6JDjxkM'
                        AddressForApi = i.name.strip()+' '+i.street.strip()+' '+i.city.name.strip()
                        if AddressForApi and AddressForApi != '':
                            AddressForApi = AddressForApi.split(' ')
                            AddressForApi = [mm.strip() for mm in AddressForApi]
                            AddressForApi = "+".join(AddressForApi)
                        mygoogleapiurl = mygoogleapibase + AddressForApi + mygoogleapikey
                        import requests
                        r = requests.post(mygoogleapiurl)
                        import json
                        rrcc = json.loads(r.content)
                        if rrcc['status'] == 'ZERO_RESULTS':
                            gformatted_address = 'ZERO_RESULTS'
                            glatitude = 'ZERO_RESULTS'
                            glongitude = 'ZERO_RESULTS'

                        if rrcc['status'] == 'OK':
                            resgoogle = rrcc['results'][0]
                            gformatted_address = resgoogle['formatted_address']
                            glatitude = resgoogle['geometry']['location']['lat']
                            glongitude = resgoogle['geometry']['location']['lng']
                    except Exception as e:
                        gformatted_address = 'Error'
                        glatitude = 'Error'
                        glongitude = 'Error'
                    writer.writerow({'Organisation ID':i.id,'Organisation Name': i.name.encode('utf-8'),
                                     'Organisation City':i.city.name.encode('utf-8'),
                                     'Organisation Locality':i.locality.name.encode('utf-8'),
                                     'Organisation Address':i.street.encode('utf-8'),
                                     'Organisation Address By Google':gformatted_address.encode('utf-8'),
                                     'Organisation Current Lat':i.latitude.encode('utf-8'),
                                     'Organisation Lat By Google':str(glatitude).encode('utf-8'),
                                     'Organisation Current Long':i.longitude.encode('utf-8'),
                                     'Organisation Long By Google':str(glongitude).encode('utf-8'),
                                     })
                    print "---------------- org id : ", i.id, '   ', i.name

                except Exception as p:
                    print p

        return response
    except Exception as e:
        print e


#######################
#Written By - Nishank #
#######################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def all_orgs_lat_long(request):
    try:
        org_records = OrganisationName.objects.filter(id__lte=2000).order_by('id')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=all_organisations_lat_long.csv'
        # with open('org_attached_docs.csv', 'w') as csvfile:

        if len(org_records):
            fieldnames = ['Organisation ID', 'Organisation Name', 'Organisation City', 'Organisation Locality',
                          'Organisation Address''Organisation Current Lat',
                          'Organisation Current Long',
                          ]
            writer = csv.DictWriter(response, fieldnames=fieldnames)
            writer.writeheader()

            for i in org_records:
                try:

                    try:
                        mygoogleapibase = 'https://maps.googleapis.com/maps/api/geocode/json?address='
                        mygoogleapikey = '&key=AIzaSyBSgwtACK4WPjYKy837g7fgaeYf6JDjxkM'
                        AddressForApi = i.name.strip()+' '+i.street.strip()+' '+i.city.name.strip()
                        if AddressForApi and AddressForApi != '':
                            AddressForApi = AddressForApi.split(' ')
                            AddressForApi = [mm.strip() for mm in AddressForApi]
                            AddressForApi = "+".join(AddressForApi)
                        mygoogleapiurl = mygoogleapibase + AddressForApi + mygoogleapikey
                        import requests
                        r = requests.post(mygoogleapiurl)
                        import json
                        rrcc = json.loads(r.content)
                        if rrcc['status'] == 'ZERO_RESULTS':
                            gformatted_address = 'ZERO_RESULTS'
                            glatitude = 'ZERO_RESULTS'
                            glongitude = 'ZERO_RESULTS'

                        if rrcc['status'] == 'OK':
                            resgoogle = rrcc['results'][0]
                            gformatted_address = resgoogle['formatted_address']
                            glatitude = resgoogle['geometry']['location']['lat']
                            glongitude = resgoogle['geometry']['location']['lng']
                    except Exception as e:
                        gformatted_address = 'Error'
                        glatitude = 'Error'
                        glongitude = 'Error'
                    writer.writerow({'Organisation ID':i.id,'Organisation Name': i.name.encode('utf-8'),
                                     'Organisation City':i.city.name.encode('utf-8'),
                                     'Organisation Locality':i.locality.name.encode('utf-8'),
                                     'Organisation Address':i.street.encode('utf-8'),
                                     'Organisation Address By Google':gformatted_address.encode('utf-8'),
                                     'Organisation Current Lat':i.latitude.encode('utf-8'),
                                     'Organisation Lat By Google':str(glatitude).encode('utf-8'),
                                     'Organisation Current Long':i.longitude.encode('utf-8'),
                                     'Organisation Long By Google':str(glongitude).encode('utf-8'),
                                     })
                    print "---------------- org id : ", i.id, '   ', i.name

                except Exception as p:
                    print p

        return response
    except Exception as e:
        print e



#######################
#Written By - Nishank #
#######################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def orgs_lat_long_pre_filled(request):
    try:
        from django.db.models import Q
        org_records = OrganisationName.objects.filter((~Q(latitude=None))&(~Q(latitude='')) &(~Q(longitude=None))&(~Q(longitude=''))).order_by('id')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=organisations_having_lat_long_prefilled.csv'
        # with open('org_attached_docs.csv', 'w') as csvfile:

        if len(org_records):
            fieldnames = ['Organisation ID','Organisation Name', 'Latitude','Longitude','Organisation City', 'Organisation Locality',
                          'Organisation Current User','Organisation Stage',
                          ]
            writer = csv.DictWriter(response, fieldnames=fieldnames)
            writer.writeheader()

            for i in org_records:
                if i.longitude == None or i.longitude == '':
                    long = ''
                else:
                    long = i.longitude
                if i.latitude == None or i.latitude == '':
                    lat = ''
                else:
                    lat = i.latitude
                try:
                    cityy = i.city.name
                except:
                    cityy = 'Not Provided'
                try:
                    localityy = i.locality.name
                except:
                    localityy= 'Not Provided'
                try:
                    cuser = i.current_user.username
                except:
                    cuser = 'None'
                try:
                    stagee = i.stage.stage_name
                except:
                    stagee = 'None'
                try:
                    writer.writerow({'Organisation ID':i.id,'Organisation Name': i.name.encode('utf-8'),
                                     'Latitude': lat.encode('utf-8'),
                                     'Longitude':long.encode('utf-8'),
                                     'Organisation City':cityy.encode('utf-8'),
                                     'Organisation Locality':localityy.encode('utf-8'),
                                     'Organisation Current User':cuser.encode('utf-8'),
                                     'Organisation Stage':stagee.encode('utf-8')
                                     })
                    print "---------------- org id : ", i.id, '   ', i.name

                except Exception as p:
                    print p

        return response
    except Exception as e:
        print e

#######################
# Written By - Nishank #
#######################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def orgs_with_lat_AND_OR_long_OR_BOTH_missing(request):
    try:
        from django.db.models import Q
        org_records = OrganisationName.objects.filter(Q(latitude=None)|Q(latitude='')|Q(longitude=None)|Q(longitude='')).order_by('id')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=orgs_with_lat_AND_OR_long_OR_BOTH_missing.csv'
        # with open('org_attached_docs.csv', 'w') as csvfile:

        if len(org_records):
            fieldnames = ['Organisation ID', 'Organisation Name', 'Latitude', 'Longitude', 'Organisation City',
                          'Organisation Locality',
                          'Organisation Current User', 'Organisation Stage',
                          ]
            writer = csv.DictWriter(response, fieldnames=fieldnames)
            writer.writeheader()


            for i in org_records:
                if i.longitude == None or i.longitude == '':
                    long = ''
                else:
                    long = i.longitude
                if i.latitude == None or i.latitude == '':
                    lat = ''
                else:
                    lat = i.latitude
                try:
                    cityy = i.city.name
                except:
                    cityy = 'Not Provided'
                try:
                    localityy = i.locality.name
                except:
                    localityy= 'Not Provided'
                try:
                    cuser = i.current_user.username
                except:
                    cuser = 'None'
                try:
                    stagee = i.stage.stage_name
                except:
                    stagee = 'None'
                try:
                    writer.writerow({'Organisation ID': i.id, 'Organisation Name': i.name.encode('utf-8'),
                                     'Latitude': lat.encode('utf-8'),
                                     'Longitude': long.encode('utf-8'),
                                     'Organisation City': cityy.encode('utf-8'),
                                     'Organisation Locality': localityy.encode('utf-8'),
                                     'Organisation Current User': cuser.encode('utf-8'),
                                     'Organisation Stage': stagee.encode('utf-8')
                                     })
                    print "---------------- org id : ", i.id, '   ', i.name

                except Exception as p:
                    print p

        return response
    except Exception as e:
        print e

# from hfu_cms.models import OrganisationName
# from django.db.models import Q
# a = OrganisationName.objects.all().count()
# empty = OrganisationName.objects.filter(Q(latitude=None)|Q(latitude='')|Q(longitude=None)|Q(longitude=''))
# full = OrganisationName.objects.filter((~Q(latitude=None))&(~Q(latitude='')) &(~Q(longitude=None))&(~Q(longitude='')))


########################
# Written By - Nishank #
########################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
def Doctor_rank_extract(request):
    try:
        import elasticsearch_client
        cat_id_list = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 14 , 15 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 33 , 34 , 35 , 36 , 37 , 39 , 40 , 41 , 42 , 45 ]
        city_list = [1,2,3,4,5]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Doctor_Rankings.csv'
        # with open('org_attached_docs.csv', 'w') as csvfile:
        if True:
            fieldnames = ['Doctor ID', 'Doctor Name', 'Is Live Doctor/Doctor', 'Stage', 'User',
                          'Category', 'City', 'Location','CC Sponsored Rank','CC Subscribed Rank', 'CC Trial Rank',
                          'CLC Sponsored Rank', 'CLC Subscribed Rank', 'CLC Trial Rank'
                         ]
            writer = csv.DictWriter(response, fieldnames=fieldnames)
            writer.writeheader()

            for cityy in city_list:
                for catt in cat_id_list:
                    livedocs_all_id_list = Live_Doctor.objects.filter(category=catt).values_list('id', flat=True)
                    docs_all_id_list = Doctor.objects.filter(category=catt).values_list('id', flat=True)

                    key = str(cityy) + '-' + str(catt)
                    orgs_id_list = OrganisationName.objects.filter(country_id=1, state_id=1,city_id=cityy).values_list('id', flat=True)


                    livedocs_final_id_list = Live_Doctor_Commonworkschedule.objects.filter(doctor_id__in=livedocs_all_id_list,clinic_id__in=orgs_id_list).values_list('doctor_id',flat=True)
                    livedocs_final_id_list = list(set(livedocs_final_id_list))
                    livedocs_final_id_list.sort()
                    livedocs_final_list = [Live_Doctor.objects.get(id=x) for x in livedocs_final_id_list]
                    livedocs_final_list = [x for x in livedocs_final_list if key in x.sponsored_rank['CC_RANK_list']]


                    docs_final_id_list = AttachWithDoctor.objects.filter(doctor_id__in=docs_all_id_list,organisation_id__in=orgs_id_list).values_list('doctor_id',flat=True)
                    docs_final_id_list = list(set(docs_final_id_list))
                    docs_final_id_list.sort()
                    docs_final_list = [Doctor.objects.get(id=x) for x in docs_final_id_list]
                    docs_final_list = [x for x in docs_final_list if key in x.sponsored_rank['CC_RANK_list']]

                    combined_list = []
                    combined_list.extend(livedocs_final_list)
                    combined_list.extend(docs_final_list)

                    CATEGORYNAME = Category.objects.get(id=catt).name
                    CITYNAME = City.objects.get(id=cityy).name

                    # try:
                    #     writer.writerow({'Doctor ID': 0, 'Doctor Name': 'THIS IS'.encode('utf-8'),
                    #                      'Is Live Doctor/Doctor': 'CC Rank Doctor LIST'.encode('utf-8'),
                    #                      'Stage': 'FOR'.encode('utf-8'),
                    #                      'User': '----'.encode('utf-8'),
                    #                      'Category': CATEGORYNAME.encode('utf-8'),
                    #                      'City': CITYNAME.encode('utf-8'),
                    #                      'Location': '----'.encode('utf-8'),
                    #                      'CC Sponsored Rank' : '----'.encode('utf-8'),
                    #                      'CC Subscribed Rank': '----'.encode('utf-8'),
                    #                      'CC Trial Rank': '----'.encode('utf-8'),
                    #                      'CLC Sponsored Rank': '----'.encode('utf-8'),
                    #                      'CLC Subscribed Rank': '----'.encode('utf-8'),
                    #                      'CLC Trial Rank' : '----'.encode('utf-8'),
                    #                      })
                    #     print "---------------- "
                    #
                    # except Exception as p:
                    #     print p

                    for ddoc in combined_list:
                        stagename = ddoc.stage.stage_name
                        username = ddoc.current_user.username
                        if ddoc.__class__.__name__ == 'Doctor':
                            type = 'Doctor'
                            docname = ddoc.name
                        else:
                            type = "Live Doctor"
                            docname = ddoc.firstName+' '+ddoc.lastName
                        try:
                            writer.writerow({'Doctor ID': ddoc.id, 'Doctor Name': docname.encode('utf-8'),
                                             'Is Live Doctor/Doctor': type.encode('utf-8'),
                                             'Stage': stagename.encode('utf-8'),
                                             'User': username.encode('utf-8'),
                                             'Category': CATEGORYNAME.encode('utf-8'),
                                             'City': CITYNAME.encode('utf-8'),
                                             'Location': 'N/A'.encode('utf-8'),
                                             'CC Sponsored Rank': ddoc.sponsored_rank['CC_RANK_list'][key],
                                             'CC Subscribed Rank': ddoc.subscribed_rank['CC_RANK_list'][key],
                                             'CC Trial Rank': ddoc.trial_rank['CC_RANK_list'][key],
                                             'CLC Sponsored Rank': 'N/A'.encode('utf-8'),
                                             'CLC Subscribed Rank': 'N/A'.encode('utf-8'),
                                             'CLC Trial Rank': 'N/A'.encode('utf-8'),
                                             })
                            print "---------------- "

                        except Exception as p:
                            print p

                    # try:
                    #     writer.writerow({'Doctor ID': 0, 'Doctor Name': 'THIS IS'.encode('utf-8'),
                    #                      'Is Live Doctor/Doctor': 'CLC Rank Doctor LIST'.encode('utf-8'),
                    #                      'Stage': 'FOR'.encode('utf-8'),
                    #                      'User': '----'.encode('utf-8'),
                    #                      'Category': CATEGORYNAME.encode('utf-8'),
                    #                      'City': CITYNAME.encode('utf-8'),
                    #                      'Location': 'LOCALITIES IN THIS CATEGORY'.encode('utf-8'),
                    #                      'CC Sponsored Rank' : '----'.encode('utf-8'),
                    #                      'CC Subscribed Rank': '----'.encode('utf-8'),
                    #                      'CC Trial Rank': '----'.encode('utf-8'),
                    #                      'CLC Sponsored Rank': '----'.encode('utf-8'),
                    #                      'CLC Subscribed Rank': '----'.encode('utf-8'),
                    #                      'CLC Trial Rank' : '----'.encode('utf-8'),
                    #                      })
                    #     print "---------------- "
                    # except Exception as p:
                    #     print p

                    locality_list = Locality.objects.filter(city_id=cityy).values_list('id',flat=True)
                    for locc in locality_list:

                        LOCALITYNAME =Locality.objects.get(id=locc).name
                        key = str(cityy) + '-' + str(locc) + '-' + str(catt)
                        orgs_id_list = OrganisationName.objects.filter(country_id=1, state_id=1,city_id=cityy,locality_id=locc).values_list('id', flat=True)

                        livedocs_final_id_list = Live_Doctor_Commonworkschedule.objects.filter(doctor_id__in=livedocs_all_id_list, clinic_id__in=orgs_id_list).values_list('doctor_id',flat=True)
                        livedocs_final_id_list = list(set(livedocs_final_id_list))
                        livedocs_final_id_list.sort()
                        livedocs_final_list = [Live_Doctor.objects.get(id=x) for x in livedocs_final_id_list]
                        livedocs_final_list = [x for x in livedocs_final_list if key in x.sponsored_rank['CC_RANK_list']]

                        docs_final_id_list = AttachWithDoctor.objects.filter(doctor_id__in=docs_all_id_list,organisation_id__in=orgs_id_list).values_list('doctor_id', flat=True)
                        docs_final_id_list = list(set(docs_final_id_list))
                        docs_final_id_list.sort()
                        docs_final_list = [Doctor.objects.get(id=x) for x in docs_final_id_list]
                        docs_final_list = [x for x in docs_final_list if key in x.sponsored_rank['CLC_RANK_list']]

                        combined_list = []
                        combined_list.extend(livedocs_final_list)
                        combined_list.extend(docs_final_list)

                        for ddoc in combined_list:
                            stagename = ddoc.stage.stage_name
                            username = ddoc.current_user.username
                            if ddoc.__class__.__name__ == 'Doctor':
                                type = 'Doctor'
                                docname = ddoc.name
                            else:
                                type = "Live Doctor"
                                docname = ddoc.firstName + ' ' + ddoc.lastName
                            try:
                                writer.writerow({'Doctor ID': ddoc.id, 'Doctor Name': docname.encode('utf-8'),
                                                 'Is Live Doctor/Doctor': type.encode('utf-8'),
                                                 'Stage': stagename.encode('utf-8'),
                                                 'User': username.encode('utf-8'),
                                                 'Category': CATEGORYNAME.encode('utf-8'),
                                                 'City': CITYNAME.encode('utf-8'),
                                                 'Location': LOCALITYNAME.encode('utf-8'),
                                                 'CC Sponsored Rank': 'N/A'.encode('utf-8'),
                                                 'CC Subscribed Rank':'N/A'.encode('utf-8'),
                                                 'CC Trial Rank':'N/A'.encode('utf-8'),
                                                 'CLC Sponsored Rank': ddoc.sponsored_rank['CLC_RANK_list'][key],
                                                 'CLC Subscribed Rank': ddoc.subscribed_rank['CLC_RANK_list'][key],
                                                 'CLC Trial Rank': ddoc.trial_rank['CLC_RANK_list'][key],
                                                 })
                                print "---------------- "

                            except Exception as p:
                                print p
                            # try:
                            #     writer.writerow({'Doctor ID': 0, 'Doctor Name': '******'.encode('utf-8'),
                            #                      'Is Live Doctor/Doctor': '******'.encode('utf-8'),
                            #                      'Stage': '******'.encode('utf-8'),
                            #                      'User': '******'.encode('utf-8'),
                            #                      'Category': '******'.encode('utf-8'),
                            #                      'City': '******'.encode('utf-8'),
                            #                      'Location': '******'.encode('utf-8'),
                            #                      'CC Sponsored Rank': '******'.encode('utf-8'),
                            #                      'CC Subscribed Rank': '******'.encode('utf-8'),
                            #                      'CC Trial Rank': '******'.encode('utf-8'),
                            #                      'CLC Sponsored Rank': '******'.encode('utf-8'),
                            #                      'CLC Subscribed Rank': '******'.encode('utf-8'),
                            #                      'CLC Trial Rank': '******'.encode('utf-8'),
                            #                      })
                            #     print "---------------- "
                            # except Exception as p:
                            #     print p

                    # for gap in range(0,3):
                    #     try:
                    #         writer.writerow({'Doctor ID': 0, 'Doctor Name': ''.encode('utf-8'),
                    #                          'Is Live Doctor/Doctor': ''.encode('utf-8'),
                    #                          'Stage': ''.encode('utf-8'),
                    #                          'User': ''.encode('utf-8'),
                    #                          'Category': ''.encode('utf-8'),
                    #                          'City': ''.encode('utf-8'),
                    #                          'Location': ''.encode('utf-8'),
                    #                          'CC Sponsored Rank': ''.encode('utf-8'),
                    #                          'CC Subscribed Rank': ''.encode('utf-8'),
                    #                          'CC Trial Rank': ''.encode('utf-8'),
                    #                          'CLC Sponsored Rank': ''.encode('utf-8'),
                    #                          'CLC Subscribed Rank': ''.encode('utf-8'),
                    #                          'CLC Trial Rank': ''.encode('utf-8'),
                    #                          })
                    #         print "---------------- "
                    #     except Exception as p:
                    #         print p
                # for gap in range(0,6):
                #     try:
                #         writer.writerow({'Doctor ID': 0, 'Doctor Name': ''.encode('utf-8'),
                #                          'Is Live Doctor/Doctor': ''.encode('utf-8'),
                #                          'Stage': ''.encode('utf-8'),
                #                          'User': ''.encode('utf-8'),
                #                          'Category': ''.encode('utf-8'),
                #                          'City': ''.encode('utf-8'),
                #                          'Location': ''.encode('utf-8'),
                #                          'CC Sponsored Rank': ''.encode('utf-8'),
                #                          'CC Subscribed Rank': ''.encode('utf-8'),
                #                          'CC Trial Rank': ''.encode('utf-8'),
                #                          'CLC Sponsored Rank': ''.encode('utf-8'),
                #                          'CLC Subscribed Rank': ''.encode('utf-8'),
                #                          'CLC Trial Rank': ''.encode('utf-8'),
                #                          })
                #         print "---------------- "
                #     except Exception as p:
                #         print p
        return response

    except Exception as e:
        print "%% OUTER %%%%%%%%%%%%%%%%%%%%%%%  ", e
        print e
        return HttpResponse("IN - COMPLETE")

#################################
# Written by Dhrumil            #
# Live Doctor all fields extract#
#################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def live_doctor_export(request):
    try:
        live_doctor=Live_Doctor.objects.all().order_by('id')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=live_doctor_extract.csv'
        # with open('org_attached_docs.csv', 'w') as csvfile:

        if len(live_doctor):
            fieldnames = ['ID','First Name', 'Last Name', 'Zone', 'Zone Location', 'User', 'Stage', 'Is Disable', 'Category', 'Services offered', 'Specility Interest',
                          'Phone Number', 'Fax', 'Mobile Number', 'Email ID', 'Secondary Email ID', 'Associated Organisation ID',
                          'Associated Organisation Name', 'Organisatin User', 'Organisation Stage', 'Organisation Is Disable',
                          'Address of Organisation', 'Location of Organisation', 'City of Organision',
                          'Organisation Mobile', 'Organisation Telephone', 'Organisation Email', 'Attach Organisation DID',
                          'Attach Organisation Extension']
            writer = csv.DictWriter(response, fieldnames=fieldnames)
            writer.writeheader()
            for i in live_doctor:
                doc_id=i.id
                # doc_id= 200194
                doc_firstname=i.firstName
                doc_lastname=i.lastName
                try:
                    doc_zone = i.zone.name
                except:
                    doc_zone = 'N/A'
                try:
                    doc_zoneloca = i.zone_location.name
                except:
                    doc_zoneloca = 'N/A'
                try:
                    doc_user = i.current_user.username
                except:
                    doc_user = 'N/A'
                try:
                    doc_stage = i.stage.stage_name
                except:
                    doc_stage - 'N/A'
                if i.is_disable == True:
                    doc_status = 'True'
                else:
                    doc_status = 'False'
                try:
                    cat=Category.objects.get(id=i.category)
                    doc_cat=cat.name
                except:
                    doc_cat='N/A'
                try:
                    so=i.new_service_offered_final
                    if so:
                        temp=[]
                        if so:
                            for j in so:
                                for k,v in j.items():
                                    if k=='name':
                                        temp.append(v)
                            doc_so=','.join(temp)
                    else:
                        doc_so='N/A'
                except:
                    temp='N/A'
                spe_int=i.new_speciality_final
                if spe_int:
                    temp1=[]
                    if spe_int:
                        for j in spe_int:
                            for k,v in j.items():
                                if k=='name':
                                    temp1.append(v)
                        doc_speint=','.join(temp1)
                else:
                    doc_speint='N/A'
                if i.phoneNo:
                    doc_phn=i.phoneNo
                else:
                    doc_phn='N/A'
                if i.mobileNo:
                    doc_mobile=i.mobileNo
                else:
                    doc_mobile='N/A'
                if i.fax:
                    doc_fax=i.fax
                else:
                    doc_fax='N/A'
                if i.email:
                    doc_email=i.email
                else:
                    doc_email='N/A'
                if i.alternateEmail:
                    doc_secdemail=i.alternateEmail
                else:
                    doc_secdemail='N/A'
                attach_org = Live_Doctor_Commonworkschedule.objects.filter(Q(doctor_id=int(doc_id)),~Q(status='delete'))
                if list(attach_org) != []:
                    for j in attach_org:
                        if j.clinic_id:
                            try:
                                org = OrganisationName.objects.get(id=int(j.clinic_id))
                            except:
                                pass
                            org_id = org.id
                            try:
                                if org.name:
                                    org_name = org.name
                                else:
                                    org_name = 'N/A'
                            except:
                                org_name = 'N/A'
                            try:
                                if org.current_user:
                                    org_user = org.current_user.username
                                else:
                                    org_user = 'N/A'
                            except:
                                org_user = 'N/A'
                            try:
                                if org.stage:
                                    org_stage = org.stage.stage_name
                                else:
                                    org_stage = 'N/A'
                            except:
                                org_stage = 'N/A'
                            if org.is_disable == True:
                                org_status = 'True'
                            else:
                                org_status = 'False'
                            try:
                                if org.street:
                                    org_address = org.street
                                else:
                                    org_address = 'N/A'
                            except:
                                org_address = 'N/A'
                            try:
                                if org.locality:
                                    org_locality_name = org.locality.name
                                else:
                                    org_locality_name = 'N/A'
                            except:
                                org_locality_name = 'N/A'
                            try:
                                if org.city:
                                    org_city = org.city.name
                                else:
                                    org_city = 'N/A'
                            except:
                                org_city = 'N/A'
                            try:
                                if org.mobile_no:
                                    org_mobile = org.mobile_no
                                else:
                                    org_mobile = 'N/A'
                            except:
                                org_mobile = 'N/A'
                            try:
                                if org.phone:
                                    org_telephone = org.phone
                                else:
                                    org_telephone = 'N/A'
                            except:
                                org_telephone = 'N/A'
                            try:
                                if org.email:
                                    org_email = org.email
                                else:
                                    org_email = 'N/A'
                            except:
                                org_email = 'N/A'
                            if j.did:
                                org_did = j.did
                            else:
                                org_did = 'N/A'
                            if j.extension:
                                org_extn = j.extension
                            else:
                                org_extn = 'N/A'
                            try:
                                writer.writerow({'ID':doc_id,
                                                 'First Name':doc_firstname.encode('utf-8'),
                                                 'Last Name':doc_lastname.encode('utf-8'),
                                                 'Zone': doc_zone.encode('utf-8'),
                                                 'Zone Location': doc_zoneloca.encode('utf-8'),
                                                 'User': doc_user.encode('utf-8'),
                                                 'Stage': doc_stage.encode('utf-8'),
                                                 'Is Disable': doc_status.encode('utf-8'),
                                                 'Category':doc_cat.encode('utf-8'),
                                                 'Services offered':doc_so.encode('utf-8'),
                                                 'Specility Interest':doc_speint.encode('utf-8'),
                                                 'Phone Number':doc_phn.encode('utf-8'),
                                                 'Fax':doc_fax.encode('utf-8'),
                                                 'Mobile Number':doc_mobile.encode('utf-8'),
                                                 'Email ID':doc_email.encode('utf-8'),
                                                 'Secondary Email ID':doc_secdemail.encode('utf-8'),
                                                 'Associated Organisation ID': org_id,
                                                 'Associated Organisation Name': org_name.encode('utf-8'),
                                                 'Organisatin User': org_user.encode('utf-8'),
                                                 'Organisation Stage': org_stage.encode('utf-8'),
                                                 'Organisation Is Disable': org_status.encode('utf-8'),
                                                 'Address of Organisation': org_address.encode('utf-8'),
                                                 'Location of Organisation': org_locality_name.encode('utf-8'),
                                                 'City of Organision': org_city.encode('utf-8'),
                                                 'Organisation Mobile': org_mobile.encode('utf-8'),
                                                 'Organisation Telephone': org_telephone.encode('utf-8'),
                                                 'Organisation Email': org_email.encode('utf-8'),
                                                 'Attach Organisation DID': org_did.encode('utf-8'),
                                                 'Attach Organisation Extension': org_extn.encode('utf-8')})
                                print i.id, '~~~~~', org.id
                            except Exception as p:
                                print p, '~~~~~~~', i.id, i.name, '~~~~~~~', org.id, org.name
                                pass
                        else:
                            pass
                else:
                    try:
                        writer.writerow({'ID': doc_id,
                                         'First Name': doc_firstname.encode('utf-8'),
                                         'Last Name': doc_lastname.encode('utf-8'),
                                         'Zone': doc_zone.encode('utf-8'),
                                         'Zone Location': doc_zoneloca.encode('utf-8'),
                                         'User': doc_user.encode('utf-8'),
                                         'Stage': doc_stage.encode('utf-8'),
                                         'Is Disable': doc_status.encode('utf-8'),
                                         'Category': doc_cat.encode('utf-8'),
                                         'Services offered': doc_so.encode('utf-8'),
                                         'Specility Interest': doc_speint.encode('utf-8'),
                                         'Phone Number': doc_phn.encode('utf-8'),
                                         'Fax': doc_fax.encode('utf-8'),
                                         'Mobile Number': doc_mobile.encode('utf-8'),
                                         'Email ID': doc_email.encode('utf-8'),
                                         'Secondary Email ID': doc_secdemail.encode('utf-8'),
                                         'Associated Organisation ID': 'N/A',
                                         'Associated Organisation Name': 'N/A',
                                         'Organisatin User': 'N/A',
                                         'Organisation Stage': 'N/A',
                                         'Organisation Is Disable': 'N/A',
                                         'Address of Organisation': 'N/A',
                                         'Location of Organisation': 'N/A',
                                         'City of Organision': 'N/A',
                                         'Organisation Mobile': 'N/A',
                                         'Organisation Telephone': 'N/A',
                                         'Organisation Email': 'N/A',
                                         'Attach Organisation DID': 'N/A',
                                         'Attach Organisation Extension': 'N/A'})
                        print i.id, '~~~~~', org.id
                    except Exception as p:
                        print p, '~~~~~~~', i.id, i.name, '~~~~~~~', org.id, org.name
                        pass
        return response
    except Exception as e:
        print e

#######################
#Written By - Dhrumil  #
#Doctor Extract        #
#######################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def docs_export(request):
    try:
        from hfu_cms.data_publisher import convert_time_str_array
        Docs=Doctor.objects.all().order_by('id')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=all_doctor_export.csv'
        # with open('org_attached_docs.csv', 'w') as csvfile:

        if len(Docs):
            fieldnames = ['Doctor ID', 'Doctor Name', 'Doctor Zone', 'User', 'Stage', 'Is Disable', 'Doctor Category',
                          'Speciality New', 'Services Offered new', 'Doctor Mobile', 'Doctor Telepohone', 'Doctor Email', 'Doctor Alternate Email',
                          'Associated Organisation ID', 'Associated Organisation Name', 'Organisatin User', 'Organisation Stage', 'Organisation Is Disable',
                          'Address of Organisation', 'Location of Organisation', 'City of Organision',
                          'Organisation Mobile', 'Organisation Telephone', 'Organisation Email', 'Attach Organisation DID',
                          'Attach Organisation Extension']
            writer = csv.DictWriter(response, fieldnames=fieldnames)
            writer.writeheader()
            for d in Docs:
                doc_id=d.id
                try:
                    if d.name:
                        doc_name=d.name
                    else:
                        doc_name='N/A'
                except:
                    doc_name='N/A'
                if d.zone:
                    doc_zone=d.zone.name
                else:
                    doc_zone='N/A'
                if d.current_user:
                    doc_user=d.current_user.username
                else:
                    doc_user='N/A'
                if d.stage:
                    doc_stage=d.stage.stage_name
                else:
                    doc_stage='N/A'
                if d.is_disable == True:
                    doc_status = 'True'
                else:
                    doc_status = 'False'
                try:
                    if d.category:
                        doc_category = d.category.name
                    else:
                        doc_category='N/A'
                except:
                    doc_category = 'N/A'
                if d.new_speciality_final:
                    spe=d.new_speciality_final.split(',')
                    temp=[]
                    for i in spe:
                        speciality=Doctor_Speciality_New.objects.get(id=i)
                        spe_name=speciality.name
                        temp.append(spe_name)
                    doc_spe_new=','.join(temp)
                else:
                    doc_spe_new='N/A'
                if d.new_service_offered_final:
                    so=d.new_service_offered_final.split(',')
                    temp=[]
                    for i in so:
                        seroff=Doctor_ServiceOffered_New.objects.get(id=i)
                        so_name=seroff.name
                        temp.append(so_name)
                    doc_so_new=','.join(temp)
                else:
                    doc_so_new='N/A'
                if d.mobile_no:
                    doc_mobile=d.mobile_no
                else:
                    doc_mobile='N/A'
                if d.phone:
                    doc_phone=d.phone
                else:
                    doc_phone='N/A'
                if d.email:
                    doc_email=d.email
                else:
                    doc_email='N/A'
                if d.secondary_email:
                    doc_alternateemail=d.secondary_email
                else:
                    doc_alternateemail='N/A'
                attached_orgs = AttachWithDoctor.objects.filter(doctor_id=d.id)
                if list(attached_orgs) != []:
                    for j in attached_orgs:
                        org = OrganisationName.objects.get(id=j.organisation_id)
                        org_id = org.id
                        try:
                            if org.name:
                                org_name = org.name
                            else:
                                org_name='N/A'
                        except:
                            org_name='N/A'
                        try:
                            if org.current_user:
                                org_user = org.current_user.username
                            else:
                                org_user='N/A'
                        except:
                            org_user='N/A'
                        try:
                            if org.stage:
                                org_stage = org.stage.stage_name
                            else:
                                org_stage='N/A'
                        except:
                            org_stage='N/A'
                        if org.is_disable == True:
                            org_status = 'True'
                        else:
                            org_status = 'False'
                        try:
                            if org.street:
                                org_address = org.street
                            else:
                                org_address='N/A'
                        except:
                            org_address='N/A'
                        try:
                            if org.locality:
                                org_locality_name = org.locality.name
                            else:
                                org_locality_name='N/A'
                        except:
                            org_locality_name='N/A'
                        try:
                            if org.city:
                                org_city = org.city.name
                            else:
                                org_city='N/A'
                        except:
                            org_city='N/A'
                        try:
                            if org.mobile_no:
                                org_mobile = org.mobile_no
                            else:
                                org_mobile='N/A'
                        except:
                            org_mobile='N/A'
                        try:
                            if org.phone:
                                org_telephone = org.phone
                            else:
                                org_telephone='N/A'
                        except:
                            org_telephone='N/A'
                        try:
                            if org.email:
                                org_email = org.email
                            else:
                                org_email='N/A'
                        except:
                            org_email='N/A'
                        if j.did:
                            org_did = j.did
                        else:
                            org_did = 'N/A'
                        if j.extension:
                            org_extn = j.extension
                        else:
                            org_extn='N/A'
                        try:
                            writer.writerow({'Doctor ID':doc_id,
                                             'Doctor Name':doc_name.encode('utf-8'),
                                             'Doctor Zone':doc_zone.encode('utf-8'),
                                             'User':doc_user.encode('utf-8'),
                                             'Stage':doc_stage.encode('utf-8'),
                                             'Is Disable':doc_status.encode('utf-8'),
                                             'Doctor Category':doc_category.encode('utf-8'),
                                             'Speciality New':doc_spe_new.encode('utf-8'),
                                             'Services Offered new':doc_so_new.encode('utf-8'),
                                             'Doctor Mobile':doc_mobile.encode('utf-8'),
                                             'Doctor Telepohone':doc_phone.encode('utf-8'),
                                             'Doctor Email':doc_email.encode('utf-8'),
                                             'Doctor Alternate Email':doc_alternateemail.encode('utf-8'),
                                             'Associated Organisation ID':org_id,
                                             'Associated Organisation Name':org_name.encode('utf-8'),
                                             'Organisatin User':org_user.encode('utf-8'),
                                             'Organisation Stage':org_stage.encode('utf-8'),
                                             'Organisation Is Disable':org_status.encode('utf-8'),
                                             'Address of Organisation':org_address.encode('utf-8'),
                                             'Location of Organisation':org_locality_name.encode('utf-8'),
                                             'City of Organision':org_city.encode('utf-8'),
                                             'Organisation Mobile':org_mobile.encode('utf-8'),
                                             'Organisation Telephone':org_telephone.encode('utf-8'),
                                             'Organisation Email':org_email.encode('utf-8'),
                                             'Attach Organisation DID':org_did.encode('utf-8'),
                                             'Attach Organisation Extension':org_extn.encode('utf-8')})
                            print d.id, '~~~~~', org.id
                        except Exception as p:
                            print p, '~~~~~~~',d.id,d.name,'~~~~~~~',org.id,org.name
                            pass
                else:
                    try:
                        writer.writerow({'Doctor ID': doc_id,
                                         'Doctor Name': doc_name.encode('utf-8'),
                                         'Doctor Zone': doc_zone.encode('utf-8'),
                                         'User': doc_user.encode('utf-8'),
                                         'Stage': doc_stage.encode('utf-8'),
                                         'Is Disable': doc_status.encode('utf-8'),
                                         'Doctor Category': doc_category.encode('utf-8'),
                                         'Speciality New': doc_spe_new.encode('utf-8'),
                                         'Services Offered new': doc_so_new.encode('utf-8'),
                                         'Doctor Mobile': doc_mobile.encode('utf-8'),
                                         'Doctor Telepohone': doc_phone.encode('utf-8'),
                                         'Doctor Email': doc_email.encode('utf-8'),
                                         'Doctor Alternate Email': doc_alternateemail.encode('utf-8'),
                                         'Associated Organisation ID': 'N\A',
                                         'Associated Organisation Name': 'N\A',
                                         'Organisatin User': 'N\A',
                                         'Organisation Stage': 'N\A',
                                         'Organisation Is Disable': 'N\A',
                                         'Address of Organisation': 'N\A',
                                         'Location of Organisation': 'N\A',
                                         'City of Organision': 'N\A',
                                         'Organisation Mobile': 'N\A',
                                         'Organisation Telephone': 'N\A',
                                         'Organisation Email': 'N\A',
                                         'Attach Organisation DID': 'N\A',
                                         'Attach Organisation Extension': 'N\A'})
                        print d.id, '~~~~~', org.id
                    except Exception as p:
                        print p, '~~~~~~~', d.id, d.name, '~~~~~~~', org.id, org.name
                        pass
        return response
    except Exception as e:
        print e