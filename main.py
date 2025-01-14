from task_manager import TaskManager

def main():
    manager = TaskManager()
    
    while True:
        print("\n1. Добавить задачу")
        print("2. Показать все задачи")
        print("3. Отметить задачу как выполненную")
        print("4. Удалить задачу")
        print("5. Выйти")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            title = input("Введите название задачи: ")
            priority = input("Введите приоритет (high/normal/low): ")
            manager.add_task(title, priority)
            print("Задача добавлена!")
            
        elif choice == "2":
            print("\nСписок задач:")
            print(manager.list_tasks())
            
        elif choice == "3":
            index = int(input("Введите номер задачи: ")) - 1
            if manager.complete_task(index):
                print("Задача отмечена как выполненная!")
            else:
                print("Неверный номер задачи!")
                
        elif choice == "4":
            index = int(input("Введите номер задачи: ")) - 1
            if manager.remove_task(index):
                print("Задача удалена!")
            else:
                print("Неверный номер задачи!")
                
        elif choice == "5":
            break

if __name__ == "__main__":
    main() 