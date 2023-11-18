from django.shortcuts import render, redirect
from django.contrib import messages
from .Grade9_models import Grade_9_Student
from Teacher.Teacher_views.Grade9_views.Grd9_assesment_models import (Grade_9_models_math_assesment,Grade_9_models_LanguageLiterature_assesment,
Grade_9_models_Science_assesment,
Grade_9_models_SocialScience_assesment,
Grade_9_models_Geography_assesment,
Grade_9_models_Chemistry_assesment,
Grade_9_models_PersonalDev_assesment,
Grade_9_models_math_files)
from Teacher.Teacher_views.Grade9_views.Grd9_teacher_models import Grade_9_Teacher_Class
from Headmin.models import Account,Upcomeing_events, PostForm
from django.views.generic import ListView
from django.utils import timezone
from datetime import timedelta
from django.views.generic import CreateView, UpdateView, DeleteView
from post.models import Post,Comment,CommentCreationForm
from django.views.generic import UpdateView, DetailView
from django.views import generic

def create_comment(request):
    if request.method == 'POST':
        form = CommentCreationForm(request.POST)
        if form.is_valid():
            comment = form.save()
            # Redirect to the comment detail page or any other page as needed
    else:
        form = CommentCreationForm()

    return render(request, 'create_comment.html', {'form': form})

