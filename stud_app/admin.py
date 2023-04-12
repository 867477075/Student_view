from django.contrib import admin
from stud_app.models import Student_Data

# Register your models here.

@admin.register(Student_Data)
class Student_Admin(admin.ModelAdmin):
    list_display = ['name','id','roll_no']
