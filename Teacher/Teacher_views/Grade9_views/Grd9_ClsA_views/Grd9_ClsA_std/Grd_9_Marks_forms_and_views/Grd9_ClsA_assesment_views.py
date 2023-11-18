# from django.shortcuts import render, redirect
# from django.urls import reverse_lazy
# from django.contrib.auth.decorators import login_required
# from ....Grade9_decorators import Grd9_ClsA_required
# #Term 1 forms
# #math A 1 forms
# from Teacher.Teacher_views.Grade9_views.Grd9_ClsA_views.Grd9_ClsA_std.Grd_9_Marks_forms_and_views.Grd9_ClsA_assesment_forms import Grd9_ClsA_math_Term_1_assesment1_form, Grd9_ClsA_math_Term_2_assesment2_form, Grd9_ClsA_math_Term_3_assesment3_form ,Grd9_ClsA_math_Term_4_assesment4_form#, TestassesmentTesting
# #english A 1 forms
# from Teacher.Teacher_views.Grade9_views.Grd9_ClsA_views.Grd9_ClsA_std.Grd_9_Marks_forms_and_views.Grd9_ClsA_assesment_forms import Grd9_ClsA_English_Term_1_assesment1_form, Grd9_ClsA_English_Term_2_assesment2_form, Grd9_ClsA_English_Term_3_assesment3_form ,Grd9_ClsA_English_Term_4_assesment4_form
# #Science forms
# from Teacher.Teacher_views.Grade9_views.Grd9_ClsA_views.Grd9_ClsA_std.Grd_9_Marks_forms_and_views.Grd9_ClsA_assesment_forms import (
# Grd9_ClsA_Science_Term_1_assesment1_form,
# Grd9_ClsA_Science_Term_2_assesment2_form,
# Grd9_ClsA_Science_Term_3_assesment3_form,
# Grd9_ClsA_Science_Term_4_assesment4_form
# )
# #Social science forms
# from Teacher.Teacher_views.Grade9_views.Grd9_ClsA_views.Grd9_ClsA_std.Grd_9_Marks_forms_and_views.Grd9_ClsA_assesment_forms import (
# Grd9_ClsA_SocialScience_Term_1_assesment1_form,
# Grd9_ClsA_SocialScience_Term_2_assesment2_form,
# Grd9_ClsA_SocialScience_Term_3_assesment3_form,
# Grd9_ClsA_SocialScience_Term_4_assesment4_form
# )
# #Personal development forms
# from Teacher.Teacher_views.Grade9_views.Grd9_ClsA_views.Grd9_ClsA_std.Grd_9_Marks_forms_and_views.Grd9_ClsA_assesment_forms import (
# Grd9_ClsA_PersonalDev_Term_1_assesment1_form,
# Grd9_ClsA_PersonalDev_Term_2_assesment2_form,
# Grd9_ClsA_PersonalDev_Term_3_assesment3_form,
# Grd9_ClsA_PersonalDev_Term_4_assesment4_form
# )

# from django.views.generic import UpdateView, CreateView
# from Student.student_views.Grade9_std_views.Grade9_models import Grade_9_Student
# from Student.student_views.Grade9_std_views.Grade9_models import Grade_9_student_classA#, Term_1_math_assesment
# from Teacher.Teacher_views.Grade9_views.Grd9_teacher_models import Grade_9_teacher_classA
# #from Headmin.models import Term_1_math_assesment
# #Term 1 
# #maths assesments models
# from Teacher.Teacher_views.Grade9_views.Grd9_assesment_models import (Grade_9_models_math_Term1_assesment_1, Grade_9_models_math_Term2_assesment_2, Grade_9_models_math_Term3_assesment_3, Grade_9_models_math_Term4_assesment_4)
# #English assesment models
# from Teacher.Teacher_views.Grade9_views.Grd9_assesment_models import (
# Grade_9_models_English_Term1_assesment_1,
# Grade_9_models_English_Term2_assesment_2,
# Grade_9_models_English_Term3_assesment_3,
# Grade_9_models_English_Term4_assesment_4
# )
# #science models
# from Teacher.Teacher_views.Grade9_views.Grd9_assesment_models import (
# Grade_9_models_Science_Term1_assesment_1,
# Grade_9_models_Science_Term2_assesment_2,
# Grade_9_models_Science_Term3_assesment_3,
# Grade_9_models_Science_Term4_assesment_4
# )
# #social science models
# from Teacher.Teacher_views.Grade9_views.Grd9_assesment_models import (
# Grade_9_models_SocialScience_Term1_assesment_1,
# Grade_9_models_SocialScience_Term2_assesment_2,
# Grade_9_models_SocialScience_Term3_assesment_3,
# Grade_9_models_SocialScience_Term4_assesment_4
# )
# #personal development 
# from Teacher.Teacher_views.Grade9_views.Grd9_assesment_models import (
# Grade_9_models_PersonalDev_Term1_assesment_1,
# Grade_9_models_PersonalDev_Term2_assesment_2,
# Grade_9_models_PersonalDev_Term3_assesment_3,
# Grade_9_models_PersonalDev_Term4_assesment_4
# )


