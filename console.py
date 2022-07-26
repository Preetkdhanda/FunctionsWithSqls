import pdb 
from models.task import Task
import repositories.task_repository as task_repository  

from models.User import User
import repositories.user_repository as user_repository


task_repository.delete_all()
user_repository.delete_all()

user1 = User('Jack', 'Jarvis')
user2 = User('Victor', 'McDade')

user_repository.save(user1)
user_repository.save(user2)

new_task = Task("Go for a run", user1, 20)

task_repository.save(new_task)

new_task1 = Task('Walk Dog', user1, 60)
task_repository.save(new_task1)

new_task2 = Task('Feed Cat', user2, 5)
task_repository.save(new_task2)

# task_repository.delete_one(new_task.id)

# new_task2.mark_complete()
# task_repository.update(new_task2)

result = task_repository.select_all()


for task in result:
    print(task.user.__dict__)

# # found_task = task_repository.select(new_task1.id)
# # print(found_task.__dict__)

# pdb.set_trace()