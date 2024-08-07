from django.shortcuts import render

# Create your views here.🐼
def login_veiw(request):
    return render(request, 'login.html')
def register_veiw(request):
    return render(request, 'register.html')

def home_veiw(request):
    return render(request, 'home.html')