# from Headmin.models import Account
# """
# #Write a create form view
# class Grd9_ClsA_math_Term_1_assesment1_createview(CreateView):
# 	form_class=Grd9_ClsA_math_Term_1_assesment1_form
# 	model=Grade_9_models_math_Term1_assesment_1
# 	template_name='Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html'
# 	def get_context_data(self, **kwargs):
# 		students=Grade_9_student_classA.objects.all()
# 		class_teacher=Grade_9_teacher_classA.objects.all()
# 		kwargs['students']=students
# 		kwargs['teachers']=class_teacher
# 		kwargs['user_type']='Maths Assesment 1'
# 		return super().get_context_data(**kwargs)
# 	def form_valid(self, form):
# 		instance=form.save(commit=False)
# 		instance.student_user_name=request.user(id=pk)
# 		return redirect('Teacher:Grade_9_students_clsA_lists')
# """
# """
# def TestassesmentTestingView(request, pk):
# 	std=Grade_9_Student.objects.filter(id=pk)
# 	if request.method=='POST':
# 		form=TestassesmentTesting(request.POST, request.FILES)
# 		if form.is_valid():
# 			instance=form.save(commit=False)
# 			instance.student_user_name=Grade_9_Student.objects.filter(id=pk)
# 			instance.save()
# 			return redirect('Teacher:Grade_9_students_clsA_lists')
# 	else:
# 		form=TestassesmentTesting()
# 	return render(request, 'Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html', {'form':form})

# """
# """

# 	form_class=TestassesmentTesting
# 	model=Grade_9_Student
# 	template_name='Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html'
# 	def get_context_data(self, **kwargs):
# 		students=Grade_9_student_classA.objects.all()
# 		class_teacher=Grade_9_teacher_classA.objects.all()
# 		kwargs['students']=students
# 		kwargs['teachers']=class_teacher
# 		kwargs['user_type']='Maths Assesment 1'
# 		return super().get_context_data(**kwargs)
# """

# def Grd9_ClsA_math_Term_1_assesment1_createview(request, pk):
# 	class_teacher=Grade_9_teacher_classA.objects.all()
# 	all_students = Grade_9_Student.objects.filter(id=pk)
	
# 	std=Grade_9_Student.objects.filter(id=pk)

# 	if request.method=='POST':
# 		form=Grd9_ClsA_math_Term_1_assesment1_form(request.POST, request.FILES)
# 		if form.is_valid():
# 			instance=form.save(commit=False)
# 			instance.user_Name=Grade_9_Student.objects.get(id=pk)
# 			instance.save()
# 			return redirect('Teacher:Grade_9_students_clsA_lists')
# 	else:
# 		form=Grd9_ClsA_math_Term_1_assesment1_form()
# 	return render(request, 'Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html', {'form':form, 'students':all_students, 'teachers':class_teacher})

# """
# class Grd9_ClsA_math_Term_1_assesment1_createview(CreateView):
# 	model=Grade_9_models_math_Term1_assesment_1
# 	form_class=Grd9_ClsA_math_Term_1_assesment1_form
# 	template_name='Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html'
	
# 	def form_valid(self, form):
# 		std=Grade_9_Student.objects.filter(id=pk)
# 		form.instance.user_Name=std
# 		return super().form_class(form)
# """
# class Grd9_ClsA_math_Term_1_assesment1_view(UpdateView):
# 	form_class=Grd9_ClsA_math_Term_1_assesment1_form
# 	model=Grade_9_models_math_Term1_assesment_1
# 	template_name='Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html'
# 	def get_context_data(self, **kwargs):
# 		#students=Grade_9_Student.objects.get(id=pk)
# 		class_teacher=Grade_9_teacher_classA.objects.all()
# 		#kwargs['students']=students
# 		kwargs['teachers']=class_teacher
# 		kwargs['user_type']='Maths Assesment 1'
# 		return super().get_context_data(**kwargs)
# 	def form_valid(self, form):
# 		form.save()
# 		return redirect('Teacher:Grade_9_students_clsA_lists')

# def Grd9_ClsA_math_Term_2_assesment2_createview(request, pk):
# 	class_teacher=Grade_9_teacher_classA.objects.all()
# 	all_students = Grade_9_Student.objects.filter(id=pk)
	
# 	std=Grade_9_Student.objects.filter(id=pk)

# 	if request.method=='POST':
# 		form=Grd9_ClsA_math_Term_2_assesment2_form(request.POST, request.FILES)
# 		if form.is_valid():
# 			instance=form.save(commit=False)
# 			instance.user_Name=Grade_9_Student.objects.get(id=pk)
# 			instance.save()
# 			return redirect('Teacher:Grade_9_students_clsA_lists')
# 	else:
# 		form=Grd9_ClsA_math_Term_2_assesment2_form()
# 	return render(request, 'Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html', {'form':form, 'students':all_students, 'teachers':class_teacher})

