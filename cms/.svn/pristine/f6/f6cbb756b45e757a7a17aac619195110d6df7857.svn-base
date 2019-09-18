from django.core.management.base import BaseCommand, CommandError
from hfu_cms.models import Category,Live_Doctor,Live_Doctor_Commonworkschedule,OrganisationName,Live_Doctor_Schedule_Stopdate_Notification
from hfu_cms.models import City,Locality
from django.db.models import Q
from hfu_cms.models import AttachWithDoctor,Doctor,Doctor_Schedule_Stopdate_Notification

class Command(BaseCommand):
    help = 'Type the help text here'

    def handle(self, *args, **options):
        with open('/tmp/schz.txt', mode='w') as ff:
            ff.write(str('----ss----'))

        try:
            All_ldoccs = Live_Doctor.objects.filter((~Q(sponsored_end_dates={})),(~Q(sponsored_end_dates=None)))
            with open('/tmp/schz.txt', mode='w') as ff:
                ff.write(str('--------'))
            for ddoc in All_ldoccs:
                already_checked = []
                doc_sch_list_count = Live_Doctor_Commonworkschedule.objects.filter((~Q(status__iexact='delete')),doctor_id=ddoc.id).count()
                if doc_sch_list_count !=  0:
                    doc_sch_list = Live_Doctor_Commonworkschedule.objects.filter((~Q(status__iexact='delete')), doctor_id=ddoc.id)
                    with open('/tmp/sch.txt', mode='w') as ff:
                        ff.write(str(doc_sch_list))
                    for sch in doc_sch_list:
                        obj_ins = None
                        days_left_cc = None
                        days_left_clc = None

                        city_id = OrganisationName.objects.get(id=sch.clinic_id).city_id
                        locality_id = OrganisationName.objects.get(id=sch.clinic_id).locality_id
                        category_id = ddoc.category

                        Key_CC_RANK = str(city_id)  + '-' + str(category_id)
                        Key_CC_RANK_LABEL = City.objects.get(id=city_id).name  + '-' + Category.objects.get(id=category_id).name
                        Key_CLC_RANK = str(city_id) + '-' + str(locality_id) + '-' + str(category_id)
                        Key_CLC_RANK_LABEL = City.objects.get(id=city_id).name + '-' + Locality.objects.get(id=locality_id).name + '-' + Category.objects.get(id=category_id).name

                        if tuple([Key_CC_RANK,Key_CLC_RANK]) not in already_checked :
                            import datetime as ddtt
                            today = ddtt.date.today()
                            days_left_15 = today + ddtt.timedelta(days=15)
                            days_left_7 = today + ddtt.timedelta(days=7)
                            days_left_3 = today + ddtt.timedelta(days=3)
                            days_left_1 = today + ddtt.timedelta(days=1)

                            cc_stop_date = ddoc.sponsored_end_dates.get(Key_CC_RANK,None)
                            if cc_stop_date != None and cc_stop_date != '' and cc_stop_date.count('/') == 2 :
                                date_split = cc_stop_date.split('/')
                                x = ddtt.date(int(date_split[2]),int(date_split[1]),int(date_split[0]))
                                do_set='No'
                                if x == days_left_15:
                                    days_left_cc = 15
                                    do_set = 'Yes'
                                if x == days_left_7:
                                    days_left_cc = 7
                                    do_set = 'Yes'
                                if x == days_left_3:
                                    days_left_cc = 3
                                    do_set = 'Yes'
                                if x == days_left_1:
                                    days_left_cc = 1
                                    do_set = 'Yes'
                                if do_set == 'Yes':
                                    try:
                                        stage_name = ddoc.stage.stage_name
                                    except:
                                        stage_name = ''
                                    obj_ins =Live_Doctor_Schedule_Stopdate_Notification(livedoctor=ddoc,livedoctorName=ddoc.firstName+' '+ddoc.lastName,
                                         category=Category.objects.get(id=category_id).name,clinic=OrganisationName.objects.get(id=sch.clinic_id),
                                         spon_cc_rank=ddoc.sponsored_rank['CC_RANK_list'].get(Key_CC_RANK,None),spon_cc_key= Key_CC_RANK,
                                         spon_cc_key_label=Key_CC_RANK_LABEL,updatedBy='CMS',
                                         livedoctorCurrentUser=ddoc.current_user.username,livedoctorStage=stage_name,
                                         days_left_cc=days_left_cc,expiry_date_cc=x)
                                x = None
                                do_set = 'No'
                                with open('/home/kanhaiya/CHECKPOINT1.txt', mode='w') as ff:
                                    ff.write(str("DONE 111"))

                            clc_stop_date = ddoc.sponsored_end_dates.get(Key_CLC_RANK, None)
                            if clc_stop_date != None and clc_stop_date != '' and clc_stop_date.count('/') == 2 :

                                date_split = clc_stop_date.split('/')
                                x = ddtt.date(int(date_split[2]), int(date_split[1]), int(date_split[0]))
                                do_set = 'No'
                                if x == days_left_15:
                                    days_left_clc = 15
                                    do_set = 'YES'
                                if x == days_left_7:
                                    days_left_clc = 7
                                    do_set = 'YES'
                                if x == days_left_3:
                                    days_left_clc = 3
                                    do_set = 'YES'
                                if x == days_left_1:
                                    days_left_clc = 1
                                    do_set = 'YES'

                                if do_set == 'YES':
                                    if obj_ins != None:
                                        obj_ins.days_left_clc = days_left_clc
                                        obj_ins.expiry_date_clc = x
                                        obj_ins.spon_clc_rank = ddoc.sponsored_rank['CLC_RANK_list'].get(Key_CLC_RANK, None)
                                        obj_ins.spon_clc_key = Key_CLC_RANK
                                        obj_ins.spon_clc_key_label = Key_CLC_RANK_LABEL
                                    else:
                                        try:
                                            stage_name = ddoc.stage.stage_name
                                        except:
                                            stage_name = ''
                                        obj_ins = Live_Doctor_Schedule_Stopdate_Notification(livedoctor=ddoc,
                                                                                         livedoctorName=ddoc.firstName + ' ' + ddoc.lastName,
                                                                                         category=Category.objects.get(
                                                                                             id=category_id).name,
                                                                                         clinic=OrganisationName.objects.get(id=sch.clinic_id),
                                                                                         spon_clc_rank=ddoc.sponsored_rank[
                                                                                             'CLC_RANK_list'].get(Key_CLC_RANK, None),
                                                                                         spon_clc_key=Key_CLC_RANK,
                                                                                         spon_clc_key_label=Key_CLC_RANK_LABEL,
                                                                                         updatedBy='CMS',
                                                                                         livedoctorCurrentUser=ddoc.current_user.username,
                                                                                         livedoctorStage=stage_name,
                                                                                         days_left_clc=days_left_clc,
                                                                                         expiry_date_clc=x)
                                    do_set = 'No'


                            if obj_ins != None:
                                already_checked.append(tuple([Key_CC_RANK,Key_CLC_RANK]))


                                obj_ins.save()


        except Exception as e:

            with open('/tmp/exception.txt',mode='w') as ff:
                ff.write(str(e))

        with open('/tmp/firstdone.txt', mode='w') as ff:
            ff.write(str("1st done"))
        try:
            All_ldoccs = Doctor.objects.filter((~Q(sponsored_end_dates={})),(~Q(sponsored_end_dates=None)))
            with open('/tmp/onlydoctor.txt', mode='w') as ff:
                ff.write(str('--------'))
            for ddoc in All_ldoccs:
                already_checked = []
                doc_sch_list_count = AttachWithDoctor.objects.filter(doctor_id=ddoc.id).count()
                if doc_sch_list_count !=  0:
                    doc_sch_list = AttachWithDoctor.objects.filter(doctor_id=ddoc.id)
                    # with open('/home/kanhaiya/sch.txt', mode='w') as ff:
                    #     ff.write(str(doc_sch_list))
                    for sch in doc_sch_list:
                        obj_ins = None
                        days_left_cc = None
                        days_left_clc = None

                        city_id = OrganisationName.objects.get(id=sch.clinic_id).city_id
                        locality_id = OrganisationName.objects.get(id=sch.clinic_id).locality_id
                        category_id = ddoc.category

                        Key_CC_RANK = str(city_id)  + '-' + str(category_id)
                        Key_CC_RANK_LABEL = City.objects.get(id=city_id).name  + '-' + Category.objects.get(id=category_id).name
                        Key_CLC_RANK = str(city_id) + '-' + str(locality_id) + '-' + str(category_id)
                        Key_CLC_RANK_LABEL = City.objects.get(id=city_id).name + '-' + Locality.objects.get(id=locality_id).name + '-' + Category.objects.get(id=category_id).name

                        if tuple([Key_CC_RANK,Key_CLC_RANK]) not in already_checked :
                            import datetime as ddtt
                            today = ddtt.date.today()
                            days_left_15 = today + ddtt.timedelta(days=15)
                            days_left_7 = today + ddtt.timedelta(days=7)
                            days_left_3 = today + ddtt.timedelta(days=3)
                            days_left_1 = today + ddtt.timedelta(days=1)

                            cc_stop_date = ddoc.sponsored_end_dates.get(Key_CC_RANK,None)
                            if cc_stop_date != None and cc_stop_date != '' and cc_stop_date.count('/') == 2 :
                                date_split = cc_stop_date.split('/')
                                x = ddtt.date(int(date_split[2]),int(date_split[1]),int(date_split[0]))
                                do_set='No'
                                if x == days_left_15:
                                    days_left_cc = 15
                                    do_set = 'Yes'
                                if x == days_left_7:
                                    days_left_cc = 7
                                    do_set = 'Yes'
                                if x == days_left_3:
                                    days_left_cc = 3
                                    do_set = 'Yes'
                                if x == days_left_1:
                                    days_left_cc = 1
                                    do_set = 'Yes'
                                if do_set == 'Yes':
                                    try:
                                        stage_name = ddoc.stage.stage_name
                                    except:
                                        stage_name = ''
                                    obj_ins =Doctor_Schedule_Stopdate_Notification(doctor=ddoc,doctorName=ddoc.name,
                                         category=Category.objects.get(id=category_id).name,clinic=OrganisationName.objects.get(id=sch.clinic_id),
                                         spon_cc_rank=ddoc.sponsored_rank['CC_RANK_list'].get(Key_CC_RANK,None),spon_cc_key= Key_CC_RANK,
                                         spon_cc_key_label=Key_CC_RANK_LABEL,updatedBy='CMS',
                                         doctorCurrentUser=ddoc.current_user.username,doctorStage=stage_name,
                                         days_left_cc=days_left_cc,expiry_date_cc=x)
                                x = None
                                do_set = 'No'
                                # with open('/home/kanhaiya/CHECKPOINT1.txt', mode='w') as ff:
                                #     ff.write(str("DONE 111"))

                            clc_stop_date = ddoc.sponsored_end_dates.get(Key_CLC_RANK, None)
                            if clc_stop_date != None and clc_stop_date != '' and clc_stop_date.count('/') == 2 :

                                date_split = clc_stop_date.split('/')
                                x = ddtt.date(int(date_split[2]), int(date_split[1]), int(date_split[0]))
                                do_set = 'No'
                                if x == days_left_15:
                                    days_left_clc = 15
                                    do_set = 'YES'
                                if x == days_left_7:
                                    days_left_clc = 7
                                    do_set = 'YES'
                                if x == days_left_3:
                                    days_left_clc = 3
                                    do_set = 'YES'
                                if x == days_left_1:
                                    days_left_clc = 1
                                    do_set = 'YES'

                                if do_set == 'YES':
                                    if obj_ins != None:
                                        obj_ins.days_left_clc = days_left_clc
                                        obj_ins.expiry_date_clc = x
                                        obj_ins.spon_clc_rank = ddoc.sponsored_rank['CLC_RANK_list'].get(Key_CLC_RANK, None)
                                        obj_ins.spon_clc_key = Key_CLC_RANK
                                        obj_ins.spon_clc_key_label = Key_CLC_RANK_LABEL
                                    else:
                                        try:
                                            stage_name = ddoc.stage.stage_name
                                        except:
                                            stage_name = ''
                                        obj_ins = Doctor_Schedule_Stopdate_Notification(doctor=ddoc,
                                                                                         doctorName=ddoc.name,
                                                                                         category=Category.objects.get(
                                                                                             id=category_id).name,
                                                                                         clinic=OrganisationName.objects.get(id=sch.clinic_id),
                                                                                         spon_clc_rank=ddoc.sponsored_rank[
                                                                                             'CLC_RANK_list'].get(Key_CLC_RANK, None),
                                                                                         spon_clc_key=Key_CLC_RANK,
                                                                                         spon_clc_key_label=Key_CLC_RANK_LABEL,
                                                                                         updatedBy='CMS',
                                                                                         doctorCurrentUser=ddoc.current_user.username,
                                                                                         doctorStage=stage_name,
                                                                                         days_left_clc=days_left_clc,
                                                                                         expiry_date_clc=x)
                                    do_set = 'No'


                            if obj_ins != None:
                                already_checked.append(tuple([Key_CC_RANK,Key_CLC_RANK]))


                                obj_ins.save()


        except Exception as e:
            with open('/tmp/onlydoctor.txt', mode='w') as ff:
                ff.write(str(e))