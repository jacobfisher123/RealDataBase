def View_Uploaded_assesment_Term1(request, tm): 
   
    class_teacher=Grade_9_Teacher_Class.objects.filter(id=request.user.id)
    assessments_list = []
    if Grade_9_Teacher_Class.objects.filter(id=request.user.id, Grade_9_Math_subj_teach=True):
	    if tm=="1":
	    	unique_assessments = Grade_9_models_math_assesment.objects.filter(Term1_assesment=True).values('Title').distinct()
	    	if Grade_9_models_math_assesment.objects.filter(Term1_assesment=True).values('Title').distinct().count()>=1:
			    for assessment in unique_assessments:
			        # Retrieve the latest assessment object for each unique title and term
			        latest_assessment = Grade_9_models_math_assesment.objects.filter(
			            Term1_assesment=True,
			            Title=assessment['Title']
			        ).order_by('-DatePosted').first()
			        assessments_list.append(latest_assessment)
	    if tm=="2":
	    	unique_assessments = Grade_9_models_math_assesment.objects.filter(Term2_assesment=True).values('Title').distinct()
	    	if Grade_9_models_math_assesment.objects.filter(Term2_assesment=True).count()>=1:
			    for assessment in unique_assessments:
			        # Retrieve the latest assessment object for each unique title and term
			        latest_assessment = Grade_9_models_math_assesment.objects.filter(
			            Term2_assesment=True,
			            Title=assessment['Title']
			        ).order_by('-DatePosted').first()
			        assessments_list.append(latest_assessment)
	    if tm=="3":
	    	unique_assessments = Grade_9_models_math_assesment.objects.filter(Term3_assesment=True).values('Title').distinct()
	    	for assessment in unique_assessments:
		        # Retrieve the latest assessment object for each unique title and term
		        latest_assessment = Grade_9_models_math_assesment.objects.filter(
		            Term3_assesment=True,
		            Title=assessment['Title']
		        ).order_by('-DatePosted').first()
		        assessments_list.append(latest_assessment)
	    if tm=="4":
	    	unique_assessments = Grade_9_models_math_assesment.objects.filter(Term4_assesment=True).values('Title').distinct()
	    	for assessment in unique_assessments:
		        # Retrieve the latest assessment object for each unique title and term
		        latest_assessment = Grade_9_models_math_assesment.objects.filter(
		            Term4_assesment=True,
		            Title=assessment['Title']
		        ).order_by('-DatePosted').first()
		        assessments_list.append(latest_assessment)
    if Grade_9_Teacher_Class.objects.filter(id=request.user.id, Grade_9_Engl_subj_teach=True):
	    if tm=="1":
	    	unique_assessments = Grade_9_models_LanguageLiterature_assesment.objects.filter(Term1_assesment=True).values('Title').distinct()
	    	if Grade_9_models_LanguageLiterature_assesment.objects.filter(Term1_assesment=True).values('Title').distinct().count()>=1:
			    for assessment in unique_assessments:
			        # Retrieve the latest assessment object for each unique title and term
			        latest_assessment = Grade_9_models_LanguageLiterature_assesment.objects.filter(
			            Term1_assesment=True,
			            Title=assessment['Title']
			        ).order_by('-DatePosted').first()
			        assessments_list.append(latest_assessment)
	    if tm=="2":
	    	unique_assessments = Grade_9_models_LanguageLiterature_assesment.objects.filter(Term2_assesment=True).values('Title').distinct()
	    	if Grade_9_models_LanguageLiterature_assesment.objects.filter(Term2_assesment=True).count()>=1:
			    for assessment in unique_assessments:
			        # Retrieve the latest assessment object for each unique title and term
			        latest_assessment = Grade_9_models_LanguageLiterature_assesment.objects.filter(
			            Term2_assesment=True,
			            Title=assessment['Title']
			        ).order_by('-DatePosted').first()
			        assessments_list.append(latest_assessment)
	    if tm=="3":
	    	unique_assessments = Grade_9_models_LanguageLiterature_assesment.objects.filter(Term3_assesment=True).values('Title').distinct()
	    	for assessment in unique_assessments:
		        # Retrieve the latest assessment object for each unique title and term
		        latest_assessment = Grade_9_models_LanguageLiterature_assesment.objects.filter(
		            Term3_assesment=True,
		            Title=assessment['Title']
		        ).order_by('-DatePosted').first()
		        assessments_list.append(latest_assessment)
	    if tm=="4":
	    	unique_assessments = Grade_9_models_LanguageLiterature_assesment.objects.filter(Term4_assesment=True).values('Maths_Title').distinct()
	    	for assessment in unique_assessments:
		        # Retrieve the latest assessment object for each unique title and term
		        latest_assessment = Grade_9_models_LanguageLiterature_assesment.objects.filter(
		            Term4_assesment=True,
		            Title=assessment['Title']
		        ).order_by('-DatePosted').first()
		        assessments_list.append(latest_assessment)
    if Grade_9_Teacher_Class.objects.filter(id=request.user.id, Grade_9_Scn_subj_teach=True):
	    if tm=="1":
	    	unique_assessments = Grade_9_models_Science_assesment.objects.filter(Term1_assesment=True).values('Title').distinct()
	    	if Grade_9_models_Science_assesment.objects.filter(Term1_assesment=True).values('Title').distinct().count()>=1:
			    for assessment in unique_assessments:
			        # Retrieve the latest assessment object for each unique title and term
			        latest_assessment = Grade_9_models_Science_assesment.objects.filter(
			            Term1_assesment=True,
			            Title=assessment['Title']
			        ).order_by('-DatePosted').first()
			        assessments_list.append(latest_assessment)
	    if tm=="2":
	    	unique_assessments = Grade_9_models_Science_assesment.objects.filter(Term2_assesment=True).values('Title').distinct()
	    	if Grade_9_models_Science_assesment.objects.filter(Term2_assesment=True).count()>=1:
			    for assessment in unique_assessments:
			        # Retrieve the latest assessment object for each unique title and term
			        latest_assessment = Grade_9_models_Science_assesment.objects.filter(
			            Term2_assesment=True,
			            LanguageLiterature_Title=assessment['Title']
			        ).order_by('-DatePosted').first()
			        assessments_list.append(latest_assessment)
	    if tm=="3":
	    	unique_assessments = Grade_9_models_Science_assesment.objects.filter(Term3_assesment=True).values('Title').distinct()
	    	for assessment in unique_assessments:
		        # Retrieve the latest assessment object for each unique title and term
		        latest_assessment = Grade_9_models_Science_assesment.objects.filter(
		            Term3_assesment=True,
		            LanguageLiterature_Title=assessment['Title']
		        ).order_by('-DatePosted').first()
		        assessments_list.append(latest_assessment)
	    if tm=="4":
	    	unique_assessments = Grade_9_models_Science_assesment.objects.filter(Term4_assesment=True).values('Title').distinct()
	    	for assessment in unique_assessments:
		        # Retrieve the latest assessment object for each unique title and term
		        latest_assessment = Grade_9_models_Science_assesment.objects.filter(
		            Term4_assesment=True,
		            LanguageLiterature_Title=assessment['Title']
		        ).order_by('-DatePosted').first()
		        assessments_list.append(latest_assessment)
    if Grade_9_Teacher_Class.objects.filter(id=request.user.id, Grade_9_SocSnc_subj_teach=True):
	    if tm=="1":
	    	unique_assessments = Grade_9_models_LanguageLiterature_assesment.objects.filter(Term1_assesment=True).values('Title').distinct()
	    	if Grade_9_models_LanguageLiterature_assesment.objects.filter(Term1_assesment=True).values('Title').distinct().count()>=1:
			    for assessment in unique_assessments:
			        # Retrieve the latest assessment object for each unique title and term
			        latest_assessment = Grade_9_models_LanguageLiterature_assesment.objects.filter(
			            Term1_assesment=True,
			            Title=assessment['Title']
			        ).order_by('-DatePosted').first()
			        assessments_list.append(latest_assessment)
	    if tm=="2":
	    	unique_assessments = Grade_9_models_LanguageLiterature_assesment.objects.filter(Term2_assesment=True).values('Title').distinct()
	    	if Grade_9_models_LanguageLiterature_assesment.objects.filter(Term2_assesment=True).count()>=1:
			    for assessment in unique_assessments:
			        # Retrieve the latest assessment object for each unique title and term
			        latest_assessment = Grade_9_models_LanguageLiterature_assesment.objects.filter(
			            Term2_assesment=True,
			            Title=assessment['Title']
			        ).order_by('-DatePosted').first()
			        assessments_list.append(latest_assessment)
	    if tm=="3":
	    	unique_assessments = Grade_9_models_LanguageLiterature_assesment.objects.filter(Term3_assesment=True).values('Title').distinct()
	    	for assessment in unique_assessments:
		        # Retrieve the latest assessment object for each unique title and term
		        latest_assessment = Grade_9_models_LanguageLiterature_assesment.objects.filter(
		            Term3_assesment=True,
		            Title=assessment['Title']
		        ).order_by('-DatePosted').first()
		        assessments_list.append(latest_assessment)
	    if tm=="4":
	    	unique_assessments = Grade_9_models_LanguageLiterature_assesment.objects.filter(Term4_assesment=True).values('Title').distinct()
	    	for assessment in unique_assessments:
		        # Retrieve the latest assessment object for each unique title and term
		        latest_assessment = Grade_9_models_LanguageLiterature_assesment.objects.filter(
		            Term4_assesment=True,
		            Title=assessment['Title']
		        ).order_by('-DatePosted').first()
		        assessments_list.append(latest_assessment)
    if Grade_9_Teacher_Class.objects.filter(id=request.user.id, Grade_9_PersDev_subj_teach=True):
	    if tm=="1":
	    	unique_assessments = Grade_9_models_LanguageLiterature_assesment.objects.filter(Term1_assesment=True).values('PersonalDev_Title').distinct()
	    	if Grade_9_models_LanguageLiterature_assesment.objects.filter(Term1_assesment=True).values('PersonalDev_Title').distinct().count()>=1:
			    for assessment in unique_assessments:
			        # Retrieve the latest assessment object for each unique title and term
			        latest_assessment = Grade_9_models_LanguageLiterature_assesment.objects.filter(
			            Term1_assesment=True,
			            PersonalDev_Title=assessment['PersonalDev_Title']
			        ).order_by('-Maths_DatePosted').first()
			        assessments_list.append(latest_assessment) 
	    if tm=="2":
	    	unique_assessments = Grade_9_models_LanguageLiterature_assesment.objects.filter(Term2_assesment=True).values('PersonalDev_Title').distinct()
	    	if Grade_9_models_LanguageLiterature_assesment.objects.filter(Term2_assesment=True).count()>=1:
			    for assessment in unique_assessments:
			        # Retrieve the latest assessment object for each unique title and term
			        latest_assessment = Grade_9_models_LanguageLiterature_assesment.objects.filter(
			            Term2_assesment=True,
			            PersonalDev_Title=assessment['PersonalDev_Title']
			        ).order_by('-Maths_DatePosted').first()
			        assessments_list.append(latest_assessment)
	    if tm=="3":
	    	unique_assessments = Grade_9_models_LanguageLiterature_assesment.objects.filter(Term3_assesment=True).values('PersonalDev_Title').distinct()
	    	for assessment in unique_assessments:
		        # Retrieve the latest assessment object for each unique title and term
		        latest_assessment = Grade_9_models_LanguageLiterature_assesment.objects.filter(
		            Term3_assesment=True,
		            PersonalDev_Title=assessment['PersonalDev_Title']
		        ).order_by('-Maths_DatePosted').first()
		        assessments_list.append(latest_assessment)
	    if tm=="4":
	    	unique_assessments = Grade_9_models_LanguageLiterature_assesment.objects.filter(Term4_assesment=True).values('PersonalDev_Title').distinct()
	    	for assessment in unique_assessments:
		        # Retrieve the latest assessment object for each unique title and term
		        latest_assessment = Grade_9_models_LanguageLiterature_assesment.objects.filter(
		            Term4_assesment=True,
		            PersonalDev_Title=assessment['PersonalDev_Title']
		        ).order_by('-Maths_DatePosted').first()
		        assessments_list.append(latest_assessment)

    context = {'subjects': assessments_list,'teachers':class_teacher}
   
    class_teacher_subj_checker(request,context)
    class_teacher_checker(request,context)
    return render(request, 'Grade9Teach/Grade9_Student_subj_templates/View_Uploaded_assesment_Term1.html', context)
