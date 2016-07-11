# -*- coding: utf-8 -*-

from mock import Mock, call

from railroad import guard


def test_guard_call_guarded_function():
    f = Mock()

    guarded = guard('a', lambda a: True)(f)
    guarded('foo')

    assert f.called
    assert f.call_args == call('foo')


# def test_guard_pass_only_selected_paramters_to_guardian