# class Grd9_ClsA_math_Term_2_assesment2_view(UpdateView):
# 	form_class=Grd9_ClsA_math_Term_2_assesment2_form
# 	model=Grade_9_models_math_Term2_assesment_2
# 	template_name='Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html'
# 	def get_context_data(self, **kwargs):
# 		students=Grade_9_student_classA.objects.all()
# 		class_teacher=Grade_9_teacher_classA.objects.all()
# 		kwargs['students']=students
# 		kwargs['teachers']=class_teacher
# 		kwargs['user_type']='Maths Assesment 2'
# 		return super().get_context_data(**kwargs)
# 	def form_valid(self, form):
# 		form.save()
# 		return redirect('Teacher:Grade_9_students_clsA_lists')
# def Grd9_ClsA_math_Term_3_assesment3_createview(request, pk):
# 	class_teacher=Grade_9_teacher_classA.objects.all()
# 	all_students = Grade_9_Student.objects.filter(id=pk)
	
# 	std=Grade_9_Student.objects.filter(id=pk)

# 	if request.method=='POST':
# 		form=Grd9_ClsA_math_Term_3_assesment3_form(request.POST, request.FILES)
# 		if form.is_valid():
# 			instance=form.save(commit=False)
# 			instance.user_Name=Grade_9_Student.objects.get(id=pk)
# 			instance.save()
# 			return redirect('Teacher:Grade_9_students_clsA_lists')
# 	else:
# 		form=Grd9_ClsA_math_Term_3_assesment3_form()
# 	return render(request, 'Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html', {'form':form, 'students':all_students, 'teachers':class_teacher})

# class Grd9_ClsA_math_Term_3_assesment3_view(UpdateView):
# 	form_class=Grd9_ClsA_math_Term_3_assesment3_form
# 	model=Grade_9_models_math_Term3_assesment_3
# 	template_name='Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html'
# 	def get_context_data(self, **kwargs):
# 		students=Grade_9_student_classA.objects.all()
# 		class_teacher=Grade_9_teacher_classA.objects.all()
# 		kwargs['students']=students
# 		kwargs['teachers']=class_teacher
# 		kwargs['user_type']='Maths Assesment 3'
# 		return super().get_context_data(**kwargs)
# 	def form_valid(self, form):
# 		form.save()
# 		return redirect('Teacher:Grade_9_students_clsA_lists')
# def Grd9_ClsA_math_Term_4_assesment4_createview(request, pk):
# 	class_teacher=Grade_9_teacher_classA.objects.all()
# 	all_students = Grade_9_Student.objects.filter(id=pk)
	
# 	std=Grade_9_Student.objects.filter(id=pk)

# 	if request.method=='POST':
# 		form=Grd9_ClsA_math_Term_4_assesment4_form(request.POST, request.FILES)
# 		if form.is_valid():
# 			instance=form.save(commit=False)
# 			instance.user_Name=Grade_9_Student.objects.get(id=pk)
# 			instance.save()
# 			return redirect('Teacher:Grade_9_students_clsA_lists')
# 	else:
# 		form=Grd9_ClsA_math_Term_4_assesment4_form()
# 	return render(request, 'Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html', {'form':form, 'students':all_students, 'teachers':class_teacher})

# class Grd9_ClsA_math_Term_4_assesment4_view(UpdateView):
# 	form_class=Grd9_ClsA_math_Term_4_assesment4_form
# 	model=Grade_9_models_math_Term4_assesment_4
# 	template_name='Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html'
# 	def get_context_data(self, **kwargs):
# 		students=Grade_9_student_classA.objects.all()
# 		class_teacher=Grade_9_teacher_classA.objects.all()
# 		kwargs['students']=students
# 		kwargs['teachers']=class_teacher
# 		kwargs['user_type']='Maths Assesment 4'
# 		return super().get_context_data(**kwargs)
# 	def form_valid(self, form):
# 		form.save()
# 		return redirect('Teacher:Grade_9_students_clsA_lists')



# #ENGLISH
# def Grd9_ClsA_English_Term_1_assesment1_createview(request, pk):
# 	class_teacher=Grade_9_teacher_classA.objects.all()
# 	all_students = Grade_9_Student.objects.filter(id=pk)
	
# 	std=Grade_9_Student.objects.filter(id=pk)
	
# 	if request.method=='POST':
# 		form=Grd9_ClsA_English_Term_1_assesment1_form(request.POST, request.FILES)
# 		if form.is_valid():
# 			instance=form.save(commit=False)
# 			instance.user_Name=Grade_9_Student.objects.get(id=pk)
# 			instance.save()
# 			return redirect('Teacher:Grade_9_students_clsA_lists')
# 	else:
# 		form=Grd9_ClsA_English_Term_1_assesment1_form()
# 	return render(request, 'Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html', {'form':form, 'students':all_students, 'teachers':class_teacher})



# #English assesments 1
# class Grd9_ClsA_English_Term_1_assesment1_view(UpdateView):
# 	form_class=Grd9_ClsA_English_Term_1_assesment1_form
# 	model=Grade_9_models_English_Term1_assesment_1
# 	template_name='Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html'
# 	def get_context_data(self, **kwargs):
# 		#students=Grade_9_Student.objects.get(id=pk)
# 		class_teacher=Grade_9_teacher_classA.objects.all()
# 		#kwargs['students']=students
# 		kwargs['teachers']=class_teacher
# 		kwargs['user_type']='English Assesment 1'
# 		return super().get_context_data(**kwargs)
# 	def form_valid(self, form):
# 		form.save()
# 		return redirect('Teacher:Grade_9_students_clsA_lists')
# """
# 	def get_success_url(self):
# 		Grade9studentclassA_id = self.kwargs['pk']
# 		return reverse_lazy('Teacher:student_details_Grd9_clsA',  kwargs={'pk': Grade9studentclassA_id})
# """

