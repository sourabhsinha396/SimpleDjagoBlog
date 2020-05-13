from django.shortcuts import render
from .forms import BlogModelForm
from .models import BlogModel
from django.http import JsonResponse
# Create your views here.

def homepage(request):
	if request.POST:
		form = BlogModelForm(request.POST)
		form.save()
		context = {'msg':"succesfully Submitted",'form':form}
		return render(request,'homepage.html',context)
	else:
		form = BlogModelForm()
		context = {'form':form}
		return render(request,'homepage.html',context)

def ajaxsave(request):
	print(request.POST)
	print(request.POST['title'])
	BlogModel.objects.create(title=request.POST['title'],content = request.POST['textareacontent'],location = request.POST['location'])
	return JsonResponse({'message':'It worked fine'})