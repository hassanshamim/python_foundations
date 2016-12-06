from itertools import islice


class Reindeer():
    def __init__(self, name, speed=0, run_time=0, rest_time=0):
        self.name = name
        self.speed = int(speed)
        self.run_time = int(run_time)
        self.rest_time = int(rest_time)

        self.position = 0
        self.state = None
        self.remaining_time = None

    def __repr__(self):
        return "<Reindeer {}: {} for {} more turns, at position {}".format(self.name, self.state, self.remaining_time, self.position)

    def take_turn(self):
        if not self.state:
            self.start_running()
        elif self.remaining_time == 0:
            self.switch_action()
        else:
            self.run() if self.state == 'running' else self.rest()

    def switch_action(self):
        if self.state == 'running':
            self.start_resting()
        else:
            self.start_running()

    def start_running(self):
        self.remaining_time = self.run_time
        self.state = 'running'
        self.run()

    def start_resting(self):
        self.remaining_time = self.rest_time
        self.state = 'resting'
        self.rest()

    def run(self):
        self.position += self.speed
        self.remaining_time -= 1

    def rest(self):
        self.remaining_time -= 1
