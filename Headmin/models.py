from django.db import models
from django.urls import reverse
import uuid
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.forms import ModelForm
    
from datetime import datetime
from django import forms
 
#from Teacher.Teacher_views.Grade9_views.Grd9_assesment_models import Grade_9_models_math_Term1_assesment_1
class MyAccountManager(BaseUserManager):
    
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError("email is not present")
        if not username:
            raise ValueError("username is not present")
        if not first_name:
            raise ValueError("first_name is not present")
        if not last_name:
            raise ValueError("last_name is not present")
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

JOB_STATUS = [
    ('looking_for_job', 'Actively looking right now'),
    ('open_but_not_looking', 'Open, but not actively looking'),
    ('not_interested_in_jobs', 'Not interested in jobs'),
]


EXPERIENCE_LEVEL = [

    ('Student','Student'),
    ('Junior', 'Junior'),
    ('Mid_Level', 'Mid Level'),
    ('Senior', 'Senior'),
    ('Lead', 'Lead'),
    ('Manager', 'Manager'),

]

JOB_TYPE_CHOICES = [

    ('FULL_TIME', 'Full Time'),
    ('CONTRCT', 'Contract'),
    ('InternShip', 'InternShip'),

]
class Account(AbstractBaseUser):
    # Identification details
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Code test

    # STUDENT BOOLEAN ID CODE
    is_student = models.BooleanField(default=False)

    # Grade 9 student
    is_Grade_9_student = models.BooleanField(default=False)
    is_Grade_9_student_classA = models.BooleanField(default=False, editable=True, verbose_name='Class A')
    is_Grade_9_student_classB = models.BooleanField(default=False, editable=True, verbose_name='Class B')
    is_Grade_9_student_classC = models.BooleanField(default=False, editable=True, verbose_name='Class C')
    is_Grade_9_student_classD = models.BooleanField(default=False, editable=True, verbose_name='Class D')
    is_Grade_9_student_classE = models.BooleanField(default=False, editable=True)
    is_Grade_9_student_classF = models.BooleanField(default=False, editable=True)
    is_Grade_9_student_classG = models.BooleanField(default=False, editable=True)
    is_Grade_9_student_classH = models.BooleanField(default=False, editable=True)
    is_Grade_9_student_classI = models.BooleanField(default=False, editable=True)
    is_Grade_9_student_classJ = models.BooleanField(default=False, editable=True)

    # TEACHER BOOLEAN ID CODE
    is_teacher = models.BooleanField(default=False)
    # Grade 9 teacher LOGIN boolean id code
    is_Grade_9_teacher = models.BooleanField(default=False)
    is_Grade_9_teacher_classA = models.BooleanField(default=False)
    is_Grade_9_teacher_classB = models.BooleanField(default=False)
    is_Grade_9_teacher_classC = models.BooleanField(default=False)
    is_Grade_9_teacher_classD = models.BooleanField(default=False)
    is_Grade_9_teacher_classE = models.BooleanField(default=False)
    is_Grade_9_teacher_classF = models.BooleanField(default=False)
    is_Grade_9_teacher_classG = models.BooleanField(default=False)
    is_Grade_9_teacher_classH = models.BooleanField(default=False)
    is_Grade_9_teacher_classI = models.BooleanField(default=False)
    is_Grade_9_teacher_classJ = models.BooleanField(default=False)

    # full_name = models.CharField(max_length=30, default='', blank=True)
    user_reputation = models.IntegerField(default=0)
    not_to_Display_Full_name = models.CharField(max_length=30, default='', blank=True)
    email = models.EmailField(max_length=30, default='')
    location = models.CharField(max_length=30, default='', blank=True)
    title = models.CharField(max_length=30, default='', blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos', default='media/isle.jpg')
    about_me = models.CharField(max_length=30, default='', blank=True, null=True)
    website_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)
    # bookmark_questions = models.ManyToManyField(Question, related_name='bookmark_questions', blank=True)
    q_edited_counter = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    reputation = models.IntegerField(default=1)
    is_banned = models.BooleanField(default=False)
    post_edit_inactive_for_six_month = models.IntegerField(default=0)
    is_moderator = models.BooleanField(default=False)
    is_high_moderator = models.BooleanField(default=False)
    targeted_tag = models.CharField(max_length=30, default='Commenter')
