from django.db import models
from django.urls import reverse_lazy, reverse 
from django import forms
from django.utils.decorators import method_decorator
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from Headmin.models import Account, Upcomeing_events
from ..Grade9_decorators import Grd9_ClsA_required

from django.contrib.postgres.search import SearchVector, SearchQuery
from Teacher.Teacher_views.Grade9_views.Grd9_teacher_models import Grade_9_Teacher_Class

from Student.student_views.Grade9_std_views.Grade9_models import Grade_9_Student, Term_11_math_assesment # Grade_9_Student
#this handles models of upload models
from post.models import Post,CommentCreationForm 
#This is the assesment models
#math models 

from Teacher.Teacher_views.Grade9_views.Grd9_assesment_models import (Grade_9_models_math_assesment,Grade_9_models_LanguageLiterature_assesment,
Grade_9_models_Science_assesment,
Grade_9_models_SocialScience_assesment,
Grade_9_models_Geography_assesment,
Grade_9_models_Chemistry_assesment,
Grade_9_models_PersonalDev_assesment)
from Teacher.Teacher_views.Grade9_views.Grd9_assesment_models import (
Grade_9_models_PersonalDev_assesment_Form,
Grade_9_models_math_assesment_Form,
Grade_9_models_SocialScience_assesment_Form,
Grade_9_models_Science_assesment_Form,
Grade_9_models_LanguageLiterature_assesment_Form,
Grade_9_models_Geography_assesment_Form,
Grade_9_models__Chemistry_assesment_Form,DeleteMathAssessmentForm
	)


from Teacher.Teacher_views.Grade9_views.Grd9_assesment_models import (Grade_9_models_math_files,Grade9mathFilesForm,Grade9ScienceFilesForm,
Grade9SocialScienceFilesForm,
Grade9LanguageLiteratureFilesForm,
Grade9GeographyFilesForm,
Grade9ChemistryFilesForm,
Grade9PersonalDevFilesForm)
from Teacher.Teacher_views.Grade9_views.Grd9_assesment_models import Grade9MathAssessment_Edit_Form

#this handles models of upload forms

#news models
from Teacher.Teacher_views.Grade9_views.Grd9_ClsA_views.Grd9ClsA_news_MVT import GrdClsA_news
'''
Grade9mathFilesForm

'''
from Headmin.models import PostForm
# userpost
# Admin_signal
# Teacher_signal
# Student
# title
# description
# posted_date
# student_boolean   

first_names = [
    "Liam",
    "Olivia",
    "Noah",
    "Emma",
    "Oliver",
    "Ava",
    "Elijah",
    "Charlotte",
    "William",
    "Sophia",
    "James",
    "Amelia",
    "Benjamin",
    "Mia",
    "Lucas",
    "Harper",
    "Henry",
    "Evelyn",
    "Alexander",
    "Abigail",
    "Samuel",
    "Emily",
    "Daniel",
    "Sofia",
    "Matthew",
    "Elizabeth",
    "Joseph",
    "Avery",
    "Jackson",
    "Ella"
]
last_names = [
    "Smith",
    "Johnson",
    "Brown",
    "Taylor",
    "Miller",
    "Anderson",
    "Wilson",
    "Moore",
    "Davis",
    "Jones",
    "Clark",
    "White",
    "Harris",
    "Young",
    "Hall",
    "Walker",
    "Lewis",
    "Lee",
    "Martin",
    "Perez",
    "Thompson",
    "Garcia",
    "Martinez",
    "Hernandez",
    "Gonzalez",
    "Rodriguez",
    "Lopez",
    "Hill",
    "Scott"
]
import random
import string

def generate_random_username(first_name, last_name):
    # Generate a random string of characters
    random_string = ''.join(random.choices(string.ascii_letters, k=6))
    
    # Combine the first name, last name, and random string to create a unique username
    username = f"{first_name.lower()}{last_name.lower()}{random_string}"

    return username

# Usage:


def create_grade_9_student(email, username, password, first_name, last_name):
    # Create a Grade 9 Student account
    if Grade_9_Student.objects.filter(first_name=first_name).count()>=1:
    	print("username existed")
    	pass
    elif Grade_9_Student.objects.filter(last_name=last_name).count()>=1:
    	print("username existed")
    	pass
    elif Grade_9_Student.objects.filter(first_name=first_name,last_name=last_name).count()>=1:
    	print("username existed")
    	pass
    else:
	    user = Grade_9_Student.objects.create_user(
	        email=email,
	        username=username,
	        password=password,
	        first_name=first_name,
	        last_name=last_name,
	    )

	    # You can set other fields specific to Grade 9 students here if needed
	    # user.Grade_9_student_classA = True
	    # user.Grade_9_student_classB = True
	    # ...

	    # Save the user object
	    user.save()
	    
	    # Retrieve the user you want to update using their id
	    user_to_update = Grade_9_Student.objects.get(id=user.id)

	    # Modify the fields of the user instance
	    user_to_update.is_student = True
	    user_to_update.is_Grade_9_student = True
	    user_to_update.is_Grade_9_student_classA = True

	    # Save the updated user instance
	    user_to_update.save()

	    return user
def create_random_user():
    for first_name in first_names:
        for last_name in last_names:
            username = generate_random_username(first_name, last_name)
            email = '{}@gmail.com'.format(username)  # Use lowercase first name as email
            username = username  # Use lowercase first name as username
            create_grade_9_student(email, username, 'yuriel117', first_name, last_name)
            print('------------------------------------------!!!USER CREATED!!!------------------------------------------')
            print(username,first_name, last_name)
            print('------------------------------------------!!!SUCCESS!!!------------------------------------------')



def class_teacher_checker(request,context):
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_Grade_9_teacher_classA=True):
		context['teacher_name_cls']='Teacher Class A'
		context['students_class']='List of Student Class A'
		context['students'] = Grade_9_Student.objects.filter(is_Grade_9_student_classA=True)
	elif Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_Grade_9_teacher_classB=True):
		context['teacher_name_cls']='Teacher Class B'
		context['students'] = Grade_9_Student.objects.filter(is_Grade_9_student_classB=True)
		context['students_class']='List of Student Class B'
	else:
		print("nope")

def class_teacher_subj_checker(request,context):
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,Grade_9_Math_subj_teach=True):
		context['Subject'] = 'Math Teacher'
		context['Subj'] = 'Math'
		
	elif Grade_9_Teacher_Class.objects.filter(id=request.user.id,Grade_9_Engl_subj_teach=True):
		context['Subject'] = 'English Teacher'
		context['Subj'] = 'English'
		
	elif Grade_9_Teacher_Class.objects.filter(id=request.user.id,Grade_9_Scn_subj_teach=True):
		context['Subject'] = 'Science Teacher'
		context['Subj'] = 'Science'
		
	elif Grade_9_Teacher_Class.objects.filter(id=request.user.id,Grade_9_SocSnc_subj_teach=True):
		context['Subject'] = 'Social Science Teacher'
		context['Subj'] = 'Social Science'
		
	elif Grade_9_Teacher_Class.objects.filter(id=request.user.id,Grade_9_PersDev_subj_teach=True):
		context['Subject'] = 'Perosnal Development Teacher'
		context['Subj'] = 'Perosnal Development'
		
	else:
		context['Subj'] = 'Not assisgned'
