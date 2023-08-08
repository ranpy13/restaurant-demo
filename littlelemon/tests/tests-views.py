from django.test import TestCase, Client
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status


class MenuViewTest(TestCase):
    def setup(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.pizza = Menu.objects.create(
            title='Pizza', price=12.99, inventory=10)
        self.burger = Menu.objects.create(
            title='Burger', price=8.99, inventory=5)
        self.pasta = Menu.objects.create(
            title='pasta', price=15.99, inventory=7)

    def test_get_all(self):
        self.loginAsTestUser()
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        self.assertEqual(response.data, serializer.data)