from django.contrib import admin
from .Teacher_views.Grade9_views.Grd9_teacher_models import Grade_9_Teacher_Class
# Register your models here.
from Teacher.Teacher_views.Grade9_views.Grd9_assesment_models import (Grade_9_models_math_assesment)

from Teacher.Teacher_views.Grade9_views.Grd9_ClsA_views.Grd9ClsA_news_MVT import GrdClsA_news
from django.contrib.auth.admin import UserAdmin
class AccountAdminMain_Teacher_Gr9(UserAdmin):
	list_display=('email', 'username', 'date_joined', 'last_login', 'is_teacher', 'is_Grade_9_teacher', 'is_Grade_9_teacher_classA',  'is_Grade_9_teacher_classB',  'is_Grade_9_teacher_classC')
	search_fields=('email', 'username')
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal=()
	list_filter=('is_Grade_9_teacher_classA',  'is_Grade_9_teacher_classB',  'is_Grade_9_teacher_classC')
	fieldsets=()

class AccountAdmin_Teacher_Gr9ClsA(UserAdmin):
	list_display=('email', 'username', 'date_joined', 'last_login', 'is_Grade_9_teacher_classA')
	search_fields=('email', 'username')
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal=()
	list_filter=()
	fieldsets=()


admin.site.register(GrdClsA_news)
admin.site.register(Grade_9_models_math_assesment)

