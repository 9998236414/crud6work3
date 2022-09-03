from django.shortcuts import render,redirect
from .models import Members
# Create your views here.
def index(request):
    mymembers = Members.objects.all()
    return render(request,'index.html',{'mymembers':mymembers})

def add(request):
    return render(request, 'add.html')

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = Members(firstname=x, lastname=y)
    member.save()
    return redirect('/')

def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return redirect('/')

def update(request, id):
    mymember = Members.objects.get(id=id)
    return render(request,'update.html',{'mymember': mymember})

def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    member = Members.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return redirect('/')