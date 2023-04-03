from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import Society_Registration, Member_Registration, Notice, Complaint, Rent_Registration

def index(request):
    """
    View function for home page of site.
    """
    
    num_members=Member_Registration.objects.all().count()
    num_notices=Notice.objects.all().count()
    # Available books (status = 'a')
    num_tenants=Rent_Registration.objects.all().count()
    num_complaints=Complaint.objects.count()  # The 'all()' is implied by default.
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_members':num_members,'num_notices':num_notices,'num_tenants': num_tenants,'num_complaints':num_complaints},
    )
    
def complaints(request):
    Complaint_all=Complaint.objects.all()[:50]
    return render(
        request,
        'complaints.html',
        context={'Complaint_all':Complaint_all}
    )

def notices(request):
    Notice_all=Notice.objects.all()[:50]
    return render(
        request,
        'notices.html',
        context={'Notice_all':Notice_all}
    )

'''
def maintenance(request):
    maint=Member_Registration.objects.all()[:50]
    base_amt=3000
    wat_amt=1000
    
    for r in maint:
        room=r.No_of_rooms
        park=r.Parking
        ramt=room*100
        pamt=park*200
        total=base_amt+wat_amt+ramt+pamt
'''

def maintenance(request):
    props = Member_Registration.objects.all()
    #dates = ClosedDate.objects.all()
    for i in props:
        
        print(i.derivate_field_1)

    context={
        "props":props,
       # "dates":dates
    }

    return  render(request,"maintenance.html",context)
'''
    
    return render(
        request,
        'maintenance.html',
        context={'maint':maint,'total':total}
    )
'''
