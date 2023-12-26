from django.contrib import admin
from apiapp.models import student
# Register your models here.

class studentAdmin(admin.ModelAdmin):
    # list_display=("name","surname","age")
    pass


admin.site.register(student,studentAdmin)

