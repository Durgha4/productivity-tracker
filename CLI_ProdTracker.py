import mysql.connector
from datetime import datetime, timedelta

CATEGORY_LIST = ['Work', 'Study', 'Break']

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Durgha@04",
        database="productivity_tracker"
    )

def add_task(task_name, description, category):
    if category not in CATEGORY_LIST:
        print("Invalid category. Using 'Work' as default.")
        category = 'Work'
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task_name, description, category, start_time) VALUES (%s, %s, %s, %s)",
                   (task_name, description, category, datetime.now()))
    conn.commit()
    print("Task added and started.")
    cursor.close()
    conn.close()

def end_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET end_time = %s WHERE task_id = %s",
                   (datetime.now(), task_id))
    conn.commit()
    print("Task ended.")
    cursor.close()
    conn.close()

def list_tasks():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT task_id, task_name, category, start_time, end_time FROM tasks")
    rows = cursor.fetchall()
    print("\nTasks:")
    for row in rows:
        print(row)
    cursor.close()
    conn.close()

def show_report():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT category, TIMESTAMPDIFF(MINUTE, start_time, IFNULL(end_time, NOW())) as duration FROM tasks")
    durations = {}
    for category, minutes in cursor.fetchall():
        durations[category] = durations.get(category, 0) + minutes
    print("\n🧾 Category-wise Time Report:")
    for category, minutes in durations.items():
        print(f"{category}: {minutes // 60}h {minutes % 60}m")
    cursor.close()
    conn.close()

def notify_long_tasks():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT task_name, start_time FROM tasks WHERE end_time IS NULL")
    for task_name, start_time in cursor.fetchall():
        elapsed = datetime.now() - start_time
        if elapsed > timedelta(hours=2):
            print(f"⏰ ALERT: '{task_name}' has been running for over 2 hours!")
    cursor.close()
    conn.close()

def main():
    while True:
        print("\n📋 Productivity Tracker")
        print("1. Add Task")
        print("2. End Task")
        print("3. View All Tasks")
        print("4. Generate Report")
        print("5. Notify Long Running Tasks")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            name = input("Task name: ")
            desc = input("Description: ")
            category = input("Category (Work/Study/Break): ")
            add_task(name, desc, category)
        elif choice == '2':
            task_id = input("Enter task ID to end: ")
            end_task(task_id)
        elif choice == '3':
            list_tasks()
        elif choice == '4':
            show_report()
        elif choice == '5':
            notify_long_tasks()
        elif choice == '6':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
