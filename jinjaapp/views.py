from django.shortcuts import render
def home(request):
    return render(request,template_name='index.html')
def about(request):
    return render(request,template_name='about.html')
def contact(request):
    return render(request,template_name='contact.html')
def gallery(request):
    return render(request,template_name='gallery.html')
# Create your views here.
