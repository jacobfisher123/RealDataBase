# from django.forms import ModelForm
# from django import forms
# #Math assesment models 
# from Teacher.Teacher_views.Grade9_views.Grd9_assesment_models import (Grade_9_models_math_Term1_assesment_1, Grade_9_models_math_Term2_assesment_2, Grade_9_models_math_Term3_assesment_3, Grade_9_models_math_Term4_assesment_4)
# #English assesment models 
# from Teacher.Teacher_views.Grade9_views.Grd9_assesment_models import (Grade_9_models_English_Term1_assesment_1, Grade_9_models_English_Term2_assesment_2, Grade_9_models_English_Term3_assesment_3, Grade_9_models_English_Term4_assesment_4)
# #Science assesment models 
# from Teacher.Teacher_views.Grade9_views.Grd9_assesment_models import (Grade_9_models_Science_Term1_assesment_1, Grade_9_models_Science_Term2_assesment_2, Grade_9_models_Science_Term3_assesment_3, Grade_9_models_Science_Term4_assesment_4)
# #Social science assessment models
# from Teacher.Teacher_views.Grade9_views.Grd9_assesment_models import (Grade_9_models_SocialScience_Term1_assesment_1, Grade_9_models_SocialScience_Term2_assesment_2, Grade_9_models_SocialScience_Term3_assesment_3, Grade_9_models_SocialScience_Term4_assesment_4)
# #Personal development models
# from Teacher.Teacher_views.Grade9_views.Grd9_assesment_models import (Grade_9_models_PersonalDev_Term1_assesment_1, Grade_9_models_PersonalDev_Term2_assesment_2, Grade_9_models_PersonalDev_Term3_assesment_3, Grade_9_models_PersonalDev_Term4_assesment_4)

# from Student.student_views.Grade9_std_views.Grade9_models import Term_11_math_assesment, Grade_9_Student
# """
# class TestassesmentTesting(ModelForm):
#     class Meta:
#         model=Grade_9_Student
#         fields=['student_user_name']
# """


# #Forms
# #Term 1 
# #Maths assesment 1
# class Grd9_ClsA_math_Term_1_assesment1_form(ModelForm):
#     T1_A1_Maths_is_Test=forms.BooleanField(widget=forms.CheckboxInput)
#     class Meta:
#         model=Grade_9_models_math_Term1_assesment_1
#         fields=['T1_A1_Maths_Title', 'T1_A1_Maths_Desc', 'T1_A1_Maths_is_Test', 'T1_A1_Maths_Marks', 'T1_A1_Maths_OutOfMarks']

# #Term 2
# #Maths assesment 2
# class Grd9_ClsA_math_Term_2_assesment2_form(ModelForm):
#     T1_A2_Maths_is_Test=forms.BooleanField(widget=forms.CheckboxInput)
#     class Meta:
#         model=Grade_9_models_math_Term2_assesment_2
#         fields=['T2_A2_Maths_Title', 'T2_A2_Maths_Desc', 'T2_A2_Maths_is_Test', 'T2_A2_Maths_Marks', 'T2_A2_Maths_OutOfMarks']
# #Term 3
# #Maths assesment 3
# class Grd9_ClsA_math_Term_3_assesment3_form(ModelForm):
#     T1_A3_Maths_is_Test=forms.BooleanField(widget=forms.CheckboxInput)
#     class Meta:
#         model=Grade_9_models_math_Term3_assesment_3
#         fields=['T3_A3_Maths_Title', 'T3_A3_Maths_Desc', 'T3_A3_Maths_is_Test', 'T3_A3_Maths_Marks', 'T3_A3_Maths_OutOfMarks']
# #Term 4
# #Maths assesment 4
# class Grd9_ClsA_math_Term_4_assesment4_form(ModelForm):
#     T1_A4_Maths_is_Test=forms.BooleanField(widget=forms.CheckboxInput)
#     class Meta:
#         model=Grade_9_models_math_Term4_assesment_4
#         fields=['T4_A4_Maths_Title', 'T4_A4_Maths_Desc', 'T4_A4_Maths_is_Test', 'T4_A4_Maths_Marks', 'T4_A4_Maths_OutOfMarks']


