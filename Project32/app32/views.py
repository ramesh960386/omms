from django.shortcuts import render,redirect
from .forms import PassportModel
from .forms import PassportForm
from .forms import PersonModel
from .forms import PersonForm
from django.contrib import messages


def addPE(request):
    return render(request, "addpe.html", {"form": PersonForm()})


def savePE(request):
    ano = request.POST.get("aadhar")
    name = request.POST.get("pname")
    cn = request.POST.get("contact")
    address = request.POST.get("address")
    PersonModel(aadhar=ano, pname=name, contact=cn, address=address).save()
    messages.success(request, "Person Details are Saved")
    return redirect('main')


def viewPE(request):
    return render(request, "viewpe.html", {"data": PersonModel.objects.all()})


def addPA(request):
    return render(request, "addpa.html", {"form": PassportForm()})


def savePA(request):
    no = request.POST.get("pno")
    details = request.POST.get("p_details")
    PassportModel(pno=no, p_details_id=details).save()
    messages.success(request, "Passport Details are Saved")
    return redirect('main')


def viewPA(request):
    return render(request, "viewpa.html", {"data": PassportModel.objects.all()})
