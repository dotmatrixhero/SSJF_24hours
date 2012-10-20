from django.db import models
from django.forms import ModelForm
from grants.models import GrantApplication
from fund.models import Membership

"""Early sketch of a model & modelform for an individual rating.  Feel free to modify or start from scratch"""
    
class ApplicationRating(models.Model):

  application = models.ForeignKey(GrantApplication)
  membership = models.ForeignKey(Membership)
  submitted = models.BooleanField(default=False)

  
  RATING_CHOICES = (
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
  )
  program = models.PositiveIntegerField(choices=RATING_CHOICES, null=True, blank=True)
  diversity = models.PositiveIntegerField(choices=RATING_CHOICES, null=True, blank=True)
  soundness = models.PositiveIntegerField(choices=RATING_CHOICES, null=True, blank=True)
  lack_of_access = models.PositiveIntegerField(choices=RATING_CHOICES, null=True, blank=True)
  collaboration = models.PositiveIntegerField(choices=RATING_CHOICES, null=True, blank=True)
  
  submission_time = models.DateTimeField(auto_now_add=True)
  def __unicode__(self):
	return ("Program" + self.program + "\nDiversity" + self.diversity + "\nSoundness" + self.soundness + "\nLack of Access" + self.lack_of_access + "\nCollaboration" + self.collaboration) 
  def total(self):
	if scoring_bonus_poc or scoring_bonus_geo:
		return (1.1*self.program*7+self.diversity*5+self.soundness*4+self.lack_of_access*2+self.collaboration*2)
	
	return (self.program*7+self.diversity*5+self.soundness*4+self.lack_of_access*2+self.collaboration*2)

class RatingForm(ModelForm):
  class Meta:
    model = ApplicationRating
    exclude = ('submission_time')
    
    
