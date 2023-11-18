from django.shortcuts import render, redirect
from Teacher.Teacher_views.Grd9_subj_upload_models import (Grade_9_math_subject_type1, Grade_9_math_subject_type2
										,Grade_9_english_subject_type1, Grade_9_english_subject_type2, Grade_9_science_subject_type1
											,Grade_9_science_subject_type2, Grade_9_socialscience_subject_type1, Grade_9_socialscience_subject_type2
												,Grade_9_personaldevelopement_subject_type1, Grade_9_personaldevelopement_subject_type2)


from Teacher.Teacher_views.Grade9_views.Grd9_teacher_models import Grade_9_Teacher_Class
def Grade9_classA_student(request):
	return render(request, 'Grade9/Grd9ClsA/Grd_9_ClsA_std.html')
def Grd9_ClsA_math_subject_view(request):
	subject_type_one=Grade_9_math_subject_type1.objects.all()
	subject_type_two=Grade_9_math_subject_type2.objects.all()
	all_teachers=Grade_9_Teacher_Class.objects.all()
	context={'teachers':all_teachers,'math_type_ones':subject_type_one, 'math_type_twos':subject_type_two}
	return render(request, 'Grade9/Grd9ClsA/view_uploaded_files/Grd_9_math_view.html', context)

def Grd9_ClsA_english_view(request):
	subject_type_one=Grade_9_english_subject_type1.objects.all()
	subject_type_two=Grade_9_english_subject_type2.objects.all()
	all_teachers=Grade_9_Teacher_Class.objects.all()
	context={'teachers':all_teachers,'english_type_ones':subject_type_one, 'english_type_twos':subject_type_two}
	return render(request, 'Grade9/Grd9ClsA/view_uploaded_files/Grd_9_english_view.html', context)

def Grd9_ClsA_science_view(request):
	subject_type_one=Grade_9_science_subject_type1.objects.all()
	subject_type_two=Grade_9_science_subject_type2.objects.all()
	all_teachers=Grade_9_Teacher_Class.objects.all()
	context={'teachers':all_teachers,'science_type_ones':subject_type_one, 'science_type_twos':subject_type_two}
	return render(request, 'Grade9/Grd9ClsA/view_uploaded_files/Grd_9_science_view.html', context)


def Grd9_ClsA_socialScn_view(request):
	subject_type_one=Grade_9_socialscience_subject_type1.objects.all()
	subject_type_two=Grade_9_socialscience_subject_type2.objects.all()
	all_teachers=Grade_9_Teacher_Class.objects.all()
	context={'teachers':all_teachers,'socialsnc_type_ones':subject_type_one, 'socialsnc_type_twos':subject_type_two}
	return render(request, 'Grade9/Grd9ClsA/view_uploaded_files/Grd_9_socialscience_view.html', context)


def Grd9_ClsA_PersDev_view(request):
	subject_type_one=Grade_9_personaldevelopement_subject_type1.objects.all()
	subject_type_two=Grade_9_personaldevelopement_subject_type2.objects.all()
	all_teachers=Grade_9_Teacher_Class.objects.all()
	context={'teachers':all_teachers,'personalDev_type_ones':subject_type_one, 'personalDev_type_twos':subject_type_two}
	return render(request, 'Grade9/Grd9ClsA/view_uploaded_files/Grd_9_PD_view.html', context)



