from ast import Delete
import re
from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def insert(request):
    email_1 = request.POST['email']
    password_1 = request.POST['password']
    # from index.html form 


    new_user = Master_User.objects.create(email=email_1,password=password_1)
    # insert record in usermaster tabel in database
    

    all_data = Master_User.objects.all()
    data = {
        'all_data':all_data 
    }
    
    # Dict sending to index.html for print
    return render(request,'show.html',data)

def delete(request):
    email1 = request.POST['email']
    try: 
        one_user = Master_User.objects.get(email=email1)
        print(one_user)
        one_user.delete()
    except:
         print("not avilableee")
    # one_user.delete()
    # if one_user:
    #     print("email is avilable in daytabse")
    # else:
    #     print("not avilableee")
   
    all_data = Master_User.objects.all()
    data = {
        'all_data':all_data 
    }
    return render(request,'show.html',data)

def update(request):
    id1 = request.POST['id']
    email1 = request.POST['email']
    try: 
        one_user = Master_User.objects.get(id=id1)

        one_user.email = email1
        one_user.save()
        all_data = Master_User.objects.all()
        data = {
        'all_data':all_data 
        }
        return render(request,'show.html',data)
    except:
        print("not avilableee")
    all_data = Master_User.objects.all()
    data = {
        'all_data':all_data 
        }
    return render(request,'show.html',data)
        

    