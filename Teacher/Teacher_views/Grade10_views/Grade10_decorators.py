from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

#grd 9 decorators
def Grd9_ClsA_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
	actual_decorator=user_passes_test(
		lambda u: u.is_active and u.is_teacher and u.is_Grade_9_teacher_classA,
		redirect_field_name=redirect_field_name,
		login_url=login_url
		)
	if function:
		return actual_decorator(function)
	return actual_decorator

def Grd9_ClsB_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
	actual_decorator=user_passes_test(
		lambda u: u.is_active and u.is_teacher and u.is_Grade_9_teacher_classB,
		redirect_field_name=redirect_field_name,
		login_url=login_url
		)
	if function:
		return actual_decorator(function)
	return actual_decorator
def Grd9_ClsC_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
	actual_decorator=user_passes_test(
		lambda u: u.is_active and u.is_teacher and u.is_Grade_9_teacher_classC,
		redirect_field_name=redirect_field_name,
		login_url=login_url
		)
	if function:
		return actual_decorator(function)
	return actual_decorator
def Grd9_ClsD_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
	actual_decorator=user_passes_test(
		lambda u: u.is_active and u.is_teacher and u.is_Grade_9_teacher_classD,
		redirect_field_name=redirect_field_name,
		login_url=login_url
		)
	if function:
		return actual_decorator(function)
	return actual_decorator
def Grd9_ClsE_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
	actual_decorator=user_passes_test(
		lambda u: u.is_active and u.is_teacher and u.is_Grade_9_teacher_classE,
		redirect_field_name=redirect_field_name,
		login_url=login_url
		)
	if function:
		return actual_decorator(function)
	return actual_decorator
def Grd9_ClsF_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
	actual_decorator=user_passes_test(
		lambda u: u.is_active and u.is_teacher and u.is_Grade_9_teacher_classF,
		redirect_field_name=redirect_field_name,
		login_url=login_url
		)
	if function:
		return actual_decorator(function)
	return actual_decorator

def Grd9_ClsG_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
	actual_decorator=user_passes_test(
		lambda u: u.is_active and u.is_teacher and u.is_Grade_9_teacher_classG,
		redirect_field_name=redirect_field_name,
		login_url=login_url
		)
	if function:
		return actual_decorator(function)
	return actual_decorator
def Grd9_ClsH_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
	actual_decorator=user_passes_test(
		lambda u: u.is_active and u.is_teacher and u.is_Grade_9_teacher_classH,
		redirect_field_name=redirect_field_name,
		login_url=login_url
		)
	if function:
		return actual_decorator(function)
	return actual_decorator
def Grd9_ClsI_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
	actual_decorator=user_passes_test(
		lambda u: u.is_active and u.is_teacher and u.is_Grade_9_teacher_classI,
		redirect_field_name=redirect_field_name,
		login_url=login_url
		)
	if function:
		return actual_decorator(function)
	return actual_decorator
def Grd9_ClsJ_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
	actual_decorator=user_passes_test(
		lambda u: u.is_active and u.is_teacher and u.is_Grade_9_teacher_classJ,
		redirect_field_name=redirect_field_name,
		login_url=login_url
		)
	if function:
		return actual_decorator(function)
	return actual_decorator