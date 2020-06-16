from django.db import models
from django.contrib.auth.models import User
from datetime import datetime as dt


class Patient(models.Model):
    surname = models.CharField("Фамилия", max_length=50)
    name = models.CharField("Имя", max_length=50)
    patronymic = models.CharField("Отчество", max_length=50)
    birth_date = models.DateField("Дата рождения", blank=False, default='2000-01-01')
    SEX = (
        ('М', 'мужской'),
        ('Ж', 'женский'),
    )
    sex = models.CharField("Пол", max_length=1, choices=SEX)
    phone = models.CharField("Номер телефона", max_length=11, blank=False, default="no_phone")
    email = models.CharField("Адрес электронной почты", max_length=50, blank=False, default="no_email")

    def __str__(self):
        return self.surname + ' ' + self.name


class App_times(models.Model):
    date = models.DateField("Дата приема", blank=False, null=False, default=dt.now)
    time_start = models.TimeField("Начало времени приема", blank=False, null=False, default=dt.now)

    def __str__(self):
        return str(self.date) + ' ' + str(self.time_start)


class Doctor(models.Model):
    surname = models.CharField("Фамилия", max_length=50)
    name = models.CharField("Имя", max_length=50)
    patronymic = models.CharField("Отчество", max_length=50)
    education = models.CharField("Образование", max_length=300)
    CATEGORIES = (
        ('1', 'Врач 1-ой категории'),
        ('2', 'Врач 2-ой категории'),
        ('3', 'Врач 3-ей категории'),
    )
    SEX = (
        ('М', 'мужской'),
        ('Ж', 'женский'),
    )
    category = models.CharField("Категория врача", max_length=1, choices=CATEGORIES)
    sex = models.CharField("Пол", max_length=1, choices=SEX)
    phone = models.CharField("Номер телефона", max_length=11, blank=False, default="no_phone")
    email = models.CharField("Адрес электронной почты", max_length=50, blank=False, default="no_email")

    def __str__(self):
        return self.surname + ' ' + self.name


#class RoomList(models.Model):
#    room = models.IntegerField("Номер кабинета", max_length=3)
#    head_room = models.ForeignKey(
#        Doctor,
#        verbose_name="Ответственный за кабинет",
#        on_delete=models.SET_NULL
#    )

class Schedule(models.Model):
    doc = models.ForeignKey(
        Doctor,
        verbose_name="Врач",
        on_delete=models.CASCADE
    )
    work_time = models.ManyToManyField(App_times, related_name='working_hours')
    vacant = models.BooleanField(default=True)


class Medical_Record(models.Model):
    patient = models.ForeignKey(
        Patient,
        verbose_name="Пациент",
        on_delete=models.CASCADE
    )
    doc = models.ForeignKey(
        Doctor,
        verbose_name="Лечащий врач",
        on_delete=models.CASCADE
    )
    record = models.TextField("Диагноз и лечение")
    date = models.DateField("Дата назначения")


class PriceList(models.Model):
    service = models.CharField("Услуга", max_length=100)
    price = models.IntegerField("Стоимость услуги")

    def __str__(self):
        return self.service


class Appointment(models.Model):
    doc = models.ForeignKey(
        Doctor,
        verbose_name="Врач",
        on_delete=models.CASCADE)
    patient = models.ForeignKey(
        Patient,
        verbose_name="Пациент",
        on_delete=models.CASCADE
    )
    service = models.ManyToManyField(PriceList)
    date = models.DateField("Дата приема")
    time = models.TimeField("Время приема")
    paid = models.BooleanField(default=False)

