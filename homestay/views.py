from distutils.command.upload import upload
from turtle import home
from urllib import request
from django.shortcuts import render, redirect
from homestay.models import Homestay
from homestay.forms import HomestayForm
from django.http import HttpResponse

# Create your views here.
def index(request):
    shelf = Homestay.objects.all()
    return render(request, 'homestay/library.html', {'shelf':shelf})

def create_homestay(request):
    homestay_form = HomestayForm()
    if request.method == 'POST':
        homestay_form = HomestayForm(request.POST, request.FILES)
        if homestay_form.is_valid():
            homestay_form.save()
            return redirect('index_homestay')
        else:
            return HttpResponse("Something is not working lah ayaaa")
    else:
        return render(request, 'homestay/upload_form.html', {'homestay_form':homestay_form})

def update_homestay(request, homestay_id):
    homestay_id = int(homestay_id)

    try:
        homestay_query = Homestay.objects.get(id=homestay_id)
    except Homestay.DoesNotExist:
        return redirect('index_homestay')

    homestay_form = HomestayForm(request.POST or None, instance=homestay_query)
    if homestay_form.is_valid():
        homestay_form.save()
        return redirect('index_homestay')
    
    return render(request, 'homestay/upload_form.html', {'homestay_form': homestay_form})

def delete_homestay(request, homestay_id):
    homestay_id = int(homestay_id)

    try:
        homestay_query = Homestay.objects.get(id=homestay_id)
    except Homestay.DoesNotExist:
        return redirect('index_homestay')

    homestay_query.delete()
    return redirect('index_homestay')