def Grade_9_Math_subj_view(request):
	return render(request,'Grade9Teach/Grade9_Student_subj_templates/Grade9_subj_templates')

def View_Uploaded_assesment(request):
	class_teacher=Grade_9_Teacher_Class.objects.filter(id=request.user.id)

	context={'teachers':class_teacher}
	class_teacher_subj_checker(request,context)
	class_teacher_checker(request,context)
	return render(request, 'Grade9Teach/Grade9_Student_subj_templates/View_Uploaded_assesment.html',context)

# Science_Title
# SocialScience_Title
# LanguageLiterature_Title
# Geography_Title
# Chemistry_Title

# Grade_9_Engl_subj_teach
# Grade_9_Scn_subj_teach
# Grade_9_SocSnc_subj_teach Grade9_classA_teacher
# Grade_9_PersDev_subj_teach

def post_view(request):
    class_teacher = Grade_9_Teacher_Class.objects.filter(id=request.user.id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.Teacher_signal = True
            for i in class_teacher:
                post = form.save(commit=False)  # Create a new Post instance but don't save it yet
                post.userpost = i  # Assign the userpost attribute
                post.save()  # Save the post to the database
            print("---------------------------------------------!!!success!!!---------------------------------------------")
            return redirect("Teacher:Grade9_classA_teacher")
    else:
        form = PostForm()
    
    context = {'teachers': class_teacher, 'form': form}
    class_teacher_subj_checker(request, context)
    class_teacher_checker(request, context)
    
    return render(request, 'Grade9Teach/Tgrd9A/G9T_post_news.html', context)


def View_Uploaded_assesment_Term12(request, tm):
    class_teacher = Grade_9_Teacher_Class.objects.filter(id=request.user.id)
    assessments_list = []

    subject_models = {
        'Math': Grade_9_models_math_assesment,
        'LanguageLiterature': Grade_9_models_LanguageLiterature_assesment,
        'Science': Grade_9_models_Science_assesment,
        'SocialScience': Grade_9_models_SocialScience_assesment,
        'PersonalDev': Grade_9_models_PersonalDev_assesment,
    }

    for subject, model in subject_models.items():
        if getattr(Grade_9_Teacher_Class.objects.filter(id=request.user.id), f'Grade_9_{subject}_subj_teach', False):
            unique_assessments = model.objects.filter(**{f'Term{tm}_assesment': True}).values('Title').distinct()
            if unique_assessments.count() >= 1:
                for assessment in unique_assessments:
                    latest_assessment = model.objects.filter(
                        **{f'Term{tm}_assesment': True},
                        Title=assessment['Title']
                    ).order_by('-DatePosted').first()
                    assessments_list.append(latest_assessment)

    context = {'subjects': assessments_list, 'teachers': class_teacher}

    class_teacher_subj_checker(request, context)
    class_teacher_checker(request, context)
    return render(request, 'Grade9Teach/Grade9_Student_subj_templates/View_Uploaded_assesment_Term1.html', context)


def View_Uploaded_assesment_Term1(request, tm): 
   
    class_teacher=Grade_9_Teacher_Class.objects.filter(id=request.user.id)
    assessments_list = []
    if Grade_9_Teacher_Class.objects.filter(id=request.user.id, Grade_9_Math_subj_teach=True):
	    if tm=="1":
	    	unique_assessments = Grade_9_models_math_assesment.objects.filter(Term1_assesment=True).values('Title').distinct()
	    	if Grade_9_models_math_assesment.objects.filter(Term1_assesment=True).values('Title').distinct().count()>=1:
			    for assessment in unique_assessments:
			        # Retrieve the latest assessment object for each unique title and term
			        latest_assessment = Grade_9_models_math_assesment.objects.filter(
			            Term1_assesment=True,
			            Title=assessment['Title']
			        ).order_by('-DatePosted').first()
			        assessments_list.append(latest_assessment)
	    if tm=="2":
	    	unique_assessments = Grade_9_models_math_assesment.objects.filter(Term2_assesment=True).values('Title').distinct()
	    	if Grade_9_models_math_assesment.objects.filter(Term2_assesment=True).count()>=1:
			    for assessment in unique_assessments:
			        # Retrieve the latest assessment object for each unique title and term
			        latest_assessment = Grade_9_models_math_assesment.objects.filter(
			            Term2_assesment=True,
			            Title=assessment['Title']
			        ).order_by('-DatePosted').first()
			        assessments_list.append(latest_assessment)
	    if tm=="3":
	    	unique_assessments = Grade_9_models_math_assesment.objects.filter(Term3_assesment=True).values('Title').distinct()
	    	for assessment in unique_assessments:
		        # Retrieve the latest assessment object for each unique title and term
		        latest_assessment = Grade_9_models_math_assesment.objects.filter(
		            Term3_assesment=True,
		            Title=assessment['Title']
		        ).order_by('-DatePosted').first()
		        assessments_list.append(latest_assessment)
	    if tm=="4":
	    	unique_assessments = Grade_9_models_math_assesment.objects.filter(Term4_assesment=True).values('Title').distinct()
	    	for assessment in unique_assessments:
		        # Retrieve the latest assessment object for each unique title and term
		        latest_assessment = Grade_9_models_math_assesment.objects.filter(
		            Term4_assesment=True,
		            Title=assessment['Title']
		        ).order_by('-DatePosted').first()
		        assessments_list.append(latest_assessment)
    if Grade_9_Teacher_Class.objects.filter(id=request.user.id, Grade_9_Engl_subj_teach=True):
	    if tm=="1":
	    	unique_assessments = Grade_9_models_LanguageLiterature_assesment.objects.filter(Term1_assesment=True).values('Title').distinct()
	    	if Grade_9_models_LanguageLiterature_assesment.objects.filter(Term1_assesment=True).values('Title').distinct().count()>=1:
			    for assessment in unique_assessments:
			        # Retrieve the latest assessment object for each unique title and term
			        latest_assessment = Grade_9_models_LanguageLiterature_assesment.objects.filter(
			            Term1_assesment=True,
			            Title=assessment['Title']
			        ).order_by('-DatePosted').first()
			        assessments_list.append(latest_assessment)
	    if tm=="2":
	    	unique_assessments = Grade_9_models_LanguageLiterature_assesment.objects.filter(Term2_assesment=True).values('Title').distinct()
	    	if Grade_9_models_LanguageLiterature_assesment.objects.filter(Term2_assesment=True).count()>=1:
			    for assessment in unique_assessments:
			        # Retrieve the latest assessment object for each unique title and term
			        latest_assessment = Grade_9_models_LanguageLiterature_assesment.objects.filter(
			            Term2_assesment=True,
			            Title=assessment['Title']
			        ).order_by('-DatePosted').first()
			        assessments_list.append(latest_assessment)
	    if tm=="3":
	    	unique_assessments = Grade_9_models_LanguageLiterature_assesment.objects.filter(Term3_assesment=True).values('Title').distinct()
	    	for assessment in unique_assessments:
		        # Retrieve the latest assessment object for each unique title and term
		        latest_assessment = Grade_9_models_LanguageLiterature_assesment.objects.filter(
		            Term3_assesment=True,
		            Title=assessment['Title']
		        ).order_by('-DatePosted').first()
		        assessments_list.append(latest_assessment)
	    if tm=="4":
	    	unique_assessments = Grade_9_models_LanguageLiterature_assesment.objects.filter(Term4_assesment=True).values('Maths_Title').distinct()
	    	for assessment in unique_assessments:
		        # Retrieve the latest assessment object for each unique title and term
		        latest_assessment = Grade_9_models_LanguageLiterature_assesment.objects.filter(
		            Term4_assesment=True,
		            Title=assessment['Title']
		        ).order_by('-DatePosted').first()
		        assessments_list.append(latest_assessment)
    if Grade_9_Teacher_Class.objects.filter(id=request.user.id, Grade_9_Scn_subj_teach=True):
	    if tm=="1":
	    	unique_assessments = Grade_9_models_Science_assesment.objects.filter(Term1_assesment=True).values('Title').distinct()
	    	if Grade_9_models_Science_assesment.objects.filter(Term1_assesment=True).values('Title').distinct().count()>=1:
			    for assessment in unique_assessments:
			        # Retrieve the latest assessment object for each unique title and term
			        latest_assessment = Grade_9_models_Science_assesment.objects.filter(
			            Term1_assesment=True,
			            Title=assessment['Title']
			        ).order_by('-DatePosted').first()
			        assessments_list.append(latest_assessment)
	    if tm=="2":
	    	unique_assessments = Grade_9_models_Science_assesment.objects.filter(Term2_assesment=True).values('Title').distinct()
	    	if Grade_9_models_Science_assesment.objects.filter(Term2_assesment=True).count()>=1:
			    for assessment in unique_assessments:
			        # Retrieve the latest assessment object for each unique title and term
			        latest_assessment = Grade_9_models_Science_assesment.objects.filter(
			            Term2_assesment=True,
			            LanguageLiterature_Title=assessment['Title']
			        ).order_by('-DatePosted').first()
			        assessments_list.append(latest_assessment)
	    if tm=="3":
	    	unique_assessments = Grade_9_models_Science_assesment.objects.filter(Term3_assesment=True).values('Title').distinct()
	    	for assessment in unique_assessments:
		        # Retrieve the latest assessment object for each unique title and term
		        latest_assessment = Grade_9_models_Science_assesment.objects.filter(
		            Term3_assesment=True,
		            LanguageLiterature_Title=assessment['Title']
		        ).order_by('-DatePosted').first()
		        assessments_list.append(latest_assessment)
	    if tm=="4":
	    	unique_assessments = Grade_9_models_Science_assesment.objects.filter(Term4_assesment=True).values('Title').distinct()
	    	for assessment in unique_assessments:
		        # Retrieve the latest assessment object for each unique title and term
		        latest_assessment = Grade_9_models_Science_assesment.objects.filter(
		            Term4_assesment=True,
		            LanguageLiterature_Title=assessment['Title']
		        ).order_by('-DatePosted').first()
		        assessments_list.append(latest_assessment)
    if Grade_9_Teacher_Class.objects.filter(id=request.user.id, Grade_9_SocSnc_subj_teach=True):
	    if tm=="1":
	    	unique_assessments = Grade_9_models_LanguageLiterature_assesment.objects.filter(Term1_assesment=True).values('Title').distinct()
	    	if Grade_9_models_LanguageLiterature_assesment.objects.filter(Term1_assesment=True).values('Title').distinct().count()>=1:
			    for assessment in unique_assessments:
			        # Retrieve the latest assessment object for each unique title and term
			        latest_assessment = Grade_9_models_LanguageLiterature_assesment.objects.filter(
			            Term1_assesment=True,
			            Title=assessment['Title']
			        ).order_by('-DatePosted').first()
			        assessments_list.append(latest_assessment)
	    if tm=="2":
	    	unique_assessments = Grade_9_models_LanguageLiterature_assesment.objects.filter(Term2_assesment=True).values('Title').distinct()
	    	if Grade_9_models_LanguageLiterature_assesment.objects.filter(Term2_assesment=True).count()>=1:
			    for assessment in unique_assessments:
			        # Retrieve the latest assessment object for each unique title and term
			        latest_assessment = Grade_9_models_LanguageLiterature_assesment.objects.filter(
			            Term2_assesment=True,
			            Title=assessment['Title']
			        ).order_by('-DatePosted').first()
			        assessments_list.append(latest_assessment)
	    if tm=="3":
	    	unique_assessments = Grade_9_models_LanguageLiterature_assesment.objects.filter(Term3_assesment=True).values('Title').distinct()
	    	for assessment in unique_assessments:
		        # Retrieve the latest assessment object for each unique title and term
		        latest_assessment = Grade_9_models_LanguageLiterature_assesment.objects.filter(
		            Term3_assesment=True,
		            Title=assessment['Title']
		        ).order_by('-DatePosted').first()
		        assessments_list.append(latest_assessment)
	    if tm=="4":
	    	unique_assessments = Grade_9_models_LanguageLiterature_assesment.objects.filter(Term4_assesment=True).values('Title').distinct()
	    	for assessment in unique_assessments:
		        # Retrieve the latest assessment object for each unique title and term
		        latest_assessment = Grade_9_models_LanguageLiterature_assesment.objects.filter(
		            Term4_assesment=True,
		            Title=assessment['Title']
		        ).order_by('-DatePosted').first()
		        assessments_list.append(latest_assessment)
    if Grade_9_Teacher_Class.objects.filter(id=request.user.id, Grade_9_PersDev_subj_teach=True):
	    if tm=="1":
	    	unique_assessments = Grade_9_models_LanguageLiterature_assesment.objects.filter(Term1_assesment=True).values('PersonalDev_Title').distinct()
	    	if Grade_9_models_LanguageLiterature_assesment.objects.filter(Term1_assesment=True).values('PersonalDev_Title').distinct().count()>=1:
			    for assessment in unique_assessments:
			        # Retrieve the latest assessment object for each unique title and term
			        latest_assessment = Grade_9_models_LanguageLiterature_assesment.objects.filter(
			            Term1_assesment=True,
			            PersonalDev_Title=assessment['PersonalDev_Title']
			        ).order_by('-Maths_DatePosted').first()
			        assessments_list.append(latest_assessment) 
	    if tm=="2":
	    	unique_assessments = Grade_9_models_LanguageLiterature_assesment.objects.filter(Term2_assesment=True).values('PersonalDev_Title').distinct()
	    	if Grade_9_models_LanguageLiterature_assesment.objects.filter(Term2_assesment=True).count()>=1:
			    for assessment in unique_assessments:
			        # Retrieve the latest assessment object for each unique title and term
			        latest_assessment = Grade_9_models_LanguageLiterature_assesment.objects.filter(
			            Term2_assesment=True,
			            PersonalDev_Title=assessment['PersonalDev_Title']
			        ).order_by('-Maths_DatePosted').first()
			        assessments_list.append(latest_assessment)
	    if tm=="3":
	    	unique_assessments = Grade_9_models_LanguageLiterature_assesment.objects.filter(Term3_assesment=True).values('PersonalDev_Title').distinct()
	    	for assessment in unique_assessments:
		        # Retrieve the latest assessment object for each unique title and term
		        latest_assessment = Grade_9_models_LanguageLiterature_assesment.objects.filter(
		            Term3_assesment=True,
		            PersonalDev_Title=assessment['PersonalDev_Title']
		        ).order_by('-Maths_DatePosted').first()
		        assessments_list.append(latest_assessment)
	    if tm=="4":
	    	unique_assessments = Grade_9_models_LanguageLiterature_assesment.objects.filter(Term4_assesment=True).values('PersonalDev_Title').distinct()
	    	for assessment in unique_assessments:
		        # Retrieve the latest assessment object for each unique title and term
		        latest_assessment = Grade_9_models_LanguageLiterature_assesment.objects.filter(
		            Term4_assesment=True,
		            PersonalDev_Title=assessment['PersonalDev_Title']
		        ).order_by('-Maths_DatePosted').first()
		        assessments_list.append(latest_assessment)

    context = {'subjects': assessments_list,'teachers':class_teacher}
   
    class_teacher_subj_checker(request,context)
    class_teacher_checker(request,context)
    return render(request, 'Grade9Teach/Grade9_Student_subj_templates/View_Uploaded_assesment_Term1.html', context)


def Grade_9_subj_view(request,pk,tm):
	class_teacher=Grade_9_Teacher_Class.objects.filter(id=request.user.id)

	context={'teachers':class_teacher}
	class_teacher_subj_checker(request,context)
	class_teacher_checker(request,context)
	return render(request,'Grade9Teach/Grade9_Student_subj_templates/Grade_9_all_subj_view.html',context)


def View_Uploaded_assesment_all_subj(request,snme):
	print(snme)
	class_teacher=Grade_9_Teacher_Class.objects.filter(id=request.user.id)
	
	context={'teachers':class_teacher}
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,Grade_9_Math_subj_teach=True):
		context['subjects '] = 'Math Teacher'
		context['Subj'] = 'Math'
		sbj=Grade_9_models_math_assesment.objects.filter(Title=snme)
		context['sbj']=sbj
	elif Grade_9_Teacher_Class.objects.filter(id=request.user.id,Grade_9_Engl_subj_teach=True):
		context['subjects '] = 'English Teacher'
		context['Subj'] = 'English'
		sbj=Grade_9_models_LanguageLiterature_assesment.objects.filter(Title=snme)
		context['sbj']=sbj
	elif Grade_9_Teacher_Class.objects.filter(id=request.user.id,Grade_9_Scn_subj_teach=True):
		context['subjects '] = 'Science Teacher'
		context['Subj'] = 'Science'
		sbj=Grade_9_models_Science_assesment.objects.filter(Title=snme)
		context['sbj']=sbj
	elif Grade_9_Teacher_Class.objects.filter(id=request.user.id,Grade_9_SocSnc_subj_teach=True):
		context['subjects '] = 'Social Science Teacher'
		context['Subj'] = 'Social Science'
		sbj=Grade_9_models_SocialScience_assesment.objects.filter(Title=snme)
		context['sbj']=sbj
	elif Grade_9_Teacher_Class.objects.filter(id=request.user.id,Grade_9_PersDev_subj_teach=True):
		context['subjects '] = 'Perosnal Development Teacher'
		context['Subj'] = 'Perosnal Development'
		sbj=Grade_9_models_PersonalDev_assesment.objects.filter(Title=snme)
		context['sbj']=sbj
	else:
		context['Subj'] = 'Not assisgned'
	class_teacher_checker(request,context)
	class_teacher_subj_checker(request,context)
	return render(request, 'Grade9Teach/Grade9_Student_subj_templates/View_Uploaded_assesment_all_subj.html',context)


