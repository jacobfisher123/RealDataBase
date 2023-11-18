from django.shortcuts import render, redirect
from ...decorators import headmin_required
from Teacher.Teacher_views.Grade9_views.Grd9_teacher_models import Grade_9_Teacher_Class
from django.contrib.auth.decorators import login_required
from Student.student_views.Grade9_std_views.Grade9_models import Grade_9_student_classA, Grade_9_student_classB, Grade_9_student_classC
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView
from django.forms import ModelForm
from django import forms
from django.utils.decorators import method_decorator
from Headmin.models import Account
#from Teacher.Teacher_views.Grade9_views.Grd9_teacher_models import Grade_9_teacher_classA
@login_required
@headmin_required
def Grade9_RegTeacher_List_view(request):
    return render(request, 'Grade9Teach/Grade9_teach_register_list.html')


# Grade_9_Math_subj_teach
# Grade_9_Engl_subj_teach
# Grade_9_Scn_subj_teach
# Grade_9_SocSnc_subj_teach
# Grade_9_PersDev_subj_teach

def multiple_class_Subject_warning_checker(context):
	Classes=[]
	warning_count=0
	if Grade_9_Teacher_Class.objects.filter(Grade_9_Math_subj_teach=True).count()>1:
		if Grade_9_Teacher_Class.objects.filter(Grade_9_Math_subj_teach=True,is_grd9_classA_teacher=True, is_grd9_classB_teacher=True):
			context['warn']=warn=True
			context['subject_type']="Math"
			context['users']=Grade_9_Teacher_Class.objects.filter(Grade_9_Math_subj_teach=True,is_grd9_classA_teacher=True, is_grd9_classB_teacher=True)
			print("------------------------------------")
			print("Two math teacher assigned to class A AND B")
			print("------------------------------------")
			warning_count=warning_count+1
		elif Grade_9_Teacher_Class.objects.filter(Grade_9_Math_subj_teach=True,is_grd9_classA_teacher=True).count()>1:
			context['warn']=warn=True
			context['subject_type']="Math"
			context['users']=Grade_9_Teacher_Class.objects.filter(Grade_9_Math_subj_teach=True,is_grd9_classA_teacher=True)
			print("------------------------------------")
			print("Two math teacher assigned to class A")
			print("------------------------------------")

		
	if Grade_9_Teacher_Class.objects.filter(Grade_9_Engl_subj_teach=True).count()>1:
		if Grade_9_Teacher_Class.objects.filter(Grade_9_Engl_subj_teach=True,is_grd9_classA_teacher=True, is_grd9_classB_teacher=True):
			context['warn']=warn=True
			context['subject_type']="English"
			context['users']=Grade_9_Teacher_Class.objects.filter(Grade_9_Engl_subj_teach=True,is_grd9_classA_teacher=True, is_grd9_classB_teacher=True)
			print("------------------------------------")
			print("Two English teacher assigned to class A AND B")
			print("------------------------------------")
			warning_count=warning_count+1
		elif Grade_9_Teacher_Class.objects.filter(Grade_9_Engl_subj_teach=True,is_grd9_classA_teacher=True).count()>1:
			context['warn']=warn=True
			context['subject_type']="English"
			context['users']=Grade_9_Teacher_Class.objects.filter(Grade_9_Engl_subj_teach=True,is_grd9_classA_teacher=True)
			print("------------------------------------")
			print("Two English teacher assigned to class A")
			print("------------------------------------")
	if Grade_9_Teacher_Class.objects.filter(Grade_9_Scn_subj_teach=True).count()>1:
		if Grade_9_Teacher_Class.objects.filter(Grade_9_Scn_subj_teach=True,is_grd9_classA_teacher=True, is_grd9_classB_teacher=True):
			context['warn']=warn=True
			context['subject_type']="Science"
			context['users']=Grade_9_Teacher_Class.objects.filter(Grade_9_Scn_subj_teach=True,is_grd9_classA_teacher=True, is_grd9_classB_teacher=True)
			print("------------------------------------")
			print("Two Science teacher assigned to class A AND B")
			print("------------------------------------")
		elif Grade_9_Teacher_Class.objects.filter(Grade_9_Scn_subj_teach=True,is_grd9_classA_teacher=True).count()>1:
			context['warn']=warn=True
			context['subject_type']="Science"
			context['users']=Grade_9_Teacher_Class.objects.filter(Grade_9_Scn_subj_teach=True,is_grd9_classA_teacher=True)
			print("------------------------------------")
			print("Two Science teacher assigned to class A")
			print("------------------------------------")
	if Grade_9_Teacher_Class.objects.filter(Grade_9_SocSnc_subj_teach=True).count()>1:
		if Grade_9_Teacher_Class.objects.filter(Grade_9_SocSnc_subj_teach=True,is_grd9_classA_teacher=True, is_grd9_classB_teacher=True):
			context['warn']=warn=True
			context['subject_type']="Social Science"
			context['users']=Grade_9_Teacher_Class.objects.filter(Grade_9_SocSnc_subj_teach=True,is_grd9_classA_teacher=True, is_grd9_classB_teacher=True)
			print("------------------------------------")
			print("Two Social Science teacher assigned to class A AND B")
			print("------------------------------------")
		elif Grade_9_Teacher_Class.objects.filter(Grade_9_SocSnc_subj_teach=True,is_grd9_classA_teacher=True).count()>1:
			context['warn']=warn=True
			context['subject_type']="Social Science"
			context['users']=Grade_9_Teacher_Class.objects.filter(Grade_9_SocSnc_subj_teach=True,is_grd9_classA_teacher=True)
			print("------------------------------------")
			print("Two Social Science teacher assigned to class A")
			print("------------------------------------")
	if Grade_9_Teacher_Class.objects.filter(Grade_9_PersDev_subj_teach=True).count()>1:
		if Grade_9_Teacher_Class.objects.filter(Grade_9_PersDev_subj_teach=True,is_grd9_classA_teacher=True, is_grd9_classB_teacher=True):
			context['warn']=warn=True
			context['subject_type']="Personal Development"
			context['users']=Grade_9_Teacher_Class.objects.filter(Grade_9_PersDev_subj_teach=True,is_grd9_classA_teacher=True, is_grd9_classB_teacher=True)
			print("------------------------------------")
			print("Two Personal Development teacher assigned to class A AND B")
			print("------------------------------------")
		elif Grade_9_Teacher_Class.objects.filter(Grade_9_PersDev_subj_teach=True,is_grd9_classA_teacher=True).count()>1:
			context['warn']=warn=True
			context['subject_type']="Personal Development"
			context['users']=Grade_9_Teacher_Class.objects.filter(Grade_9_PersDev_subj_teach=True,is_grd9_classA_teacher=True)
			print("------------------------------------")
			print("Two Personal Development teacher assigned to class A")
			print("------------------------------------")

	if warning_count>1:
		warning_count="{}, issues"

	elif warning_count==1:
		warning_count="{}, issue".format(warning_count)
	context['warning_count']=warning_count



