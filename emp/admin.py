from django.contrib import admin
from .models import Emp
from .models import Testimonial
# Register your models here.


class EmpAdmin(admin.ModelAdmin):
    list_display=('name','working','department','phone')
    list_editable=('working',)
    search_fields=('name','department')

admin.site.register(Emp,EmpAdmin)
admin.site.register(Testimonial)
