from django.shortcuts import render
from .models import StaffMember


# Create your views here.
def all_staff(request):
    staff_members = StaffMember.objects.all()
    return render(request, 'about.html', {"staff_members": staff_members})
