from django.db import models
# Create your models here.

from Headmin.models import Account, MyAccountManager
from django.contrib.auth.models import AbstractBaseUser
from django.db.models import Avg, Sum, Count, Min, Max
from django.urls import reverse
import uuid
# from Teacher.Teacher_views.Grade9_views.Grd9_assesment_models import (Grade_9_models_math_Term1_assesment_1, Grade_9_models_math_Term2_assesment_2, Grade_9_models_math_Term3_assesment_3, Grade_9_models_math_Term4_assesment_4)
"""
class Term_11_math_assesment(models.Model):
	#id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	id=models.OneToOneField(Grade_9_Student, to_field=id, default=None)
	#student_user=models.ForeignKey(full_name, on_delete=models.CASCADE)
	#student_user_name=models.ForeignKey(full_name, on_delete=models.CASCADE, null=True, blank=True, default=None)
	T1_A1_Maths_Title=models.CharField(max_length=50, blank=True, null=True)
	T1_A1_Maths_Desc=models.CharField(max_length=100, blank=True, null=True)
	T1_A1_Maths_is_Test=models.BooleanField(default=False)
	T1_A1_Maths_Marks=models.IntegerField(blank=True, null=True, default=0)
	T1_A1_Maths_OutOfMarks=models.IntegerField(blank=True, null=True, default=0)
	T1_A1_Maths_DatePosted=models.DateTimeField(verbose_name='date posted', auto_now_add=False, null=True, blank=True)
	def get_absolute_url(self):
		return reverse('Teacher:student_details_Grd9_clsA', args=[str(self.id)])
"""




class Grade_9_Student(Account):
	#student_user_name=models.ForeignKey(Grade_9_models_math_Term1_assesment_1, on_delete=models.CASCADE, related_name='Student_name', null=True)#, related_name='Student_name'
	#T1_A1_Maths_Marks=models.ForeignKey(Grade_9_models_math_Term1_assesment_1, null=True, blank=True, on_delete=models.CASCADE)
	Grade_9_student_classA_A=models.BooleanField(default=False)
	Grd9_ClsA_std_profile_picture=models.ImageField(upload_to='Student/Grade9/Grd9ClassA/Grd9ClsAProPic/')
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=30)
	phone_no=models.CharField(max_length=11, blank=True, null=True)
	date_of_birth=models.DateField(blank=True, null=True)
	full_name=models.CharField(max_length=100)
	Resident=models.CharField(max_length=100)

	
	#Out of score
	Main_score=models.IntegerField(default=1)

	#English subjects

	#Upload one
	English_name1=models.CharField(max_length=200, blank=True, null=True)
	English_score1=models.IntegerField(blank=True, null=True, default=0)
	#Upload two
	English_name2=models.CharField(max_length=200, blank=True, null=True)
	English_score2=models.IntegerField(blank=True, null=True, default=0)
	#Upload three
	English_name3=models.CharField(max_length=200, blank=True, null=True)
	English_score3=models.IntegerField(blank=True, null=True, default=0)
	
	
	English_score_sum=models.IntegerField(blank=True, null=True, default=0)
	
	
	#Math Subjects
	#Upload one
	Math_name1=models.CharField(max_length=200, blank=True, null=True)
	Math_score1=models.IntegerField(blank=True, null=True, default=0)
	#Upload two
	Math_name2=models.CharField(max_length=200, blank=True, null=True)
	Math_score2=models.IntegerField(blank=True, null=True, default=0)
	#Upload three
	Math_name3=models.CharField(max_length=200, blank=True, null=True)
	Math_score3=models.IntegerField(blank=True, null=True, default=0)

	Math_score_sum=models.IntegerField(blank=True, null=True, default=0)
	
	#Science Subjects
	#Upload one
	Science_name1=models.CharField(max_length=200, blank=True, null=True)
	Science_score1=models.IntegerField(blank=True, null=True, default=0)
	#Upload two
	Science_name2=models.CharField(max_length=200, blank=True, null=True)
	Science_score2=models.IntegerField(blank=True, null=True, default=0)
	#Upload three
	Science_name3=models.CharField(max_length=200, blank=True, null=True)
	Science_score3=models.IntegerField(blank=True, null=True, default=0)

	Science_score_sum=models.IntegerField(blank=True, null=True, default=0)
	
	#SS Subjects
	#Upload one
	SocialScience_name1=models.CharField(max_length=200, blank=True, null=True)
	SocialScience_score1=models.IntegerField(blank=True, null=True, default=0)
	#Upload two
	SocialScience_name2=models.CharField(max_length=200, blank=True, null=True)
	SocialScience_score2=models.IntegerField(blank=True, null=True, default=0)
	#Upload three
	SocialScience_name3=models.CharField(max_length=200, blank=True, null=True)
	SocialScience_score3=models.IntegerField(blank=True, null=True, default=0)

	SocialScience_score_sum=models.IntegerField(blank=True, null=True, default=0)
	
	#PD Subjects
	#Upload one
	PersonalDevelopment_name1=models.CharField(max_length=200, blank=True, null=True)
	PersonalDevelopment_score1=models.IntegerField(blank=True, null=True, default=0)
	#Upload two
	PersonalDevelopment_name2=models.CharField(max_length=200, blank=True, null=True)
	PersonalDevelopment_score2=models.IntegerField(blank=True, null=True, default=0)
	#Upload three
	PersonalDevelopment_name3=models.CharField(max_length=200, blank=True, null=True)
	PersonalDevelopment_score3=models.IntegerField(blank=True, null=True, default=0)


	PersonalDevelopment_score_sum=models.IntegerField(blank=True, null=True, default=0)
	def save(self, *args, **kwargs):
		#self.T1_A1_Maths_Percentage=self.T1_A1_Maths_Marks%self.T1_A1_Maths_OutOfMarks
		self.English_score_sum=self.English_score1+self.English_score2+self.English_score3
		self.full_name=self.first_name+" "+self.last_name
		self.Math_score_sum=self.Math_score1+self.Math_score2+self.Math_score3
		self.Science_score_sum=self.Science_score1+self.Science_score2+self.Science_score3
		self.SocialScience_score_sum=self.SocialScience_score1+self.SocialScience_score2+self.SocialScience_score3
		self.PersonalDevelopment_score_sum=self.PersonalDevelopment_score1+self.PersonalDevelopment_score2+self.PersonalDevelopment_score3
		super(Grade_9_Student, self).save(*args, **kwargs)
	def get_absolute_url(self):
		return reverse('Teacher:student_details_Grd9_clsA', args=[str(self.id)])

