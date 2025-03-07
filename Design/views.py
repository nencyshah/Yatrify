from . models import ScriptInfo,UserInfo,BuyInfo,SellInfo
from django.shortcuts import render, redirect
from . models import ScriptInfo,UserInfo,BuyInfo,SellInfo,PlaceInfo
from . forms import Scriptform,Userform,Buyform,Sellform, Placeform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.db.models import Q,F
# Create your views here.
def Indexview(request):
    return render(request, 'index.html')

def Aboutus(request):
    return render(request, 'about.html')

def Contactus(request):
    return render(request, 'contact.html')

def Service(request):
    return render(request, 'service.html')

def Package(request):
    return render(request, 'package.html')


def AdminDashBoard(request):
    return redirect('Scripttrans')

def UserDashBoard(request):
    return redirect('Buytrans')




def Scripttrans(request):
    
    form = Scriptform(request.POST)
    if(form.is_valid()):
        form.save()
    return render(request,"Admin/CategoryForm.html",{'form': form})


def Usertrans(request):
    
    form = Userform(request.POST, request.FILES)
    if(form.is_valid()):
        form.save()
    return render(request,"UserForm.html",{'form': form})

def Buytrans(request):
    
    form = Buyform(request.POST)
    if(form.is_valid()):
        form.save()
    return render(request,"User/BuyForm.html",{'form': form})

def Selltrans(request):
    
    form = Sellform(request.POST)
    if(form.is_valid()):
        form.save()
    return render(request,"User/SellForm.html",{'form': form})

def Login(request):
    flag = 0
    if (request.method == 'POST' and flag == 0):
#        form = AuthenticationForm()
        Uname = request.POST['username']
        Pword = request.POST['password']
        UserType = request.POST['User']
        #x = loginfun(Username, Password)
        #y = loginfun1(Username, Password)
        #z = loginfun2(Username, Password)
        
        if (Uname == 'Admin' and Pword == 'Admin' and UserType=='Admin'):
            request.session['admin'] = Uname
            flag = 1
            
            return redirect('AdminDashBoard')
        elif (flag == 0 and UserType=='User' and (UserInfo.objects.filter(Q(UserName=Uname) & Q(Password=Pword)).exists())):
            
                request.session['User'] = Uname
                flag = 1
                return redirect('UserDashBoard')
            
        
         

        else:
            form = AuthenticationForm()
            return render(request, 'login.html', {'form': form})

    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def PlaceTrans(request):
    
    form = Placeform(request.POST, request.FILES)
    if(form.is_valid()):
        form.save()
    return render(request,"PlaceForm.html",{'form': form})

def PlaceView(request):
    context ={"PlaceDDL":PlaceInfo.objects.all()}
    return render(request, "PlaceViewHtml.html",context)

def PlaceViewInfo(request,id=0):
    context = {"PlaceDDL1":PlaceInfo.objects.filter(Q(id=id))}
    return render(request, 'PlaceViewInfo.html', context)