# def Grd9_ClsA_English_Term_2_assesment2_createview(request, pk):
# 	class_teacher=Grade_9_teacher_classA.objects.all()
# 	all_students = Grade_9_Student.objects.filter(id=pk)
	
# 	std=Grade_9_Student.objects.filter(id=pk)
	
# 	if request.method=='POST':
# 		form=Grd9_ClsA_English_Term_2_assesment2_form(request.POST, request.FILES)
# 		if form.is_valid():
# 			instance=form.save(commit=False)
# 			instance.user_Name=Grade_9_Student.objects.get(id=pk)
# 			instance.save()
# 			return redirect('Teacher:Grade_9_students_clsA_lists')
# 	else:
# 		form=Grd9_ClsA_English_Term_2_assesment2_form()
# 	return render(request, 'Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html', {'form':form, 'students':all_students, 'teachers':class_teacher})

# class Grd9_ClsA_English_Term_2_assesment2_view(UpdateView):
# 	form_class=Grd9_ClsA_English_Term_2_assesment2_form
# 	model=Grade_9_models_English_Term2_assesment_2
# 	template_name='Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html'
# 	def get_context_data(self, **kwargs):
# 		students=Grade_9_student_classA.objects.all()
# 		class_teacher=Grade_9_teacher_classA.objects.all()
# 		kwargs['students']=students
# 		kwargs['teachers']=class_teacher
# 		kwargs['user_type']='English Assesment 2'
# 		return super().get_context_data(**kwargs)
# 	def form_valid(self, form):
# 		form.save()
# 		return redirect('Teacher:Grade_9_students_clsA_lists')
# def Grd9_ClsA_English_Term_3_assesment3_createview(request, pk):
# 	class_teacher=Grade_9_teacher_classA.objects.all()
# 	all_students = Grade_9_Student.objects.filter(id=pk)
	
# 	std=Grade_9_Student.objects.filter(id=pk)
	
# 	if request.method=='POST':
# 		form=Grd9_ClsA_English_Term_3_assesment3_form(request.POST, request.FILES)
# 		if form.is_valid():
# 			instance=form.save(commit=False)
# 			instance.user_Name=Grade_9_Student.objects.get(id=pk)
# 			instance.save()
# 			return redirect('Teacher:Grade_9_students_clsA_lists')
# 	else:
# 		form=Grd9_ClsA_English_Term_3_assesment3_form()
# 	return render(request, 'Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html', {'form':form, 'students':all_students, 'teachers':class_teacher})

# class Grd9_ClsA_English_Term_3_assesment3_view(UpdateView):
# 	form_class=Grd9_ClsA_English_Term_3_assesment3_form
# 	model=Grade_9_models_English_Term3_assesment_3
# 	template_name='Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html'
# 	def get_context_data(self, **kwargs):
# 		students=Grade_9_student_classA.objects.all()
# 		class_teacher=Grade_9_teacher_classA.objects.all()
# 		kwargs['students']=students
# 		kwargs['teachers']=class_teacher
# 		kwargs['user_type']='English Assesment 3'
# 		return super().get_context_data(**kwargs)
# 	def form_valid(self, form):
# 		form.save()
# 		return redirect('Teacher:Grade_9_students_clsA_lists')
# def Grd9_ClsA_English_Term_4_assesment4_createview(request, pk):
# 	class_teacher=Grade_9_teacher_classA.objects.all()
# 	all_students = Grade_9_Student.objects.filter(id=pk)
	
# 	std=Grade_9_Student.objects.filter(id=pk)
	
# 	if request.method=='POST':
# 		form=Grd9_ClsA_English_Term_4_assesment4_form(request.POST, request.FILES)
# 		if form.is_valid():
# 			instance=form.save(commit=False)
# 			instance.user_Name=Grade_9_Student.objects.get(id=pk)
# 			instance.save()
# 			return redirect('Teacher:Grade_9_students_clsA_lists')
# 	else:
# 		form=Grd9_ClsA_English_Term_4_assesment4_form()
# 	return render(request, 'Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html', {'form':form, 'students':all_students, 'teachers':class_teacher})

# class Grd9_ClsA_English_Term_4_assesment4_view(UpdateView):
# 	form_class=Grd9_ClsA_English_Term_4_assesment4_form
# 	model=Grade_9_models_English_Term4_assesment_4
# 	template_name='Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html'
# 	def get_context_data(self, **kwargs):
# 		students=Grade_9_student_classA.objects.all()
# 		class_teacher=Grade_9_teacher_classA.objects.all()
# 		kwargs['students']=students
# 		kwargs['teachers']=class_teacher
# 		kwargs['user_type']='English Assesment 4'
# 		return super().get_context_data(**kwargs)
# 	def form_valid(self, form):
# 		form.save()
# 		return redirect('Teacher:Grade_9_students_clsA_lists')
# #SCIENCE
# #Science assesments 1
# def Grd9_ClsA_Science_Term_1_assesment1_createview(request, pk):
# 	class_teacher=Grade_9_teacher_classA.objects.all()
# 	all_students = Grade_9_Student.objects.filter(id=pk)
	
