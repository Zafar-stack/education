from django.shortcuts import render
from main.models import *

# Create your views here.
def indexHandler(request):
    courses = Course.objects.all()[:3]
    services = Service.objects.all()
    comments = Comment.objects.all()
    events = Event.objects.all()
    return render(request, 'index.html', {'courses':courses,
                                        'services':services,
                                        'comments':comments,
                                        'events':events,

                                          })


def aboutHandler(request):
    return render(request, 'about.html', {})



def coursesHandler(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses':courses,

                                            })



def newsHandler(request):
    posts = Post.objects.all()
    latposts = Post.objects.all()[:3]
    return render(request, 'news.html', {'posts':posts,
                                         'latposts':latposts,

                                         })

def newspostHandler(request, news_id):
    newspost = Post.objects.get(id = int(news_id))
    return render(request, 'news_post.html', {'newspost':newspost,

                                              })


def contactHandler(request):
    return render(request, 'contact.html', {})


def teachersHandler(request):
    return render(request, 'teachers.html', {})