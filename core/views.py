from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html", {"title": "Home"})

def about(request):
    data = {
        "title": "About",
        "name": "James Emmanuel P. Fernandez",
        "student_id": "2020-10067",
    }
    return render(request, "about.html", data)