#Django
from django.contrib import admin
#Models
from .models import *

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Cualification)
admin.site.register(Period)