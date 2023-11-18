from django.db import models
from .student_views.Grade9_std_views.Grade9_models import Grade_9_Student
"""
from django.urls import reverse
import uuid
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
class MyAccounsstManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError("email is not pressent")
		if not username:
			raise ValueError("username is not pressent")
		user=self.model(
			email=self.normalize_email(email),
			username=username
			)
		user.set_password(password)
		user.save(using=self._db)
		return user
	def create_superuser(self, email, username, password):
		user=self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username			
			)
		user.is_admin=True
		user.is_staff=True
		user.is_superuser=True
		user.save(using=self._db)
		return user




class Acasdfasfasfcount(AbstractBaseUser):
	#Identification details

	id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	email=models.EmailField(verbose_name="email", max_length=60, unique=True)
	username=models.CharField(max_length=30, unique=True)
	date_joined=models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login=models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin=models.BooleanField(default=False)
	is_active=models.BooleanField(default=True)
	is_staff=models.BooleanField(default=False)
	is_superuser=models.BooleanField(default=False)
	#Code test
	

	
	USERNAME_FIELD='username'
	REQUIRED_FIELDS=['email',]
	def get_absolute_url(self):
		return reverse('headmin:Grade_9_Teacher_list_details', args=[str(self.id)])

	objects=MyAccounsstManager()
	def __str__(self):
		return self.email
	def has_perm(self, perm, obj=None):
		return self.is_admin
	def has_module_perms(self, app_label):
		return True
	def __str__(self):
		return self.username


"""

