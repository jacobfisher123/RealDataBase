from django.shortcuts import render, redirect

# Create your views here.
def student_redirector(request):
	if request.user.is_Grade_9_student:
		if request.user.is_Grade_9_student_classA:
			return redirect("Student:Grade9_classA_student")
		elif request.user.is_Grade_9_student_classB:
			return redirect("Student:Grade9_classB_student")
		elif request.user.is_Grade_9_student_classC:
			return redirect("Student:Grade9_classC_student")
		elif request.user.is_Grade_9_student_classD:
			return redirect("Student:Grade9_classD_student")
		elif request.user.is_Grade_9_student_classE:
			return redirect("Student:Grade9_classE_student")
		elif request.user.is_Grade_9_student_classF:
			return redirect("Student:Grade9_classF_student")
		elif request.user.is_Grade_9_student_classG:
			return redirect("Student:Grade9_classG_student")
		elif request.user.is_Grade_9_student_classH:
			return redirect("Student:Grade9_classH_student")
		elif request.user.is_Grade_9_student_classI:
			return redirect("Student:Grade9_classI_student")
		elif request.user.is_Grade_9_student_classJ:
			return redirect("Student:Grade9_classJ_student")
		else:
			return redirect("login")