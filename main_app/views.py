from django.shortcuts import render , redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout 

# Create your views here.🐼
def login_veiw(request):
    if request.method =='POST':
        usename = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=usename, password=password,)
        if user:
            login(request,user)
            return redirect('home')
    return render(request, 'login.html')

def register_veiw(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password == cpassword:
            user = User(username=username,email=email)
            user.set_password(password)
            user.save()
            return redirect ('login')
    return render (request,'register.html')

    
    
def logout_veiw(request):
        logout(request)
        return redirect('home')
    
    
def home_view(request):
    return render(request,'home.html')
    

        
        
    

