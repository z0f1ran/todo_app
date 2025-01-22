from .task_manager import TaskManager

def main():
    manager = TaskManager()
    
    while True:
        print("\n=== Менеджер задач ===")
        print("1. Добавить задачу")
        print("2. Добавить категорию")
        print("3. Добавить подзадачу")
        print("4. Показать все задачи")
        print("5. Показать задачи по категории")
        print("6. Показать все категории")
        print("7. Отметить задачу как выполненную")
        print("8. Удалить задачу")
        print("9. Добавить тег к задаче")
        print("10. Найти задачи по тегу")
        print("0. Выйти")
        
        choice = input("\nВыберите действие: ")
        
        if choice == "1":
            title = input("Введите название задачи: ")
            priority = input("Введите приоритет (high/normal/low): ")
            print("\nДоступные категории:")
            print(manager.list_categories())
            category_name = input("Введите название категории (или Enter для пропуска): ")
            
            category = next((c for c in manager.categories if c.name == category_name), None)
            task = manager.add_task(title, priority, category)
            print("Задача добавлена!")
            
        elif choice == "2":
            name = input("Введите название категории: ")
            description = input("Введите описание категории: ")
            manager.add_category(name, description)
            print("Категория добавлена!")
            
        elif choice == "3":
            if not manager.tasks:
                print("Сначала создайте основную задачу!")
                continue
                
            print("\nСписок задач:")
            print(manager.list_tasks())
            parent_index = int(input("Введите номер родительской задачи: ")) - 1
            
            if 0 <= parent_index < len(manager.tasks):
                title = input("Введите название подзадачи: ")
                priority = input("Введите приоритет (high/normal/low): ")
                manager.add_subtask(manager.tasks[parent_index], title, priority)
                print("Подзадача добавлена!")
            else:
                print("Неверный номер задачи!")
                
        elif choice == "4":
            print("\nСписок всех задач:")
            print(manager.list_tasks())
            
        elif choice == "5":
            print("\nДоступные категории:")
            print(manager.list_categories())
            category_name = input("Введите название категории: ")
            category = next((c for c in manager.categories if c.name == category_name), None)
            if category:
                print(f"\nЗадачи в категории {category.name}:")
                print(manager.list_tasks(category))
            else:
                print("Категория не найдена!")
                
        elif choice == "6":
            print("\nСписок категорий:")
            print(manager.list_categories())
            
        elif choice == "7":
            index = int(input("Введите номер задачи: ")) - 1
            if manager.complete_task(index):
                print("Задача отмечена как выполненная!")
            else:
                print("Неверный номер задачи!")
                
        elif choice == "8":
            index = int(input("Введите номер задачи: ")) - 1
            if manager.remove_task(index):
                print("Задача удалена!")
            else:
                print("Неверный номер задачи!")
                
        elif choice == "9":
            print("\nСписок задач:")
            print(manager.list_tasks())
            index = int(input("Введите номер задачи: ")) - 1
            if 0 <= index < len(manager.tasks):
                tag = input("Введите тег: ")
                manager.tasks[index].add_tag(tag)
                print("Тег добавлен!")
            else:
                print("Неверный номер задачи!")
                
        elif choice == "10":
            tag = input("Введите тег для поиска: ")
            tasks = manager.find_tasks_by_tag(tag)
            if tasks:
                print(f"\nЗадачи с тегом '{tag}':")
                for task in tasks:
                    print(str(task))
            else:
                print(f"Задачи с тегом '{tag}' не найдены!")
                
        elif choice == "0":
            break

if __name__ == "__main__":
    main() 