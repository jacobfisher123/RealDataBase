from django.db import models
from Headmin.models import Account, MyAccountManager
 
class Grade_9_Teacher_Class(Account):
		#Grd cls A profile picture
	Grd9_profile_picture=models.ImageField(upload_to='Teacher/Grd9ProPic/')
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=30)
	phone_no=models.CharField(max_length=11, blank=True, null=True)
	date_of_birth=models.DateField(blank=True, null=True)
	full_name=models.CharField(max_length=100)
	Resident=models.CharField(max_length=100)


	#subject upload file regulation
	Grade_9_Math_subj_teach=models.BooleanField(default=False, verbose_name="Grade 9 Math Teacher")
	Grade_9_Engl_subj_teach=models.BooleanField(default=False, verbose_name="Grade 9 English Teacher")
	Grade_9_Scn_subj_teach=models.BooleanField(default=False, verbose_name="Grade 9 Science Teacher")
	Grade_9_SocSnc_subj_teach=models.BooleanField(default=False, verbose_name="Grade 9 Social Science Teacher")
	Grade_9_PersDev_subj_teach=models.BooleanField(default=False, verbose_name="Grade 9 Personal development Teacher")
	#Grade 9 teacher class regulation boolean id code
	is_grd9_classA_teacher=models.BooleanField(default=False, verbose_name="Grade 9 Class A")
	is_grd9_classB_teacher=models.BooleanField(default=False, verbose_name="Grade 9 Class B")
	is_grd9_classC_teacher=models.BooleanField(default=False, verbose_name="Grade 9 Class C")
	is_grd9_classD_teacher=models.BooleanField(default=False, verbose_name="Grade 9 Class D")
	is_grd9_classE_teacher=models.BooleanField(default=False, verbose_name="Grade 9 Class E")
	is_grd9_classF_teacher=models.BooleanField(default=False, verbose_name="Grade 9 Class F")
	is_grd9_classG_teacher=models.BooleanField(default=False, verbose_name="Grade 9 Class G")
	is_grd9_classH_teacher=models.BooleanField(default=False, verbose_name="Grade 9 Class H")
	is_grd9_classI_teacher=models.BooleanField(default=False, verbose_name="Grade 9 Class I")
	is_grd9_classJ_teacher=models.BooleanField(default=False, verbose_name="Grade 9 Class J")


	#Subjects Types
	#Math teacher types
	Grade9_math_teacher_one=models.BooleanField(default=False)
	Grade9_math_teacher_two=models.BooleanField(default=False)


	#English teacher types
	Grade9_engl_teacher_one=models.BooleanField(default=False)
	Grade9_engl_teacher_two=models.BooleanField(default=False)	

	#Science
	Grade9_scn_teacher_one=models.BooleanField(default=False)
	Grade9_scn_teacher_two=models.BooleanField(default=False)	

	#Social science
	Grade9_socscn_teacher_one=models.BooleanField(default=False)
	Grade9_socscn_teacher_two=models.BooleanField(default=False)

	#Personal development
	Grade9_persdev_teacher_one=models.BooleanField(default=False)
	Grade9_persdev_teacher_two=models.BooleanField(default=False)
	def save(self, *args, **kwargs):
		self.full_name=self.first_name+" "+self.last_name
		super(Grade_9_Teacher_Class, self).save(*args, **kwargs)
	#designation=models.ForeignKey(Designation, on_delete=models.CASCADE)

# class Grade9StudentUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Grade_9_Student
#         fields = ['Grd9_ClsA_std_profile_picture', 'first_name', 'last_name', 'phone_no', 'date_of_birth', 'full_name', 'Resident']
