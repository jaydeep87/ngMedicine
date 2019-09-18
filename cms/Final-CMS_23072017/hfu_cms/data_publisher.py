from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import elasticsearch_client
from hfu_cms.models import *
from providers.models import *
from news.models import *
from news.models import *
from providers.models import *
from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.core.mail import send_mail
import datetime

# def send_email(type,slist,flist):
#     import smtplib
#     gmail_user = 'nishank.gupta@jaguarinfotech.com'
#     gmail_pwd = ''
#     FROM = 'nishank.gupta@jaguarinfotech.com'
#     TO = "ashutosh@jaguarinfotech.com"
#     Subject = "Hi Mail"
#     CC = ""
#     BCC = ""
#
#     sslist = ",".join(slist)
#     fflist = ",".join(flist)
#     # Prepare actual message
#     msg = "\r\n".join([
# "Subject: Just a message",
# "From: nishank.gupta@jaguarinfotech.com",
# "To: ashutosh@jaguarinfotech.com",
# "CC:",
# "The Following {} were Successfully Published",
# "{}",
# "The Following {} were Not Published",
# "{}",
# "Why, oh why"
#     ])
#
#     # msg = "\r\n".join([
#     #     "Subject: Just a message",
#     #     "From: nishank.gupta@jaguarinfotech.com",
#     #     "To: ashutosh@jaguarinfotech.com",
#     #     "The Following {} were Successfully Published",
#     #     "{}",
#     #     "The Following {} were Not Published",
#     #     "{}",
#     #     "Why, oh why"""
#     # ])
#
#     msg = msg.format(type,sslist,type,fflist)
#     try:
#         server = smtplib.SMTP("smtp.gmail.com", 587)
#         server.ehlo()
#         server.starttls()
#         server.login(gmail_user, gmail_pwd)
#         server.sendmail(FROM,TO,msg,[CC,BCC])
#         server.close()
#         print 'successfully sent the mail'
#     except Exception as e:
#         print e


# def send_email(type,slist,flist,subjectt):
#     import smtplib
#     from email.mime.multipart import MIMEMultipart
#     from email.mime.text import MIMEText
#
#     # me == my email address
#     # you == recipient's email address
#     me = "nishank.gupta@jaguarinfotech.com"
#     you = "ashutosh@jaguarinfotech.com"
#
#     # Create message container - the correct MIME type is multipart/alternative.
#     msg = MIMEMultipart('alternative')
#     msg['Subject'] = subjectt
#     msg['From'] = me
#     msg['To'] = you
#
#     # Create the body of the message (a plain-text and an HTML version).
#     text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
#     html = """\
#     <html>
#       <head></head>
#       <body>
#         <p>The Following <a style="color:red;">{}</a> were Successfully Published :</p>
#         <p>{}</p>
#         <p>The Following <a style="color:red;" >{}</a> were Not Published :</p>
#         <p>{}</p>
#       </body>
#     </html>
#     """.format(type.title(),",".join(slist),type.title(),",".join(flist))
#
#     # Record the MIME types of both parts - text/plain and text/html.
#     part1 = MIMEText(text, 'plain')
#     part2 = MIMEText(html, 'html')
#
#     # Attach parts into message container.
#     # According to RFC 2046, the last part of a multipart message, in this case
#     # the HTML message, is best and preferred.
#     msg.attach(part1)
#     msg.attach(part2)
#     # Send the message via local SMTP server.
#     mail = smtplib.SMTP('smtp.gmail.com', 587)
#
#     mail.ehlo()
#
#     mail.starttls()
#
#     mail.login('nishank.gupta@jaguarinfotech.com', '')
#     mail.sendmail(me, you, msg.as_string())
#     mail.quit()

def my_send_mail(request,type,slist,flist,subjectt=None,actionn=None):
    try:
        # Create the body of the message (a plain-text and an HTML version).
        from datetime import datetime as datetimechild, timedelta
        from datetime import timedelta
        current_time_in_utc = datetimechild.utcnow()
        result = current_time_in_utc + timedelta(hours=5.5)
        naames = ''
        temps = []
        naamef = ''
        tempf = []
        mymodel = None
        varset = 99
        if type == "doctor":
            mymodel = Doctor
            varset = 'found'
        elif type == "organisation":
            mymodel = OrganisationName
            varset = 'found'
        elif type == "ambulance":
            mymodel = Ambulance
            varset = 'found'
        elif type == "bloodbank":
            mymodel = BloodBank
            varset = 'found'
        elif type == "dietitian":
            mymodel = Dietitian
            varset = 'found'
        elif type == "nurse_bureau":
            mymodel = Nurse_Bureau
            varset = 'found'
        elif type == "pharmacy":
            mymodel = MedicalPharmacyStore
            varset = 'found'
        elif type == "lab":
            mymodel = Labs
            varset = 'found'
        if mymodel != None and varset == 'found':
            for i in slist:
                obj = mymodel.objects.get(id=int(i))
                temps.append(obj.name.strip())
            naames = ",".join(temps)
            for i in flist:
                obj = mymodel.objects.get(id=int(i))
                tempf.append(obj.name.strip())
            naamef = ",".join(tempf)


        if type == "livedoctor":
            for i in slist:
                obj = Live_Doctor.objects.get(id=int(i))
                temps.append(obj.firstName.strip()+' '+obj.lastName.strip())
            naames = ",".join(temps)
            for i in flist:
                obj = Live_Doctor.objects.get(id=int(i))
                tempf.append(obj.firstName.strip()+' '+obj.lastName.strip())
            naamef = ",".join(tempf)
        elif type == "enterpriseplan" or type == "lifeplan" or type == "homeplan":
            for i in slist:
                obj = ServicePlan.objects.get(id=int(i))
                temps.append(obj.plan_name.strip())
            naames = ",".join(temps)
            for i in flist:
                obj = ServicePlan.objects.get(id=int(i))
                tempf.append(obj.plan_name.strip())
            naamef = ",".join(tempf)
        elif type == "disease":
            for i in slist:
                obj = Disease.objects.get(id=int(i))
                temps.append(obj.topic_title.strip())
            naames = ",".join(temps)
            for i in flist:
                obj = Disease.objects.get(id=int(i))
                tempf.append(obj.topic_title.strip())
            naamef = ",".join(tempf)
        elif type == "rehabitation":
            for i in slist:
                obj = RehabCenter.objects.get(id=int(i))
                temps.append(obj.clinic_name.strip())
            naames = ",".join(temps)
            for i in flist:
                obj = RehabCenter.objects.get(id=int(i))
                tempf.append(obj.clinic_name.strip())
            naamef = ",".join(tempf)
        elif type == "symptom":
            for i in slist:
                obj = Symptoms.objects.get(id=int(i))
                temps.append(obj.topic_title.strip())
            naames = ",".join(temps)
            for i in flist:
                obj = Symptoms.objects.get(id=int(i))
                tempf.append(obj.topic_title.strip())
            naamef = ",".join(tempf)
        text = "Hi!\nHow are you?"
        html = """\
        <html>
          <head></head>
          <body>
            <p>The Following <a style="color:red;">{}(s)</a> were Successfully {} : </p>
            <p>{}</p>
            <p>The Following <a style="color:red;" >{}(s)</a> were Not {} :</p>
            <p>{}</p>
            <p>{} by :<span style="color: #19a3e7" >{}</span> </p>
            <p></p>
            <p>{} At :<span style="color: #19a3e7" >{}</span> </p>
          </body>
        </html>
        """.format(type.title(),actionn,naames,type.title(),actionn,naamef,actionn,request.user.username,
                   actionn,str(result))

        respmail = send_mail(
            subject=subjectt,
            message='Here is the message.',
            from_email='alert@healthforu.com',
            recipient_list = ['alert@healthforu.com'],
            fail_silently=False,
            html_message=html,
        )
        return respmail
    except Exception as e:
        print e, respmail
        return respmail

####################################################################
# Name - publish_interrupt_missing_data                            #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
def publish_interrupt_missing_data(request,type=None,name=None,id=None,reason = None):
    try:
        err_message = ''
        if type and name and id and reason:

            err_message =  'Record TYPE : '+ type +' with NAME : '+name+ ' and ID : '+str(id) + '>>not published<< REASON : '+ reason
            messages.error(request,err_message)

        else:
            messages.error(request, 'Unknown Error')
        if type.lower() == 'doctor':
            return HttpResponseRedirect(reverse('publisher-doctor-listing'))
        if type.lower() == 'organisation':
            return HttpResponseRedirect(reverse('publisher-organisation-listing'))
        if type.lower() == 'ambulance':
            return HttpResponseRedirect(reverse('publisher-ambulance-listing'))
        if type.lower() == 'bloodbank':
            return HttpResponseRedirect(reverse('publisher-bloodbank-listing'))
        if type.lower() == 'dietitian':
            return HttpResponseRedirect(reverse('publisher-dietitian-listing'))
        if type.lower() == 'disease':
            return HttpResponseRedirect(reverse('publisher-disease-listing'))
        if type.lower() ==  "enterpriseplan" or type.lower() == "lifeplan" or type.lower() == "homeplan":
            return HttpResponseRedirect(reverse('publisher-disease-listing'))
    except Exception as e:
        print
        '%s (%s)' % (e.message, type(e))
    return HttpResponse("Default mapping creation")

####################################################################
# Name - default_mapping                                                #
# Owner - jitendra dixit
# testing:                                             #
# Review by -                                                 #
#                                                                  #
####################################################################

@login_required(login_url='/')
@csrf_exempt
def default_mapping(request):
    try:
        elasticsearch_client.mapping_define()
    except Exception as e:
        print
        '%s (%s)' % (e.message, type(e))
    return HttpResponse("Default mapping creation")


####################################################################
# Name - default_mapping                                           #
# Owner - jitendra dixit
# testing:                                                         #
# Review by -                                                      #
#                                                                  #
####################################################################

@login_required(login_url='/')
@csrf_exempt
def demo_data_publish(request):
    try:
        data_publisher("master", [1])

        # doctor_obj = Doctor.objects.filter()
        # for doc in doctor_obj:
        #     doc_list = []
        #     doc_list.append(doc.id)
        #     data_publisher("doctor", doc_list)
        #
        #     organizationObjs = OrganisationName.objects.filter()
        #     for organization in organizationObjs:
        #         orgList = []
        #         orgList.append(organization.id)
        #         data_publisher("organization", orgList)

    except Exception as e:
        print
        '%s (%s)' % (e.message, type(e))
    return HttpResponse("data publish")


####################################################################
# Name - default_mapping                                           #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def publish_all_models(request):
    try:
        doctor_obj = Doctor.objects.filter(current_user_id=request.user.id,stage_id__gte=4)
        doc_list = []
        for doc in doctor_obj:
            doc_list.append(doc.id)
        data_publisher("doctor", doc_list)

        organizationObjs = OrganisationName.objects.filter(current_user_id=request.user.id,stage_id__gte=4)
        orgList = []
        for organization in organizationObjs:
            orgList.append(organization.id)
        data_publisher("organisation", orgList)

        bloodbankObjs = BloodBank.objects.filter(current_user_id=request.user.id,stage_id__gte=4)
        bbList = []
        for bbank in bloodbankObjs:
            bbList.append(bbank.id)
        data_publisher("bloodbank", bbList)

        labObjs = Labs.objects.filter(current_user_id=request.user.id, stage_id__gte=4)
        labList = []
        for lab in labObjs:
            labList.append(lab.id)
        data_publisher("lab", labList)

        phaObjs = MedicalPharmacyStore.objects.filter(current_user_id=request.user.id, stage_id__gte=4)
        pList = []
        for p in phaObjs:
            pList.append(p.id)
        data_publisher("pharmacy", pList)

        rehabObjs = RehabCenter.objects.filter(current_user_id=request.user.id, stage_id__gte=4)
        rehabList = []
        for rehab in rehabObjs:
            rehabList.append(rehab.id)
        data_publisher("rehabitation", rehabList)

    except Exception as e:
        print
        '%s (%s)' % (e.message, type(e))
    return HttpResponse("data publish")



####################################################################
# Name - default_mapping                                           #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def publish_all_models_two(request):
    try:
        disease_obj = Disease.objects.filter(current_user_id=request.user.id,stage_id__gte=4)
        disease_list = []
        for dis in disease_obj:
            disease_list.append(dis.id)
        data_publisher("disease", disease_list)

        SymptomsObjs = Symptoms.objects.filter(current_user_id=request.user.id,stage_id__gte=4)
        syList = []
        for sy in SymptomsObjs:
            syList.append(sy.id)
        data_publisher("symptom", syList)

        newsfeedObjs = NewsFeed.objects.filter(current_user_id=request.user.id,stage_id__gte=4)
        nList = []
        for news in newsfeedObjs:
            nList.append(news.id)
        data_publisher("newsfeed", nList)


    except Exception as e:
        print
        '%s (%s)' % (e.message, type(e))
    return HttpResponse("data publish")


####################################################################
# Name - data_publisher                                            #
# Owner - jitendra dixit
# testing:                                                         #
# Review by -                                                      #
#                                                                  #
####################################################################
def data_publisher(type, ids,request):
    response_result = True
    try:
        counter = 0
        if type == "doctor":
            succes_list = []
            fail_list = []
            for id in ids:
                doc_obj = Doctor.objects.get(id=id)
                if doc_obj.is_disable == False:
                    data = __doctor_data_creation(id)
                    response = elasticsearch_client.index_data("global", 'doctor', id, data)
                    if response:
                        succes_list.append(id)
                        doctor_obj = Doctor.objects.filter(id=id)
                        if doctor_obj:
                            doctor_obj.update(publish=True, stage=5)
                            #print(type + " is indexed: " + str(id))
                    else:
                        fail_list.append(id)
                        #print("Failed To " + type + ": " + str(id))
            my_send_mail(request, type, succes_list, fail_list, 'Doctor Published','Published')

        if type == "city":
            succes_list = []
            fail_list = []
            for id in ids:
                city_obj = City.objects.get(id=id)
                if city_obj.delete == False:
                    # data = __doctor_data_creation(id)
                    response_data_dict = {}
                    response_data_dict['id'] = city_obj.id
                    response_data_dict['name'] = city_obj.name
                    response_data_dict['city_code'] = city_obj.city_code
                    response_data_dict['state_id'] = city_obj.state.id
                    response_data_dict['state_name'] = city_obj.state.name
                    response = elasticsearch_client.index_data('master', 'city', id, response_data_dict)
                    # response = elasticsearch_client.index_data("msater", 'city', id, data)
                    if response:
                        succes_list.append(id)
                        city_obj = City.objects.filter(id=id)
                        if city_obj:
                            # city_obj.update(publish=True, stage=5)
                            print(type + " is indexed: " + str(id))
                    else:
                        fail_list.append(id)
                        #print("Failed To " + type + ": " + str(id))
            my_send_mail(request, type, succes_list, fail_list, 'City Master For Search, Published','Published')

        elif type == "livedoctor":
            succes_list = []
            fail_list = []
            for id in ids:
                doc_obj = Live_Doctor.objects.get(id=id)
                data = __live_doctor_data_creation(id)
                response = elasticsearch_client.index_data("global", 'doctor', id, data)
                if response:
                    succes_list.append(id)
                    doctor_obj = Live_Doctor.objects.filter(id=id)
                    if doctor_obj:
                        doctor_obj.update(publish=True, stage=5)
                        #print(type + " is indexed: " + str(id))
                else:
                    fail_list.append(id)
                    #print("Failed To "  + str(id))
            try:
                my_send_mail(request, type, succes_list, fail_list, 'Live Doctor(s) Published','Published')
            except:
                print 1
        elif type == "organisation":
            succes_list = []
            fail_list = []
            for id in ids:
                org_obj = OrganisationName.objects.get(id=id)
                if org_obj.is_disable == False:
                    data = __organisation_data_creation(id)
                    response = elasticsearch_client.index_data("global", "organisation", id, data)
                    if response:
                        succes_list.append(id)
                        organisation_obj = OrganisationName.objects.filter(id=id)
                        if organisation_obj:
                            organisation_obj.update(publish=True, stage=5)
                        #print(type + " is indexed: " + str(id))
                    else:
                        fail_list.append(id)
                        #print("Failed To " + type + ": " + str(id))
            try:
                my_send_mail(request, type, succes_list, fail_list, 'Hospital(s) Published','Published')
            except Exception as e:
                print e
        elif type == "newsfeed":
            succes_list = []
            fail_list = []
            for id in ids:
                news_obj = NewsFeed.objects.get(id=id)
                if news_obj.blocked_news == False :
                    data = _news_feed_data_creation(id)
                    response = elasticsearch_client.index_data('news', type, id, data)
                    if response:
                        succes_list.append(id)
                        newsFeed_obj = NewsFeed.objects.filter(id=id)
                        if newsFeed_obj:
                            newsFeed_obj.update(publish=True, stage=5)
                        print(type + " is indexed: " + str(id))
                    else:
                        fail_list.append(id)
                        print("Failed To " + type + ": " + str(id))
            my_send_mail(request, type, succes_list, fail_list, 'NewsFeed(s) Published','Published')
        elif type == "docsfeed":
            succes_list = []
            fail_list = []
            for id in ids:
                docs_obj = Doctorsfeed.objects.get(id=id)
                if docs_obj.blocked_news == False :
                    data = _docs_feed_data_creation(id)
                    response = elasticsearch_client.index_data('news', 'doctors_feed', id, data)
                    if response:
                        succes_list.append(id)
                        newsFeed_obj = NewsFeed.objects.filter(id=id)
                        if newsFeed_obj:
                            newsFeed_obj.update(publish=True, stage=5)
                        print(type + " is indexed: " + str(id))
                    else:
                        fail_list.append(id)
                        print("Failed To " + type + ": " + str(id))
            # my_send_mail(request, type, succes_list, fail_list, 'Doctors NewsFeed(s) Published','Published')
        elif type == "ambulance":
            succes_list = []
            fail_list = []
            for id in ids:
                amb_obj = Ambulance.objects.get(id=id)
                if amb_obj.is_disable == False :
                    data = _ambulance_data_creation(id)
                    response = elasticsearch_client.index_data('global', type, id, data)
                    if response:
                        succes_list.append(id)
                        ambulance_obj = Ambulance.objects.filter(id=id)
                        if ambulance_obj:
                            ambulance_obj.update(publish=True, stage=5)
                        #print(type + " is indexed: " + str(id))
                    else:
                        fail_list.append(id)
                        #print("Failed To " + type + ": " + str(id))
            my_send_mail(request,type, succes_list, fail_list,'Ambulance(s) Published','Published')



        elif type == "bloodbank":
            succes_list = []
            fail_list = []
            for id in ids:
                bb_obj = BloodBank.objects.get(id=id)
                if bb_obj.is_disable == False :
                    data = _bloodbank_data_creation(id)
                    response = elasticsearch_client.index_data('global', type, id, data)
                    if response:
                        succes_list.append(id)
                        bloodbank_obj = BloodBank.objects.filter(id=id)
                        if bloodbank_obj:
                            bloodbank_obj.update(publish=True, stage=5)
                        #print(type + " is indexed: " + str(id))
                    else:
                        fail_list.append(id)
                        #print("Failed To " + type + ": " + str(id))
            my_send_mail(request, type, succes_list, fail_list, 'BloodBank(s) Published', 'Published')

        elif type == "dietitian":
            succes_list = []
            fail_list = []
            for id in ids:
                diet_obj = Dietitian.objects.get(id=id)
                if diet_obj.is_disable == False :
                    data = _dietitian_data_creation(id)
                    response = elasticsearch_client.index_data('home', type, id, data)
                    if response:
                        succes_list.append(id)
                        dietitian_obj = Dietitian.objects.filter(id=id)
                        if dietitian_obj:
                            dietitian_obj.update(publish=True, stage=5)
                        #print(type + " is indexed: " + str(id))
                    else:
                        fail_list.append(id)
                        #print("Failed To " + type + ": " + str(id))
            my_send_mail(request, type, succes_list, fail_list, 'Dietitian(s) Published', 'Published')

        elif type == "disease":
            succes_list = []
            fail_list = []
            for id in ids:
                dis_obj = Disease.objects.get(id=id)
                if dis_obj.is_disable == False :
                    data = _disease_data_creation(id)
                    response = elasticsearch_client.index_data('home', type, id, data)
                    if response:
                        succes_list.append(id)
                        disease_obj = Disease.objects.filter(id=id)
                        if disease_obj:
                            disease_obj.update(publish=True, stage=5)
                        #print(type + " is indexed: " + str(id))
                    else:
                        fail_list.append(id)
                        #print("Failed To " + type + ": " + str(id))
            my_send_mail(request, type, succes_list, fail_list, 'Disease(s) Published', 'Published')

        elif type == "enterpriseplan" or type == "lifeplan" or type == "homeplan":
            succes_list = []
            fail_list = []
            for id in ids:
                pl_obj = ServicePlan.objects.get(id=id)
                if pl_obj.activation_status == True :
                    data = _plan_data_creation(id)
                    response = elasticsearch_client.index_data('home', 'services', id, data)
                    if response:
                        succes_list.append(id)
                        plan_obj = ServicePlan.objects.filter(id=id)
                        if plan_obj:
                            plan_obj.update(publish=True, stage=5)
                        #print(type + " is indexed: " + str(id))
                    else:
                        fail_list.append(id)
                        #print("Failed To " + type + ": " + str(id))
            my_send_mail(request, type, succes_list, fail_list, 'Plan(s) Published', 'Published')

        elif type == "serviceplan":
            succes_list = []
            fail_list = []
            for id in ids:
                pl_obj = PlanNew.objects.get(id=id)
                if pl_obj.activation_status == True :
                    data = _service_plan_data_creation(id)
                    response = elasticsearch_client.index_data('corporate', 'plan', id, data)
                    if response:
                        succes_list.append(id)
                        plan_obj = PlanNew.objects.filter(id=id)
                        if plan_obj:
                            plan_obj.update(publish=True, stage=5)
                    else:
                        fail_list.append(id)
            my_send_mail(request, type, succes_list, fail_list, 'Plan(s) Published', 'Published')

        elif type == "nurse_bureau":
            succes_list = []
            fail_list = []
            for id in ids:
                nbureau_obj = Nurse_Bureau.objects.get(id=id)
                if nbureau_obj.is_disable == False :
                    data = _nurse_bureau_data_creation(id)
                    response = elasticsearch_client.index_data('home', type, id, data)
                    if response:
                        succes_list.append(id)
                        nurse_bureau_obj = Nurse_Bureau.objects.filter(id=id)
                        if nurse_bureau_obj:
                            nurse_bureau_obj.update(publish=True, stage=5)
                        #print(type + " is indexed: " + str(id))
                    else:
                        fail_list.append(id)
                        #print("Failed To " + type + ": " + str(id))
            my_send_mail(request, type, succes_list, fail_list, 'Nurse Bureau(s) Published', 'Published')

        elif type == "pharmacy":
            succes_list = []
            fail_list = []
            for id in ids:
                p_obj = MedicalPharmacyStore.objects.get(id=id)
                if p_obj.is_disable == False :
                    data = _pharmacy_data_creation(id)
                    response = elasticsearch_client.index_data('global', type, id, data)
                    if response:
                        succes_list.append(id)
                        pharmacy_obj = MedicalPharmacyStore.objects.filter(id=id)
                        if pharmacy_obj:
                            pharmacy_obj.update(publish=True, stage=5)
                        #print(type + " is indexed: " + str(id))
                    else:
                        fail_list.append(id)
                        #print("Failed To " + type + ": " + str(id))
            my_send_mail(request, type, succes_list, fail_list, 'Medical Pharmacy(s) Published', 'Published')

        elif type == "lab":
            succes_list = []
            fail_list = []
            for id in ids:
                l_obj = Labs.objects.get(id=id)
                if l_obj.is_disable == False :
                    data = _lab_data_creation(id)
                    response = elasticsearch_client.index_data('global', type, id, data)
                    if response:
                        succes_list.append(id)
                        lab_obj = Labs.objects.filter(id=id)
                        if lab_obj:
                            lab_obj.update(publish=True, stage=5)
                        #print(type + " is indexed: " + str(id))
                    else:
                        fail_list.append(id)
                        #print("Failed To " + type + ": " + str(id))
            my_send_mail(request, type, succes_list, fail_list, 'Lab(s) Published', 'Published')

        elif type == "rehabitation":
            succes_list = []
            fail_list = []
            for id in ids:
                reh_obj = RehabCenter.objects.get(id=id)
                if reh_obj.is_disable == False :
                    data = _rehab_data_creation(id)
                    response = elasticsearch_client.index_data('home', type, id, data)
                    if response:
                        succes_list.append(id)
                        rehab_obj = RehabCenter.objects.filter(id=id)
                        if rehab_obj:
                            rehab_obj.update(publish=True, stage=5)
                        #print(type + " is indexed: " + str(id))
                    else:
                        fail_list.append(id)
                        #print("Failed To " + type + ": " + str(id))
            my_send_mail(request, type, succes_list, fail_list, 'Rehab(s) Published', 'Published')

        elif type == "symptom":
            succes_list = []
            fail_list = []
            for id in ids:
                sym_obj = Symptoms.objects.get(id=id)
                if  sym_obj.is_disable == False :
                    data = _symptoms_data_creation(id)
                    response = elasticsearch_client.index_data('home', type, id, data)
                    if response:
                        succes_list.append(id)
                        symptoms_obj = Symptoms.objects.filter(id=id)
                        if symptoms_obj:
                            symptoms_obj.update(publish=True, stage=5)
                        #print(type + " is indexed: " + str(id))
                    else:
                        fail_list.append(id)
                        #print("Failed To " + type + ": " + str(id))
            my_send_mail(request, type, succes_list, fail_list, 'Symptom(s) Published', 'Published')

        # elif type == "therapist":
        #     for id in ids:
        #         data = _therapist_data_creation(id)
        #         response = elasticsearch_client.index_data('home', type, id, data)
        #         if response:
        #             therapist_obj = Therapist.objects.filter(id=id)
        #             if therapist_obj:
        #                 therapist_obj.update(publish=True, stage=5)
        #             print(type + " is indexed: " + str(id))
        #         else:
        #             print("Failed To " + type + ": " + str(id))

        elif type == "master":
            # ************************ All master publish in******************* #
            data = {}

            Org_types = Organisation_types.objects.filter(delete=False)
            for Org in Org_types:
                data = {}
                data['id'] = Org.id
                data['name'] = Org.type_name
                data['name'].strip()
                response = elasticsearch_client.index_data('globalmaster', 'organisationtypes', Org.id, data)
                response = elasticsearch_client.index_data('master', 'organisationtypes', Org.id, data)
                if response:
                    print(type + " is indexed: " + str(data['id']))
                else:
                    print("Failed To " + type + ": " + str(data['id']))

            lab_types = Lab_type_master.objects.filter(delete=False)
            for typela in lab_types:
                data = {}
                data['id'] = typela.id
                data['name'] = typela.name
                data['name'].strip()
                response = elasticsearch_client.index_data('master', 'labtypes', typela.id, data)
                if response:
                    print(type + " is indexed: " + str(data['id']))
                else:
                    print("Failed To " + type + ": " + str(data['id']))

            lab_departments = Lab_department_master.objects.filter(delete=False)
            for dep in lab_departments:
                data = {}
                data['id'] = dep.id
                data['name'] = dep.name
                data['name'].strip()
                response = elasticsearch_client.index_data('globalmaster', 'labdepartments', dep.id, data)
                print "A)globalmaster : ",response
                response = elasticsearch_client.index_data('master', 'labdepartments', dep.id, data)
                print "B)master : ", response
                if response:
                    print(type + " is indexed: " + str(data['id']))
                else:
                    print("Failed To " + type + ": " + str(data['id']))

            department_objs = Department.objects.filter(delete=False)
            for department in department_objs:
                data = {}
                data['id'] = department.id
                data['name'] = department.name
                data['name'].strip()
                response = elasticsearch_client.index_data('globalmaster', 'department', department.id, data)
                response = elasticsearch_client.index_data('master', 'department', department.id, data)
                if response:
                    print(type + " is indexed: " + str(data['id']))
                else:
                    print("Failed To " + type + ": " + str(data['id']))

            Category_obj = Category.objects.filter(delete=False)
            for category in Category_obj:
                data = {}
                data['id'] = category.id
                data['name'] = category.name
                data['name'].strip()
                response = elasticsearch_client.index_data('globalmaster', 'category', category.id, data)
                response = elasticsearch_client.index_data('master', 'category', category.id, data)
                if response:
                    print(type + " is indexed: " + str(data['id']))
                else:
                    print("Failed To " + type + ": " + str(data['id']))

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
                    print(type + " is indexed: " + str(data['id']))
                else:
                    print("Failed To " + type + ": " + str(data['id']))

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
                    print(type + " is indexed: " + str(data['id']))
                else:
                    print("Failed To " + type + ": " + str(data['id']))

            Country_obj = Country.objects.filter(delete=False)
            for country in Country_obj:
                data = {}
                data['id'] = country.id
                data['name'] = country.name
                data['name'].strip()
                response = elasticsearch_client.index_data('master', 'country', country.id, data)
                if response:
                    print(type + " is indexed: " + str(data['id']))
                else:
                    print("Failed To " + type + ": " + str(data['id']))

            State_obj = State.objects.filter(delete=False)
            for state in State_obj:
                data = {}
                data['id'] = state.id
                data['name'] = state.name
                data['name'].strip()
                data['country_id'] = state.country_id
                response = elasticsearch_client.index_data('master', 'state', state.id, data)
                if response:
                    print(type + " is indexed: " + str(data['id']))
                else:
                    print("Failed To " + type + ": " + str(data['id']))

            City_obj = City.objects.filter(delete=False)
            for city in City_obj:
                data = {}
                data['id'] = city.id
                data['name'] = city.name
                data['name'].strip()
                data['state_id'] = city.state_id
                response = elasticsearch_client.index_data('master', 'city', city.id, data)
                if response:
                    print(type + " is indexed: " + str(data['id']))
                else:
                    print("Failed To " + type + ": " + str(data['id']))

            Lab_accreditation_body_master_obj = Lab_accreditation_body_master.objects.filter(delete=False)
            for lab_acc in Lab_accreditation_body_master_obj:
                data = {}
                data['id'] = lab_acc.id
                data['name'] = lab_acc.name
                data['name'].strip()
                data['address'] = lab_acc.address
                data['address'].strip()
                data['pincode'] = lab_acc.pincode
                data['pincode'].strip()
                data['telephone'] = lab_acc.telephone
                data['telephone'].strip()

                response = elasticsearch_client.index_data('globalmaster', 'labaccreditation', lab_acc.id, data)
                response = elasticsearch_client.index_data('master', 'labaccreditation', lab_acc.id, data)
                if response:
                    print(type + " is indexed: " + str(data['id']))
                else:
                    print("Failed To " + type + ": " + str(data['id']))

            Lab_services_master_obj = Lab_services_master.objects.filter(delete=False)
            for lab_ser in Lab_services_master_obj:
                data = {}
                data['id'] = lab_ser.id
                data['name'] = lab_ser.name
                data['name'].strip()

                response = elasticsearch_client.index_data('globalmaster', 'labservices', lab_ser.id, data)
                response = elasticsearch_client.index_data('master', 'labservices', lab_ser.id, data)
                if response:
                    print(type + " is indexed: " + str(data['id']))
                else:
                    print("Failed To " + type + ": " + str(data['id']))

            Lab_test_master_obj = Lab_test_master.objects.filter(delete=False)
            for lab_t in Lab_test_master_obj:
                data = {}
                data['id'] = lab_t.id
                data['name'] = lab_t.name
                data['name'].strip()

                response = elasticsearch_client.index_data('globalmaster', 'labtest', lab_t.id, data)
                response = elasticsearch_client.index_data('master', 'labtest', lab_t.id, data)
                if response:
                    print(type + " is indexed: " + str(data['id']))
                else:
                    print("Failed To " + type + ": " + str(data['id']))

            MedicalPharmacyStoreType_obj = MedicalPharmacyStoreType.objects.filter(delete=False)
            for mpty in MedicalPharmacyStoreType_obj:
                data = {}
                data['id'] = mpty.id
                data['name'] = mpty.name
                data['name'].strip()

                response = elasticsearch_client.index_data('master', 'pharmacytype', mpty.id, data)
                if response:
                    print(type + " is indexed: " + str(data['id']))
                else:
                    print("Failed To " + type + ": " + str(data['id']))

            MedicalPharmacyStoreServices_obj = MedicalPharmacyStoreServices.objects.filter(delete=False)
            for mpser in MedicalPharmacyStoreServices_obj:
                data = {}
                data['id'] = mpser.id
                data['name'] = mpser.name
                data['name'].strip()

                response = elasticsearch_client.index_data('master', 'pharmacyServices', mpser.id, data)
                if response:
                    print(type + " is indexed: " + str(data['id']))
                else:
                    print("Failed To " + type + ": " + str(data['id']))

            # lab_branches_all = Lab_branches.objects.all()
            # for b in lab_branches_all:
            #     data = {}
            #     save_id = 0
            #     data = b.branches
            #     save_id = int(data['lab_id'])
            #     del data['lab_id']
            #     data.update({'id': save_id})
            #
            #     response = elasticsearch_client.index_data('master', 'lab_branches', b.id, data)
            #     if response:
            #         print(type + " is indexed: " + str(data['id']))
            #     else:
            #         print("Failed To " + type + ": " + str(data['id']))

            # org_branches_all = Organisation_branches.objects.all()
            # for b in org_branches_all:
            #     data = {}
            #     save_id = 0
            #     data = b.branches
            #     save_id = int(data['organisation_id'])
            #     del data['organisation_id']
            #     data.update({'id': save_id})
            #
            #     response = elasticsearch_client.index_data('master', 'organisation_branches', b.id, data)
            #     if response:
            #         print(type + " is indexed: " + str(data['id']))
            #     else:
            #         print("Failed To " + type + ": " + str(data['id']))
            #
            Locality_obj = Locality.objects.filter(delete=False)
            for locality in Locality_obj:
                data = {}
                data['id'] = locality.id
                data['name'] = locality.name
                data['name'].strip()
                data['city_id'] = locality.city_id
                response = elasticsearch_client.index_data('master', 'locality', locality.id, data)
                if response:
                    print(type + " is indexed: " + str(data['id']))
                else:
                    print("Failed To " + type + ": " + str(data['id']))

            facility_objs = Facility.objects.filter(delete=False)
            for facility in facility_objs:
                data = {}
                data['id'] = facility.id
                data['name'] = facility.name
                data['name'].strip()
                response = elasticsearch_client.index_data('globalmaster', 'facility', facility.id, data)
                response = elasticsearch_client.index_data('master', 'facility', facility.id, data)
                if response:
                    print(type + " is indexed: " + str(data['id']))
                else:
                    print("Failed To " + type + " : " + str(data['id']))

    except Exception as e:
        response_result = False
        print e
        '%s (%s)' % (e.message, type(e))
    return response_result


