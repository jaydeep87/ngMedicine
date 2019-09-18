from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from hfu_cms.models import Doctor,Doctor_Education,RewardRecognisation,Membership,Doctor_Experience, \
AttachWithDoctor,Schedule

from remote.serializers import RemoteDoctorSerializer,RemoteDoctorEducationSerializer,RemoteRewardRecognisationSerializer, \
RemoteMembershipSerializer,RemoteDoctorExperienceSerializer,RemoteAttachWithDoctorSerializer,RemoteScheduleSerializer

import uuid

#-------------Doctor remote Views------------------------

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def doctor_list(request):
    """
    List all doctors, or create a new snippet.
    """
    if request.method == 'GET':
        docs = Doctor.objects.all()
        serializer = RemoteDoctorSerializer(docs, many=True)
        return JSONResponse(serializer.data)
    """
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RemoteDoctorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)        
    """

@csrf_exempt
def doctor_detail(request, pk):
    """
    Retrieve, update or delete a doctor.
    """
    try:
        doc = Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RemoteDoctorSerializer(doc)
        return JSONResponse(serializer.data)

    #elif request.method == 'PUT':
    #    data = JSONParser().parse(request)
    #    serializer = RemoteDoctorSerializer(doc, data=data)
    #    if serializer.is_valid():
    #        serializer.save()
    #        return JSONResponse(serializer.data)
    #    return JSONResponse(serializer.errors, status=400)

    #elif request.method == 'DELETE':
    #    doc.delete()
    #    return HttpResponse(status=204)



@csrf_exempt
def doctor_add(request):
    """
    Add a doctor.

    if request.method == 'PUT':
        print "request =", request
        data = JSONParser().parse(request)
        serializer = RemoteDoctorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    """
    if request.method == 'PUT':
        print "request =", request
        data = JSONParser().parse(request)
        serializer = RemoteDoctorSerializer(data=data)
        if serializer.is_valid():
            doc = serializer.save()
            doc.stage_id =1
            admin_list = User.objects.filter(is_superuser=True)
            doc.unique_id=uuid.uuid4()
            doc.save()
            print admin_list
            print doc, type(doc)
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

#--------------Doctor Education remote Views-----------------------

@csrf_exempt
def doctor_education_list(request):

    if request.method == 'GET':
        docs = Doctor_Education.objects.all()
        serializer = RemoteDoctorEducationSerializer(docs, many=True)
        return JSONResponse(serializer.data)
    """
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RemoteDoctorEducationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
    """

@csrf_exempt
def doctor_education_detail(request, pk):

    try:
        doc = Doctor_Education.objects.get(pk=pk)
    except Doctor_Education.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RemoteDoctorEducationSerializer(doc)
        return JSONResponse(serializer.data)


@csrf_exempt
def doctor_education_add(request):

    if request.method == 'PUT':
        print "request =", request
        data = JSONParser().parse(request)
        serializer = RemoteDoctorEducationSerializer(data=data)
        if serializer.is_valid():
            doc_education = serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)


#--------------RewardRecognisation remote Views-----------------------

@csrf_exempt
def doctor_reward_recognition_list(request):

    if request.method == 'GET':
        docs = RewardRecognisation.objects.all()
        serializer = RemoteRewardRecognisationSerializer(docs, many=True)
        return JSONResponse(serializer.data)
    """
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RemoteRewardRecognisationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
    """

@csrf_exempt
def doctor_reward_recognition_detail(request, pk):

    try:
        reward_recognisation = RewardRecognisation.objects.get(pk=pk)
    except RewardRecognisation.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RemoteRewardRecognisationSerializer(reward_recognisation)
        return JSONResponse(serializer.data)


@csrf_exempt
def doctor_reward_recognition_add(request):

    if request.method == 'PUT':
        print "request =", request
        data = JSONParser().parse(request)
        serializer = RemoteRewardRecognisationSerializer(data=data)
        if serializer.is_valid():
            reward_recognisation = serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

#--------------Membership remote Views-----------------------

