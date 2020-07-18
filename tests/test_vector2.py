def test_init():
    from maths.vector2 import Vector2
    a = Vector2(0, 0)
    b = Vector2()
    c = Vector2(1)
    d = Vector2(1, 2)
    f = Vector2(x=1, y=1)
    assert all([isinstance(a, Vector2),
                isinstance(b, Vector2),
                isinstance(c, Vector2),
                isinstance(d, Vector2),
                isinstance(f, Vector2)])


def test_repr():
    from maths.vector2 import Vector2
    a = Vector2(0, 0)
    assert str(a) == "Vector2: [0.0, 0.0]"


def test_x_getter_setter():
    from maths.vector2 import Vector2
    a = Vector2(0, 0)
    a.x = 5.0
    assert a.x == 5.0


def test_y_getter_setter():
    from maths.vector2 import Vector2
    a = Vector2(0, 0)
    a.y = 5.0
    assert a.y== 5.0

def test_add():
    from maths.vector2 import Vector2
    a = Vector2(1, 0)
    b = Vector2(0, 1)
    a += b
    c = a + b
    assert all([a.as_tuple() == (1.0, 1.0),
                c.as_tuple() == (1.0, 2.0)])


def test_subtract():
    from maths.vector2 import Vector2
    a = Vector2(1, 0)
    b = Vector2(0, 1)
    a -= b
    c = a - b
    assert all([a.as_tuple() == (1.0, -1.0),
                c.as_tuple() == (1.0, -2.0)])


def test_multiply():
    from maths.vector2 import Vector2
    a = Vector2(1, 2)
    b = 2
    a *= b
    c = a * b
    assert all([a.as_tuple() == (2.0, 4.0),
                c.as_tuple() == (4.0, 8.0)])


def test_divide():
    from maths.vector2 import Vector2
    a = Vector2(1, 2)
    b = 2
    a /= b
    c = a / b
    assert all([a.as_tuple() == (0.5, 1.0),
                c.as_tuple() == (0.25, 0.5)])


def test_as_tuple():
    from maths.vector2 import Vector2
    a = Vector2(1, 2).as_tuple()
    assert all([isinstance(a, tuple),
                a == (1.0, 2.00)])


def test_magnitude():
    from maths.vector2 import Vector2
    a = Vector2(0, 90)
    mag = a.magnitude
    assert mag == 90


def test_normalize():
    from maths.vector2 import Vector2
    a = Vector2(10, 10)
    a.normalize()
    a_n = a.as_tuple()
    b = Vector2(0, 10)
    b.normalize()
    b_n = b.as_tuple()
    assert all([a_n == (0.7071067811865475, 0.7071067811865475),
                b_n == (0, 1)])


def test_normalized():
    from maths.vector2 import Vector2
    a = Vector2(10, 10)
    a_n = a.normalized().as_tuple()
    b = Vector2(0, 10)
    b_n = b.normalized().as_tuple()
    assert all([a_n == (0.7071067811865475, 0.7071067811865475),
                b_n == (0, 1)])


def test_dot():
    from maths.vector2 import Vector2
    a = Vector2(5, 4)
    b = Vector2(10, 10)
    d = a.dot(b)
    assert d == 90


def test_distance_to():
    from maths.vector2 import Vector2
    a = Vector2(0, 10)
    b = Vector2(0, 9)
    d = a.distance_to(b)
    assert d == 1


def test_angle_to():
    from maths.vector2 import Vector2
    a = Vector2(0, 90)
    b = Vector2(1, 0)
    c = Vector2(1, 1)
    ab_angle = a.angle_to(b)
    ac_angle = a.angle_to(c)
    assert all([ab_angle == 90,
                ac_angle == 45])
