from django.contrib import admin
from main.models import *

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class DegreeAdmin(admin.ModelAdmin):
    pass

class CourseAdmin(admin.ModelAdmin):
    pass

class ServiceAdmin(admin.ModelAdmin):
    pass

class EventAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

class Send_messageAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class TeacherAdmin(admin.ModelAdmin):
    pass

class ClientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Degree, DegreeAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Send_message, Send_messageAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Client, ClientAdmin)