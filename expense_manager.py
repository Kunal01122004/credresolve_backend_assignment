class ExpenseManager:
    def __init__(self):
        self.users = {}        # user_id -> User
        self.groups = {}       # group_id -> Group
        self.balances = {}     # (u1, u2) -> amount (u1 owes u2)

    def add_user(self, user):
        self.users[user.user_id] = user

    def add_group(self, group):
        self.groups[group.group_id] = group

    def _add_balance(self, from_user, to_user, amount):
        if from_user == to_user:
            return

        self.balances[(from_user, to_user)] = self.balances.get(
            (from_user, to_user), 0
        ) + amount

    def add_equal_expense(self, paid_by, amount, users):
        split = amount / len(users)
        for user in users:
            self._add_balance(user, paid_by, split)

    def add_exact_expense(self, paid_by, splits):
        for user, amount in splits.items():
            self._add_balance(user, paid_by, amount)

    def add_percentage_expense(self, paid_by, amount, percentages):
        for user, percent in percentages.items():
            self._add_balance(user, paid_by, amount * percent / 100)

    def show_balances(self):
        simplified = {}
        for (u1, u2), amt in self.balances.items():
            if amt <= 0:
                continue
            simplified[(u1, u2)] = round(amt, 2)

        if not simplified:
            print("No balances")
            return

        for (u1, u2), amt in simplified.items():
            print(f"{self.users[u1].name} owes {self.users[u2].name}: ₹{amt}")