def cord(std,all_students):
	for i in std:
			all_students.append(i)
#This codes filters out the teachers subject so it uploads its specific files subjects
def Grd9_ClsA_Subj_files_createview_all_std(request, Subj):
    print("---------------------")
    print("{}".format(Subj))
    print("---------------------")
    
    class_teacher = Grade_9_Teacher_Class.objects.filter(id=request.user.id)
    
    subject_forms = {
        'Math': Grade9mathFilesForm,
        'English': Grade9LanguageLiteratureFilesForm,
        'Science': Grade9ScienceFilesForm,
        'Social Science': Grade9SocialScienceFilesForm,
        'Personal Development': Grade9PersonalDevFilesForm,
    }
    
    if Subj in subject_forms:
        form_class = subject_forms[Subj]

        for i in class_teacher:
            print(i)
            if request.method == 'POST':
                form = form_class(request.POST, request.FILES)
                if form.is_valid():
                    print(request.POST.get('Term'))
                    instance = form.save(commit=False)
                    instance.Teacher_user_Name = i
                    if request.POST.get('assesment_type') == 'Assignment':
                        instance.Maths_is_Assignement = True
                    if request.POST.get('assesment_type') == 'Test':
                        instance.Maths_is_Test = True
                    term_field = request.POST.get('Term')
                    if term_field in ["Term1_assesment", "Term2_assesment", "Term3_assesment", "Term4_assesment"]:
                        setattr(instance, term_field, True)
                        instance.save()
                        tm = int(term_field[-1])
                    else:
                        print("failed")
                return redirect('Teacher:Grd9_ClsA_Subj_files_view_all_std', Subj=Subj)
            else:
                form = form_class()
    else:
        form = None

    context = {'form': form, 'teachers': class_teacher, 'Subj': Subj}
    class_teacher_subj_checker(request, context)
    class_teacher_checker(request, context)
    return render(request, 'Grade9Teach/Grade9_Student_subj_templates/Grade_9_Math_subj_view.html', context)

