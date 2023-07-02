from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Contact


class HomeView(TemplateView):
    """Display the HomePage"""

    contacts = Contact.objects.all()
    extra_context = {"contacts": contacts}


class CreateContact(CreateView):
    """Create a new Contact"""

    model = Contact
    fields = ["name", "phone_number", "id_number"]
    template_name = "create_contact.html"


class UpdateContact(UpdateView):
    """Update an existing contact"""

    model = Contact
    fields = "__all__"
    template_name = "update_contact.html"
    context_object_name = "contact"


class DeleteContact(DeleteView):
    """Delete an existing contact"""

    model = Contact
    template_name = "delete_contact.html"
    success_url = reverse_lazy("home")
    context_object_name = "contact"