@login_required
@headmin_required
def Grade_9_teacher_list(request):
	all_teacher=Grade_9_Teacher_Class.objects.filter(is_teacher=True, is_Grade_9_teacher=True)
	context={'teachers':all_teacher,'Display_all_teacher_list_view':'active'}
	if Grade_9_Teacher_Class.objects.filter(is_Grade_9_teacher_classA=True).count()>1:
		context['warn']=warn=True
		context['users']=Grade_9_Teacher_Class.objects.filter(is_Grade_9_teacher_classA=True)
	else:
		context['warn']=warn=False
	multiple_class_Subject_warning_checker(context)
	return render(request, 'Grade9Teach/Grd9_all_teacher_list_view.html', context)

#Patron/Matron checker
def class_Identifier_checker(context,pk):
	if Grade_9_Teacher_Class.objects.filter(id=pk,is_Grade_9_teacher_classA=True):
		context['class']="A"
	elif Grade_9_Teacher_Class.objects.filter(id=pk,is_Grade_9_teacher_classB=True):
		context['class']="B"
	elif Grade_9_Teacher_Class.objects.filter(id=pk,is_Grade_9_teacher_classC=True):
		context['class']="C"
	elif Grade_9_Teacher_Class.objects.filter(id=pk,is_Grade_9_teacher_classD=True):
		context['class']="D"
	elif Grade_9_Teacher_Class.objects.filter(id=pk,is_Grade_9_teacher_classE=True):
		context['class']="E"
	else:
		context['class']="NONE"

