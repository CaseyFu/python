class DirtyError(Exception):
    """胀字异常"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class MoralError(Exception):
    """道德字异常"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
