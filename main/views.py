from django.shortcuts import render
from .models import Gallery, Product, Contact


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def gallery(request):
    images = Gallery.objects.all()
    return render(request, "gallery.html", {"images": images})


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

    return render(request, "contact.html")