#Multiple class assigned checker
def class_Identifier_Multiple_checker(context,pk):
	classes=[]
	if Grade_9_Teacher_Class.objects.filter(id=pk,is_grd9_classA_teacher=True):
		classes.append("A")
	if Grade_9_Teacher_Class.objects.filter(id=pk,is_grd9_classB_teacher=True):
		classes.append("B")
	if Grade_9_Teacher_Class.objects.filter(id=pk,is_grd9_classC_teacher=True):
		classes.append("C")
	if Grade_9_Teacher_Class.objects.filter(id=pk,is_grd9_classD_teacher=True):
		classes.append("D")
	if Grade_9_Teacher_Class.objects.filter(id=pk,is_grd9_classE_teacher=True):
		classes.append("E")
	if Grade_9_Teacher_Class.objects.filter(id=pk,is_grd9_classF_teacher=True):
		classes.append("F")
	return classes




@login_required
@headmin_required
def Grade_9_Teacher_list_details(request, pk):
	
	#dont forget to add number of students
	sum_std_clsA=Grade_9_student_classA.objects.all().count()
	sum_std_clsB=Grade_9_student_classB.objects.all().count()
	sum_std_clsC=Grade_9_student_classC.objects.all().count()
	all_teacher=Grade_9_Teacher_Class.objects.filter(id=pk)
	context={'teachers':all_teacher, 'sum_std_clsA':sum_std_clsA, 'sum_std_clsB':sum_std_clsB,'sum_std_clsC':sum_std_clsC,'teachers':all_teacher,'Display_all_teacher_list_view':'active'}

	context['classes']=class_Identifier_Multiple_checker(context,pk)
	class_Identifier_checker(context,pk)
	multiple_class_Subject_warning_checker(context)
	return  render(request, 'Grade9Teach/Grade9_Teacher_list_details.html', context)



	

#This code handles the file upload regulation of grd6 class A (__all__ grade 9)

class Update_Grade9_cls_teacher_subject_file_regulator(ModelForm):
	class_choices=(('Select', "Select Subject"),
	('Grade_9_Math_subj_teach', "Math"),
    ('Grade_9_Engl_subj_teach', "English"),
    ("Grade_9_Scn_subj_teach", "Science"),
    ("Grade_9_SocSnc_subj_teach", "Social Science"),
    ("Grade_9_PersDev_subj_teach", "Personal Development"))
    
	Subject = forms.ChoiceField(choices = class_choices)

    
	class Meta:
		model=Grade_9_Teacher_Class
		fields=('Subject',)


class Update_Grade9_cls_Main_selector_ragualtor(ModelForm):
	class_choices=(
	('Select', "Select class"),
	('is_Grade_9_teacher_classA', "Class A"),
    ('is_Grade_9_teacher_classB', "Class B"),
    ("is_Grade_9_teacher_classC", "Class C"),
    ("is_Grade_9_teacher_classD", "Class D"),
    ("is_Grade_9_teacher_classE", "Class E"))
	Class = forms.ChoiceField(choices = class_choices)

	class Meta:
		model=Account
		fields=('Class',)

			
#Main class matron/patron form
class Update_Grade9_cls_selector_ragualtor(ModelForm):

	class Meta:
		model=Grade_9_Teacher_Class
		fields=('is_grd9_classA_teacher', 'is_grd9_classB_teacher', 'is_grd9_classC_teacher', 'is_grd9_classD_teacher', 'is_grd9_classE_teacher', 'is_grd9_classF_teacher', 'is_grd9_classG_teacher', 'is_grd9_classH_teacher', 'is_grd9_classI_teacher', 'is_grd9_classJ_teacher')
		

#This code handles the subject type regulator of grade 9

class Update_Grade9_math_type(ModelForm):
	class Meta:
		model=Grade_9_Teacher_Class
		fields=('Grade9_math_teacher_one', 'Grade9_math_teacher_two')

class Update_Grade9_english_type(ModelForm):
	class Meta:
		model=Grade_9_Teacher_Class
		fields=('Grade9_engl_teacher_one', 'Grade9_engl_teacher_two')

class Update_Grade9_science_type(ModelForm):
	class Meta:
		model=Grade_9_Teacher_Class
		fields=('Grade9_scn_teacher_one', 'Grade9_scn_teacher_two')

class Update_Grade9_socialscience_type(ModelForm):
	class Meta:
		model=Grade_9_Teacher_Class
		fields=('Grade9_socscn_teacher_one', 'Grade9_socscn_teacher_two')

class Update_Grade9_personaldevelopment_type(ModelForm):
	class Meta:
		model=Grade_9_Teacher_Class
		fields=('Grade9_persdev_teacher_one', 'Grade9_persdev_teacher_two')



