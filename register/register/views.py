from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from resumedata.models import Resume
from service.models import Service
# from apply.models import Apply
from django.core.paginator import Paginator
from .file import html2pdf
from createjob.models import Create


# Create your views here.

@login_required(login_url='log')
def home(request):
    return render(request,'home.html')

def log(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')
    

def resume(request):
        
    return render(request,'resume.html')

def result(request, id):
    data = Resume.objects.get(pk=id)
    
    return render(request,'home.html',{'data':data})

def pdf(request):
    pdf=html2pdf('home.html')
    return HttpResponse(pdf,content_type="application/pdf")

def register_data(request):
    try:

        if request.method=='POST':
            user_name = request.POST.get('name')
            user_address = request.POST.get('address')
            user_city = request.POST.get('city')
            user_state = request.POST.get('state')
            user_phone = request.POST.get('phone')
            user_email = request.POST.get('email')
            user_summary = request.POST.get('summary')
        
            user_education = request.POST.get('education')
            user_experience = request.POST.get('experience')
            user_skills = request.POST.get('skills')
            final = Resume(name=user_name,address=user_address,city=user_city,state=user_state,phone=user_phone,email=user_email,summary=user_summary,education=user_education,experience=user_experience,skills=user_skills)
            final.save()
            return redirect('home')
    except:
        pass
        
    return render(request,'resume.html')



def signup(request):
    try:
        if request.method == 'POST':
            uname=request.POST.get('username')
            email=request.POST.get('email')
            pass1=request.POST.get('password1')
            pass2=request.POST.get('password2')
            if pass1!=pass2:
                return HttpResponse('wrong password')
            else:

                my_user = User.objects.create_user(uname,email,pass1)
                my_user.save()
                return redirect('log')
    except:
        pass
       

    return render(request, 'signup.html')

def log_out(request):
    logout(request)
    return redirect('log')

def index(request):
    if request.method == 'GET':
        return render(request,'index.html')
    
def createjob(request):
    try:
        if request.method=='POST':
            create_info=request.POST.get('title')
            create_desc=request.POST.get('desc')
            create_link=request.POST.get('link')
            mydata=Create(create_info=create_info,create_desc=create_desc,create_link=create_link)
            mydata.save()

            return redirect('job')
    except:
        pass

        

    return render(request,'createjob.html')
    

# def apply(request):
#     applydata=Apply.objects.all()
#     # paginator = Paginator(applydata,2)
#     # page_no=request.Get.get('page')
#     # applydatafinal=paginator.get_page(page_no)

#     data={
#         'applydata':applydata
#     }
#     return render(request,"apply.html",data)

def testi(request):
    servicedata=Service.objects.all()
    data={
        'servicedata':servicedata
    }
    return render(request,"testi.html",data)


def apply(request):
    job_data=Create.objects.all()
    data={
        'job_data':job_data
    }
    return render(request,"apply.html",data)

# def apply(request):
#     return render(request,"apply.html")











