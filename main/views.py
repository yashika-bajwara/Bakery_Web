from django.shortcuts import render, redirect
from .models import Product, Gallery, Contact
from django.core.mail import send_mail



def home(request):

    return render(request, "home.html")



def about(request):

    return render(request, "about.html")



def products(request):

    product_data = Product.objects.all()

    return render(request, "products.html", {"products": product_data})



def gallery(request):

    images = Gallery.objects.all()

    return render(request, "gallery.html", {"images": images})



def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")

        email = request.POST.get("email")

        subject = request.POST.get("subject")

        message = request.POST.get("message")



        # Save data in database

        Contact.objects.create(

            name=name,

            email=email,

            subject=subject,

            message=message

        )



        # Send email

        send_mail(

            subject,

            f"""
Name: {name}

Email: {email}

Message:
{message}
            """,

            "yourgmail@gmail.com",

            ["yashikabajwara2006@gmail.com"],

            fail_silently=False,

        )


        return redirect("contact")



    return render(request,"contact.html")