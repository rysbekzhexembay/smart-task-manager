from datetime import datetime
from storage import load_tasks, save_tasks

def add_task(title, description, deadline_str):
    tasks = load_tasks()
    
    # Умная генерация ID: ищем максимальный ID и прибавляем 1. Если список пуст — ID = 1.
    task_id = max([t["id"] for t in tasks]) + 1 if tasks else 1
    
    new_task = {
        "id": task_id,
        "title": title,
        "description": description,
        "deadline": deadline_str,
        "status": "To Do"
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return task_id

def get_all_tasks():
    return load_tasks()

def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Done"
            save_tasks(tasks)
            return True
    return False

def delete_task(task_id):
    """Удаляет задачу по её ID."""
    tasks = load_tasks()
    initial_count = len(tasks)
    
    # Фильтруем список, оставляя все задачи, кроме удаляемой
    tasks = [task for task in tasks if task["id"] != task_id]
    
    # Если размер списка уменьшился, значит задача была найдена и удалена
    if len(tasks) < initial_count:
        save_tasks(tasks)
        return True
    return False

def get_urgent_tasks():
    tasks = load_tasks()
    urgent = []
    today = datetime.today().date()
    
    for task in tasks:
        if task["status"] != "Done":
            try:
                task_date = datetime.strptime(task["deadline"], "%Y-%m-%d").date()
                if task_date <= today:
                    urgent.append(task)
            except ValueError:
                continue
    return urgent