from models.todo import Todo


class TodoList:
    def __init__(self) -> None:
        self.todos: list[Todo] = []
        pass

    def add_todo(self, todo: str) -> None:
        pass