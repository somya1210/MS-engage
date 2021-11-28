from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView
from Users.forms import UserForm, StudentProfileForm, LoginForm, TeacherProfileForm, TaskForm
from Users.models import UserProfile, Contact, Task
from modules.models import Standard
from django.views import generic

def user_login(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "Users/login.html", {"form": form, "msg": msg})



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered=False
    msg = None
    if request.method== "POST" :
        user_form=UserForm(data=request.POST)
        studentprofile_form=StudentProfileForm(data=request.POST)

        if user_form.is_valid() and studentprofile_form.is_valid():
            user=user_form.save()
            user.is_active=True
            user.save()
            profile=studentprofile_form.save(commit=False)
            profile.user=user
            profile.is_active=True
            profile.save()
            msg = 'User created - please <a href="/user_login">login</a>.'
            registered=True
        else:
            msg='Form is invalid'
            print(user_form.errors,studentprofile_form.errors)
    else:
        user_form=UserForm()
        studentprofile_form=StudentProfileForm()
    return render(request, 'Users/registration.html',
                  { 'registered': registered ,
                    'user_form': user_form ,
                    'studentprofile_form' : studentprofile_form,
                    'msg':msg
                    })



def register_teacher(request):
    registered=False
    msg = None
    if request.method== "POST" :
        user_form=UserForm(data=request.POST)
        userprofile_form=TeacherProfileForm(data=request.POST)
        if user_form.is_valid() and userprofile_form.is_valid():

            user=user_form.save()
            user.is_active = False
            user.save()
            profile=userprofile_form.save(commit=False)
            profile.user=user
            profile.is_active=False
            profile.save()
            msg = 'Dear Teacher ,Your account will be approved by the admin! Kindly wait for the approval'

        else:
            msg='Form is invalid'
            print(user_form.errors,userprofile_form.errors)
    else:
        user_form=UserForm()
        userprofile_form=TeacherProfileForm()
    return render(request, 'Users/registration_teacher.html',
                  { 'registered': registered ,
                    'user_form': user_form ,
                    'userprofile_form' : userprofile_form,
                    'msg':msg
                    })
class HomeView(TemplateView):
    template_name = 'Users/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        standards = Standard.objects.all()
        teachers = UserProfile.objects.filter(user_type='teacher',is_active=True )
        context['standards'] = standards
        context['teachers'] = teachers
        return context

class ContactView(generic.CreateView):
    model = Contact
    fields = '__all__'
    template_name = 'Users/contact.html'

def dashboard(request):
    standards = Standard.objects.all()
    return render(request,'Users/dashboard.html')

def todolist(request):
    Tasks=Task.objects.all()

    context={'Tasks':Tasks}
    return render(request,'Users/todolist.html',context)

def update(request,pk):
    task=Task.objects.get(id=pk,user=request.user)
    task.completed=True
    task.save()
    return redirect('/dashboard')
#def HomePage(request):
 #   Tasks=Task.objects.all().order_by('-created_on')

  #  context={'Tasks':Tasks}
   # return render(request,'Users/homework.html',context)
class HomePage(generic.ListView):

  queryset=Task.objects.all().order_by('-created_on')
  template_name = 'Users/homework.html'


class DetailView(generic.DetailView):
 model = Task
 template_name = 'Users/task_detail.html'
 def get_context_data(self,*args,**kwargs):
     context=super(DetailView,self).get_context_data(*args,**kwargs)
     return context


class TaskUpdateView(UpdateView):
    # fields = ('lesson_id','name','position','image','video','ppt','Notes')
    form_class = TaskForm
    model= Task
    template_name = 'Users/submit_assignment.html'

    def get_success_url(self):
        self.object = self.get_object()
        return reverse_lazy('homework',kwargs={'slug':self.object.slug})


    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.created_by = self.request.user
        fm.Standard = self.object.standard
        fm.subject = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

def progress(request):
    task=Task.objects.all()
    count=0
    user=request.user
    for t in task:
        if(t.completed == True):
            if(t.standard== user.profile.standard):
             count+=1
    rewards=2*count
    context={'count':count,'rewards':rewards}
    return render(request,'Users/progress.html',context)