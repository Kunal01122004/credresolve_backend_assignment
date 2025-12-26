class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name


class Group:
    def __init__(self, group_id, name, users):
        self.group_id = group_id
        self.name = name
        self.users = users  # list of user_ids
