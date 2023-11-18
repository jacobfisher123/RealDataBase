from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .student_views.Grade9_std_views.Grade9_models import (Term_11_math_assesment,Grade_9_Student)

#from .student_views.Grade9_std_views.Grade9_models import Term_11_math_assesment
class AccountAdminMain_Grd9(UserAdmin):
	list_display=('email', 'username', 'date_joined', 'last_login', 'is_student', 'is_Grade_9_student', 'is_Grade_9_student_classA',  'is_Grade_9_student_classB',  'is_Grade_9_student_classC', 
					'is_Grade_9_student_classD', 'is_Grade_9_student_classE', 'is_Grade_9_student_classF', 'is_Grade_9_student_classG', 'is_Grade_9_student_classH' ,'is_Grade_9_student_classI', 'is_Grade_9_student_classJ')
	search_fields=('email', 'username')
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal=()
	list_filter=('is_Grade_9_student_classA',  'is_Grade_9_student_classB',  'is_Grade_9_student_classC', 
					'is_Grade_9_student_classD', 'is_Grade_9_student_classE', 'is_Grade_9_student_classF', 'is_Grade_9_student_classG', 'is_Grade_9_student_classH' ,'is_Grade_9_student_classI', 'is_Grade_9_student_classJ')
	fieldsets=()
class Grd9ClsA(UserAdmin):
	list_display=('email', 'username', 'date_joined', 'last_login', 'is_Grade_9_student_classA')
	search_fields=('email', 'username')
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal=()
	list_filter=()
	fieldsets=()
class Grd9ClsB(UserAdmin):
	list_display=('email', 'username', 'date_joined', 'last_login', 'is_Grade_9_student_classB')
	search_fields=('email', 'username')
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal=()
	list_filter=()
	fieldsets=()
class Grd9ClsC(UserAdmin):
	list_display=('email', 'username', 'date_joined', 'last_login', 'is_Grade_9_student_classC')
	search_fields=('email', 'username')
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal=()
	list_filter=()
	fieldsets=()
class Grd9ClsD(UserAdmin):
	list_display=('email', 'username', 'date_joined', 'last_login', 'is_Grade_9_student_classD')
	search_fields=('email', 'username')
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal=()
	list_filter=()
	fieldsets=()
class Grd9ClsE(UserAdmin):
	list_display=('email', 'username', 'date_joined', 'last_login', 'is_Grade_9_student_classE')
	search_fields=('email', 'username')
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal=()
	list_filter=()
	fieldsets=()
class Grd9ClsF(UserAdmin):
	list_display=('email', 'username', 'date_joined', 'last_login', 'is_Grade_9_student_classF')
	search_fields=('email', 'username')
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal=()
	list_filter=()
	fieldsets=()
class Grd9ClsG(UserAdmin):
	list_display=('email', 'username', 'date_joined', 'last_login', 'is_Grade_9_student_classG')
	search_fields=('email', 'username')
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal=()
	list_filter=()
	fieldsets=()
class Grd9ClsH(UserAdmin):
	list_display=('email', 'username', 'date_joined', 'last_login', 'is_Grade_9_student_classH')
	search_fields=('email', 'username')
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal=()
	list_filter=()
	fieldsets=()
class Grd9ClsI(UserAdmin):
	list_display=('email', 'username', 'date_joined', 'last_login', 'is_Grade_9_student_classI')
	search_fields=('email', 'username')
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal=()
	list_filter=()
	fieldsets=()
class Grd9ClsJ(UserAdmin):
	list_display=('email', 'username', 'date_joined', 'last_login', 'is_Grade_9_student_classJ')
	search_fields=('email', 'username')
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal=()
	list_filter=()
	fieldsets=()

admin.site.register(Grade_9_Student, AccountAdminMain_Grd9)

admin.site.register(Term_11_math_assesment)

