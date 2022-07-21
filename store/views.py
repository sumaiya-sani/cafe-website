from hashlib import new
from logging.handlers import RotatingFileHandler
from django.urls import reverse_lazy
from django.views import generic
from sre_constants import SUCCESS
from django.shortcuts import redirect, render
from django.views.generic import ListView
from.models import Review, cafe
from .forms import AddcafeForm, EditForm, LoginForm, NewUserForm, ReviewsForm
from store.models import cafe,Review
from django.contrib.auth import authenticate,login,logout


def index(request):
    
    return render(request ,'index.html')

def CafeList(request):
    cafe_list=cafe.objects.all()
   
    return render(request,'cafe_list.html', {'cafe_list':cafe_list, })

def CafeDetail(request,slug ):
    rating=Review.objects.all()
    cafe_slug=cafe.objects.get(slug=slug)
    
   
    form=ReviewsForm()
    if request.method =='POST':
      form=ReviewsForm(request.POST ,instance=cafe_slug)
      if form.is_valid():
    
         

        #new_rating=form.cleaned_data["rating"]
        #new_content=form.cleaned_data["content"]
      
        form= Review(
        rating=request.POST["rating"],
        content=request.POST["content"],
        created_by=request.user,
        cafe_name=cafe.objects.get(slug=slug)
        )
        form.save()
        return render(request,'cafe_details.html',{
            'form':ReviewsForm(),
            'cafe_slug':cafe_slug,
            SUCCESS:True
       })

      
      else:
        form=ReviewsForm()
        return render(request,'cafe_list.html',{
            'form':form,
            'cafe_slug':cafe_slug,

            
        })

    return render(request,'cafe_details.html',{'cafe_slug':cafe_slug, 'form':ReviewsForm(),'rating':rating   })




def search_page(request):
 if request.method=="POST":
    searched=request.POST['searched']
    search_pages=cafe.objects.filter(name__contains=searched)

    return render(request,"search.html",{'searched':searched,'search_pages':search_pages})
 else:
      return render(request,"search.html",{})   


def add_cafe(request):
    cafe_list=cafe.objects.all()

    form=AddcafeForm()
    if request.method=="POST":
        form=AddcafeForm(request.POST,request.FILES)
        if form.is_valid:
            form= cafe(
            user=request.user,
            name=request.POST["name"],
            disc=request.POST["disc"],
            picture=request.FILES.get("picture"),
            recent_picture=request.FILES.get("recent_picture"),
            city=request.POST["city"],
            working_hours=request.POST["working_hours"],
            signture=request.POST["signture"],
            slug="slug"
             )

            form.save()
            return render(request,'cafe_list.html', {'cafe_list':cafe_list})    
        else:
          form=AddcafeForm()
  

    return render(request,'add_cafe.html' ,{"form":form})    


class register(generic.CreateView):
    form_class=NewUserForm
    template_name='register.html'
    success_url=reverse_lazy('cafe:cafe_list')


 
class UserEditView(generic.CreateView):
    form_class=EditForm
    template_name='edit_profile.html'
    success_url=reverse_lazy('cafe:index')
    
#To find the user who login in and bring the profile of him 
    def get_object(self):
        return self.request.user

def login_page(request):

    if request.method=="POST":
     form=LoginForm()
     username=request.POST.get('username')
     password=request.POST.get('password')
     user=authenticate(request,username=username,password=password)
     if user is not None:
        login(request,user)
        return redirect('cafe:index')
    else:
        form=LoginForm()    
    
    return render(request,'login.html',{'form':form})     

