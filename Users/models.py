import os

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

from modules.models import Standard


class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    bio=models.CharField(max_length=250)
    profile_pic=models.ImageField(upload_to='Images/', blank=True, verbose_name="Profile Pic",null=True)
    is_active=models.BooleanField(default=False)
    score=models.IntegerField(default=0)
    student='student'
    teacher='teacher'
    user_types=[(student,'student'),(teacher,'teacher')]
    user_type=models.CharField(max_length=10,choices=user_types,default=student)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, related_name="standard", null=True, blank=True,
                                 default=None)
    class Meta:
        ordering = ['-score']
    def __str__(self):
        return self.user.username


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    feedback = models.TextField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')


def save_homework_files(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.title:
        filename = 'homework_files/{}/{}.{}'.format(instance.title,instance.title, ext)
        if os.path.exists(filename):
            new_name = str(instance.title) + str('1')
            filename =  'lesson_images/{}/{}.{}'.format(instance.title,new_name, ext)
    return os.path.join(upload_to, filename)


class Task(models.Model):
    title = models.CharField(max_length=250,unique=True)
    content = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, null=True)
    user = models.ManyToManyField(User)
    created_on=models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200,unique=True)
    ppt = models.FileField(upload_to=save_homework_files, verbose_name="Presentations", blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Task, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('task_detail',kwargs={'slug': self.slug})
        #return reverse('modules:lesson_list', kwargs={'slug': self.subject.slug, 'standard': self.Standard.slug})




