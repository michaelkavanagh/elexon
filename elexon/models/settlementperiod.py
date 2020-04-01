class sp(int):
    def __new__(cls, value, *args, **kwargs):
        if value < 1:
            raise ValueError("sp types must not be less than one.")
        elif value > 50:
            raise ValueError("sp types must not be greater than fifty.")
        # elif value != '*':
        #     raise ValueError("sp types must not be greater than fifty.")
        return  super(cls, cls).__new__(cls, value)

    def __add__(self, other):
        res = super(sp, self).__add__(other)
        return self.__class__(max(res, 0))

    def __sub__(self, other):
        res = super(sp, self).__sub__(other)
        return self.__class__(max(res, 0))

    def __mul__(self, other):
        res = super(sp, self).__mul__(other)
        return self.__class__(max(res, 0))

    def __div__(self, other):
        res = super(sp, self).__div__(other)
        return self.__class__(max(res, 0))

    def __str__(self):
        return "%d" % int(self)

    def __repr__(self):
        return "sp(%d)" % int(self)
