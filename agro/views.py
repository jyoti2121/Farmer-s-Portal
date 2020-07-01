from django.shortcuts import redirect, render
from django.http import response, JsonResponse
from .models import Services, News, Plantation, Teams, Gallery, Customer, What_we_do, Labour, Tasks
from django.conf import settings
import os
import pickle
import numpy as np
from django.contrib import messages
from django.contrib.staticfiles.templatetags.staticfiles import static
import csv

# Create your views here.
def index(request):
    plant1 = Plantation.objects.all() 
    news1 = News.objects.all()
    context= {"plant1" : plant1, "news1" : news1}
    return render(request,'index.html',{'context':context})

def contact(request):
    return render(request,'contact.html')

def gallery(request):
    gallery1 = Gallery.objects.all()
    return render(request,'gallery.html',{'gallery1':gallery1})

def about(request):
    team1 = Teams.objects.all()
    return render(request,'about.html',{'team1':team1})

def services(request):
    serv1 = Services.objects.all()
    cust1 = Customer.objects.all()
    what1 = What_we_do.objects.all()
    return render(request,'services.html',{'serv1':serv1})

def rainfall_predict(request):
    if request.method == 'POST':
        path=os.path.join(settings.MODELS_ROOT,'rainfall_model.p')
        with open(path, 'rb') as pickled:
            data = pickle.load(pickled)
        reg = data['reg']
        x1 = int(request.POST['x1'])
        x2 = int(request.POST['x2'])
        x3 = int(request.POST['x3'])
        x=np.array([x1,x2,x3])
        x=x.reshape(1,3)
        prediction=reg.predict(x)
        prediction=round(float(prediction),2)
        prediction='Predicted Rainfall is '+str(prediction)+' mm'
        messages.info(request,prediction)
        return redirect('rainfall_predict')
        #return render(request,'rainfall_predict.html',{'prediction':prediction})
    else:
        return render(request,'rainfall_predict.html')

def labour(request):
    current_user=request.user
    labour1 = Labour.objects.filter(farmer_id=current_user.id)
    return render(request,'labour.html',{'labour1':labour1})

def add_labour(request):
    if request.method == 'POST':
        if request.POST['button'] == 'ADD':
            name = request.POST['name']
            state = request.POST['state'] 
            city = request.POST['city']
            role = request.POST['role']
            salary = request.POST['salary']
            labour = Labour.objects.create(farmer_id=request.user.id, labour_name=name, labour_state=state, labours_city=city, labours_role=role, labour_salary =salary)
            labour.save()
            return redirect('labour')
        else:
            id=request.POST['id']
            labour = Labour.objects.get(id=id)
            labour.delete()
            return redirect('labour')
    else:
        return render(request,'add_labour.html')

def tasks(request):
    if request.method == 'POST':
        if request.POST['submit']=='Submit':
            task_id = int(request.POST['task_id'])
            tasks1 = Tasks.objects.get(id=task_id)
            tasks1.task_complete= True
            tasks1.save()
            return redirect('tasks')
        else:
            task_id = int(request.POST['task_id'])
            tasks1 = Tasks.objects.get(id=task_id)
            tasks1.delete()
            return redirect('tasks')
    else:
        current_user=request.user
        tasks1 = Tasks.objects.filter(farmer_id=current_user.id)
        return render(request,'tasks.html',{'tasks1':tasks1})

def add_tasks(request):
    if request.method == 'POST':
        task_name = request.POST['name']
        task_date = request.POST['date']
        task_priority = request.POST['priority']
        task = Tasks.objects.create(farmer_id=request.user.id, task_complete=False, task_name=task_name, task_date=task_date, task_priority=task_priority)
        task.save()
        return redirect('tasks')
    
    else:
        return render(request,'add_tasks.html')

def production_predict(request):
    if request.method == 'POST':
        State = str(request.POST['state'])
        Crop = str(request.POST['crop'])
        Rainfall = float(request.POST['rainfall'])
        Area = float(request.POST['area'])
        name="model_"+State+"_"+Crop+".p"
        path=os.path.join(settings.MODELS_ROOT,name)
        with open(path, 'rb') as pickled:
            data = pickle.load(pickled)
        model = data['model']
        x=np.array([Rainfall,Area])
        x=x.reshape(1,2)
        prediction=model.predict(x)
        prediction=round(float(prediction),2)
        prediction='Predicted Production for '+State+' for '+Crop+ ' is '+str(prediction)+' tons'
        messages.info(request,prediction)
        return redirect('production_predict')
    else:
        return render(request,'production_predict.html')

        