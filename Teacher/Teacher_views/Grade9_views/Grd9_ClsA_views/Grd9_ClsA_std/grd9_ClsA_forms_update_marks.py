from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import Tab, TabHolder
from crispy_forms.layout import (Layout, Fieldset, Field,
                                 ButtonHolder, Submit, Div)

#split it up


"""
class Grade_9_student_classA_updateMarks_forms(ModelForm):
    class Meta:
        model = Grade_9_student_classA
        fields = [
            #upload one
            'English_name1',
            'English_score1',
            #upload two
            'English_name2',
            'English_score2',
            #upload three
            'English_name3',
            'English_score3',

            #upload one
            'Math_name1',
            'Math_score1',
            #upload two
            'Math_name2',
            'Math_score2',
            #upload three
            'Math_name3',
            'Math_score3',

            #upload one
            'Science_name1',
            'Science_score1',
            #upload two
            'Science_name2',
            'Science_score2',
            #upload three
            'Science_name3',
            'Science_score3',

            #upload one
            'SocialScience_name1',
            'SocialScience_score1',
            #upload two
            'SocialScience_name2',
            'SocialScience_score2',
            #upload three
            'SocialScience_name3',
            'SocialScience_score3',

            #upload one
            'PersonalDevelopment_name1',
            'PersonalDevelopment_score1',
            #upload two
            'PersonalDevelopment_name2',
            'PersonalDevelopment_score2',
            #upload three
            'PersonalDevelopment_name3',
            'PersonalDevelopment_score3',
           
        ]

    def __init__(self, *args, **kwargs):
        super(Grade_9_student_classA_updateMarks_forms, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            TabHolder(
                Tab('English subjects',
                    #upload one
                    'English_name1',
                    'English_score1',
                    #upload two
                    'English_name2',
                    'English_score2',
                    #upload three
                    'English_name3',
                    'English_score3',
                    ),
                Tab('Math subjects',
                    #upload one
                    Field('Math_name1', css_class="extra"),
                    Field('Math_score1',),
                    #upload two
                    Field('Math_name2',),
                    Field('Math_score2',),
                    #upload three
                    Field('Math_name3',),
                    Field('Math_score3',),
                    
           
                    ),
                Tab('Science subjects',
                    #upload one
                    Field('Science_name1', css_class="extra"),
                    Field('Science_score1',),
                    #upload two
                    Field('Science_name2',),
                    Field('Science_score2',),
                    #upload three
                    Field('Science_name3',),
                    Field('Science_score3',),
    
                    ),
                Tab('SocialScience subjects',
                    #upload one
                    Field('SocialScience_name1', css_class="extra"),
                    Field('SocialScience_score1',),
                    #upload two
                    Field('SocialScience_name2',),
                    Field('SocialScience_score2',),
                    #upload three
                    Field('SocialScience_name3',),
                    Field('SocialScience_score3',),
    
                    ),
                Tab('PersonalDevelopment subjects',
                    #upload one
                    Field('PersonalDevelopment_name1', css_class="extra"),
                    Field('PersonalDevelopment_score1',),
                    #upload two
                    Field('PersonalDevelopment_name2',),
                    Field('PersonalDevelopment_score2',),
                    #upload three
                    Field('PersonalDevelopment_name3',),
                    Field('PersonalDevelopment_score3',),
    
                    ),
            ),
            ButtonHolder(
                Submit('submit', 'Update marks',
                       css_class='float-right btn-dark mr-3')
            )
        )
        """