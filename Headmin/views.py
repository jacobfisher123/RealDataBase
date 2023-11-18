from django.shortcuts import render, redirect, get_object_or_404
#decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from Teacher.Teacher_views.Grade9_views.Grd9_teacher_models import Grade_9_Teacher_Class


from .models import Upcomeing_events, create_event, PostForm
from .decorators import headmin_required
@login_required
def homeView(request):

	if request.user.is_authenticated:
		#This executes the codes if the user is recognized as the admin
		if request.user.is_admin:
			return redirect("headmin:HeadminView")
		#This executes the codes if the user is recognized as a teacher
		elif request.user.is_teacher:
			#This executes the codes if the user is recognized as a grade 9 teacher
			if request.user.is_Grade_9_teacher:
				return redirect('Teacher:Grade9_classA_teacher')
					# return redirect('Teacher:Grade9_classA_teacher')
		
			#This executes the codes if the user is recognized as a grade 10 teacher
			elif request.user.is_Grade_10_teacher:
				if request.user.is_Grade_10_teacher_classA:
					return redirect('Teacher:Grade10_classA_teacher')
				elif request.user.is_Grade_10_teacher_classB:
					return redirect('Teacher:Grade10_classB_teacher')
				elif request.user.is_Grade_10_teacher_classC:
					return redirect('Teacher:Grade10_classC_teacher')
				elif request.user.is_Grade_10_teacher_classD:
					return redirect('Teacher:Grade10_classD_teacher')
				elif request.user.is_Grade_10_teacher_classE:
					return redirect('Teacher:Grade10_classE_teacher')
				elif request.user.is_Grade_10_teacher_classF:
					return redirect('Teacher:Grade10_classF_teacher')
				elif request.user.is_Grade_10_teacher_classG:
					return redirect('Teacher:Grade10_classG_teacher')
				elif request.user.is_Grade_10_teacher_classH:
					return redirect('Teacher:Grade10_classH_teacher')
				elif request.user.is_Grade_10_teacher_classI:
					return redirect('Teacher:Grade10_classI_teacher')
				elif request.user.is_Grade_10_teacher_classJ:
					return redirect('Teacher:Grade10_classJ_teacher')

			#This executes the codes if the user is recognized as a grade 11 teacher
			elif request.user.is_Grade_11_teacher:
				if request.user.is_Grade_11_teacher_classA:
					return redirect('Teacher:Grade11_classA_teacher')
				elif request.user.is_Grade_11_teacher_classB:
					return redirect('Teacher:Grade11_classB_teacher')
				elif request.user.is_Grade_11_teacher_classC:
					return redirect('Teacher:Grade11_classC_teacher')
				elif request.user.is_Grade_11_teacher_classD:
					return redirect('Teacher:Grade11_classD_teacher')
				elif request.user.is_Grade_11_teacher_classE:
					return redirect('Teacher:Grade11_classE_teacher')
				elif request.user.is_Grade_11_teacher_classF:
					return redirect('Teacher:Grade11_classF_teacher')
				elif request.user.is_Grade_11_teacher_classG:
					return redirect('Teacher:Grade11_classG_teacher')
				elif request.user.is_Grade_11_teacher_classH:
					return redirect('Teacher:Grade11_classH_teacher')
				elif request.user.is_Grade_11_teacher_classI:
					return redirect('Teacher:Grade11_classI_teacher')
				elif request.user.is_Grade_11_teacher_classJ:
					return redirect('Teacher:Grade11_classJ_teacher')

			#This executes the codes if the user is recognized as a grade 12 teacher 
			elif request.user.is_Grade_12_teacher:
				if request.user.is_Grade_12_teacher_classA:
					return redirect('Teacher:Grade12_classA_teacher')
				elif request.user.is_Grade_12_teacher_classB:
					return redirect('Teacher:Grade12_classB_teacher')
				elif request.user.is_Grade_12_teacher_classC:
					return redirect('Teacher:Grade12_classC_teacher')
				elif request.user.is_Grade_12_teacher_classD:
					return redirect('Teacher:Grade12_classD_teacher')
				elif request.user.is_Grade_12_teacher_classE:
					return redirect('Teacher:Grade12_classE_teacher')
				elif request.user.is_Grade_12_teacher_classF:
					return redirect('Teacher:Grade12_classF_teacher')
				elif request.user.is_Grade_12_teacher_classG:
					return redirect('Teacher:Grade12_classG_teacher')
				elif request.user.is_Grade_12_teacher_classH:
					return redirect('Teacher:Grade12_classH_teacher')
				elif request.user.is_Grade_12_teacher_classI:
					return redirect('Teacher:Grade12_classI_teacher')
				elif request.user.is_Grade_12_teacher_classJ:
					return redirect('Teacher:Grade12_classJ_teacher')
			else:
				#This just closes the code
				pass
		#This executes the codes if the user is recognized as a student

		elif request.user.is_student:
			return redirect("Student:Student:Grade9_class_student")
			#This executes the code if the user is recognized as a grade 9 students
			# if request.user.is_Grade_9_student:
			# 	return redirect("Student:Grade9_classA_student")
	else:
		print("not identified")
