from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = User
        fields = ("id", "username")


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'surname', 'name', 'patronymic', 'birth_date', 'sex', 'phone', 'email')


class PatientPostSerializer(serializers.ModelSerializer):
    # sex = serializers.SlugRelatedField(
    #     many=True,
    #     slug_field='sex',
    #     queryset=Patient.objects.all(),
    # )
    class Meta:
        model = Patient
        fields = ('surname', 'name', 'patronymic', 'birth_date', 'sex')


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('id', 'surname', 'name', 'patronymic', 'education', 'category', 'sex', 'phone', 'email')


class DoctorPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('id', 'surname', 'name', 'patronymic', 'education', 'category', 'sex', 'phone', 'email')


class TimesSerializer(serializers.ModelSerializer):

    class Meta:
        model = App_times
        fields = ('date', 'time_start')


class PriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = PriceList
        fields = ('service', 'price')


class AppointmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    doc = DoctorSerializer()
#    service_set = PriceSerializer()

    class Meta:
        model = Appointment
        fields = ('id', 'doc', 'patient', 'date', 'time', 'paid')


class MedCardSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    doc = DoctorSerializer()

    class Meta:
        model = Medical_Record
        fields = ('id', 'patient', 'doc', 'record', 'date')