# class Grade_9_student_classA(Grade_9_Student):
# 	user=models.OneToOneField(Grade_9_Student, on_delete=models.CASCADE, unique=True, parent_link=True)

# class Grade_9_student_classB(Grade_9_Student):
# 	user=models.OneToOneField(Grade_9_Student, on_delete=models.CASCADE, unique=True, parent_link=True)

# class Grade_9_student_classC(Grade_9_Student):
# 	user=models.OneToOneField(Grade_9_Student, on_delete=models.CASCADE, unique=True, parent_link=True)

# class Grade_9_student_classD(Grade_9_Student):
# 	user=models.OneToOneField(Grade_9_Student, on_delete=models.CASCADE, unique=True, parent_link=True)

# class Grade_9_student_classE(Grade_9_Student):
# 	user=models.OneToOneField(Grade_9_Student, on_delete=models.CASCADE, unique=True, parent_link=True)

# class Grade_9_student_classF(Grade_9_Student):
# 	user=models.OneToOneField(Grade_9_Student, on_delete=models.CASCADE, unique=True, parent_link=True)

# class Grade_9_student_classG(Grade_9_Student):
# 	user=models.OneToOneField(Grade_9_Student, on_delete=models.CASCADE, unique=True, parent_link=True)

# class Grade_9_student_classH(Grade_9_Student):
# 	user=models.OneToOneField(Grade_9_Student, on_delete=models.CASCADE, unique=True, parent_link=True)

# class Grade_9_student_classI(Grade_9_Student):
# 	user=models.OneToOneField(Grade_9_Student, on_delete=models.CASCADE, unique=True, parent_link=True)

# class Grade_9_student_classJ(Grade_9_Student):
# 	user=models.OneToOneField(Grade_9_Student, on_delete=models.CASCADE, unique=True, parent_link=True)

	#T1_A1_Maths_nameofTheTeacher
class Term_11_math_assesment(models.Model):
	#id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	#id=models.ManyToManyField(Grade_9_Student, default=None)
	#student_user=models.ForeignKey(full_name, on_delete=models.CASCADE)
	#student_user_name=models.ForeignKey(full_name, on_delete=models.CASCADE, null=True, blank=True, default=None)
	#reuse_id=models.ForeignKey(Account, to_field=id, default=None, on_delete=models.CASCADE)
	student_user_name=models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True, default=None)
	T1_A1_Maths_Title=models.CharField(max_length=50, blank=True, null=True)
	T1_A1_Maths_Desc=models.CharField(max_length=100, blank=True, null=True)
	T1_A1_Maths_is_Test=models.BooleanField(default=False)
	T1_A1_Maths_Marks=models.IntegerField(blank=True, null=True, default=0)
	T1_A1_Maths_OutOfMarks=models.IntegerField(blank=True, null=True, default=0)
	T1_A1_Maths_DatePosted=models.DateTimeField(verbose_name='date posted', auto_now_add=False, null=True, blank=True)
	def get_absolute_url(self):
		return reverse('Teacher:student_details_Grd9_clsA', args=[str(self.id)])