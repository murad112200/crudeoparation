from django.shortcuts import render,redirect
from myapp.models import Teacher,Student
from .models import Store
# Create your views here.
def home(request):
    return render (request,("home.html"))



def indax(request):
    return render (request,("indax.html"))


def master(request):
    return render (request,("master.html"))


def navbar(request):
    return render (request,("navbar.html"))


def footer(request):
    return render (request,("footer.html"))


def valupass(request,n):
    context={"N":n}
    return render (request,"valupass.html",context)



def teacher(request):
    teacher_data=Teacher.objects.all()
    return render(request,"teacher.html",{"data":teacher_data})



def froms(request):
    if request.method =="POST":
        sname=request.POST.get("name")
        spassword=request.POST.get("password")
        snumber=request.POST.get("number")
        saddress=request.POST.get("address")
        semil=request.POST.get("email")
        obj=Student.objects.create(name=sname,password=spassword,number=snumber,address=saddress,email=semil)
      
        obj.save()

    return render(request,"from.html")



def storetable(request):
    table_data=Store.objects.all()  

    return render(request,"storetabel.html",{"data":table_data})




def storefrom(req):
    if req.method=="POST":
        sname=req.POST.get("name")
        snumber=req.POST.get("number")
        simage=req.FILES.get("image")
        sfile=req.FILES.get("file")
        obj=Store(name=sname,number=snumber,image=simage,file=sfile)
        obj.save()

       
        return redirect('storetable')



    return render(req, "storeform.html")


def storetable2(request):
    stores=Store.objects.all()  

    return render(request,"store.html",{"data":stores})


def updatestore(request,PK):
    store_instance = Store.objects.get(id=PK)
    if request.method=="POST":
        sname=request.POST.get("name")
        snumber=request.POST.get("number")
        simage=request.FILES.get("image")
        sfile=request.FILES.get("file")
        obj=Store(id=PK,name=sname,number=snumber,image=simage,file=sfile)
        obj.save()
        return redirect("storetable2")

    return render(request,"update.html",{"data": store_instance})


def deleteitem(request,PK):
    store_instance = Store.objects.get(id=PK).delete()

    return redirect("storetable2")