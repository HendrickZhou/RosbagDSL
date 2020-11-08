from .pipe import Pipe

@Pipe
def compute(m1, m2, m3, *, extra_arg):
    if m3 > extra_arg:
    return m1 * m3