from django.contrib import admin
from DB_Learning.models import Student
# Register your models here.
# admin.site.register(Student)
@admin.register(Student)
class Register_Student(admin.ModelAdmin):
    list_display = ('name', 'age', 'department')
    search_fields = ['name','age']
    list_filter = ("name", 'age')