# 	std=Grade_9_Student.objects.filter(id=pk)
	
# 	if request.method=='POST':
# 		form=Grd9_ClsA_Science_Term_1_assesment1_form(request.POST, request.FILES)
# 		if form.is_valid():
# 			instance=form.save(commit=False)
# 			instance.user_Name=Grade_9_Student.objects.get(id=pk)
# 			instance.save()
# 			return redirect('Teacher:Grade_9_students_clsA_lists')
# 	else:
# 		form=Grd9_ClsA_Science_Term_1_assesment1_form()
# 	return render(request, 'Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html', {'form':form, 'students':all_students, 'teachers':class_teacher})

# class Grd9_ClsA_Science_Term_1_assesment1_view(UpdateView):
# 	form_class=Grd9_ClsA_Science_Term_1_assesment1_form
# 	model=Grade_9_models_Science_Term1_assesment_1
# 	template_name='Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html'
# 	def get_context_data(self, **kwargs):
# 		students=Grade_9_Student.objects.get(id=pk)
# 		class_teacher=Grade_9_teacher_classA.objects.all()
# 		kwargs['students']=students
# 		kwargs['teachers']=class_teacher
# 		kwargs['user_type']='English Assesment 1'
# 		return super().get_context_data(**kwargs)
# 	def form_valid(self, form):
# 		form.save()
# 		return redirect('Teacher:Grade_9_students_clsA_lists')\
# #Science assesments 2
# def Grd9_ClsA_Science_Term_2_assesment2_createview(request, pk):
# 	class_teacher=Grade_9_teacher_classA.objects.all()
# 	all_students = Grade_9_Student.objects.filter(id=pk)
	
# 	std=Grade_9_Student.objects.filter(id=pk)
	
# 	if request.method=='POST':
# 		form=Grd9_ClsA_Science_Term_2_assesment2_form(request.POST, request.FILES)
# 		if form.is_valid():
# 			instance=form.save(commit=False)
# 			instance.user_Name=Grade_9_Student.objects.get(id=pk)
# 			instance.save()
# 			return redirect('Teacher:Grade_9_students_clsA_lists')
# 	else:
# 		form=Grd9_ClsA_Science_Term_2_assesment2_form()
# 	return render(request, 'Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html', {'form':form, 'students':all_students, 'teachers':class_teacher})

# class Grd9_ClsA_Science_Term_2_assesment2_view(UpdateView):
# 	form_class=Grd9_ClsA_Science_Term_2_assesment2_form
# 	model=Grade_9_models_Science_Term2_assesment_2
# 	template_name='Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html'
# 	def get_context_data(self, **kwargs):
# 		students=Grade_9_Student.objects.get(id=pk)
# 		class_teacher=Grade_9_teacher_classA.objects.all()
# 		kwargs['students']=students
# 		kwargs['teachers']=class_teacher
# 		kwargs['user_type']='English Assesment 1'
# 		return super().get_context_data(**kwargs)
# 	def form_valid(self, form):
# 		form.save()
# 		return redirect('Teacher:Grade_9_students_clsA_lists')
# #Science assesments 3
# def Grd9_ClsA_Science_Term_3_assesment3_createview(request, pk):
# 	class_teacher=Grade_9_teacher_classA.objects.all()
# 	all_students = Grade_9_Student.objects.filter(id=pk)
	
# 	std=Grade_9_Student.objects.filter(id=pk)
	
# 	if request.method=='POST':
# 		form=Grd9_ClsA_Science_Term_3_assesment3_form(request.POST, request.FILES)
# 		if form.is_valid():
# 			instance=form.save(commit=False)
# 			instance.user_Name=Grade_9_Student.objects.get(id=pk)
# 			instance.save()
# 			return redirect('Teacher:Grade_9_students_clsA_lists')
# 	else:
# 		form=Grd9_ClsA_Science_Term_3_assesment3_form()
# 	return render(request, 'Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html', {'form':form, 'students':all_students, 'teachers':class_teacher})

# class Grd9_ClsA_Science_Term_3_assesment3_view(UpdateView):
# 	form_class=Grd9_ClsA_Science_Term_3_assesment3_form
# 	model=Grade_9_models_Science_Term3_assesment_3
# 	template_name='Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html'
# 	def get_context_data(self, **kwargs):
# 		students=Grade_9_Student.objects.get(id=pk)
# 		class_teacher=Grade_9_teacher_classA.objects.all()
# 		kwargs['students']=students
# 		kwargs['teachers']=class_teacher
# 		kwargs['user_type']='English Assesment 1'
# 		return super().get_context_data(**kwargs)
# 	def form_valid(self, form):
# 		form.save()
# 		return redirect('Teacher:Grade_9_students_clsA_lists')
# #Science assesments 4
# def Grd9_ClsA_Science_Term_4_assesment4_createview(request, pk):
# 	class_teacher=Grade_9_teacher_classA.objects.all()
# 	all_students = Grade_9_Student.objects.filter(id=pk)
	
# 	std=Grade_9_Student.objects.filter(id=pk)
	