@csrf_exempt
def doctor_membership_list(request):

    if request.method == 'GET':
        docs = Membership.objects.all()
        serializer = RemoteMembershipSerializer(docs, many=True)
        return JSONResponse(serializer.data)
    """
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RemoteMembershipSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
    """

@csrf_exempt
def doctor_membership_detail(request, pk):

    try:
        membership = Membership.objects.get(pk=pk)
    except Membership.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RemoteMembershipSerializer(membership)
        return JSONResponse(serializer.data)


@csrf_exempt
def doctor_membership_add(request):

    if request.method == 'PUT':
        print "request =", request
        data = JSONParser().parse(request)
        serializer = RemoteMembershipSerializer(data=data)
        if serializer.is_valid():
            reward_recognisation = serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)


#--------------Doctor Experience remote Views-----------------------

@csrf_exempt
def doctor_experience_list(request):

    if request.method == 'GET':
        docs = Doctor_Experience.objects.all()
        serializer = RemoteDoctorExperienceSerializer(docs, many=True)
        return JSONResponse(serializer.data)
    """
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RemoteDoctorExperienceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
    """

@csrf_exempt
def doctor_experience_detail(request, pk):

    try:
        docex = Doctor_Experience.objects.get(pk=pk)
    except Doctor_Experience.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RemoteDoctorExperienceSerializer(docex)
        return JSONResponse(serializer.data)


@csrf_exempt
def doctor_experience_add(request):

    if request.method == 'PUT':
        print "request =", request
        data = JSONParser().parse(request)
        serializer = RemoteDoctorExperienceSerializer(data=data)
        if serializer.is_valid():
            doc_education = serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)


#--------------Doctor AttachWithDoctor remote Views-----------------------

@csrf_exempt
def attachwithdoctor_list(request):

    if request.method == 'GET':
        docs = AttachWithDoctor.objects.all()
        serializer = RemoteAttachWithDoctorSerializer(docs, many=True)
        return JSONResponse(serializer.data)
    """
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RemoteAttachWithDoctorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
    """

@csrf_exempt
def attachwithdoctor_detail(request, pk):

    try:
        attach = AttachWithDoctor.objects.get(pk=pk)
    except AttachWithDoctor.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RemoteAttachWithDoctorSerializer(attach)
        return JSONResponse(serializer.data)


@csrf_exempt
def attachwithdoctor_add(request):

    if request.method == 'PUT':
        print "request =", request
        data = JSONParser().parse(request)
        serializer = RemoteAttachWithDoctorSerializer(data=data)
        if serializer.is_valid():
            doc_education = serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)


#-------------Schedule remote Views------------------------

class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def schedule_list(request):

    if request.method == 'GET':
        docs = Schedule.objects.all()
        serializer = RemoteScheduleSerializer(docs, many=True)
        return JSONResponse(serializer.data)


@csrf_exempt
def schedule_detail(request, pk):
    """
    Retrieve, update or delete a doctor.
    """
    try:
        doc = Schedule.objects.get(pk=pk)
    except Schedule.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RemoteScheduleSerializer(doc)
        return JSONResponse(serializer.data)


@csrf_exempt
def schedule_add(request):
    try:
        data = JSONParser().parse(request)
        doctor = data['doctor']
        organisation =  data['organisation']
        schedule_list = data['schedule_data']

        if request.method == 'PUT':

            attach_list = AttachWithDoctor.objects.filter(doctor=doctor, organisation=organisation)
            if len(attach_list) > 0 :
                schedule_obj_list = Schedule.objects.filter(doctor=doctor, organisation=organisation)
                if len(schedule_obj_list) > 0 :
                    schedule_obj_list.update(schedule_data=schedule_list )
                    return JSONResponse("Successfully Updated Schedule", status=200)

                else:
                    new_schedule =Schedule(doctor=doctor, organisation=organisation,schedule_data=schedule_list )
                    new_schedule.save()
                    return JSONResponse("Successfully Created Schedule", status=200)



            else:
                return JSONResponse("Organization not attached with Doctor", status=400)

    except Exception as e:
        print e
        raise Http404
