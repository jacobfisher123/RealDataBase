"""SchoolDatabaseTrial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Headmin.views import homeView
from django.conf import settings
from django.conf.urls.static import static
from Student.views import student_redirector
urlpatterns = [
    path('student_redirector/', student_redirector, name='student_redirector'),
	path('', homeView, name="profile_view"),
    path('account/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('Teacher/', include("Teacher.urls")),
    path('Headmin/', include("Headmin.urls")),
    path('Student/', include("Student.urls")),
    path('martor/', include('martor.urls')),
    path('post/', include('post.urls')),
    
  #   path('', include('profile.urls')),post
    path('', include('qa.urls')),
  #   path('', include('notification.urls')),
  #   path('', include('tagbadge.urls')),
  #   path('', include('help.urls')),
    path('', include('review.urls')),
  #   path('', include('tools.urls')),
  # path('adminactions/', include('adminactions.urls')),
  #   path('martor/', include('martor.urls')),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