# #Terms 1
# #English assesment 1
# class Grd9_ClsA_English_Term_1_assesment1_form(ModelForm):
#     T1_A1_English_is_Test=forms.BooleanField(widget=forms.CheckboxInput)
#     class Meta:
#         model=Grade_9_models_English_Term1_assesment_1
#         fields=['T1_A1_English_Title', 'T1_A1_English_Desc', 'T1_A1_English_is_Test', 'T1_A1_English_Marks', 'T1_A1_English_OutOfMarks']
# #Terms 2
# #English assesment 2
# class Grd9_ClsA_English_Term_2_assesment2_form(ModelForm):
#     T1_A2_English_is_Test=forms.BooleanField(widget=forms.CheckboxInput)
#     class Meta:
#         model=Grade_9_models_English_Term2_assesment_2
#         fields=['T2_A2_English_Title', 'T2_A2_English_Desc', 'T2_A2_English_is_Test', 'T2_A2_English_Marks', 'T2_A2_English_OutOfMarks']
# #Terms 3
# #English assesment 3
# class Grd9_ClsA_English_Term_3_assesment3_form(ModelForm):
#     T1_A3_English_is_Test=forms.BooleanField(widget=forms.CheckboxInput)
#     class Meta:
#         model=Grade_9_models_English_Term3_assesment_3
#         fields=['T3_A3_English_Title', 'T3_A3_English_Desc', 'T3_A3_English_is_Test', 'T3_A3_English_Marks', 'T3_A3_English_OutOfMarks']
# #Terms 4
# #English assesment 4
# class Grd9_ClsA_English_Term_4_assesment4_form(ModelForm):
#     T1_A4_English_is_Test=forms.BooleanField(widget=forms.CheckboxInput)
#     class Meta:
#         model=Grade_9_models_English_Term4_assesment_4
#         fields=['T4_A4_English_Title', 'T4_A4_English_Desc', 'T4_A4_English_is_Test', 'T4_A4_English_Marks', 'T4_A4_English_OutOfMarks']

# #Terms 1
# #Science assesment 1
# class Grd9_ClsA_Science_Term_1_assesment1_form(ModelForm):
#     T1_A1_Science_is_Test=forms.BooleanField(widget=forms.CheckboxInput)
#     class Meta:
#         model=Grade_9_models_Science_Term1_assesment_1
#         fields=['T1_A1_Science_Title', 'T1_A1_Science_Desc', 'T1_A1_Science_is_Test', 'T1_A1_Science_Marks', 'T1_A1_Science_OutOfMarks']
# #Terms 2
# #Science assesment 2
# class Grd9_ClsA_Science_Term_2_assesment2_form(ModelForm):
#     T1_A2_Science_is_Test=forms.BooleanField(widget=forms.CheckboxInput)
#     class Meta:
#         model=Grade_9_models_Science_Term2_assesment_2
#         fields=['T2_A2_Science_Title', 'T2_A2_Science_Desc', 'T2_A2_Science_is_Test', 'T2_A2_Science_Marks', 'T2_A2_Science_OutOfMarks']
# #Terms 3
# #Science assesment 3
# class Grd9_ClsA_Science_Term_3_assesment3_form(ModelForm):
#     T1_A3_Science_is_Test=forms.BooleanField(widget=forms.CheckboxInput)
#     class Meta:
#         model=Grade_9_models_Science_Term3_assesment_3
#         fields=['T3_A3_Science_Title', 'T3_A3_Science_Desc', 'T3_A3_Science_is_Test', 'T3_A3_Science_Marks', 'T3_A3_Science_OutOfMarks']
# #Terms 4
# #Science assesment 4
# class Grd9_ClsA_Science_Term_4_assesment4_form(ModelForm):
#     T1_A4_Science_is_Test=forms.BooleanField(widget=forms.CheckboxInput)
#     class Meta:
#         model=Grade_9_models_Science_Term4_assesment_4
#         fields=['T4_A4_Science_Title', 'T4_A4_Science_Desc', 'T4_A4_Science_is_Test', 'T4_A4_Science_Marks', 'T4_A4_Science_OutOfMarks']




