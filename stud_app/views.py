from django.shortcuts import render,HttpResponse
from django.urls import reverse_lazy


from django.views.generic import ListView, CreateView, UpdateView, DeleteView,DetailView
from stud_app.models import Student_Data
# Create your views here.


class StudentView(ListView):
    model = Student_Data


class StudentDetailView(DetailView):
    model = Student_Data
    queryset = Student_Data.objects.all()


# application_name/Student_data_list.html
# object_list



    # def get_queryset(self):
    #
    #     return Student_Data.objects.filter(name="SATISH SONAWALE").all()




class StudentCreate(CreateView):
    model = Student_Data

    fields = ['name','roll_no']
    success_url = reverse_lazy("satish")


class StudentUpdate(UpdateView):
    model = Student_Data

    fields = ['name','roll_no']

    success_url = reverse_lazy("student-list")


class StudentDelete(DeleteView):
    model = Student_Data
    success_url = reverse_lazy("student-list")




def welcome(request):

    return HttpResponse("Hello")




