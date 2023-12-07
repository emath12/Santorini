class InvalidWorker(BaseException):
    def __init__(self) -> None:
        pass

class NotYourWorker(BaseException):
    def __init__(self) -> None:
        pass

class InvalidDirection(BaseException):
    def __init__(self) -> None:
        pass

class InvalidMovementDirection(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class InvalidBuildDirection(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class WorkerCannotMove(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)