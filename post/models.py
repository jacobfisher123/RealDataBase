from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils.text import slugify
from django.urls import reverse
import random 
import string
import uuid
from Headmin.models import Account
from django.forms import ModelForm
from django import forms
class Post(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200,)
    body = models.TextField(max_length = None,)
    date = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(Account, on_delete=models.CASCADE, default=None, max_length=250, blank=True, null=True, related_name='headadmin_post')
    slug = models.SlugField(unique=True, null=True, blank=True)
    Admin_signal=models.BooleanField(default=False)
    Teacher_signal=models.BooleanField(default=False)
    Student=models.BooleanField(default=False)
    student_boolean=models.BooleanField(default=False)

    class Meta:
        ordering = ['title', 'user']

    def get_absolute_url(self):
        if self.request.user.is_student:
            print("==================get_absolute_url ID=STUDENT==================")
            return reverse('Student:Student:post_detail', kwargs={'slug': self.slug})
            
        elif self.request.user.is_teacher:
            print("==================get_absolute_url ID=Teacher==================")
            return reverse('Teacher:Teacher_post_detail', kwargs={'slug': self.slug})

        else:

            return reverse('post-detail', kwargs={'slug': self.slug})
    
    def generate_unique_slug(self):
        slug = slugify(self.title)
        unique_slug=slug
        count=1
        while Post.objects.filter(slug=unique_slug).exists():
            random_chars = "".join(random.choices(string.ascii_lowercase + string.digits, k=4))
            unique_slug = f"{slug}-{random_chars}-{count}"
            count += 1
        return unique_slug

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)
        
    def __Str__(self):
        return self.title


class Comment(models.Model):
    """
    Model representing a comment against a blog post.
    """
    description = models.TextField(max_length=1000, help_text="Enter comment about blog here.")
    author = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='headadmin_comments')
      # Foreign Key used because BlogComment can only have one author/User, but users can have multiple comments
    post_date = models.DateTimeField(auto_now_add=True)
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["post_date"]

    def get_absolute_url(self):
        return reverse('comment-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        len_title=75
        if len(self.description)>len_title:
            titlestring=self.description[:len_title] + '...'
        else:
            titlestring=self.description
        return titlestring


class Reply(models.Model):
    """
    Model representing a comment against a blog post.
    """
    description = models.TextField(max_length=1000, help_text="Enter comment reply!")
    author = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
      # Foreign Key used because BlogComment can only have one author/User, but users can have multiple comments
    post_date = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    class Meta:
        ordering = ["post_date"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        len_title=75
        if len(self.description)>len_title:
            titlestring=self.description[:len_title] + '...'
        else:
            titlestring=self.description
        return titlestring

from django import forms 

class CommentCreationForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['description']

    def clean_description(self):
        description = self.cleaned_data.get('description')
        # Add any additional validation for the description field if needed
        return description
