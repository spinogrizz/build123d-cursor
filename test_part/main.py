length, width, thickness = 80.0, 30.0, 10.0 

sk3 = Circle(width) - Rectangle(length / 2, width / 2)
ex3 = extrude(sk3, amount=2 * thickness)

test = Circle(10) + Rectangle(10, 10) + Circle(15)
ex4 = extrude(test, amount=2 * thickness)

ex3 += ex4

result = ex3
