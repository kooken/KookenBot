from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from habit.models import Habit
from habit.paginations import CustomPagination
from habit.permissions import IsCreator
from habit.serializers import HabitSerializer


class HabitListApiView(ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Habit.objects.all()
        elif user.is_authenticated:
            return Habit.objects.filter(creator=user)


class HabitIsPublishedListApiView(ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Habit.objects.filter(is_published=True)


class HabitCreateApiView(CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.creator = self.request.user
        new_habit.save()


class HabitUpdateApiView(UpdateAPIView):
    serializer_class = HabitSerializer
    permission_classes = (
        IsAuthenticated,
        IsCreator,
    )

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Habit.objects.filter(creator=user)


class HabitDestroyApiView(DestroyAPIView):
    permission_classes = (IsCreator,)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Habit.objects.filter(creator=user)
