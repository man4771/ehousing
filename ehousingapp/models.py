from django.db import models

class UserRole(models.Model):
    Role = models.CharField(max_length=10)

    class Meta:
        db_table = 'userrole'

    def __str__(self) -> str:
        return self.Role

class Master(models.Model):
    UserRole = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=12)
    IsActive = models.BooleanField(default=False)
    RegDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'master'

    def __str__(self) -> str:
        return self.Email

gender_choices = (
    ('m', 'male'),
    ('f', 'female'),
)
class Student(models.Model):
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    ProfileImage = models.FileField(upload_to='profiles/', default='avatar.png')
    FullName = models.CharField(max_length=25, default='', blank=True)
    Gender = models.CharField(max_length=5, choices=gender_choices)
    Date_of_birth = models.DateField(auto_created=True, default='1991-01-01')
    Date_of_joining = models.DateField(auto_created=True, default='1991-01-01')
    Roll_no = models.IntegerField(default='1', blank=True)
    Address = models.TextField(max_length=150, default='', blank=True)

    class Meta:
        db_table = 'student'

class Teacher(models.Model):
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    ProfileImage = models.FileField(upload_to='profiles/', default='avatar.png')
    FullName = models.CharField(max_length=25, default='', blank=True)
    Gender = models.CharField(max_length=5, choices=gender_choices)
    Date_of_birth = models.DateField(auto_created=True, default='1991-01-01')
    Date_of_joining = models.DateField(auto_created=True, default='1991-01-01')
    Roll_no = models.IntegerField()
    Address = models.TextField(max_length=150, default='', blank=True)

    class Meta:
        db_table = 'teacher'   

class Book(models.Model):
    Content = models.TextField(max_length=5000)
    PublishDate = models.DateTimeField(auto_now_add=True)
    UpdatedDate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'book'
# Create your models here.



# Create your models here.