def Grd9_ClsA_Subj_files_createview_all_std1(request,Subj):
	print("---------------------")
	print("{}".format(Subj))
	print("---------------------")
	class_teacher=Grade_9_Teacher_Class.objects.filter(id=request.user.id)
	all_students = []
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classA_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classA=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classB_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classB=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classC_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classC=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classD_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classD=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classE_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classE=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classF_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classF=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classG_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classG=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classH_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classH=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classI_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classI=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classJ_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classJ=True)
		cord(std,all_students)

	if Subj=='Math':
		
		for i in class_teacher:
			print(i)
			if request.method=='POST':

				form=Grade9mathFilesForm(request.POST, request.FILES)
				if form.is_valid():
					print(request.POST.get('Term'))
					instance=form.save(commit=False)
					instance.Teacher_user_Name=i
					if request.POST.get('assesment_type')=='Assignment':
						instance.Maths_is_Assignement=True
					if request.POST.get('assesment_type')=='Test':
						instance.Maths_is_Test=True
					if request.POST.get('Term')=='Term1_assesment':
						instance.Term1_assesment=True
						instance.save()
						tm=1
					elif request.POST.get('Term')=='Term2_assesment':
						instance.Term2_assesment=True
						instance.save()
						tm=2
					elif request.POST.get('Term')=='Term3_assesment':
						instance.Term3_assesment=True
						instance.save()
						tm=3
					elif request.POST.get('Term')=='Term4_assesment':
						instance.Term4_assesment=True
						instance.save()
						tm=4
					else:
						print("failed")
				return redirect('Teacher:Grd9_ClsA_Subj_files_view_all_std',Subj=Subj)
				
			else:
				form=Grade9mathFilesForm()
	if Subj=='English':
		
		for i in class_teacher:
			print(i)
			if request.method=='POST':

				form=Grade9LanguageLiteratureFilesForm(request.POST, request.FILES)
				if form.is_valid():
					print(request.POST.get('Term'))
					instance=form.save(commit=False)
					instance.Teacher_user_Name=i
					if request.POST.get('assesment_type')=='Assignment':
						instance.Maths_is_Assignement=True
					if request.POST.get('assesment_type')=='Test':
						instance.Maths_is_Test=True
					if request.POST.get('Term')=='Term1_assesment':
						instance.Term1_assesment=True
						instance.save()
						tm=1
					elif request.POST.get('Term')=='Term2_assesment':
						instance.Term2_assesment=True
						instance.save()
						tm=2
					elif request.POST.get('Term')=='Term3_assesment':
						instance.Term3_assesment=True
						instance.save()
						tm=3
					elif request.POST.get('Term')=='Term4_assesment':
						instance.Term4_assesment=True
						instance.save()
						tm=4
					else:
						print("failed")
				return redirect('Teacher:Grd9_ClsA_Subj_files_view_all_std',Subj=Subj)
				
			else:
				form=Grade9LanguageLiteratureFilesForm()
	if Subj=='Science':
		
		for i in class_teacher:
			print(i)
			if request.method=='POST':

				form=Grade9ScienceFilesForm(request.POST, request.FILES)
				if form.is_valid():
					print(request.POST.get('Term'))
					instance=form.save(commit=False)
					instance.Teacher_user_Name=i
					if request.POST.get('assesment_type')=='Assignment':
						instance.Maths_is_Assignement=True
					if request.POST.get('assesment_type')=='Test':
						instance.Maths_is_Test=True
					if request.POST.get('Term')=='Term1_assesment':
						instance.Term1_assesment=True
						instance.save()
						tm=1
					elif request.POST.get('Term')=='Term2_assesment':
						instance.Term2_assesment=True
						instance.save()
						tm=2
					elif request.POST.get('Term')=='Term3_assesment':
						instance.Term3_assesment=True
						instance.save()
						tm=3
					elif request.POST.get('Term')=='Term4_assesment':
						instance.Term4_assesment=True
						instance.save()
						tm=4
					else:
						print("failed")
				return redirect('Teacher:Grd9_ClsA_Subj_files_view_all_std',Subj=Subj)
				
			else:
				form=Grade9ScienceFilesForm()
	if Subj=='Social Science':
		
		for i in class_teacher:
			print(i)
			if request.method=='POST':

				form=Grade9SocialScienceFilesForm(request.POST, request.FILES)
				if form.is_valid():
					print(request.POST.get('Term'))
					instance=form.save(commit=False)
					instance.Teacher_user_Name=i
					if request.POST.get('assesment_type')=='Assignment':
						instance.Maths_is_Assignement=True
					if request.POST.get('assesment_type')=='Test':
						instance.Maths_is_Test=True
					if request.POST.get('Term')=='Term1_assesment':
						instance.Term1_assesment=True
						instance.save()
						tm=1
					elif request.POST.get('Term')=='Term2_assesment':
						instance.Term2_assesment=True
						instance.save()
						tm=2
					elif request.POST.get('Term')=='Term3_assesment':
						instance.Term3_assesment=True
						instance.save()
						tm=3
					elif request.POST.get('Term')=='Term4_assesment':
						instance.Term4_assesment=True
						instance.save()
						tm=4
					else:
						print("failed")
				return redirect('Teacher:Grd9_ClsA_Subj_files_view_all_std',Subj=Subj)
				
			else:
				form=Grade9SocialScienceFilesForm()
	if Subj=='Perosnal Development':
		
		for i in class_teacher:
			print(i)
			if request.method=='POST':

				form=Grade9PersonalDevFilesForm(request.POST, request.FILES)
				if form.is_valid():
					print(request.POST.get('Term'))
					instance=form.save(commit=False)
					instance.Teacher_user_Name=i
					if request.POST.get('assesment_type')=='Assignment':
						instance.Maths_is_Assignement=True
					if request.POST.get('assesment_type')=='Test':
						instance.Maths_is_Test=True
					if request.POST.get('Term')=='Term1_assesment':
						instance.Term1_assesment=True
						instance.save()
						tm=1
					elif request.POST.get('Term')=='Term2_assesment':
						instance.Term2_assesment=True
						instance.save()
						tm=2
					elif request.POST.get('Term')=='Term3_assesment':
						instance.Term3_assesment=True
						instance.save()
						tm=3
					elif request.POST.get('Term')=='Term4_assesment':
						instance.Term4_assesment=True
						instance.save()
						tm=4
					else:
						print("failed")
				return redirect('Teacher:Grd9_ClsA_Subj_files_view_all_std',Subj=Subj)
				
			else:
				form=Grade9PersonalDevFilesForm()


	context={'form':form, 'teachers':class_teacher,'Subj':Subj}
	class_teacher_subj_checker(request,context)
	class_teacher_checker(request,context)
	return render(request, 'Grade9Teach/Grade9_Student_subj_templates/Grade_9_Math_subj_view.html', context)

