import logging
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from fund.decorators import approved_membership
<<<<<<< HEAD
from django.shortcuts import get_object_or_404, redirect
import grants.models
import models
=======
import grants.models
import fund.models 
from django.shortcuts import get_object_or_404
>>>>>>> b0eb629c4343099c7e4beaa097de99a78982b60a

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
def specific_project_admin(request, project_id):
	
	project = get_object_or_404(GivingProject, pk = project_id)
	project_app_list = grants.models.GrantApplication.objects.filter(grant_cycle = project.grant_cycle)
	total_ratings = models.ApplicationRating.objects.filter(membership__giving_project = project, submitted=True)
	dict = {}
	for rating in total_ratings:
		if dict[rating.application]:
			dict[rating.application].append(rating)
		else:
			dict[rating.application]=[]
			dict[rating.application].append(rating)
	return render_to_response("scoring/project_summary.html", {"app_list":project_app_list, "dict":dict })
	
@login_required(login_url='/fund/login/')
def all_giving_projects(request):
	all_giving_projects = fund.models.GivingProject.objects.all()
	return render_to_response("scoring/single_giving_project.html", {"projects":all_giving_projects})
	
	
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
