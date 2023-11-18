from django.urls import path, include
from . import views
#from .Teacher_views.Grade9_views.Grd9_ClsA_views import Grade9_ClsA_Teacher_views

from Teacher.Teacher_views.Grade9_views.Grd9_ClsA_views import Grd9_ClsA_Teach_view
#from Teacher.Teacher_views.Grade9_views.Grd9_ClsB_views import Grd9_ClsB_Teach_view
from Teacher.Teacher_views.Grade9_views.Grade_9_urls import urlpatterns_G9
from Teacher.Student_views.Grade_9_std.Grd9_ClsA_std import grd9_ClsA_chart_views
#from Teacher.Student_views.Grade_9_std.Grd9_ClsB_std import grd9_ClsB_chart_views
#assesment views
from Teacher.Teacher_views.Grade9_views.Grd9_ClsA_views.Grd9_ClsA_std.Grd_9_Marks_forms_and_views import Grd9_ClsA_assesment_views
#from Teacher.Student_views.Grade_9_std.Grd9_ClsB_std.Grd_9_Marks_forms_and_views import Grd9_ClsB_assesment_views
from Teacher.Teacher_views.Grade9_views.Grd9_ClsA_views.Grd9_ClsA_std.Grd_9_Marks_forms_and_views import Grd9_ClsA_assesment_views
"""
Grd9_ClsA_math_Term_1_assesment1_createview

Grd9_ClsA_math_Term_1_assesment1_view,
Grd9_ClsA_math_Term_2_assesment2_view,
Grd9_ClsA_math_Term_3_assesment3_view,
Grd9_ClsA_math_Term_4_assesment4_view
"""


# <uuid:pk>
app_name = 'Teacher'
urlpatterns=[
    # path('Grade9_classA_teacher/', include(([



            #This path lists all the students registered under Grade 9 Class A
        path('Grade9_classA_teacher/Grade_9_students_clsA_lists/', Grd9_ClsA_Teach_view.Grade_9_students_clsA_lists, name='Grade_9_students_clsA_lists'),
            #These codes handles the codes of uploading files __OPEN__
        #MATH UPLOAD 1-2
       
            #edit uploaded files
        path('Grd9_teach_edit_uploaded_files/', Grd9_ClsA_Teach_view.Grd9_teach_edit_uploaded_files, name='Grd9_teach_edit_uploaded_files'),
            #__CLOSES__
            #Details of a single student Class A Grd 9 user
        path('student_details_Grd9_clsA<uuid:pk>/?', Grd9_ClsA_Teach_view.student_details_Grd9_clsA, name='student_details_Grd9_clsA'),
        path('student_details_Grd9_clsA/Change_students_class_gr9A<uuid:pk>/?', Grd9_ClsA_Teach_view.Change_students_class_gr9A.as_view(), name='Change_students_class_gr9A'),
        
            #These codes handles the student registration path
        path('Grade_9_teacher_classA_Studevnt_SignUpView/', Grd9_ClsA_Teach_view.Grade_9_teacher_classA_Student_SignUpView.as_view(), name='Grade_9_teacher_classA_Student_SignUpView'),
        
        #THESE CODE UPDATES THE STUDENTS MARKS
            #Updated assessment marks
            #Term 1 assesments
            #MATH
    
 
        
    # ], 'Teacher'))),


]+urlpatterns_G9