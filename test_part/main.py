length, width, thickness = 80.0, 40.0, 8.0

sk3 = Circle(width) - Rectangle(length / 2, width / 2)
ex3 = extrude(sk3, amount=2 * thickness)


result = ex3


