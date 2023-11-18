from django.db import models
from Teacher.Teacher_views.Grade9_views.Grd9_teacher_models import Grade_9_Teacher_Class
# Create your models here.
#ENGLISH
"""
class Grade_9_english_subject_type1(models.Model):
	#English_1
	Grd9_Engl_Title=models.CharField(max_length=200, verbose_name='English Title')
	Grd9_Engl_file=models.FileField(upload_to='Grade9Subject/Engl_test_grd9/')
	Grd9_Engl_Desc=models.TextField(max_length=500, null=True, blank=True)
	Grd9_Engl_posted_date=models.DateTimeField(verbose_name='posted_date', auto_now_add=True)

class Grade_9_english_subject_type2(models.Model):
	#English_2
	Grd9_Engl_Title=models.CharField(max_length=200, verbose_name='English Title')
	Grd9_Engl_file=models.FileField(upload_to='Grade9Subject/Engl_test_grd9/')
	Grd9_Engl_Desc=models.TextField(max_length=500, null=True, blank=True)
	Grd9_Engl_posted_date=models.DateTimeField(verbose_name='posted_date', auto_now_add=True)

#SCIENCE
class Grade_9_science_subject_type1(models.Model):
	#Science_1
	Grd9_Scn_Title=models.CharField(max_length=200, verbose_name='Science Title')
	Grd9_Scn_file=models.FileField(upload_to='Grade9Subject/Scn_test_grd9/')
	Grd9_Scn_Desc=models.TextField(max_length=500, null=True, blank=True)
	Grd9_Scn_posted_date=models.DateTimeField(verbose_name='posted_date', auto_now_add=True)

class Grade_9_science_subject_type2(models.Model):
	#Science_2
	Grd9_Scn_Title=models.CharField(max_length=200, verbose_name='Science Title')
	Grd9_Scn_file=models.FileField(upload_to='Grade9Subject/Scn_test_grd9/')
	Grd9_Scn_Desc=models.TextField(max_length=500, null=True, blank=True)
	Grd9_Scn_posted_date=models.DateTimeField(verbose_name='posted_date', auto_now_add=True)

#SOCIAL_SCIENCE
class Grade_9_socialscience_subject_type1(models.Model):
	#Social_Science_1
	Grd9_SocSnc_Title=models.CharField(max_length=200, verbose_name='Social Science Title')
	Grd9_SocSnc_file=models.FileField(upload_to='Grade9Subject/SocSnc_test_grd9/')
	Grd9_SocSnc_Desc=models.TextField(max_length=500, null=True, blank=True)
	Grd9_SocSnc_posted_date=models.DateTimeField(verbose_name='posted_date', auto_now_add=True)

class Grade_9_socialscience_subject_type2(models.Model):
	#Social_Science_2
	Grd9_SocSnc_Title=models.CharField(max_length=200, verbose_name='Social Science Title')
	Grd9_SocSnc_file=models.FileField(upload_to='Grade9Subject/SocSnc_test_grd9/')
	Grd9_SocSnc_Desc=models.TextField(max_length=500, null=True, blank=True)
	Grd9_SocSnc_posted_date=models.DateTimeField(verbose_name='posted_date', auto_now_add=True)

class Grade_9_personaldevelopement_subject_type1(models.Model):
	#Personal_development_1
	Grd9_PersDev_Title=models.CharField(max_length=200, verbose_name='Personal development Title')
	Grd9_PersDev_file=models.FileField(upload_to='Grade9Subject/PersDev_test_grd9/')
	Grd9_PersDev_Desc=models.TextField(max_length=500, null=True, blank=True)
	Grd9_PersDev_posted_date=models.DateTimeField(verbose_name='posted_date', auto_now_add=True)

class Grade_9_personaldevelopement_subject_type2(models.Model):
	#Personal_development_2
	Grd9_PersDev_Title=models.CharField(max_length=200, verbose_name='Personal development Title')
	Grd9_PersDev_file=models.FileField(upload_to='Grade9Subject/PersDev_test_grd9/')
	Grd9_PersDev_Desc=models.TextField(max_length=500, null=True, blank=True)
	Grd9_PersDev_posted_date=models.DateTimeField(verbose_name='posted_date', auto_now_add=True)


"""