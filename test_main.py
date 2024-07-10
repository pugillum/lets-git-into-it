from main import add


def test_main():
    result = add(1, 2, 3)
    assert result == 6
