from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from Teacher.Teacher_views.Grade9_views.Grd9_teacher_models import Grade_9_Teacher_Class







#Grd9_ClsA_profile_picture 'first_name', 'last_name', 'phone_no', 'Grd9_ClsA_profile_picture', 'date_of_birth', 

#GRADE9 TEACHER SIGNUP FORM from class A 
class TeacherGrd9_Class_SignUp_Form(UserCreationForm):

	class_choices=(
	('Select', "Select class"),
	('is_Grade_9_teacher_classA', "Class A"),
    ('is_Grade_9_teacher_classB', "Class B"),
    ("is_Grade_9_teacher_classC", "Class C"),
    ("is_Grade_9_teacher_classD", "Class D"),
    ("is_Grade_9_teacher_classE", "Class E"),
    ("is_Grade_9_teacher_classF", "Class F"),
    ("is_Grade_9_teacher_classG", "Class G"),
    ("is_Grade_9_teacher_classH", "Class H"),
    ("is_Grade_9_teacher_classI", "Class I"),
    ("is_Grade_9_teacher_classJ", "Class J"),
)
	email=forms.EmailField(required=True)
	Class = forms.ChoiceField(choices = class_choices)
	password1=forms.CharField(label='Password', widget=forms.PasswordInput)
	password2=forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
# 	Subject_choices=(
# 	('Select', "Select Subject"),
# 	('Grade_9_Math_subj_teach', ""),
#     ('Grade_9_Engl_subj_teach', ""),
#     ("Grade_9_Scn_subj_teach", ""),
#     ("Grade_9_SocSnc_subj_teach", ""),
#     ("Grade_9_PersDev_subj_teach", ""),

# )
	class Meta(UserCreationForm.Meta):
		model=Grade_9_Teacher_Class
		fields=('first_name', 'last_name', 'phone_no', 'Grd9_profile_picture', 'date_of_birth','Class', 'username', 'Resident', 'email',  'password1', 'password2')
	def save(self, commit=True):
		user=super().save(commit=False)
		user.email=self.cleaned_data['email']
		user.is_teacher=True
		user.is_Grade_9_teacher=True
		# print('--------------------------------------------------------')
		# value=user.Class=self.cleaned_data['Class']
		# print(value)
		# if value=='is_Grade_9_teacher_classB':
		# 	user.is_Grade_9_teacher_classB=True
		if commit:
			user.save()
		return user

#update identification of grade 9 teacher class A
class TeacherGrd9_Class_SignUp_Detail_Form(ModelForm):
	class Meta:
		model=Grade_9_Teacher_Class
		fields=('first_name', 'last_name', 'phone_no', 'Grd9_profile_picture', 'date_of_birth')
























































