#This code distinctive class assign regulator
@method_decorator([login_required, headmin_required], name='dispatch') 
class Grd9_Update_class_assign_regulator(UpdateView):
	model=Grade_9_Teacher_Class
	form_class=Update_Grade9_cls_selector_ragualtor
	template_name='Grade9Teach/Grd9_Update_Teacher_class_regulator.html'
	def get_success_url(self):
		Grade9teacherclassA_id = self.kwargs['pk']
		return reverse_lazy('headmin:Grade_9_Teacher_list_details',  kwargs={'pk': Grade9teacherclassA_id})

#@method_decorator([login_required, headmin_required], name='dispatch') 
# def Grd9_Update_main_class_assign_regulator(request, pk):

# 	pk=Account.objects.filter(id=pk)
# 	if request.method=='POST':
# 		form=Update_Grade9_cls_selector_ragualtor(request.POST)
# 		if form.is_valid():
# 			print(pk.==True)
# 			form.save()
			
def checker(form, value):
	if value=='is_Grade_9_teacher_classA':
		form.is_Grade_9_teacher_classA=True
	else:
		form.is_Grade_9_teacher_classA=False
	if value=='is_Grade_9_teacher_classB':
		form.is_Grade_9_teacher_classB=True
	else:
		form.is_Grade_9_teacher_classB=False
	if value=='is_Grade_9_teacher_classC':
		form.is_Grade_9_teacher_classC=True
	else:
		form.is_Grade_9_teacher_classC=False
	if value=='is_Grade_9_teacher_classD':
		form.is_Grade_9_teacher_classD=True
	else:
		form.is_Grade_9_teacher_classD=False
	if value=='is_Grade_9_teacher_classE':
		form.is_Grade_9_teacher_classE=True
	else:
		form.is_Grade_9_teacher_classE=False
"""
Grade_9_Math_subj_teach
Grade_9_Engl_subj_teach
Grade_9_Scn_subj_teach
Grade_9_SocSnc_subj_teach
Grade_9_PersDev_subj_teach
"""
def sub_checker(form,value):
	if value=='Grade_9_Math_subj_teach':
		form.Grade_9_Math_subj_teach=True
	else:
		form.Grade_9_Math_subj_teach=False
	if value=='Grade_9_Engl_subj_teach':
		form.Grade_9_Engl_subj_teach=True
	else:
		form.Grade_9_Engl_subj_teach=False
	if value=='Grade_9_Scn_subj_teach':
		form.Grade_9_Scn_subj_teach=True
	else:
		form.Grade_9_Scn_subj_teach=False
	if value=='Grade_9_Scn_subj_teach':
		form.Grade_9_Scn_subj_teach=True
	else:
		form.Grade_9_Scn_subj_teach=False
	if value=='Grade_9_SocSnc_subj_teach':
		form.Grade_9_SocSnc_subj_teach=True
	else:
		form.Grade_9_SocSnc_subj_teach=False
	if value=='Grade_9_PersDev_subj_teach':
		form.Grade_9_PersDev_subj_teach=True
	else:
		form.Grade_9_PersDev_subj_teach=False
# 	return render(request, 'Grade9Teach/Grd9_Upda
# 	return render(request, 'Grade9Teach/Grd9_Update_Teacher_class_regulator.html', {'pk':pk})
@method_decorator([login_required, headmin_required], name='dispatch')
class Grd9_Update_main_class_assign_regulator(UpdateView):
	model=Account
	form_class=Update_Grade9_cls_Main_selector_ragualtor
	template_name='Grade9Teach/Grd9_Update_Teacher_class_regulator.html'
	def form_valid(self, form):
		form=form.save(commit=False)
		Grade9teacherclassA_id =  self.kwargs['pk']
		value=self.request.POST.get('Class')
		if  value=='Select':
			return redirect('headmin:Grd9_Update_main_class_assign_regulator', pk=Grade9teacherclassA_id)
		else:
			checker(form, value)
			form.save()
			return redirect('headmin:Grade_9_Teacher_list_details', pk=Grade9teacherclassA_id)


