def classify_triangle(a,b,c):
    # Validierung für ints
    if type(a) is not int:
        raise ValueError("A is not an integer")
    if type(b) is not int:
        raise ValueError("B is not an integer")
    if type(c) is not int:
        raise ValueError("C is not an integer")

    # Validierung für >=0
    if a < 0:
        raise ValueError("A is smaller than 0")
    if b < 0:
        raise ValueError("B is smaller than 0")
    if c < 0:
        raise ValueError("C is smaller than 0")

    # Validierung für Gleichseitiges Dreieck
    if (a == b) and (b == c):
        return "Gleichseitig"

    # Validierung für Gleichschenkeliges Dreieck
    if (a == b) or (a == c) or (b == c):
        return "Gleichschenkelig"

    return "Ungleichseitig"
