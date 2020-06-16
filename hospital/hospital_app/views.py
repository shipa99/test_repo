from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from rest_framework import permissions

from .models import Patient, Appointment, Schedule, Medical_Record, Doctor
from .serializers import *


class Patients(APIView):
#    permission_classes = [permissions.IsAuthenticated, ]
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        patients = PatientPostSerializer(data=request.data)
        if patients.is_valid():
            patients.save()
            return Response({"status": "Add"})
        else:
            return Response({"status": "Error"})

class Doctors(APIView):
#    permission_classes = [permissions.IsAuthenticated, ]
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        docs = Doctor.objects.all()
        serializer = DoctorSerializer(docs, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        docs = DoctorPostSerializers(data=request.data)
        if docs.is_valid():
            docs.save(user=request.user)
            return Response({"status": "Add"})
        else:
            return Response({"status": "Error"})

class Apps(APIView):
#    permission_classes = [permissions.IsAuthenticated, ]
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        apps = Appointment.objects.all()
        serializer = AppointmentSerializer(apps, many=True)
        return Response({"data": serializer.data})


class MedCard(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        med_records = Medical_Record.objects.all()
        serializer = MedCardSerializer(med_records, many=True)
        return Response({"data": serializer.data})


class Appointments(APIView):
    def get(self, request):
        apps = Appointment.objects.all()
        serializer = AppointmentSerializer(apps, many=True)
        return Response(serializer.data)


# class AppCreateView(CreateView):
#     model = Appointment
#     form_class = TimeForm
#     success_url = reverse_lazy('time_changelist')
#
#  class AppUpdateView(UpdateView):
#     model = Appointment
#     form_class = TimeForm
#     success_url = reverse_lazy('time_changelist')
#
# def load_times(request):
#     doc_id = request.GET.get('doc')
#     schedule = Schedule.objects.filter(doc_id=doc_id).order_by('doc')
#     return render(request, 'api/v1/hospital/time_options.html', {'schedule': schedule})
#
# def make_appointment(request):
#     if request.method == 'POST':
#         form = TimeForm(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.doc = request.doc
#             form.patient = request.patient
#             form.date = request.date
#             form.time = request.time
#             form.paid = request.paid
#             form.save()
#             return 'OK'
#     else:
#         form = TimeForm()
#     return render(request, "main.html",
#                   {"form2": form})
#
# def test(request):
#     times = TimeForm()
#     context = {
#         'time_list': times,
#
#     }
#     return render(request, 'main.html', context)

