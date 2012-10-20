import logging
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from fund.decorators import approved_membership
from grants import models

# Create your views here.
def read_grant(request, app_id):
    return render_to_response("scoring/reading.html", {})
#  "grant": models.GrantApplication.objects.get(pk=app_id)})
    

""" There are two blank templates created:
scoring/reading.html
scoring/project_summary.html

Add new ones as needed """
