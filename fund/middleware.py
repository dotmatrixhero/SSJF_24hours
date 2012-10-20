from fund import models
import logging

#sets request.membership, request.membership_status
class MembershipMiddleware(object):

  #checks
  # member exists
  # membership exists (try to find one that does)
  # membership is approved (try to find one that is)
  
  #changes to member.current
  # if member had no membership for that proj (approved or not)
  #  -> first membership in query, 0 if no memberships exist
  # if current is not approved, but 1+ other membershipsj are
  #  -> first approved membership in query
  
  #resulting request vars
  # .membership_status=
  #   0 = no member object
  #   1 = no membership objects assoc w/member
  #   2 = no approved memberships
  #   3 = approved :) (current was, or current was changed -> is now)
  # .member - present in 1-3
  # .membership - present in 2-3
  
  def process_view(self, request, view_func, view_args, view_kwargs):
    #if view_func.__module__.startswith('fund') or view_func.__module__.startswith('scoring'):
    if request.user.is_authenticated():
    request.membership_status=0
    request.membership=none
    
    try:
      member = models.member.objects.get(email=request.user.username)
    except models.member.doesnotexist: #no member object
      logging.warning('custom middleware: no member object with email of '+request.user.username)
      return none
    
    try:
      membership = models.membership.objects.get(member = member, pk=member.current)
      request.membership_status=3
      request.membership = membership
    except models.membership.doesnotexist: #current is wrong
      all = member.membership_set.all()
      if all: #if 1+ memberships, update current & set ship var
      logging.warning('custom middleware: current was wrong even though memberships exist')
      request.membership_status=3
      request.membership = all[0] ###
      membership = all[0]
      member.current=membership.pk
      member.save()
      else: #no memberships
      member.current=0
      member.save()
      request.membership_status=1
      return none
    
    #membership exists, status is 3      
    if membership.approved==false: #current not approved
      ships = member.membership_set.filter(approved=true)
      if ships: #switch default to their first approved gp
      request.membership_status = 3
      request.membership = ships[0]
      member.current=membership.pk
      member.save()
      else: #no approved gps
      request.membership_status = 2        
    return none