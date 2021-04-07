from django.shortcuts import render,redirect
from .models import TodayList
from .forms import uploadForm



# Create your views here.

# class uploadedListView(ListView):
#     model = TodayList
#     todo = TodayList.objects.all()
#     return render(request,'.html',{'todo':todo})

def listpage(request):
    todo = TodayList.objects.all()
    return render(request,'listpage.html',{'todo':todo})

def uploadpage(request):
    if request.method == 'POST':
        form = uploadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listpage')

        
    else:
        form = uploadForm()

    return render(request,'uploadpage.html',{"form":form})
    
def delete(request,pk):
    item = TodayList.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    return render(request,"delete.html",{"item":item})