import logging
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from fund.decorators import approved_membership
from django.shortcuts import get_object_or_404, redirect
import grants.models
import models

# Create your views here.


@login_required(login_url='/fund/login/')
@approved_membership()
def read_grant(request, app_id):
  #application = get_object_or_404(grants.models.GrantApplication, pk = app_id)
  #form = models.RatingForm(initial={'application': application})
  membership = request.membership
  form = models.RatingForm(initial={'membership': membership})
  return render_to_response("scoring/reading.html", {'form': form})
#  "grant": models.GrantApplication.objects.get(pk=app_id)})
    


@login_required(login_url='/fund/login/')
@approved_membership() 
def Save(request):
  logging.info("first")
  if request.method=='POST':
    form = models.RatingForm(request.POST)
    if form.is_valid():
      logging.info(form.errors == False)
      if not request.is_ajax():
        form.submitted = True
        return redirect('/org/nr')
      try:
        form.save()
      except Exception, e:
        logging.info(e)



  
  return HttpResponse("")



""" There are two blank templates created:
scoring/reading.html
scoring/project_summary.html

Add new ones as needed """
