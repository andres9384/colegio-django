#Django
from django import forms
#Models
from .models import *
#Plugins
from bootstrap_modal_forms.forms import BSModalModelForm

class StudentForm(BSModalModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['edad'].widget.attrs['min'] = 1

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class CualificationForm(forms.ModelForm):
    class Meta:
        model = Cualification
        fields = '__all__'


class PeriodForm(forms.ModelForm):
    class Meta:
        model = Period
        fields = '__all__'