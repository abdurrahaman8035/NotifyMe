from django.test import TestCase, Client
from django.shortcuts import reverse
from django.contrib.auth.models import User
from utils.send_sms import send_sms
from message.models import Contact


class TestViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_user(username="testuser", password="testpass")
        cls.contact = Contact.objects.create(
            name="Test User", phone_number="08012324568", id_number="U/CS/01/005"
        )

    def test_home_view(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_create_contact_view(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(
            reverse("contact_new"),
            {
                "name": "Test User",
                "phone_number": "08012324568",
                "id_number": "U/CS/01/005",
            },
        )
        self.assertEqual(Contact.objects.get(id=1).name, "Test User")
        self.assertEqual(response.status_code, 302)

    def test_update_contact_view(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(
            reverse("edit_contact", args=[self.contact.id]),
            {
                "name": "Updated Name",
                "phone_number": "08012324568",
                "id_number": "U/CS/01/005",
            },
        )
        self.assertEqual(Contact.objects.get(id=1).name, "Updated Name")
        self.assertEqual(response.status_code, 302)

    def test_delete_contact_view(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(reverse("delete_contact", args=[self.contact.id]))
        self.assertEqual(response.status_code, 302)

    def test_send_message_view(self):
        message = "Hello, Students. This is to inform you that the examinations Time Table is out."
        response = send_sms(message=message)
        self.assertEqual(response, "Sent")
