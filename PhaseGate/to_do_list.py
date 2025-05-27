tasks= []
def display_interface():
	print("""
	To- Do List Manager
	1. Add a Task
	2. View Tasks
	3. Mark task as completer
	4. Delete Task
	5. Exit
	""")

def add_task(task):
	new_task = task
	tasks.append(task)
def view_all_tasks(tasks):
	return tasks
def delete_task(task_number):
	delete_task = int(task_number - 1)
	del(tasks[delete_task])
def mark_as_complete(task_number):
	task_int = int(task_number - 1)
	marked_task = tasks[task_int]+"[X]"
	tasks.append(marked_task)
	delete_task(task_number)
	
	