def Grd9_ClsA_math_assesment_createview_all_std(request,Subj):
	class_teacher=Grade_9_Teacher_Class.objects.filter(id=request.user.id)
	all_students = []
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classA_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classA=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classB_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classB=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classC_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classC=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classD_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classD=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classE_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classE=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classF_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classF=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classG_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classG=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classH_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classH=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classI_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classI=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classJ_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classJ=True)
		cord(std,all_students)

	if Subj=='Math':
		
		for i in all_students:
			print(i)
		if request.method=='POST':

			for i in all_students:
				form=Grade_9_models_math_assesment_Form(request.POST, request.FILES)
				if form.is_valid():
					print(request.POST.get('Term'))
					instance=form.save(commit=False)
					instance.user_Name=Grade_9_Student.objects.get(id=i.id)
					if request.POST.get('assesment_type')=='Assignment':
						instance.Maths_is_Assignement=True
					if request.POST.get('assesment_type')=='Test':
						instance.Maths_is_Test=True
					if request.POST.get('Term')=='Term1_assesment':
						instance.Term1_assesment=True
						instance.save()
						tm=1
					elif request.POST.get('Term')=='Term2_assesment':
						instance.Term2_assesment=True
						instance.save()
						tm=2
					elif request.POST.get('Term')=='Term3_assesment':
						instance.Term3_assesment=True
						instance.save()
						tm=3
					elif request.POST.get('Term')=='Term4_assesment':
						instance.Term4_assesment=True
						instance.save()
						tm=4
					else:
						print("failed")
			return redirect('Teacher:View_Uploaded_assesment_Term1',tm=tm)
			
		else:
			form=Grade_9_models_math_assesment_Form()
	if Subj=='English':
		
		for i in all_students:
			print(i)
		if request.method=='POST': 

			for i in all_students:
				form=Grade_9_models_LanguageLiterature_assesment_Form(request.POST, request.FILES)
				if form.is_valid():
					print(request.POST.get('Term'))
					instance=form.save(commit=False)
					instance.user_Name=Grade_9_Student.objects.get(id=i.id)
					if request.POST.get('assesment_type')=='Assignment':
						instance.Maths_is_Assignement=True
					if request.POST.get('assesment_type')=='Test':
						instance.Maths_is_Test=True
					if request.POST.get('Term')=='Term1_assesment':
						instance.Term1_assesment=True
						instance.save()
						tm=1
						return redirect('Teacher:View_Uploaded_assesment_Term1',tm=tm)
					elif request.POST.get('Term')=='Term2_assesment':
						instance.Term2_assesment=True
						instance.save()
						tm=2
						return redirect('Teacher:View_Uploaded_assesment_Term1',tm=tm)
					elif request.POST.get('Term')=='Term3_assesment':
						instance.Term3_assesment=True
						instance.save()
						tm=3
						return redirect('Teacher:View_Uploaded_assesment_Term1',tm=tm)
					elif request.POST.get('Term')=='Term4_assesment':
						instance.Term4_assesment=True
						instance.save()
						tm=4
						return redirect('Teacher:View_Uploaded_assesment_Term1',tm=tm)
					else:
						print("failed")
			
			
		else:
			form=Grade_9_models_LanguageLiterature_assesment_Form()
	if Subj=='Science':
		
		for i in std:
			print(i)
		if request.method=='POST':

			for i in std:
				form=Grade_9_models_Science_assesment_Form(request.POST, request.FILES)
				if form.is_valid():
					print(request.POST.get('Term'))
					instance=form.save(commit=False)
					instance.user_Name=Grade_9_Student.objects.get(id=i.id)
					if request.POST.get('assesment_type')=='Assignment':
						instance.Maths_is_Assignement=True
					if request.POST.get('assesment_type')=='Test':
						instance.Maths_is_Test=True
					if request.POST.get('Term')=='Term1_assesment':
						instance.Term1_assesment=True
						instance.save()
						tm=1
					elif request.POST.get('Term')=='Term2_assesment':
						instance.Term2_assesment=True
						instance.save()
						tm=2
					elif request.POST.get('Term')=='Term3_assesment':
						instance.Term3_assesment=True
						instance.save()
						tm=3
					elif request.POST.get('Term')=='Term4_assesment':
						instance.Term4_assesment=True
						instance.save()
						tm=4
					else:
						print("failed")
			return redirect('Teacher:View_Uploaded_assesment_Term1',tm=tm)
			
		else:
			form=Grade_9_models_Science_assesment_Form()
	if Subj=='Social Science':
		
		for i in std:
			print(i)
		if request.method=='POST':

			for i in std:
				form=Grade_9_models_SocialScience_assesment_Form(request.POST, request.FILES)
				if form.is_valid():
					print(request.POST.get('Term'))
					instance=form.save(commit=False)
					instance.user_Name=Grade_9_Student.objects.get(id=i.id)
					if request.POST.get('assesment_type')=='Assignment':
						instance.Maths_is_Assignement=True
					if request.POST.get('assesment_type')=='Test':
						instance.Maths_is_Test=True
					if request.POST.get('Term')=='Term1_assesment':
						instance.Term1_assesment=True
						instance.save()
						tm=1
					elif request.POST.get('Term')=='Term2_assesment':
						instance.Term2_assesment=True
						instance.save()
						tm=2
					elif request.POST.get('Term')=='Term3_assesment':
						instance.Term3_assesment=True
						instance.save()
						tm=3
					elif request.POST.get('Term')=='Term4_assesment':
						instance.Term4_assesment=True
						instance.save()
						tm=4
					else:
						print("failed")
			return redirect('Teacher:View_Uploaded_assesment_Term1',tm=tm)
			
		else:
			form=Grade_9_models_SocialScience_assesment_Form()
	if Subj=='Perosnal Development':
		
		for i in std:
			print(i)
		if request.method=='POST':

			for i in std:
				form=Grade_9_models_PersonalDev_assesment_Form(request.POST, request.FILES)
				if form.is_valid():
					print(request.POST.get('Term'))
					instance=form.save(commit=False)
					instance.user_Name=Grade_9_Student.objects.get(id=i.id)
					if request.POST.get('assesment_type')=='Assignment':
						instance.Maths_is_Assignement=True
					if request.POST.get('assesment_type')=='Test':
						instance.Maths_is_Test=True
					if request.POST.get('Term')=='Term1_assesment':
						instance.Term1_assesment=True
						instance.save()
						tm=1
					elif request.POST.get('Term')=='Term2_assesment':
						instance.Term2_assesment=True
						instance.save()
						tm=2
					elif request.POST.get('Term')=='Term3_assesment':
						instance.Term3_assesment=True
						instance.save()
						tm=3
					elif request.POST.get('Term')=='Term4_assesment':
						instance.Term4_assesment=True
						instance.save()
						tm=4
					else:
						print("failed")
			return redirect('Teacher:View_Uploaded_assesment_Term1',tm=tm)
			
		else:
			form=Grade_9_models_PersonalDev_assesment_Form()



	context={'form':form, 'teachers':class_teacher}
	class_teacher_subj_checker(request,context)

	return render(request, 'Grade9Teach/Grade9_Student_subj_templates/Grade_9_Math_subj_view.html', context)

