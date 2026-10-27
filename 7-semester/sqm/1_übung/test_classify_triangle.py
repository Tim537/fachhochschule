import pytest
from classify_triangle import classify_triangle


def test_a_int():
    with pytest.raises(ValueError):
        classify_triangle("A", 2, 3)

def test_b_int():
    with pytest.raises(ValueError):
        classify_triangle(1, "B", 3)

def test_c_int():
    with pytest.raises(ValueError):
        classify_triangle(1, 2, "C")

def test_a_positive():
    with pytest.raises(ValueError):
        classify_triangle(-1, 2, 3)

def test_b_positive():
    with pytest.raises(ValueError):
        classify_triangle(1, -2, 3)

def test_c_positive():
    with pytest.raises(ValueError):
        classify_triangle(1, 2, -3)

def test_triangle_gleichseitig():
    assert classify_triangle(1, 1, 1) == "Gleichseitig"

def test_triangle_not_gleichseitig():
    assert classify_triangle(1, 2, 3) == "Ungleichseitig"

def test_triangle_gleichschenkelig_a_b():
    assert classify_triangle(1, 1, 3) == "Gleichschenkelig"

def test_triangle_gleichschenkelig_a_c():
    assert classify_triangle(1, 2, 1) == "Gleichschenkelig"

def test_triangle_gleichschenkelig_b_c():
    assert classify_triangle(1, 2, 2) == "Gleichschenkelig"

def test_triangle_not_gleichschenkelig():
    assert classify_triangle(2, 2, 2) == "Gleichseitig"

def test_triangle_not_ungleichschenkelig():
    assert classify_triangle(3, 3, 3) == "Gleichseitig"

def test_triangle_ungleichschenkelig():
    assert classify_triangle(1, 2, 3) == "Ungleichseitig"