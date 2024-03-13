from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.template.loader import render_to_string

# In models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=(('teacher', 'Teacher'), ('learner', 'Learner')), default='user')

    def _str_(self):
        return f"{self.user.username} - {self.role}"
    
# # class Learner(models.Model):
# #     id = models.AutoField(primary_key=True)
# #     name = models.CharField(max_length=100)
# #     address = models.CharField(max_length=255)
# #     email = models.EmailField(unique=True)
# #     phone_no = models.CharField(max_length=15)
# #     dob = models.DateField()

# #     def __str__(self):
# #         return self.name

# class Teacher(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     address = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     phone_no = models.CharField(max_length=15)
#     dob = models.DateField()

#     def __str__(self):
#         return self.name

# class Course(models.Model):
#     owner = models.ForeignKey(User, related_name="courses_created", on_delete=models.CASCADE)
#     subject = models.CharField(related_name="courses", on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     overview = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)
#     students = models.ManyToManyField(Learner, related_name="courses_joined", blank=True)

#     def __str__(self):
#         return self.title

# class Content(models.Model):
#     Course = models.ForeignKey(Course, related_name="contents", on_delete=models.CASCADE)
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'model__in': (
#         'text', 'video', 'image', 'file')})
#     object_id = models.PositiveIntegerField()
#     item = GenericForeignKey('content_type', 'object_id')

# class ItemBase(models.Model):
#     owner = models.ForeignKey(User, related_name='%(class)s_related', on_delete=models.CASCADE)
#     title = models.CharField(max_length=250)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True

#     def __str__(self):
#         return self.title


# class Text(ItemBase):
#     content = models.TextField()


# class File(ItemBase):
#     file = models.FileField(upload_to='files')


# class Image(ItemBase):
#     image = models.ImageField(upload_to='images')


# class Video(ItemBase):
#     url = models.URLField()

   
# class Cart(models.Model):
#     id = models.AutoField(primary_key=True)
#     learner_id = models.ForeignKey(Learner, on_delete=models.CASCADE)
#     course_id = models.ForeignKey(Course, on_delete=models.CASCADE)


# class Payment(models.Model):
#     id = models.AutoField(primary_key=True)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     payment_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Payment for {self.course.name} by {self.learner.name}"
    

