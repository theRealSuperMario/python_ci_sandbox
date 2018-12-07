import pytest


def test_stuff():
    from tasks import cli
    c = cli.CLI()
    assert c.run()
