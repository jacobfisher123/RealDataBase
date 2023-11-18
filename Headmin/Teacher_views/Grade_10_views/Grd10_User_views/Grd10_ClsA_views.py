from django.shortcuts import render, redirect
from django import forms 
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView
from Teacher.Teacher_views.Grade9_views.Grd9_teacher_models import Grade_9_Teacher_Class
from .Grd9_ClsA_forms import TeacherGrd9_Class_SignUp_Form, TeacherGrd9_Class_SignUp_Detail_Form
from ....decorators import headmin_required
@method_decorator([login_required, headmin_required], name='dispatch') 
class Grade9_Teacher_signUp_view(CreateView):
	form_class=TeacherGrd9_Class_SignUp_Form
	model=Grade_9_Teacher_Class
	template_name='Grade9Teach/signup.html'
	def get_context_data(self,**kwargs):
		kwargs['user_type']='Grade 9 Teacher Registration'
		return super().get_context_data(**kwargs)
	def form_valid(self, form):
		user=form.save(commit=False)
		if  self.request.POST.get('Class')=='Select':

			return redirect('headmin:Grade9_Teacher_signUp_view')
		elif  self.request.POST.get('Class')=='is_Grade_9_teacher_classA':
			user.is_Grade_9_teacher_classA=True
			user.save()
			return redirect('headmin:Grade_9_teacher_list')

		elif self.request.POST.get('Class')=='is_Grade_9_teacher_classB':
			user.is_Grade_9_teacher_classB=True
			user.save()
			return redirect('headmin:Grade_9_teacher_list')
		elif self.request.POST.get('Class')=='is_Grade_9_teacher_classC':
			user.is_Grade_9_teacher_classC=True
			user.save()
			return redirect('headmin:Grade_9_teacher_list')
		elif self.request.POST.get('Class')=='is_Grade_9_teacher_classD':
			user.is_Grade_9_teacher_classD=True
			user.save()
			return redirect('headmin:Grade_9_teacher_list')
		elif self.request.POST.get('Class')=='is_Grade_9_teacher_classE':
			user.is_Grade_9_teacher_classE=True
			user.save()
			return redirect('headmin:Grade_9_teacher_list')
		elif self.request.POST.get('Class')=='is_Grade_9_teacher_classF':
			user.is_Grade_9_teacher_classF=True
			user.save()
			return redirect('headmin:Grade_9_teacher_list')
		elif self.request.POST.get('Class')=='is_Grade_9_teacher_classG':
			user.is_Grade_9_teacher_classG=True
			user.save()
			return redirect('headmin:Grade_9_teacher_list')
		elif self.request.POST.get('Class')=='is_Grade_9_teacher_classH':
			user.is_Grade_9_teacher_classH=True
			user.save()
			return redirect('headmin:Grade_9_teacher_list')
		elif self.request.POST.get('Class')=='is_Grade_9_teacher_classI':
			user.is_Grade_9_teacher_classI=True
			user.save()
			return redirect('headmin:Grade_9_teacher_list')
		elif self.request.POST.get('Class')=='is_Grade_9_teacher_classJ':
			user.is_Grade_9_teacher_classJ=True
			user.save()
			return redirect('headmin:Grade_9_teacher_list')


@method_decorator([login_required, headmin_required], name='dispatch') 
class TeacherGrd9_Class_SignUp_Detail_view(UpdateView):
	form_class=TeacherGrd9_Class_SignUp_Detail_Form
	model=Grade_9_Teacher_Class
	template_name='Grade9Teach/signup.html'
	def get_context_data(self, **kwargs):
		kwargs['user_type']='Grade 9 Teacher: Class A'
		return super().get_context_data(**kwargs)
	def form_valid(self, form):
		user=form.save()
		return redirect('headmin:Grade_9_teacher_list')
