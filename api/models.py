from django.db import models


class Employee(models.Model):
    gender_choices = (
        (0, 'male'),
        (1, 'female'),
        (2, 'other'),
    )

    username = models.CharField(max_length=25)
    password = models.CharField(max_length=32)
    gender = models.SmallIntegerField(choices=gender_choices, default=0)
    phone = models.CharField(max_length=11, null=True, blank=True)
    pic = models.ImageField(upload_to='pic', default='pic/1.jpg')

    class Meta:
        db_table = 'bz_employee'
        verbose_name = '员工'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Student(models.Model):
    gender_choices = (
        (0, 'male'),
        (1, 'female'),
        (2, 'other'),
    )

    name = models.CharField(max_length=20)
    password = models.CharField(max_length=16)
    gender = models.SmallIntegerField(choices=gender_choices, default=0)
    photo = models.ImageField(upload_to='pic', default='pic/1.jpg')
    student_number = models.CharField(max_length=9, null=True, blank=True)

    class Meta:
        db_table = 'bz_student'
        verbose_name = '学生'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