@method_decorator([login_required, headmin_required], name='dispatch') 
class Grd9_Update_Teacher_file_regulator(UpdateView):
	model = Grade_9_Teacher_Class
	#feilds= 'is_grd6_classA_teacher', 'is_grd6_classB_teacher', 'is_grd6_classC_teacher'


	form_class=Update_Grade9_cls_teacher_subject_file_regulator
	template_name = 'Grade9Teach/Grd9_Update_Teacher_file_regulator.html'
	#std=Grade6studentclassB.objects.all()
	#context={'students':std}
	def form_valid(self, form):
		form=form.save(commit=False)
		Grade9teacherclassA_id =  self.kwargs['pk']
		value=self.request.POST.get('Subject')
		if  value=='Select':
			return redirect('headmin:Grd9_Update_Teacher_file_regulator', pk=Grade9teacherclassA_id)

		else:
			sub_checker(form, value)
			form.save()
			return redirect('headmin:Grade_9_Teacher_list_details', pk=Grade9teacherclassA_id)
	def get_success_url(self):
		Grade9teacher_id = self.kwargs['pk']
		return reverse_lazy('headmin:Grade_9_Teacher_list_details',  kwargs={'pk': Grade9teacher_id})

# @method_decorator([login_required, headmin_required], name='dispatch') 
# class Grd9_Update_Teacher_file_regulator(UpdateView):
# 	model = Grade_9_Teacher_Class
# 	#feilds= 'is_grd6_classA_teacher', 'is_grd6_classB_teacher', 'is_grd6_classC_teacher'


# 	form_class=Update_Grade9_cls_teacher_subject_file_regulator
# 	template_name = 'Grade9Teach/Grd9_Update_Teacher_file_regulator.html'
# 	#std=Grade6studentclassB.objects.all()
# 	#context={'students':std}
# 	def get_success_url(self):
# 		Grade9teacher_id = self.kwargs['pk']
# 		return reverse_lazy('headmin:Grade_9_Teacher_list_details',  kwargs={'pk': Grade9teacher_id})

#These codes gives the distinctifies the teacher subject types
#MATH TYPE
@method_decorator([login_required, headmin_required], name='dispatch') 
class Grd9_Update_math_teacher_type_regulator(UpdateView):
	model=Grade_9_Teacher_Class
	form_class=Update_Grade9_math_type
	template_name='Grade9Teach/Grd9_subject_type_reg/update_math_teacher_type.html'
	def get_succecc_url(self):
		Grade9teacherclass_id=self.kwargs['pk']
		return reverse_lazy('headmin:Grade_9_Teacher_list_details', kwargs={'pk':Grade9teacherclass_id})
#ENGLISH TYPE
@method_decorator([login_required, headmin_required], name='dispatch') 
class Grd9_Update_english_teacher_type_regulator(UpdateView):
	model=Grade_9_Teacher_Class
	form_class=Update_Grade9_english_type
	template_name='Grade9Teach/Grd9_subject_type_reg/update_english_teacher_type.html'
	def get_succecc_url(self):
		Grade9teacherclass_id=self.kwargs['pk']
		return reverse_lazy('headmin:Grade_9_Teacher_list_details', kwargs={'pk':Grade9teacherclass_id})
#SCIENCE TYPE
@method_decorator([login_required, headmin_required], name='dispatch') 
class Grd9_Update_science_teacher_type_regulator(UpdateView):
	model=Grade_9_Teacher_Class
	form_class=Update_Grade9_science_type
	template_name='Grade9Teach/Grd9_subject_type_reg/update_science_teacher_type.html'
	def get_succecc_url(self):
		Grade9teacherclass_id=self.kwargs['pk']
		return reverse_lazy('headmin:Grade_9_Teacher_list_details', kwargs={'pk':Grade9teacherclass_id})
#SOCIAL SCIENCE
@method_decorator([login_required, headmin_required], name='dispatch') 
class Grd9_Update_socialscience_teacher_type_regulator(UpdateView):
	model=Grade_9_Teacher_Class
	form_class=Update_Grade9_socialscience_type
	template_name='Grade9Teach/Grd9_subject_type_reg/update_socialscience_teacher_type.html'
	def get_succecc_url(self):
		Grade9teacherclass_id=self.kwargs['pk']
		return reverse_lazy('headmin:Grade_9_Teacher_list_details', kwargs={'pk':Grade9teacherclass_id})
#PERSONAL DEVELOPMENT
@method_decorator([login_required, headmin_required], name='dispatch') 
class Grd9_Update_persdev_teacher_type_regulator(UpdateView):
	model=Grade_9_Teacher_Class
	form_class=Update_Grade9_personaldevelopment_type
	template_name='Grade9Teach/Grd9_subject_type_reg/update_persdev_teacher_type.html'
	def get_succecc_url(self):
		Grade9teacherclass_id=self.kwargs['pk']
		return reverse_lazy('headmin:Grade_9_Teacher_list_details', kwargs={'pk':Grade9teacherclass_id})

