#from Student.student_views.Grade9_std_views.Grade9_models import Grade_9_Student
from Student.student_views.Grade9_std_views.Grade9_models import Grade_9_Student
from Headmin.models import Account
#from Student.student_views.Grade9_std_views.Grade9_models import Grade_9_Student
#from Student.student_views.Grade9_std_views.Grade9_models import Grade_9_Student
from django import forms
from django.forms import ModelForm

from django.db import models  
from Headmin.models import Account
import uuid
from Teacher.Teacher_views.Grade9_views.Grd9_teacher_models import Grade_9_Teacher_Class
#create a boolean field of term 1-4 and a choice field of them in the form area

#create a boolean field of assesments 1-4 and a choice field of them in the form area
'''
Science
SocialScience
LanguageLiterature
Geography
Chemistry
'''

class Grade_9_models_math_assesment(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_Name=models.ForeignKey(Grade_9_Student, on_delete=models.CASCADE, default=None, max_length=250, blank=True, null=True)

    Term1_assesment=models.BooleanField(default=False)
    Term2_assesment=models.BooleanField(default=False)
    Term3_assesment=models.BooleanField(default=False)
    Term4_assesment=models.BooleanField(default=False)

    Title=models.CharField(max_length=50, blank=True, null=True)
    Desc=models.CharField(max_length=100, blank=True, null=True)
    is_Test=models.BooleanField(default=False)
    is_Assignement=models.BooleanField(default=False)
    Marks=models.IntegerField(blank=True, null=True, default=0)
    OutOfMarks=models.IntegerField(blank=True, null=True, default=0)
    DatePosted=models.DateTimeField(verbose_name='date posted', auto_now_add=True)

class Grade_9_models_Science_assesment(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_Name=models.ForeignKey(Grade_9_Student, on_delete=models.CASCADE, default=None, max_length=250, blank=True, null=True)

    Term1_assesment=models.BooleanField(default=False)
    Term2_assesment=models.BooleanField(default=False)
    Term3_assesment=models.BooleanField(default=False)
    Term4_assesment=models.BooleanField(default=False)

    Title=models.CharField(max_length=50, blank=True, null=True)
    Desc=models.CharField(max_length=100, blank=True, null=True)
    is_Test=models.BooleanField(default=False)
    is_Assignement=models.BooleanField(default=False)
    Marks=models.IntegerField(blank=True, null=True, default=0)
    OutOfMarks=models.IntegerField(blank=True, null=True, default=0)
    DatePosted=models.DateTimeField(verbose_name='date posted', auto_now_add=True)
class Grade_9_models_SocialScience_assesment(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_Name=models.ForeignKey(Grade_9_Student, on_delete=models.CASCADE, default=None, max_length=250, blank=True, null=True)

    Term1_assesment=models.BooleanField(default=False)
    Term2_assesment=models.BooleanField(default=False)
    Term3_assesment=models.BooleanField(default=False)
    Term4_assesment=models.BooleanField(default=False)

    Title=models.CharField(max_length=50, blank=True, null=True)
    Desc=models.CharField(max_length=100, blank=True, null=True)
    is_Test=models.BooleanField(default=False)
    is_Assignement=models.BooleanField(default=False)
    Marks=models.IntegerField(blank=True, null=True, default=0)
    OutOfMarks=models.IntegerField(blank=True, null=True, default=0)
    DatePosted=models.DateTimeField(verbose_name='date posted', auto_now_add=True)

class Grade_9_models_LanguageLiterature_assesment(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_Name=models.ForeignKey(Grade_9_Student, on_delete=models.CASCADE, default=None, max_length=250, blank=True, null=True)

    Term1_assesment=models.BooleanField(default=False)
    Term2_assesment=models.BooleanField(default=False)
    Term3_assesment=models.BooleanField(default=False)
    Term4_assesment=models.BooleanField(default=False)

    Title=models.CharField(max_length=50, blank=True, null=True)
    Desc=models.CharField(max_length=100, blank=True, null=True)
    is_Test=models.BooleanField(default=False)
    is_Assignement=models.BooleanField(default=False)
    Marks=models.IntegerField(blank=True, null=True, default=0)
    OutOfMarks=models.IntegerField(blank=True, null=True, default=0)
    DatePosted=models.DateTimeField(verbose_name='date posted', auto_now_add=True)


class Grade_9_models_Geography_assesment(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_Name=models.ForeignKey(Grade_9_Student, on_delete=models.CASCADE, default=None, max_length=250, blank=True, null=True)

    Term1_assesment=models.BooleanField(default=False)
    Term2_assesment=models.BooleanField(default=False)
    Term3_assesment=models.BooleanField(default=False)
    Term4_assesment=models.BooleanField(default=False)

    Title=models.CharField(max_length=50, blank=True, null=True)
    Desc=models.CharField(max_length=100, blank=True, null=True)
    is_Test=models.BooleanField(default=False)
    is_Assignement=models.BooleanField(default=False)
    Marks=models.IntegerField(blank=True, null=True, default=0)
    OutOfMarks=models.IntegerField(blank=True, null=True, default=0)
    DatePosted=models.DateTimeField(verbose_name='date posted', auto_now_add=True)
class Grade_9_models_Chemistry_assesment(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_Name=models.ForeignKey(Grade_9_Student, on_delete=models.CASCADE, default=None, max_length=250, blank=True, null=True)

    Term1_assesment=models.BooleanField(default=False)
    Term2_assesment=models.BooleanField(default=False)
    Term3_assesment=models.BooleanField(default=False)
    Term4_assesment=models.BooleanField(default=False)

    Title=models.CharField(max_length=50, blank=True, null=True)
    Desc=models.CharField(max_length=100, blank=True, null=True)
    is_Test=models.BooleanField(default=False)
    is_Assignement=models.BooleanField(default=False)
    Marks=models.IntegerField(blank=True, null=True, default=0)
    OutOfMarks=models.IntegerField(blank=True, null=True, default=0)
    DatePosted=models.DateTimeField(verbose_name='date posted', auto_now_add=True)
class Grade_9_models_PersonalDev_assesment(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_Name=models.ForeignKey(Grade_9_Student, on_delete=models.CASCADE, default=None, max_length=250, blank=True, null=True)

    Term1_assesment=models.BooleanField(default=False)
    Term2_assesment=models.BooleanField(default=False)
    Term3_assesment=models.BooleanField(default=False)
    Term4_assesment=models.BooleanField(default=False)

    Title=models.CharField(max_length=50, blank=True, null=True)
    Desc=models.CharField(max_length=100, blank=True, null=True)
    is_Test=models.BooleanField(default=False)
    is_Assignement=models.BooleanField(default=False)
    Marks=models.IntegerField(blank=True, null=True, default=0)
    OutOfMarks=models.IntegerField(blank=True, null=True, default=0)
    DatePosted=models.DateTimeField(verbose_name='date posted', auto_now_add=True)


class Grade_9_models_PersonalDev_assesment_Form(ModelForm):
    term_choices=(
    ('Select', "Select Term assesment"),
    ('Term1_assesment', "Term 1"),
    ('Term2_assesment', "Term 2"),
    ("Term3_assesment", "Term 3"),
    ("Term4_assesment", "Term 4"),)
    Term = forms.ChoiceField(choices = term_choices)
    assesment=(
    ('Select', "Select assesment type"),
    ('Test', "Test"),
    ('Assignment', "Assignment"),)
    assesment_type= forms.ChoiceField(choices = assesment)
    class Meta:
        model=Grade_9_models_PersonalDev_assesment
        fields=('Title','Desc','assesment_type','Marks','OutOfMarks','Term')

class Grade_9_models_math_assesment_Form(ModelForm):
    term_choices=(
    ('Select', "Select Term assesment"),
    ('Term1_assesment', "Term 1"),
    ('Term2_assesment', "Term 2"),
    ("Term3_assesment", "Term 3"),
    ("Term4_assesment", "Term 4"),)
    assesment=(
    ('Select', "Select assesment type"),
    ('Test', "Test"),
    ('Assignment', "Assignment"),)
    assesment_type= forms.ChoiceField(choices = assesment)
    Term = forms.ChoiceField(choices = term_choices)
    class Meta:
        model=Grade_9_models_math_assesment
        fields=('Title','Desc','assesment_type','Marks','OutOfMarks','Term')
class Grade_9_models_SocialScience_assesment_Form(ModelForm):
    term_choices=(
    ('Select', "Select Term assesment"),
    ('Term1_assesment', "Term 1"),
    ('Term2_assesment', "Term 2"),
    ("Term3_assesment", "Term 3"),
    ("Term4_assesment", "Term 4"),)
    Term = forms.ChoiceField(choices = term_choices)
    assesment=(
    ('Select', "Select assesment type"),
    ('Test', "Test"),
    ('Assignment', "Assignment"),)
    assesment_type= forms.ChoiceField(choices = assesment)
    class Meta:
        model=Grade_9_models_SocialScience_assesment
        fields=('Title','Desc','assesment_type','Marks','OutOfMarks','Term')
class Grade_9_models_Science_assesment_Form(ModelForm):
    term_choices=(
    ('Select', "Select Term assesment"),
    ('Term1_assesment', "Term 1"),
    ('Term2_assesment', "Term 2"),
    ("Term3_assesment", "Term 3"),
    ("Term4_assesment", "Term 4"),)
    Term = forms.ChoiceField(choices = term_choices)
    assesment=(
    ('Select', "Select assesment type"),
    ('Test', "Test"),
    ('Assignment', "Assignment"),)
    assesment_type= forms.ChoiceField(choices = assesment)
    class Meta:
        model=Grade_9_models_Science_assesment
        fields=('Title','Desc','assesment_type','Marks','OutOfMarks','Term')
class Grade_9_models_LanguageLiterature_assesment_Form(ModelForm):
    term_choices=(
    ('Select', "Select Term assesment"),
    ('Term1_assesment', "Term 1"),
    ('Term2_assesment', "Term 2"),
    ("Term3_assesment", "Term 3"),
    ("Term4_assesment", "Term 4"),)
    Term = forms.ChoiceField(choices = term_choices)
    assesment=(
    ('Select', "Select assesment type"),
    ('Test', "Test"),
    ('Assignment', "Assignment"),)
    assesment_type= forms.ChoiceField(choices = assesment)
    class Meta:
        model=Grade_9_models_LanguageLiterature_assesment
        fields=('Title','Desc','assesment_type','Marks','OutOfMarks','Term')
class Grade_9_models_Geography_assesment_Form(ModelForm):
    term_choices=(
    ('Select', "Select Term assesment"),
    ('Term1_assesment', "Term 1"),
    ('Term2_assesment', "Term 2"),
    ("Term3_assesment", "Term 3"),
    ("Term4_assesment", "Term 4"),)
    Term = forms.ChoiceField(choices = term_choices)
    assesment=(
    ('Select', "Select assesment type"),
    ('Test', "Test"),
    ('Assignment', "Assignment"),)
    assesment_type= forms.ChoiceField(choices = assesment)
    class Meta:
        model=Grade_9_models_Geography_assesment
        fields=('Title','Desc','assesment_type','Marks','OutOfMarks','Term')
class Grade_9_models__Chemistry_assesment_Form(ModelForm):
    term_choices=(
    ('Select', "Select Term assesment"),
    ('Term1_assesment', "Term 1"),
    ('Term2_assesment', "Term 2"),
    ("Term3_assesment", "Term 3"),
    ("Term4_assesment", "Term 4"),)
    Term = forms.ChoiceField(choices = term_choices)
    assesment=(
    ('Select', "Select assesment type"),
    ('Test', "Test"),
    ('Assignment', "Assignment"),)
    assesment_type= forms.ChoiceField(choices = assesment)
    class Meta:
        model=Grade_9_models_Chemistry_assesment
        fields=('Title','Desc','assesment_type','Marks','OutOfMarks','Term')


class Grade_9_models_math_files(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Teacher_user_Name=models.ForeignKey(Grade_9_Teacher_Class, on_delete=models.CASCADE, default=None, max_length=250, blank=True, null=True, related_name='math_teacher')
    Term1_assesment=models.BooleanField(default=False)
    Term2_assesment=models.BooleanField(default=False)
    Term3_assesment=models.BooleanField(default=False)
    Term4_assesment=models.BooleanField(default=False)

    Title=models.CharField(max_length=50, blank=True, null=True)
    Desc=models.CharField(max_length=100, blank=True, null=True)
    file_upload = models.FileField(upload_to='uploads/', blank=True, null=True)
    DatePosted=models.DateTimeField(verbose_name='date posted', auto_now_add=True)
    

class Grade_9_models_Science_files(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Teacher_user_Name=models.ForeignKey(Grade_9_Teacher_Class, on_delete=models.CASCADE, default=None, max_length=250, blank=True, null=True, related_name='science_teacher')
    Term1_assesment=models.BooleanField(default=False)
    Term2_assesment=models.BooleanField(default=False)
    Term3_assesment=models.BooleanField(default=False)
    Term4_assesment=models.BooleanField(default=False)

    Title=models.CharField(max_length=50, blank=True, null=True)
    Desc=models.CharField(max_length=100, blank=True, null=True)
    file_upload = models.FileField(upload_to='uploads/', blank=True, null=True)
    DatePosted=models.DateTimeField(verbose_name='date posted', auto_now_add=True)
class Grade_9_models_SocialScience_files(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Teacher_user_Name=models.ForeignKey(Grade_9_Teacher_Class, on_delete=models.CASCADE, default=None, max_length=250, blank=True, null=True, related_name='socialscience_teacher')
    

    Term1_assesment=models.BooleanField(default=False)
    Term2_assesment=models.BooleanField(default=False)
    Term3_assesment=models.BooleanField(default=False)
    Term4_assesment=models.BooleanField(default=False)

    Title=models.CharField(max_length=50, blank=True, null=True)
    Desc=models.CharField(max_length=100, blank=True, null=True)
    file_upload = models.FileField(upload_to='uploads/', blank=True, null=True)
    DatePosted=models.DateTimeField(verbose_name='date posted', auto_now_add=True)

class Grade_9_models_LanguageLiterature_files(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Teacher_user_Name=models.ForeignKey(Grade_9_Teacher_Class, on_delete=models.CASCADE, default=None, max_length=250, blank=True, null=True, related_name='languageNLiterature_teacher')
    

    Term1_assesment=models.BooleanField(default=False)
    Term2_assesment=models.BooleanField(default=False)
    Term3_assesment=models.BooleanField(default=False)
    Term4_assesment=models.BooleanField(default=False)

    Title=models.CharField(max_length=50, blank=True, null=True)
    Desc=models.CharField(max_length=100, blank=True, null=True)
    file_upload = models.FileField(upload_to='uploads/', blank=True, null=True)
    DatePosted=models.DateTimeField(verbose_name='date posted', auto_now_add=True)


class Grade_9_models_Geography_files(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Teacher_user_Name=models.ForeignKey(Grade_9_Teacher_Class, on_delete=models.CASCADE, default=None, max_length=250, blank=True, null=True, related_name='geo_teacher')
    

    Term1_assesment=models.BooleanField(default=False)
    Term2_assesment=models.BooleanField(default=False)
    Term3_assesment=models.BooleanField(default=False)
    Term4_assesment=models.BooleanField(default=False)

    Title=models.CharField(max_length=50, blank=True, null=True)
    Desc=models.CharField(max_length=100, blank=True, null=True)
    file_upload = models.FileField(upload_to='uploads/', blank=True, null=True)
    DatePosted=models.DateTimeField(verbose_name='date posted', auto_now_add=True)
class Grade_9_models_Chemistry_files(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Teacher_user_Name=models.ForeignKey(Grade_9_Teacher_Class, on_delete=models.CASCADE, default=None, max_length=250, blank=True, null=True, related_name='chemistry_teacher')
    student_user_Name=models.ForeignKey(Grade_9_Student, on_delete=models.CASCADE, default=None, max_length=250, blank=True, null=True)

    Term1_assesment=models.BooleanField(default=False)
    Term2_assesment=models.BooleanField(default=False)
    Term3_assesment=models.BooleanField(default=False)
    Term4_assesment=models.BooleanField(default=False)

    Title=models.CharField(max_length=50, blank=True, null=True)
    Desc=models.CharField(max_length=100, blank=True, null=True)
    file_upload = models.FileField(upload_to='uploads/', blank=True, null=True)
    DatePosted=models.DateTimeField(verbose_name='date posted', auto_now_add=True)
class Grade_9_models_PersonalDev_files(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Teacher_user_Name=models.ForeignKey(Grade_9_Teacher_Class, on_delete=models.CASCADE, default=None, max_length=250, blank=True, null=True, related_name='personalDev_teacher')
   

    Term1_assesment=models.BooleanField(default=False)
    Term2_assesment=models.BooleanField(default=False)
    Term3_assesment=models.BooleanField(default=False)
    Term4_assesment=models.BooleanField(default=False)

    Title=models.CharField(max_length=50, blank=True, null=True)
    Desc=models.CharField(max_length=100, blank=True, null=True)
    file_upload = models.FileField(upload_to='uploads/', blank=True, null=True)
    DatePosted=models.DateTimeField(verbose_name='date posted', auto_now_add=True)









class Grade9mathFilesForm(forms.ModelForm):
    term_choices=(
    ('Select', "Select Term assesment"),
    ('Term1_assesment', "Term 1"),
    ('Term2_assesment', "Term 2"),
    ("Term3_assesment", "Term 3"),
    ("Term4_assesment", "Term 4"),)
    Term = forms.ChoiceField(choices = term_choices)
    class Meta:
        model = Grade_9_models_math_files
        fields = [ 'Title', 'Desc', 'file_upload','Term']



class Grade9ScienceFilesForm(forms.ModelForm):
    term_choices=(
    ('Select', "Select Term assesment"),
    ('Term1_assesment', "Term 1"),
    ('Term2_assesment', "Term 2"),
    ("Term3_assesment", "Term 3"),
    ("Term4_assesment", "Term 4"),)
    Term = forms.ChoiceField(choices = term_choices)
    class Meta:
        model = Grade_9_models_Science_files
        fields = [ 'Title', 'Desc', 'file_upload','Term']

class Grade9SocialScienceFilesForm(forms.ModelForm):
    term_choices=(
    ('Select', "Select Term assesment"),
    ('Term1_assesment', "Term 1"),
    ('Term2_assesment', "Term 2"),
    ("Term3_assesment", "Term 3"),
    ("Term4_assesment", "Term 4"),)
    Term = forms.ChoiceField(choices = term_choices)
    class Meta:
        model = Grade_9_models_SocialScience_files
        fields = [ 'Title', 'Desc', 'file_upload','Term']

class Grade9LanguageLiteratureFilesForm(forms.ModelForm):
    term_choices=(
    ('Select', "Select Term assesment"),
    ('Term1_assesment', "Term 1"),
    ('Term2_assesment', "Term 2"),
    ("Term3_assesment", "Term 3"),
    ("Term4_assesment", "Term 4"),)
    Term = forms.ChoiceField(choices = term_choices)
    class Meta:
        model = Grade_9_models_LanguageLiterature_files
        fields = [ 'Title', 'Desc', 'file_upload','Term']
class Grade9GeographyFilesForm(forms.ModelForm):
    term_choices=(
    ('Select', "Select Term assesment"),
    ('Term1_assesment', "Term 1"),
    ('Term2_assesment', "Term 2"),
    ("Term3_assesment", "Term 3"),
    ("Term4_assesment", "Term 4"),)
    Term = forms.ChoiceField(choices = term_choices)
    class Meta:
        model = Grade_9_models_Geography_files
        fields = [ 'Title', 'Desc', 'file_upload','Term']
class Grade9ChemistryFilesForm(forms.ModelForm):
    term_choices=(
    ('Select', "Select Term assesment"),
    ('Term1_assesment', "Term 1"),
    ('Term2_assesment', "Term 2"),
    ("Term3_assesment", "Term 3"),
    ("Term4_assesment", "Term 4"),)
    Term = forms.ChoiceField(choices = term_choices)
    class Meta:
        model = Grade_9_models_Chemistry_files
        fields = [ 'Title', 'Desc', 'file_upload','Term']
class Grade9PersonalDevFilesForm(forms.ModelForm):
    term_choices=(
    ('Select', "Select Term assesment"),
    ('Term1_assesment', "Term 1"),
    ('Term2_assesment', "Term 2"),
    ("Term3_assesment", "Term 3"),
    ("Term4_assesment", "Term 4"),)
    Term = forms.ChoiceField(choices = term_choices)
    class Meta:
        model = Grade_9_models_PersonalDev_files
        fields = [ 'Title', 'Desc', 'file_upload','Term']
class Grade9MathAssessment_Edit_Form(forms.ModelForm):
    class Meta:
        model = Grade_9_models_math_assesment
        fields = ['Marks',]

class DeleteMathAssessmentForm(forms.Form):
    title_to_delete = forms.CharField(max_length=50, label='Title to Delete')