"""
				if request.user.is_Grade_9_student_classA:
					return redirect("Student:Grade9_classA_student")
				elif request.user.is_Grade_9_student_classB:
					return redirect("Student:Grade9_classB_student")
				elif request.user.is_Grade_9_student_classC:
					return redirect("Student:Grade9_classC_student")
				elif request.user.is_Grade_9_student_classD:
					return redirect("Student:Grade9_classD_student")
				elif request.user.is_Grade_9_student_classE:
					return redirect("Student:Grade9_classE_student")
				elif request.user.is_Grade_9_student_classF:
					return redirect("Student:Grade9_classF_student")
				elif request.user.is_Grade_9_student_classG:
					return redirect("Student:Grade9_classG_student")
				elif request.user.is_Grade_9_student_classH:
					return redirect("Student:Grade9_classH_student")
				elif request.user.is_Grade_9_student_classI:
					return redirect("Student:Grade9_classI_student")
				elif request.user.is_Grade_9_student_classJ:
					return redirect("Student:Grade9_classJ_student")
				else:
					return redirect("login")
"""
"""
			elif request.user.is_Grade_10_student:
				if request.user.is_Grade_10_student_classA:
					return redirect("Student:Grade10_classA_student")
				elif request.user.is_Grade_10_student_classB:
					return redirect("Student:Grade10_classB_student")
				elif request.user.is_Grade_10_student_classC:
					return redirect("Student:Grade10_classC_student")
				elif request.user.is_Grade_10_student_classD:
					return redirect("Student:Grade10_classD_student")
				elif request.user.is_Grade_10_student_classE:
					return redirect("Student:Grade10_classE_student")
				elif request.user.is_Grade_10_student_classF:
					return redirect("Student:Grade10_classF_student")
				elif request.user.is_Grade_10_student_classG:
					return redirect("Student:Grade10_classG_student")
				elif request.user.is_Grade_10_student_classH:
					return redirect("Student:Grade10_classH_student")
				elif request.user.is_Grade_10_student_classI:
					return redirect("Student:Grade10_classI_student")
				elif request.user.is_Grade_10_student_classJ:
					return redirect("Student:Grade10_classJ_student")
				else:
					pass
			elif request.user.is_Grade_11_student:
				if request.user.is_Grade_11_student_classA:
					return redirect("Student:Grade11_classA_student")
				elif request.user.is_Grade_11_student_classB:
					return redirect("Student:Grade11_classB_student")
				elif request.user.is_Grade_11_student_classC:
					return redirect("Student:Grade11_classC_student")
				elif request.user.is_Grade_11_student_classD:
					return redirect("Student:Grade11_classD_student")
				elif request.user.is_Grade_11_student_classE:
					return redirect("Student:Grade11_classE_student")
				elif request.user.is_Grade_11_student_classF:
					return redirect("Student:Grade11_classF_student")
				elif request.user.is_Grade_11_student_classG:
					return redirect("Student:Grade11_classG_student")
				elif request.user.is_Grade_11_student_classH:
					return redirect("Student:Grade11_classH_student")
				elif request.user.is_Grade_11_student_classI:
					return redirect("Student:Grade11_classI_student")
				elif request.user.is_Grade_11_student_classJ:
					return redirect("Student:Grade11_classJ_student")
				else:
					pass
			elif request.user.is_Grade_12_student:
				if request.user.is_Grade_12_student_classA:
					return redirect("Student:Grade12_classA_student")
				elif request.user.is_Grade_12_student_classB:
					return redirect("Student:Grade12_classB_student")
				elif request.user.is_Grade_12_student_classC:
					return redirect("Student:Grade12_classC_student")
				elif request.user.is_Grade_12_student_classD:
					return redirect("Student:Grade12_classD_student")
				elif request.user.is_Grade_12_student_classE:
					return redirect("Student:Grade12_classE_student")
				elif request.user.is_Grade_12_student_classF:
					return redirect("Student:Grade12_classF_student")
				elif request.user.is_Grade_12_student_classG:
					return redirect("Student:Grade12_classG_student")
				elif request.user.is_Grade_12_student_classH:
					return redirect("Student:Grade12_classH_student")
				elif request.user.is_Grade_12_student_classI:
					return redirect("Student:Grade12_classI_student")
				elif request.user.is_Grade_12_student_classJ:
					return redirect("Student:Grade12_classJ_student")
				else:
					pass
			else:
				return redirect("headmin:HeadminView")

"""
"""
#This code is used for the class based view
#@method_decorator([login_required, headmin_required], name='dispatch') 
@login_required
def Delete_admin_post(request, pk):
	admin_post=Upcomeing_events.objects.get(id=pk)
	admin_post.delete()
	return redirect('headmin:HeadminView')
"""	

@login_required
@headmin_required
def HeadminView(request):
	# create_event()
	Headmin_news=Upcomeing_events.objects.all()
	#Grade6Tall = get_object_or_404(Grade_6_Teacher_Class)
	total_teachers =Grade_9_Teacher_Class.objects.count()
	context = {'total_teachers': total_teachers, 'Headmin_news':Headmin_news, 'HeadminView':'active'}
	return render(request, 'headminView.html', context)

@login_required
@headmin_required
def all_teacher_list_view(request):
	context={'all_teacher_list_view':'active'}
	return render(request, 'Teacher_list.html', context)
	
@login_required
@headmin_required
def Display_all_teacher_list_view(request):
	context={'Display_all_teacher_list_view':'active'}
	return render(request, 'Display_all_teacher.html', context)


def post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm()
    return render(request,'post_news.html',{'form':form})

class Delete_post_view(DeleteView):
	model=Upcomeing_events
	template_name='delete_view.html'
	success_url="Teacher:Grade_9_students_clsA_lists"
	def get_success_url(self):
		return reverse(self.success_url)
	def get_context_data(self,**kwargs):
		#all_students = Grade_9_student_classA.objects.filter(id=pk)
		#class_teacher=Grade_9_teacher_classA.objects.all()
		#kwargs['students']=all_students
		#kwargs['teachers']=class_teacher
		return super().get_context_data(**kwargs)