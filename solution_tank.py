#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO
from settings import SOLUTION_TANK_CONFIG


class SolutionTankInterface:
    """
    Solution tank interface uses float switch to check solution level.
    """

    def __init__(self, config):
        self.gpio_float_switch = config['gpio_float_switch']
        self.float_switch_state_when_full = config['float_switch_state_when_full']

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.gpio_float_switch, GPIO.IN)

    def __del__(self):
        GPIO.cleanup()

    def is_full(self):
        float_switch_state = GPIO.input(self.gpio_float_switch)
        return float_switch_state == self.float_switch_state_when_full


def main():
    t = SolutionTankInterface(SOLUTION_TANK_CONFIG)
    while True:
        try:
            is_full = t.is_full()
            print('Is full: ' + str(is_full))
            time.sleep(1)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
