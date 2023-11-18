from django.urls import path
from . import views

from .Teacher_views.Grade_9_views.grade_9_urls import grade_9_urls



app_name='headmin'
urlpatterns=[
	path('', views.HeadminView, name='HeadminView'),
	#This deletes the post
	path('Delete_post_view<int:pk>/',views.Delete_post_view.as_view(), name='Delete_post_view'),
	path('post_view/',views.post_view, name='post_view'),
	#headmin post
	#path('Delete_admin_post<uuid:pk>/', views.Delete_admin_post, name='Delete_admin_post'),
	#List of all the teacher that the headmin wants to register 
	path('all_teacher_list/', views.all_teacher_list_view, name='all_teacher_reg'),
	path('Display_all_teacher_list_view/', views.Display_all_teacher_list_view, name='Display_all_teacher_list_view'),

]+grade_9_urls