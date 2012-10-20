import logging
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from fund.decorators import approved_membership

# Create your views here.

@approved_membership() 
def Save(request):
  if request.method=='POST':
    form = models.RatingForm(request.POST)
    if form.is_valid():
      form.save()
		 
   #render_to_response('debug.html', {'form': form})


""" There are two blank templates created:
scoring/reading.html
scoring/project_summary.html

Add new ones as needed """