# BADGES
    review_close_votes = models.BooleanField(default=False)
    favorite_question_S = models.BooleanField(default=False)
    lifeJacket = models.BooleanField(default=False)


    altruist = models.BooleanField(default=False)
# PRIVILEGES
    commenter = models.BooleanField(default=False)


# OTHERS


    logout_on_all_devices = models.BooleanField(default=False)
    send_email_notifications = models.BooleanField(default=False)

    voting_flags = models.IntegerField(default=0)
    helpful_close_votes = models.IntegerField(default=0)
    # profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='account_profile')

# DEVELOPER STORY
    name = models.CharField(max_length=30, default='')
    prefered_technologies = models.CharField(max_length=30, default='')
    min_expierence_level = models.CharField(max_length=30,choices=EXPERIENCE_LEVEL, default='')
    max_expierence_level = models.CharField(max_length=30,choices=EXPERIENCE_LEVEL, default='')
    job_type = models.CharField(max_length=30, choices=JOB_TYPE_CHOICES)
    job_search_status = models.CharField(max_length=30, choices=JOB_STATUS)
    phone_number = models.CharField(max_length=30, blank=True, null=True)


    create_posts = models.BooleanField(default=True) # Done
    create_wiki_posts = models.BooleanField(default=False) # Done
    remove_new_user_restrictions = models.BooleanField(default=False) # Done
    voteUpPriv = models.BooleanField(default=False) # Done
    flag_posts = models.BooleanField(default=False) # Done
    comment_everywhere_Priv = models.BooleanField(default=False) # Done
    set_bounties = models.BooleanField(default=False) # Done
    edit_community_wiki = models.BooleanField(default=False)
    voteDownPriv = models.BooleanField(default=False) # Done
    view_close_votes_Priv = models.BooleanField(default=False)
    access_review_queues = models.BooleanField(default=False)
    established_user_Priv = models.BooleanField(default=False) # Done
    create_tags = models.BooleanField(default=False) # Done
    edit_questions_answers = models.BooleanField(default=False) # Done
    cast_close_AND_Reopen_votes = models.BooleanField(default=False) # Done
    accessTo_moderatorTools = models.BooleanField(default=False)
    protect_questions = models.BooleanField(default=False) # Done
    trusted_user_Priv = models.BooleanField(default=False)

    helpful_flags_counter = models.IntegerField(default=0, blank=True, null=True)
    posts_edited_counter = models.IntegerField(default=0, blank=True, null=True)
    suggested_Edit_counter = models.IntegerField(default=0, blank=True, null=True)
    editPostTimeOfUser = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    Refiner_Illuminator_TagPostCounter = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return f'{self.user}'

    def get_absolute_url(self):
        return reverse('profile:activityPageTabProfile', kwargs={'user_id': self.user_id,'username': self.user.username})

    @property
    def age(self):
        current_datetime = datetime.datetime.now(timezone.utc)
        return (current_datetime - self.time).days
    # profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    def get_absolute_url(self):
        return reverse('headmin:Grade_9_Teacher_list_details', args=[str(self.id)])

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True



class Upcomeing_events(models.Model):
	
	Title=models.CharField(max_length=200)
	Subtitle=models.CharField(max_length=50)
	Desc=models.TextField(max_length=500)
	Due_Date=models.DateTimeField()
	posted_date=models.DateTimeField(verbose_name='posted_date', auto_now_add=True)
	def __str__(self):
		return "{}-{}".format(self.Title, self.posted_date)

	def snippet(self):
		return self.Desc[:40]+"..."

class Post(models.Model):
	id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	userpost=models.ForeignKey(Account, on_delete=models.CASCADE, default=None, max_length=250, blank=True, null=True)
	Admin_signal=models.BooleanField(default=False)
	Teacher_signal=models.BooleanField(default=False)
	Student=models.BooleanField(default=False)
	
	title=models.CharField(max_length=200)
	# Subtitle=models.CharField(max_length=50)
	description=models.TextField(max_length=5000)
	posted_date=models.DateTimeField(verbose_name='posted_date', auto_now_add=True)
	student_boolean=models.BooleanField(default=False)
	def __str__(self):
		return "{}-{}".format(self.title, self.posted_date)

	def snippet(self):
		return self.description[:40]+"..."


