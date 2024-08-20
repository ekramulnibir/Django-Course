from django import forms
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        # fields = ['name', 'roll']
        # exclude = ['name'] #Shows all fields except 
        labels = {
            'name' : 'Student Name',
            'roll' : 'Student Roll'
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'btn-primary'}),
            # 'roll' : forms.PasswordInput()
        }

        help_texts = {
            'name' : "Write your full name"
        }

        error_messages = {
            'name' : {'required' : 'Name is required'}
        }
