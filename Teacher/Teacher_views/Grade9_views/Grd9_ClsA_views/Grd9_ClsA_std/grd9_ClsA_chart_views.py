from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from Student.student_views.Grade9_std_views.Grade9_models import (Grade_9_student_classA, Grade_9_student_classB, 
                           Grade_9_student_classC, Grade_9_Student, Grade_9_Student)

from chartit import DataPool, Chart, PivotDataPool, PivotChart
from django.db.models import Avg, Sum, Count, Min, Max, F
#This python file handls all the codes views
from Teacher.Teacher_views.Grade9_views.Grd9_teacher_models import Grade_9_teacher_classA
#Term 1 
#maths assesments models
from Teacher.Teacher_views.Grade9_views.Grd9_assesment_models import (Grade_9_models_math_Term1_assesment_1, Grade_9_models_math_Term2_assesment_2, Grade_9_models_math_Term3_assesment_3, Grade_9_models_math_Term4_assesment_4)
#English assesment models
from Teacher.Teacher_views.Grade9_views.Grd9_assesment_models import (
Grade_9_models_English_Term1_assesment_1,
Grade_9_models_English_Term2_assesment_2,
Grade_9_models_English_Term3_assesment_3,
Grade_9_models_English_Term4_assesment_4
)


def Grade_9ClsA_all_std_marks(request, pk):
    class_teacher=Grade_9_teacher_classA.objects.all()
   
    all_students = Grade_9_student_classA.objects.filter(id=pk)
    all_sub_mrks =  DataPool(
      series=
      [{'options': {
            #    'source': SalesReport.objects.all()},
      'source': all_students},
            #'source': SalesReport.objects.filter(sales__lte=10.00)},
      'terms': [{'full_name': 'full_name', 'English_score_sum': 'English_score_sum', 'Math_score_sum':'Math_score_sum', 'Science_score_sum':'Science_score_sum', 'PersonalDevelopment_score_sum':'PersonalDevelopment_score_sum', 'SocialScience_score_sum':'SocialScience_score_sum'}]
      },
             ])
    all_mrks=Chart(
      datasource=all_sub_mrks,
      series_options=
      [{'options':{
        'type': 'column',
        'stacking':False},
        'terms':{
          'full_name':['English_score_sum', 'Math_score_sum','Science_score_sum', 'PersonalDevelopment_score_sum', 'SocialScience_score_sum']
        }}],
    chart_options =
              {'title': {
                   'text': 'Total marks sum'},
               'xAxis': {
                   'title':{'text': 'Students name'}},
               'yAxis': {
                   'title': {'text': 'Marks'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},


                  # x_sortf_mapf_mts=(None, monthname, False)
                  )
    Test1_all_mrks =  DataPool(
      series=
      [{'options': {
            #    'source': SalesReport.objects.all()},
      'source': Grade_9_student_classA.objects.filter(id=pk)},
            #'source': SalesReport.objects.filter(sales__lte=10.00)},
      'terms': [{'full_name': 'full_name', 'English_score1': 'English_score1', 'Math_score1':'Math_score1', 'Science_score1':'Science_score1', 'Personal Development_score1':'PersonalDevelopment_score1', 'Social Science_score1':'SocialScience_score1'}]
      },
             ])
   
    Test1=Chart(
      datasource=Test1_all_mrks,
      series_options=
      [{'options':{
        'type': 'column',
        'stacking':False},
        'terms':{
          'full_name':['English_score1', 'Math_score1','Science_score1', 'Personal Development_score1', 'Social Science_score1']
        }}],
    chart_options =
              {'title': {
                   'text': 'Students Test1 score'},
               'xAxis': {
                   'title':{'text': 'Students name'}},
               'yAxis': {
                   'title': {'text': 'Marks'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},


                  # x_sortf_mapf_mts=(None, monthname, False)
                  )
    Test2_all_mrks =  DataPool(
      series=
      [{'options': {
            #    'source': SalesReport.objects.all()},
      'source': Grade_9_student_classA.objects.filter(id=pk)},
            #'source': SalesReport.objects.filter(sales__lte=10.00)},
      'terms': [{'full_name': 'full_name', 'English_score2': 'English_score2', 'Math_score2':'Math_score2', 'Science_score2':'Science_score2', 'Personal Development_score2':'PersonalDevelopment_score2', 'Social Science_score2':'SocialScience_score2'}]
      },
             ])
   
    Test2=Chart(
      datasource=Test2_all_mrks,
      series_options=
      [{'options':{
        'type': 'column',
        'stacking':False},
        'terms':{
          'full_name':['English_score2', 'Math_score2','Science_score2', 'Personal Development_score2', 'Social Science_score2']
        }}],
    chart_options =
              {'title': {
                   'text': 'Students Test2 score'},
               'xAxis': {
                   'title':{'text': 'Students name'}},
               'yAxis': {
                   'title': {'text': 'Marks'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},


                  # x_sortf_mapf_mts=(None, monthname, False)
                  )
    Test3_all_mrks =  DataPool(
      series=
      [{'options': {
            #    'source': SalesReport.objects.all()},
      'source': Grade_9_student_classA.objects.filter(id=pk)},
            #'source': SalesReport.objects.filter(sales__lte=10.00)},
      'terms': [{'full_name': 'full_name', 'English_score3': 'English_score3', 'Math_score3':'Math_score3', 'Science_score3':'Science_score3', 'Personal Development_score3':'PersonalDevelopment_score3', 'Social Science_score3':'SocialScience_score3'}]
      },
             ])
   
    Test3=Chart(
      datasource=Test3_all_mrks,
      series_options=
      [{'options':{
        'type': 'column',
        'stacking':False},
        'terms':{
          'full_name':['English_score3', 'Math_score3','Science_score3', 'Personal Development_score3', 'Social Science_score3']
        }}],
    chart_options =
              {'title': {
                   'text': 'Students Test3 score'},
               'xAxis': {
                   'title':{'text': 'Students name'}},
               'yAxis': {
                   'title': {'text': 'Marks'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},


                  # x_sortf_mapf_mts=(None, monthname, False)
                  )

    return render(request, 'Grade9Teach/Tgrd9A/view_std_chart _marks/view_all_Grd9_student_marks.html', {'chart_list':[Test1, all_mrks,Test2,Test3], 'teachers':class_teacher})

def Grade_9ClsA_all_std_marks_2(request):
    class_teacher=Grade_9_teacher_classA.objects.all()
    all_students = Grade_9_Student.objects.filter(is_Grade_9_student_classA=True)
    all_sub_mrks =  DataPool(
      series=
      [{'options': {
            #    'source': SalesReport.objects.all()},
      'source': all_students},
            #'source': SalesReport.objects.filter(sales__lte=10.00)},
      'terms': [{'full_name': 'full_name', 'English_score_sum': 'English_score_sum', 'Math_score_sum':'Math_score_sum', 'Science_score_sum':'Science_score_sum', 'PersonalDevelopment_score_sum':'PersonalDevelopment_score_sum', 'SocialScience_score_sum':'SocialScience_score_sum'}]
      },
             ])
    all_mrks=Chart(
      datasource=all_sub_mrks,
      series_options=
      [{'options':{
        'type': 'column',
        'stacking':False},
        'terms':{
          'full_name':['English_score_sum', 'Math_score_sum','Science_score_sum', 'PersonalDevelopment_score_sum', 'SocialScience_score_sum']
        }}],
    chart_options =
              {'title': {
                   'text': 'Total marks sum'},
               'xAxis': {
                   'title':{'text': 'Students name'}},
               'yAxis': {
                   'title': {'text': 'Marks'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},


                  # x_sortf_mapf_mts=(None, monthname, False)
                  )
    Test1_all_mrks =  DataPool(
      series=
      [{'options': {
            #    'source': SalesReport.objects.all()},
      'source': Grade_9_Student.objects.filter(is_Grade_9_student_classA=True)},
            #'source': SalesReport.objects.filter(sales__lte=10.00)},
      'terms': [{'full_name': 'full_name', 'English_score1': 'English_score1', 'Math_score1':'Math_score1', 'Science_score1':'Science_score1', 'Personal Development_score1':'PersonalDevelopment_score1', 'Social Science_score1':'SocialScience_score1'}]
      },
             ])
   
    Test1=Chart(
      datasource=Test1_all_mrks,
      series_options=
      [{'options':{
        'type': 'column',
        'stacking':False},
        'terms':{
          'full_name':['English_score1', 'Math_score1','Science_score1', 'Personal Development_score1', 'Social Science_score1']
        }}],
    chart_options =
              {'title': {
                   'text': 'Students Test1 score'},
               'xAxis': {
                   'title':{'text': 'Students name'}},
               'yAxis': {
                   'title': {'text': 'Marks'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},


                  # x_sortf_mapf_mts=(None, monthname, False)
                  )
    Test2_all_mrks =  DataPool(
      series=
      [{'options': {
            #    'source': SalesReport.objects.all()},
      'source': Grade_9_Student.objects.filter(is_Grade_9_student_classA=True)},
            #'source': SalesReport.objects.filter(sales__lte=10.00)},
      'terms': [{'full_name': 'full_name', 'English_score2': 'English_score2', 'Math_score2':'Math_score2', 'Science_score2':'Science_score2', 'Personal Development_score2':'PersonalDevelopment_score2', 'Social Science_score2':'SocialScience_score2'}]
      },
             ])
   
    Test2=Chart(
      datasource=Test2_all_mrks,
      series_options=
      [{'options':{
        'type': 'column',
        'stacking':False},
        'terms':{
          'full_name':['English_score2', 'Math_score2','Science_score2', 'Personal Development_score2', 'Social Science_score2']
        }}],
    chart_options =
              {'title': {
                   'text': 'Students Test2 score'},
               'xAxis': {
                   'title':{'text': 'Students name'}},
               'yAxis': {
                   'title': {'text': 'Marks'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},


                  # x_sortf_mapf_mts=(None, monthname, False)
                  )
    Test3_all_mrks =  DataPool(
      series=
      [{'options': {
            #    'source': SalesReport.objects.all()},
      'source':Grade_9_Student.objects.filter(is_Grade_9_student_classA=True)},
            #'source': SalesReport.objects.filter(sales__lte=10.00)},
      'terms': [{'full_name': 'full_name', 'English_score3': 'English_score3', 'Math_score3':'Math_score3', 'Science_score3':'Science_score3', 'Personal Development_score3':'PersonalDevelopment_score3', 'Social Science_score3':'SocialScience_score3'}]
      },
             ])
   
    Test3=Chart(
      datasource=Test3_all_mrks,
      series_options=
      [{'options':{
        'type': 'column',
        'stacking':False},
        'terms':{
          'full_name':['English_score3', 'Math_score3','Science_score3', 'Personal Development_score3', 'Social Science_score3']
        }}],
    chart_options =
              {'title': {
                   'text': 'Students Test3 score'},
               'xAxis': {
                   'title':{'text': 'Students name'}},
               'yAxis': {
                   'title': {'text': 'Marks'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},


                  # x_sortf_mapf_mts=(None, monthname, False)
                  )

    return render(request, 'Grade9Teach/Tgrd9A/view_std_chart _marks/view_all_Grd9_student_marks.html', {'chart_list':[Test1, all_mrks,Test2,Test3], 'teachers':class_teacher})




def Grade_9ClsA_students_English_view(request, pk):
    id_students = Account.objects.filter(id=pk)
    students=Grade_9_student_classA.objects.filter(id=pk)
    class_teacher=Grade_9_teacher_classA.objects.all()

    queryset = Grade_9_models_English_Term1_assesment_1.objects.filter(user_Name__in=id_students)
    sales =  DataPool(
		series=
			[{'options': {

            #    'source': SalesReport.objects.all()},
            'source': queryset},
            #'source': SalesReport.objects.filter(sales__lte=10.00)},
                #'terms': [{'full_name': 'full_name', 'English_score1': 'English_score1', 'English_score2': 'English_score2', 'English_score3': 'English_score3'}]
                #'terms':[{'user_Name','T1_A1_Maths_Title', 'T1_A1_Maths_Desc', 'T1_A1_Maths_is_Test', 'T1_A1_Maths_Marks', 'T1_A1_Maths_OutOfMarks', 'T1_A1_Maths_DatePosted'}]
                'terms':[{'user_Name': 'user_Name','T1_A1_English_Marks': 'T1_A1_English_Marks'}]
                },


             ])
    cht = Chart(
			datasource = sales,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{'user_Name': ['T1_A1_English_Marks']}
                  }],
            chart_options =
              {'title': {
                   'text': 'English'},
               'xAxis': {
                   'title':{'text': 'Students name'}},
               'yAxis': {
                   'title': {'text': 'Marks'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},


                  # x_sortf_mapf_mts=(None, monthname, False)
                  )
    return render(request, 'Grade9Teach/Tgrd9A/view_std_chart _marks/Grade_9std_chart_marks.html', {'chart_list':[cht], 'students':students, 'teachers':class_teacher})

def Grade_9ClsA_students_Math_view(request, pk):
    id_students = Account.objects.filter(id=pk)
    students=Grade_9_student_classA.objects.filter(id=pk)
    queryset = Grade_9_models_math_Term1_assesment_1.objects.filter(user_Name__in=id_students)
    sales =  DataPool(
		series=
			[{'options': {
            #    'source': SalesReport.objects.all()},
            'source': queryset},
            #'source': SalesReport.objects.filter(sales__lte=10.00)},
                'terms':[{'user_Name':'user_Name','T1_A1_Maths_Marks':'T1_A1_Maths_Marks'}]
                },


             ])
    cht = Chart(
			datasource = sales,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{'user_Name': ['T1_A1_Maths_Marks']}
                  }],
            chart_options =
              {'title': {
                   'text': 'Math'},
               'xAxis': {
                   'title':{'text': 'Students name'}},
               'yAxis': {
                   'title': {'text': 'Marks'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},


                  # x_sortf_mapf_mts=(None, monthname, False)
                  )
    
    return render(request, 'Grade9Teach/Tgrd9A/view_std_chart _marks/Grade_9std_chart_marks.html', {'chart_list':[cht], 'students':students , 'teachers':class_teacher})
def Grade_9ClsA_students_Math_view(request, pk):

    class_teacher=Grade_9_teacher_classA.objects.all()
    students=Grade_9_student_classA.objects.filter(id=pk)
    queryset = Grade_9_student_classA.objects.filter(id=pk)
    sales =  DataPool(
		series=
			[{'options': {
            #    'source': SalesReport.objects.all()},
            'source': students},
            #'source': SalesReport.objects.filter(sales__lte=10.00)},
                'terms': [{'username': 'username', 'Math_score1': 'Math_score1', 'Math_score2': 'Math_score2', 'Math_score3': 'Math_score3'}]
                },


             ])
    cht = Chart(
			datasource = sales,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{'username': ['Math_score1', 'Math_score2', 'Math_score3']}
                  }],
            chart_options =
              {'title': {
                   'text': 'Math'},
               'xAxis': {
                   'title':{'text': 'Students name'}},
               'yAxis': {
                   'title': {'text': 'Marks'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},


                  # x_sortf_mapf_mts=(None, monthname, False)
                  )
    
    return render(request, 'Grade9Teach/Tgrd9A/view_std_chart _marks/Grade_9std_chart_marks.html', {'chart_list':[cht], 'students':students , 'teachers':class_teacher})
def Grade_9ClsA_students_Science_view(request, pk):
    class_teacher=Grade_9_teacher_classA.objects.all()
    students=Grade_9_student_classA.objects.filter(id=pk)
    queryset = Grade_9_student_classA.objects.filter(id=pk)
    sales =  DataPool(
		series=
			[{'options': {
            #    'source': SalesReport.objects.all()},
            'source': students},
            #'source': SalesReport.objects.filter(sales__lte=10.00)},
                'terms': [{'username': 'username', 'Science_score1': 'Science_score1', 'Science_score2': 'Science_score2', 'Science_score3': 'Science_score3'}]
                },


             ])
    cht = Chart(
			datasource = sales,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{'username': ['Science_score1', 'Science_score2', 'Science_score3']}
                  }],
            chart_options =
              {'title': {
                   'text': 'Science'},
               'xAxis': {
                   'title':{'text': 'Students name'}},
               'yAxis': {
                   'title': {'text': 'Marks'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},


                  # x_sortf_mapf_mts=(None, monthname, False)
                  )
    
    return render(request, 'Grade9Teach/Tgrd9A/view_std_chart _marks/Grade_9std_chart_marks.html', {'chart_list':[cht], 'students':students , 'teachers':class_teacher})
def Grade_9ClsA_students_Science_view(request, pk):
    class_teacher=Grade_9_teacher_classA.objects.all()
    students=Grade_9_student_classA.objects.filter(id=pk)
    queryset = Grade_9_student_classA.objects.filter(id=pk)
    sales =  DataPool(
		series=
			[{'options': {
            #    'source': SalesReport.objects.all()},
            'source': students},
            #'source': SalesReport.objects.filter(sales__lte=10.00)},
                'terms': [{'username': 'username', 'Science_score1': 'Science_score1', 'Science_score2': 'Science_score2', 'Science_score3': 'Science_score3'}]
                },


             ])
    cht = Chart(
			datasource = sales,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{'username': ['Science_score1', 'Science_score2', 'Science_score3']}
                  }],
            chart_options =
              {'title': {
                   'text': 'Science'},
               'xAxis': {
                   'title':{'text': 'Students name'}},
               'yAxis': {
                   'title': {'text': 'Marks'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},


                  # x_sortf_mapf_mts=(None, monthname, False)
                  )
    
    return render(request, 'Grade9Teach/Tgrd9A/view_std_chart _marks/Grade_9std_chart_marks.html', {'chart_list':[cht], 'students':students , 'teachers':class_teacher})
def Grade_9ClsA_students_SocialScience_view(request, pk):
    class_teacher=Grade_9_teacher_classA.objects.all()
    students=Grade_9_student_classA.objects.filter(id=pk)
    queryset = Grade_9_student_classA.objects.filter(id=pk)
    sales =  DataPool(
		series=
			[{'options': {
            #    'source': SalesReport.objects.all()},
            'source': students},
            #'source': SalesReport.objects.filter(sales__lte=10.00)},
                'terms': [{'username': 'username', 'SocialScience_score1': 'SocialScience_score1', 'SocialScience_score2': 'SocialScience_score2', 'SocialScience_score3': 'SocialScience_score3'}]
                },


             ])
    cht = Chart(
			datasource = sales,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{'username': ['SocialScience_score1', 'SocialScience_score2', 'SocialScience_score3']}
                  }],
            chart_options =
              {'title': {
                   'text': 'Soscial science'},
               'xAxis': {
                   'title':{'text': 'Students name'}},
               'yAxis': {
                   'title': {'text': 'Marks'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},


                  # x_sortf_mapf_mts=(None, monthname, False)
                  )
    
    return render(request, 'Grade9Teach/Tgrd9A/view_std_chart _marks/Grade_9std_chart_marks.html', {'chart_list':[cht], 'students':students , 'teachers':class_teacher})
def Grade_9ClsA_students_PersonalDevelopment_view(request, pk):
    class_teacher=Grade_9_teacher_classA.objects.all()
    students=Grade_9_student_classA.objects.filter(id=pk)
    queryset = Grade_9_student_classA.objects.filter(id=pk)
    sales =  DataPool(
		series=
			[{'options': {
            #    'source': SalesReport.objects.all()},
            'source': students},
            #'source': SalesReport.objects.filter(sales__lte=10.00)},
                'terms': [{'username': 'username', 'PersonalDevelopment_score1': 'PersonalDevelopment_score1', 'PersonalDevelopment_score2': 'PersonalDevelopment_score2', 'PersonalDevelopment_score3': 'PersonalDevelopment_score3'}]
                },


             ])
    cht = Chart(
			datasource = sales,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{'username': ['PersonalDevelopment_score1', 'PersonalDevelopment_score2', 'PersonalDevelopment_score3']}
                  }],
            chart_options =
              {'title': {
                   'text': 'Personal Development'},
               'xAxis': {
                   'title':{'text': 'Students name'}},
               'yAxis': {
                   'title': {'text': 'Marks'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},


                  # x_sortf_mapf_mts=(None, monthname, False)
                  )
    
    return render(request, 'Grade9Teach/Tgrd9A/view_std_chart _marks/Grade_9std_chart_marks.html', {'chart_list':[cht], 'students':students , 'teachers':class_teacher})
def Grade_9ClsA_students_English_view1(request, pk):
    class_teacher=Grade_9_teacher_classA.objects.all()
    students=Grade_9_student_classA.objects.filter(id=pk)
    queryset = Grade_9_student_classA.objects.filter(id=pk)
    ds = PivotDataPool(
		series=[
		{'options': {
          'source': Grade_6_student_classA.objects.filter(id=pk),
          'categories': ['English_score1', 'English_score2', 'English_score3'],
          },
        'terms': {
          'total_English_score':Sum('English_score_sum'),
          'total_Math_score':Sum('Math_score_sum'),
          'total_Science_score':Sum('Science_score_sum'),
          'total_Social_Science_score':Sum('SocialScience_score_sum'),
          'total_Personal_development_score':Sum('PersonalDevelopment_score_sum'),
          },
       }])
    cht = PivotChart(
          datasource=ds,
          series_options=[
            {'options': {
               'type': 'column'
               },
             'terms': ['total_English_score','total_Math_score','total_Science_score','total_Social_Science_score','total_Personal_development_score'],
            }],
            chart_options =
				{'title': {
					'text': 'Student marks'},
						'xAxis': {
							'title':{'text': 'Subjects'}},
						'yAxis': {
							'title': {'text': 'Marks scored'}},
						'legend': {
							'enabled': True},
						'credits': {
							'enabled': True}},

					)
    return render(request, 'Grade9Teach/Tgrd9A/view_std_chart _marks/Grade_9std_chart_marks.html', {'chart_list':[cht], 'students':students , 'teachers':class_teacher})
def Grade_9ClsA_students_view_chart_markss(request, pk):
    class_teacher=Grade_9_teacher_classA.objects.all()
    students=Grade_9_student_classA.objects.filter(id=pk)
    queryset = Grade_9_student_classA.objects.filter(id=pk)
	
    ds = PivotDataPool(
		series=[
		{'options': {
          'source': Grade_9_student_classA.objects.filter(id=pk),
          'categories': ['English_score_sum', 'Math_score_sum', 'Science_score_sum', 'SocialScience_score_sum', 'PersonalDevelopment_score_sum'],
          },
        'terms': {
          'total_English_score':Sum('English_score_sum'),
          'total_Math_score':Sum('Math_score_sum'),
          'total_Science_score':Sum('Science_score_sum'),
          'total_Social_Science_score':Sum('SocialScience_score_sum'),
          'total_Personal_development_score':Sum('PersonalDevelopment_score_sum'),
          },
       }])
    cht = PivotChart(
          datasource=ds,
          series_options=[
            {'options': {
               'type': 'column'
               },
             'terms': ['total_English_score','total_Math_score','total_Science_score','total_Social_Science_score','total_Personal_development_score'],
            }],
            chart_options =
				{'title': {
					'text': 'Student marks'},
						'xAxis': {
							'title':{'text': 'Subjects'}},
						'yAxis': {
							'title': {'text': 'Marks scored'}},
						'legend': {
							'enabled': True},
						'credits': {
							'enabled': True}},

					)
    return render(request, 'Grade9Teach/Tgrd9A/view_std_chart _marks/Grade_9std_chart_marks.html', {'chart_list':[cht], 'students':students , 'teachers':class_teacher})

"""
def Grade_6_students_view_chart_markss(request, pk):
	students=Grade_6_student_classA.objects.filter(id=pk)
	#context={'students':students}
	queryset = Grade_6_student_classA.objects.filter(id=pk)
	def total_english_marks():
		Total_English_score=Grade_6_student_classA.objects.values_list('English_score1').get(id=pk)+Grade_6_student_classA.objects.values_list('English_score2').get(id=pk)+Grade_6_student_classA.objects.values_list('English_score3').get(id=pk)
		return Total_English_score[num]
	sales =  PivotDataPool(
			series=[
       {'options': {
          'source': Grade_6_student_classA.objects.filter(id=pk),
          'categories': 'English_score1',
          },
            #'source': SalesReport.objects.filter(sales__lte=10.00)},
			#'terms': [ 'English_name', {'English_name':'English_name'}]
			'terms':[{'total English score':Sum('English_score1'),}, 'Main_score']
			},
			])

	def monthname(month_num):
		names = {1: Grade_6_student_classA.objects.values_list('username').get(id=pk)}#, 2:  Grade_6_student_classB.objects.values_list('username').get(id=pk), 3: 'Classroom C', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
		return names[month_num]
	cht=PivotChart(
			datasource=sales,
			series_options=
			[{'options':{
				'type': 'column',
				'stacking':False},
				'terms':{
					
					'Main_score':['total English score',],
					#, 'Math_score', 'Science_score', 'SocialScience_score', 'PersonalDevelopment_score'],
					
				},
				'terms2':{
					'Math_name1':['total English score',],
				}
				}],


		chart_options =
				{'title': {
					'text': 'Student marks'},
						'xAxis': {
							'title':{'text': 'Subjects'}},
						'yAxis': {
							'title': {'text': 'Marks scored'}},
						'legend': {
							'enabled': True},
						'credits': {
							'enabled': True}},

					)
	return render(request, 'Grade6Teach/Tgrd6A/charts.html', {'chart_list':[cht], 'students':students})
"""