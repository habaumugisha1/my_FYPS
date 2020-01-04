from django.db import models
from django.contrib.auth.models import User
from depart.models import Department

# # Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    reg_number = models.IntegerField(help_text='If you are not student type 12345')
    phone_number = models.IntegerField()
    department_name = models.ForeignKey(Department, related_name='userprofile', on_delete=models.CASCADE)
    ROLE_CHOICES = (
        ("-", "---------"),
        ("HOD", "HOD"),
        ("supervisor", "supervisor"),
        ("dean", "dean"),
        ("cordinator", "cordinator"),
        ("principle", "principle"),
        ("lecturor", "lecturor"),
        ("student", "student"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    image = models.ImageField(upload_to='images_profiles', blank=True)

    
    

    User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])




    






