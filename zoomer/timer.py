import time

class Timer:
    def __init__(self, name, verbose=False):
        self.name = name
        self.verbose = verbose
        self.stop = -1
    def __enter__(self): 
        self.start = time.perf_counter() 
    def elapsed(self):
        return (time.perf_counter() if self.stop == -1 else self.stop) - self.start
    def __exit__(self, *args):
        self.stop = time.perf_counter()
        if(self.verbose):
            print(f"{self.name}: {self.elapsed():.5f}s")