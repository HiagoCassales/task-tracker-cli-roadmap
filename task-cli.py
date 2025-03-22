import json, datetime, re

def open_json():
    try: 
        with open("db_task.json", 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
task = open_json()


def write_json(task):
    with open("db_task.json", "w", encoding="utf-8") as file:
        return json.dump(task, file, ensure_ascii=False, indent=4)
    

def add_new_task(item):
    new_id = max([int(task_item["id"]) for task_item in task], default=0) + 1

    new_task = {
        "id": new_id,
        "description": item,
        "status": "todo",
        "createdAt": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updatedAt": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    task.append(new_task)
    write_json(task)

    print(f"Task added successfully (ID: {new_task['id']})")


def delete_task(task_id):
    for item in task:
        if item["id"] == int(task_id[0]):
            task.remove(item)

    write_json(task)
    print(f"Item with (ID: {item['id']}) has been deleted.")


def update_description_task(item, task_id):
    for update_item in task:
        if update_item["id"] == int(task_id[0]):
            update_item['description'], update_item['updatedAt'] = item, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    write_json(task)
    print(f"Item with (ID: {update_item['id']}) has been updated.")


def update_status_task(status, task_id):
    for item in task:
        if item["id"] == int(task_id[0]):
            item['status'], item['updatedAt'] = status, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    write_json(task)
    print(f"Item with (ID: {item['id']}) has been updated with a new status.")


def main():
    while True:
        command = input("CLI-Task-Tracker-Roadmap: ").lower()

        if command == "exit":
            break

        item = re.findall(r'"(.*?)"', command)
        task_id = re.findall(r"(\d+)", command)

        if 'add' in command:
            if len(item) == 1:
                add_new_task(item[0])
            else:
                if len(item) == 0:
                    print("Error: The item is empty.")
                else:
                    print("Error: Only one item should be provided.")

        elif 'delete' in command:
            if len(task_id) == 1:
                delete_task(task_id)
            else:
                if len(task_id) == 0:
                    print("Error: The item is empty.")
                else:
                    print("Error: Only one id should be provided.")

        elif 'update' in command:
            if len(item) == 1 and len(task_id) == 1:
                update_description_task(item[0], task_id)
            else:
                if len(item) == 0 and len(task_id) == 0 or len(item) == 0 or len(task_id) == 0:
                    print("Error: The item is empty.")
                else:
                    print("Error: Only one id/item should be provided.")
        
        elif 'mark-in-progress' in command:
            if len(task_id) == 1:
                update_status_task('in-progress', task_id)
            else:
                if len(task_id) == 0:
                    print("Error: The item is empty.")
                else:
                    print("Error: Only one id should be provided.")
        elif 'mark-done' in command:
            if len(task_id) == 1:
                update_status_task('done', task_id)
            else:
                if len(task_id) == 0:
                    print("Error: The item is empty.")
                else:
                    print("Error: Only one id should be provided.")

        elif 'list all' in command:
            header = ["ID", "Description", "Status", "Creation date", "Update date"]
            print(f"{header[0]:<5} | {header[1]:<40} | {header[2]:<15} | {header[3]:<20} | {header[4]:<20}")
            print("-" * 120)
            for item in task:
                print(f"{item['id']:<5} | {item['description']:<40} | {item['status']:<15} | {item['createdAt']:<20} | {item['updatedAt']:<20}")
            print("-" * 120)

        elif 'list todo' in command:
            header = ["ID", "Description", "Status", "Creation date", "Update date"]
            print(f"{header[0]:<5} | {header[1]:<40} | {header[2]:<15} | {header[3]:<20} | {header[4]:<20}")
            print("-" * 120)
            for item in task:
                if item["status"] == "todo":
                    print(f"{item['id']:<5} | {item['description']:<40} | {item['status']:<15} | {item['createdAt']:<20} | {item['updatedAt']:<20}")
            print("-" * 120)

        elif 'list done' in command:
            header = ["ID", "Description", "Status", "Creation date", "Update date"]
            print(f"{header[0]:<5} | {header[1]:<40} | {header[2]:<15} | {header[3]:<20} | {header[4]:<20}")
            print("-" * 120)
            for item in task:
                if item["status"] == "done":
                    print(f"{item['id']:<5} | {item['description']:<40} | {item['status']:<15} | {item['createdAt']:<20} | {item['updatedAt']:<20}")
            print("-" * 120)

        elif 'list in-progress' in command:
            header = ["ID", "Description", "Status", "Creation date", "Update date"]
            print(f"{header[0]:<5} | {header[1]:<40} | {header[2]:<15} | {header[3]:<20} | {header[4]:<20}")
            print("-" * 120)
            for item in task:
                if item["status"] == "in-progress":
                    print(f"{item['id']:<5} | {item['description']:<40} | {item['status']:<15} | {item['createdAt']:<20} | {item['updatedAt']:<20}")
            print("-" * 120)
        else:
            print("Enter a valid command")
main()   