def Grd9_ClsA_Subj_files_createview_all_std(request,Subj):
	print("---------------------")
	print("{}".format(Subj))
	print("---------------------")
	class_teacher=Grade_9_Teacher_Class.objects.filter(id=request.user.id)
	all_students = []
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classA_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classA=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classB_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classB=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classC_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classC=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classD_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classD=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classE_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classE=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classF_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classF=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classG_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classG=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classH_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classH=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classI_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classI=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classJ_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classJ=True)
		cord(std,all_students)

	if Subj=='Math':
		
		for i in class_teacher:
			print(i)
			if request.method=='POST':

				form=Grade9mathFilesForm(request.POST, request.FILES)
				if form.is_valid():
					print(request.POST.get('Term'))
					instance=form.save(commit=False)
					instance.Teacher_user_Name=i
					if request.POST.get('assesment_type')=='Assignment':
						instance.Maths_is_Assignement=True
					if request.POST.get('assesment_type')=='Test':
						instance.Maths_is_Test=True
					if request.POST.get('Term')=='Term1_assesment':
						instance.Term1_assesment=True
						instance.save()
						tm=1
					elif request.POST.get('Term')=='Term2_assesment':
						instance.Term2_assesment=True
						instance.save()
						tm=2
					elif request.POST.get('Term')=='Term3_assesment':
						instance.Term3_assesment=True
						instance.save()
						tm=3
					elif request.POST.get('Term')=='Term4_assesment':
						instance.Term4_assesment=True
						instance.save()
						tm=4
					else:
						print("failed")
				return redirect('Teacher:Grd9_ClsA_Subj_files_view_all_std',Subj=Subj)
				
			else:
				form=Grade9mathFilesForm()
	if Subj=='English':
		
		for i in class_teacher:
			print(i)
			if request.method=='POST':

				form=Grade9LanguageLiteratureFilesForm(request.POST, request.FILES)
				if form.is_valid():
					print(request.POST.get('Term'))
					instance=form.save(commit=False)
					instance.Teacher_user_Name=i
					if request.POST.get('assesment_type')=='Assignment':
						instance.Maths_is_Assignement=True
					if request.POST.get('assesment_type')=='Test':
						instance.Maths_is_Test=True
					if request.POST.get('Term')=='Term1_assesment':
						instance.Term1_assesment=True
						instance.save()
						tm=1
					elif request.POST.get('Term')=='Term2_assesment':
						instance.Term2_assesment=True
						instance.save()
						tm=2
					elif request.POST.get('Term')=='Term3_assesment':
						instance.Term3_assesment=True
						instance.save()
						tm=3
					elif request.POST.get('Term')=='Term4_assesment':
						instance.Term4_assesment=True
						instance.save()
						tm=4
					else:
						print("failed")
				return redirect('Teacher:Grd9_ClsA_Subj_files_view_all_std',Subj=Subj)
				
			else:
				form=Grade9LanguageLiteratureFilesForm()
	if Subj=='Science':
		
		for i in class_teacher:
			print(i)
			if request.method=='POST':

				form=Grade9ScienceFilesForm(request.POST, request.FILES)
				if form.is_valid():
					print(request.POST.get('Term'))
					instance=form.save(commit=False)
					instance.Teacher_user_Name=i
					if request.POST.get('assesment_type')=='Assignment':
						instance.Maths_is_Assignement=True
					if request.POST.get('assesment_type')=='Test':
						instance.Maths_is_Test=True
					if request.POST.get('Term')=='Term1_assesment':
						instance.Term1_assesment=True
						instance.save()
						tm=1
					elif request.POST.get('Term')=='Term2_assesment':
						instance.Term2_assesment=True
						instance.save()
						tm=2
					elif request.POST.get('Term')=='Term3_assesment':
						instance.Term3_assesment=True
						instance.save()
						tm=3
					elif request.POST.get('Term')=='Term4_assesment':
						instance.Term4_assesment=True
						instance.save()
						tm=4
					else:
						print("failed")
				return redirect('Teacher:Grd9_ClsA_Subj_files_view_all_std',Subj=Subj)
				
			else:Grd9_ClsA_math_assesment_createview_all_std
				form=Grade9ScienceFilesForm()
	if Subj=='Social Science':
		
		for i in class_teacher:
			print(i)
			if request.method=='POST':

				form=Grade9SocialScienceFilesForm(request.POST, request.FILES)
				if form.is_valid():
					print(request.POST.get('Term'))
					instance=form.save(commit=False)
					instance.Teacher_user_Name=i
					if request.POST.get('assesment_type')=='Assignment':
						instance.Maths_is_Assignement=True
					if request.POST.get('assesment_type')=='Test':
						instance.Maths_is_Test=True
					if request.POST.get('Term')=='Term1_assesment':
						instance.Term1_assesment=True
						instance.save()
						tm=1
					elif request.POST.get('Term')=='Term2_assesment':
						instance.Term2_assesment=True
						instance.save()
						tm=2
					elif request.POST.get('Term')=='Term3_assesment':
						instance.Term3_assesment=True
						instance.save()
						tm=3
					elif request.POST.get('Term')=='Term4_assesment':
						instance.Term4_assesment=True
						instance.save()
						tm=4
					else:
						print("failed")
				return redirect('Teacher:Grd9_ClsA_Subj_files_view_all_std',Subj=Subj)
				
			else:
				form=Grade9SocialScienceFilesForm()
	if Subj=='Perosnal Development':
		
		for i in class_teacher:
			print(i)
			if request.method=='POST':

				form=Grade9PersonalDevFilesForm(request.POST, request.FILES)
				if form.is_valid():
					print(request.POST.get('Term'))
					instance=form.save(commit=False)
					instance.Teacher_user_Name=i
					if request.POST.get('assesment_type')=='Assignment':
						instance.Maths_is_Assignement=True
					if request.POST.get('assesment_type')=='Test':
						instance.Maths_is_Test=True
					if request.POST.get('Term')=='Term1_assesment':
						instance.Term1_assesment=True
						instance.save()
						tm=1
					elif request.POST.get('Term')=='Term2_assesment':
						instance.Term2_assesment=True
						instance.save()
						tm=2
					elif request.POST.get('Term')=='Term3_assesment':
						instance.Term3_assesment=True
						instance.save()
						tm=3
					elif request.POST.get('Term')=='Term4_assesment':
						instance.Term4_assesment=True
						instance.save()
						tm=4
					else:
						print("failed")
				return redirect('Teacher:Grd9_ClsA_Subj_files_view_all_std',Subj=Subj)
				
			else:
				form=Grade9PersonalDevFilesForm()


	context={'form':form, 'teachers':class_teacher,'Subj':Subj}
	class_teacher_subj_checker(request,context)
	class_teacher_checker(request,context)
	return render(request, 'Grade9Teach/Grade9_Student_subj_templates/Grade_9_Math_subj_view.html', context)