####################################################################
# Name - data_un_publish                                           #
# Owner - jitendra dixit
# testing:                                                         #
# Review by -                                                      #
#                                                                  #
####################################################################

un_publish_doctor = elasticsearch_client.base_url + 'doctor/document/'
un_publish_organisation = elasticsearch_client.base_url + 'organisation/document/'
un_publish_news = elasticsearch_client.base_url + 'news_feed/document/'


def data_un_publisher(type_data, ids,request):
    response_result = True
    try:
        if type_data == "doctor":
            succes_list = []
            fail_list = []
            for id in ids:
                # response = requests.delete(un_publish_doctor + str(id))
                response = elasticsearch_client.delete_document('global', type_data, id)
                if response:
                    succes_list.append(id)
                    doctor_obj = Doctor.objects.filter(id=id)
                    if doctor_obj:
                        doctor_obj.update(publish=False, stage=4)
                    # print(response.text)
                else:
                    fail_list.append(id)
            my_send_mail(request, type_data, succes_list, fail_list, 'Doctor(s) Un-Published', 'Un-Published')

        if type_data == "livedoctor":
            succes_list = []
            fail_list = []
            for id in ids:
                # response = requests.delete(un_publish_doctor + str(id))
                response = elasticsearch_client.delete_document('global', "doctor", id)
                if response:
                    succes_list.append(id)
                    doctor_obj = Live_Doctor.objects.filter(id=id)
                    if doctor_obj:
                        doctor_obj.update(publish=False, stage=4)
                else:
                    fail_list.append(id)
            my_send_mail(request, type_data, succes_list, fail_list, 'Live Doctor(s) Un-Published', 'Un-Published')

        elif type_data == "organisation":
            succes_list = []
            fail_list = []
            for id in ids:
                # response = requests.delete(un_publish_organisation + str(id))
                response = elasticsearch_client.delete_document('global', type_data, id)

                if response:
                    succes_list.append(id)
                    organisation_obj = OrganisationName.objects.filter(id=id)
                    if organisation_obj:
                        organisation_obj.update(publish=False, stage=4)
                        # print(response.text)
                else:
                    fail_list.append(id)
            my_send_mail(request, type_data, succes_list, fail_list, 'Hospital(s) Un-Published', 'Un-Published')

        elif type_data == "newsfeed":
            succes_list = []
            fail_list = []
            for id in ids:
                response = elasticsearch_client.delete_document('news', type_data, id)
                if response:
                    succes_list.append(id)
                    news_feed_obj = NewsFeed.objects.filter(id=id)
                    if news_feed_obj:
                        news_feed_obj.update(publish=False, stage=4)
                else:
                    fail_list.append(id)
                    response_result = False
            my_send_mail(request, type_data, succes_list, fail_list, 'NewsFeed(s) Un-Published', 'Un-Published')

        elif type_data == "docsfeed":
            succes_list = []
            fail_list = []
            for id in ids:
                response = elasticsearch_client.delete_document('news', 'doctors_feed', id)
                if response:
                    succes_list.append(id)
                    feed_obj = Doctorsfeed.objects.filter(id=id)
                    if feed_obj:
                        feed_obj.update(publish=False, stage=4)
                else:
                    fail_list.append(id)
                    response_result = False
            my_send_mail(request, type_data, succes_list, fail_list, 'DoctorsewsFeed(s) Un-Published', 'Un-Published')

        elif type_data == "lab":
            succes_list = []
            fail_list = []
            for id in ids:
                response = elasticsearch_client.delete_document('global', type_data, id)
                if response:
                    succes_list.append(id)
                    news_feed_obj = Labs.objects.filter(id=id)
                    if news_feed_obj:
                        news_feed_obj.update(publish=False, stage=4)
                else:
                    fail_list.append(id)
                    response_result = False
            my_send_mail(request, type_data, succes_list, fail_list, 'Lab(s) Un-Published', 'Un-Published')

        elif type_data == "pharmacy":
            succes_list = []
            fail_list = []
            for id in ids:
                response = elasticsearch_client.delete_document('global', type_data, id)
                if response:
                    succes_list.append(id)
                    news_feed_obj = MedicalPharmacyStore.objects.filter(id=id)
                    if news_feed_obj:
                        news_feed_obj.update(publish=False, stage=4)
                else:
                    fail_list.append(id)
                    response_result = False
            my_send_mail(request, type_data, succes_list, fail_list, 'Pharmacy(s) Un-Published', 'Un-Published')

        elif type_data == "bloodbank":
            succes_list = []
            fail_list = []
            for id in ids:
                response = elasticsearch_client.delete_document('global', type_data, id)
                if response:
                    succes_list.append(id)
                    news_feed_obj = BloodBank.objects.filter(id=id)
                    if news_feed_obj:
                        news_feed_obj.update(publish=False, stage=4)
                else:
                    fail_list.append(id)
                    response_result = False
            my_send_mail(request, type_data, succes_list, fail_list, 'BloodBank(s) Un-Published', 'Un-Published')

        elif type_data == "ambulance":
            succes_list = []
            fail_list = []
            for id in ids:
                response = elasticsearch_client.delete_document('global', type_data, id)
                if response:
                    succes_list.append(id)
                    news_feed_obj = Ambulance.objects.filter(id=id)
                    if news_feed_obj:
                        news_feed_obj.update(publish=False, stage=4)
                else:
                    fail_list.append(id)
                    response_result = False
            my_send_mail(request, type_data, succes_list, fail_list, 'Ambulance(s) Un-Published', 'Un-Published')

        elif type_data == "symptom":
            succes_list = []
            fail_list = []
            for id in ids:
                response = elasticsearch_client.delete_document('home', type_data, id)
                if response:
                    succes_list.append(id)
                    news_feed_obj = Symptoms.objects.filter(id=id)
                    if news_feed_obj:
                        news_feed_obj.update(publish=False, stage=4)
                else:
                    fail_list.append(id)
                    response_result = False
            my_send_mail(request, type_data, succes_list, fail_list, 'Symptom(s) Un-Published', 'Un-Published')

        elif type_data == "disease":
            succes_list = []
            fail_list = []
            for id in ids:
                response = elasticsearch_client.delete_document('home', type_data, id)
                if response:
                    succes_list.append(id)
                    news_feed_obj = Disease.objects.filter(id=id)
                    if news_feed_obj:
                        news_feed_obj.update(publish=False, stage=4)
                else:
                    fail_list.append(id)
                    response_result = False
            my_send_mail(request, type_data, succes_list, fail_list, 'Disease(s) Un-Published', 'Un-Published')

        elif type_data == "rehabitation":
            succes_list = []
            fail_list = []
            for id in ids:
                response = elasticsearch_client.delete_document('home', type_data, id)
                if response:
                    succes_list.append(id)
                    news_feed_obj = RehabCenter.objects.filter(id=id)
                    if news_feed_obj:
                        news_feed_obj.update(publish=False, stage=4)
                else:
                    fail_list.append(id)
                    response_result = False
            my_send_mail(request, type_data, succes_list, fail_list, 'Rehab(s) Un-Published', 'Un-Published')

        elif type_data == "enterpriseplan" or type_data == "lifeplan" or type_data == "homeplan":
            succes_list = []
            fail_list = []
            for id in ids:
                response = elasticsearch_client.delete_document('home', 'services', id)
                if response:
                    succes_list.append(id)
                    service_plan_obj = ServicePlan.objects.filter(id=id)
                    if service_plan_obj:
                        service_plan_obj.update(publish=False, stage=4)
                else:
                    fail_list.append(id)
                    response_result = False
            my_send_mail(request, type_data, succes_list, fail_list, 'Plan(s) Un-Published', 'Un-Published')

        elif type_data == "dietitian":
            succes_list = []
            fail_list = []
            for id in ids:
                response = elasticsearch_client.delete_document('home', type_data, id)
                if response:
                    succes_list.append(id)
                    news_feed_obj = Dietitian.objects.filter(id=id)
                    if news_feed_obj:
                        news_feed_obj.update(publish=False, stage=4)
                else:
                    fail_list.append(id)
                    response_result = False
            my_send_mail(request, type_data, succes_list, fail_list, 'Dietitian(s) Un-Published', 'Un-Published')

        elif type_data == "nurse_bureau":
            succes_list = []
            fail_list = []
            for id in ids:
                response = elasticsearch_client.delete_document('home', type_data, id)
                if response:
                    succes_list.append(id)
                    news_feed_obj = Nurse_Bureau.objects.filter(id=id)
                    if news_feed_obj:
                        news_feed_obj.update(publish=False, stage=4)
                else:
                    fail_list.append(id)
                    response_result = False
            my_send_mail(request, type_data, succes_list, fail_list, 'Nurse_Bureau(s) Un-Published', 'Un-Published')

        elif type_data == "serviceplan":
            succes_list = []
            fail_list = []
            for id in ids:
                response = elasticsearch_client.delete_document('home', 'plan', id)
                if response:
                    succes_list.append(id)
                    service_plan_obj = PlanNew.objects.get(id=id)
                    if service_plan_obj:
                        service_plan_obj.publish = False
                        service_plan_obj.stage_id = 4
                        service_plan_obj.save()
                else:
                    fail_list.append(id)
                    response_result = False
            my_send_mail(request, type_data, succes_list, fail_list, 'Plan(s) Un-Published', 'Un-Published')


    except Exception as e:
        response_result = False
        print e
        '%s (%s)' % (e.message, type(e))
    return response_result


####################################################################
# Name - __doctor_data_creation                                                #
# Owner - jitendra dixit
# testing:                                             #
# Review by -                                                 #
#                                                                  #
####################################################################


