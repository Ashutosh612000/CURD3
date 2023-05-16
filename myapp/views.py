from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Myapp_Detail
from django.contrib.auth.models import User
from django.contrib import messages
import datetime



def index(request):

    mdata = Myapp_Detail.objects.all()

    return render(request, 'home.html', {'mdata': mdata})


def delete_data(request,id):
    ddata= Myapp_Detail.objects.get(id=id)
    ddata.delete()
    return redirect('myapp')

def update_data(request,id):
    udata = Myapp_Detail.objects.get(id=id)

    if request.method == 'POST':

        name = request.POST.get('name','')
        mobile = request.POST.get('mobile','')
        email = request.POST.get('email','')
        age = request.POST.get('age','')

        newage =  datetime.datetime.strptime(age,'%b %d, %Y').date()
        nage = newage.strftime('%Y-%m-%d')

        udata.name = name
        udata.mobile = mobile
        udata.email = email
        udata.age = nage

        udata.save()
        return redirect('myapp')

    return render(request, 'update.html', {'udata': udata})


def Buyer(request):

    return render(request, 'buyer.html')


def Seller(request):
    return render(request, 'seller.html')


def Add_data(request):
    if request.method == "POST":

        name = request.POST.get('name','')
        mobile = request.POST.get('mobile','')
        email = request.POST.get('email','')
        age = request.POST.get('age','')

        a = Myapp_Detail(name= name , mobile= mobile , email= email , age= age)
        a.save()
        return redirect('myapp')

    return render(request, 'add.html')

# def Signup(request):
#     return render(request, 'signup.html')


def handleSignup(request):
    if request.method == 'POST':
        #Get teh post parameters
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if len(username)>10:
            messages.error(request, 'username must be at least 10 characters')
            return redirect('handlesignup')

        if pass1 != pass2:
            messages.error(request, 'password dose not match')
            return redirect('handlesignup')
        #craete user 
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name =fname
        myuser.last_name =lname
        myuser.save()
      
        messages.success(request, "Profile details updated.")
        
        return redirect('myapp')

    return render(request, 'signup.html')
    # else:
    #     return HttpResponse('404 - Not Found')
       

def handleLogin(request):
    if request.method == 'POST':
        #Get teh post parameters
        loginusername=request.POST['username']
        loginpassword=request.POST['pass2']
    return render(request, 'login.html')

def handleLogout(request):
    return render(request, 'logout.html')