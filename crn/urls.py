#Django
from django.urls import path
#Views
from .views import *

urlpatterns = [
    path('showstudents/', StudentList.as_view() , name='student_list'),
    path('newstudents/', StudentCreate.as_view() , name='student_create'),
    path('newstudents/<int:pk>', StudentEdit.as_view() , name='student_edit'),
    path('newstudents/delete/<int:pk>', StudentDelete.as_view() , name='student_delete'),
]