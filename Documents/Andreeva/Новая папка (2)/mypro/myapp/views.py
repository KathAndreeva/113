from django.shortcuts import render
from myapp.models import product

# Create your views here.


def index(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        new = product(name=data["name1"],
                      count=data["name2"],  cost=data["name3"])
        new.save()

    return render(request, "Index.html")


def card(request):
    data = product.objects.all()
    return render(request, "card.html", {"res": data})


def card_2(request):
    data = product.objects.all()
    return render(request, "main.html", {"res": data})
