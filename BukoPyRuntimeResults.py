class RTResult:
    def __init__(self):
        self.reset()

    def reset(self):
        self.value = None
        self.error = None

    def register(self, res):
        self.error = res.error
        return res.value

    def success(self, value):
        self.reset()
        self.value = value
        return self

    def failure(self, error):
        self.reset()
        self.error = error
        return self
