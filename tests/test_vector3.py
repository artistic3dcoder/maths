

def test_init():
    from maths.vector3 import Vector3
    a = Vector3(0, 0, 0)
    b = Vector3()
    c = Vector3(1)
    d = Vector3(1, 2)
    e = Vector3(z=1)
    f = Vector3(x=1, y=1, z=1)
    assert all([isinstance(a, Vector3),
                isinstance(b, Vector3),
                isinstance(c, Vector3),
                isinstance(d, Vector3),
                isinstance(e, Vector3),
                isinstance(f, Vector3)])


def test_repr():
    from maths.vector3 import Vector3
    a = Vector3(0, 0, 0)
    assert str(a) == "Vector3: [0.0, 0.0, 0.0]"


def test_x_getter_setter():
    from maths.vector3 import Vector3
    a = Vector3(0, 0, 0)
    a.x = 5.0
    assert a.x == 5.0


def test_y_getter_setter():
    from maths.vector3 import Vector3
    a = Vector3(0, 0, 0)
    a.y = 5.0
    assert a.y== 5.0


def test_z_getter_setter():
    from maths.vector3 import Vector3
    a = Vector3(0, 0, 0)
    a.z = 5.0
    assert a.z == 5.0


def test_add():
    from maths.vector3 import Vector3
    a = Vector3(1, 0, 0)
    b = Vector3(0, 0, 1)
    a += b
    c = a + b
    assert all([a.as_tuple() == (1.0, 0.0, 1.0),
                c.as_tuple() == (1.0, 0.0, 2.0)])


def test_subtract():
    from maths.vector3 import Vector3
    a = Vector3(1, 0, 0)
    b = Vector3(0, 0, 1)
    a -= b
    c = a - b
    assert all([a.as_tuple() == (1.0, 0.0, -1.0),
                c.as_tuple() == (1.0, 0.0, -2.0)])


def test_multiply():
    from maths.vector3 import Vector3
    a = Vector3(1, 0, 2)
    b = 2
    a *= b
    c = a * b
    assert all([a.as_tuple() == (2.0, 0.0, 4.0),
                c.as_tuple() == (4.0, 0.0, 8.0)])


def test_divide():
    from maths.vector3 import Vector3
    a = Vector3(1, 0, 2)
    b = 2
    a /= b
    c = a / b
    assert all([a.as_tuple() == (0.5, 0.0, 1.0),
                c.as_tuple() == (0.25, 0.0, 0.5)])


def test_as_tuple():
    from maths.vector3 import Vector3
    a = Vector3(1, 2, 3).as_tuple()
    assert all([isinstance(a, tuple),
                a == (1.0, 2.0, 3.0)])


def test_magnitude():
    from maths.vector3 import Vector3
    a = Vector3(0, 0, 90)
    mag = a.magnitude()
    assert mag == 90


def test_cross():
    from maths.vector3 import Vector3
    a = Vector3(0, 0, 1)
    b = Vector3(1, 0, 0)
    cross = a.cross(b)
    assert cross.as_tuple() == (0, 1, 0)


def test_normalize():
    from maths.vector3 import Vector3
    a = Vector3(10, 10, 10)
    a.normalize()
    a_n = a.as_tuple()
    b = Vector3(0, 0, 10)
    b.normalize()
    b_n = b.as_tuple()
    assert all([a_n == (0.5773502691896257, 0.5773502691896257, 0.5773502691896257),
                b_n == (0, 0, 1)])


def test_normalized():
    from maths.vector3 import Vector3
    a = Vector3(10, 10, 10)
    a_n = a.normalized().as_tuple()
    b = Vector3(0, 0, 10)
    b_n = b.normalized().as_tuple()
    assert all([a_n == (0.5773502691896257, 0.5773502691896257, 0.5773502691896257),
                b_n == (0, 0, 1)])


def test_dot():
    from maths.vector3 import Vector3
    a = Vector3(5, 4, 3)
    b = Vector3(10, 10, 10)
    d = a.dot(b)
    assert d == 120


def test_distance_to():
    from maths.vector3 import Vector3
    a = Vector3(0, 0, 10)
    b = Vector3(0, 0, 9)
    d = a.distance_to(b)
    assert d == 1


def test_angle_to():
    from maths.vector3 import Vector3
    a = Vector3(0, 0, 90)
    b = Vector3(1, 0, 0)
    c = Vector3(1, 0, 1)
    ab_angle = a.angle_to(b)
    ac_angle = a.angle_to(c)
    assert all([ab_angle == 90,
                ac_angle == 45])