# 	if request.method=='POST':
# 		form=Grd9_ClsA_Science_Term_4_assesment4_form(request.POST, request.FILES)
# 		if form.is_valid():
# 			instance=form.save(commit=False)
# 			instance.user_Name=Grade_9_Student.objects.get(id=pk)
# 			instance.save()
# 			return redirect('Teacher:Grade_9_students_clsA_lists')
# 	else:
# 		form=Grd9_ClsA_Science_Term_4_assesment4_form()
# 	return render(request, 'Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html', {'form':form, 'students':all_students, 'teachers':class_teacher})

# class Grd9_ClsA_Science_Term_4_assesment4_view(UpdateView):
# 	form_class=Grd9_ClsA_Science_Term_4_assesment4_form
# 	model=Grade_9_models_Science_Term4_assesment_4
# 	template_name='Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html'
# 	def get_context_data(self, **kwargs):
# 		students=Grade_9_Student.objects.get(id=pk)
# 		class_teacher=Grade_9_teacher_classA.objects.all()
# 		kwargs['students']=students
# 		kwargs['teachers']=class_teacher
# 		kwargs['user_type']='English Assesment 1'
# 		return super().get_context_data(**kwargs)
# 	def form_valid(self, form):
# 		form.save()
# 		return redirect('Teacher:Grade_9_students_clsA_lists')
# #SOCIAL SCIENCE ASSESMENT 
# #Social Science assesments 1
# def Grd9_ClsA_SocialScn_Term_1_assesment1_createview(request, pk):
# 	class_teacher=Grade_9_teacher_classA.objects.all()
# 	all_students = Grade_9_Student.objects.filter(id=pk)
	
# 	std=Grade_9_Student.objects.filter(id=pk)
	
# 	if request.method=='POST':
# 		form=Grd9_ClsA_SocialScience_Term_1_assesment1_form(request.POST, request.FILES)
# 		if form.is_valid():
# 			instance=form.save(commit=False)
# 			instance.user_Name=Grade_9_Student.objects.get(id=pk)
# 			instance.save()
# 			return redirect('Teacher:Grade_9_students_clsA_lists')
# 	else:
# 		form=Grd9_ClsA_SocialScience_Term_1_assesment1_form()
# 	return render(request, 'Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html', {'form':form, 'students':all_students, 'teachers':class_teacher})

# class Grd9_ClsA_SocialScn_Term_1_assesment1_view(UpdateView):
# 	form_class=Grd9_ClsA_SocialScience_Term_1_assesment1_form
# 	model=Grade_9_models_SocialScience_Term1_assesment_1
# 	template_name='Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html'
# 	def get_context_data(self, **kwargs):
# 		students=Grade_9_Student.objects.get(id=pk)
# 		class_teacher=Grade_9_teacher_classA.objects.all()
# 		kwargs['students']=students
# 		kwargs['teachers']=class_teacher
# 		kwargs['user_type']='English Assesment 1'
# 		return super().get_context_data(**kwargs)
# 	def form_valid(self, form):
# 		form.save()
# 		return redirect('Teacher:Grade_9_students_clsA_lists')
# #Social Science assesments 2
# def Grd9_ClsA_SocialScn_Term_2_assesment2_createview(request, pk):
# 	class_teacher=Grade_9_teacher_classA.objects.all()
# 	all_students = Grade_9_Student.objects.filter(id=pk)
	
# 	std=Grade_9_Student.objects.filter(id=pk)
	
# 	if request.method=='POST':
# 		form=Grd9_ClsA_SocialScience_Term_2_assesment2_form(request.POST, request.FILES)
# 		if form.is_valid():
# 			instance=form.save(commit=False)
# 			instance.user_Name=Grade_9_Student.objects.get(id=pk)
# 			instance.save()
# 			return redirect('Teacher:Grade_9_students_clsA_lists')
# 	else:
# 		form=Grd9_ClsA_SocialScience_Term_2_assesment2_form()
# 	return render(request, 'Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html', {'form':form, 'students':all_students, 'teachers':class_teacher})

# class Grd9_ClsA_SocialScn_Term_2_assesment2_view(UpdateView):
# 	form_class=Grd9_ClsA_SocialScience_Term_2_assesment2_form
# 	model=Grade_9_models_SocialScience_Term2_assesment_2
# 	template_name='Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html'
# 	def get_context_data(self, **kwargs):
# 		students=Grade_9_Student.objects.get(id=pk)
# 		class_teacher=Grade_9_teacher_classA.objects.all()
# 		kwargs['students']=students
# 		kwargs['teachers']=class_teacher
# 		kwargs['user_type']='English Assesment 1'
# 		return super().get_context_data(**kwargs)
# 	def form_valid(self, form):
# 		form.save()
# 		return redirect('Teacher:Grade_9_students_clsA_lists')
# #Social Science assesments 3
# def Grd9_ClsA_SocialScn_Term_3_assesment3_createview(request, pk):
# 	class_teacher=Grade_9_teacher_classA.objects.all()
# 	all_students = Grade_9_Student.objects.filter(id=pk)
	
# 	std=Grade_9_Student.objects.filter(id=pk)
	
