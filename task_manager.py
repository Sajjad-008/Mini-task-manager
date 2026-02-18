import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title})
    save_tasks(tasks)


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task['title']}")


def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
    else:
        print("Invalid task number.")


def count_tasks():
    tasks = load_tasks()
    print(f"Total tasks: {len(tasks)}")