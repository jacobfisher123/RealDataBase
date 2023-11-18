from django.urls import path
from django.urls import path, include
from . import views
#from .Teacher_views.Grade9_views.Grd9_ClsA_views import Grade9_ClsA_Teacher_views
from .student_views.Grade9_std_views import Grade_9_Student_view



app_name='Student'

urlpatterns=[
    
    


    path('Grade9_classA_student/', include(([

        path('', Grade_9_Student_view.Grade9_class_student, name='Grade9_class_student'),
        path('post_view', Grade_9_Student_view.post_view, name='post_view'),
        path('CommentCreate/', Grade_9_Student_view.CommentCreate.as_view(), name='CommentCreate'),
        path('PostUpdate<slug:slug>', Grade_9_Student_view.PostUpdate.as_view(), name='PostUpdate'),
        path('post_detail<slug:slug>', Grade_9_Student_view.post_detail, name='post_detail'),
        path('PostDetailView', Grade_9_Student_view.PostDetailView.as_view(), name='PostDetailView'),
        path('new_question', Grade_9_Student_view.new_question, name='new_question'),
        path('delete_post<uuid:pk>', Grade_9_Student_view.delete_post, name='delete_post'),

        
        path('View_assesment_by_term/', Grade_9_Student_view.View_assesment_by_term, name='View_assesment_by_term'),
        path('View_Student_user_all_assesment<tm>/', Grade_9_Student_view.View_Student_user_all_assesment, name='View_Student_user_all_assesment'),
        path('View_Student_user_single_assesment<sbj><tm>/', Grade_9_Student_view.View_Student_user_single_assesment, name='View_Student_user_single_assesment'),
        path('View_Uploaded_assesment_files/', Grade_9_Student_view.View_Uploaded_assesment_files, name='View_Uploaded_assesment_files'),
        path('View_Uploaded_assesment_single_file<sbj>/', Grade_9_Student_view.View_Uploaded_assesment_single_file, name='View_Uploaded_assesment_single_file'),
        
        #view uploaded teacher files
        #MATH VIEW 1-2
        # path('Grd9_ClsA_math_subject_view/', Grd9_ClsA_std_views.Grd9_ClsA_math_subject_view, name='Grd9_ClsA_math_subject_view'),
        # #SCIENCE VIEW 1-2
        # path('Grd9_ClsA_science_view/', Grd9_ClsA_std_views.Grd9_ClsA_science_view, name='Grd9_ClsA_science_view'),
        # #SOCIAL SCIENCE VIEW 1-2
        # path('Grd9_ClsA_socialScn_view/', Grd9_ClsA_std_views.Grd9_ClsA_socialScn_view, name='Grd9_ClsA_socialScn_view'),
        # #PERSONAL DEVELOPMENT VIEW 1-2 
        # path('Grd9_ClsA_PersDev_view/', Grd9_ClsA_std_views.Grd9_ClsA_PersDev_view, name='Grd9_ClsA_PersDev_view'),
		# #ENGLISH VIEW 1-2 
		# path('Grd9_ClsA_english_view/', Grd9_ClsA_std_views.Grd9_ClsA_english_view, name='Grd9_ClsA_english_view'),


        	#Details of a single student Class A Grd 9 user
      
       	 	#These codes handles the student registration path
      
       		#These codes handles the chart visual analysis of Grd9 Cls A students

    ], 'Student'))),













	

	

	

]
