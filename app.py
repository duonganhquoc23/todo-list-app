# Danh sách để lưu các công việc
tasks = []

def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append(task_name)
    print(f"Đã thêm công việc: '{task_name}'")

# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")

def list_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{i}. {status} {task['name']}")


if __name__ == "__main__":
    tasks = [
    {"name": "Học bài Git", "completed": False},
    {"name": "Làm bài tập", "completed": False}
]
    list_tasks(tasks)

def add_task(tasks, name):
    tasks.append({
        "name": name,
        "completed": False
    })

def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
    else:
        print("Chỉ số không hợp lệ.")

if __name__ == "__main__":
    tasks = []
    add_task(tasks, "Học bài Git")
    add_task(tasks, "Làm bài tập")
    complete_task(tasks, 0)
    list_tasks(tasks)