def __doctor_data_creation(id):
    response_data_dict = {}
    try:
        Doctor_obj = Doctor.objects.get(id=id)
        if Doctor_obj:
            response_data_dict['name'] = Doctor_obj.name
            emergency_data = {}
            if Doctor_obj.is_emergency != None :
                response_data_dict['is_emergency'] = Doctor_obj.is_emergency
            else:
                response_data_dict['is_emergency'] = False

            if Doctor_obj.is_emergency == True :
                emergency_data['fee'] = 0
                emergency_data['efee'] = Doctor_obj.emergency_fee
                #emergency_data['is_emergency'] = Doctor_obj.is_emergency
                if Doctor_obj.country != None:
                    emergency_data['country_id'] =  int(Doctor_obj.country_id)
                    emergency_data['country_name'] = Doctor_obj.country.name
                else:
                    emergency_data['country_id'] = 0
                    emergency_data['country_name'] = ''
                if Doctor_obj.state != None:
                    emergency_data['state_id'] = int(Doctor_obj.state_id)
                    emergency_data['state_name'] = Doctor_obj.state.name
                else:
                    emergency_data['state_id'] = 0
                    emergency_data['state_name'] = ''
                if Doctor_obj.city != None:
                    emergency_data['city_id'] = int(Doctor_obj.city_id)
                    emergency_data['city_name'] = Doctor_obj.city.name
                else:
                    emergency_data['city_id'] = 0
                    emergency_data['city_name'] = ''
                LLIST =[]
                locality_list = []
                if Doctor_obj.localities and Doctor_obj.localities != '':
                     LLIST = Doctor_obj.localities.split(',')
                     for i in LLIST:
                         loc = Locality.objects.get(id=int(i))
                         locality_list.append({'id':int(i),'name':loc.name})

                else:
                    locality_list = []
                emergency_data['locality_list'] = locality_list

            else:
                emergency_data['fee'] = 0
                emergency_data['efee'] = ''
                #emergency_data['is_emergency'] = False
                emergency_data['country_id'] = 0
                emergency_data['country_name'] = ''
                emergency_data['state_id'] = 0
                emergency_data['state_name'] = ''
                emergency_data['city_id'] = 0
                emergency_data['city_name'] = ''
                emergency_data['locality_list'] = []

            response_data_dict['emergency_data'] = emergency_data

            if Doctor_obj.audio != None :
                response_data_dict['audio'] = Doctor_obj.audio
            else:
                response_data_dict['audio'] = False

            if Doctor_obj.video != None :
                response_data_dict['video'] = Doctor_obj.video
            else:
                response_data_dict['video'] = False

            if Doctor_obj.chat != None :
                response_data_dict['chat'] = Doctor_obj.chat
            else:
                response_data_dict['chat'] = False

            if Doctor_obj.talk_to_doc != None :
                response_data_dict['talk_to_doc'] = Doctor_obj.talk_to_doc
            else:
                response_data_dict['talk_to_doc'] = False

            if Doctor_obj.talk_to_doc == True:
                response_data_dict['talk_fee'] = Doctor_obj.talk_fee
            else:
                response_data_dict['talk_fee'] = ''

            # response_data_dict['dob']= str(Doctor_obj.dob)
            response_data_dict['doctor_experience_year'] = Doctor_obj.doctor_experience_year
            if response_data_dict['doctor_experience_year']:
                response_data_dict['doctor_experience_year'].strip()
            response_data_dict['unique_id'] = Doctor_obj.id

            response_data_dict['image_url'] = Doctor_obj.profile_photo # Doctor_obj.image_url
            # if response_data_dict['image_url']:
            #     response_data_dict['image_url'].strip()

            response_data_dict['zone'] = Doctor_obj.zone.name
            if response_data_dict['zone']:
                response_data_dict['zone'].strip()

            response_data_dict['zone_location'] = Doctor_obj.zone_location.name
            if response_data_dict['zone_location']:
                response_data_dict['zone_location'].strip()

            response_data_dict['category_id'] = Doctor_obj.category_id

            response_data_dict['category'] = Doctor_obj.category.name
            if response_data_dict['category']:
                response_data_dict['category'].strip()

            response_data_dict['mobile_no'] = Doctor_obj.mobile_no
            if response_data_dict['mobile_no']:
                response_data_dict['mobile_no'].strip()

            response_data_dict['phone'] = Doctor_obj.phone
            if response_data_dict['phone']:
                response_data_dict['phone'].strip()

            if  Doctor_obj.skype_id != None:
                response_data_dict['skype_id'] = Doctor_obj.skype_id
            else:
                response_data_dict['skype_id'] = ''
            if response_data_dict['skype_id']:
                response_data_dict['skype_id'].strip()

            response_data_dict['email'] = Doctor_obj.email
            if response_data_dict['email']:
                response_data_dict['email'].strip()

            response_data_dict['registration_data'] = Doctor_obj.registration_data
            if response_data_dict['registration_data']:
                response_data_dict['registration_data'].strip()

            # Added by Manoj
            if Doctor_obj.registration_data:
                response_data_dict['mci'] = str(Doctor_obj.registration_data).split(None, 1)[0]

            response_data_dict['secondary_email'] = Doctor_obj.secondary_email
            if response_data_dict['secondary_email']:
                response_data_dict['secondary_email'].strip()

            response_data_dict['qualification_data'] = Doctor_obj.qualification_data
            if response_data_dict['qualification_data']:
                response_data_dict['qualification_data'].strip()

            response_data_dict['male_doctor'] = str(Doctor_obj.male_doctor)
            if response_data_dict['male_doctor']:
                response_data_dict['male_doctor'].strip()

            response_data_dict['female_doctor'] = str(Doctor_obj.female_doctor)
            if response_data_dict['female_doctor']:
                response_data_dict['female_doctor'].strip()


            # ****  FOR OLD MASTERS  START******************
            # #******************************* Get Specilaity *************************#
            # if Doctor_obj.speciality:
            #     speciality_get_list = Doctor_obj.speciality.split(',')
            #     speciality_list = []
            #     for speciality in speciality_get_list:
            #         speciality_dict = {}
            #         if speciality != '':
            #             Speciality_obj = Speciality.objects.get(id=int(speciality))
            #             if Speciality_obj:
            #                 speciality_dict['id'] = Speciality_obj.id
            #                 if Speciality_obj.name:
            #                     speciality_dict['name'] = Speciality_obj.name.strip()
            #                 else:
            #                     speciality_dict['name'] = ""
            #                 speciality_list.append(speciality_dict)
            #     response_data_dict['speciality'] = speciality_list
            # else:
            #     response_data_dict['speciality'] = []
            #
            #     # #***************************** Create a doctor service **************************#
            # if Doctor_obj.service_offered:
            #     service_get_list = Doctor_obj.service_offered.split(',')
            #     service_list = []
            #     for service in service_get_list:
            #         service_dict = {}
            #         if service != '':
            #             Service_obj = Service_Offred.objects.get(id=int(service))
            #             if Service_obj:
            #                 service_dict['id'] = Service_obj.id
            #                 if Service_obj.name:
            #                     service_dict['name'] = Service_obj.name.strip()
            #                 else:
            #                     service_dict['name'] = ""
            #                 service_list.append(service_dict)
            #     response_data_dict['service'] = service_list
            # else:
            #     response_data_dict['service'] = []
            # ****  FOR OLD MASTERS  END******************
            #*********************************************

            # ****  FOR NEW MASTERS  START******************
            # #******************************* Get Specilaity *************************#

            if Doctor_obj.new_speciality_final != '' and Doctor_obj.new_speciality_final != None:
                speciality_get_list = Doctor_obj.new_speciality_final.split(',')
                speciality_list = []
                for speciality in speciality_get_list:
                    speciality_dict = {}
                    if speciality != '':
                        Speciality_obj = Doctor_Speciality_New.objects.get(id=int(speciality))
                        if Speciality_obj:
                            speciality_dict['id'] = Speciality_obj.id
                            if Speciality_obj.name:
                                speciality_dict['name'] = Speciality_obj.name.strip()
                            else:
                                speciality_dict['name'] = ""
                            speciality_list.append(speciality_dict)
                response_data_dict['speciality'] = speciality_list
            else:
                response_data_dict['speciality'] = []

            #***************************** Create a doctor service **************************#

            if Doctor_obj.new_service_offered_final != '' and Doctor_obj.new_service_offered_final != None:
                service_get_list = Doctor_obj.new_service_offered_final.split(',')
                service_list = []
                for service in service_get_list:
                    service_dict = {}
                    if service != '':
                        Service_obj = Doctor_ServiceOffered_New.objects.get(id=int(service))
                        if Service_obj:
                            service_dict['id'] = Service_obj.id
                            if Service_obj.name:
                                service_dict['name'] = Service_obj.name.strip()
                            else:
                                service_dict['name'] = ""
                            service_list.append(service_dict)
                response_data_dict['service'] = service_list
            else:
                response_data_dict['service'] = []

            # ****  FOR NEW MASTERS  END******************
            #*********************************************

            # #******************************* Doctor membership *********************#
            Membership_list = []
            RewardRecognisation_list = []
            Doctor_Education_list = []
            Doctor_Experience_list = []
            Membership_obj = Membership.objects.values_list('name', flat=True).filter(doctor_id=Doctor_obj.id)
            for membership in Membership_obj:
                Membership_list.append(membership)
            response_data_dict['membership'] = Membership_list

            # #*************************************** Reward and recognisation ********#
            RewardRecognisation_obj = RewardRecognisation.objects.values_list('reward_data', flat=True).filter(
                doctor_id=Doctor_obj.id)
            for reward in RewardRecognisation_obj:
                RewardRecognisation_list.append(reward)
            response_data_dict['rewardrecognisation'] = RewardRecognisation_list

            # #************************** Education ***************************#
            Doctor_Education_obj = Doctor_Education.objects.values_list('education_data', flat=True).filter(
                doctor_id=Doctor_obj.id)
            for doctor_edu in Doctor_Education_obj:
                Doctor_Education_list.append(doctor_edu)
            response_data_dict['education'] = Doctor_Education_list

            # #******************************** Experience**************************** #
            Doctor_Experience_obj = Doctor_Experience.objects.values_list('experience_data', flat=True).filter(
                doctor_id=Doctor_obj.id)
            for doctor_exp in Doctor_Experience_obj:
                Doctor_Experience_list.append(doctor_exp)
            response_data_dict['experience'] = Doctor_Experience_list

            # ******************************** Attached Organisation *************************#
            AttachWithDoctor_obj = AttachWithDoctor.objects.filter(doctor_id=Doctor_obj.id)
            attach_org_list = []
            for attach_with_doctor in AttachWithDoctor_obj:
                attach_org_dict = {}
                attach_org_dict['consultancy_fee'] = 0
                try:
                    if attach_with_doctor.consultancy_fee:
                        attach_org_dict['consultancy_fee'] = int(attach_with_doctor.consultancy_fee)
                except:
                    attach_org_dict['consultancy_fee'] = 0
                attach_org_dict['did'] = attach_with_doctor.did
                attach_org_dict['extension'] = attach_with_doctor.extension
                attach_org_dict['email_attach'] = (attach_with_doctor.email_attach)
                attach_org_dict['telephone_attach'] = (attach_with_doctor.telephone_attach)
                attach_org_dict['name'] = attach_with_doctor.organisation.name
                attach_org_dict['is_clinic'] = attach_with_doctor.organisation.is_clinic
                attach_org_dict['is_hospital'] = attach_with_doctor.organisation.is_hospital
                attach_org_dict['street'] = attach_with_doctor.organisation.street
                attach_org_dict['organisation_id'] = attach_with_doctor.organisation.id
                attach_org_dict['locality_id'] = attach_with_doctor.organisation.locality.id
                attach_org_dict['locality_name'] = attach_with_doctor.organisation.locality.name
                attach_org_dict['city_id'] = attach_with_doctor.organisation.city.id
                attach_org_dict['city_name'] = attach_with_doctor.organisation.city.name
                attach_org_dict['state_id'] = attach_with_doctor.organisation.state.id
                attach_org_dict['state_name'] = attach_with_doctor.organisation.state.name
                attach_org_dict['country_id'] = attach_with_doctor.organisation.country.id
                attach_org_dict['country_name'] = attach_with_doctor.organisation.country.name
                attach_org_dict['phone'] = attach_with_doctor.organisation.phone
                attach_org_dict['mobile_no'] = attach_with_doctor.organisation.mobile_no
                attach_org_dict['fax'] = attach_with_doctor.organisation.fax
                attach_org_dict['emergency_no'] = attach_with_doctor.organisation.emergency_no
                attach_org_dict['email'] = attach_with_doctor.organisation.email
                attach_org_dict['pincode'] = attach_with_doctor.organisation.pincode

                attach_org_dict['location'] = {
                    "lat": 0,
                    "long": 0
                }
                if attach_with_doctor.organisation.latitude and attach_with_doctor.organisation.longitude:
                    attach_org_dict['location'] = {
                        "lat": float(attach_with_doctor.organisation.latitude),
                        "long": float(attach_with_doctor.organisation.longitude)
                    }

                # ***************************** schedule in organisation *************#
                Schedule_obj = Schedule.objects.get(doctor_id=Doctor_obj.id,
                                                    organisation_id=attach_with_doctor.organisation_id)
                if Schedule_obj:
                    if Schedule_obj.by_appointment == False:
                        try:
                            schedule_data = Schedule_obj.schedule_data
                            attach_org_dict['timing'] = convert_time_array(schedule_data)
                            attach_org_dict['timing_str'] = convert_time_str_array(schedule_data)
                            attach_org_dict['time_object'] = Schedule_obj.schedule_data
                            attach_org_dict['by_appointment'] = False

                        except:
                            attach_org_dict['timing'] = []
                            attach_org_dict['timing_str'] = []
                            attach_org_dict['time_object'] = []
                            attach_org_dict['by_appointment'] = False
                    else:
                        attach_org_dict['timing'] = []
                        attach_org_dict['timing_str'] = []
                        attach_org_dict['time_object'] = []
                        attach_org_dict['by_appointment'] = True
                else:
                    attach_org_dict['timing'] = []
                    attach_org_dict['timing_str'] = []
                    attach_org_dict['time_object'] = []
                    attach_org_dict['by_appointment'] = False

                attach_org_list.append(attach_org_dict)
            response_data_dict['attach_organisation'] = attach_org_list
            from .views import hostname, port
            hostport = hostname + port
            gallery_images = []
            gallery_obj_list = Doctor_Imagegallery.objects.filter(doctor_id=Doctor_obj.id, publish=True)
            if list(gallery_obj_list) != []:
                for imobj in gallery_obj_list:
                    tempurl = ''
                    tempurl = tempurl + hostport + imobj.name.strip()
                    gallery_images.append(tempurl)
            response_data_dict['gallery_images'] = gallery_images
            response_data_dict['activationStatus'] = False

            response_data_dict['associated_diseases'] = []
            if Doctor_obj.associated_diseases and Doctor_obj.associated_diseases !='' and Doctor_obj.associated_diseases != []:
                temp2 = []
                temp1 = []
                temp1 = Doctor_obj.associated_diseases.split(',')
                for i in temp1:
                    if i!=''  and i != ' ':
                        dis_obj = Disease_search_master.objects.get(id = int(i))
                        temp2.append({"id":int(i),"name":dis_obj.name})
                response_data_dict['associated_diseases'] = temp2
            else:
                response_data_dict['associated_diseases'] = []

            response_data_dict['associated_symptoms'] = []
            if Doctor_obj.associated_symptoms and Doctor_obj.associated_symptoms !='' and Doctor_obj.associated_symptoms != []:
                temp2 = []
                temp1 = []
                temp1 = Doctor_obj.associated_symptoms.split(',')
                for i in temp1:
                    if i!=''  and i != ' ':
                        dis_obj = Symptoms_search_master.objects.get(id = int(i))
                        temp2.append({"id":int(i),"name":dis_obj.name})
                response_data_dict['associated_symptoms'] = temp2
            else:
                response_data_dict['associated_symptoms'] = []

            response_data_dict['did'] = Doctor_obj.did
            response_data_dict['extension'] = Doctor_obj.extension
            response_data_dict['points'] = Doctor_obj.points


    except Exception as e:
        print
        '%s (%s)' % (e.message, type(e))
    return response_data_dict


####################################################################
# Name - __organisation_data_creation                                                #
# Owner - jitendra dixit
# testing:                                             #
# Review by -                                                 #
#                                                                  #
####################################################################
# A = {
#     "detail": {
#         "properties": {
#             "ambulance_service": {
#                 "type": "boolean"
#             },
#             "ambulance_service_no": {
#                 "type": "string"
#             },
#             "brochure": {
#                 "type": "string"
#             },
#             "burn_center": {
#                 "type": "boolean"
#             },
#             "department_list": {
#                 "properties": {
#                     "id": {
#                         "type": "long"
#                     },
#                     "name": {
#                         "type": "string"
#                     }
#                 }
#             },
#             "department_wise_doctor_list": {
#                 "type": "object"
#             },
#             "doctors_on_board": {
#                 "type": "string"
#             },
#             "email": {
#                 "type": "string"
#             },
#             "emergency_no": {
#                 "type": "string"
#             },
#             "year_of_establishment": {
#                 "type": "string"
#             },
#             "facility_list": {
#                 "properties": {
#                     "id": {
#                         "type": "long"
#                     },
#                     "name": {
#                         "type": "string"
#                     }
#                 }
#             },
#             "fax": {
#                 "type": "string"
#             },
#             "geolocation": {
#                 "type": "geo_point"
#             },
#             "id": {
#                 "type": "long"
#             },
#             "is_clinic": {
#                 "type": "boolean"
#             },
#             "is_hospital": {
#                 "type": "boolean"
#             },
#             "locality_id": {
#                 "type": "long"
#             },
#             "locality_name": {
#                 "type": "string"
#             },
#             "mobile_no": {
#                 "type": "string"
#             },
#             "name": {
#                 "type": "string"
#             },
#             "niche_department": {
#                 "type": "string"
#             },
#             "phone": {
#                 "type": "string"
#             },
#             "state_id": {
#                 "type": "long"
#             },
#             "state_name": {
#                 "type": "string"
#             },
#             "street": {
#                 "type": "string"
#             },
#             "city_id": {
#                 "type": "long"
#             },
#             "city_name": {
#                 "type": "string"
#             },
#             "country_id": {
#                 "type": "long"
#             },
#             "country_name": {
#                 "type": "string"
#             },
#             "category_type": {
#                 "type": "string"
#             },
#             "timing_str": {
#                 "type": "object"
#             },
#             "trauma_center": {
#                 "type": "boolean"
#             },
#             "hospital_type": {
#                 "type": "string"
#             },
#             "website": {
#                 "type": "string"
#             }
#         }
#     }
# }


