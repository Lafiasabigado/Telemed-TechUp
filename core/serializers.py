from rest_framework import serializers
from .models import User, Appointment, Feedback, MedicalRecord, Reminder

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        ref_name = "CustomUser"
        fields = '__all__'

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class AppointmentSerializer(serializers.ModelSerializer):
    patient_username = serializers.CharField(source='patient.username', read_only=True)
    doctor_username = serializers.CharField(source='doctor.username', read_only=True)
    class Meta:
        model = Appointment
        fields = ["patient",'doctor',"patient_username","doctor_username",'datetime','status']

class FeedbackSerializer(serializers.ModelSerializer):
    patient_username = serializers.CharField(source='patient.username', read_only=True)
    doctor_username = serializers.CharField(source='doctor.username', read_only=True)
    class Meta:
        model = Feedback
        fields = ['id','patient', 'doctor','patient_username', 'doctor_username', 'rating', 'comment']


class MedicalRecordSerializer(serializers.ModelSerializer):
    patient_username = serializers.CharField(source='patient.username', read_only=True)
    class Meta:
        model = MedicalRecord
        fields = ['patient','patient_username','created_at','diagnosis','treatment','file']

class ReminderSerializer(serializers.ModelSerializer):
    patient_username = serializers.CharField(source='patient.username', read_only=True)
    class Meta:
        model = Reminder
        fields = ["patient",'patient_username','message','date_time']
