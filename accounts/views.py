from django.shortcuts import render
from .forms import TeacherLoginForm

# Create your views here.


def login_view(request):
    form = TeacherLoginForm()
    if request.teachers.is_authenticated:
        return redirect('home.html')
    if request.method == 'POST':
        form = TeacherLoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        if form.is_valid():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home.html')
            else:
                return render(request, 'login.html', {'form': form})
