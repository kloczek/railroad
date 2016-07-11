# -*- coding: utf-8 -*-

from functools import wraps


class GuardError(Exception):
    pass


def guard(params, guardian, error_class=GuardError, message=''):
    '''
    A guard function - check parameters
    with guardian function on decorated function

    :param tuple or string params: guarded function parameter/s
    :param function guardian: verifying the conditions for the selected parameter
    :param Exception error_class: raised class when guardian return false
    :param string message: error message
    '''
    def guard_decorate(f):
        @wraps(f)
        def _guard_decorate(*args, **kwargs):
            if guardian(*args):
                return f(*args, **kwargs)
            else:
                raise error_class(message=message)
        return _guard_decorate
    return guard_decorate
