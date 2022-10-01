import time
from dataclasses import dataclass, field
from typing import Any, ClassVar


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

# The @dataclass decorator defines Timer as a data class.


@dataclass
class Timer:
    # The special ClassVar annotation is necessary for data classes to specify that .timers is a class variable.
    timers: ClassVar = {}
    name: Any = None
    text: Any = 'Elapse time: {:0.4f} seconds.'
    logger: Any = print
    # Define special visibility for this attribute. Don't init with construct or be seeing under class representation call with type() or others.
    _start_timer: Any = field(default=None, init=False, repr=False)

    def __post_init__(self):
        """Initialization: add timer to dict of timers"""
        # if name is passed, add new named timers to dictionary of timers.
        if self.name:
            self.timers.setdefault(self.name, 0)

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
        if self.name:
            # each timer will be an accumulation of time spent under those task names.
            self.timers[self.name] += elapsed_time

        return elapsed_time
