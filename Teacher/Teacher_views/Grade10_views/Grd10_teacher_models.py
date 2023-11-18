from django.db import models
from Headmin.models import Account, MyAccountManager
 
class Grade_10_Teacher_Class(Account):
		#Grd cls A profile picture
	Grd10_profile_picture=models.ImageField(upload_to='Teacher/Grd10ProPic/')
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=30)
	phone_no=models.CharField(max_length=11, blank=True, null=True)
	date_of_birth=models.DateField(blank=True, null=True)
	full_name=models.CharField(max_length=100)
	Resident=models.CharField(max_length=100)


	#subject upload file regulation
	Grade_10_Math_subj_teach=models.BooleanField(default=False, verbose_name="Grade 10 Math Teacher")
	Grade_10_Engl_subj_teach=models.BooleanField(default=False, verbose_name="Grade 10 English Teacher")
	Grade_10_Scn_subj_teach=models.BooleanField(default=False, verbose_name="Grade 10 Science Teacher")
	Grade_10_SocSnc_subj_teach=models.BooleanField(default=False, verbose_name="Grade 10 Social Science Teacher")
	Grade_10_PersDev_subj_teach=models.BooleanField(default=False, verbose_name="Grade 10 Personal development Teacher")
	#Grade 9 teacher class regulation boolean id code
	is_grd10_classA_teacher=models.BooleanField(default=False, verbose_name="Grade 10 Class A")
	is_grd10_classB_teacher=models.BooleanField(default=False, verbose_name="Grade 10 Class B")
	is_grd10_classC_teacher=models.BooleanField(default=False, verbose_name="Grade 10 Class C")
	is_grd10_classD_teacher=models.BooleanField(default=False, verbose_name="Grade 10 Class D")
	is_grd10_classE_teacher=models.BooleanField(default=False, verbose_name="Grade 10 Class E")
	is_grd10_classF_teacher=models.BooleanField(default=False, verbose_name="Grade 10 Class F")
	is_grd10_classG_teacher=models.BooleanField(default=False, verbose_name="Grade 10 Class G")
	is_grd10_classH_teacher=models.BooleanField(default=False, verbose_name="Grade 10 Class H")
	is_grd10_classI_teacher=models.BooleanField(default=False, verbose_name="Grade 10 Class I")
	is_grd10_classJ_teacher=models.BooleanField(default=False, verbose_name="Grade 10 Class J")


	def save(self, *args, **kwargs):
		self.full_name=self.first_name+" "+self.last_name
		super(Grade_10_Teacher_Class, self).save(*args, **kwargs)
	#designation=models.ForeignKey(Designation, on_delete=models.CASCADE)