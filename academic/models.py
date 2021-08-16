from django.db.models import *
from django.contrib.auth.models import User

# Create your models here.


class Semester(Model):
    name        = CharField(max_length=40)
    
    def __str__(self):
        return self.name


class Lectuer(Model):
    title       = CharField(max_length=100)
    description = TextField(max_length=300)
    add_date    = DateTimeField(auto_now_add=True)
    question    = TextField(max_length=1000)
    semester    = ForeignKey(Semester, on_delete=CASCADE,related_name="lectuers")
    video       = FileField(upload_to='media/',null=True ,blank=True)

    def __str__(self):
        return self.title



class Comment(Model):
    writer     = ForeignKey(User, on_delete=CASCADE , related_name="comments")
    content    = TextField(max_length=400)
    lectuer    = ForeignKey(Lectuer,on_delete=CASCADE , related_name="comments")
    add_date   = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.writer} is commented at {self.lectuer} "


class Perfect_student(Model):
    student   = ForeignKey(User,on_delete=CASCADE , related_name="perfect_students")
    semester  = ForeignKey(Semester, on_delete=CASCADE , related_name="perfect_students")

    def __str__(self):
        return str(self.student)










