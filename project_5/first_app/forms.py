from django import forms
from django.core import validators

#widgets == field to html input
class contactForm(forms.Form):
    name = forms.CharField(label="User Name",  help_text="Enter your name", required=False, widget=forms.Textarea(attrs={'id':'text_area', 'class':'class1 class2', 'placeholder':'Enter your name'}))
    #file = forms.FileField()
    email = forms.EmailField(label="User Email")
    # age = forms.IntegerField(label="Age")
    # weight = forms.FloatField(label="Weight")
    # Balance = forms.DecimalField()
    age = forms.CharField(widget=forms.NumberInput)
    check = forms.BooleanField()
    brithday = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    appointment = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    CHOICES =[('S', 'Small'), ('M', 'Meidum'), ('L', 'Large')]
    # size = forms.ChoiceField(choices=CHOICES)
    size = forms.ChoiceField(choices=CHOICES, widget = forms.RadioSelect)
    TOOPINGS = [('P', 'Pepperoni'),('S', 'Sun-Dried Tomatoes'),('T', 'Truffle Oil Drizzle')]
    pizza = forms.MultipleChoiceField(choices= TOOPINGS, widget=forms.CheckboxSelectMultiple)
    
# class studentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname) < 5:
#     #         raise forms.ValidationError("Lenght must be excced 10 character")
#     #     return valname
    
#     # def clean_email(self):
#     #     valname = self.cleaned_data['email']
#     #     if '.com' not in valname:
#     #         raise forms.ValidationError("Mail must contain .com")

#     def clean(self):
#         clean_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname) < 5:
#             raise forms.ValidationError("Lenght must be excced 10 character")
    
#         if '.com' not in valemail:
#             raise forms.ValidationError("Mail must contain .com")

def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter a value with at least 10 chars")

class studentData(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(5, message= 'Enter a value with atleast 10 characters')])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message="Enter a valid mail")])
    address = forms.CharField(widget=forms.TextInput, validators=[len_check])
    age = forms.IntegerField (validators=[validators.MaxValueValidator(34, message= "Age must be less than 35"), validators.MinValueValidator(25, message="Age must be greater than 24")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'], message='File externsion must be end with .pdf')])


class passwordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)
      
    def clean(self):
        cleaned_data = super().clean()
        val_name = self.cleaned_data['name']
        val_pass = self.cleaned_data['password']
        val_repass = self.cleaned_data['re_password']

        if val_pass!=val_repass:
            raise forms.ValidationError("Password doesn't match")
        if len(val_name) < 5:
            raise forms.ValidationError("Name length should be greater than 5")