def Grd9_ClsA_Subj_files_view_all_std(request,Subj):
	class_teacher=Grade_9_Teacher_Class.objects.filter(id=request.user.id)
	if Subj=='Math':
		suj=Grade_9_models_math_files.objects.all()
	context={'subjs':suj,'Subj':Subj}
	class_teacher_subj_checker(request,context)
	class_teacher_checker(request,context)
	return render(request, 'Grade9Teach/Grade9_Student_subj_templates/Grade_9_Math_subj_files_view.html',context)
def Grd9_Subj_files_view_all_std_delete(request,assessment_id,Subj):
    # assessment = get_object_or_404(Grade_9_models_math_assesment, Title=snme)
    assessments_list=Grade_9_models_math_files.objects.filter(id=assessment_id)
    if request.method == 'POST':
        # Delete the assessment
        assessments_list.delete()
        
        return redirect('Teacher:Grd9_ClsA_Subj_files_view_all_std', Subj=Subj) # Replace 'list_assessments_url' with the URL where you list assessments.
    context={'s_title':Subj}
    class_teacher_subj_checker(request,context)
    class_teacher_checker(request,context)
    return render(request, 'Grade9Teach/Grade9_Student_subj_templates/delete_assesment.html', context)

from django.shortcuts import render, redirect, get_object_or_404



