import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch employee information
    response_employee = requests.get(employee_url)
    employee_data = response_employee.json()
    employee_name = employee_data.get("name")

    # Fetch TODO list
    response_todo = requests.get(todo_url)
    todo_list = response_todo.json()

    # Calculate progress
    total_tasks = len(todo_list)
    completed_tasks = sum(1 for task in todo_list if task["completed"])

    # Display progress
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    for task in todo_list:
        if task["completed"]:
            print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