def __organisation_data_creation(id):
    response_data_dict = {}
    try:
        organisation_obj = OrganisationName.objects.get(id=id)
        if organisation_obj:
            response_data_dict['name'] = organisation_obj.name
            response_data_dict['pincode'] = organisation_obj.pincode
            response_data_dict['id'] = organisation_obj.id
            response_data_dict['is_emergency'] = organisation_obj.is_emergency
            response_data_dict['is_hospital'] = organisation_obj.is_hospital
            response_data_dict['is_clinic'] = organisation_obj.is_clinic
            response_data_dict['street'] = organisation_obj.street
            response_data_dict['locality_id'] = organisation_obj.locality_id
            response_data_dict['locality_name'] = organisation_obj.locality.name
            response_data_dict['city_id'] = organisation_obj.city_id
            response_data_dict['city_name'] = organisation_obj.city.name
            response_data_dict['state_id'] = organisation_obj.state_id
            response_data_dict['state_name'] = organisation_obj.state.name
            response_data_dict['country_id'] = organisation_obj.country_id
            response_data_dict['country_name'] = organisation_obj.country.name
            response_data_dict['phone'] = organisation_obj.phone
            response_data_dict['mobile_no'] = organisation_obj.mobile_no
            response_data_dict['ambulance_service_no'] = organisation_obj.ambulance_service_no
            response_data_dict['is_live_org'] = organisation_obj.is_live_org
            response_data_dict['Finalise'] = organisation_obj.finalise
            # if  organisation_obj.is_live_org == True:
                # response_data_dict['profile_image'] = 'profile_image_path'
            response_data_dict['profile_image'] = organisation_obj.profileImage
            # else:
            #     response_data_dict['profile_image'] = ''

            # response_data_dict['department_list'] = organisation_obj.department
            # ******************************* Get Department *************************#
            # if organisation_obj.department:
            #     department_get_list = organisation_obj.department.split(',')
            #     departments = []
            #     for department in department_get_list:
            #         department_dict = {}
            #         if department != '':
            #             department_obj = Department.objects.get(id=int(department))
            #             if department_obj:
            #                 department_dict['id'] = department_obj.id
            #                 if department_obj.name:
            #                     department_dict['name'] = department_obj.name.strip()
            #                 else:
            #                     department_dict['name'] = ""
            #                 departments.append(department_dict)
            #     response_data_dict['department_list'] = departments

            # ******************************* Get Facility *************************#
            if organisation_obj.facility and organisation_obj.facility != [] and organisation_obj.facility != '[]':
                facility_get_list = organisation_obj.facility.split(',')
                facilities = []
                for facility in facility_get_list:
                    facility_dict = {}
                    if facility != '':
                        department_obj = Facility.objects.get(id=int(facility))
                        if department_obj:
                            facility_dict['id'] = department_obj.id
                            if department_obj.name:
                                facility_dict['name'] = department_obj.name.strip()
                            else:
                                facility_dict['name'] = ""
                            facilities.append(facility_dict)
                if organisation_obj.no_of_beds and organisation_obj.no_of_beds != '':
                    nbeds_dict = {}
                    bkey = 0
                    value = organisation_obj.no_of_beds.strip()
                    nbeds_dict['id'] = bkey
                    nbeds_dict['name'] = value
                    facilities.append(nbeds_dict)
                response_data_dict['facility_list'] = facilities
            else:
                response_data_dict['facility_list'] = []

            response_data_dict['niche_department'] = organisation_obj.niche_department

            response_data_dict['brochure'] = organisation_obj.broucher
            response_data_dict['fax'] = organisation_obj.fax
            response_data_dict['email'] = organisation_obj.email
            response_data_dict['emergency_no'] = organisation_obj.emergency_no
            response_data_dict['website'] = organisation_obj.website
            response_data_dict['category_type'] = organisation_obj.category

            ###
            category_id = 1;
            if str(response_data_dict['category_type']).upper() == 'PUBLIC':
                category_id = 2
            elif str(response_data_dict['category_type']).upper() == 'NURSING HOME':
                category_id = 3
            categories = [{
                "id": category_id,
                "name": response_data_dict['category_type']
            }]
            response_data_dict['category_list'] = categories;

            response_data_dict['doctors_on_board'] = organisation_obj.doctors_on_board
            if organisation_obj.type and organisation_obj.type != [] and organisation_obj.type != '[]':
                #response_data_dict['hospital_type'] = organisation_obj.type
                temp = []
                type_list = []
                temp = organisation_obj.type.split(',')
                for i in temp:
                    for j in Organisation_types.objects.all():
                        if i.strip().lower() == j.type_name.strip().lower():
                            type_list.append({'id':j.id,'name':j.type_name})
                response_data_dict['hospital_type'] = type_list

            else:
                response_data_dict['hospital_type'] = []
            response_data_dict['ambulance_service'] = organisation_obj.ambulance_service
            response_data_dict['trauma_center'] = organisation_obj.trauma_center
            response_data_dict['burn_center'] = organisation_obj.burn_center
            response_data_dict['year_of_establishment'] = organisation_obj.year_of_establishment

            # if organisation_obj.latitude and organisation_obj.longitude and float(organisation_obj.latitude) and float(
            #         organisation_obj.longitude):
            if organisation_obj.latitude and organisation_obj.longitude:
                try:
                    lat = float(organisation_obj.latitude)
                    lon = float(organisation_obj.longitude)
                    response_data_dict['geolocation'] = {
                        "lat": lat,
                        "lon": lon
                    }
                except:
                    response_data_dict['geolocation'] = {
                        "lat": 0,
                        "lon": 0
                    }

            else:
                response_data_dict['geolocation'] = {
                    "lat": 0,
                    "lon": 0
                }
            response_data_dict['timing_str'] = []

            # ----------------------------------------------------
            # Dep Wise DOC LIST OLD start
            # ----------------------------------------------------
            # try:
            #     department_obj = AssociateDoctorWithOrganization.objects.filter(organisation_id=id).values(
            #         'department').distinct()
            # except:
            #     department_obj = []
            #
            # department_wise_doctor_list = []
            #
            # chk = []
            # for dp in department_obj:
            #     department_wise_doctor_obj = {}
            #     if dp['department'] not in chk:
            #         chk.append(dp['department'])
            #         # [8808, 14523]
            #         department_doctor_obj = AssociateDoctorWithOrganization.objects.filter(organisation_id=id,
            #                                                                                department_id=dp[
            #                                                                                    'department']).values_list(
            #             'doctor', flat=True).distinct()
            #         doc_list = []
            #         for i in department_doctor_obj:
            #             # if i not in check_repeatation and
            #             tmp_dict = {}
            #             doc = Doctor.objects.get(id=i)
            #             doctor_photo_url = None
            #             tmp_dict.update({'doctor_photo_url': doctor_photo_url})
            #             tmp_dict.update({'unique_id': doc.id})
            #             tmp_dict.update({'name': doc.name})
            #             tmp_dict.update({'doctor_category': doc.category.name})
            #             tmp_dict.update({'qualification': doc.qualification_data})
            #             Doctor_Education_obj = Doctor_Education.objects.values_list('education_data', flat=True).filter(
            #                 doctor_id=doc.id)
            #             Doctor_Education_list = []
            #             for doctor_edu in Doctor_Education_obj:
            #                 Doctor_Education_list.append(doctor_edu)
            #             tmp_dict.update({'educationStr': Doctor_Education_list})
            #             try:
            #                 Schedule_obj = Schedule.objects.get(doctor_id=doc.id, organisation_id=organisation_obj.id)
            #             except:
            #                 Schedule_obj = None
            #
            #             if Schedule_obj:
            #                 if Schedule_obj.by_appointment == False:
            #                     try:
            #                         schedule_data = Schedule_obj.schedule_data
            #                         timing = convert_time_array(schedule_data)
            #                         timing_str = convert_time_str_array(schedule_data)
            #                         # tmp_dict.update({'timing': timing})
            #                         tmp_dict.update({'timing_str': timing_str})
            #                         tmp_dict.update({'timing': timing})
            #                         tmp_dict.update({'time_object': schedule_data})
            #                         tmp_dict['by_appointment'] = False
            #
            #                     except:
            #                         tmp_dict.update({'timing_str': []})
            #                         tmp_dict.update({'timing': []})
            #                         tmp_dict.update({'time_object': []})
            #                         tmp_dict['by_appointment'] = False
            #                 else:
            #                     tmp_dict.update({'timing_str': []})
            #                     tmp_dict.update({'timing': []})
            #                     tmp_dict.update({'time_object': []})
            #                     tmp_dict['by_appointment'] = True
            #             else:
            #                 tmp_dict.update({'timing_str': []})
            #                 tmp_dict.update({'timing': []})
            #                 tmp_dict.update({'time_object': []})
            #                 tmp_dict['by_appointment'] = False
            #
            #             consultancy_fee = 0
            #             try:
            #                 AttachWithDoctor_obj = AttachWithDoctor.objects.get(doctor_id=doc.id,
            #                                                                     organisation_id=organisation_obj.id)
            #                 if AttachWithDoctor_obj.consultancy_fee:
            #                     consultancy_fee = int(AttachWithDoctor_obj.consultancy_fee)
            #             except:
            #                 consultancy_fee = 0
            #             tmp_dict.update({'consultancy_fee': consultancy_fee})
            #
            #             doctor_avg_expr = doc.doctor_experience_year
            #             if doctor_avg_expr:
            #                 doctor_avg_expr = doctor_avg_expr.strip()
            #             tmp_dict.update({'doctor_avg_expr': doctor_avg_expr})
            #             # department_wise_doctor_obj.update({i:tmp_dict})
            #             doc_list.append(tmp_dict)
            #         department_wise_doctor_obj.update({'doctor_list': doc_list})
            #         dp_obj = Department.objects.get(id=dp['department'])
            #         if dp_obj:
            #             department_wise_doctor_obj['department_name'] = dp_obj.name
            #             department_wise_doctor_obj['department_id'] = dp_obj.id
            #             department_wise_doctor_list.append(department_wise_doctor_obj)
            #
            #     else:
            #         pass
            # response_data_dict['department_wise_doctor_list'] = (department_wise_doctor_list)
            #----------------------------------------------------
            # Dep Wise DOC LIST OLD end
            #----------------------------------------------------
            # ----------------------------------------------------
            # Dep Wise DOC LIST NEW start
            # ----------------------------------------------------
            all_attach_with_doctor_object_list = AttachWithDoctor.objects.filter(organisation_id = organisation_obj.id )
            all_org_dep_list = []
            if all_attach_with_doctor_object_list:
                for i in all_attach_with_doctor_object_list:
                    if i.department and i.department != '' and i.department != ' ':
                        temp =[]
                        temp = i.department.split(',')
                        for iii in temp:
                            if iii not in all_org_dep_list:
                                all_org_dep_list.append(iii)
                if all_org_dep_list != []:
                    department_wise_doctor_list = []
                    doctor_n_department_dict = {}
                    for i in all_org_dep_list:
                        temp_list =[]
                        for j in all_attach_with_doctor_object_list:
                            if i in j.department:
                                temp_list.append(j.doctor_id)
                        doctor_n_department_dict.update({i:temp_list})

                    for k,v in doctor_n_department_dict.items():
                        dep_wise_doctor_object = {}
                        department_obj = Department.objects.get(id=k)
                        dep_wise_doctor_object.update({'department_id':department_obj.id})
                        dep_wise_doctor_object.update({'department_name':department_obj.name})
                        doc_list = []
                        for doc_id in v:
                            tmp_dict = {}
                            doc = Doctor.objects.get(id=doc_id)
                            doctor_photo_url = None
                            tmp_dict.update({'doctor_photo_url': doctor_photo_url})
                            tmp_dict.update({'unique_id': doc.id})
                            tmp_dict.update({'name': doc.name})
                            tmp_dict.update({'doctor_category': doc.category.name})
                            tmp_dict.update({'qualification': doc.qualification_data})
                            Doctor_Education_obj = Doctor_Education.objects.values_list('education_data', flat=True).filter(
                                doctor_id=doc.id)
                            Doctor_Education_list = []
                            for doctor_edu in Doctor_Education_obj:
                                Doctor_Education_list.append(doctor_edu)
                            tmp_dict.update({'educationStr': Doctor_Education_list})
                            try:
                                Schedule_obj = Schedule.objects.get(doctor_id=doc.id, organisation_id=organisation_obj.id)
                            except:
                                Schedule_obj = None

                            if Schedule_obj:
                                if Schedule_obj.by_appointment == False:
                                    try:
                                        schedule_data = Schedule_obj.schedule_data
                                        timing = convert_time_array(schedule_data)
                                        timing_str = convert_time_str_array(schedule_data)
                                        # tmp_dict.update({'timing': timing})
                                        tmp_dict.update({'timing_str': timing_str})
                                        tmp_dict.update({'timing': timing})
                                        tmp_dict.update({'time_object': schedule_data})
                                        tmp_dict['by_appointment'] = False

                                    except:
                                        tmp_dict.update({'timing_str': []})
                                        tmp_dict.update({'timing': []})
                                        tmp_dict.update({'time_object': []})
                                        tmp_dict['by_appointment'] = False
                                else:
                                    tmp_dict.update({'timing_str': []})
                                    tmp_dict.update({'timing': []})
                                    tmp_dict.update({'time_object': []})
                                    tmp_dict['by_appointment'] = True
                            else:
                                tmp_dict.update({'timing_str': []})
                                tmp_dict.update({'timing': []})
                                tmp_dict.update({'time_object': []})
                                tmp_dict['by_appointment'] = False

                            consultancy_fee = 0
                            try:
                                AttachWithDoctor_obj = AttachWithDoctor.objects.get(doctor_id=doc.id,
                                                                                    organisation_id=organisation_obj.id)
                                if AttachWithDoctor_obj.consultancy_fee:
                                    consultancy_fee = int(AttachWithDoctor_obj.consultancy_fee)
                            except:
                                consultancy_fee = 0
                            tmp_dict.update({'consultancy_fee': consultancy_fee})

                            doctor_avg_expr = doc.doctor_experience_year
                            if doctor_avg_expr:
                                doctor_avg_expr = doctor_avg_expr.strip()
                            tmp_dict.update({'doctor_avg_expr': doctor_avg_expr})
                            # department_wise_doctor_obj.update({i:tmp_dict})
                            doc_list.append(tmp_dict)
                        dep_wise_doctor_object.update({'doctor_list': doc_list})
                        department_wise_doctor_list.append(dep_wise_doctor_object)
                    response_data_dict['department_wise_doctor_list'] = department_wise_doctor_list
                else:
                    response_data_dict['department_wise_doctor_list'] = []
                    department_wise_doctor_list = []
            else:
                response_data_dict['department_wise_doctor_list'] = []
                department_wise_doctor_list = []

            # ----------------------------------------------------
            # Dep Wise DOC LIST NEW  end
            # ----------------------------------------------------
            # ----------------------------------------------------
            # Dep Wise LIVE DOC LIST NEW START
            # ----------------------------------------------------
            all_attach_with_doctor_object_list = Live_Doctor_Commonworkschedule.objects.filter(
                clinic_id=organisation_obj.id)
            all_clinic_dep_list = []
            existing_clinic_dep_list = []
            new_clinic_dep_list = []

            if all_attach_with_doctor_object_list:
                for i in all_attach_with_doctor_object_list:
                    if i.department and i.department != '' and i.department != ' ':
                        temp = []
                        temp = i.department.split(',')
                        for iii in temp:
                            if iii not in all_clinic_dep_list:
                                all_clinic_dep_list.append(iii)
                if department_wise_doctor_list!=[]:
                    #for i in all_clinic_dep_list:
                    for j in department_wise_doctor_list:
                        if str(j['department_id']) in all_clinic_dep_list:
                            if str(j['department_id']) not in existing_clinic_dep_list:
                                existing_clinic_dep_list.append(str(j['department_id']))
                        # else:
                        #     if str(j['department_id']) not in new_clinic_dep_list:
                        #         new_clinic_dep_list.append(str(j['department_id']))
                    for i in all_clinic_dep_list:
                        if i not in existing_clinic_dep_list:
                            new_clinic_dep_list.append(i)

                else:
                    new_clinic_dep_list=all_clinic_dep_list
                if existing_clinic_dep_list:
                    doctor_n_department_dict = {}
                    for i in existing_clinic_dep_list:
                        temp_list = []
                        for j in all_attach_with_doctor_object_list:
                            if j.department!=None:
                                if i in j.department:
                                    temp_list.append(j.doctor_id)
                        doctor_n_department_dict.update({i: temp_list})
                    for k, v in doctor_n_department_dict.items():
                        dep_wise_doctor_object = {}
                        # department_obj = Department.objects.get(id=k)
                        # dep_wise_doctor_object.update({'department_id': department_obj.id})
                        # dep_wise_doctor_object.update({'department_name': department_obj.name})
                        live_doc_list = []
                        for doc_id in v:
                            tmp_dict = {}
                            doc = Live_Doctor.objects.get(id=doc_id)
                            doctor_photo_url = None
                            tmp_dict.update({'doctor_photo_url': doctor_photo_url})
                            tmp_dict.update({'unique_id': doc.id})
                            name = 'Dr. ' + doc.firstName + ' ' + doc.lastName
                            tmp_dict.update({'name': name})
                            ldcat = Category.objects.get(id=doc.category)
                            tmp_dict.update({'doctor_category': ldcat.name})
                            ldcat = None
                            ttttemp = ''
                            edu_list = Live_Doctor_Education.objects.filter(doctor_id=doc.id)
                            count = 0
                            for i in edu_list:
                                if i.degree != None and i.degree != '' and i.degree != []:
                                    count += 1
                                    if count == 1:
                                        ttttemp = ttttemp + i.degree
                                    else:
                                        ttttemp = ttttemp + ',' + i.degree.strip()
                            #response_data_dict['qualification_data'] = ttttemp
                            #tmp_dict.update({'qualification': doc.qualification_points})

                            tmp_dict.update({'qualification': ttttemp})                            
                            Doctor_Education_obj = Live_Doctor_Education.objects.filter(
                                doctor_id=doc_id)
                            Doctor_Education_list = []
                            for doctor_edu in Doctor_Education_obj:
                                degree = doctor_edu.degree
                                college = doctor_edu.college
                                year = doctor_edu.year
                                docedu = degree + college + str(year)
                                Doctor_Education_list.append(docedu)
                            tmp_dict.update({'educationStr': Doctor_Education_list})
                            try:
                                Schedule_obj = Live_Doctor_Commonworkschedule.objects.get(doctor_id=doc.id,
                                                                                          clinic_id=organisation_obj.id)
                            except:
                                Schedule_obj = None

                            by_appointment = False
                            if Schedule_obj:
                                if by_appointment == False:
                                    try:
                                        schedule_data = Schedule_obj.time_object
                                        timing = convert_time_array(schedule_data)
                                        # timing_str = convert_time_str_array(schedule_data)
                                        # tmp_dict.update({'timing': timing})
                                        timing_str = []
                                        tmp_dict.update({'timing_str': timing_str})
                                        tmp_dict.update({'timing': timing})
                                        tmp_dict.update({'time_object': schedule_data})
                                        tmp_dict['by_appointment'] = False

                                    except:
                                        tmp_dict.update({'timing_str': []})
                                        tmp_dict.update({'timing': []})
                                        tmp_dict.update({'time_object': []})
                                        tmp_dict['by_appointment'] = False
                                else:
                                    tmp_dict.update({'timing_str': []})
                                    tmp_dict.update({'timing': []})
                                    tmp_dict.update({'time_object': []})
                                    tmp_dict['by_appointment'] = True
                            else:
                                tmp_dict.update({'timing_str': []})
                                tmp_dict.update({'timing': []})
                                tmp_dict.update({'time_object': []})
                                tmp_dict['by_appointment'] = False

                            consultancy_fee = 0
                            try:
                                AttachWithDoctor_obj = Live_Doctor_Commonworkschedule.objects.get(doctor_id=doc.id,
                                                                                                  clinic_id=organisation_obj.id)
                                if AttachWithDoctor_obj.consultingCharge:
                                    consultancy_fee = int(AttachWithDoctor_obj.consultingCharge)
                            except:
                                consultancy_fee = 0
                            tmp_dict.update({'consultancy_fee': consultancy_fee})
                            All_experience = Live_Doctor_Experience.objects.filter(doctor_id=doc.id)
                            # sum_exp = 0
                            # for expe in All_experience:
                            #     if expe.toYear != None and expe.fromYear != None:
                            #         sum_exp = sum_exp + int(expe.toYear) - int(expe.fromYear)
                            # doctor_avg_expr = str(sum_exp) + " Years"
                            sum_exp = 0
                            lgest = 0
                            slest = 300000
                            for expe in All_experience:
                                if expe.toYear != None:
                                    if expe.toYear > lgest:
                                        lgest = expe.toYear
                                if expe.fromYear != None:
                                    if expe.fromYear < slest:
                                        slest = expe.fromYear
                            sum_exp = lgest - slest
                            if sum_exp < 1 or sum_exp == None or sum_exp == 0 or lgest == 0 or slest == 300000:
                                here_nnew_asso_obj = Live_Doctor_Associated_Data.objects.get(doctor_id=doc.id)
                                if here_nnew_asso_obj.totalexperience != None:
                                    doctor_avg_expr = here_nnew_asso_obj.totalexperience + " Years"
                                else:
                                    doctor_avg_expr = "Not Available"
                            else:
                                doctor_avg_expr = str(sum_exp) + " Years"


                            tmp_dict.update({'doctor_avg_expr': doctor_avg_expr})
                            # doctor_avg_expr = doc.experience_points
                            # if doctor_avg_expr:
                            #     doctor_avg_expr = doctor_avg_expr.strip()
                            # tmp_dict.update({'doctor_avg_expr': doctor_avg_expr})
                            # department_wise_doctor_obj.update({i:tmp_dict})
                            live_doc_list.append(tmp_dict)
                            print live_doc_list
                        for j in department_wise_doctor_list:
                            if str(j['department_id']) == k:
                                for xx in live_doc_list:
                                    j['doctor_list'].append(xx)
                                # department_wise_doctor_list.append(dep_wise_doctor_object)
                    #response_data_dict['department_wise_doctor_list'] = department_wise_doctor_list
                if new_clinic_dep_list:
                    # department_wise_doctor_list = []
                    doctor_n_department_dict = {}
                    for i in new_clinic_dep_list:
                        temp_list = []
                        for j in all_attach_with_doctor_object_list:
                            if j.department!=None:
                                if i in j.department:
                                    temp_list.append(j.doctor_id)
                        doctor_n_department_dict.update({i: temp_list})
                    for k, v in doctor_n_department_dict.items():
                        dep_wise_doctor_object = {}
                        department_obj = Department.objects.get(id=k)
                        dep_wise_doctor_object.update({'department_id': department_obj.id})
                        dep_wise_doctor_object.update({'department_name': department_obj.name})
                        doctor_list = []
                        for doc_id in v:
                            tmp_dict = {}
                            doc = Live_Doctor.objects.get(id=doc_id)
                            doctor_photo_url = None
                            tmp_dict.update({'doctor_photo_url': doctor_photo_url})
                            tmp_dict.update({'unique_id': doc.id})
                            name = 'Dr. ' + doc.firstName + ' ' + doc.lastName
                            tmp_dict.update({'name': name})
                            ldcat = Category.objects.get(id=doc.category)
                            tmp_dict.update({'doctor_category': ldcat.name})
                            ldcat = None
                            ttttemp = ''
                            edu_list = Live_Doctor_Education.objects.filter(doctor_id=doc.id)
                            count = 0
                            for i in edu_list:
                                if i.degree != None and i.degree != '' and i.degree != []:
                                    count += 1
                                    if count == 1:
                                        ttttemp = ttttemp + i.degree
                                    else:
                                        ttttemp = ttttemp + ',' + i.degree.strip()
                            # response_data_dict['qualification_data'] = ttttemp
                            # tmp_dict.update({'qualification': doc.qualification_points})

                            tmp_dict.update({'qualification': ttttemp})
                            Doctor_Education_obj = Live_Doctor_Education.objects.filter(
                                doctor_id=doc_id)
                            Doctor_Education_list = []
                            for doctor_edu in Doctor_Education_obj:
                                degree = doctor_edu.degree
                                college = doctor_edu.college
                                year = doctor_edu.year
                                docedu = degree + college + str(year)
                                Doctor_Education_list.append(docedu)
                            tmp_dict.update({'educationStr': Doctor_Education_list})
                            try:
                                Schedule_obj = Live_Doctor_Commonworkschedule.objects.get(doctor_id=doc.id,
                                                                                          clinic_id=organisation_obj.id)
                            except:
                                Schedule_obj = None

                            by_appointment = False
                            if Schedule_obj:
                                if by_appointment == False:
                                    try:
                                        #aa = Schedule_obj.timing

                                        # Done
                                        new_lllist = oolist = []

                                        for oo in Schedule_obj.time_object:
                                            oo['id'] = ''
                                            oolist.append(oo)
                                        new_lllist = []
                                        for i in oolist:
                                            if i['from_day'].lower() == 'mon':
                                                new_lllist.append(i)

                                        for i in oolist:
                                            if i['from_day'].lower() == 'tue':
                                                new_lllist.append(i)

                                        for i in oolist:
                                            if i['from_day'].lower() == 'wed':
                                                new_lllist.append(i)

                                        for i in oolist:
                                            if i['from_day'].lower() == 'thu':
                                                new_lllist.append(i)

                                        for i in oolist:
                                            if i['from_day'].lower() == 'fri':
                                                new_lllist.append(i)

                                        for i in oolist:
                                            if i['from_day'].lower() == 'sat':
                                                new_lllist.append(i)

                                        for i in oolist:
                                            if i['from_day'].lower() == 'sun':
                                                new_lllist.append(i)


                                        schedule_data = Schedule_obj.time_object
                                        timing = convert_time_array(schedule_data)
                                        # timing_str = convert_time_str_array(schedule_data)
                                        # tmp_dict.update({'timing': timing})
                                        timing_str = []
                                        tmp_dict.update({'timing_str': timing_str})
                                        tmp_dict.update({'timing': timing})
                                        tmp_dict.update({'time_object': new_lllist})
                                        tmp_dict['by_appointment'] = False


                                    except:
                                        tmp_dict.update({'timing_str': []})
                                        tmp_dict.update({'timing': []})
                                        tmp_dict.update({'time_object': []})
                                        tmp_dict['by_appointment'] = False
                                else:
                                    tmp_dict.update({'timing_str': []})
                                    tmp_dict.update({'timing': []})
                                    tmp_dict.update({'time_object': []})
                                    tmp_dict['by_appointment'] = True
                            else:
                                tmp_dict.update({'timing_str': []})
                                tmp_dict.update({'timing': []})
                                tmp_dict.update({'time_object': []})
                                tmp_dict['by_appointment'] = False

                            consultancy_fee = 0
                            try:
                                AttachWithDoctor_obj = Live_Doctor_Commonworkschedule.objects.get(doctor_id=doc.id,
                                                                                                  clinic_id=organisation_obj.id)
                                if AttachWithDoctor_obj.consultingCharge:
                                    consultancy_fee = int(AttachWithDoctor_obj.consultingCharge)
                            except:
                                consultancy_fee = 0
                            tmp_dict.update({'consultancy_fee': consultancy_fee})

                            All_experience = Live_Doctor_Experience.objects.filter(doctor_id=doc.id)
                            # sum_exp = 0
                            # for expe in All_experience:
                            #     if expe.toYear != None and expe.fromYear != None:
                            #         sum_exp = sum_exp + int(expe.toYear) - int(expe.fromYear)
                            # doctor_avg_expr = str(sum_exp) + " Years"

                            sum_exp = 0
                            lgest = 0
                            slest = 300000
                            for expe in All_experience:
                                if expe.toYear != None:
                                    if expe.toYear > lgest:
                                        lgest = expe.toYear
                                if expe.fromYear != None:
                                    if expe.fromYear < slest:
                                        slest = expe.fromYear
                            sum_exp = lgest - slest
                            if sum_exp < 1 or sum_exp == None or sum_exp == 0 or lgest == 0 or slest == 300000:
                                here_nnew_asso_obj = Live_Doctor_Associated_Data.objects.get(doctor_id=doc.id)
                                if here_nnew_asso_obj.totalexperience != None:
                                    doctor_avg_expr = here_nnew_asso_obj.totalexperience + " Years"
                                else:
                                    doctor_avg_expr = "Not Available"
                            else:
                                doctor_avg_expr = str(sum_exp) + " Years"

                            tmp_dict.update({'doctor_avg_expr': doctor_avg_expr})
                            # doctor_avg_expr = doc.experience_points
                            # if doctor_avg_expr:
                            #     doctor_avg_expr = doctor_avg_expr.strip()
                            # tmp_dict.update({'doctor_avg_expr': doctor_avg_expr})
                            # department_wise_doctor_obj.update({i:tmp_dict})
                            doctor_list.append(tmp_dict)
                        dep_wise_doctor_object.update({'doctor_list': doctor_list})
                        department_wise_doctor_list.append(dep_wise_doctor_object)
                    response_data_dict['department_wise_doctor_list'] = department_wise_doctor_list
                
                    
            else:
                pass
                # ----------------------------------------------------
                # Dep Wise LIVE DOC LIST NEW  end
                # ----------------------------------------------------






            if organisation_obj.schedule_data:
                response_data_dict['timing_str'] = convert_time_str_array(organisation_obj.schedule_data)
                response_data_dict['timing'] = convert_time_array(organisation_obj.schedule_data)
                response_data_dict['time_object'] = organisation_obj.schedule_data
            else:
                response_data_dict['timing_str'] = []
                response_data_dict['timing'] = []
                response_data_dict['time_object'] = []

            response_data_dict['did'] = organisation_obj.did
            response_data_dict['extension'] = organisation_obj.extension

            print  response_data_dict
    except Exception as e:
        print e
        '%s (%s)' % (e.message, type(e))
    return response_data_dict


####################################################################
# Name - _news_feed_data_creation                                  #
# Owner - jitendra dixittesting:                                   #
# Review by -                                                      #
#                                                                  #
####################################################################

def _news_feed_data_creation(id):
    response_data_dict = {}
    try:
        global_obj_data = NewsFeed.objects.get(id=id)
        # global_obj_data.update(publish_data=True)
        if global_obj_data:
            news_type_name = ''
            if global_obj_data.news_type_id == 1:
                news_type_name = 'Global News Feed'
            elif global_obj_data.news_type_id == 2:
                news_type_name = 'Wellness News Feed'
            elif global_obj_data.news_type_id == 3:
                news_type_name = 'Health News Feed'

            response_data_dict['id'] = global_obj_data.id
            response_data_dict['title'] = global_obj_data.topic_title.strip()
            #response_data_dict['doctors_category'] = global_obj_data.doctors_category.strip()
            response_data_dict['image_file_name'] = global_obj_data.newsfeed_image_file_name.strip()

            try:
                doctors_category = global_obj_data.doctors_category.strip()
                cat_list = []
                if doctors_category != '' and doctors_category != ' ' and doctors_category != []:
                    temp = doctors_category.split(',')
                    for i in temp:
                        cat_obj = Category.objects.get(id=int(i))
                        cat_list.append({'id': int(i), 'name': cat_obj.name})
                else:
                    cat_list = []
                response_data_dict['doctors_category'] = cat_list
            except:
                response_data_dict['doctors_category'] = []

            response_data_dict['related_topics'] = []
            if global_obj_data.related_topics:
                fnlist = []
                listls = global_obj_data.related_topics.split(',')
                objs = NewsFeed.objects.filter(is_disable=False, blocked_news=False,
                                               news_type_id=global_obj_data.news_type_id)
                for i in objs:
                    if str(i.id) in listls:
                        if i.publish_date:
                            attach_publish_date = str(i.publish_date)
                            attach_publish_date = attach_publish_date[:10]
                        else:
                            import datetime
                            attach_publish_date = str(datetime.date.today())
                            attach_publish_date = attach_publish_date[:10]

                        fnlist.append({'id': i.id, 'title': i.topic_title, 'image': i.newsfeed_image_file_name,
                                       'publish_date': attach_publish_date})
                        response_data_dict['related_topics'] = fnlist

            else:
                response_data_dict['related_topics'] = []

            response_data_dict['type_id'] = global_obj_data.news_type_id
            response_data_dict['type'] = global_obj_data.news_type.name
            if global_obj_data.publish_date:
                response_data_dict['publish_date'] = str(global_obj_data.publish_date)
                response_data_dict['publish_date'] = response_data_dict['publish_date'][:10]
            else:
                import datetime
                response_data_dict['publish_date'] = str(datetime.date.today())
                response_data_dict['publish_date'] = response_data_dict['publish_date'][:10]
            if global_obj_data.small_description:
                response_data_dict['small_description'] = global_obj_data.small_description.strip()
            else:
                response_data_dict['small_description'] = ""
            response_data_dict['html'] = global_obj_data.newsfeed_html_refined.strip()
            response_data_dict['tag_string'] = global_obj_data.tag_string.strip()

            if global_obj_data.page_title != None and global_obj_data.page_title.strip() != 'None':
                response_data_dict['page_title'] = global_obj_data.page_title.strip()
            else:
                response_data_dict['page_title'] = ''

            if global_obj_data.page_keywords != None and  global_obj_data.page_keywords.strip() != 'None':
                response_data_dict['page_keywords'] = global_obj_data.page_keywords.strip()
            else:
                response_data_dict['page_keywords'] = ''

            if global_obj_data.page_description != None and global_obj_data.page_description.strip() != 'None':
                response_data_dict['page_description'] = global_obj_data.page_description.strip()
            else:
                response_data_dict['page_description'] = ''


    except Exception as e:
        print
        '%s (%s)' % (e.message, type(e))
    return response_data_dict

####################################################################
# Name - _ambulance_data_creation                                  #
# Owner - jitendra dixit                                           #
# testing:                                                         #
# Review by -                                                      #
#                                                                  #
####################################################################

def _ambulance_data_creation(id):
    response_data_dict = {}
    try:
        ambulance_obj_data = Ambulance.objects.get(id=id)
        # global_obj_data.update(publish_data=True)
        if ambulance_obj_data:
            response_data_dict['id'] = ambulance_obj_data.id
            response_data_dict['name'] = ambulance_obj_data.name.strip()
            response_data_dict['address'] = ambulance_obj_data.address.strip()
            response_data_dict['locality_id'] = ambulance_obj_data.locality_id
            response_data_dict['locality_name'] = ambulance_obj_data.locality.name
            response_data_dict['city_id'] = ambulance_obj_data.city_id
            response_data_dict['city_name'] = ambulance_obj_data.city.name
            response_data_dict['state_id'] = ambulance_obj_data.state_id
            response_data_dict['state_name'] = ambulance_obj_data.state.name
            response_data_dict['country_id'] = ambulance_obj_data.country_id
            response_data_dict['country_name'] = ambulance_obj_data.country.name
            response_data_dict['pincode'] = ambulance_obj_data.pincode.strip()
            response_data_dict['telephone'] = ambulance_obj_data.telephone.strip()
            response_data_dict['mobile'] = ambulance_obj_data.mobile.strip()
            # response_data_dict['type'] = ambulance_obj_data.type.strip()
            # response_data_dict['service'] = ambulance_obj_data.service.strip()

            if ambulance_obj_data.service:
                response_data_dict['service'] = ambulance_obj_data.service.strip()
                fnlist = []
                listls = ambulance_obj_data.service.split(',')
                objs = AmbulanceServices.objects.filter(delete=False)
                for i in objs:
                    if str(i.id) in listls:
                        fnlist.append({'id': i.id, 'name': i.name})
                response_data_dict['service'] = fnlist

            else:
                response_data_dict['service'] = []

            if ambulance_obj_data.type:
                response_data_dict['type'] = ambulance_obj_data.type.strip()
                fnlist = []
                listls = ambulance_obj_data.type.split(',')
                objs = Ambulance_type_master.objects.filter(delete=False)
                for i in objs:
                    if str(i.id) in listls:
                        fnlist.append({'id': i.id, 'name': i.name})
                response_data_dict['type'] = fnlist

            else:
                response_data_dict['type'] = []

            # if ambulance_obj_data.service_contact_person :
            #     response_data_dict['service_contact_person'] = ambulance_obj_data.service_contact_person.strip()
            # else:
            #     response_data_dict['service_contact_person'] = ''
            response_data_dict['is_emergency'] = ambulance_obj_data.is_emergency
            # if ambulance_obj_data.ambulance_locality_coverage_to_id :
            #     response_data_dict['ambulance_locality_coverage_to_id'] = ambulance_obj_data.ambulance_locality_coverage_to_id
            # else:
            #     response_data_dict['ambulance_locality_coverage_to_id'] = 326
            # response_data_dict['ambulance_locality_coverage_from_id'] = ambulance_obj_data.ambulance_locality_coverage_from_id
            # if ambulance_obj_data.rates:
            #     response_data_dict['rates'] = ambulance_obj_data.rates.strip()
            # else:
            #     response_data_dict['rates'] = ''
            # response_data_dict = json.dumps(response_data_dict)
            print response_data_dict
            print response_data_dict
            print response_data_dict

    except Exception as e:
        print
        '%s (%s)' % (e.message, type(e))
    return response_data_dict


####################################################################
# Name - _bloodbank_data_creation                                  #
# Owner - jitendra dixit                                           #
# testing:                                                         #
# Review by -                                                      #
#                                                                  #
####################################################################