def edit_assessment_one(request, assessment_id, snme):
    assessment = get_object_or_404(Grade_9_models_math_assesment, id=assessment_id)

    if request.method == 'POST':
        form = Grade9MathAssessment_Edit_Form(request.POST, instance=assessment)
        if form.is_valid():
            form.save()
            return redirect('Teacher:View_Uploaded_assesment_all_subj', snme=snme)  # Replace 'success_url' with the URL you want to redirect to after editing.

    else:
        form = Grade9MathAssessment_Edit_Form(instance=assessment)
    context={'form': form, 'assessment': assessment}
    class_teacher_subj_checker(request,context)
    class_teacher_checker(request,context)
    return render(request, 'Grade9Teach/Grade9_Student_subj_templates/Grade_9_Math_subj_view.html', context)


from django.shortcuts import render, redirect, get_object_or_404

# 'English'
# 'Science'
# 'Social Science'
# 'Perosnal Development'
def delete_math_assessment(request,snme):
    # assessment = get_object_or_404(Grade_9_models_math_assesment, Title=snme)
    assessments_list=Grade_9_models_math_assesment.objects.filter(Title=snme)
    if request.method == 'POST':
        # Delete the assessment
        for i in assessments_list:
        	i.delete()
        
        return redirect('Teacher:View_Uploaded_assesment_all_subj', snme=snme) # Replace 'list_assessments_url' with the URL where you list assessments.
    context={'s_title':snme}
    class_teacher_subj_checker(request,context)
    class_teacher_checker(request,context)
    return render(request, 'Grade9Teach/Grade9_Student_subj_templates/delete_assesment.html', context)
# ,Grade9mathFilesForm,Grade9ScienceFilesForm,
# Grade9SocialScienceFilesForm,
# Grade9LanguageLiteratureFilesForm,
# Grade9GeographyFilesForm,
# Grade9ChemistryFilesForm,
# Grade9PersonalDevFilesForm)

# userpost
# Admin_signal
# Teacher_signal
# Student
# title
# description
# posted_date
# student_boolean   
# is_Grade_9_teacher_classA
@login_required
# @Grd9_ClsA_required
def Grade9_classA_teacher(request):
	u_id=Account.objects.all()
	a_t=Grade_9_Teacher_Class.objects.all()
	Post_list=[]
	a_s=Grade_9_Student.objects.all()
	all_users=[]


	# Posts_TS=Post.objects.filter(userpost=i)
	all_teacher = []


	if Grade_9_Teacher_Class.objects.filter(id=request.user.id, is_Grade_9_teacher_classA=True):
		a_s=Grade_9_Student.objects.filter(is_Grade_9_student_classA=True)
		a_t=Grade_9_Teacher_Class.objects.filter(is_grd9_classA_teacher=True)
		print("A correct")
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id, is_Grade_9_teacher_classB=True):
		a_s=Grade_9_Student.objects.filter(is_Grade_9_student_classB=True)
		a_t=Grade_9_Teacher_Class.objects.filter(is_grd9_classB_teacher=True)
		print("B correct")

	if Grade_9_Teacher_Class.objects.filter(id=request.user.id, is_Grade_9_teacher_classC=True):
		a_s=Grade_9_Student.objects.filter(is_Grade_9_student_classC=True)
		a_t=Grade_9_Teacher_Class.objects.filter(is_grd9_classC_teacher=True)
		print("C correct")

	if Grade_9_Teacher_Class.objects.filter(id=request.user.id, is_Grade_9_teacher_classD=True):
		a_s=Grade_9_Student.objects.filter(is_Grade_9_student_classD=True)
		a_t=Grade_9_Teacher_Class.objects.filter(is_grd9_classD_teacher=True)


	for i in a_s:
		all_users.append(i)
	for i in a_t:
		all_users.append(i)
	# for i in all_users:
	# 	print(i.first_name)

	class_teacher=Grade_9_Teacher_Class.objects.filter(id=request.user.id)



	all_students = []
	post=Post.objects.all().order_by('-date')
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classA_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classA=True)
		for i in std:
			all_students.append(i)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classB_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classB=True)
		for i in std:
			all_students.append(i)
	print(all_students)
	# for i in all_students:
	# 	print(i.id)
	teacher_news=GrdClsA_news.objects.all()
	class_teacher=Grade_9_Teacher_Class.objects.filter(id=request.user.id)
	
	Headmin_news=Upcomeing_events.objects.all()
	context={'all_students':a_s,'teachers':class_teacher, 'Headmin_news':Headmin_news, 'teacher_news':teacher_news,'Posts':post,'all_users':all_users}
	class_teacher_checker(request,context)
	class_teacher_subj_checker(request,context)
	return render(request, 'Grade9Teach/Tgrd9A/TeacherGrade9_Profile.html', context) 

@login_required
# @Grd9_ClsA_required
def Grade_9_students_clsA_lists(request):
	# create_random_user()
	# if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_Grade_9_teacher_classA=True:)
	students_number=Grade_9_Student.objects.filter(is_Grade_9_student_classA=True).count() #specify the Boolean ID code and count it
	class_teacher=Grade_9_Teacher_Class.objects.filter(id=request.user.id)
	context={'teachers':class_teacher, 'students_number':students_number}
	class_teacher_checker(request,context)
	class_teacher_subj_checker(request,context)
	return render(request, 'Grade9Teach/Tgrd9A/students_list.html', context)
	# return render(request, 'Grade9Teach/Tgrd9A/some_list_2.html', context)

#Student details function
@login_required
# @Grd9_ClsA_required 
def student_details_Grd9_clsA(request, pk):
	id_students = Account.objects.filter(id=pk)
	#Math assesments


	all_students = Grade_9_Student.objects.filter(id=pk)
	for i in all_students:
		print(i.first_name)
	
	#marks2=marks_percentage/marks*100
	context={'studentss':all_students}
	class_teacher_checker(request,context)
	class_teacher_subj_checker(request,context)
	return render(request, 'Grade9Teach/Tgrd9A/students_details.html', context)

