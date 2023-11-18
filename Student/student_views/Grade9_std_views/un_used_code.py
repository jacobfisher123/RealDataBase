
def View_Uploaded_assesment_single_file1(request,sbj):


	students=Grade_9_Student.objects.filter(id=request.user.id)
	if sbj=='1':
		if request.user.is_Grade_9_student_classA==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classA_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_math_files.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------A------------")
		if request.user.is_Grade_9_student_classB==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classB_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_math_files.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------B------------")
		if request.user.is_Grade_9_student_classC==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classC_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_math_files.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------C------------")
		if request.user.is_Grade_9_student_classD==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classD_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_math_files.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------D------------")
		if request.user.is_Grade_9_student_classE==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classE_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_math_files.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------E------------")
		if request.user.is_Grade_9_student_classF==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classF_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_math_files.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------F------------")
		if request.user.is_Grade_9_student_classG==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classG_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_math_files.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------G------------")
		if request.user.is_Grade_9_student_classH==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classH_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_math_files.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------H------------")
		if request.user.is_Grade_9_student_classI==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classI_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_math_files.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------I------------")
		if request.user.is_Grade_9_student_classJ==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classJ_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_math_files.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------J------------")
	if sbj=='2':
		if request.user.is_Grade_9_student_classA==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classA_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_LanguageLiterature_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------A------------")
		if request.user.is_Grade_9_student_classB==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classB_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_LanguageLiterature_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------B------------")
		if request.user.is_Grade_9_student_classC==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classC_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_LanguageLiterature_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------C------------")
		if request.user.is_Grade_9_student_classD==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classD_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_LanguageLiterature_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------D------------")
		if request.user.is_Grade_9_student_classE==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classE_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_LanguageLiterature_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------E------------")
		if request.user.is_Grade_9_student_classF==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classF_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_LanguageLiterature_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------F------------")
		if request.user.is_Grade_9_student_classG==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classG_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_LanguageLiterature_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------G------------")
		if request.user.is_Grade_9_student_classH==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classH_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_LanguageLiterature_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------H------------")
		if request.user.is_Grade_9_student_classI==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classI_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_LanguageLiterature_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------I------------")
		if request.user.is_Grade_9_student_classJ==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classJ_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_LanguageLiterature_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------J------------")
	if sbj=='3':
		if request.user.is_Grade_9_student_classA==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classA_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_Science_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------A------------")
		if request.user.is_Grade_9_student_classB==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classB_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_Science_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------B------------")
		if request.user.is_Grade_9_student_classC==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classC_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_Science_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------C------------")
		if request.user.is_Grade_9_student_classD==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classD_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_Science_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------D------------")
		if request.user.is_Grade_9_student_classE==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classE_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_Science_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------E------------")
		if request.user.is_Grade_9_student_classF==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classF_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_Science_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------F------------")
		if request.user.is_Grade_9_student_classG==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classG_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_Science_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------G------------")
		if request.user.is_Grade_9_student_classH==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classH_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_Science_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------H------------")
		if request.user.is_Grade_9_student_classI==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classI_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_Science_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------I------------")
		if request.user.is_Grade_9_student_classJ==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classJ_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_Science_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------J------------")
	if sbj=='4':
		if request.user.is_Grade_9_student_classA==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classA_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_SocialScience_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------A------------")
		if request.user.is_Grade_9_student_classB==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classB_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_SocialScience_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------B------------")
		if request.user.is_Grade_9_student_classC==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classC_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_SocialScience_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------C------------")
		if request.user.is_Grade_9_student_classD==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classD_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_SocialScience_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------D------------")
		if request.user.is_Grade_9_student_classE==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classE_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_SocialScience_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------E------------")
		if request.user.is_Grade_9_student_classF==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classF_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_SocialScience_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------F------------")
		if request.user.is_Grade_9_student_classG==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classG_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_SocialScience_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------G------------")
		if request.user.is_Grade_9_student_classH==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classH_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_SocialScience_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------H------------")
		if request.user.is_Grade_9_student_classI==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classI_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_SocialScience_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------I------------")
		if request.user.is_Grade_9_student_classJ==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classJ_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_SocialScience_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------J------------")
	if sbj=='5':
		if request.user.is_Grade_9_student_classA==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classA_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_PersonalDev_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------A------------")
		if request.user.is_Grade_9_student_classB==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classB_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_PersonalDev_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------B------------")
		if request.user.is_Grade_9_student_classC==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classC_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_PersonalDev_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------C------------")
		if request.user.is_Grade_9_student_classD==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classD_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_PersonalDev_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------D------------")
		if request.user.is_Grade_9_student_classE==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classE_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_PersonalDev_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------E------------")
		if request.user.is_Grade_9_student_classF==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classF_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_PersonalDev_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------F------------")
		if request.user.is_Grade_9_student_classG==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classG_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_PersonalDev_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------G------------")
		if request.user.is_Grade_9_student_classH==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classH_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_PersonalDev_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------H------------")
		if request.user.is_Grade_9_student_classI==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classI_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_PersonalDev_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------I------------")
		if request.user.is_Grade_9_student_classJ==True:
			class_teacher_=[]
			class_teacher=Grade_9_Teacher_Class.objects.filter(is_grd9_classJ_teacher=True,Grade_9_Math_subj_teach=True)
			for i in class_teacher:
				class_teacher_.append(i)
			subjects=Grade_9_models_PersonalDev_assesment.objects.filter(Teacher_user_Name=class_teacher_[0])
			print("------------J------------")





	context={'students':students,'subjects':subjects}
	return render(request, 'Grade9/Grd9ClsA/View_Uploaded_assesment_single_files.html', context)

