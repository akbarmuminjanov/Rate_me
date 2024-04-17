from django.shortcuts import render
from .models import Stars, Register


# Create your views here.
def index(request):
    stars = Stars.objects.all()
    return render(request, "index.html", {"stars":stars})

def articles(request, full_name):
    article = Stars.objects.get(full_name=full_name)
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        acc = Register.objects.create(username=username, password=password)
        acc.save()
        if acc:
            article.view+=1
            article.save()
            return render(request, "article.html", {"article":article})
    return render(request, "article.html", {"article":article})