@method_decorator([login_required, Grd9_ClsA_required], name='dispatch')
class searchResult_view_grd9_A(ListView):
	template_name='Grade9Teach/Tgrd9A/search_results.html'
	context_object_name='students'
	model=Grade_9_Student
	def get_context_data(self, **kwargs):
		if Grade_9_Student.objects.filter(id=self.request.user.id,is_Grade_9_student_classA=True):
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_Grade_9_teacher_classA=True)
		kwargs['teachers']=class_teacher
		return super().get_context_data(**kwargs)

	def get_queryset(self):
		query=self.request.GET.get('q')
		return Grade_9_Student.objects.filter(Q(first_name__icontains=query)|Q(last_name__icontains=query)|Q(username__icontains=query), is_Grade_9_student_classA=True)
		#objects_list=Grade_9_Student.objects.annotate(search=SearchVector('first_name', 'last_name'),).filter(search=SearchQuery(query))
		#return objects_list
    #This codes handle the subject upload codes of teacher(REGULATORY SYSTEM)
 
"""
#testing
class Math_assesment_one(forms.ModelForm):
	class Meta:
		model=Term_11_math_assesment
		fields=
"""

#MATH 1
#Change_students_classes
#__OPEN__





#update students account

class Grade9StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Grade_9_Student
        fields = ['Grd9_ClsA_std_profile_picture', 'first_name', 'last_name', 'phone_no', 'date_of_birth', 'full_name', 'Resident']


class Grade9StudentUpdateView(UpdateView):
    model = Grade_9_Student
    form_class = Grade9StudentUpdateForm
    template_name = 'G9ClsAStdSignUp.html'  # Replace with the actual template name

    # Optionally, you can override the get_object method to customize the queryset
    def get_context_data(self, **kwargs):
        if Grade_9_Teacher_Class.objects.filter(id=self.request.user.id, is_Grade_9_teacher_classA=True):
            st = 'Grade 9 class A students registration form'

        if Grade_9_Teacher_Class.objects.filter(id=self.request.user.id, is_Grade_9_teacher_classB=True):
            st = 'Grade 9 class B students registration form'

        if Grade_9_Teacher_Class.objects.filter(id=self.request.user.id, Grade_9_Math_subj_teach=True):
            kwargs['Subject'] = 'Math Teacher'
            kwargs['Subj'] = 'Math'

        elif Grade_9_Teacher_Class.objects.filter(id=self.request.user.id, Grade_9_Engl_subj_teach=True):
            kwargs['Subject'] = 'English Teacher'
            kwargs['Subj'] = 'English'

        elif Grade_9_Teacher_Class.objects.filter(id=self.request.user.id, Grade_9_Scn_subj_teach=True):
            kwargs['Subject'] = 'Science Teacher'
            kwargs['Subj'] = 'Science'

        elif Grade_9_Teacher_Class.objects.filter(id=self.request.user.id, Grade_9_SocSnc_subj_teach=True):
            kwargs['Subject'] = 'Social Science Teacher'
            kwargs['Subj'] = 'Social Science'

        elif Grade_9_Teacher_Class.objects.filter(id=self.request.user.id, Grade_9_PersDev_subj_teach=True):
            kwargs['Subject'] = 'Personal Development Teacher'
            kwargs['Subj'] = 'Personal Development'

        else:
            print("nope")

        class_teacher = Grade_9_Teacher_Class.objects.filter(id=self.request.user.id, is_Grade_9_teacher_classA=True)
        kwargs['teachers'] = class_teacher
        kwargs['user_type'] = st
        return super().get_context_data(**kwargs)

    def get_object(self, queryset=None):
        return Grade_9_Student.objects.get(pk=self.kwargs['pk'])

    def get_success_url(self):
        student_id = self.kwargs['pk']
        return reverse_lazy('Teacher:student_details_Grd9_clsA', kwargs={'pk': student_id})


#These codes handles the grade 9 student sign up forms

class Grade_9_teacher_classA_Student_SignUpform(UserCreationForm):
	email=forms.EmailField(required=True)
	#Grd9_ClsA_std_profile_picture=forms.CharField(label='Grd9_ClsA_std_profile_picture', widget=forms.FileInput)
	password1=forms.CharField(label='Password', widget=forms.PasswordInput)
	password2=forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
	class Meta(UserCreationForm.Meta):
		model=Grade_9_Student
		fields=('first_name', 'last_name', 'username','Grd9_ClsA_std_profile_picture',  'email','phone_no', 'date_of_birth', 'Resident', 'password1', 'password2')
	def save(self, commit=True):
		user=super().save(commit=False)
		user.email=self.cleaned_data['email']
		user.is_student=True
		user.is_Grade_9_student=True
		if commit:
			user.save()
		return user



# @method_decorator([login_required, Grd9_ClsA_required], name='dispatch')
class Grade_9_teacher_classA_Student_SignUpView(CreateView):
	model=Grade_9_Student
	form_class=Grade_9_teacher_classA_Student_SignUpform
	template_name='Grade9Teach/Tgrd9A/G9ClsAStdSignUp.html'
	def get_context_data(self, **kwargs):
		if Grade_9_Teacher_Class.objects.filter(id=self.request.user.id,is_Grade_9_teacher_classA=True):
			st='Grade 9 class A students registration form'

		if Grade_9_Teacher_Class.objects.filter(id=self.request.user.id,is_Grade_9_teacher_classB=True):
			st='Grade 9 class B students registration form'
	
		if Grade_9_Teacher_Class.objects.filter(id=self.request.user.id,Grade_9_Math_subj_teach=True):
			kwargs['Subject'] = 'Math Teacher'
			kwargs['Subj'] = 'Math'
			
		elif Grade_9_Teacher_Class.objects.filter(id=self.request.user.id,Grade_9_Engl_subj_teach=True):
			kwargs['Subject'] = 'English Teacher'
			kwargs['Subj'] = 'English'

		elif Grade_9_Teacher_Class.objects.filter(id=self.request.user.id,Grade_9_Scn_subj_teach=True):
			kwargs['Subject'] = 'Science Teacher'
			kwargs['Subj'] = 'Science'
		
		elif Grade_9_Teacher_Class.objects.filter(id=self.request.user.id,Grade_9_SocSnc_subj_teach=True):
			kwargs['Subject'] = 'Social Science Teacher'
			kwargs['Subj'] = 'Social Science'
			
		elif Grade_9_Teacher_Class.objects.filter(id=self.request.user.id,Grade_9_PersDev_subj_teach=True):
			kwargs['Subject'] = 'Perosnal Development Teacher'
			kwargs['Subj'] = 'Perosnal Development'
			
		else:
			print("nope")
		class_teacher=Grade_9_Teacher_Class.objects.filter(id=self.request.user.id,is_Grade_9_teacher_classA=True)
		kwargs['teachers']=class_teacher
		kwargs['user_type']=st
		return super().get_context_data(**kwargs)
	def form_valid(self, form):
		user=form.save(commit=False)
		if Grade_9_Teacher_Class.objects.filter(id=self.request.user.id,is_Grade_9_teacher_classA=True):
			user.is_Grade_9_student_classA=True
			user.save()
		elif Grade_9_Teacher_Class.objects.filter(id=self.request.user.id,is_Grade_9_teacher_classB=True):
			user.is_Grade_9_student_classB=True
			user.save()
		
		return redirect('Teacher:Grade_9_students_clsA_lists')





