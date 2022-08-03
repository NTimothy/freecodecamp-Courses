import copy
import random

# Creates a "Hat" class object that contains given number of colored balls
class Hat:
    def __init__(self, **balls):
        self.contents = []
        self.totals = balls
        for ball in balls:
            num_balls = balls[ball]
            while num_balls > 0:
                self.contents.append(ball)
                num_balls -= 1
        self.contents_full = list(self.contents)

    # Removes a ball from hat for n times, w/o replacement
    def draw(self, num):
        self.contents = list(self.contents_full)
        self.drawn_balls = []
        # While draws remain and balls remain in the
        if test:
            print("Full Copy:",self.contents_full)
            print("Contents:",self.contents)
        while num > 0 and len(self.contents) > 0:
            # Determine a random ball index
            x = random.randint(0, len(self.contents)-1)

            # Remove ball from contents and place into new list
            self.drawn_balls.append(self.contents.pop(x))
            num -= 1

        return self.drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # Prepare probability variables
    M = float(0)
    N = float(num_experiments)
    
    while num_experiments > 0:
        # Creates list of drawn balls in 1 experiment
        drawn = sorted(hat.draw(num_balls_drawn))

        # Creates dictionary of drawn ball color totals
        totals = {}
        for draw in drawn:
            if draw in totals:
                totals[draw] +=1
            else:
                totals[draw] = 1

        valid = {}
        # Compare drawn totals against expected totals
        try:
            for color in expected_balls:
                # print(color, "|", totals[color], " <--> ", expected_balls[color])
                if totals[color] >= expected_balls[color]:
                    valid[color] = 0
                elif totals[color]<expected_balls[color]:
                    valid[color] = 1
                    pass
        except KeyError:
            # Missing ball color -> proceed to next experiment
            num_experiments -=1
            continue

        # If expected balls met, +1 to qualifying experiment
        if sum(valid.values()) == 0:
            M +=1

        # Proceed to next experiment
        num_experiments -=1

    prob = float(M/N)
    return prob
