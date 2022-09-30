
import time


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class Timer:
    def __init__(self):
        self._start_timer = None

    def start(self):
        if self._start_timer is not None:
            raise TimerError(f'Timer is running. Use stop() to stop it.')

        self._start_timer = time.perf_counter()

    def stop(self):
        if self._start_timer is None:
            raise TimerError(
                f'Timer is not running. Use start() to start ir first.')

        elapse_time = time.perf_counter() - self._start_timer
        self._start_timer = None
        print(f'Elapse time is: {elapse_time:0.6f} seconds.')
