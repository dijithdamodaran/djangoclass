from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def about(request):
    return redirect('/contact')
    #return HttpResponse("hello from function based view")

def contact(request):
    return HttpResponse("hello from function based view contact")

def edit(request,rid):
    return HttpResponse("hello this is edit page:"+rid)

def delete(request,rid):
    return HttpResponse("this is the delete page:",rid)

def addition(request,a,b):
    c=int(a)+int(b)
    return HttpResponse("this is addition :"+str(c))

def renderhtml(request):
    return render(request,'hello.html')

#passing data to hello.html file

def passdatatohello(request):
    #content={'data':'hello world'}
    content={}
    content['data']="hello world"

    return render(request,'hello.html',content)

