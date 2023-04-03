from django.contrib import admin

# Register your models here.
from .models import Society_Registration, Member_Registration, Notice, Complaint, Rent_Registration

admin.site.register(Society_Registration)
admin.site.register(Member_Registration)
admin.site.register(Notice)
admin.site.register(Complaint)
admin.site.register(Rent_Registration)
admin.site.site_header="A for Assistant"
admin.site.site_title = 'A for Assistant'