# 	if request.method=='POST':
# 		form=Grd9_ClsA_SocialScience_Term_3_assesment3_form(request.POST, request.FILES)
# 		if form.is_valid():
# 			instance=form.save(commit=False)
# 			instance.user_Name=Grade_9_Student.objects.get(id=pk)
# 			instance.save()
# 			return redirect('Teacher:Grade_9_students_clsA_lists')
# 	else:
# 		form=Grd9_ClsA_SocialScience_Term_3_assesment3_form()
# 	return render(request, 'Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html', {'form':form, 'students':all_students, 'teachers':class_teacher})

# class Grd9_ClsA_SocialScn_Term_3_assesment3_view(UpdateView):
# 	form_class=Grd9_ClsA_SocialScience_Term_3_assesment3_form
# 	model=Grade_9_models_SocialScience_Term3_assesment_3
# 	template_name='Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html'
# 	def get_context_data(self, **kwargs):
# 		students=Grade_9_Student.objects.get(id=pk)
# 		class_teacher=Grade_9_teacher_classA.objects.all()
# 		kwargs['students']=students
# 		kwargs['teachers']=class_teacher
# 		kwargs['user_type']='English Assesment 1'
# 		return super().get_context_data(**kwargs)
# 	def form_valid(self, form):
# 		form.save()
# 		return redirect('Teacher:Grade_9_students_clsA_lists')
# #Social Science assesments 4
# def Grd9_ClsA_SocialScn_Term_4_assesment4_createview(request, pk):
# 	class_teacher=Grade_9_teacher_classA.objects.all()
# 	all_students = Grade_9_Student.objects.filter(id=pk)
	
# 	std=Grade_9_Student.objects.filter(id=pk)
	
# 	if request.method=='POST':
# 		form=Grd9_ClsA_SocialScience_Term_4_assesment4_form(request.POST, request.FILES)
# 		if form.is_valid():
# 			instance=form.save(commit=False)
# 			instance.user_Name=Grade_9_Student.objects.get(id=pk)
# 			instance.save()
# 			return redirect('Teacher:Grade_9_students_clsA_lists')
# 	else:
# 		form=Grd9_ClsA_SocialScience_Term_4_assesment4_form()
# 	return render(request, 'Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html', {'form':form, 'students':all_students, 'teachers':class_teacher})

# class Grd9_ClsA_SocialScn_Term_4_assesment4_view(UpdateView):
# 	form_class=Grd9_ClsA_SocialScience_Term_4_assesment4_form
# 	model=Grade_9_models_SocialScience_Term4_assesment_4
# 	template_name='Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html'
# 	def get_context_data(self, **kwargs):
# 		students=Grade_9_Student.objects.get(id=pk)
# 		class_teacher=Grade_9_teacher_classA.objects.all()
# 		kwargs['students']=students
# 		kwargs['teachers']=class_teacher
# 		kwargs['user_type']='English Assesment 1'
# 		return super().get_context_data(**kwargs)
# 	def form_valid(self, form):
# 		form.save()
# 		return redirect('Teacher:Grade_9_students_clsA_lists')

# #SOCIAL SCIENCE ASSESMENT 
# #Personal Development assesments 1
# def Grd9_ClsA_PersonalDev_Term_1_assesment1_createview(request, pk):
# 	class_teacher=Grade_9_teacher_classA.objects.all()
# 	all_students = Grade_9_Student.objects.filter(id=pk)
	
# 	std=Grade_9_Student.objects.filter(id=pk)
	
# 	if request.method=='POST':
# 		form=Grd9_ClsA_PersonalDev_Term_1_assesment1_form(request.POST, request.FILES)
# 		if form.is_valid():
# 			instance=form.save(commit=False)
# 			instance.user_Name=Grade_9_Student.objects.get(id=pk)
# 			instance.save()
# 			return redirect('Teacher:Grade_9_students_clsA_lists')
# 	else:
# 		form=Grd9_ClsA_PersonalDev_Term_1_assesment1_form()
# 	return render(request, 'Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html', {'form':form, 'students':all_students, 'teachers':class_teacher})

# class Grd9_ClsA_PersonalDev_Term_1_assesment1_view(UpdateView):
# 	form_class=Grd9_ClsA_PersonalDev_Term_1_assesment1_form 
# 	model=Grade_9_models_PersonalDev_Term1_assesment_1
# 	template_name='Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html'
# 	def get_context_data(self, **kwargs):
# 		students=Grade_9_Student.objects.get(id=pk)
# 		class_teacher=Grade_9_teacher_classA.objects.all()
# 		kwargs['students']=students
# 		kwargs['teachers']=class_teacher
# 		kwargs['user_type']='English Assesment 1'
# 		return super().get_context_data(**kwargs)
# 	def form_valid(self, form):
# 		form.save()
# 		return redirect('Teacher:Grade_9_students_clsA_lists')
# #Personal Development assesments 2
# def Grd9_ClsA_PersonalDev_Term_2_assesment2_createview(request, pk):
# 	class_teacher=Grade_9_teacher_classA.objects.all()
# 	all_students = Grade_9_Student.objects.filter(id=pk)
	
# 	std=Grade_9_Student.objects.filter(id=pk)
	
