import to_do_list
import unittest

class TestToDoList(unittest.TestCase):
	def setUp(self):
		to_do_list.tasks.clear()
	def test_that_add_task_function_exist(self):
		to_do_list.add_task("Buy groceries")
	def test_that_add_task_function_works(self):
		to_do_list.add_task("Buy groceries")
		to_do_list.add_task("Buy meat")
		self.assertListEqual(["Buy groceries","Buy meat"], to_do_list.view_all_tasks(to_do_list.tasks)) 
	def test_that_function_view_all_tasks_exits(self):
		to_do_list.view_all_tasks(to_do_list.tasks)
	def test_that_function_view_all_tasks_works(self):
		to_do_list.view_all_tasks(to_do_list.tasks)
		to_do_list.add_task("Sleep")
		to_do_list.add_task("Read")
		self.assertListEqual(["Sleep","Read"], to_do_list.view_all_tasks(to_do_list.tasks))
	def test_view_all_task_returns_tasks_in_order(self):
		to_do_list.view_all_tasks(to_do_list.tasks)
		to_do_list.add_task("Sleep")
		to_do_list.add_task("Read")
		self.assertListEqual(["Sleep","Read"], to_do_list.view_all_tasks(to_do_list.tasks))
	def test_delete_function_exist(self):
		to_do_list.add_task("Sleep")
		to_do_list.add_task("Read")
		to_do_list.add_task("Buy groceries")
		to_do_list.delete_task(1)
	def test_delete_function_works(self):
		to_do_list.add_task("Sleep")
		to_do_list.add_task("Read")
		to_do_list.add_task("Buy groceries")
		to_do_list.add_task("Buy meat")
		to_do_list.delete_task(1)
		self.assertListEqual(["Read", "Buy groceries", "Buy meat"], to_do_list.view_all_tasks(to_do_list.tasks))
	def test_mark_as_complete_exists(self):
		to_do_list.add_task("Sleep")
		to_do_list.mark_as_complete(1)
	def test_mark_as_complete_works(self):		
		to_do_list.add_task("Sleep")
		to_do_list.add_task("Read")
		to_do_list.mark_as_complete(1)
		self.assertListEqual(["Read","Sleep[X]"], to_do_list.view_all_tasks(to_do_list.tasks))









		

		