class ZigZag:
    def __init__(self, l1, l2):
        self.queue = [l1, l2]

    def next(self):
        v = self.queue.pop(0)
        r = v.pop(0)
        if v:
            self.queue.append(v)
        return r

    def has_next(self):
        if self.queue:
            return True
        return False