# 	if request.method=='POST':
# 		form=Grd9_ClsA_PersonalDev_Term_2_assesment2_form(request.POST, request.FILES)
# 		if form.is_valid():
# 			instance=form.save(commit=False)
# 			instance.user_Name=Grade_9_Student.objects.get(id=pk)
# 			instance.save()
# 			return redirect('Teacher:Grade_9_students_clsA_lists')
# 	else:
# 		form=Grd9_ClsA_PersonalDev_Term_2_assesment2_form()
# 	return render(request, 'Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html', {'form':form, 'students':all_students, 'teachers':class_teacher})

# class Grd9_ClsA_PersonalDev_Term_2_assesment2_view(UpdateView):
# 	form_class=Grd9_ClsA_PersonalDev_Term_2_assesment2_form
# 	model=Grade_9_models_PersonalDev_Term2_assesment_2 
# 	template_name='Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html'
# 	def get_context_data(self, **kwargs):
# 		students=Grade_9_Student.objects.get(id=pk)
# 		class_teacher=Grade_9_teacher_classA.objects.all()
# 		kwargs['students']=students
# 		kwargs['teachers']=class_teacher
# 		kwargs['user_type']='English Assesment 1'
# 		return super().get_context_data(**kwargs)
# 	def form_valid(self, form):
# 		form.save()
# 		return redirect('Teacher:Grade_9_students_clsA_lists')
# #Personal Development assesments 3
# def Grd9_ClsA_PersonalDev_Term_3_assesment3_createview(request, pk):
# 	class_teacher=Grade_9_teacher_classA.objects.all()
# 	all_students = Grade_9_Student.objects.filter(id=pk)
	
# 	std=Grade_9_Student.objects.filter(id=pk)
	
# 	if request.method=='POST':
# 		form=Grd9_ClsA_PersonalDev_Term_3_assesment3_form(request.POST, request.FILES)
# 		if form.is_valid():
# 			instance=form.save(commit=False)
# 			instance.user_Name=Grade_9_Student.objects.get(id=pk)
# 			instance.save()
# 			return redirect('Teacher:Grade_9_students_clsA_lists')
# 	else:
# 		form=Grd9_ClsA_PersonalDev_Term_3_assesment3_form()
# 	return render(request, 'Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html', {'form':form, 'students':all_students, 'teachers':class_teacher})

# class Grd9_ClsA_PersonalDev_Term_3_assesment3_view(UpdateView):
# 	form_class=Grd9_ClsA_PersonalDev_Term_3_assesment3_form
# 	model=Grade_9_models_PersonalDev_Term3_assesment_3
# 	template_name='Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html'
# 	def get_context_data(self, **kwargs):
# 		students=Grade_9_Student.objects.get(id=pk)
# 		class_teacher=Grade_9_teacher_classA.objects.all()
# 		kwargs['students']=students
# 		kwargs['teachers']=class_teacher
# 		kwargs['user_type']='English Assesment 1'
# 		return super().get_context_data(**kwargs)
# 	def form_valid(self, form):
# 		form.save()
# 		return redirect('Teacher:Grade_9_students_clsA_lists')
# #Personal Development assesments 4
# def Grd9_ClsA_PersonalDev_Term_4_assesment4_createview(request, pk):
# 	class_teacher=Grade_9_teacher_classA.objects.all()
# 	all_students = Grade_9_Student.objects.filter(id=pk)
	
# 	std=Grade_9_Student.objects.filter(id=pk)
	
# 	if request.method=='POST':
# 		form=Grd9_ClsA_PersonalDev_Term_4_assesment4_form(request.POST, request.FILES)
# 		if form.is_valid():
# 			instance=form.save(commit=False)
# 			instance.user_Name=Grade_9_Student.objects.get(id=pk)
# 			instance.save()
# 			return redirect('Teacher:Grade_9_students_clsA_lists')
# 	else:
# 		form=Grd9_ClsA_PersonalDev_Term_4_assesment4_form()
# 	return render(request, 'Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html', {'form':form, 'students':all_students, 'teachers':class_teacher})

# class Grd9_ClsA_PersonalDev_Term_4_assesment4_view(UpdateView):
# 	form_class=Grd9_ClsA_PersonalDev_Term_4_assesment4_form
# 	model=Grade_9_models_PersonalDev_Term4_assesment_4
# 	template_name='Grade9Teach/Tgrd9A/Upload_assesments_subjects/upload_assesments.html'
# 	def get_context_data(self, **kwargs):
# 		students=Grade_9_Student.objects.get(id=pk)
# 		class_teacher=Grade_9_teacher_classA.objects.all()
# 		kwargs['students']=students
# 		kwargs['teachers']=class_teacher
# 		kwargs['user_type']='English Assesment 1'
# 		return super().get_context_data(**kwargs)

# 	def get_success_url(self):
# 		Grade9studentclassA_id = self.kwargs['pk']
# 		return reverse_lazy('Teacher:student_details_Grd9_clsA',  kwargs={'pk': Grade9studentclassA_id})

# @login_required
# @Grd9_ClsA_required
# def Delete_English_subject_A1(request, pk):
# 	subject=Grade_9_models_PersonalDev_Term4_assesment_4.objects.filter(id=pk)
# 	subject.delete()
# 	return redirect("Teacher:Grade_9_students_clsA_lists")
	
	