def _bloodbank_data_creation(id):
    response_data_dict = {}
    try:
        bloodbank_obj_data = BloodBank.objects.get(id=id)
        # global_obj_data.update(publish_data=True)
        if bloodbank_obj_data:
            response_data_dict['id'] = bloodbank_obj_data.id
            response_data_dict['name'] = bloodbank_obj_data.name.strip()
            response_data_dict['license'] = bloodbank_obj_data.license.strip()
            response_data_dict['address_1'] = bloodbank_obj_data.address_1.strip()
            response_data_dict['address_2'] = bloodbank_obj_data.address_2.strip()
            response_data_dict['locality_id'] = bloodbank_obj_data.locality_id
            response_data_dict['locality_name'] = bloodbank_obj_data.locality.name
            response_data_dict['city_id'] = bloodbank_obj_data.city_id
            response_data_dict['city_name'] = bloodbank_obj_data.city.name
            response_data_dict['state_id'] = bloodbank_obj_data.state_id
            response_data_dict['state_name'] = bloodbank_obj_data.state.name
            response_data_dict['country_id'] = bloodbank_obj_data.country_id
            response_data_dict['country_name'] = bloodbank_obj_data.country.name
            response_data_dict['pincode'] = bloodbank_obj_data.pincode.strip()
            if bloodbank_obj_data.telephone:
                response_data_dict['telephone'] = bloodbank_obj_data.telephone.strip()
            else:
                response_data_dict['telephone'] = ''
            if bloodbank_obj_data.services:
                response_data_dict['services'] = bloodbank_obj_data.services.strip()
                fnlist = []
                listls = bloodbank_obj_data.services.split(',')
                objs = BloodBankServices.objects.filter(delete=False)
                for i in objs:
                    if str(i.id) in listls:
                        fnlist.append({'id': i.id, 'name': i.name})
                response_data_dict['services'] = fnlist
            else:
                response_data_dict['services'] = []

            # if bloodbank_obj_data.bloodbank_schedule and bloodbank_obj_data.bloodbank_schedule != []:
            #
            #     bs = bloodbank_obj_data.bloodbank_schedule
            #     mpty = []
            #
            #     for i in bs:
            #         mpty2 = []
            #         import time
            #         for j in i['timing']:
            #
            #             st = j['start_time']
            #             et = j['end_time']
            #             st = time.strftime('%H:%M:%S', time.strptime(st, '%I:%M %p'))
            #             et = time.strftime('%H:%M:%S', time.strptime(et, '%I:%M %p'))
            #             j['start_time'] = st
            #             j['end_time'] = et
            #             mpty2.append(j)
            #         i['timing'] = mpty2
            #         mpty.append(i)
            #     response_data_dict['bloodbank_schedule'] = mpty
            # else:
            #     response_data_dict['bloodbank_schedule'] = []

            if bloodbank_obj_data.bloodbank_schedule and bloodbank_obj_data.bloodbank_schedule != []:
                response_data_dict['timing_str'] = convert_time_str_array(bloodbank_obj_data.bloodbank_schedule)
                response_data_dict['timing'] = convert_time_array(bloodbank_obj_data.bloodbank_schedule)
                response_data_dict['time_object'] = bloodbank_obj_data.bloodbank_schedule
            else:
                response_data_dict['timing_str'] = []
                response_data_dict['timing'] = []
                response_data_dict['time_object'] = []

            response_data_dict['is_emergency'] = bloodbank_obj_data.is_emergency

            # response_data_dict = json.dumps(response_data_dict)

    except Exception as e:
        print
        '%s (%s)' % (e.message, type(e))
    return response_data_dict


####################################################################
# Name - _dietitian_data_creation                                  #
# Owner - jitendra dixit                                           #
# testing:                                                         #
# Review by -                                                      #
#                                                                  #
####################################################################

def _dietitian_data_creation(id):
    response_data_dict = {}
    try:
        dietitian_obj_data = Dietitian.objects.get(id=id)
        # global_obj_data.update(publish_data=True)
        if dietitian_obj_data:
            response_data_dict['id'] = dietitian_obj_data.id
            response_data_dict['name'] = dietitian_obj_data.name.strip()
            response_data_dict['institution'] = dietitian_obj_data.institution.strip()
            response_data_dict['qualification'] = dietitian_obj_data.qualification.strip()
            response_data_dict['experience'] = dietitian_obj_data.experience.strip()

            if dietitian_obj_data.type:
                fnlist = []
                listls = dietitian_obj_data.type.split(',')
                objs = Dietitian_type_master.objects.filter(delete=False)
                for i in objs:
                    if str(i.id) in listls:
                        fnlist.append({'id': i.id, 'name': i.name})
                response_data_dict['type'] = fnlist

            else:
                response_data_dict['type'] = []

            if dietitian_obj_data.services:
                fnlist = []
                listls = dietitian_obj_data.services.split(',')
                objs = DietitianServices.objects.filter(delete=False)
                for i in objs:
                    if str(i.id) in listls:
                        fnlist.append({'id': i.id, 'name': i.name})
                response_data_dict['services'] = fnlist

            else:
                response_data_dict['services'] = []

            if dietitian_obj_data.dietitian_locality_coverage_from_id:
                response_data_dict[
                    'dietitian_locality_coverage_from_id'] = dietitian_obj_data.dietitian_locality_coverage_from_id
            else:
                response_data_dict['dietitian_locality_coverage_from_id'] = 326
            if dietitian_obj_data.dietitian_locality_coverage_to_id:
                response_data_dict[
                    'dietitian_locality_coverage_to_id'] = dietitian_obj_data.dietitian_locality_coverage_to_id
            else:
                response_data_dict['dietitian_locality_coverage_to_id'] = 326
            response_data_dict['rates'] = dietitian_obj_data.rates.strip()
            response_data_dict['packages'] = dietitian_obj_data.packages
            response_data_dict['address'] = dietitian_obj_data.address.strip()
            response_data_dict['locality_id'] = dietitian_obj_data.locality_id
            response_data_dict['city_id'] = dietitian_obj_data.city_id
            response_data_dict['state_id'] = dietitian_obj_data.state_id
            response_data_dict['country_id'] = dietitian_obj_data.country_id
            response_data_dict['pincode'] = dietitian_obj_data.pincode.strip()
            response_data_dict['email'] = dietitian_obj_data.email.strip()
            response_data_dict['telephone'] = dietitian_obj_data.telephone.strip()
            response_data_dict['alternate_telephone'] = dietitian_obj_data.alternate_telephone.strip()
            if dietitian_obj_data.mobile:
                response_data_dict['mobile'] = dietitian_obj_data.mobile.strip()
            else:
                response_data_dict['mobile'] = ''
                # response_data_dict = json.dumps(response_data_dict)


    except Exception as e:
        print
        '%s (%s)' % (e.message, type(e))
    return response_data_dict


####################################################################
# Name - _disease_data_creation                                    #
# Owner - jitendra dixit                                           #
# testing:                                                         #
# Review by -                                                      #
#                                                                  #
####################################################################

def _disease_data_creation(id):
    response_data_dict = {}
    try:
        disease_obj_data = Disease.objects.get(id=id)
        # global_obj_data.update(publish_data=True)
        if disease_obj_data:
            response_data_dict['id'] = disease_obj_data.id
            response_data_dict['title'] = disease_obj_data.topic_title.strip()
            #response_data_dict['doctors_category'] = disease_obj_data.doctors_category.strip()

            try:
                doctors_category = disease_obj_data.doctors_category.strip()
                cat_list =[]
                if doctors_category != '' and doctors_category != ' ' and doctors_category != []:
                    temp = doctors_category.split(',')
                    for i in temp :
                        cat_obj =  Category.objects.get(id = int(i))
                        cat_list.append({'id':int(i),'name': cat_obj.name})
                else:
                    cat_list = []
                response_data_dict['doctors_category'] = cat_list
            except:
                response_data_dict['doctors_category'] = []

            response_data_dict['image_file_name'] = disease_obj_data.disease_image_file_name.strip()

            response_data_dict['related_topics'] = []
            if disease_obj_data.related_topics:
                fnlist = []
                disease_obj_data.related_topics = disease_obj_data.related_topics.strip()
                listls = disease_obj_data.related_topics.split(',')
                objs = Disease.objects.filter(is_disable=False)
                for i in objs:
                    if str(i.id) in listls:
                        if i.publish_date:
                            attach_publish_date = str(i.publish_date)
                            attach_publish_date = attach_publish_date[:10]
                        else:
                            import datetime
                            attach_publish_date = str(datetime.date.today())
                            attach_publish_date = attach_publish_date[:10]

                        fnlist.append({'id': i.id, 'title': i.topic_title, 'image': i.disease_image_file_name,
                                       'publish_date': attach_publish_date})
                        response_data_dict['related_topics'] = fnlist

            else:
                response_data_dict['related_topics'] = []

            response_data_dict['html'] = disease_obj_data.disease_html_refined.strip()
            response_data_dict['tag_string'] = disease_obj_data.tag_string.strip()
            if disease_obj_data.small_description:
                response_data_dict['small_description'] = disease_obj_data.small_description.strip()
            else:
                response_data_dict['small_description'] = ''
            if disease_obj_data.publish_date:
                response_data_dict['publish_date'] = str(disease_obj_data.publish_date)
                response_data_dict['publish_date'] = response_data_dict['publish_date'][:10]
            else:
                import datetime
                response_data_dict['publish_date'] = str(datetime.date(int(2000), int(01), int(01)))
                response_data_dict['publish_date'] = response_data_dict['publish_date'][:10]
                # response_data_dict = json.dumps(response_data_dict)

            if disease_obj_data.page_title != None and disease_obj_data.page_title.strip() != 'None':
                response_data_dict['page_title'] = disease_obj_data.page_title.strip()
            else:
                response_data_dict['page_title'] = ''

            if disease_obj_data.page_keywords != None and disease_obj_data.page_keywords.strip() != 'None' :
                response_data_dict['page_keywords'] = disease_obj_data.page_keywords.strip()
            else:
                response_data_dict['page_keywords'] = ''

            if disease_obj_data.page_description != None and disease_obj_data.page_description.strip() != 'None':
                response_data_dict['page_description'] = disease_obj_data.page_description.strip()
            else:
                response_data_dict['page_description'] = ''


    except Exception as e:
        print e
        '%s (%s)' % (e.message, type(e))
    return response_data_dict


####################################################################
# Name - _plan_data_creation                                       #
# Owner - jitendra dixit                                           #
# testing:                                                         #
# Review by -                                                      #
#                                                                  #
####################################################################

def _plan_data_creation(id):
    response_data_dict = {}
    namelist = []
    try:
        plan_obj_data = ServicePlan.objects.get(id=id)
        # global_obj_data.update(publish_data=True)



        if plan_obj_data:
            response_data_dict['id'] = plan_obj_data.id

            # response_data_dict['provider_id'] = plan_obj_data.provider_id
            # response_data_dict['plan_category_id'] = plan_obj_data.plan_category_id

            response_data_dict['service_type_id'] = 0
            response_data_dict['service_type_name'] = ''
            response_data_dict['service_cotegory_master_list'] = []
            if plan_obj_data.is_life_service == True:
                kcp = plan_obj_data.kurable_plan_type
                if plan_obj_data.kurable_plan_type:
                    kcp = plan_obj_data.kurable_plan_type
                    kurable_current_plans = kcp.split(',')
                    kutypes = Kurable_subtype_master.objects.filter(delete=False)
                    namelist = []
                    for i in kutypes:
                        if str(i.id) in kurable_current_plans:
                            namelist.append({'id': i.id, 'name': i.name})
                    kurable_current_plans = namelist
                else:
                    kurable_current_plans = []

                response_data_dict['service_type_id'] = 3
                response_data_dict['service_type_name'] = 'Kurable'
                response_data_dict['service_cotegory_master_list'] = namelist

            elif plan_obj_data.is_enterprise_service == True:
                hcp = plan_obj_data.healthoholic_plan_type
                if plan_obj_data.healthoholic_plan_type:
                    hcp = plan_obj_data.healthoholic_plan_type
                    healthoholic_current_plans = hcp.split(',')
                    hetypes = Healthoholic_subtype_master.objects.filter(delete=False)
                    namelist = []
                    for i in hetypes:
                        if str(i.id) in healthoholic_current_plans:
                            namelist.append({'id': i.id, 'name': i.name})
                    healthoholic_current_plans = namelist
                else:
                    healthoholic_current_plans = []
                response_data_dict['service_type_id'] = 1
                response_data_dict['service_type_name'] = 'Healthoholic'
                response_data_dict['service_cotegory_master_list'] = namelist

            elif plan_obj_data.is_home_service == True:
                hsp = plan_obj_data.caresidense_plan_type
                if plan_obj_data.caresidense_plan_type:
                    hsp = plan_obj_data.caresidense_plan_type
                    caresidense_current_plans = hsp.split(',')
                    crtypes = CaResidense_subtype_master.objects.filter(delete=False)
                    namelist = []
                    for i in crtypes:
                        if str(i.id) in caresidense_current_plans:
                            namelist.append({'id': i.id, 'name': i.name})
                    caresidense_current_plans = namelist
                else:
                    caresidense_current_plans = []

                response_data_dict['service_type_id'] = 2
                response_data_dict['service_type_name'] = 'CaResidense'
                response_data_dict['service_cotegory_master_list'] = namelist

            response_data_dict['plan_name'] = plan_obj_data.plan_name.strip()
            if plan_obj_data.plan_price:
                response_data_dict['plan_price'] = plan_obj_data.plan_price
            else:
                response_data_dict['plan_price'] = 0
            response_data_dict['plan_validity'] = plan_obj_data.plan_validity.strip()
            if plan_obj_data.age_group:
                response_data_dict['age_group'] = plan_obj_data.age_group.strip()
            else:
                response_data_dict['age_group'] = ''

            response_data_dict['package_description'] = plan_obj_data.package_description.strip()

            # if plan_obj_data.no_of_employee :
            #     response_data_dict['no_of_employee'] = plan_obj_data.no_of_employee
            # else:
            #     response_data_dict['no_of_employee'] = 0
            #

            # if plan_obj_data.investigation
            if plan_obj_data.investigation:
                temp = plan_obj_data.investigation
                templist = []
                for key in temp:
                    templist.append(temp[key])
                response_data_dict['investigation'] = templist
            else:
                response_data_dict['investigation'] = []

            if plan_obj_data.consultation:
                temp = plan_obj_data.consultation
                templist = []
                for key in temp:
                    templist.append(temp[key])
                response_data_dict['consultation'] = templist
            else:
                response_data_dict['consultation'] = []

            if plan_obj_data.imaging:
                temp = plan_obj_data.imaging
                templist = []
                for key in temp:
                    templist.append(temp[key])
                response_data_dict['imaging'] = templist
            else:
                response_data_dict['imaging'] = []

            if plan_obj_data.others:
                temp = plan_obj_data.others
                templist = []
                for key in temp:
                    templist.append(temp[key])
                response_data_dict['others'] = templist
            else:
                response_data_dict['others'] = []

            # if plan_obj_data.discount_on_plan :
            #     response_data_dict['discount_on_plan'] = plan_obj_data.discount_on_plan
            # else:
            #     response_data_dict['discount_on_plan'] = 0
            # if plan_obj_data.price_of_plan_after_discount :
            #     response_data_dict['price_of_plan_after_discount'] = plan_obj_data.price_of_plan_after_discount
            # else:
            #     response_data_dict['price_of_plan_after_discount'] = 0


            # if plan_obj_data.user_category :
            #     response_data_dict['user_category'] = plan_obj_data.user_category.strip()
            # else:
            #     response_data_dict['user_category'] = ''
            response_data_dict['timings'] = plan_obj_data.timings.strip()
            response_data_dict['instructions'] = plan_obj_data.instructions.strip()

            if plan_obj_data.plan_title:
                response_data_dict['plan_title'] = plan_obj_data.plan_title.strip()
            else:
                response_data_dict['plan_title'] = ''
            response_data_dict['image_url'] = ''

            # if plan_obj_data.image_url :
            #     response_data_dict['image_url'] = plan_obj_data.image_url.strip()
            # else:
            #     response_data_dict['image_url'] = ''
            # if plan_obj_data.submission_date :
            #     response_data_dict['submission_date'] = str(plan_obj_data.submission_date)
            # else:
            #     response_data_dict['submission_date'] = None
            # if plan_obj_data.service_offered_in_plan :
            #     response_data_dict['service_offered_in_plan'] = plan_obj_data.service_offered_in_plan.strip()
            # else:
            #     response_data_dict['service_offered_in_plan'] = ''
            # if plan_obj_data.working_hours :
            #     response_data_dict['working_hours'] = plan_obj_data.working_hours.strip()
            # else:
            #     response_data_dict['working_hours'] = ''
            # response_data_dict['corporate_plan'] = plan_obj_data.corporate_plan
            # response_data_dict['nurse_plan'] = plan_obj_data.nurse_plan
            # response_data_dict['wellness_plan'] = plan_obj_data.wellness_plan
            # response_data_dict['hfues_plan'] = plan_obj_data.hfues_plan
            # response_data_dict['is_home_service'] = plan_obj_data.is_home_service
            # response_data_dict['is_enterprise_service'] = plan_obj_data.is_enterprise_service
            # response_data_dict['is_life_service'] = plan_obj_data.is_life_service
            # if plan_obj_data.type :
            #     response_data_dict['type'] = plan_obj_data.type.strip()
            # else:
            #     response_data_dict['type'] = ''
            # response_data_dict = json.dumps(response_data_dict)
            response_data_dict['provider_name'] = plan_obj_data.provider.owner_name
            response_data_dict['provider_id'] = plan_obj_data.provider.id

    except Exception as e:
        print
        '%s (%s)' % (e.message, type(e))
    return response_data_dict

###################################################################
#Name - _service_plan_data_creation                               #
#Owner - Dhrumil Shah                                             #
###################################################################

def _service_plan_data_creation(id):
    response_data_dict = {}
    namelist = []
    try:
        plan_obj_data = PlanNew.objects.get(id=id)
        if plan_obj_data:
            response_data_dict['plan_id'] = plan_obj_data.id
            response_data_dict['plan_provider'] = {'id':plan_obj_data.provider.id, 'name':plan_obj_data.provider.owner_name}
            response_data_dict['plan_city'] = {'id':plan_obj_data.city.id, 'name': plan_obj_data.city.name}
            response_data_dict['plan_category'] = {'id': plan_obj_data.plan_category.id, 'name': plan_obj_data.plan_category.name}
            response_data_dict['plan_sub_category'] = {'id': plan_obj_data.plan_sub_category.id, 'name': plan_obj_data.plan_sub_category.name}
            response_data_dict['other_details'] = plan_obj_data.other_details
            response_data_dict['test_details'] = plan_obj_data.test_details
            response_data_dict['total_price'] = plan_obj_data.total_price
            response_data_dict['discounted_price'] = plan_obj_data.discounted_price

    except Exception as e:
        print
        '%s (%s)' % (e.message, type(e))
    return response_data_dict


####################################################################
# Name - _nurse_bureau_data_creation                               #
# Owner - jitendra dixit                                           #
# testing:                                                         #
# Review by -                                                      #
#                                                                  #
####################################################################

def _nurse_bureau_data_creation(id):
    response_data_dict = {}
    try:
        nurse_bureau_obj_data = Nurse_Bureau.objects.get(id=id)
        # global_obj_data.update(publish_data=True)
        if nurse_bureau_obj_data:
            response_data_dict['id'] = nurse_bureau_obj_data.id
            response_data_dict['name'] = nurse_bureau_obj_data.name.strip()
            response_data_dict['certification'] = nurse_bureau_obj_data.certification.strip()
            response_data_dict['experience'] = nurse_bureau_obj_data.experience.strip()
            response_data_dict['services'] = nurse_bureau_obj_data.services.strip()
            response_data_dict['speciality'] = nurse_bureau_obj_data.speciality.strip()
            if nurse_bureau_obj_data.nurse_bureau_locality_coverage_to_id:
                response_data_dict[
                    'nurse_bureau_locality_coverage_to_id'] = nurse_bureau_obj_data.nurse_bureau_locality_coverage_to_id
            else:
                response_data_dict['nurse_bureau_locality_coverage_to_id'] = 326
            if nurse_bureau_obj_data.nurse_bureau_locality_coverage_from_id:
                response_data_dict[
                    'nurse_bureau_locality_coverage_from_id'] = nurse_bureau_obj_data.nurse_bureau_locality_coverage_from_id
            else:
                response_data_dict['nurse_bureau_locality_coverage_from_id'] = 326
            response_data_dict['locality_id'] = nurse_bureau_obj_data.locality_id
            response_data_dict['city_id'] = nurse_bureau_obj_data.city_id
            response_data_dict['state_id'] = nurse_bureau_obj_data.state_id
            response_data_dict['country_id'] = nurse_bureau_obj_data.country_id
            response_data_dict['pincode'] = nurse_bureau_obj_data.pincode.strip()
            response_data_dict['address'] = nurse_bureau_obj_data.address.strip()
            response_data_dict['email'] = nurse_bureau_obj_data.email.strip()

            if nurse_bureau_obj_data.nurse_bureau_schedule and nurse_bureau_obj_data.nurse_bureau_schedule != []:

                bs = nurse_bureau_obj_data.nurse_bureau_schedule
                mpty = []

                for i in bs:
                    mpty2 = []
                    import time
                    for j in i['timing']:
                        st = j['start_time']
                        et = j['end_time']
                        st = time.strftime('%H:%M:%S', time.strptime(st, '%I:%M %p'))
                        et = time.strftime('%H:%M:%S', time.strptime(et, '%I:%M %p'))
                        j['start_time'] = st
                        j['end_time'] = et
                        mpty2.append(j)
                    i['timing'] = mpty2
                    mpty.append(i)
                response_data_dict['nurse_bureau_schedule'] = mpty
            else:
                response_data_dict['nurse_bureau_schedule'] = []

            response_data_dict['rates'] = nurse_bureau_obj_data.rates.strip()
            response_data_dict['telephone'] = nurse_bureau_obj_data.telephone.strip()
            if nurse_bureau_obj_data.mobile:
                response_data_dict['mobile'] = nurse_bureau_obj_data.mobile.strip()
            else:
                response_data_dict['mobile'] = ''
            if nurse_bureau_obj_data.contact_person:
                response_data_dict['contact_person'] = nurse_bureau_obj_data.contact_person.strip()
            else:
                response_data_dict['contact_person'] = ''
            if nurse_bureau_obj_data.branches:
                response_data_dict['branches'] = nurse_bureau_obj_data.branches.strip()
            else:
                response_data_dict['branches'] = ''
            response_data_dict['website'] = nurse_bureau_obj_data.website.strip()
            if nurse_bureau_obj_data.nurse_bureau_packages:
                response_data_dict['nurse_bureau_packages'] = nurse_bureau_obj_data.nurse_bureau_packages.strip()
            else:
                response_data_dict['nurse_bureau_packages'] = ''
            if nurse_bureau_obj_data.no_of_nurses:
                response_data_dict['no_of_nurses'] = nurse_bureau_obj_data.no_of_nurses.strip()
            else:
                response_data_dict['no_of_nurses'] = ''
            if nurse_bureau_obj_data.nurses_experience:
                response_data_dict['nurses_experience'] = nurse_bureau_obj_data.nurses_experience.strip()
            else:
                response_data_dict['nurses_experience'] = ''
            if nurse_bureau_obj_data.contact_person_contact_no:
                response_data_dict[
                    'contact_person_contact_no'] = nurse_bureau_obj_data.contact_person_contact_no.strip()
            else:
                response_data_dict['contact_person_contact_no'] = ''
            if nurse_bureau_obj_data.contact_person_email:
                response_data_dict['contact_person_email'] = nurse_bureau_obj_data.contact_person_email.strip()
            else:
                response_data_dict['contact_person_email'] = ''
            if nurse_bureau_obj_data.packages:
                response_data_dict['packages'] = nurse_bureau_obj_data.packages
            else:
                response_data_dict['packages'] = None
                # response_data_dict = json.dumps(response_data_dict)

    except Exception as e:
        print
        '%s (%s)' % (e.message, type(e))
    return response_data_dict


####################################################################
# Name - _pharmacy_data_creation                                   #
# Owner - jitendra dixit                                           #
# testing:                                                         #
# Review by -                                                      #
#                                                                  #
####################################################################

def _pharmacy_data_creation(id):
    response_data_dict = {}
    try:
        pharmacy_obj_data = MedicalPharmacyStore.objects.get(id=id)
        # global_obj_data.update(publish_data=True)
        if pharmacy_obj_data:
            response_data_dict['id'] = pharmacy_obj_data.id
            response_data_dict['name'] = pharmacy_obj_data.name.strip()
            response_data_dict['locality_id'] = pharmacy_obj_data.locality_id
            response_data_dict['locality_name'] = pharmacy_obj_data.locality.name
            response_data_dict['city_id'] = pharmacy_obj_data.city_id
            response_data_dict['city_name'] = pharmacy_obj_data.city.name
            response_data_dict['state_id'] = pharmacy_obj_data.state_id
            response_data_dict['state_name'] = pharmacy_obj_data.state.name
            response_data_dict['country_id'] = pharmacy_obj_data.country_id
            response_data_dict['country_name'] = pharmacy_obj_data.country.name
            response_data_dict['pincode'] = pharmacy_obj_data.pincode.strip()
            response_data_dict['address'] = pharmacy_obj_data.address.strip()
            if pharmacy_obj_data.telephone:
                response_data_dict['telephone'] = pharmacy_obj_data.telephone.strip()
            else:
                response_data_dict['telephone'] = ''
            if pharmacy_obj_data.mobile:
                response_data_dict['mobile'] = pharmacy_obj_data.mobile.strip()
            else:
                response_data_dict['mobile'] = ''
            if pharmacy_obj_data.type:
                mptylist = []
                listl = pharmacy_obj_data.type.split(',')
                all_type_pharmacy = MedicalPharmacyStoreType.objects.filter(delete=False)
                for i in all_type_pharmacy:
                    if str(i.id) in listl:
                        mptylist.append({'id': i.id, 'name': i.name})

                response_data_dict['type'] = mptylist
            else:
                response_data_dict['type'] = []

            if pharmacy_obj_data.services:
                response_data_dict['services'] = pharmacy_obj_data.services.strip()
                fnlist = []
                listls = pharmacy_obj_data.services.split(',')
                objs = MedicalPharmacyStoreServices.objects.filter(delete=False)
                for i in objs:
                    if str(i.id) in listls:
                        fnlist.append({'id': i.id, 'name': i.name})
                response_data_dict['services'] = fnlist

            else:
                response_data_dict['services'] = []

            if pharmacy_obj_data.pharmacy_schedule and pharmacy_obj_data.pharmacy_schedule != []:
                response_data_dict['timing_str'] = convert_time_str_array(pharmacy_obj_data.pharmacy_schedule)
                response_data_dict['timing'] = convert_time_array(pharmacy_obj_data.pharmacy_schedule)
                response_data_dict['time_object'] = pharmacy_obj_data.pharmacy_schedule
            else:
                response_data_dict['timing_str'] = []
                response_data_dict['timing'] = []
                response_data_dict['time_object'] = []

            response_data_dict['is_emergency'] = pharmacy_obj_data.is_emergency
            # response_data_dict = json.dumps(response_data_dict)


    except Exception as e:
        print
        '%s (%s)' % (e.message, type(e))
    return response_data_dict


