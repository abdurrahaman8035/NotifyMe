from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from utils.send_sms import send_sms
from .models import Contact


class HomeView(TemplateView):
    """Display the HomePage"""

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contact.objects.all()
        return context


class CreateContact(CreateView):
    """Create a new Contact"""

    model = Contact
    fields = ["name", "phone_number", "id_number"]
    template_name = "create_contact.html"

    def get_success_url(self):
        return reverse_lazy("home")


class UpdateContact(UpdateView):
    """Update an existing contact"""

    model = Contact
    fields = "__all__"
    template_name = "update_contact.html"
    context_object_name = "contact"
    success_url = reverse_lazy("home")


class DeleteContact(DeleteView):
    """Delete an existing contact"""

    model = Contact
    template_name = "delete_contact.html"
    success_url = reverse_lazy("home")
    context_object_name = "contact"

def SendMessage(request):
    """Send SMS to Recipients Contacts"""
    if request.method == 'POST':
        # Get the message
        message = request.POST['message']
        # Send the message
        send_sms(message)
        return redirect("home")
    else:
        return redirect("home")
