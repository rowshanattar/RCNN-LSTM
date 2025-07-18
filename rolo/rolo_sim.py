class RoloTracker:
    def __init__(self):
        self.previous_box = None

    def track(self, box):
        # Simulated tracking: return input box directly
        self.previous_box = box
        return box