####################################################################
# Name - _lab_data_creation                                        #
# Owner - jitendra dixit                                           #
# testing:                                                         #
# Review by -                                                      #
#                                                                  #
####################################################################

def _lab_data_creation(id):
    response_data_dict = {}
    try:
        lab_obj_data = Labs.objects.get(id=id)
        # global_obj_data.update(publish_data=True)
        if lab_obj_data:
            response_data_dict['id'] = lab_obj_data.id
            response_data_dict['name'] = lab_obj_data.name.strip()
            response_data_dict['locality_id'] = lab_obj_data.locality_id
            response_data_dict['locality_name'] = lab_obj_data.locality.name
            response_data_dict['city_id'] = lab_obj_data.city_id
            response_data_dict['city_name'] = lab_obj_data.city.name
            response_data_dict['state_id'] = lab_obj_data.state_id
            response_data_dict['state_name'] = lab_obj_data.state.name
            response_data_dict['country_id'] = lab_obj_data.country_id
            response_data_dict['country_name'] = lab_obj_data.country.name
            response_data_dict['pincode'] = lab_obj_data.pincode.strip()
            response_data_dict['address'] = lab_obj_data.address.strip()
            response_data_dict['telephone'] = lab_obj_data.telephone.strip()
            response_data_dict['url'] = lab_obj_data.lab_website.strip()

            response_data_dict['branches'] = {}
            databr = {}
            save_id = 0
            try:
                b = Lab_branches.objects.get(lab_id=lab_obj_data.id)
            except:
                b = None
            response_data_dict['branches'] = listmpty = []
            if b:
                databr = b.branches
                save_id = int(databr['lab_id'])
                del databr['lab_id']
                databr.update({'id': save_id})
                bb = databr['branch_details']

                for k in bb:
                    try:
                        sch_test = bb[k]['branch_schedule']
                    except:
                        bb[k]['branch_schedule'] = []
                    if bb[k]['branch_schedule'] and bb[k]['branch_schedule'] != []:
                        timing_str = timing = []
                        timing_str = convert_time_str_array(sch_test)
                        timing = convert_time_array(sch_test)
                        bb[k].update({'timing': timing})
                        bb[k].update({'timing_str': timing_str})
                        bb[k].update({'time_object': sch_test})

                        del bb[k]['branch_schedule']

                    else:
                        del bb[k]['branch_schedule']
                        bb[k].update({'timing': []})
                        bb[k].update({'timing_str': []})
                        bb[k].update({'time_object': []})
                    listmpty.append(bb[k])

                # databr['branch_details'] = bb
                response_data_dict['branches'] = listmpty
            else:
                response_data_dict['branches'] = listmpty

            if lab_obj_data.lab_services:
                fnlist = []
                listls = lab_obj_data.lab_services.split(',')
                objs = Lab_services_master.objects.filter(delete=False)
                for i in objs:
                    if str(i.id) in listls:
                        fnlist.append({'id': i.id, 'name': i.name})
                response_data_dict['lab_services'] = fnlist

            else:
                response_data_dict['lab_services'] = []

            if lab_obj_data.lab_schedule and lab_obj_data.lab_schedule != []:
                response_data_dict['timing_str'] = convert_time_str_array(lab_obj_data.lab_schedule)
                response_data_dict['timing'] = convert_time_array(lab_obj_data.lab_schedule)
                response_data_dict['time_object'] = lab_obj_data.lab_schedule
            else:
                response_data_dict['timing_str'] = []
                response_data_dict['timing'] = []
                response_data_dict['time_object'] = []

            response_data_dict['lab_collection_timing'] = lab_obj_data.lab_collection_timing.strip()
            # response_data_dict['ratings'] = lab_obj_data.ratings.strip()
            # response_data_dict['pathology_doctor_name'] = lab_obj_data.pathology_doctor_name.strip()
            # response_data_dict['pathology_email'] = lab_obj_data.pathology_email.strip()
            # response_data_dict['rate'] = lab_obj_data.rate.strip()



            if lab_obj_data.lab_doctors_on_board:
                response_data_dict['lab_doctors_on_board'] = lab_obj_data.lab_doctors_on_board.strip()
            else:
                response_data_dict['lab_doctors_on_board'] = ''

            if lab_obj_data.lab_type_id:
                response_data_dict['lab_type_id'] = lab_obj_data.lab_type_id
                response_data_dict['lab_type_name'] = lab_obj_data.lab_type.name
            else:
                response_data_dict['lab_type_id'] = 0
                response_data_dict['lab_type_name'] = ''

            response_data_dict['is_emergency'] = lab_obj_data.is_emergency
            if lab_obj_data.tests:
                listl = []
                test_all_master = Lab_test_master.objects.all()
                tdetails = lab_obj_data.tests['test_details']
                if tdetails:
                    for k in tdetails:
                        for i in test_all_master:
                            if i.name == k:
                                listl.append({'id': i.id, 'name': k, 'price': int(tdetails[k])})

                    response_data_dict['tests'] = listl
                else:
                    response_data_dict['tests'] = []
            else:
                response_data_dict['tests'] = []

            if lab_obj_data.lab_accreditation_body:

                acc_objs = Lab_accreditation_body_master.objects.filter(delete=False)
                templist = lab_obj_data.lab_accreditation_body.split(',')
                buildlist = []
                for i in acc_objs:
                    if str(i.id) in templist:
                        buildlist.append({'id': i.id, 'name': i.name})
                response_data_dict['lab_accreditation_body'] = buildlist
            else:
                response_data_dict['lab_accreditation_body'] = []

            if lab_obj_data.lab_mobile:
                response_data_dict['lab_mobile'] = lab_obj_data.lab_mobile.strip()
            else:
                response_data_dict['lab_mobile'] = ''
            if lab_obj_data.lab_departments:
                lab_dep_all = Lab_department_master.objects.filter(delete=False)
                response_data_dict['lab_departments'] = []
                if len(lab_dep_all) > 0:
                    listld = lab_obj_data.lab_departments.split(',')
                    for i in lab_dep_all:
                        if str(i.id) in listld:
                            response_data_dict['lab_departments'].append({'id': i.id, 'name': i.name})
                else:
                    response_data_dict['lab_departments'] = []
            else:
                response_data_dict['lab_departments'] = []
                # response_data_dict = json.dumps(response_data_dict)

            response_data_dict['did'] = lab_obj_data.did
            response_data_dict['extension'] = lab_obj_data.extension


    except Exception as e:
        print e
        '%s (%s)' % (e.message, type(e))
    return response_data_dict


####################################################################
# Name - _rehab_data_creation                                      #
# Owner - jitendra dixit                                           #
# testing:                                                         #
# Review by -                                                      #
#                                                                  #
####################################################################

def _rehab_data_creation(id):
    response_data_dict = {}
    try:
        rehab_obj_data = RehabCenter.objects.get(id=id)
        # global_obj_data.update(publish_data=True)
        if rehab_obj_data:
            response_data_dict['id'] = rehab_obj_data.id
            response_data_dict['clinic_name'] = rehab_obj_data.clinic_name.strip()
            response_data_dict['locality_id'] = rehab_obj_data.locality_id
            response_data_dict['locality_name'] = rehab_obj_data.locality.name
            response_data_dict['city_id'] = rehab_obj_data.city.id
            response_data_dict['city_name'] = rehab_obj_data.city.name
            response_data_dict['state_id'] = rehab_obj_data.state_id
            response_data_dict['state_name'] = rehab_obj_data.state.name
            response_data_dict['country_id'] = rehab_obj_data.country_id
            response_data_dict['country_name'] = rehab_obj_data.country.name
            response_data_dict['pincode'] = rehab_obj_data.pincode.strip()
            response_data_dict['address'] = rehab_obj_data.address.strip()
            response_data_dict['doctor_name'] = rehab_obj_data.doctor_name.strip()
            # response_data_dict['experience'] = rehab_obj_data.experience.strip()
            # response_data_dict['qualification'] = rehab_obj_data.qualification.strip()
            # if rehab_obj_data.rehab_locality_coverage_from_id :
            #     response_data_dict['rehab_locality_coverage_from_id'] = rehab_obj_data.rehab_locality_coverage_from_id
            #     response_data_dict['rehab_locality_coverage_from_name'] = rehab_obj_data.rehab_locality_coverage_from.name
            # else:
            #
            #
            #     response_data_dict['rehab_locality_coverage_to_id'] = 0
            #     response_data_dict['rehab_locality_coverage_to_name'] = ''
            # response_data_dict['services'] = rehab_obj_data.services.strip()
            response_data_dict['telephone'] = rehab_obj_data.telephone.strip()
            if rehab_obj_data.mobile:
                response_data_dict['mobile'] = rehab_obj_data.mobile.strip()
            else:
                response_data_dict['mobile'] = ''
                # response_data_dict['email'] = rehab_obj_data.email.strip()
            # response_data_dict['rates'] = rehab_obj_data.rates.strip()
            # response_data_dict['type'] = rehab_obj_data.type.strip()
            response_data_dict['speciality'] = []
            if rehab_obj_data.speciality:
                templist = []
                temp = rehab_obj_data.speciality.split(',')
                all_spe = Rehab_speciality_master.objects.filter(delete=False)
                for i in all_spe:
                    if str(i.id) in temp:
                        aa = {'id':i.id,'name':i.name}
                        templist.append(aa)
                        aa = {}
                response_data_dict['speciality'] = templist
            else:
                response_data_dict['speciality'] = []

            response_data_dict['services'] = []
            if rehab_obj_data.services:
                templist = []
                temp = rehab_obj_data.services.split(',')
                all_ser = RehabServices.objects.filter(delete=False)
                for i in all_ser:
                    if str(i.id) in temp:
                        aa = {'id':i.id,'name':i.name}
                        templist.append(aa)
                        aa = {}
                response_data_dict['services'] = templist
            else:
                response_data_dict['services'] = []

            response_data_dict['type'] = []
            if rehab_obj_data.type:
                templist = []
                temp = rehab_obj_data.type.split(',')
                all_ser = Rehab_type_master.objects.filter(delete=False)
                for i in all_ser:
                    if str(i.id) in temp:
                        aa = {'id':i.id,'name':i.name}
                        templist.append(aa)
                        aa = {}
                response_data_dict['type'] = templist
            else:
                response_data_dict['type'] = []

            # if rehab_obj_data.rehab_schedule and rehab_obj_data.rehab_schedule != []:
            #     response_data_dict['timing_str'] = convert_time_str_array(rehab_obj_data.rehab_schedule)
            #     response_data_dict['timing'] = convert_time_array(rehab_obj_data.rehab_schedule)


            response_data_dict['is_emergency'] = rehab_obj_data.is_emergency
            # response_data_dict = json.dumps(response_data_dict)
            print response_data_dict
    except Exception as e:
        print e
        '%s (%s)' % (e.message, type(e))
    return response_data_dict


####################################################################
# Name - _symptoms_data_creation                                   #
# Owner - jitendra dixit                                           #
# testing:                                                         #
# Review by -                                                      #
#                                                                  #
####################################################################

def _symptoms_data_creation(id):
    response_data_dict = {}
    try:
        symptoms_obj_data = Symptoms.objects.get(id=id)
        # global_obj_data.update(publish_data=True)
        if symptoms_obj_data:
            response_data_dict['id'] = symptoms_obj_data.id
            response_data_dict['title'] = symptoms_obj_data.topic_title.strip()
            #response_data_dict['doctors_category'] = symptoms_obj_data.doctors_category.strip()
            response_data_dict['image_file_name'] = symptoms_obj_data.symptoms_image_file_name.strip()

            try:
                doctors_category = symptoms_obj_data.doctors_category.strip()
                cat_list = []
                if doctors_category != '' and doctors_category != ' ' and doctors_category != []:
                    temp = doctors_category.split(',')
                    for i in temp:
                        cat_obj = Category.objects.get(id=int(i))
                        cat_list.append({'id': int(i), 'name': cat_obj.name})
                else:
                    cat_list = []
                response_data_dict['doctors_category'] = cat_list
            except:
                response_data_dict['doctors_category'] = []

            response_data_dict['related_topics'] = []
            if symptoms_obj_data.related_topics:
                fnlist = []
                symptoms_obj_data.related_topics = symptoms_obj_data.related_topics.strip()
                listls = symptoms_obj_data.related_topics.split(',')
                objs = Symptoms.objects.filter(is_disable=False)
                for i in objs:
                    if str(i.id) in listls:
                        if i.publish_date:
                            attach_publish_date = str(i.publish_date)
                            attach_publish_date = attach_publish_date[:10]
                        else:
                            import datetime
                            attach_publish_date = str(datetime.date.today())
                            attach_publish_date = attach_publish_date[:10]

                        fnlist.append({'id': i.id, 'title': i.topic_title, 'image': i.symptoms_image_file_name,
                                       'publish_date': attach_publish_date})
                        response_data_dict['related_topics'] = fnlist

            else:
                response_data_dict['related_topics'] = []

            response_data_dict['html'] = symptoms_obj_data.symptoms_html_refined.strip()
            response_data_dict['tag_string'] = symptoms_obj_data.tag_string.strip()
            if symptoms_obj_data.small_description:
                response_data_dict['small_description'] = symptoms_obj_data.small_description.strip()
            else:
                response_data_dict['small_description'] = ''
            if symptoms_obj_data.publish_date:
                response_data_dict['publish_date'] = str(symptoms_obj_data.publish_date)
                response_data_dict['publish_date'] = response_data_dict['publish_date'][:10]
            else:
                import datetime
                response_data_dict['publish_date'] = str(datetime.date(int(2000), int(01), int(01)))
                response_data_dict['publish_date'] = response_data_dict['publish_date'][:10]

                # response_data_dict = json.dumps(response_data_dict)
            if symptoms_obj_data.page_title != None and symptoms_obj_data.page_title.strip() != 'None' :
                response_data_dict['page_title'] = symptoms_obj_data.page_title.strip()
            else:
                response_data_dict['page_title'] = ''

            if symptoms_obj_data.page_keywords != None and symptoms_obj_data.page_keywords.strip() != 'None':
                response_data_dict['page_keywords'] = symptoms_obj_data.page_keywords.strip()
            else:
                response_data_dict['page_keywords'] = ''

            if symptoms_obj_data.page_description != None and symptoms_obj_data.page_description.strip() != 'None' :
                response_data_dict['page_description'] = symptoms_obj_data.page_description.strip()
            else:
                response_data_dict['page_description'] = ''

    except Exception as e:
        print e
        '%s (%s)' % (e.message, type(e))
    return response_data_dict


####################################################################
# Name - _therapist_data_creation                                  #
# Owner - jitendra dixit                                           #
# testing:                                                         #
# Review by -                                                      #
#                                                                  #
####################################################################

def _therapist_data_creation(id):
    response_data_dict = {}
    try:
        therapist_obj_data = Therapist.objects.get(id=id)
        # global_obj_data.update(publish_data=True)
        if therapist_obj_data:
            response_data_dict['id'] = therapist_obj_data.id
            response_data_dict['name'] = therapist_obj_data.name.strip()
            response_data_dict['institution'] = therapist_obj_data.institution.strip()
            response_data_dict['qualification'] = therapist_obj_data.qualification.strip()
            response_data_dict['experience'] = therapist_obj_data.experience.strip()
            if therapist_obj_data.type:
                response_data_dict['type'] = therapist_obj_data.type.strip()
            else:
                response_data_dict['type'] = ''
            if therapist_obj_data.services:
                response_data_dict['services'] = therapist_obj_data.services.strip()
            else:
                response_data_dict['services'] = ''
            if therapist_obj_data.speciality:
                response_data_dict['speciality'] = therapist_obj_data.speciality.strip()
            else:
                response_data_dict['speciality'] = ''
            if therapist_obj_data.therapist_locality_coverage_from_id:
                response_data_dict[
                    'therapist_locality_coverage_from_id'] = therapist_obj_data.therapist_locality_coverage_from_id
                response_data_dict[
                    'therapist_locality_coverage_from_name'] = therapist_obj_data.therapist_locality_coverage_from.name
            else:
                response_data_dict['therapist_locality_coverage_to_id'] = 0
                response_data_dict['therapist_locality_coverage_to_name'] = ''
            response_data_dict['rates'] = therapist_obj_data.rates.strip()
            if therapist_obj_data.packages:
                response_data_dict['packages'] = therapist_obj_data.packages
            else:
                response_data_dict['packages'] = {}
            response_data_dict['address'] = therapist_obj_data.address.strip()
            response_data_dict['pincode'] = therapist_obj_data.pincode.strip()
            response_data_dict['country_id'] = therapist_obj_data.country_id
            response_data_dict['state_id'] = therapist_obj_data.state_id
            response_data_dict['city_id'] = therapist_obj_data.city_id
            response_data_dict['locality_id'] = therapist_obj_data.locality_id
            response_data_dict['email'] = therapist_obj_data.email.strip()
            response_data_dict['telephone'] = therapist_obj_data.telephone.strip()
            if therapist_obj_data.alternate_telephone:
                response_data_dict['alternate_telephone'] = therapist_obj_data.alternate_telephone.strip()
            else:
                response_data_dict['alternate_telephone'] = ''
            response_data_dict['mobile'] = therapist_obj_data.mobile.strip()

            # response_data_dict = json.dumps(response_data_dict)

    except Exception as e:
        print
        '%s (%s)' % (e.message, type(e))
    return response_data_dict


####################################################################
# Name - convert_time_str_array                                                #
# Owner - jitendra dixit
# testing:                                             #
# Review by -                                                 #
#                                                                  #
####################################################################


def convert_time_str_array(JSON_data_list):
    timing_shw_list = []
    days_list = []
    time__list = []
    timing__shw__list = []
    for time in JSON_data_list:
        timing_shw_dict = {}
        time_list = []
        if time['from_day'] and time['to_day']:
            timing_shw_dict['day'] = str(time['from_day'] + ' - ' + time['to_day']).upper()
        elif time['from_day']:
            timing_shw_dict['day'] = str(time['from_day']).upper()

        for time_temp in time['timing']:
            time_list.append(str(time_temp['start_time'] + ' - ' + time_temp['end_time']).upper())
        timing_shw_dict['timing'] = time_list
        timing_shw_list.append(timing_shw_dict)
    for i in timing_shw_list:
        days_list.append(i['day'])
        time__list.append(','.join(i['timing']))
    timing__shw__list.append({
        'days': ','.join(days_list),
        'timing': ','.join(time__list)
    })
    return timing__shw__list


####################################################################
# Name - convert_time_array                                                #
# Owner - jitendra dixit
# testing:                                             #
# Review by -                                                 #
#                                                                  #
####################################################################


def convert_time_array(JSON_data_list):
    short_day_list = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    full_day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    timing_list = []
    for time in JSON_data_list:
        if time['from_day'] and time['to_day']:
            from_day_range = short_day_list.index(time['from_day'])
            to_day_range = short_day_list.index(time['to_day']) + 1
            for i in range(from_day_range, to_day_range):
                for time_temp in time['timing']:
                    timing_shw_dict = {}
                    timing_shw_dict['day'] = full_day_list[i]
                    timing_shw_dict['start_time'] = convert_am_pm_24_hours_string(time_temp['start_time'])
                    timing_shw_dict['end_time'] = convert_am_pm_24_hours_string(time_temp['end_time'])
                    timing_list.append(timing_shw_dict)

        elif time['from_day']:
            # special case
            time_list = time['from_day'].split(',')
            for time_ in time_list:
                from_day_range = short_day_list.index(time_.strip())
                for time_temp in time['timing']:
                    timing_shw_dict = {}
                    timing_shw_dict['day'] = full_day_list[from_day_range]
                    timing_shw_dict['start_time'] = convert_am_pm_24_hours_string(time_temp['start_time'])
                    timing_shw_dict['end_time'] = convert_am_pm_24_hours_string(time_temp['end_time'])
                    timing_list.append(timing_shw_dict)
    return timing_list


####################################################################
# Name - convert_am_pm_24_hours_string                                                #
# Owner - jitendra dixit
# testing:                                             #
# Review by -                                                 #
#                                                                  #
####################################################################

def convert_am_pm_24_hours_string(time):
    if time == '' or time == ' ':
        return time
    t_split = time.split(':')
    if (t_split[1][2:]).strip() == 'PM' and t_split[0] != '12':
        t_split[0] = str(12 + int(t_split[0]))
    elif int(t_split[0]) == 12 and t_split[1][2:] == 'AM':
        t_split[0] = '00'
    t_split[1] = t_split[1][:2]
    t_split.append('00')
    return ':'.join(t_split)


