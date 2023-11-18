from django.urls import path, include

#from .Teacher_views.Grade9_views.Grd9_ClsA_views import Grade9_ClsA_Teacher_views

from Teacher.Teacher_views.Grade9_views.Grd9_ClsA_views import Grd9_ClsA_Teach_view
#from Teacher.Teacher_views.Grade9_views.Grd9_ClsB_views import Grd9_ClsB_Teach_view

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


urlpatterns_G9=[
    # path('Grade9_classA_teacher/', include(([
        path('Grade9_class_teacher/', Grd9_ClsA_Teach_view.Grade9_classA_teacher, name='Grade9_classA_teacher'),
        path('Teacher_post_detail<slug:slug>/', Grd9_ClsA_Teach_view.Teacher_post_detail, name='Teacher_post_detail'),
         path('Grade9StudentUpdateView<uuid:pk>/', Grd9_ClsA_Teach_view.Grade9StudentUpdateView.as_view(), name='Grade9StudentUpdateView'),
        path('post_view/', Grd9_ClsA_Teach_view.post_view, name='post_view'),
        path('searchResult_view_grd9_A/', Grd9_ClsA_Teach_view.searchResult_view_grd9_A.as_view(), name='searchResult_view_grd9_A'),
        path('Grade_9_subj_view<uuid:pk>/<tm>/',Grd9_ClsA_Teach_view.Grade_9_subj_view, name='Grade_9_subj_view'),
        path('Grd9_ClsA_math_assesment_createview_all_std<Subj>/',Grd9_ClsA_Teach_view.Grd9_ClsA_math_assesment_createview_all_std, name='Grd9_ClsA_math_assesment_createview_all_std'),
        path('View_Uploaded_assesment/',Grd9_ClsA_Teach_view.View_Uploaded_assesment, name='View_Uploaded_assesment'),
        path('View_Uploaded_assesment_Term1/<tm>/',Grd9_ClsA_Teach_view.View_Uploaded_assesment_Term1, name='View_Uploaded_assesment_Term1'),
        path('View_Uploaded_assesment_all_subj/<snme>/',Grd9_ClsA_Teach_view.View_Uploaded_assesment_all_subj, name='View_Uploaded_assesment_all_subj'),
        path('Grd9_ClsA_Subj_files_createview_all_std/<Subj>/',Grd9_ClsA_Teach_view.Grd9_ClsA_Subj_files_createview_all_std, name='Grd9_ClsA_Subj_files_createview_all_std'),
        path('Grd9_ClsA_Subj_files_view_all_std/<Subj>/',Grd9_ClsA_Teach_view.Grd9_ClsA_Subj_files_view_all_std, name='Grd9_ClsA_Subj_files_view_all_std'),
        path('edit_assessment_one/<assessment_id>/<snme>',Grd9_ClsA_Teach_view.edit_assessment_one, name='edit_assessment_one'),
        path('delete_math_assessment/<snme>',Grd9_ClsA_Teach_view.delete_math_assessment, name='delete_math_assessment'),
        path('Grd9_Subj_files_view_all_std_delete/<uuid:assessment_id><Subj>',Grd9_ClsA_Teach_view.Grd9_Subj_files_view_all_std_delete, name='Grd9_Subj_files_view_all_std_delete'),
]

