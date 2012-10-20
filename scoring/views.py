import logging
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from fund.decorators import approved_membership
from grants import models

# Create your views here.


@login_required(login_url='/fund/login/')
def read_grant(request, app_id):
    return render_to_response("scoring/reading.html", {})
#  "grant": models.GrantApplication.objects.get(pk=app_id)})
    


 
@approved_membership() 
def Save(request):
  if request.method=='POST':
    form = models.RatingForm(request.POST)
    if form.is_valid():
      form.save()
  
  return render_to_response('debug.html', {'form': form})



""" There are two blank templates created:
scoring/reading.html
scoring/project_summary.html

Add new ones as needed """
