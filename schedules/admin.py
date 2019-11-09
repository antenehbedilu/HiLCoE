from django.contrib import admin
from .models import CourseType, CreditHour, Course, LectureRoom, BatchNumber, ScheduleDay, ScheduleTime, Message, Schedule, Announcement, CourseFees

# Register your models here.
class CourseTypeAdmin(admin.ModelAdmin):
    list_display = ('id','course_type')

class CreditHourAdmin(admin.ModelAdmin):
    list_display = ('id','credit_hour')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id','course_code','course_title','credit_hour_fk','course_type_fk')

class LectureRoomAdmin(admin.ModelAdmin):
    list_display = ('id','lecture_room')

class BatchNumberAdmin(admin.ModelAdmin):
    list_display = ('id','batch_number')

class ScheduleDayAdmin(admin.ModelAdmin):
    list_display = ('id','schedule_day')

class ScheduleTimeAdmin(admin.ModelAdmin):
    list_display = ('id','schedule_time')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id','message')

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id','batch_number_fk','schedule_day_fk','course_fk','lecture_room_fk','schedule_time_fk')

class AnnouncementAdmin(admin.ModelAdmin):
    exclude = ('date_created',)
    list_display = ('id','batch_number_fk','schedule_day_fk','course_fk','schedule_time_fk','message_fk','date_created')

class CourseFeesAdmin(admin.ModelAdmin):
    list_display = ('id','batch_number_fk','course_fk','course_fee')

admin.site.register(CourseType, CourseTypeAdmin)
admin.site.register(CreditHour, CreditHourAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(LectureRoom, LectureRoomAdmin)
admin.site.register(BatchNumber, BatchNumberAdmin)
admin.site.register(ScheduleDay, ScheduleDayAdmin)
admin.site.register(ScheduleTime, ScheduleTimeAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(CourseFees, CourseFeesAdmin)