# #Social science
# #Terms 1
# #Science assesment 1
# class Grd9_ClsA_SocialScience_Term_1_assesment1_form(ModelForm):
#     T1_A1_SocialScience_is_Test=forms.BooleanField(widget=forms.CheckboxInput)
#     class Meta:
#         model=Grade_9_models_SocialScience_Term1_assesment_1
#         fields=['T1_A1_SocialScience_Title', 'T1_A1_SocialScience_Desc', 'T1_A1_SocialScience_is_Test', 'T1_A1_SocialScience_Marks', 'T1_A1_SocialScience_OutOfMarks']
# #Terms 2
# #Science assesment 2
# class Grd9_ClsA_SocialScience_Term_2_assesment2_form(ModelForm):
#     T1_A2_SocialScience_is_Test=forms.BooleanField(widget=forms.CheckboxInput)
#     class Meta:
#         model=Grade_9_models_SocialScience_Term2_assesment_2
#         fields=['T2_A2_SocialScience_Title', 'T2_A2_SocialScience_Desc', 'T2_A2_SocialScience_is_Test', 'T2_A2_SocialScience_Marks', 'T2_A2_SocialScience_OutOfMarks']
# #Terms 3
# #Science assesment 3
# class Grd9_ClsA_SocialScience_Term_3_assesment3_form(ModelForm):
#     T1_A3_SocialScience_is_Test=forms.BooleanField(widget=forms.CheckboxInput)
#     class Meta:
#         model=Grade_9_models_SocialScience_Term3_assesment_3
#         fields=['T3_A3_SocialScience_Title', 'T3_A3_SocialScience_Desc', 'T3_A3_SocialScience_is_Test', 'T3_A3_SocialScience_Marks', 'T3_A3_SocialScience_OutOfMarks']
# #Terms 4
# #Science assesment 4
# class Grd9_ClsA_SocialScience_Term_4_assesment4_form(ModelForm):
#     T1_A4_SocialScience_is_Test=forms.BooleanField(widget=forms.CheckboxInput)
#     class Meta:
#         model=Grade_9_models_SocialScience_Term4_assesment_4
#         fields=['T4_A4_SocialScience_Title', 'T4_A4_SocialScience_Desc', 'T4_A4_SocialScience_is_Test', 'T4_A4_SocialScience_Marks', 'T4_A4_SocialScience_OutOfMarks']




# #Personal development
# #Terms 1
# #Science assesment 1
# class Grd9_ClsA_PersonalDev_Term_1_assesment1_form(ModelForm):
#     T1_A1_PersonalDev_is_Test=forms.BooleanField(widget=forms.CheckboxInput)
#     class Meta:
#         model=Grade_9_models_PersonalDev_Term1_assesment_1
#         fields=['T1_A1_PersonalDev_Title', 'T1_A1_PersonalDev_Desc', 'T1_A1_PersonalDev_is_Test', 'T1_A1_PersonalDev_Marks', 'T1_A1_PersonalDev_OutOfMarks']
# #Terms 2
# #Science assesment 2
# class Grd9_ClsA_PersonalDev_Term_2_assesment2_form(ModelForm):
#     T1_A2_PersonalDev_is_Test=forms.BooleanField(widget=forms.CheckboxInput)
#     class Meta:
#         model=Grade_9_models_PersonalDev_Term2_assesment_2
#         fields=['T2_A2_PersonalDev_Title', 'T2_A2_PersonalDev_Desc', 'T2_A2_PersonalDev_is_Test', 'T2_A2_PersonalDev_Marks', 'T2_A2_PersonalDev_OutOfMarks']
# #Terms 3
# #Science assesment 3
# class Grd9_ClsA_PersonalDev_Term_3_assesment3_form(ModelForm):
#     T1_A3_PersonalDev_is_Test=forms.BooleanField(widget=forms.CheckboxInput)
#     class Meta:
#         model=Grade_9_models_PersonalDev_Term3_assesment_3
#         fields=['T3_A3_PersonalDev_Title', 'T3_A3_PersonalDev_Desc', 'T3_A3_PersonalDev_is_Test', 'T3_A3_PersonalDev_Marks', 'T3_A3_PersonalDev_OutOfMarks']
# #Terms 4
# #Science assesment 4
# class Grd9_ClsA_PersonalDev_Term_4_assesment4_form(ModelForm):
#     T1_A4_PersonalDev_is_Test=forms.BooleanField(widget=forms.CheckboxInput)
#     class Meta:
#         model=Grade_9_models_PersonalDev_Term4_assesment_4
#         fields=['T4_A4_PersonalDev_Title', 'T4_A4_PersonalDev_Desc', 'T4_A4_PersonalDev_is_Test', 'T4_A4_PersonalDev_Marks', 'T4_A4_PersonalDev_OutOfMarks']