class Comment(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    userpost=models.ForeignKey(Account, on_delete=models.CASCADE, default=None, max_length=250, blank=True, null=True)
    comments = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comments']








class Upcomeing_eventss(ModelForm):
	class Meta:
		model=Upcomeing_events
		fields=('Title', 'Subtitle', 'Desc')










def create_event():
    event_data = [
        {
            'Title': 'Event 1',
            'Subtitle': 'Subtitle 1',
            'Desc': 'Description for Event 1. Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'Due_Date': datetime(2023, 9, 30),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 2',
            'Subtitle': 'Subtitle 2',
            'Desc': 'Description for Event 2. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
            'Due_Date': datetime(2023, 10, 15),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 3',
            'Subtitle': 'Subtitle 3',
            'Desc': 'Description for Event 3. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 4',
            'Subtitle': 'Subtitle 4',
            'Desc': 'Description for Event 4. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 5',
            'Subtitle': 'Subtitle 5',
            'Desc': 'Description for Event 5. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 6',
            'Subtitle': 'Subtitle 6',
            'Desc': 'Description for Event 6. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 6',
            'Subtitle': 'Subtitle 6',
            'Desc': 'Description for Event 6. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 7',
            'Subtitle': 'Subtitle 7',
            'Desc': 'Description for Event 7. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 8',
            'Subtitle': 'Subtitle 8',
            'Desc': 'Description for Event 8. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 9',
            'Subtitle': 'Subtitle 9',
            'Desc': 'Description for Event 9. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 10',
            'Subtitle': 'Subtitle 10',
            'Desc': 'Description for Event 10. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 10',
            'Subtitle': 'Subtitle 10',
            'Desc': 'Description for Event 10. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 11',
            'Subtitle': 'Subtitle 11',
            'Desc': 'Description for Event 11. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 12',
            'Subtitle': 'Subtitle 12',
            'Desc': 'Description for Event 12. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },

        {
            'Title': 'Event 13',
            'Subtitle': 'Subtitle 13',
            'Desc': 'Description for Event 13. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 14',
            'Subtitle': 'Subtitle 14',
            'Desc': 'Description for Event 14. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 15',
            'Subtitle': 'Subtitle 15',
            'Desc': 'Description for Event 15. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 16',
            'Subtitle': 'Subtitle 16',
            'Desc': 'Description for Event 16. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 17',
            'Subtitle': 'Subtitle 17',
            'Desc': 'Description for Event 17. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 18',
            'Subtitle': 'Subtitle 18',
            'Desc': 'Description for Event 18. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 19',
            'Subtitle': 'Subtitle 19',
            'Desc': 'Description for Event 19. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 20',
            'Subtitle': 'Subtitle 20',
            'Desc': 'Description for Event 20. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 21',
            'Subtitle': 'Subtitle 21',
            'Desc': 'Description for Event 21. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 22',
            'Subtitle': 'Subtitle 22',
            'Desc': 'Description for Event 22. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 23',
            'Subtitle': 'Subtitle 23',
            'Desc': 'Description for Event 23. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 24',
            'Subtitle': 'Subtitle 24',
            'Desc': 'Description for Event 24. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 25',
            'Subtitle': 'Subtitle 25',
            'Desc': 'Description for Event 25. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 26',
            'Subtitle': 'Subtitle 26',
            'Desc': 'Description for Event 26. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 27',
            'Subtitle': 'Subtitle 27',
            'Desc': 'Description for Event 27. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 28',
            'Subtitle': 'Subtitle 28',
            'Desc': 'Description for Event 28. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 29',
            'Subtitle': 'Subtitle 29',
            'Desc': 'Description for Event 29. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 30',
            'Subtitle': 'Subtitle 30',
            'Desc': 'Description for Event 30. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },
        {
            'Title': 'Event 31',
            'Subtitle': 'Subtitle 31',
            'Desc': 'Description for Event 31. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'Due_Date': datetime(2023, 11, 5),
            'posted_date': datetime.now(),
        },

    ]

    for event_info in event_data:
        Upcomeing_events.objects.create(
            Title=event_info['Title'],
            Subtitle=event_info['Subtitle'],
            Desc=event_info['Desc'],
            Due_Date=event_info['Due_Date'],
            posted_date=event_info['posted_date'],
        )
        print("----------------------------------created----------------------------------")
#now loop through those 2 list and create multiple users
