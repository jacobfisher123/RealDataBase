from django.urls import path
from . import Grade_9_view
from .Grd9_User_views import Grd9_ClsA_views 


grade_9_urls=[
	path('all_teacher_list/Grade9_RegTeacher_List_view/Grade9_Teacher_signUp_view/', Grd9_ClsA_views.Grade9_Teacher_signUp_view.as_view() , name='Grade9_Teacher_signUp_view'),

	#All Grade 9 Teacher list view
	path('Display_all_teacher_list_view/Grade_9_teacher_list/', Grade_9_view.Grade_9_teacher_list, name='Grade_9_teacher_list'),
	path('all_teacher_list/Grade_9_teacher_list/TeacherGrd9_Class_SignUp_Detail_view<uuid:pk>/', Grd9_ClsA_views.TeacherGrd9_Class_SignUp_Detail_view.as_view(), name='TeacherGrd9_Class_SignUp_Detail_view'),
	#GRADE 9 CODES
	#This path code handles the list detail of a particular grade 9 teacher
	path('Display_all_teacher_list_view/Grade_9_teacher_list/Grade_9_Teacher_list_details<uuid:pk>/', Grade_9_view.Grade_9_Teacher_list_details, name='Grade_9_Teacher_list_details'),
	#This code handles the class assign regulator for grade 9 teachers
	path('Display_all_teacher_list_view/Grade_9_teacher_list/Grd9_Update_class_assign_regulator<uuid:pk>/', Grade_9_view.Grd9_Update_class_assign_regulator.as_view(), name='Grd9_Update_class_assign_regulator'),
	path('Display_all_teacher_list_view/Grade_9_teacher_list/Grd9_Update_main_class_assign_regulator<uuid:pk>/', Grade_9_view.Grd9_Update_main_class_assign_regulator.as_view(), name='Grd9_Update_main_class_assign_regulator'),
	#This path code handles the file upload regulator for grade 9 teachers
	path('Display_all_teacher_list_view/Grade_9_teacher_list/Grd9_Update_Teacher_file_regulator<uuid:pk>/', Grade_9_view.Grd9_Update_Teacher_file_regulator.as_view(), name='Grd9_Update_Teacher_file_regulator'),
	#Teacher subject type regulators for grade 9 teachers
	path('Display_all_teacher_list_view/Grade_9_teacher_list/Grd9_Update_math_teacher_type_regulator<uuid:pk>/', Grade_9_view.Grd9_Update_math_teacher_type_regulator.as_view(), name='Grd9_Update_math_teacher_type_regulator'),
	path('Display_all_teacher_list_view/Grade_9_teacher_list/Grd9_Update_english_teacher_type_regulator<uuid:pk>/', Grade_9_view.Grd9_Update_english_teacher_type_regulator.as_view(), name='Grd9_Update_english_teacher_type_regulator'),
	path('Display_all_teacher_list_view/Grade_9_teacher_list/Grd9_Update_science_teacher_type_regulator<uuid:pk>/', Grade_9_view.Grd9_Update_science_teacher_type_regulator.as_view(), name='Grd9_Update_science_teacher_type_regulator'),
	path('Display_all_teacher_list_view/Grade_9_teacher_list/Grd9_Update_socialscience_teacher_type_regulator<uuid:pk>/', Grade_9_view.Grd9_Update_socialscience_teacher_type_regulator.as_view(), name='Grd9_Update_socialscience_teacher_type_regulator'),
	path('Display_all_teacher_list_view/Grade_9_teacher_list/Grd9_Update_persdev_teacher_type_regulator<uuid:pk>/', Grade_9_view.Grd9_Update_persdev_teacher_type_regulator.as_view(), name='Grd9_Update_persdev_teacher_type_regulator'),

]