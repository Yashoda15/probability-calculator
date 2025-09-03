import random
import copy

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num):
        drawn = []
        if num >= len(self.contents):
            drawn = self.contents[:]
            self.contents.clear()
            return drawn
        for _ in range(num):
            index = random.randint(0, len(self.contents) - 1)
            drawn.append(self.contents.pop(index))
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    for _ in range(num_experiments):
        experiment_hat = copy.deepcopy(hat)
        drawn_balls = experiment_hat.draw(num_balls_drawn)
        drawn_counts = {}
        for ball in drawn_balls:
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1
        success = True
        for color, count in expected_balls.items():
            if drawn_counts.get(color, 0) < count:
                success = False
                break
        if success:
            success_count += 1
    return success_count / num_experiments

def main():
    print("=== Probability Calculator ===\n")
    balls = {}
    while True:
        color = input("Enter ball color (or 'done' to finish): ").strip()
        if color.lower() == 'done':
            break
        count = int(input(f"Enter number of {color} balls: "))
        balls[color] = count

    hat = Hat(**balls)
    num_balls_drawn = int(input("\nNumber of balls to draw: "))
    expected_balls = {}
    while True:
        color = input("Enter expected ball color (or 'done' to finish): ").strip()
        if color.lower() == 'done':
            break
        count = int(input(f"Enter minimum number of {color} balls: "))
        expected_balls[color] = count

    num_experiments = int(input("\nNumber of experiments to run: "))
    probability = experiment(hat, expected_balls, num_balls_drawn, num_experiments)
    print(f"\nEstimated Probability: {probability:.4f}")

if __name__ == "__main__":
    main()
