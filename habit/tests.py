from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habit.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="test@test.com",
            password="testpassword"
        )
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            creator=self.user,
            place="Shop",
            time="18:00:00",
            action="Go shopping"
        )

    def test_create_habit(self):
        url = reverse("habit:habit_create")
        data = {
            "creator": self.user.pk,
            "place": "Shop",
            "time": "18:00:00",
            "action": "Go shopping"
        }

        response = self.client.post(url, data=data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data.get("creator"), self.user.pk)
        self.assertEqual(data.get("place"), "Shop")
        self.assertEqual(data.get("time"), "18:00:00")
        self.assertEqual(data.get("action"), "Go shopping")

    def test_list_habit(self):
        response = self.client.get(reverse('habit:habit_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_habit(self):
        url = reverse("habit:habit_update", args=(self.habit.pk,))
        data = {
            "creator": self.user.pk,
            "place": "Gym",
            "time": "19:00:00",
            "action": "Training",
        }
        response = self.client.put(url, data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("creator"), self.habit.owner.id)
        self.assertEqual(data.get("place"), "Gym")
        self.assertEqual(data.get("time"), "19:00:00")
        self.assertEqual(data.get("action"), "Training")

    def test_delete_habit(self):
        url = reverse("habit:habit_delete", args=(self.habit.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
