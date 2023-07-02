from django.urls import path
from message.views import HomeView, CreateContact, UpdateContact, DeleteContact, SendMessage

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/edit/<int:pk>/', UpdateContact.as_view(), name='edit_contact'),
    path('contact/delete/<int:pk>/', DeleteContact.as_view(), name='delete_contact'),
    path('contact/new/', CreateContact.as_view(), name='contact_new'),
    path('send_message/', SendMessage, name='send_message'),
]
