from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse


def password_changed(request):
	messages.add_message(request, messages.INFO, 'Your password changed')
	return redirect(reverse('profile:home'))