class Change_students_class_gr9A_form(ModelForm):

	class Meta:
		model=Grade_9_Student
		fields=['is_Grade_9_student_classA', 'is_Grade_9_student_classB','is_Grade_9_student_classC','is_Grade_9_student_classD','is_Grade_9_student_classE','is_Grade_9_student_classF','is_Grade_9_student_classG','is_Grade_9_student_classH','is_Grade_9_student_classI','is_Grade_9_student_classJ']

# @method_decorator([login_required, Grd9_ClsA_required], name='dispatch')
class Change_students_class_gr9A(UpdateView):
	template_name='Grade9Teach/Tgrd9A/change_students_class.html'
	form_class=Change_students_class_gr9A_form
	model=Grade_9_Student

	def get_context_data(self, **kwargs):
		class_teacher=Grade_9_teacher_classA.objects.all()
		kwargs['teachers']=class_teacher
		kwargs['user_type']='Change Grade 9 students class'
		return super().get_context_data(**kwargs)
	def get_success_url(self):
		Grade9studentclassA_id = self.kwargs['pk']
		return reverse_lazy('Teacher:Grade_9_students_clsA_lists')
#__CLOSE__

@login_required
# @Grd9_ClsA_required
def Grd9_teach_edit_uploaded_files(request):
	class_teacher=Grade_9_teacher_classA.objects.all()
	Grd_9_MsT1=Grade_9_math_subject_type1.objects.all()
	Grd_9_MsT2=Grade_9_math_subject_type2.objects.all()
	Grd_9_EsT1=Grade_9_english_subject_type1.objects.all()
	Grd_9_EsT2=Grade_9_english_subject_type2.objects.all()
	Grd_9_SsT1=Grade_9_science_subject_type1.objects.all()
	Grd_9_SsT2=Grade_9_science_subject_type2.objects.all()
	Grd_9_SocSsT1=Grade_9_socialscience_subject_type1.objects.all()
	Grd_9_SocSsT2=Grade_9_socialscience_subject_type2.objects.all()
	Grd_9_PDT1=Grade_9_personaldevelopement_subject_type1.objects.all()
	Grd_9_PDT2=Grade_9_personaldevelopement_subject_type2.objects.all()
	context={'Grd_9_MsT1':Grd_9_MsT1, 'Grd_9_MsT2':Grd_9_MsT2,'Grd_9_EsT1':Grd_9_EsT1,'Grd_9_EsT2':Grd_9_EsT2,'Grd_9_SsT1':Grd_9_SsT1,'Grd_9_SsT2':Grd_9_SsT2,'Grd_9_SocSsT1':Grd_9_SocSsT1,'Grd_9_SocSsT2':Grd_9_SocSsT2,'Grd_9_PDT1':Grd_9_PDT1,'Grd_9_PDT2':Grd_9_PDT2, 'teachers':class_teacher}
	return render(request, 'Grade9Teach/Tgrd9A/Subjects_upload_template/view_uploaded_subjects.html', context)

# # @method_decorator([login_required, Grd9_ClsA_required], name='dispatch')
# class Grade_9_students_view_enter_marks_english(UpdateView):
# 	model = Grade_9_math_subject_type1
# 	form_class=Grd9_class_Math_upload_form_1
# 	template_name = 'Grade9Teach/Tgrd9A/Subjects_upload_template/edit_uploaded_subjects.html'
# 	#std=Grade6studentclassB.objects.all()
# 	#context={'students':std}
# 	def get_context_data(self,**kwargs):
# 		#all_students = Grade_9_student_classA.objects.filter(id=pk)
# 		class_teacher=Grade_9_teacher_classA.objects.all()
# 		#kwargs['students']=all_students
# 		kwargs['teachers']=class_teacher
# 		return super().get_context_data(**kwargs)
#OPENING DELETE CODES
#Term 1 delete codes





#TEACHER NEWSBOARD POST

class Teacher_grd9ClsA_NewsPost_model(models.Model):
	Title=models.CharField(max_length=200)
	Desc=models.TextField(max_length=500)
	Due_Date=models.DateTimeField()
	posted_date=models.DateTimeField(verbose_name='posted_date', auto_now_add=True)
	def __str__(self):
		return "{}-{}".format(self.Title, self.posted_date)

class Teacher_grd9ClsA_NewsPost_form(ModelForm):
	class Meta:
		model=Teacher_grd9ClsA_NewsPost_model
		fields=('__all__')


def Teacher_post_detail(request,slug):
	a_t=[]
	a_s=Grade_9_Student.objects.all()
	Post_list=[]
	students = Grade_9_Student.objects.filter(id=request.user.id)
	all_users=[]

	if Grade_9_Teacher_Class.objects.filter(id=request.user.id, is_grd9_classA_teacher=True):
		a_s=Grade_9_Student.objects.filter(is_Grade_9_student_classA=True)
		a_t=Grade_9_Teacher_Class.objects.filter(is_grd9_classA_teacher=True)
		print("A correct")
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id, is_grd9_classB_teacher=True):
		a_s=Grade_9_Student.objects.filter(is_Grade_9_student_classB=True)
		a_t=Grade_9_Teacher_Class.objects.filter(is_grd9_classB_teacher=True)

	if Grade_9_Teacher_Class.objects.filter(id=request.user.id, is_grd9_classC_teacher=True):
		a_s=Grade_9_Student.objects.filter(is_Grade_9_student_classC=True)
		a_t=Grade_9_Teacher_Class.objects.filter(is_grd9_classC_teacher=True)

	if Grade_9_Teacher_Class.objects.filter(id=request.user.id, is_grd9_classD_teacher=True):
		a_s=Grade_9_Student.objects.filter(is_Grade_9_student_classD=True)
		a_t=Grade_9_Teacher_Class.objects.filter(is_grd9_classD_teacher=True)

	for i in a_s:
		all_users.append(i)
	for i in a_t:
		all_users.append(i)
	for i in all_users:
		print(i.first_name)
	class_teacher=Grade_9_Teacher_Class.objects.filter(id=request.user.id)

	


	
	# for i in u_id:
	post=Post.objects.filter(slug=slug)
	print("-------------------------------")
	print(post)
	print("-------------------------------")
	
	



	
	if request.method == 'POST':
		form = CommentCreationForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.author = request.user
			comment.post=get_object_or_404(Post, slug = slug)
			

			comment.save()
            # Redirect to the comment detail page or any other page as needed
	else:
		print("Comment creation failed")
		form = CommentCreationForm()
	
	context={'teachers':class_teacher,'Post':post,'Posts':post,'all_teacher':a_t,"all_students":a_s,'students':students,'all_users':all_users,'form':form}
	class_teacher_subj_checker(request,context)
	class_teacher_checker(request,context)

	
	return render(request, 'Grade9Teach/Tgrd9A/post_details.html', context)