def Grd9_ClsA_math_assesment_createview_all_std(request,Subj):
	class_teacher=Grade_9_Teacher_Class.objects.filter(id=request.user.id)
	all_students = []
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classA_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classA=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classB_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classB=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classC_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classC=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classD_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classD=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classE_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classE=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classF_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classF=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classG_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classG=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classH_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classH=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classI_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classI=True)
		cord(std,all_students)
	if Grade_9_Teacher_Class.objects.filter(id=request.user.id,is_grd9_classJ_teacher=True):
		std=Grade_9_Student.objects.filter(is_Grade_9_student_classJ=True)
		cord(std,all_students)

	if Subj=='Math':
		
		for i in all_students:
			print(i)
		if request.method=='POST':

			for i in all_students:
				form=Grade_9_models_math_assesment_Form(request.POST, request.FILES)
				if form.is_valid():
					print(request.POST.get('Term'))
					instance=form.save(commit=False)
					instance.user_Name=Grade_9_Student.objects.get(id=i.id)
					if request.POST.get('assesment_type')=='Assignment':
						instance.Maths_is_Assignement=True
					if request.POST.get('assesment_type')=='Test':
						instance.Maths_is_Test=True
					if request.POST.get('Term')=='Term1_assesment':
						instance.Term1_assesment=True
						instance.save()
						tm=1
					elif request.POST.get('Term')=='Term2_assesment':
						instance.Term2_assesment=True
						instance.save()
						tm=2
					elif request.POST.get('Term')=='Term3_assesment':
						instance.Term3_assesment=True
						instance.save()
						tm=3
					elif request.POST.get('Term')=='Term4_assesment':
						instance.Term4_assesment=True
						instance.save()
						tm=4
					else:
						print("failed")
			return redirect('Teacher:View_Uploaded_assesment_Term1',tm=tm)
			
		else:
			form=Grade_9_models_math_assesment_Form()
	if Subj=='English':
		
		for i in all_students:
			print(i)
		if request.method=='POST': 

			for i in all_students:
				form=Grade_9_models_LanguageLiterature_assesment_Form(request.POST, request.FILES)
				if form.is_valid():
					print(request.POST.get('Term'))
					instance=form.save(commit=False)
					instance.user_Name=Grade_9_Student.objects.get(id=i.id)
					if request.POST.get('assesment_type')=='Assignment':
						instance.Maths_is_Assignement=True
					if request.POST.get('assesment_type')=='Test':
						instance.Maths_is_Test=True
					if request.POST.get('Term')=='Term1_assesment':
						instance.Term1_assesment=True
						instance.save()
						tm=1
						return redirect('Teacher:View_Uploaded_assesment_Term1',tm=tm)
					elif request.POST.get('Term')=='Term2_assesment':
						instance.Term2_assesment=True
						instance.save()
						tm=2
						return redirect('Teacher:View_Uploaded_assesment_Term1',tm=tm)
					elif request.POST.get('Term')=='Term3_assesment':
						instance.Term3_assesment=True
						instance.save()
						tm=3
						return redirect('Teacher:View_Uploaded_assesment_Term1',tm=tm)
					elif request.POST.get('Term')=='Term4_assesment':
						instance.Term4_assesment=True
						instance.save()
						tm=4
						return redirect('Teacher:View_Uploaded_assesment_Term1',tm=tm)
					else:
						print("failed")
			
			
		else:
			form=Grade_9_models_LanguageLiterature_assesment_Form()
	if Subj=='Science':
		
		for i in std:
			print(i)
		if request.method=='POST':

			for i in std:
				form=Grade_9_models_Science_assesment_Form(request.POST, request.FILES)
				if form.is_valid():
					print(request.POST.get('Term'))
					instance=form.save(commit=False)
					instance.user_Name=Grade_9_Student.objects.get(id=i.id)
					if request.POST.get('assesment_type')=='Assignment':
						instance.Maths_is_Assignement=True
					if request.POST.get('assesment_type')=='Test':
						instance.Maths_is_Test=True
					if request.POST.get('Term')=='Term1_assesment':
						instance.Term1_assesment=True
						instance.save()
						tm=1
					elif request.POST.get('Term')=='Term2_assesment':
						instance.Term2_assesment=True
						instance.save()
						tm=2
					elif request.POST.get('Term')=='Term3_assesment':
						instance.Term3_assesment=True
						instance.save()
						tm=3
					elif request.POST.get('Term')=='Term4_assesment':
						instance.Term4_assesment=True
						instance.save()
						tm=4
					else:
						print("failed")
			return redirect('Teacher:View_Uploaded_assesment_Term1',tm=tm)
			
		else:
			form=Grade_9_models_Science_assesment_Form()
	if Subj=='Social Science':
		
		for i in std:
			print(i)
		if request.method=='POST':

			for i in std:
				form=Grade_9_models_SocialScience_assesment_Form(request.POST, request.FILES)
				if form.is_valid():
					print(request.POST.get('Term'))
					instance=form.save(commit=False)
					instance.user_Name=Grade_9_Student.objects.get(id=i.id)
					if request.POST.get('assesment_type')=='Assignment':
						instance.Maths_is_Assignement=True
					if request.POST.get('assesment_type')=='Test':
						instance.Maths_is_Test=True
					if request.POST.get('Term')=='Term1_assesment':
						instance.Term1_assesment=True
						instance.save()
						tm=1
					elif request.POST.get('Term')=='Term2_assesment':
						instance.Term2_assesment=True
						instance.save()
						tm=2
					elif request.POST.get('Term')=='Term3_assesment':
						instance.Term3_assesment=True
						instance.save()
						tm=3
					elif request.POST.get('Term')=='Term4_assesment':
						instance.Term4_assesment=True
						instance.save()
						tm=4
					else:
						print("failed")
			return redirect('Teacher:View_Uploaded_assesment_Term1',tm=tm)
			
		else:
			form=Grade_9_models_SocialScience_assesment_Form()
	if Subj=='Perosnal Development':
		
		for i in std:
			print(i)
		if request.method=='POST':

			for i in std:
				form=Grade_9_models_PersonalDev_assesment_Form(request.POST, request.FILES)
				if form.is_valid():
					print(request.POST.get('Term'))
					instance=form.save(commit=False)
					instance.user_Name=Grade_9_Student.objects.get(id=i.id)
					if request.POST.get('assesment_type')=='Assignment':
						instance.Maths_is_Assignement=True
					if request.POST.get('assesment_type')=='Test':
						instance.Maths_is_Test=True
					if request.POST.get('Term')=='Term1_assesment':
						instance.Term1_assesment=True
						instance.save()
						tm=1
					elif request.POST.get('Term')=='Term2_assesment':
						instance.Term2_assesment=True
						instance.save()
						tm=2
					elif request.POST.get('Term')=='Term3_assesment':
						instance.Term3_assesment=True
						instance.save()
						tm=3
					elif request.POST.get('Term')=='Term4_assesment':
						instance.Term4_assesment=True
						instance.save()
						tm=4
					else:
						print("failed")
			return redirect('Teacher:View_Uploaded_assesment_Term1',tm=tm)
			
		else:
			form=Grade_9_models_PersonalDev_assesment_Form()



	context={'form':form, 'teachers':class_teacher}
	class_teacher_subj_checker(request,context)

	return render(request, 'Grade9Teach/Grade9_Student_subj_templates/Grade_9_Math_subj_view.html', context)
