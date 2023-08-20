class run:
    def __init__(self, in_distance, in_time, in_type, in_notes):
        self.distance = in_distance
        self.time = in_time
        self.notes = in_notes
        #Type of run accepted inputs are, Easy, Long, Workout, Warmup, Cooldown
        self.type = in_type
