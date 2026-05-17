import logic

def print_menu():
    print("\n=== Task Manager CLI ===")
    print("1. Посмотреть все задачи")
    print("2. Добавить новую задачу")
    print("3. Отметить задачу как выполненную")
    print("4. Показать горящие задачи (Дедлайн <= сегодня)")
    print("5. Удалить задачу")
    print("6. Выход")

def main():
    while True:
        print_menu()
        choice = input("Выберите действие (1-6): ")

        if choice == '1':
            tasks = logic.get_all_tasks()
            if not tasks:
                print("\nСписок задач пуст.")
            else:
                print("\n--- Ваши задачи ---")
                for t in tasks:
                    status = "[x]" if t["status"] == "Done" else "[ ]"
                    print(f"{t['id']}. {status} {t['title']} (Дедлайн: {t['deadline']})")
        
        elif choice == '2':
            title = input("Название задачи: ")
            desc = input("Описание: ")
            deadline = input("Дедлайн (в формате YYYY-MM-DD): ")
            t_id = logic.add_task(title, desc, deadline)
            print(f"\nЗадача '{title}' успешно добавлена с ID {t_id}!")
            
        elif choice == '3':
            try:
                task_id = int(input("Введите ID задачи для завершения: "))
                if logic.complete_task(task_id):
                    print(f"\nЗадача {task_id} отмечена как выполненная!")
                else:
                    print(f"\nЗадача с ID {task_id} не найдена.")
            except ValueError:
                print("\nОшибка: ID должен быть числом.")
                
        elif choice == '4':
            urgent = logic.get_urgent_tasks()
            if not urgent:
                print("\nГорящих задач нет! Можно отдыхать.")
            else:
                print("\n--- ГОРЯЩИЕ ЗАДАЧИ ---")
                for t in urgent:
                    print(f"!!! {t['id']}. {t['title']} (Дедлайн: {t['deadline']})")
                    
        elif choice == '5':
            try:
                task_id = int(input("Введите ID задачи для удаления: "))
                if logic.delete_task(task_id):
                    print(f"\nЗадача с ID {task_id} успешно удалена!")
                else:
                    print(f"\nЗадача с ID {task_id} не найдена.")
            except ValueError:
                print("\nОшибка: ID должен быть числом.")
                    
        elif choice == '6':
            print("\nВыход из программы.")
            break
        else:
            print("\nНеверный ввод. Пожалуйста, выберите от 1 до 6.")

if __name__ == "__main__":
    main()