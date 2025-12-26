from models import User, Group
from expense_manager import ExpenseManager

manager = ExpenseManager()
user_id_counter = 1
group_id_counter = 1
user_name_to_id = {}

print("Expense Sharing App (type HELP)")

while True:
    command = input("\n> ").strip()

    if command == "EXIT":
        break

    if command == "HELP":
        print("""
Commands:
ADD_USER <name>
ADD_GROUP <group_name> <user1> <user2> ...
ADD_EQUAL <group_name> <paid_by> <amount>
SHOW_BALANCES
EXIT
""")

    elif command.startswith("ADD_USER"):
        _, name = command.split()
        user = User(user_id_counter, name)
        manager.add_user(user)
        user_name_to_id[name] = user_id_counter
        user_id_counter += 1
        print(f"User {name} added")

    elif command.startswith("ADD_GROUP"):
        parts = command.split()
        group_name = parts[1]
        users = [user_name_to_id[u] for u in parts[2:]]
        group = Group(group_id_counter, group_name, users)
        manager.add_group(group)
        group_id_counter += 1
        print(f"Group {group_name} created")

    elif command.startswith("ADD_EQUAL"):
        parts = command.split()
        group_name = parts[1]
        paid_by = user_name_to_id[parts[2]]
        amount = float(parts[3])

        group = next(g for g in manager.groups.values() if g.name == group_name)
        manager.add_equal_expense(paid_by, amount, group.users)
        print("Expense added")

    elif command == "SHOW_BALANCES":
        manager.show_balances()

    else:
        print("Invalid command. Type HELP.")
