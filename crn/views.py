#Django
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView , UpdateView , DeleteView
from  django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
#Models
from .models import *
#Forms
from .forms import *
#Plugins
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView


class StudentList(LoginRequiredMixin,ListView):
    """lista de estudiante"""
    model = Student
    template_name = 'crn/studentList.html'
    context_object_name = 'student'


class StudentCreate(LoginRequiredMixin, BSModalCreateView):
    """crear estudiante"""
    model = Student
    template_name = 'crn/studentForm.html'
    form_class =  StudentForm
    success_url = reverse_lazy('student_list')


class StudentEdit(LoginRequiredMixin, BSModalUpdateView):
    """editar estudiante"""
    model = Student
    template_name = 'crn/studentForm.html'
    context_object_name = 'student'
    form_class =  StudentForm
    success_url = reverse_lazy('student_list')
    context_object_name = 'student'



class StudentDelete(LoginRequiredMixin, BSModalDeleteView):
    """liminar  estudiante"""
    model = Student
    template_name = 'crn/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')




