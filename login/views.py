from django.shortcuts import redirect, render
from django.http import response
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def login(request):

    # for post request
    if request.method=='POST':
    
        # for submit
        if request.POST['button']=='Submit':
            username=request.POST['username']
            password=request.POST['password']
            
            #autheticate
            user = auth.authenticate(username = username,password = password)
        
            if user is not None:
                auth.login(request, user)
                return redirect('/')

            else:
                messages.error (request,'invalid credentials')
                return redirect('register')
             
        # for register
        else:
            return redirect('register')
            #return render(response,'register.html')
   
   # for get request
    else:
        return render(request,'login.html')


def register(request):

    #for post request 
    if request.method == 'POST':

        #get all the data from register.html
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['confirm_password']

        # check the comstraints
        if password == cpassword:

            if User.objects.filter(username=username).exists():
                print('Username already exists')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                print('email already exits')
                return redirect('register')

            else:
                #pass the data to the database
                user = User.objects.create_user(username=username, email=email, password= password, first_name=first_name, last_name=last_name,)
                #commit the changes
                user.save()
                return redirect('login')

        else:
            print('Password not matching')
            return redirect('register')

    #for get request        
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
def index(request):
    return redirect('/')
