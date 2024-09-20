from rest_framework.serializers import ValidationError
from datetime import timedelta


class NotCombinationValidator:

    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, habit):
        if habit.get("connection_habit") and habit.get("reward"):
            raise ValidationError(
                "You can't choose a habit and a reward at the same time"
            )


class TimeDurationValidator:
    duration_time = timedelta(seconds=120)

    def __init__(self, field_1):
        self.field_1 = field_1

    def __call__(self, habit):
        if habit.get("duration") and habit.get("duration") > 120:
            raise ValidationError("Duration is more than 2 minutes!")


class CombinationValidator:

    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, habit):
        if habit.get("connection_habit"):
            if not habit.get("habit_is_pleasant"):
                raise ValidationError("Connected habits can be only pleasant")


class AbsenceValidator:

    def __init__(self, field_1, field_2, field_3):
        self.field_1 = field_1
        self.field_2 = field_2
        self.field_3 = field_3

    def __call__(self, habit):
        if habit.get("habit_is_pleasant"):
            if habit.get("connection_habit") or habit.get("reward"):
                raise ValidationError(
                    "Pleasant habit can't have a connected habit or a reward"
                )


class FrequencyValidator:

    def __init__(self, field_1):
        self.field_1 = field_1

    def __call__(self, habit):
        number_list = [1, 2, 3, 4, 5, 6, 7]
        num = habit.get("number_of_executions")
        try:
            num in number_list
        except ValidationError:
            print("Habit can't be done less than 1 time and more than 7 times a week")
