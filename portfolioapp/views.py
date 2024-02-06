from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    datas = soat.objects.all()
    return render(request=request, template_name="index.html", context={'datas':datas})