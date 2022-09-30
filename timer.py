
from asyncio.log import logger
import time


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class Timer:
    def __init__(self, text='Elapse time: {:0.4f} seconds.', logger=print):
        self._start_timer = None
        self.text = text
        self.logger = logger

    def start(self):
        if self._start_timer is not None:
            raise TimerError(f'Timer is running. Use stop() to stop it.')

        self._start_timer = time.perf_counter()

    def stop(self):
        if self._start_timer is None:
            raise TimerError(
                f'Timer is not running. Use start() to start ir first.')

        elapsed_time = time.perf_counter() - self._start_timer
        self._start_timer = None

        if self.logger:
            self.logger(self.text.format(elapsed_time))
            # print(self.text.format(elapsed_time))

        return elapsed_time
