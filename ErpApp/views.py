from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from ErpApp.models import Register
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
def base(request):
    return render(request, 'base.html')


def Administrator(request):
    if request.method == "POST":
        if Register.objects.get(category="Admin"):
            return render(request, '/inlogin.html')

        else:
            return HttpResponse("YOU are not Admin")

    else:
        return render(request, 'Administrator.html')


def euser(request):

    now = datetime.now().time()  # time object

    return render(request, 'user.html', {'currenttime': now})


def registration(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        categeory = request.POST.get('categeory')
        from datetime import datetime
        now = datetime.now().time()
        register = Register(fullname=fullname, email=email,
                            password=password, categeory=categeory, logintime=now)
        register.save()

        return HttpResponse("<h1> login Successfull<h1>")

    return render(request, 'registration.html',)


# if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             adminusername = form.cleaned_data.get('username')
#             adminpassword = form.cleaned_data.get('password')
#             user = authenticate(username=adminusername, password=adminpassword)
#             login(request, user)
#             return redirect('/')

def inlogin(request):

    if request.method == "POST":
        name = request.POST.get('username', '')
        list1 = []
        for p in Register.objects.raw('SELECT * FROM ErpApp_register'):
            list1.append(p)
        #h = Register.objects.filter(fullname = name )
        # member = Register.objects.all()
        # name = request.POST.get('username', '')
        # post = Register.objects.get(fullname = name)
        # distofname  = {" name ": member}
        # print(distofname)
        # print(post)
        # print(h)
        return render(request, 'withinlogin.html', {"context": list1})


def passwordchanging(request):
    if request.method == "GET":
        return render(request, 'changepassword.html')
    else:
        emailid = request.POST.get('email1', '')
        passfromdb = Register.objects.get(email=emailid)
        # passfromdb = Register.objects.filter(email=emailid)

        # print(emailid)
        # print(passfromdb)
        if passfromdb:
            return render(request, "successful.html", {"data": passfromdb})
            return redirect("/registration/")
