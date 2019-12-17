from django.db import models

# Create your models here.

class QRCode(models.Model):
	pass

class QRZone(models.Model):
	name = models.CharField(max_length=128)
		
class FeedBack(models.Model):
	qr_id = None
	text = models.CharField(max_length=512)	
	name = models.CharField(max_length=128)
	contact = models.CharField(max_length=48)