from django.db import models
from django.utils import timezone

# Create your models here.
class CourseType(models.Model):
    course_type = models.CharField(max_length=255)

    def __str__(self):
        return self.course_type

class CreditHour(models.Model):
    credit_hour = models.CharField(max_length=255)

    def __str__(self):
        return self.credit_hour

class Course(models.Model):
    course_code = models.CharField(max_length=5)
    course_title = models.CharField(max_length=255)
    credit_hour_fk = models.ForeignKey(CreditHour, on_delete=models.CASCADE)
    course_type_fk = models.ForeignKey(CourseType, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_title

class LectureRoom(models.Model):
    lecture_room = models.CharField(max_length=5)

    def __str__(self):
        return self.lecture_room

class BatchNumber(models.Model):
    batch_number = models.CharField(max_length=255)

    def __str__(self):
        return self.batch_number

class ScheduleDay(models.Model):
    schedule_day = models.CharField(max_length=255)

    def __str__(self):
        return self.schedule_day

class ScheduleTime(models.Model):
    schedule_time = models.CharField(max_length=255)

    def __str__(self):
        return self.schedule_time

class Message(models.Model):
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.message

class Schedule(models.Model):
    batch_number_fk = models.ForeignKey(BatchNumber, on_delete=models.CASCADE)
    schedule_day_fk = models.ForeignKey(ScheduleDay, on_delete=models.CASCADE)
    course_fk = models.ForeignKey(Course, on_delete=models.CASCADE)
    lecture_room_fk = models.ForeignKey(LectureRoom, on_delete=models.CASCADE)
    schedule_time_fk = models.ForeignKey(ScheduleTime, on_delete=models.CASCADE)

class Announcement(models.Model):
    batch_number_fk = models.ForeignKey(BatchNumber, on_delete=models.CASCADE)
    schedule_day_fk = models.ForeignKey(ScheduleDay, on_delete=models.CASCADE)
    course_fk = models.ForeignKey(Course, on_delete=models.CASCADE)
    schedule_time_fk = models.ForeignKey(ScheduleTime, on_delete=models.CASCADE)
    message_fk = models.ForeignKey(Message, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now )

class CourseFees(models.Model):
    batch_number_fk = models.ForeignKey(BatchNumber, on_delete=models.CASCADE)
    course_fk = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_fee = models.CharField(max_length=255)