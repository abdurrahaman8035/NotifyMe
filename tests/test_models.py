from django.test import TestCase, Client
from django.shortcuts import reverse
from django.contrib.auth.models import User
from message.models import Contact


class ContactModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.contact = Contact.objects.create(
            name="Test User",
            phone_number="08012324568",
            id_number="U/CS/01/005",
        )
        cls.user = User.objects.create_user(username="testuser", password="testpass")

    def test_get_absolute_url(self):
        self.client.login(username="testuser", password="testpass")
        expected_url = reverse("home")
        self.assertEqual(self.contact.get_absolute_url(), expected_url)
        self.assertEqual(Contact.objects.get(id=1).name, "Test User")

        response = self.client.get(reverse("home"))
        self.assertContains(response, self.contact.name)
