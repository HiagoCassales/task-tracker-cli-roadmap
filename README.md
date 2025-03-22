# Task Tracker CLI

## About the Project

This is a simple Task Tracker project made in Python. Since I'm a beginner, I did everything on my own, without the help of an AI, so it's very likely there are mistakes or not the most efficient ways of solving the problems.

The idea is to learn by doing, so if you find something that can be improved, let me know! I want to learn more about programming logic and best practices. 😃

## How It Works

The program allows you to add, list, update, and remove tasks directly from the terminal. The tasks are saved in a file called `db_task.json`.

Each task has:

- **id**: Unique identifier
- **description**: Task description
- **status**: Can be `todo`, `in-progress`, or `done`
- **createdAt**: Creation date
- **updatedAt**: Last update


## How to Install

1. Clone the repository:
 ```bash
   git clone https://github.com/HiagoCassales/task-tracker-cli-roadmap.git
   ```
2. Access the project directory:
 ```bash
   cd task-tracker-cli
   ```

## How to Use

The application runs directly in the terminal. Just run the script and enter the commands.

1. Add a Task:
 ```bash
   add "Buy bread"
   ```
Expected output:
 ```bash
   Task added successfully (ID: 1)
   ```

2. Update a Task:
 ```bash
   update 1 "Buy bread and milk"
   ```
Expected output:
 ```bash
   Item with (ID: 1) has been updated.
   ```

3. Delete a Task:
 ```bash
   delete 1
   ``` 
Expected output:
 ```bash
   Item with (ID: 1) has been deleted.
   ```

4. Mark a Task as "In Progress":
 ```bash
   mark-in-progress 1
   ```

5. Mark a Task as "Done":
 ```bash
   mark-done 1
   ```

6. List All Tasks:
 ```bash
   list all
   ```

7. List Tasks by Status:
 ```bash
   list todo
   list in-progress
   list done
   ```

## JSON File Structure

The tasks are stored in the db_task.json file with the following format:

 ```bash
[
  {
    "id": 1,
    "description": "Buy bread",
    "status": "todo",
    "createdAt": "2025-03-22 14:00:00",
    "updatedAt": "2025-03-22 14:00:00"
  }
]
   ```
   
## Contributing

If you found any errors, have suggestions, or want to discuss better ways to do something, feel free to jump in! The focus here is learning, so any feedback is welcome. 😃

Open an issue or create a pull request, and I’ll review it and learn from the suggestions.

Thanks for checking out the project! 🚀