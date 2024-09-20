import requests
from config.settings import TELEGRAM_TOKEN, TELEGRAM_URL
from habit.models import Habit


def message_create(habit_id):
    habit = Habit.objects.get(id=habit_id)
    user = habit.creator
    name = name_of_user(user.email)

    time = habit.time
    if habit.place is None:
        place = "Любое место"
    else:
        place = habit.place

    action = habit.action

    if habit.connection_habit_id:
        message = (f"Hello {name}! It's time {time}! You need to do {action},"
                   f" at {place},"
                   f" You can also do {Habit.objects.get(id=habit.connection_habit_id).action}!")
    elif habit.reward:
        message = (f"Hello {name}! It's time {time}! You need to do {action},"
                   f" at {place}, and you will get {habit.reward}!")
    else:
        message = (f"Hello {name}! It's time {time}! You need to do {action},"
                   f" at{place}.")

    return message


def send_tg(chat_id, message):
    params = {
        "text": message,
        "chat_id": chat_id,
    }
    requests.post(f"{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage", params=params)


def name_of_user(email):
    name = ""
    for letter in email:
        if letter != "@":
            name += letter
        else:
            break
    return name
