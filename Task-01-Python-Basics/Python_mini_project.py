# Terminal Task & Goal Deadline Tracker
from datetime import datetime

def parse_date(date_str):
    """Converts a string formatted as YYYY-MM-DD to a datetime object."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None

def get_urgency_status(due_date):
    """Calculates days remaining and assigns an urgency indicator."""
    today = datetime.now().date()
    days_left = (due_date - today).days

    if days_left < 0:
        return f"OVERDUE 🔴 ({abs(days_left)} days past)"
    elif days_left <= 3:
        return f"DUE SOON 🟡 ({days_left} days left)"
    else:
        return f"ON TRACK 🟢 ({days_left} days left)"

def display_tasks(tasks):
    """Prints all recorded tasks in a clean tabular layout."""
    if not tasks:
        print("\n⚠️ No tasks found in your tracker.")
        return

    print("\n" + "=" * 70)
    print(f"{'ID':<4} | {'Task Name':<22} | {'Priority':<8} | {'Due Date':<10} | {'Status':<20}")
    print("=" * 70)

    for idx, task in enumerate(tasks, start=1):
        status = get_urgency_status(task["due_date"])
        print(f"{idx:<4} | {task['name']:<22} | {task['priority']:<8} | {task['due_date']} | {status}")
    print("=" * 70)

def main():
    task_list = []

    while True:
        print("\n📋 PERSONAL TASK & DEADLINE TRACKER")
        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. Delete a Task")
        print("4. Exit Tracker")

        choice = input("\nSelect an option (1-4): ").strip()

        if choice == "1":
            name = input("Enter Task Name: ").strip()
            if not name:
                print("❌ Task name cannot be empty.")
                continue

            priority = input("Enter Priority (High/Medium/Low): ").strip().capitalize()
            if priority not in ["High", "Medium", "Low"]:
                priority = "Medium"

            date_input = input("Enter Due Date (YYYY-MM-DD): ").strip()
            due_date = parse_date(date_input)

            if not due_date:
                print("❌ Invalid date format! Please use YYYY-MM-DD.")
                continue

            # Store task dictionary into main list
            task_list.append({
                "name": name,
                "priority": priority,
                "due_date": due_date
            })
            print(f"✅ Task '{name}' added successfully!")

        elif choice == "2":
            display_tasks(task_list)

        elif choice == "3":
            display_tasks(task_list)
            if task_list:
                try:
                    task_id = int(input("\nEnter Task ID to delete: "))
                    if 1 <= task_id <= len(task_list):
                        removed = task_list.pop(task_id - 1)
                        print(f"🗑️ Removed task: '{removed['name']}'")
                    else:
                        print("❌ Invalid Task ID.")
                except ValueError:
                    print("❌ Please enter a valid numerical ID.")

        elif choice == "4":
            print("\nExiting Task Tracker. Have a productive day!")
            break
        else:
            print("❌ Invalid selection! Please choose options 1 through 4.")

if __name__ == "__main__":
    main()