class CommentCreate(CreateView):
    """
    Form for adding a blog comment. Requires login. 
    """
    model = Comment
    fields = ['description',]
    template_name='Grade9/Grd9ClsA/post_details.html'


    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(CommentCreate, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['post'] = get_object_or_404(Post, slug = self.kwargs['slug'])
        return context
        
    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.author = self.request.user
        #Associate comment with blog based on passed id
        form.instance.post=get_object_or_404(Post, slug = self.kwargs['slug'])
        # Call super-class form validation behaviour
        return super(CommentCreate, self).form_valid(form)

    def get_success_url(self): 
        """
        After posting comment return to associated blog.
        """
        return reverse('Student:Student:post_detail', kwargs={'slug': self.kwargs['slug'],})



class PostUpdate(generic.DetailView):
    model = Post
    fields = ['title', 'body',]

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'G9ClsAStdSignUp.html'  # Replace with the actual template name

def student_checker(request, context):
	if Grade_9_Student.objects.filter(id=request.user.id,is_Grade_9_student_classA=True):
		context['students_type']='Class A'
		print("correct")
	elif Grade_9_Student.objects.filter(id=request.user.id,is_Grade_9_student_classB=True):
		context['students_type']='Class B'
	elif Grade_9_Student.objects.filter(id=request.user.id,is_Grade_9_student_classC=True):
		context['students_type']='Class C'
	elif Grade_9_Student.objects.filter(id=request.user.id,is_Grade_9_student_classD=True):
		context['students_type']='Class D'
	elif Grade_9_Student.objects.filter(id=request.user.id,is_Grade_9_student_classE=True):
		context['students_type']='Class E'
	elif Grade_9_Student.objects.filter(id=request.user.id,is_Grade_9_student_classF=True):
		context['students_type']='Class F'
	elif Grade_9_Student.objects.filter(id=request.user.id,is_Grade_9_student_classG=True):
		context['students_type']='Class G'
	elif Grade_9_Student.objects.filter(id=request.user.id,is_Grade_9_student_classH=True):
		context['students_type']='Class H'
	elif Grade_9_Student.objects.filter(id=request.user.id,is_Grade_9_student_classI=True):
		context['students_type']='Class I'
	elif Grade_9_Student.objects.filter(id=request.user.id,is_Grade_9_student_classJ=True):
		context['students_type']='Class J'
	else:
		return print("nope")

def post_detail(request,slug):
	students = Grade_9_Student.objects.filter(id=request.user.id)
	
	a_t=[]
	a_s=Grade_9_Student.objects.all()
	Post_list=[]
	students = Grade_9_Student.objects.filter(id=request.user.id)
	all_users=[]

	if Grade_9_Student.objects.filter(id=request.user.id, is_Grade_9_student_classA=True):
		a_s=Grade_9_Student.objects.filter(is_Grade_9_student_classA=True)
		a_t=Grade_9_Teacher_Class.objects.filter(is_grd9_classA_teacher=True)
		print("A correct")
	if Grade_9_Student.objects.filter(id=request.user.id, is_Grade_9_student_classB=True):
		a_s=Grade_9_Student.objects.filter(is_Grade_9_student_classB=True)
		a_t=Grade_9_Teacher_Class.objects.filter(is_grd9_classB_teacher=True)

	if Grade_9_Student.objects.filter(id=request.user.id, is_Grade_9_student_classC=True):
		a_s=Grade_9_Student.objects.filter(is_Grade_9_student_classC=True)
		a_t=Grade_9_Teacher_Class.objects.filter(is_grd9_classC_teacher=True)

	if Grade_9_Student.objects.filter(id=request.user.id, is_Grade_9_student_classD=True):
		a_s=Grade_9_Student.objects.filter(is_Grade_9_student_classD=True)
		a_t=Grade_9_Teacher_Class.objects.filter(is_grd9_classD_teacher=True)

	for i in a_s:
		all_users.append(i)
	for i in a_t:
		all_users.append(i)
	for i in all_users:
		print(i.first_name)


	
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
	context={'Posts':post,'all_teacher':a_t,"all_students":a_s,'students':students,'all_users':all_users,'form':form}
	student_checker(request, context)
	return render(request, 'Grade9/Grd9ClsA/post_details.html', context)
def View_assesment_by_term(request):
	students=Grade_9_Student.objects.filter(id=request.user.id)
	context={'students':students}
	student_checker(request, context)
	return render(request, 'Grade9/Grd9ClsA/term_assesment.html', context)





def View_Student_user_all_assesment(request, tm):
	students=Grade_9_Student.objects.filter(id=request.user.id)
	term=tm
	context={'students':students,'term':term}
	student_checker(request, context)
	return render(request, 'Grade9/Grd9ClsA/all_subj_assesment.html', context)

def View_Uploaded_assesment_files(request):
	students=Grade_9_Student.objects.filter(id=request.user.id)
	context={'students':students}
	student_checker(request, context)
	return render(request, 'Grade9/Grd9ClsA/View_Uploaded_assesment_files.html', context)

 
# Math
# English
# Science
# Social Science
# Personal Development

# Grade_9_models_math_assesment
# Grade_9_models_LanguageLiterature_assesment
# Grade_9_models_Science_assesment
# Grade_9_models_SocialScience_assesment
# Grade_9_models_PersonalDev_assesment
# is_grd9_classA_teacher
# is_grd9_classB_teacher
# is_grd9_classC_teacher
# is_grd9_classD_teacher
# is_grd9_classE_teacher
# is_grd9_classF_teacher
# is_grd9_classG_teacher
# is_grd9_classH_teacher
# is_grd9_classI_teacher
# is_grd9_classJ_teacher

# is_Grade_9_student_classA
# is_Grade_9_student_classB
# is_Grade_9_student_classC
# is_Grade_9_student_classD
# is_Grade_9_student_classE
# is_Grade_9_student_classF
# is_Grade_9_student_classG
# is_Grade_9_student_classH
# is_Grade_9_student_classI
# is_Grade_9_student_classJ

# Grade_9_models_math_files
# Teacher_user_Name
# Grade_9_Math_subj_teach
# Grade_9_Engl_subj_teach
# Grade_9_Scn_subj_teach
# Grade_9_SocSnc_subj_teach
# Grade_9_PersDev_subj_teach

from collections import defaultdict
from django.core.exceptions import FieldError
def View_Uploaded_assesment_single_file(request, sbj):
    try:
        students = Grade_9_Student.objects.filter(id=request.user.id)

        class_subjects_mapping = {
            '1': 'Math',
            '2': 'LanguageLiterature',
            '3': 'Science',
            '4': 'SocialScience',
            '5': 'PersonalDev',
        }

        class_letters = 'ABCDEFGHIJ'

        subject = class_subjects_mapping.get(sbj)

        class_teacher_dict = defaultdict(list)

        for letter in class_letters:
            is_student_class = getattr(request.user, f'is_Grade_9_student_class{letter}', False)
            
            if is_student_class:
                class_teacher = Grade_9_Teacher_Class.objects.filter(
                    **{f'is_grd9_class{letter}_teacher': True, f'Grade_9_{subject}_subj_teach': True}
                ).first()
                
                if class_teacher:
                    class_teacher_dict[letter].append(class_teacher)

        subjects = []

        for teacher_list in class_teacher_dict.values():
            for teacher in teacher_list:
                if subject == 'Math':
                    subjects.extend(Grade_9_models_math_files.objects.filter(Teacher_user_Name=teacher))
                elif subject == 'LanguageLiterature':
                    subjects.extend(Grade_9_models_LanguageLiterature_assesment.objects.filter(Teacher_user_Name=teacher))
                elif subject == 'Science':
                    subjects.extend(Grade_9_models_Science_assesment.objects.filter(Teacher_user_Name=teacher))
                elif subject == 'SocialScience':
                    subjects.extend(Grade_9_models_SocialScience_assesment.objects.filter(Teacher_user_Name=teacher))
                elif subject == 'PersonalDev':
                    subjects.extend(Grade_9_models_PersonalDev_assesment.objects.filter(Teacher_user_Name=teacher))

        SSJ = class_subjects_mapping.get(sbj)
        print(SSJ)
        context = {'students': students, 'subjects': subjects, 'SSJ': SSJ}
        student_checker(request, context)
        return render(request, 'Grade9/Grd9ClsA/View_Uploaded_assesment_single_files.html', context)
    except FieldError as e:
        SSJ = class_subjects_mapping.get(sbj)
        context = {'students': students, 'SSJ': SSJ}
        context['error'] = f'No {SSJ} uploaded'
        student_checker(request, context)
        return render(request, 'Grade9/Grd9ClsA/View_Uploaded_assesment_single_files.html', context)


def View_Student_user_single_assesment(request, sbj, tm):
    students = Grade_9_Student.objects.filter(id=request.user.id)
    context = {'students': students}

    term_mapping = {
        '1': 'Term1_assesment',
        '2': 'Term2_assesment',
        '3': 'Term3_assesment',
        '4': 'Term4_assesment',
    }

    subject_mapping = {
        '1': ('Math', Grade_9_models_math_assesment),
        '2': ('Language', Grade_9_models_LanguageLiterature_assesment),
        '3': ('Science', Grade_9_models_Science_assesment),
        '4': ('Social Science', Grade_9_models_SocialScience_assesment),
        '5': ('Personal Development', Grade_9_models_PersonalDev_assesment),
    }

    subject_number = sbj
    term_field = term_mapping.get(tm, '')

    if subject_number in subject_mapping and term_field:
        subject_name, subject_model = subject_mapping[subject_number]
        subjects = subject_model.objects.filter(
            **{term_field: True, 'user_Name__in': students.values_list('id', flat=True)}
        )
        context.update({'subjects': subjects, 'sbj': subject_name, 'term': sbj})
        print("green")

    student_checker(request, context)

    return render(request, 'Grade9/Grd9ClsA/subj_assesment.html', context)

def View_Student_user_single_assesment1(request, sbj, tm):
    students = Grade_9_Student.objects.filter(id=request.user.id)
    context = {'students': students}

    subject_models = {
        '1': Grade_9_models_math_assesment,
        '2': Grade_9_models_LanguageLiterature_assesment,
        '3': Grade_9_models_Science_assesment,
        '4': Grade_9_models_SocialScience_assesment,
        '5': Grade_9_models_PersonalDev_assesment,
    }

    if tm in subject_models:
        subject_model = subject_models[tm]
        subjects = subject_model.objects.filter(**{f'Term{tm}_assesment': True, 'user_Name': request.user.id})
        context['subjects'] = subjects
        subject_names = {
            '1': 'Math',
            '2': 'Language',
            '3': 'Science',
            '4': 'Social Science',
            '5': 'Personal Development',
        }
        context['sbj'] = subject_names.get(sbj, '')
        context['term'] = sbj
        print("green")

    student_checker(request, context)

    return render(request, 'Grade9/Grd9ClsA/subj_assesment.html', context)

def View_Student_user_single_assesment2(request, sbj,tm):
	students=Grade_9_Student.objects.filter(id=request.user.id)
	context={'students':students}
	if tm=="1":
		if sbj=='1':
			for i in students:
				subjects=Grade_9_models_math_assesment.objects.filter(Term1_assesment=True,user_Name=i.id)
				print(subjects)
				context['subjects']=subjects
				context['sbj']='Math'
				context['term']=sbj
				print("green")
		if sbj=='2':
			for i in students:
				subjects=Grade_9_models_LanguageLiterature_assesment.objects.filter(Term1_assesment=True,user_Name=i.id)
				print(subjects)
				context['subjects']=subjects
				context['sbj']='Language'
				context['term']=sbj
				print("green")
		if sbj=='3':
			for i in students:
				subjects=Grade_9_models_Science_assesment.objects.filter(Term1_assesment=True,user_Name=i.id)
				print(subjects)
				context['subjects']=subjects
				context['sbj']='Science'
				context['term']=sbj
				print("green")
		if sbj=='4':
			for i in students:
				subjects=Grade_9_models_SocialScience_assesment.objects.filter(Term1_assesment=True,user_Name=i.id)
				print(subjects)
				context['subjects']=subjects
				context['sbj']='Social Science'
				context['term']=sbj
				print("green")
		if sbj=='5':
			for i in students:
				subjects=Grade_9_models_PersonalDev_assesment.objects.filter(Term1_assesment=True,user_Name=i.id)
				print(subjects)
				context['subjects']=subjects
				context['sbj']='Personal Development'
				context['term']=sbj
				print("green")
	if tm=="2":
		if sbj=='1':
			for i in students:
				subjects=Grade_9_models_math_assesment.objects.filter(Term2_assesment=True,user_Name=i.id)
				print(subjects)
				context['subjects']=subjects
				context['sbj']='Math'
				context['term']=sbj
				print("green")
		if sbj=='2':
			for i in students:
				subjects=Grade_9_models_LanguageLiterature_assesment.objects.filter(Term2_assesment=True,user_Name=i.id)
				print(subjects)
				context['subjects']=subjects
				context['sbj']='Language'
				context['term']=sbj
				print("green")
		if sbj=='3':
			for i in students:
				subjects=Grade_9_models_Science_assesment.objects.filter(Term2_assesment=True,user_Name=i.id)
				print(subjects)
				context['subjects']=subjects
				context['sbj']='Science'
				context['term']=sbj
				print("green")
		if sbj=='4':
			for i in students:
				subjects=Grade_9_models_SocialScience_assesment.objects.filter(Term2_assesment=True,user_Name=i.id)
				print(subjects)
				context['subjects']=subjects
				context['sbj']='Social Science'
				context['term']=sbj
				print("green")
		if sbj=='5':
			for i in students:
				subjects=Grade_9_models_PersonalDev_assesment.objects.filter(Term2_assesment=True,user_Name=i.id)
				print(subjects)
				context['subjects']=subjects
				context['sbj']='Personal Development'
				context['term']=sbj
				print("green")
	if tm=="3":
		if sbj=='1':
			for i in students:
				subjects=Grade_9_models_math_assesment.objects.filter(Term3_assesment=True,user_Name=i.id)
				print(subjects)
				context['subjects']=subjects
				context['sbj']='Math'
				context['term']=sbj
				print("green")
		if sbj=='2':
			for i in students:
				subjects=Grade_9_models_LanguageLiterature_assesment.objects.filter(Term3_assesment=True,user_Name=i.id)
				print(subjects)
				context['subjects']=subjects
				context['sbj']='Language'
				context['term']=sbj
				print("green")
		if sbj=='3':
			for i in students:
				subjects=Grade_9_models_Science_assesment.objects.filter(Term3_assesment=True,user_Name=i.id)
				print(subjects)
				context['subjects']=subjects
				context['sbj']='Science'
				context['term']=sbj
				print("green")
		if sbj=='4':
			for i in students:
				subjects=Grade_9_models_SocialScience_assesment.objects.filter(Term3_assesment=True,user_Name=i.id)
				print(subjects)
				context['subjects']=subjects
				context['sbj']='Social Science'
				context['term']=sbj
				print("green")
		if sbj=='5':
			for i in students:
				subjects=Grade_9_models_PersonalDev_assesment.objects.filter(Term3_assesment=True,user_Name=i.id)
				print(subjects)
				context['subjects']=subjects
				context['sbj']='Personal Development'
				context['term']=sbj
				print("green")
	if tm=="4":
		if sbj=='1':
			for i in students:
				subjects=Grade_9_models_math_assesment.objects.filter(Term4_assesment=True,user_Name=i.id)
				print(subjects)
				context['subjects']=subjects
				context['sbj']='Math'
				context['term']=sbj
				print("green")
		if sbj=='2':
			for i in students:
				subjects=Grade_9_models_LanguageLiterature_assesment.objects.filter(Term4_assesment=True,user_Name=i.id)
				print(subjects)
				context['subjects']=subjects
				context['sbj']='Language'
				context['term']=sbj
				print("green")
		if sbj=='3':
			for i in students:
				subjects=Grade_9_models_Science_assesment.objects.filter(Term4_assesment=True,user_Name=i.id)
				print(subjects)
				context['subjects']=subjects
				context['sbj']='Science'
				context['term']=sbj
				print("green")
		if sbj=='4':
			for i in students:
				subjects=Grade_9_models_SocialScience_assesment.objects.filter(Term4_assesment=True,user_Name=i.id)
				print(subjects)
				context['subjects']=subjects
				context['sbj']='Social Science'
				context['term']=sbj
				print("green")
		if sbj=='5':
			for i in students:
				subjects=Grade_9_models_PersonalDev_assesment.objects.filter(Term2_assesment=True,user_Name=i.id)
				print(subjects)
				context['subjects']=subjects
				context['sbj']='Personal Development'
				context['term']=sbj
				print("green")

	
	student_checker(request, context)

	return render(request, 'Grade9/Grd9ClsA/subj_assesment.html', context)

# class Upcomeing_events(models.Model):
	
# 	Title=models.CharField(max_length=200)
# 	Subtitle=models.CharField(max_length=50)
# 	Desc=models.TextField(max_length=500)
# 	Due_Date=models.DateTimeField()
# 	posted_date=models.DateTimeField(verbose_name='posted_date', auto_now_add=True)
# 	def __str__(self):
# 		return "{}-{}".format(self.Title, self.posted_date)

# 	def snippet(self):
# 		return self.Desc[:40]+"..."

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def posts_view(request):
    # Query all posts from the database, ordered by title
    posts = Post.objects.all().order_by('title')

    # Number of posts to display per page
    posts_per_page = 5

    # Create a Paginator object
    paginator = Paginator(posts, posts_per_page)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Get the Page object for the requested page
    page = paginator.get_page(page_number)

    context = {
        
    }

    return render(request, 'posts.html', context)
'''
You think God is up there and be like, "hmmm i dont care if 746 plus and more children in the future is killed, i want Hamas to surrender". Cain killed Able to hurt God, because God rejected his offering and then God told Cain, "Sin is at your Door, and you've invited it in, so look to yourself", that made Cain angry with God, now Cain cannot hurt God directly, but Cain knew what God loves, and it was Able, and Able was without Sin and innocent , that was the only way to hurt God, to kill the innocent.  You think God is up there cheering every time a building goes down? oh wow. Yes Hamas is Evil, but the Israel military is not innocent either. When diplomacy is out the window, innocent will always be causalities. God is not winning this one, because it involves dead children, the only person celebrating would be Satan. Until they find a precise and surgical way to remove Hamas physically or in a diplomatically peaceful way, what they doing in Gaza is evil.  
'''

# is_Grade_9_teacher_classA
# class Grade9_class_student(ListView):
#     model = Post
#     context_object_name = 'posts'
#     paginate_by = 5
#     template_name = 'Grade9/Grd9ClsA/Grade9_Profile.html'

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'Grade 9 Teacher: Class A'
#         kwargs['students'] = Grade_9_Student.objects.filter(id=self.request.user.id)
#         return super().get_context_data(**kwargs)


# is_grd9_classA_teacher
# is_grd9_classB_teacher
# is_grd9_classC_teacher
# is_grd9_classD_teacher
# is_grd9_classE_teacher
from django import forms
from django.db.models import Q
from django.shortcuts import get_object_or_404
class DeletePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = []
def delete_post(request, pk):
    post = get_object_or_404(Post, id=pk)

    if request.method == 'POST':
        form = DeletePostForm(request.POST, instance=post)
        if form.is_valid():
            post.delete()
            return redirect("Student:Student:Grade9_class_student")
    else:
        form = DeletePostForm(instance=post)

    return render(request, 'Grade9/Grd9ClsA/G9S_Delete_news.html', {'form': form, 'post': post})

def Grade9_class_student(request):
	a_t=[]
	a_s=Grade_9_Student.objects.all()
	Post_list=[]
	students = Grade_9_Student.objects.filter(id=request.user.id)
	all_users=[]

	if Grade_9_Student.objects.filter(id=request.user.id, is_Grade_9_student_classA=True):
		a_s=Grade_9_Student.objects.filter(is_Grade_9_student_classA=True)
		a_t=Grade_9_Teacher_Class.objects.filter(is_grd9_classA_teacher=True)
		print("A correct")
	if Grade_9_Student.objects.filter(id=request.user.id, is_Grade_9_student_classB=True):
		a_s=Grade_9_Student.objects.filter(is_Grade_9_student_classB=True)
		a_t=Grade_9_Teacher_Class.objects.filter(is_grd9_classB_teacher=True)

	if Grade_9_Student.objects.filter(id=request.user.id, is_Grade_9_student_classC=True):
		a_s=Grade_9_Student.objects.filter(is_Grade_9_student_classC=True)
		a_t=Grade_9_Teacher_Class.objects.filter(is_grd9_classC_teacher=True)

	if Grade_9_Student.objects.filter(id=request.user.id, is_Grade_9_student_classD=True):
		a_s=Grade_9_Student.objects.filter(is_Grade_9_student_classD=True)
		a_t=Grade_9_Teacher_Class.objects.filter(is_grd9_classD_teacher=True)

	# Posts_TS=Post.objects.filter(userpost=i)
	for i in a_s:
		all_users.append(i)
	for i in a_t:
		all_users.append(i)
	for i in all_users:
		print(i.first_name)


	
	# for i in u_id:
	post=Post.objects.all().order_by('-date')
	print("-------------------------------")
	print(post)
	print("-------------------------------")

	

	context={'Posts':post,'all_teacher':a_t,"all_students":a_s,'students':students,'all_users':all_users}
	student_checker(request, context)

	return render(request, 'Grade9/Grd9ClsA/Grade9_Profile.html', context) 
        

def post_view(request):
    student = Grade_9_Student.objects.filter(id=request.user.id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.Teacher_signal = True
            for i in student:
                post = form.save(commit=False)  # Create a new Post instance but don't save it yet
                post.userpost = i  # Assign the userpost attribute
                post.save()  # Save the post to the database
            print("---------------------------------------------!!!success!!!---------------------------------------------")
            return redirect("Student:Student:Grade9_class_student")
    else:
        form = PostForm()
    
    context = {'form': form}
    student_checker(request, context)

    return render(request, 'Grade9/Grd9ClsA/G9T_post_news.html', context)
from taggit.models import Tag
from qa.models import Question
from qa.forms import QuestionForm
def new_question(request):
    AllTags = Tag.objects.all().values_list('name', flat=True)
    last_posted_q = Question.objects.filter(post_owner=request.user).last()
    is_olderThan_nintyMinutes = timezone.now() - timedelta(minutes=90)

    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            if last_posted_q is None:
                formTags = form.cleaned_data['tags']
                gettingBody = form.cleaned_data['body']
                gettingTitle = form.cleaned_data['title']
                new_post = form.save(commit=False)
                new_post.post_owner = request.user

                for typedTags in formTags:

                    check_if_everything_is_fine = all(
                        typedTags in AllTags for typedTags in formTags)

                    # if request.user.profile.create_tags:
                    #     if len(gettingBody) >= 0 and len(gettingBody) <= 29:
                    #         messages.error(
                    #             request, "Body Text should atleast 30 words. You entered " + str(len(gettingBody)))
                    #     elif len(gettingTitle) >= 0 and len(gettingTitle) <= 14:
                    #         messages.error(
                    #             request, "Title must be at least 15 characters.")
                    #     else:
                    #         print(form.errors)
                    #         form.save()
                    #         form.save_m2m()
                    #         if len(gettingBody) <= 200:
                    #             create_Low_Quality_Post_Instance, cre = LowQualityPostsCheck.objects.get_or_create(
                    #                 suggested_through="Automatic", low_is=new_post, why_low_quality="Question_Less_Than_200", is_completed=False)
                    #             createReview_item = ReviewLowQualityPosts.objects.get_or_create(
                    #                 review_of=create_Low_Quality_Post_Instance, is_question=new_post, is_reviewed=False)
                    #         return redirect('qa:questions')
                    if check_if_everything_is_fine:
                        if len(gettingBody) >= 0 and len(gettingBody) <= 29:
                            messages.error(
                                request, "Body Text should atleast 30 words. You entered " + str(len(gettingBody)))
                        elif len(gettingTitle) >= 0 and len(gettingTitle) <= 14:
                            messages.error(
                                request, "Title must be at least 15 characters.")
                        else:
                            form.save()
                            print(form.errors)
                            form.save_m2m()
                            if len(gettingBody) <= 200:
                                create_Low_Quality_Post_Instance, cre = LowQualityPostsCheck.objects.get_or_create(
                                    suggested_through="Automatic", low_is=new_post, why_low_quality="Question_Less_Than_200", is_completed=False)
                                createReview_item = ReviewLowQualityPosts.objects.get_or_create(
                                    review_of=create_Low_Quality_Post_Instance, is_question=new_post, is_reviewed=False)
                            return redirect('qa:questions')

                    else:
                        print("Problem 2")
                        messages.error(
                            request, f'You need atleast 1500 Reputation to create a New Tag - {formTags}')

            else:
                if not request.user.profile.remove_new_user_restrictions:
                    if last_posted_q.date >= is_olderThan_nintyMinutes:
                        messages.error(
                            request, 'Question Asking Limit Exceed, You will be able to ask in 90 minutes')
                    else:
                        formTags = form.cleaned_data['tags']
                        gettingBody = form.cleaned_data['body']
                        gettingTitle = form.cleaned_data['title']
                        new_post = form.save(commit=False)
                        new_post.post_owner = request.user

                        for typedTags in formTags:

                            check_if_everything_is_fine = all(
                                typedTags in AllTags for typedTags in formTags)

                            if request.user.profile.create_tags:
                                if len(gettingBody) >= 0 and len(
                                        gettingBody) <= 29:
                                    messages.error(
                                        request, "Body Text should atleast 30 words. You entered " + str(len(gettingBody)))
                                elif len(gettingTitle) >= 0 and len(gettingTitle) <= 14:
                                    messages.error(
                                        request, "Title must be at least 15 characters.")
                                else:
                                    form.save()
                                    print(form.errors)
                                    form.save_m2m()
                                    if len(gettingBody) <= 200:
                                        create_Low_Quality_Post_Instance, cre = LowQualityPostsCheck.objects.get_or_create(
                                            suggested_through="Automatic", low_is=new_post, why_low_quality="Question_Less_Than_200", is_completed=False)
                                        createReview_item = ReviewLowQualityPosts.objects.get_or_create(
                                            review_of=create_Low_Quality_Post_Instance, is_question=new_post, is_reviewed=False)
                                    return redirect('qa:questions')

                            elif check_if_everything_is_fine:
                                if len(gettingBody) >= 0 and len(
                                        gettingBody) <= 29:
                                    messages.error(
                                        request, "Body Text should atleast 30 words. You entered " + str(len(gettingBody)))
                                elif len(gettingTitle) >= 0 and len(gettingTitle) <= 14:
                                    messages.error(
                                        request, "Title must be at least 15 characters.")
                                else:
                                    form.save()
                                    print(form.errors)
                                    form.save_m2m()
                                    if len(gettingBody) <= 200:
                                        create_Low_Quality_Post_Instance, cre = LowQualityPostsCheck.objects.get_or_create(
                                            suggested_through="Automatic", low_is=new_post, why_low_quality="Question_Less_Than_200", is_completed=False)
                                        createReview_item = ReviewLowQualityPosts.objects.get_or_create(
                                            review_of=create_Low_Quality_Post_Instance, is_question=new_post, is_reviewed=False)
                                    return redirect('qa:questions')
                            else:
                                messages.error(
                                    request, f'You need atleast 1500 Reputation to create a New Tag - {typedTags}')
                else:
                    formTags = form.cleaned_data['tags']
                    gettingBody = form.cleaned_data['body']
                    gettingTitle = form.cleaned_data['title']

                    new_post = form.save(commit=False)
                    new_post.post_owner = request.user
                    for typedTags in formTags:

                        check_if_everything_is_fine = all(
                            typedTags in AllTags for typedTags in formTags)

                        if request.user.profile.create_tags:
                            print(len(gettingTitle))
                            if len(gettingBody) >= 0 and len(
                                    gettingBody) <= 29:
                                messages.error(
                                    request, "Body Text should atleast 30 words. You entered " + str(len(gettingBody)))
                            elif len(gettingTitle) >= 0 and len(gettingTitle) <= 14:
                                messages.error(
                                    request, "Title must be at least 15 characters.")
                            else:
                                form.save()
                                print(form.errors)
                                form.save_m2m()
                                if len(gettingBody) <= 200:
                                    create_Low_Quality_Post_Instance, cre = LowQualityPostsCheck.objects.get_or_create(
                                        suggested_through="Automatic", low_is=new_post, why_low_quality="Question_Less_Than_200", is_completed=False)
                                    createReview_item = ReviewLowQualityPosts.objects.get_or_create(
                                        review_of=create_Low_Quality_Post_Instance, is_question=new_post, is_reviewed=False)
                                return redirect('qa:questions')
                        elif check_if_everything_is_fine:
                            print(len(gettingBody))
                            if len(gettingBody) >= 0 and len(
                                    gettingBody) <= 29:
                                messages.error(
                                    request, "Body Text should atleast 30 words. You entered " + str(len(gettingBody)))
                            elif len(gettingTitle) >= 0 and len(gettingTitle) <= 14:
                                messages.error(
                                    request, "Title must be at least 15 characters.")
                            else:
                                # counting >= 0 and counting <= 29
                                print(form.errors)
                                form.save()
                                form.save_m2m()
                                if len(gettingBody) <= 200:
                                    create_Low_Quality_Post_Instance, cre = LowQualityPostsCheck.objects.get_or_create(
                                        suggested_through="Automatic", low_is=new_post, why_low_quality="Question_Less_Than_200", is_completed=False)
                                    createReview_item = ReviewLowQualityPosts.objects.get_or_create(
                                        review_of=create_Low_Quality_Post_Instance, is_question=new_post, is_reviewed=False)
                                return redirect('qa:questions')
                        else:
                            messages.error(
                                request, f'You need atleast 1500 Reputation to create a New Tag - {typedTags}')
    else:
        form = QuestionForm()

    context = {'form': form}
    return render(request, 'qa/new_question.html', context) 