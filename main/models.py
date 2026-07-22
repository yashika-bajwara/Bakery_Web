from django.db import models



class Product(models.Model):

    name = models.CharField(max_length=100)

    image = models.ImageField(upload_to="products/")

    price = models.DecimalField(max_digits=8, decimal_places=2)

    description = models.TextField()


    def __str__(self):

        return self.name




class Gallery(models.Model):

    title = models.CharField(max_length=100)

    image = models.ImageField(upload_to="gallery/")


    def __str__(self):

        return self.title





class Contact(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    subject = models.CharField(max_length=150)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return self.name