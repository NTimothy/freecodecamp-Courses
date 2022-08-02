import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        self.balls = balls
        for ball in balls:
            num_balls = balls[ball]
            while num_balls >0:
                self.contents.append(ball)
                num_balls -= 1

    def draw(self, num):
        contents_copy = self.contents.copy()
        self.drawn_balls = []

        # While draws remain and balls remain in the hat
        while num > 0 and len(contents_copy)>0:
            # Determine a random ball index
            x = random.randint(0, len(contents_copy)-1)

            # Remove ball from contents and place into new list
            self.drawn_balls.append(contents_copy.pop(x))

            num -=1
        return self.drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass



hat1 = Hat(blue=2, green=2, yellow=2)
print(hat1.draw(3))
