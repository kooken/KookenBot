from django.db import models
from datetime import timedelta
from config.settings import AUTH_USER_MODEL


class Habit(models.Model):
    creator = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Creator",
    )
    place = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Location"
    )
    time = models.TimeField(blank=True, null=True, verbose_name="Time")
    action = models.CharField(max_length=100, verbose_name="Action")
    habit_is_pleasant = models.BooleanField(
        default=True, verbose_name="Good habit"
    )
    connection_habit = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Connected habit",
    )
    number_of_executions = models.IntegerField(
        default=1, verbose_name="Number of actions per week"
    )
    duration = models.DurationField(
        default=timedelta(seconds=120), verbose_name="Duration of habit"
    )
    is_published = models.BooleanField(default=True, verbose_name="Is habit published")
    reward = models.CharField(
        max_length=100, verbose_name="Reward", blank=True, null=True
    )

    def __str__(self):
        return f"{self.action}{self.creator}"

    class Meta:
        verbose_name = "Habit"
        verbose_name_plural = "Habits"
