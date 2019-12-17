from django.shortcuts import render

from django.views.generic.edit import FormView
from .forms import FeedbackForm

# Create your views here.

class FeedbackView(FormView):
	form_class = FeedbackForm
	template_name = 'quickstart/qr.html'