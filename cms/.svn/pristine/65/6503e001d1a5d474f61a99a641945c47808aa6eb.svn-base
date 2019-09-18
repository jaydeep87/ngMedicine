from rest_framework import serializers
from hfu_cms.models import Doctor,Doctor_Education,RewardRecognisation,Membership,Doctor_Experience,AttachWithDoctor , \
Schedule


class RemoteDoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        #Fields not in json
        #current_user, previous_user,free_text, is_disable, id, resource_validate,stage,unique_id
        fields = ('name','image_url','category','zone','zone_location','speciality','service_offered','dob','mobile_no','phone',
                  'skype_id','email','secondary_email','doctor_experience_year','qualification_data','registration_data','male_doctor',
                  'female_doctor')

class RemoteDoctorEducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor_Education
        #Fields not in json
        #id,
        fields = ('doctor','education_data')

class RemoteRewardRecognisationSerializer(serializers.ModelSerializer):

    class Meta:
        model = RewardRecognisation
        #Fields not in json
        #id,
        fields = ('doctor','reward_data')
class RemoteMembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Membership
        #Fields not in json
        #id,
        fields = ('doctor','name')
class RemoteDoctorExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor_Experience
        #Fields not in json
        #id,
        fields = ('doctor','experience_data')

class RemoteAttachWithDoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttachWithDoctor
        #Fields not in json
        #id,
        fields = ('doctor','organisation','consultancy_fee','email_attach','telephone_attach')

class RemoteScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        #Fields not in json
        #id,
        fields = ('doctor','organisation','schedule_data','by_appointment')