####################################################################
# Name -master_SingleRecord_elastic_update                         #
# By - Nishank                                                     #
#                                                                  #
#                                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def master_SingleRecord_elastic_update(request, action=None, master_type=None, id=None, edit=None):
    try:
        response = False

        if master_type == "country" and id:
            try:
                country_obj = Country.objects.get(id=id)
            except:
                print 'No object with this id found -RECORD NOT SENT TO ELASTIC'
                return False

            if action == "publish":
                if edit == 'Yes':
                    if country_obj.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = country_obj.id
                        response_data_dict['name'] = country_obj.name
                        response_data_dict['country_code'] = country_obj.country_code
                        response = elasticsearch_client.index_data('master', 'country', id, response_data_dict)
                        if response:
                            # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                            print 'Succesfully Published single ' + master_type + ' Record FROM ELASTIC'
                            return True
                        else:
                            print 'Record NOT SENT TO ELASTIC - UNKNOWN'
                            return True
                    else:
                        print "Could not publish as Record is Deactive IN CMS"
                else:
                    response_data_dict = {}
                    response_data_dict['id'] = country_obj.id
                    response_data_dict['name'] = country_obj.name
                    response_data_dict['country_code'] = country_obj.country_code
                    response = elasticsearch_client.index_data('master', 'country', id, response_data_dict)
                    if response:
                        # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                        print 'Succesfully Published single ' + master_type + ' Record FROM ELASTIC'
                        return True
                    else:
                        print 'Record NOT SENT TO ELASTIC - UNKNOWN'
                        return True
            elif action == "un-publish":
                response = elasticsearch_client.delete_document('master', 'country', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    print 'Succesfully Published single ' + master_type + ' Record'
                else:
                    print 'Record NOT DELTEED FROM ELASTIC - UNKNOWN'
                    return False

        if master_type == "state" and id:
            try:
                state_obj = State.objects.get(id=id)
            except:
                print 'No object with this id found -RECORD NOT SENT TO ELASTIC'
                return False

            if action == "publish":
                if edit == 'Yes':
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
                            print 'Succesfully Published single ' + master_type + ' Record FROM ELASTIC'
                            return True
                        else:
                            print 'Record NOT SENT TO ELASTIC - UNKNOWN'
                            return True
                    else:
                        print "Could not publish as Record is Deactive IN CMS"
                else:
                    response_data_dict = {}
                    response_data_dict['id'] = state_obj.id
                    response_data_dict['name'] = state_obj.name
                    response_data_dict['state_code'] = state_obj.state_code
                    response_data_dict['country_id'] = state_obj.country.id
                    response_data_dict['country_name'] = state_obj.country.name
                    response = elasticsearch_client.index_data('master', 'state', id, response_data_dict)
                    if response:
                        # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                        print 'Succesfully Published single ' + master_type + ' Record FROM ELASTIC'
                        return True
                    else:
                        print 'Record NOT SENT TO ELASTIC - UNKNOWN'
                        return True
            elif action == "un-publish":
                response = elasticsearch_client.delete_document('master', 'state', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    print 'Succesfully Published single ' + master_type + ' Record'
                    return True
                else:
                    print 'Record NOT DELTEED FROM ELASTIC - UNKNOWN'
                    return False
        if master_type == "city" and id:
            try:
                city_obj = City.objects.get(id=id)
            except:
                print 'No object with this id found -RECORD NOT SENT TO ELASTIC'
                return False

            if action == "publish":
                if edit == 'Yes':
                    if city_obj.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = city_obj.id
                        response_data_dict['name'] = city_obj.name
                        response_data_dict['city_code'] = city_obj.city_code
                        response_data_dict['state_id'] = city_obj.state.id
                        response_data_dict['state_name'] = city_obj.state.name
                        response = elasticsearch_client.index_data('master', 'city', id, response_data_dict)
                        if response:
                            # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                            print 'Succesfully Published single ' + master_type + ' Record FROM ELASTIC'
                            return True
                        else:
                            print 'Record NOT SENT TO ELASTIC - UNKNOWN'
                            return True
                    else:
                        print "Could not publish as Record is Deactive IN CMS"
                else:
                    response_data_dict = {}
                    response_data_dict['id'] = city_obj.id
                    response_data_dict['name'] = city_obj.name
                    response_data_dict['city_code'] = city_obj.city_code
                    response_data_dict['state_id'] = city_obj.state.id
                    response_data_dict['state_name'] = city_obj.state.name
                    response = elasticsearch_client.index_data('master', 'city', id, response_data_dict)
                    if response:
                        # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                        print 'Succesfully Published single ' + master_type + ' Record FROM ELASTIC'
                        return True
                    else:
                        print 'Record NOT SENT TO ELASTIC - UNKNOWN'
                        return True
            elif action == "un-publish":
                response = elasticsearch_client.delete_document('master', 'city', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    print 'Succesfully Published single ' + master_type + ' Record'
                    return True
                else:
                    print 'Record NOT DELTEED FROM ELASTIC - UNKNOWN'
                    return False

        if master_type == "locality" and id:
            try:
                locality_obj = Locality.objects.get(id=id)
            except:
                print 'No object with this id found -RECORD NOT SENT TO ELASTIC'
                return False

            if action == "publish":
                if edit == 'Yes':
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
                            print 'Succesfully Published single ' + master_type + ' Record FROM ELASTIC'
                            return True
                        else:
                            print 'Record NOT SENT TO ELASTIC - UNKNOWN'
                            return True
                    else:
                        print "Could not publish as Record is Deactive IN CMS"
                else:
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
                        print 'Succesfully Published single ' + master_type + ' Record FROM ELASTIC'
                        return True
                    else:
                        print 'Record NOT SENT TO ELASTIC - UNKNOWN'
                        return True
            elif action == "un-publish":
                response = elasticsearch_client.delete_document('master', 'locality', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    print 'Succesfully Published single ' + master_type + ' Record'
                    return True
                else:
                    print 'Record NOT DELTEED FROM ELASTIC - UNKNOWN'
                    return False

        if master_type == "category" and id:
            try:
                category_obj = Category.objects.get(id=id)
            except:
                print 'No object with this id found -RECORD NOT SENT TO ELASTIC'
                return False

            if action == "publish":
                if edit == 'Yes':
                    if category_obj.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = category_obj.id
                        response_data_dict['name'] = category_obj.name
                        response = elasticsearch_client.index_data('master', 'category', id, response_data_dict)
                        response = elasticsearch_client.index_data('globalmaster', 'category', id, response_data_dict)
                        if response:
                            # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                            print 'Succesfully Published single ' + master_type + ' Record FROM ELASTIC'
                            return True
                        else:
                            print 'Record NOT SENT TO ELASTIC - UNKNOWN'
                            return True
                    else:
                        print "Could not publish as Record is Deactive IN CMS"
                else:
                    response_data_dict = {}
                    response_data_dict['id'] = category_obj.id
                    response_data_dict['name'] = category_obj.name
                    response = elasticsearch_client.index_data('master', 'category', id, response_data_dict)
                    response = elasticsearch_client.index_data('globalmaster', 'category', id, response_data_dict)
                    if response:
                        # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                        print 'Succesfully Published single ' + master_type + ' Record FROM ELASTIC'
                        return True
                    else:
                        print 'Record NOT SENT TO ELASTIC - UNKNOWN'
                        return True
            elif action == "un-publish":
                response = elasticsearch_client.delete_document('master', 'category', id)
                response = elasticsearch_client.delete_document('globalmaster', 'category', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    print 'Succesfully Published single ' + master_type + ' Record'
                    return True
                else:
                    print 'Record NOT DELTEED FROM ELASTIC - UNKNOWN'
                    return False

        if master_type == "speciality" and id:
            try:
                speciality_obj = Speciality.objects.get(id=id)
            except:
                print 'No object with this id found -RECORD NOT SENT TO ELASTIC'
                return False

            if action == "publish":
                if edit == 'Yes':
                    if speciality_obj.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = speciality_obj.id
                        response_data_dict['name'] = speciality_obj.name
                        response_data_dict['category_id'] = speciality_obj.category.id
                        response_data_dict['category_name'] = speciality_obj.category.name
                        response = elasticsearch_client.index_data('master', 'speciality', id, response_data_dict)
                        response = elasticsearch_client.index_data('globalmaster', 'speciality', id, response_data_dict)

                        if response:
                            # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                            print 'Succesfully Published single ' + master_type + ' Record FROM ELASTIC'
                            return True
                        else:
                            print 'Record NOT SENT TO ELASTIC - UNKNOWN'
                            return True
                    else:
                        print "Could not publish as Record is Deactive IN CMS"
                else:
                    response_data_dict = {}
                    response_data_dict['id'] = speciality_obj.id
                    response_data_dict['name'] = speciality_obj.name
                    response_data_dict['category_id'] = speciality_obj.category.id
                    response_data_dict['category_name'] = speciality_obj.category.name
                    response = elasticsearch_client.index_data('master', 'speciality', id, response_data_dict)
                    response = elasticsearch_client.index_data('globalmaster', 'speciality', id, response_data_dict)
                    if response:
                        # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                        print 'Succesfully Published single ' + master_type + ' Record FROM ELASTIC'
                        return True
                    else:
                        print 'Record NOT SENT TO ELASTIC - UNKNOWN'
                        return True
            elif action == "un-publish":
                response = elasticsearch_client.delete_document('master', 'speciality', id)
                response = elasticsearch_client.delete_document('globalmaster', 'speciality', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    print 'Succesfully Published single ' + master_type + ' Record'
                    return True
                else:
                    print 'Record NOT DELTEED FROM ELASTIC - UNKNOWN'
                    return False

        if master_type == "service_offered" and id:
            try:
                service_offered_obj = Service_Offred.objects.get(id=id)
            except:
                print 'No object with this id found -RECORD NOT SENT TO ELASTIC'
                return False

            if action == "publish":
                if edit == 'Yes':
                    if service_offered_obj.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = service_offered_obj.id
                        response_data_dict['name'] = service_offered_obj.name
                        response_data_dict['category_id'] = service_offered_obj.category.id
                        response_data_dict['category_name'] = service_offered_obj.category.name
                        response = elasticsearch_client.index_data('master', 'service_offered', id, response_data_dict)
                        response = elasticsearch_client.index_data('globalmaster', 'service_offered', id, response_data_dict)
                        if response:
                            # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                            print 'Succesfully Published single ' + master_type + ' Record FROM ELASTIC'
                            return True
                        else:
                            print 'Record NOT SENT TO ELASTIC - UNKNOWN'
                            return True
                    else:
                        print "Could not publish as Record is Deactive IN CMS"
                else:
                    response_data_dict = {}
                    response_data_dict['id'] = service_offered_obj.id
                    response_data_dict['name'] = service_offered_obj.name
                    response_data_dict['category_id'] = service_offered_obj.category.id
                    response_data_dict['category_name'] = service_offered_obj.category.name
                    response = elasticsearch_client.index_data('master', 'service_offered', id, response_data_dict)
                    response = elasticsearch_client.index_data('globalmaster', 'service_offered', id, response_data_dict)
                    if response:
                        # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                        print 'Succesfully Published single ' + master_type + ' Record FROM ELASTIC'
                        return True
                    else:
                        print 'Record NOT SENT TO ELASTIC - UNKNOWN'
                        return True
            elif action == "un-publish":
                response = elasticsearch_client.delete_document('master', 'service_offered', id)
                response = elasticsearch_client.delete_document('globalmaster', 'service_offered', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    print 'Succesfully Published single ' + master_type + ' Record'
                    return True
                else:
                    print 'Record NOT DELTEED FROM ELASTIC - UNKNOWN'
                    return False

        if master_type == "labservices" and id:
            try:
                labservices_obj = Lab_services_master.objects.get(id=id)
            except:
                print 'No object with this id found -RECORD NOT SENT TO ELASTIC'
                return False

            if action == "publish":
                if edit == 'Yes':
                    if labservices_obj.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = labservices_obj.id
                        response_data_dict['name'] = labservices_obj.name
                        response = elasticsearch_client.index_data('master', 'labservices', id, response_data_dict)
                        response = elasticsearch_client.index_data('globalmaster', 'labservices', id, response_data_dict)
                        if response:
                            # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                            print 'Succesfully Published single ' + master_type + ' Record FROM ELASTIC'
                            return True
                        else:
                            print 'Record NOT SENT TO ELASTIC - UNKNOWN'
                            return True
                    else:
                        print "Could not publish as Record is Deactive IN CMS"
                else:
                    response_data_dict = {}
                    response_data_dict['id'] = labservices_obj.id
                    response_data_dict['name'] = labservices_obj.name
                    response = elasticsearch_client.index_data('master', 'labservices', id, response_data_dict)
                    response = elasticsearch_client.index_data('globalmaster', 'labservices', id, response_data_dict)
                    if response:
                        # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                        print 'Succesfully Published single ' + master_type + ' Record FROM ELASTIC'
                        return True
                    else:
                        print 'Record NOT SENT TO ELASTIC - UNKNOWN'
                        return True
            elif action == "un-publish":
                response = elasticsearch_client.delete_document('master', 'labservices', id)
                response = elasticsearch_client.delete_document('globalmaster', 'labservices', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    print 'Succesfully Published single ' + master_type + ' Record'
                    return True
                else:
                    print 'Record NOT DELTEED FROM ELASTIC - UNKNOWN'
                    return False

        if master_type == "labtest" and id:
            try:
                labtest_obj = Lab_test_master.objects.get(id=id)
            except:
                print 'No object with this id found -RECORD NOT SENT TO ELASTIC'
                return False

            if action == "publish":
                if edit == 'Yes':
                    if labtest_obj.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = labtest_obj.id
                        response_data_dict['name'] = labtest_obj.name
                        response = elasticsearch_client.index_data('master', 'labtest', id, response_data_dict)
                        response = elasticsearch_client.index_data('globalmaster', 'labtest', id, response_data_dict)
                        if response:
                            # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                            print 'Succesfully Published single ' + master_type + ' Record FROM ELASTIC'
                            return True
                        else:
                            print 'Record NOT SENT TO ELASTIC - UNKNOWN'
                            return True
                    else:
                        print "Could not publish as Record is Deactive IN CMS"
                else:
                    response_data_dict = {}
                    response_data_dict['id'] = labtest_obj.id
                    response_data_dict['name'] = labtest_obj.name
                    response = elasticsearch_client.index_data('master', 'labtest', id, response_data_dict)
                    response = elasticsearch_client.index_data('globalmaster', 'labtest', id, response_data_dict)
                    if response:
                        # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                        print 'Succesfully Published single ' + master_type + ' Record FROM ELASTIC'
                        return True
                    else:
                        print 'Record NOT SENT TO ELASTIC - UNKNOWN'
                        return True
            elif action == "un-publish":
                response = elasticsearch_client.delete_document('master', 'labtest', id)
                response = elasticsearch_client.delete_document('globalmaster', 'labtest', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    print 'Succesfully Published single ' + master_type + ' Record'
                    return True
                else:
                    print 'Record NOT DELTEED FROM ELASTIC - UNKNOWN'
                    return False

        if master_type == "pharmacytype" and id:
            try:
                pharmacytype_obj = MedicalPharmacyStoreType.objects.get(id=id)
            except:
                print 'No object with this id found -RECORD NOT SENT TO ELASTIC'
                return False

            if action == "publish":
                if edit == 'Yes':
                    if pharmacytype_obj.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = pharmacytype_obj.id
                        response_data_dict['name'] = pharmacytype_obj.name
                        response = elasticsearch_client.index_data('master', 'pharmacytype', id, response_data_dict)
                        if response:
                            # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                            print 'Succesfully Published single ' + master_type + ' Record FROM ELASTIC'
                            return True
                        else:
                            print 'Record NOT SENT TO ELASTIC - UNKNOWN'
                            return True
                    else:
                        print "Could not publish as Record is Deactive IN CMS"
                else:
                    response_data_dict = {}
                    response_data_dict['id'] = pharmacytype_obj.id
                    response_data_dict['name'] = pharmacytype_obj.name
                    response = elasticsearch_client.index_data('master', 'pharmacytype', id, response_data_dict)
                    if response:
                        # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                        print 'Succesfully Published single ' + master_type + ' Record FROM ELASTIC'
                        return True
                    else:
                        print 'Record NOT SENT TO ELASTIC - UNKNOWN'
                        return True
            elif action == "un-publish":
                response = elasticsearch_client.delete_document('master', 'pharmacytype', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    print 'Succesfully Published single ' + master_type + ' Record'
                    return True
                else:
                    print 'Record NOT DELTEED FROM ELASTIC - UNKNOWN'
                    return False

        if master_type == "pharmacyServices" and id:
            try:
                pharmacyServices_obj = MedicalPharmacyStoreServices.objects.get(id=id)
            except:
                print 'No object with this id found -RECORD NOT SENT TO ELASTIC'
                return False
            if action == "publish":
                if edit == 'Yes':
                    if pharmacyServices_obj.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = pharmacyServices_obj.id
                        response_data_dict['name'] = pharmacyServices_obj.name
                        response = elasticsearch_client.index_data('master', 'pharmacyServices', id, response_data_dict)
                        if response:
                            # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                            print 'Succesfully Published single ' + master_type + ' Record FROM ELASTIC'
                            return True
                        else:
                            print 'Record NOT SENT TO ELASTIC - UNKNOWN'
                            return True
                    else:
                        print "Could not publish as Record is Deactive IN CMS"
                else:
                    response_data_dict = {}
                    response_data_dict['id'] = pharmacyServices_obj.id
                    response_data_dict['name'] = pharmacyServices_obj.name
                    response = elasticsearch_client.index_data('master', 'pharmacyServices', id, response_data_dict)
                    if response:
                        # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                        print 'Succesfully Published single ' + master_type + ' Record FROM ELASTIC'
                        return True
                    else:
                        print 'Record NOT SENT TO ELASTIC - UNKNOWN'
                        return True
            elif action == "un-publish":
                response = elasticsearch_client.delete_document('master', 'pharmacyServices', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    print 'Succesfully Published single ' + master_type + ' Record'
                    return True
                else:
                    print 'Record NOT DELTEED FROM ELASTIC - UNKNOWN'
                    return False
        if master_type == "facility" and id:
            try:
                facility_obj = Facility.objects.get(id=id)
            except:
                print 'No object with this id found -RECORD NOT SENT TO ELASTIC'
                return False

            if action == "publish":
                if edit == 'Yes':
                    if facility_obj.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = facility_obj.id
                        response_data_dict['name'] = facility_obj.name
                        response = elasticsearch_client.index_data('master', 'facility', id, response_data_dict)
                        response = elasticsearch_client.index_data('globalmaster', 'facility', id, response_data_dict)
                        if response:
                            # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                            print 'Succesfully Published single ' + master_type + ' Record FROM ELASTIC'
                            return True
                        else:
                            print 'Record NOT SENT TO ELASTIC - UNKNOWN'
                            return True
                    else:
                        print "Could not publish as Record is Deactive IN CMS"
                else:
                    response_data_dict = {}
                    response_data_dict['id'] = facility_obj.id
                    response_data_dict['name'] = facility_obj.name
                    response = elasticsearch_client.index_data('master', 'facility', id, response_data_dict)
                    response = elasticsearch_client.index_data('globalmaster', 'facility', id, response_data_dict)
                    if response:
                        # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                        print 'Succesfully Published single ' + master_type + ' Record FROM ELASTIC'
                        return True
                    else:
                        print 'Record NOT SENT TO ELASTIC - UNKNOWN'
                        return True
            elif action == "un-publish":
                response = elasticsearch_client.delete_document('master', 'facility', id)
                response = elasticsearch_client.delete_document('globalmaster', 'facility', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    print 'Succesfully Published single ' + master_type + ' Record'
                    return True
                else:
                    print 'Record NOT DELTEED FROM ELASTIC - UNKNOWN'
                    return False

        if master_type == "department" and id:
            try:
                department_obj = Department.objects.get(id=id)
            except:
                print 'No object with this id found -RECORD NOT SENT TO ELASTIC'
                return False

            if action == "publish":
                if edit == 'Yes':
                    if department_obj.delete == False:
                        response_data_dict = {}
                        response_data_dict['id'] = department_obj.id
                        response_data_dict['name'] = department_obj.name
                        response = elasticsearch_client.index_data('master', 'department', id, response_data_dict)
                        response = elasticsearch_client.index_data('globalmaster', 'department', id, response_data_dict)
                        if response:
                            # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                            print 'Succesfully Published single ' + master_type + ' Record FROM ELASTIC'
                            return True
                        else:
                            print 'Record NOT SENT TO ELASTIC - UNKNOWN'
                            return True
                    else:
                        print "Could not publish as Record is Deactive IN CMS"
                else:
                    response_data_dict = {}
                    response_data_dict['id'] = department_obj.id
                    response_data_dict['name'] = department_obj.name
                    response = elasticsearch_client.index_data('master', 'department', id, response_data_dict)
                    response = elasticsearch_client.index_data('globalmaster', 'department', id, response_data_dict)
                    if response:
                        # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                        print 'Succesfully Published single ' + master_type + ' Record FROM ELASTIC'
                        return True
                    else:
                        print 'Record NOT SENT TO ELASTIC - UNKNOWN'
                        return True
            elif action == "un-publish":
                response = elasticsearch_client.delete_document('master', 'department', id)
                response = elasticsearch_client.delete_document('globalmaster', 'department', id)
                if response:
                    # messages.success(request, 'Success Un-Published single '+master_type+' Record FROM ELASTIC')
                    print 'Succesfully Published single ' + master_type + ' Record'
                    return True
                else:
                    print 'Record NOT DELTEED FROM ELASTIC - UNKNOWN'
                    return False

        if master_type == 'countrymaster' and id:
            try:
                countrymaster=Countrymaster.objects.get(id=id)
            except:
                return False
            if action=="publish":
                response_data_dict = {}
                response_data_dict['id'] = countrymaster.id
                response_data_dict['name'] = countrymaster.name
                response = elasticsearch_client.index_data('nonsearchmaster', 'countrymaster', id, response_data_dict)
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    return True
                else:
                    return True
            if action=="unpublish":
                response_data_dict = {}
                response_data_dict['id'] = countrymaster.id
                response_data_dict['name'] = countrymaster.name
                response = elasticsearch_client.delete_document('nonsearchmaster', 'countrymaster', id)
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    return True
                else:
                    return True

        if master_type == 'statemaster' and id:
            try:
                statemaster=Statemaster.objects.get(id=id)
            except:
                return False
            if action == "publish":
                response_data_dict = {}
                response_data_dict['id'] = statemaster.id
                response_data_dict['name'] = statemaster.name
                response_data_dict['country_id'] = statemaster.countrymaster.id
                response = elasticsearch_client.index_data('nonsearchmaster', 'statemaster', id, response_data_dict)
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    return True
                else:
                    return True
            if action=="unpublish":
                response_data_dict = {}
                response_data_dict['id'] = statemaster.id
                response_data_dict['name'] = statemaster.name
                response_data_dict['country_id'] = statemaster.countrymaster.id
                response = elasticsearch_client.delete_document('nonsearchmaster', 'statemaster', id)
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    return True
                else:
                    return True

        if master_type == 'citymaster' and id:
            try:
                citymaster=Citymaster.objects.get(id=id)
            except:
                return False
            if action=="publish":
                response_data_dict = {}
                response_data_dict['id'] = citymaster.id
                response_data_dict['name'] = citymaster.name
                response_data_dict['state_id'] = citymaster.statemaster.id
                response = elasticsearch_client.index_data('nonsearchmaster', 'citymaster', id, response_data_dict)
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    print 1
                    return True
                else:
                    return True
            if action=="unpublish":
                response_data_dict = {}
                response_data_dict['id'] = citymaster.id
                response_data_dict['name'] = citymaster.name
                response_data_dict['state_id'] = citymaster.statemaster
                response = elasticsearch_client.delete_document('nonsearchmaster', 'citymaster', id)
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    return True
                else:
                    return True

        if master_type == 'localitymaster' and id:
            try:
                localitymaster=Localitymaster.objects.get(id=id,deletee=False)
            except:
                return False
            if action=="publish":
                response_data_dict = {}
                response_data_dict['id'] = localitymaster.id
                response_data_dict['name'] = localitymaster.name
                response_data_dict['city_id'] = localitymaster.citymaster.id
                response = elasticsearch_client.index_data('nonsearchmaster', 'localitymaster', id, response_data_dict)
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    return True
                else:
                    return True
            if action=="unpublish":
                response_data_dict = {}
                response_data_dict['id'] = localitymaster.id
                response_data_dict['name'] = localitymaster.name
                response_data_dict['city_id'] = localitymaster.citymaster
                response = elasticsearch_client.delete_document('nonsearchmaster', 'localitymaster', id)
                if response:
                    # messages.success(request, 'Succesfully Published single '+master_type+' Record')
                    return True
                else:
                    return True
        else:
            print 'MISSING INFORMATION - RECORD NOT SENT TO ELASTIC'
            return False

    except Exception as e:

        raise Http404

####################################################################
# Name - __live_doctor_data_creation                               #
# By - Nishank                                                     #
####################################################################
def __live_doctor_data_creation(id):
    response_data_dict = {}
    try:
        Doctor_obj = Live_Doctor.objects.get(id=id)
        asso_obj = Live_Doctor_Associated_Data.objects.get(doctor_id=id)
        if Doctor_obj:
            response_data_dict['name'] = 'Dr. '+Doctor_obj.firstName +' '+Doctor_obj.lastName
            emergency_data = {}
            if asso_obj.is_emergency != None :
                response_data_dict['is_emergency'] = asso_obj.is_emergency
            else:
                response_data_dict['is_emergency'] = False

            if asso_obj.is_emergency == True :
                emergency_data['fee'] = 0
                emergency_data['efee'] = asso_obj.emergency_fee
                if asso_obj.country != None:
                    emergency_data['country_id'] =  int(asso_obj.country_id)
                    emergency_data['country_name'] = asso_obj.country.name
                else:
                    emergency_data['country_id'] = 0
                    emergency_data['country_name'] = ''
                if asso_obj.state != None:
                    emergency_data['state_id'] = int(asso_obj.state_id)
                    emergency_data['state_name'] = asso_obj.state.name
                else:
                    emergency_data['state_id'] = 0
                    emergency_data['state_name'] = ''
                if asso_obj.city != None:
                    emergency_data['city_id'] = int(asso_obj.city_id)
                    emergency_data['city_name'] = asso_obj.city.name
                else:
                    emergency_data['city_id'] = 0
                    emergency_data['city_name'] = ''
                LLIST =[]
                locality_list = []
                if asso_obj.localities and asso_obj.localities != '' and asso_obj.localities != []:
                     LLIST = asso_obj.localities.split(',')
                     for i in LLIST:
                         loc = Locality.objects.get(id=int(i))
                         locality_list.append({'id':int(i),'name':loc.name})

                else:
                    locality_list = []
                emergency_data['locality_list'] = locality_list

            else:
                emergency_data['fee'] = 0
                emergency_data['efee'] = ''
                #emergency_data['is_emergency'] = False
                emergency_data['country_id'] = 0
                emergency_data['country_name'] = ''
                emergency_data['state_id'] = 0
                emergency_data['state_name'] = ''
                emergency_data['city_id'] = 0
                emergency_data['city_name'] = ''
                emergency_data['locality_list'] = []

            response_data_dict['emergency_data'] = emergency_data

            if asso_obj.talk_to_doc != None :
                response_data_dict['talk_to_doc'] = asso_obj.talk_to_doc
            else:
                response_data_dict['talk_to_doc'] = False

            if asso_obj.audio != None :
                response_data_dict['audio'] = asso_obj.audio
            else:
                response_data_dict['audio'] = False

            if asso_obj.video != None :
                response_data_dict['video'] = asso_obj.video
            else:
                response_data_dict['video'] = False

            if asso_obj.chat != None :
                response_data_dict['chat'] = asso_obj.chat
            else:
                response_data_dict['chat'] = False

            if asso_obj.talk_to_doc == True:
                response_data_dict['talk_fee'] = asso_obj.talk_fee
            else:
                response_data_dict['talk_fee'] = ''

            # response_data_dict['dob']= str(Doctor_obj.dob)   KEEP COMMENTED

            All_experience = Live_Doctor_Experience.objects.filter(doctor_id=Doctor_obj.id)
            sum_exp = 0
            lgest = 0
            slest = 300000
            for expe in All_experience:
                if expe.toYear != None :
                    if expe.toYear > lgest:
                        lgest = expe.toYear
                if expe.fromYear != None :
                    if expe.fromYear < slest:
                        slest = expe.fromYear
            sum_exp = lgest - slest
            if sum_exp < 1 or sum_exp == None or sum_exp == 0 or lgest == 0 or slest == 300000 :
                if asso_obj.totalexperience != None:
                    response_data_dict['doctor_experience_year'] = asso_obj.totalexperience + " Years"
                else:
                    response_data_dict['doctor_experience_year'] = "Not Available"
            else:
                response_data_dict['doctor_experience_year'] = str(sum_exp) + " Years"

            response_data_dict['unique_id'] = Doctor_obj.id
            #
            response_data_dict['image_url'] = Doctor_obj.profileImage


            try:
                response_data_dict['zone'] = Doctor_obj.zone.name
                if response_data_dict['zone']:
                    response_data_dict['zone'].strip()
            except:
                response_data_dict['zone'] =''

            try:
                response_data_dict['zone_location'] = Doctor_obj.zone_location.name
                if response_data_dict['zone_location']:
                    response_data_dict['zone_location'].strip()
            except:
                response_data_dict['zone_location'] = ''

            try:
                Category_obj = Category.objects.get(id = Doctor_obj.category)
                response_data_dict['category_id'] = Category_obj.id

                response_data_dict['category'] = Category_obj.name
                if response_data_dict['category']:
                    response_data_dict['category'].strip()
            except:
                response_data_dict['category_id'] = 0
                response_data_dict['category'] = ''

            response_data_dict['mobile_no'] = Doctor_obj.mobileNo
            if response_data_dict['mobile_no']:
                response_data_dict['mobile_no'].strip()

            response_data_dict['phone'] = Doctor_obj.phoneNo
            if response_data_dict['phone']:
                response_data_dict['phone'].strip()

            if Doctor_obj.skypeId != None:
                response_data_dict['skype_id'] = Doctor_obj.skypeId
            else:
                response_data_dict['skype_id'] = ''
            if response_data_dict['skype_id']:
                response_data_dict['skype_id'].strip()

            response_data_dict['email'] = Doctor_obj.email
            if response_data_dict['email']:
                response_data_dict['email'].strip()

            response_data_dict['registration_data'] = Doctor_obj.mciRegistrationNo.strip() +' '+ Doctor_obj.registrationBoard.strip() +' '+ str(Doctor_obj.registrationYear)

            response_data_dict['mci'] = Doctor_obj.mciRegistrationNo

            response_data_dict['secondary_email'] = Doctor_obj.alternateEmail
            if response_data_dict['secondary_email']:
                response_data_dict['secondary_email'].strip()


            #response_data_dict['qualification_data'] = asso_obj.qualification_data
            ttttemp =''
            edu_list = Live_Doctor_Education.objects.filter(doctor_id = Doctor_obj.id)
            count = 0
            for i in edu_list:
                if i.degree != None and i.degree != '' and i.degree != []:
                    count += 1
                    if count == 1:
                        ttttemp =  ttttemp + i.degree
                    else:
                        ttttemp = ttttemp +','+ i.degree.strip()
            response_data_dict['qualification_data'] = ttttemp

            if Doctor_obj.gender.strip().lower() == 'male':
                response_data_dict['male_doctor'] = "True"
                response_data_dict['female_doctor'] = "False"
            else:
                response_data_dict['male_doctor'] = "False"
                response_data_dict['female_doctor'] = "True"

            # if Doctor_obj.speciality:
            #     response_data_dict['speciality'] = Doctor_obj.speciality
            # else:
            #     response_data_dict['speciality'] = []
            #
            # if Doctor_obj.serviceOffered:
            #     response_data_dict['service'] = Doctor_obj.serviceOffered
            # else:
            #     response_data_dict['service'] = []


            if Doctor_obj.new_speciality_final != None and Doctor_obj.new_speciality_final != []:
                response_data_dict['speciality'] = Doctor_obj.new_speciality_final
            else:
                response_data_dict['speciality'] = []

            if Doctor_obj.new_service_offered_final != None and Doctor_obj.new_service_offered_final != []:
                response_data_dict['service'] = Doctor_obj.new_service_offered_final
            else:
                response_data_dict['service'] = []

            # # #******************************* Doctor membership *********************#
            Membership_list = []
            RewardRecognisation_list = []
            Doctor_Education_list = []
            Doctor_Experience_list = []

            Membership_obj = Live_Doctor_Membership.objects.filter(doctor_id=Doctor_obj.id)
            for membership in Membership_obj:
                 Membership_list.append(membership.name)
            response_data_dict['membership'] = Membership_list
            #
            # # #*************************************** Reward and recognisation ********#
            RewardRecognisation_obj = Live_Doctor_Rewardrecog.objects.filter(doctor_id=Doctor_obj.id)
            for reward in RewardRecognisation_obj:
                 row =''
                 if reward.name != None  and reward.name != '' and reward.name != ' ' :
                     if reward.year != None :
                         row = str(reward.year) +" - "+ reward.name.strip()
                     else:
                         row = reward.name.strip()
                 else:
                     row = ''
                 if row.strip() != '' and  row != ' ' and row != None:
                    RewardRecognisation_list.append(row)
            response_data_dict['rewardrecognisation'] = RewardRecognisation_list
            #
            # # #************************** Education ***************************#
            Doctor_Education_obj = Live_Doctor_Education.objects.filter(doctor_id=Doctor_obj.id)
            for doctor_edu in Doctor_Education_obj:
                row = ''
                if doctor_edu.degree == None or doctor_edu.degree == ' ' or doctor_edu.degree == '' or doctor_edu.degree == 'None' :
                    ldocdegree = ''
                    edu_dash = ''
                else:
                    ldocdegree = doctor_edu.degree.strip()
                    edu_dash = '-'
                if doctor_edu.college == None or doctor_edu.college == ' ' or doctor_edu.college == '' or doctor_edu.college == 'None':
                    ldoccollege = ''
                    edu_dash = ''
                else:
                    ldoccollege = doctor_edu.college.strip()
                    edu_dash = '-'
                if doctor_edu.year == None :
                    ldocyear = ''
                    eduspace = ''
                else:
                    ldocyear = doctor_edu.year
                    eduspace = ' '
                row = str(ldocyear) + eduspace + ldocdegree + edu_dash + ldoccollege
                Doctor_Education_list.append(row)
            response_data_dict['education'] = Doctor_Education_list
            #
            # # #******************************** Experience**************************** #
            All_experience = Live_Doctor_Experience.objects.filter(doctor_id=Doctor_obj.id)
            for expe in All_experience:
                temp_str = ''
                ename = efY = etY = edesign = ecity  = ''

                if expe.name != None and expe.name.strip() != 'None':
                    ename = expe.name.strip()
                    var_at = ' at '
                else:
                    ename = ''
                    var_at = ''

                if expe.fromYear != None :
                    efY = str(expe.fromYear)
                    var_dash = '-'
                else:
                    efY = ''
                    var_dash = ''

                if expe.toYear != None :
                    etY = str(expe.toYear)
                if expe.designation != None and expe.designation.strip() != 'None':
                    edesign = expe.designation.strip()

                if expe.city != None and expe.city.strip() != 'None':
                    ecity = expe.city.strip()
                    var_comma = ' , '
                else:
                    ecity = ''
                    var_comma = ''
                if ename == '' and efY == '' and etY == '' and edesign == '' and ecity == '':
                    pass
                else:
                    temp_str =  efY + var_dash + etY + ' ' + edesign + var_at + ename + var_comma + ecity
                    temp_str = temp_str.strip()
                if temp_str.strip() != '-' and temp_str != ' ' and temp_str.strip() != ''  and temp_str != None:
                    Doctor_Experience_list.append(temp_str)
            response_data_dict['experience'] = Doctor_Experience_list
            ename = efY = etY = edesign = ecity = ''



            # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            All_doc_schedule = Live_Doctor_Commonworkschedule.objects.filter(Q(doctor_id=Doctor_obj.id),~Q(status='delete'))


            attach_org_list = []
            for schedule in All_doc_schedule:
                tim_type=schedule.time_type
                attach_org_dict = {}
                attach_org_dict['consultancy_fee'] = 0
                try:
                    if schedule.consultingCharge:
                                attach_org_dict['consultancy_fee'] = int(schedule.consultingCharge)
                except:
                    attach_org_dict['consultancy_fee'] = 0

                org_oobj = OrganisationName.objects.get(id = int(schedule.clinic_id) )
                attach_org_dict['did'] = schedule.did
                attach_org_dict['extension'] = schedule.extension
                attach_org_dict['appointmentMinute'] = schedule.appointmentMinute
                attach_org_dict['email_attach'] = None
                attach_org_dict['telephone_attach'] = None
                attach_org_dict['name'] = org_oobj.name
                attach_org_dict['is_clinic'] = org_oobj.is_clinic
                attach_org_dict['is_hospital'] = org_oobj.is_hospital
                attach_org_dict['street'] = org_oobj.street
                attach_org_dict['organisation_id'] = org_oobj.id
                attach_org_dict['locality_id'] = org_oobj.locality.id
                attach_org_dict['locality_name'] = org_oobj.locality.name
                attach_org_dict['city_id'] = org_oobj.city.id
                attach_org_dict['city_name'] = org_oobj.city.name
                attach_org_dict['state_id'] = org_oobj.state.id
                attach_org_dict['state_name'] = org_oobj.state.name
                attach_org_dict['country_id'] = org_oobj.country.id
                attach_org_dict['country_name'] = org_oobj.country.name
                attach_org_dict['phone'] = org_oobj.phone
                attach_org_dict['mobile_no'] = org_oobj.mobile_no
                attach_org_dict['fax'] = org_oobj.fax
                attach_org_dict['emergency_no'] = org_oobj.emergency_no
                attach_org_dict['email'] = org_oobj.email
                attach_org_dict['pincode'] = org_oobj.pincode

                attach_org_dict['location'] = {
                        "lat": 0,
                        "long": 0
                    }
                if org_oobj.latitude and org_oobj.longitude:
                    attach_org_dict['location'] = {
                        "lat": float(org_oobj.latitude),
                        "long": float(org_oobj.longitude)
                                                  }
                # ***************************** schedule in organisation ************ #
                #~~Schedule_obj = Schedule.objects.get(doctor_id=Doctor_obj.id,organisation_id=org_oobj.id)
                by_appointment = False

                if schedule:
                    if by_appointment == False:
                        try:
                            #~~schedule_data = Schedule_obj.schedule_data
                            #Done
                            aa = schedule.timing
                            attach_org_dict['timing'] = schedule.timing
                            # Done
                            attach_org_dict['timing_str'] = []
                            #Done
                            new_lllist =  []
                            oolist = []
                            for oo in schedule.time_object:
                                oo['id'] = ''
                                oolist.append(oo)
                            new_lllist = []
                            for i in oolist:
                                if i['from_day'].lower() == 'mon':
                                    new_lllist.append(i)

                            for i in oolist:
                                if i['from_day'].lower() == 'tue':
                                    new_lllist.append(i)

                            for i in oolist:
                                if i['from_day'].lower() == 'wed':
                                    new_lllist.append(i)

                            for i in oolist:
                                if i['from_day'].lower() == 'thu':
                                    new_lllist.append(i)

                            for i in oolist:
                                if i['from_day'].lower() == 'fri':
                                    new_lllist.append(i)

                            for i in oolist:
                                if i['from_day'].lower() == 'sat':
                                    new_lllist.append(i)

                            for i in oolist:
                                if i['from_day'].lower() == 'sun':
                                    new_lllist.append(i)

                            if tim_type == 'single' or tim_type =='single_double':
                                tt=new_lllist
                                fflag=0
                                new_tt={}
                                globalflaf=0
                                o_tt=[]
                                u={}
                                tueflag=0
                                wedflag=0
                                thuflag=0
                                friflag=0
                                satflag=0
                                sunflag=0
                                for t in tt:
                                    u=t
                                    if t['from_day']=='mon':
                                        globalflag=1
                                        new_tt.update(u)
                                        fflag=1
                                        continue

                                    if t['from_day']=='tue' and tueflag==0:
                                        tueflag=1
                                        globalflag = 1
                                        if fflag==1:
                                            new_tt['to_day']='tue'
                                            continue
                                        else:
                                            if new_tt != {} :
                                                o_tt.append(new_tt)
                                            new_tt={}
                                            new_tt.update(u)
                                            fflag=1
                                            continue
                                    elif tueflag==0:
                                        tueflag=1
                                        fflag = 0

                                    if t['from_day']=='wed'and wedflag==0:
                                        wedflag=1
                                        globalflag = 1
                                        if fflag==1:
                                            new_tt['to_day']='wed'
                                            continue
                                        else:
                                            if new_tt != {}:
                                                o_tt.append(new_tt)
                                            new_tt ={}
                                            new_tt.update(u)
                                            fflag = 1
                                            continue
                                    elif wedflag==0:
                                        wedflag=1
                                        fflag = 0


                                    if t['from_day']=='thu' and thuflag==0:
                                        thuflag=1
                                        globalflag = 1
                                        if fflag==1:
                                            new_tt['to_day']='thu'
                                            continue
                                        else:
                                            if new_tt != {}:
                                                o_tt.append(new_tt)
                                            new_tt = {}
                                            new_tt.update(u)
                                            fflag = 1
                                            continue
                                    elif thuflag==0:
                                        thuflag=1
                                        fflag = 0


                                    if t['from_day']=='fri' and friflag==0:
                                        friflag=1
                                        globalflag = 1
                                        if fflag == 1:
                                            new_tt['to_day'] = 'fri'
                                            continue
                                        else:
                                            if new_tt != {}:
                                                o_tt.append(new_tt)
                                            new_tt = {}
                                            new_tt.update(u)
                                            fflag = 1
                                            continue
                                    elif friflag==0:
                                        friflag=1
                                        fflag = 0


                                    if t['from_day']=='sat' and satflag==0:
                                        satflag=1
                                        globalflag = 1
                                        if fflag == 1:
                                            new_tt['to_day'] = 'sat'
                                            continue
                                        else:
                                            if new_tt != {}:
                                                o_tt.append(new_tt)
                                            new_tt = {}
                                            new_tt.update(u)
                                            fflag = 1
                                            continue
                                    elif satflag==0:
                                        satflag=1
                                        fflag = 0


                                    if t['from_day']=='sun' and sunflag==0:
                                        sunflag=1
                                        globalflag = 1
                                        if fflag == 1:
                                            new_tt['to_day'] = 'sun'
                                            continue
                                        else:
                                            if new_tt != {}:
                                                o_tt.append(new_tt)
                                            new_tt = {}
                                            new_tt.update(u)
                                            fflag = 1
                                            continue
                                    elif sunflag==0:
                                        sunflag=1
                                        fflag = 0
                                o_tt.append(new_tt)
                                attach_org_dict['time_object'] = o_tt
                                attach_org_dict['by_appointment'] = False


                            else:
                                attach_org_dict['time_object'] = new_lllist
                                attach_org_dict['by_appointment'] = False

                        except Exception as e:
                            attach_org_dict['timing'] = []
                            attach_org_dict['timing_str'] = []
                            attach_org_dict['time_object'] = []
                            attach_org_dict['by_appointment'] = False
                    else:
                        attach_org_dict['timing'] = []
                        attach_org_dict['timing_str'] = []
                        attach_org_dict['time_object'] = []
                        attach_org_dict['by_appointment'] = False
                else:
                    attach_org_dict['timing'] = []
                    attach_org_dict['timing_str'] = []
                    attach_org_dict['time_object'] = []
                    attach_org_dict['by_appointment'] = False
                attach_org_list.append(attach_org_dict)
            response_data_dict['attach_organisation'] = attach_org_list

            from .views import hostname,port
            hostport = hostname+port
            gallery_images = []
            gallery_obj_list = Live_Doctor_Imagegallery.objects.filter(doctor_id=Doctor_obj.id)
            if list(gallery_obj_list) != []:
                for imobj in gallery_obj_list:
                    tempurl = ''
                    tempurl = tempurl + hostport + imobj.name.strip()
                    gallery_images.append(tempurl)

            response_data_dict['gallery_images'] = gallery_images
            response_data_dict['activationStatus'] = Doctor_obj.activationStatus
            response_data_dict['did'] = Doctor_obj.did
            response_data_dict['extension'] = Doctor_obj.extension
            if not Doctor_obj.qualification_points:
                qp = 0.0
            else:
                qp = Doctor_obj.qualification_points
            if not Doctor_obj.experience_points:
                ep = 0.0
            else:
                ep = Doctor_obj.experience_points
            if not Doctor_obj.emergency_points:
                emp = 0.0
            else:
                emp = Doctor_obj.emergency_points
            response_data_dict['points'] = qp + ep + emp

            #response_data_dict['points'] = Doctor_obj.qualification_points + Doctor_obj.experience_points + Doctor_obj.emergency_points
            # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

            # # ******************************** Attached Organisation *************************#
            # AttachWithDoctor_obj = AttachWithDoctor.objects.filter(doctor_id=Doctor_obj.id)
            # attach_org_list = []
            # for attach_with_doctor in AttachWithDoctor_obj:
            #     attach_org_dict = {}
            #     attach_org_dict['consultancy_fee'] = 0
            #     try:
            #         if attach_with_doctor.consultancy_fee:
            #             attach_org_dict['consultancy_fee'] = int(attach_with_doctor.consultancy_fee)
            #     except:
            #         attach_org_dict['consultancy_fee'] = 0
            #     attach_org_dict['email_attach'] = (attach_with_doctor.email_attach)
            #     attach_org_dict['telephone_attach'] = (attach_with_doctor.telephone_attach)
            #     attach_org_dict['name'] = attach_with_doctor.organisation.name
            #     attach_org_dict['is_clinic'] = attach_with_doctor.organisation.is_clinic
            #     attach_org_dict['is_hospital'] = attach_with_doctor.organisation.is_hospital
            #     attach_org_dict['street'] = attach_with_doctor.organisation.street
            #     attach_org_dict['organisation_id'] = attach_with_doctor.organisation.id
            #     attach_org_dict['locality_id'] = attach_with_doctor.organisation.locality.id
            #     attach_org_dict['locality_name'] = attach_with_doctor.organisation.locality.name
            #     attach_org_dict['city_id'] = attach_with_doctor.organisation.city.id
            #     attach_org_dict['city_name'] = attach_with_doctor.organisation.city.name
            #     attach_org_dict['state_id'] = attach_with_doctor.organisation.state.id
            #     attach_org_dict['state_name'] = attach_with_doctor.organisation.state.name
            #     attach_org_dict['country_id'] = attach_with_doctor.organisation.country.id
            #     attach_org_dict['country_name'] = attach_with_doctor.organisation.country.name
            #     attach_org_dict['phone'] = attach_with_doctor.organisation.phone
            #     attach_org_dict['mobile_no'] = attach_with_doctor.organisation.mobile_no
            #     attach_org_dict['fax'] = attach_with_doctor.organisation.fax
            #     attach_org_dict['emergency_no'] = attach_with_doctor.organisation.emergency_no
            #     attach_org_dict['email'] = attach_with_doctor.organisation.email
            #     attach_org_dict['pincode'] = attach_with_doctor.organisation.pincode
            #
            #     attach_org_dict['location'] = {
            #         "lat": 0,
            #         "long": 0
            #     }
            #     if attach_with_doctor.organisation.latitude and attach_with_doctor.organisation.longitude:
            #         attach_org_dict['location'] = {
            #             "lat": float(attach_with_doctor.organisation.latitude),
            #             "long": float(attach_with_doctor.organisation.longitude)
            #         }
            #
            #     # ***************************** schedule in organisation *************#
            #     Schedule_obj = Schedule.objects.get(doctor_id=Doctor_obj.id,
            #                                         organisation_id=attach_with_doctor.organisation_id)
            #     if Schedule_obj:
            #         if Schedule_obj.by_appointment == False:
            #             try:
            #                 schedule_data = Schedule_obj.schedule_data
            #                 attach_org_dict['timing'] = convert_time_array(schedule_data)
            #                 attach_org_dict['timing_str'] = convert_time_str_array(schedule_data)
            #                 attach_org_dict['time_object'] = Schedule_obj.schedule_data
            #                 attach_org_dict['by_appointment'] = False
            #
            #             except:
            #                 attach_org_dict['timing'] = []
            #                 attach_org_dict['timing_str'] = []
            #                 attach_org_dict['time_object'] = []
            #                 attach_org_dict['by_appointment'] = False
            #         else:
            #             attach_org_dict['timing'] = []
            #             attach_org_dict['timing_str'] = []
            #             attach_org_dict['time_object'] = []
            #             attach_org_dict['by_appointment'] = True
            #     else:
            #         attach_org_dict['timing'] = []
            #         attach_org_dict['timing_str'] = []
            #         attach_org_dict['time_object'] = []
            #         attach_org_dict['by_appointment'] = False
            #
            #     attach_org_list.append(attach_org_dict)
            # response_data_dict['attach_organisation'] = attach_org_list
    except Exception as e:
        print
        '%s (%s)' % (e.message, type(e))
    return response_data_dict



####################################################################
# Name - _news_feed_data_creation                                  #
# Owner - jitendra dixittesting:                                   #
# Review by -                                                      #
#                                                                  #
####################################################################

def _docs_feed_data_creation(id):
    response_data_dict = {}
    try:
        docsfeed_obj_data = Doctorsfeed.objects.get(id=id)
        # global_obj_data.update(publish_data=True)
        if docsfeed_obj_data:
            news_type_name = ''
            if docsfeed_obj_data.news_type_id == 1:
                news_type_name = 'Global News Feed'
            elif docsfeed_obj_data.news_type_id == 2:
                news_type_name = 'Wellness News Feed'
            elif docsfeed_obj_data.news_type_id == 3:
                news_type_name = 'Health News Feed'

            response_data_dict['id'] = docsfeed_obj_data.id
            response_data_dict['title'] = docsfeed_obj_data.topic_title.strip()
            #response_data_dict['doctors_category'] = global_obj_data.doctors_category.strip()
            response_data_dict['image_file_name'] = docsfeed_obj_data.newsfeed_image_file_name.strip()

            # try:
            #     doctors_category = docsfeed_obj_data.doctors_category.strip()
            #     cat_list = []
            #     if doctors_category != '' and doctors_category != ' ' and doctors_category != []:
            #         temp = doctors_category.split(',')
            #         for i in temp:
            #             cat_obj = Category.objects.get(id=int(i))
            #             cat_list.append({'id': int(i), 'name': cat_obj.name})
            #     else:
            #         cat_list = []
            #     response_data_dict['doctors_category'] = cat_list
            # except:
            #     response_data_dict['doctors_category'] = []

            response_data_dict['related_topics'] = []
            if docsfeed_obj_data.related_topics:
                fnlist = []
                listls = docsfeed_obj_data.related_topics.split(',')
                objs = Doctorsfeed.objects.filter(is_disable=False, blocked_news=False,
                                               news_type_id=docsfeed_obj_data.news_type_id)
                for i in objs:
                    if str(i.id) in listls:
                        if i.publish_date:
                            attach_publish_date = str(i.publish_date)
                            attach_publish_date = attach_publish_date[:10]
                        else:
                            import datetime
                            attach_publish_date = str(datetime.date.today())
                            attach_publish_date = attach_publish_date[:10]

                        fnlist.append({'id': i.id, 'title': i.topic_title, 'image': i.newsfeed_image_file_name,
                                       'publish_date': attach_publish_date})
                        response_data_dict['related_topics'] = fnlist

            else:
                response_data_dict['related_topics'] = []

            response_data_dict['type_id'] = docsfeed_obj_data.news_type_id
            response_data_dict['type'] = docsfeed_obj_data.news_type.name
            if docsfeed_obj_data.publish_date:
                response_data_dict['publish_date'] = str(docsfeed_obj_data.publish_date)
                response_data_dict['publish_date'] = response_data_dict['publish_date'][:10]
            else:
                import datetime
                response_data_dict['publish_date'] = str(datetime.date.today())
                response_data_dict['publish_date'] = response_data_dict['publish_date'][:10]
            if docsfeed_obj_data.small_description:
                response_data_dict['small_description'] = docsfeed_obj_data.small_description.strip()
            else:
                response_data_dict['small_description'] = ""
            response_data_dict['html'] = docsfeed_obj_data.newsfeed_html_refined.strip()
            response_data_dict['tag_string'] = docsfeed_obj_data.tag_string.strip()

            if docsfeed_obj_data.page_title != None and docsfeed_obj_data.page_title.strip() != 'None':
                response_data_dict['page_title'] = docsfeed_obj_data.page_title.strip()
            else:
                response_data_dict['page_title'] = ''

            if docsfeed_obj_data.page_keywords != None and  docsfeed_obj_data.page_keywords.strip() != 'None':
                response_data_dict['page_keywords'] = docsfeed_obj_data.page_keywords.strip()
            else:
                response_data_dict['page_keywords'] = ''

            if docsfeed_obj_data.page_description != None and docsfeed_obj_data.page_description.strip() != 'None':
                response_data_dict['page_description'] = docsfeed_obj_data.page_description.strip()
            else:
                response_data_dict['page_description'] = ''


    except Exception as e:
        print
        '%s (%s)' % (e.message, type(e))
    return response_data_dict


####################################################################
# Name - publish unpublish doctors feed                             #
# BY - Ashutosh kesharvani                                          #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def publish_unpublish_docsfeed(request):
    try:
        ids = request.POST.get("checked_values")
        type = request.POST.get("type")
        if type == 'publish':
            response = data_publisher('docsfeed', ids)
            if response == True:
                print response
        if type == 'un-publish':
            response = data_un_publisher('docsfeed',ids)
            if response == True:
                print response
        print 1
    except Exception as e:
        print e
