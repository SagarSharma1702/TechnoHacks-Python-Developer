''Task 7 : To-do list
Create a program that allows the user to
create and manage a to-do list.'''
class ToDoList:
  def __init__(self):
      self.tasks = []

  def add_task(self, task):
      self.tasks.append(task)
      print(f"Task '{task}' added to the to-do list.")

  def view_tasks(self):
      if not self.tasks:
          print("No tasks in the to-do list.")
      else:
          print("\nTo-Do List:")
          for index, task in enumerate(self.tasks, start=1):
              print(f"{index}. {task}")

  def remove_task(self, task_index):
      if 1 <= task_index <= len(self.tasks):
          removed_task = self.tasks.pop(task_index - 1)
          print(f"Task '{removed_task}' removed from the to-do list.")
      else:
          print("Invalid task index. Please enter a valid index.")

def todo_list_manager():
  todo_list = ToDoList()

  while True:
      print("\nTo-Do List Manager")
      print("1. Add Task")
      print("2. View Tasks")
      print("3. Remove Task")
      print("4. Exit")

      choice = input("Enter your choice (1-4): ")

      if choice == '1':
          task = input("Enter the task: ")
          todo_list.add_task(task)
      elif choice == '2':
          todo_list.view_tasks()
      elif choice == '3':
          todo_list.view_tasks()
          task_index = int(input("Enter the index of the task to remove: "))
          todo_list.remove_task(task_index)
      elif choice == '4':
          print("Thank you for using the To-Do List Manager. Have a great day!")
          break
      else:
          print("Invalid choice. Please enter a number between 1 and 4.")

# Call the todo_list_manager function to start the to-do list management
todo_list_manager()

