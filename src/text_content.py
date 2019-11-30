from config.system import PROJECT_NAME


class TextMessage:
    root_greeting = f"{PROJECT_NAME} started!"
    start = "Hello, world!"
    add_new_user_data = "Data was added"
    get_user_data = "Data is {}"


class AdminTextMessage:
    start = "Hello, admin {}"


class ButtonText:
    push_me = "push_me"
