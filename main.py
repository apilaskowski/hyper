#!/usr/bin/env python3

from logger import get_logger
from random import random
import signal

logger = get_logger()
log = logger.info

interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def is_float(v):
    try:
        float(v)
        return True
    except ValueError:
        return False


class Hyper:
    def __init__(self):
        self.llh_types = [(0, 'Creation'), (1, 'Perturbation')]

        self.sum_of_improvements = [0, 0]

        self.creating_number = 0
        self.perturbation_number = 0
        self.ask_heuristics_number(0)
        self.ask_heuristics_number(1)

        self.best_score = .0

        self.heuristic_reliability = []
        self.init_reliability_table()

        self.use_heuristic(0, 0)

    def init_reliability_table(self):
        self.heuristic_reliability = [[1 for _ in range(self.creating_number)], [1 for _ in range(self.perturbation_number)]]

    def ask_heuristics_number(self, heuristic_type=0):
        print('GET ' + str(self.llh_types[heuristic_type][0]))
        number = int(input())

        if heuristic_type == 0:
            self.creating_number = number
        else:
            self.perturbation_number = number
            self.sum_of_improvements[heuristic_type] = number

    def use_heuristic(self, heuristic_id, heuristic_type=1, address=0):
        if heuristic_type is 1:
            print('USE ' + str(heuristic_type) + ' ' + str(heuristic_id) + ' ' + str(address))
        else:
            print('USE ' + str(heuristic_type) + ' ' + str(heuristic_id))
        data, status = input().split()

        if is_float(status) and int(status) is not 0:
            self.sum_of_improvements[heuristic_type] -= self.heuristic_reliability[heuristic_type][heuristic_id]
            self.heuristic_reliability[heuristic_type][heuristic_id] = 0
            return

        score = float(data)

        if float(score) > self.best_score:
            self.best_score = float(score)
            self.sum_of_improvements[heuristic_type] += 1
            self.heuristic_reliability[heuristic_type][heuristic_id] += 1

    def choose_heuristic(self, heuristic_type=1):
        choice = float(self.sum_of_improvements[heuristic_type]) * random()
        index = 0
        while choice - self.heuristic_reliability[heuristic_type][index] > 0:
            choice -= self.heuristic_reliability[heuristic_type][index]
            index += 1
        return index

    @staticmethod
    def declare_solution(): # should be something smarter
        print('FINAL')


if __name__ == '__main__':
    signal.signal(signal.SIGTERM, signal_handler)

    hyper = Hyper()

    while not interrupted:
        h_id = hyper.choose_heuristic()
        hyper.use_heuristic(h_id)

    hyper.declare_solution()
