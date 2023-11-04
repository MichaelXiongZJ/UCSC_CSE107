import random
import copy

class Urn:
    def __init__(self, a_init):
        c_num = 100 - a_init
        self.all_balls = []
        for i in range(a_init):
            self.all_balls.append('a')
        for i in range(c_num):
            self.all_balls.append('c')

    def pick_a_ball(self):
        random.shuffle(self.all_balls)
        ball = self.all_balls.pop()
        return ball

    def run_test(self):
        current_color = ''
        while len(self.all_balls) > 1:
            ball = self.pick_a_ball()
            if(current_color == ''):
                current_color = ball
            elif(current_color != ball):
                current_color = ''
                self.all_balls.append(ball)
            else:
                continue
        last_ball = self.pick_a_ball()
        return last_ball

    def run_experiment(self):
        a_count = 0
        for i in range(2000):
            temp = copy.deepcopy(self)
            if(temp.run_test() == 'a'):
                a_count += 1
        ratio = a_count/2000
        return ratio

    def print_me(self):
        a_num = 0
        c_num = 0
        for x in self.all_balls:
            if x == 'a':
                a_num += 1
            else:
                c_num += 1
        print("Number of Aure balls =", a_num)
        print("Number of Carmine balls =", c_num)

list = (10, 50, 90)
for n in list:
    urn = Urn(n)
    ratio = urn.run_experiment()
    print("When a =", n, "ratio =",ratio)

