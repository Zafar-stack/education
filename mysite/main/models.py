from django.db import models
from datetime import datetime, date


# Create your models here.

class Author(models.Model):
    logo = models.ImageField(upload_to='upload')
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Degree(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Course(models.Model):
    logo = models.ImageField(upload_to='upload')
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, default=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    logo = models.ImageField(upload_to='upload')
    title = models.CharField(max_length=200)
    description = models.TextField()


    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=200)
    description1 = models.TextField()
    description2 = models.TextField()
    logo = models.ImageField(upload_to='upload')
    pub_date = models.DateField(blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    message = models.TextField()
    logo = models.ImageField(upload_to='upload')
    name = models.CharField(max_length=200)
    description = models.TextField()
    pub_date3 = models.DateField(blank=True, null=True)


    def __str__(self):
        return self.name


class Send_message(models.Model):
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name





class Teacher(models.Model):
    logo = models.ImageField(upload_to='upload')
    name = models.CharField(max_length=200)
    description = models.TextField()
    link1 = models.CharField(max_length=200)
    link2 = models.CharField(max_length=200)
    link3 = models.CharField(max_length=200)
    link4 = models.CharField(max_length=200)
    link5 = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Client(models.Model):
    logo = models.ImageField(upload_to='upload')
    count = models.IntegerField()
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=200)
    description1 = models.TextField()
    logo = models.ImageField(upload_to='upload')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date2 = models.DateField(blank=True)
    description2 = models.TextField(blank=True)
    description3 = models.TextField(blank=True)

    def __str__(self):
        return self.title
