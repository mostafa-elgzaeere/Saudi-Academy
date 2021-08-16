from django.shortcuts import render ,HttpResponseRedirect
from academic.models import Semester ,  Lectuer , Comment , Perfect_student
from django.contrib.auth.decorators import login_required
# Create your views here.

def home_page(request):
    semesters=Semester.objects.all()
    return render(request,'academic/home.html',{"semesters":semesters})


def show_classes(request,semester_number):
    semester=Semester.objects.get(id=semester_number)
    students=Perfect_student.objects.filter(semester=semester)

    return render(request,'academic/classes.html',{"semester":semester,"students":students})

@login_required
def show_lectuer(request,semester_number,lectuer_number):
    lectuer=Lectuer.objects.get(id=lectuer_number,semester__id=semester_number)
    v=lectuer.video

    if request.method == "POST":
        name=request.user
        content=request.POST.get("comment")
        lec=Lectuer.objects.get(id=lectuer_number)
        c=Comment(writer=name,content=content,lectuer=lec)
        c.save()
  

    lec=Lectuer.objects.get(id=lectuer_number)
    comments=Comment.objects.filter(lectuer=lec)
    return render(request,'academic/lectuer.html',{"video":v,"lectuer":lectuer,"comments":comments})



