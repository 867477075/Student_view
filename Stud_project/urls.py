"""
URL configuration for Stud_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from stud_app import views,view_2,view_3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/',views.welcome,name="welcome_page"),
    path('student/',views.StudentView.as_view(),name="student-list"),
    path('student/create/',views.StudentCreate.as_view(),name="student-create"),
    path("student/update/<int:pk>", views.StudentUpdate.as_view(), name="student-update"),
    path("student/delete/<int:pk>", views.StudentDelete.as_view(), name="student-delete"),
    path("student/details/<int:pk>", views.StudentDetailView.as_view(), name="student-detail-view"),

    # View_2 Started here

    path("v2/student/", view_2.StudentDetails.as_view(), name="v2-get-student"),

    # view_3 started here
    path("v3/student/", view_3.student_details, name="v3-get-student")



]
