class BaseError(Exception):
    def __init__(self, message="this is an error"):

        self.message = message
        super().__init__(self.message)
