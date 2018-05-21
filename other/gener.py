# range test

class range_copy(object):
    def __init__(self, *args, **kwargs):
        self.args = args

    def __next__(self):
        return next(self.__iter__())

    def __iter__(self):
        if self.__len__() == 1:
            return iter([self.args[0]])
        elif self.__len__() == 2:
            return iter([])

    def __len__(self):
        return len(self.args)


class obj(object):
    def __init__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        print("/" * 66)

    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        print(cls)
        print("?" * 55)
        _cls = object.__new__(cls, *args, **kwargs)
        return _cls


# a = _obj()
# print(a)
# import copy
# b = copy.deepcopy(a)
# print(b)
# c = copy.copy(a)
# print(c)
# setattr(a, "abc", "sbc")
# print(a.__dict__)
# print(getattr(a, "abc"))
# print(getattr(c, "abc"))
# print(getattr(b, "abc"))

# a = type('MyClass', (), {})
# print(a)
# print(a())

class parent(object):
    x = 1


class child1(parent):
    pass


class child2(parent):
    pass


# print(parent.x, child1.x, child2.x)
# child1.x = 2
# print(parent.x, child1.x, child2.x)
# parent.x = 3
# print(parent.x, child1.x, child2.x)
# print(['a', 'b'][10:])
# print(1 and 2 or 3)
# print(2 and 0 or 1)
# print(1 or 2 and 0)
# print(2 or 0 and 1)
# # print(1 and 2)
# a = 'a'
# print(a.__class__)
# print(a.__class__.__class__)


# def upattr(futre_class_name, future_class_parents, future_class_attrs):
#     attrs = ((k, v) for k, v in future_class_attrs.items() if not k.startswith('__'))
#     uppercase_attr = dict((k.upper(), v) for k, v in attrs)
#     return type(futre_class_name, future_class_parents, uppercase_attr)
#
#
# class upattr(type):
#     def __new__(cls, cls_name, cls_parents, cls_attrs):
#         _attrs = ((k, v) for k, v in cls_attrs.items() if not k.startswith('__'))
#         attrs_upper = dict((k.upper(), v) for k, v in _attrs)
#         return super().__new__(cls, cls_name, cls_parents, attrs_upper)
#
# class Foo(metaclass=upattr):
#     bar = 'pip'
#
#
# print(hasattr(Foo, 'bar'))  # False
# print(hasattr(Foo, 'BAR'))  # True

# class Base(object):
#     def __init__(self):
#         print('Base.__init__')
# class A(Base):
#     def __init__(self):
#         super().__init__()
#         print('a.__init__')
# class B(Base):
#     def __init__(self):
#         super().__init__()
#         print('b.__init__')
# class C(A, B):
#     def __init__(self):
#         super().__init__()
#         print('c.__init__')
# c = C()
# print(C.__mro__)

# class Base(object):
#     def __init__(self):
#         print('Base.__init__')
# class A(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print('a.__init__')
# class B(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print('b.__init__')
# class C(A, B):
#     def __init__(self):
#         A.__init__(self)
#         B.__init__(self)
#         print('c.__init__')
# c = C()
# print(C.__mro__)

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<{}:{}>'.format(self.__class__.__name__, self.name)


# class ModelMetaClass(type):
#     def __new__(cls, cls_name, cls_parents, cls_attrs):
#         if cls_name == 'Model':
#             return super().__new__(cls, cls_name, cls_parents, cls_attrs)
#         _mapping = {}
#         for k, v in cls_attrs.items():
#             if not isinstance(v, Field):
#                 continue
#             print('found mapping <{}===>{}>'.format(k, v))
#             _mapping[k] = v
#         for k in _mapping.keys():
#             cls_attrs.pop(k)
#         cls_attrs['__table__'] = cls_name.lower()
#         cls_attrs['__mappings__'] = _mapping
#         return super().__new__(cls, cls_name, cls_parents, cls_attrs)
#
#
# class Model(metaclass=ModelMetaClass):
#     def __init__(self, **kw):
#         for k, v in kw.items():
#             setattr(self, k, v)
#
#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except:
#             raise AttributeError('Model has not found attr <{}>'.format(key))
#
#     def save(self):
#         for k, v in self.__mappings__.items():
#             print("{}===++++>{}".format(k, v))


# class User(Model):
#     id = IntegerField('id')
#     name = StringField('username')
#     email = StringField('email')
#     password = StringField('password')


# u = User(id=10, name='abc', email='82190@qq.com', password='abcd%$#')
# u.save()
# print(User.__dict__)
# print(u.__dict__)

class Foo(object):
    def __init__(self, **kwargs):
        print(kwargs)
        print("/" * 66)

    def __new__(cls, **kwargs):
        print("?" * 66)
        print(kwargs)
        return super().__new__(cls)


class Too(Foo):
    def __new__(cls, **kwargs):
        print("-" * 66)
        return object.__new__(cls)


class Eoo(Foo):
    def __new__(cls, **kwargs):
        print(":" * 66)
        return super().__new__(cls, **kwargs)


# f = Too(a=10)
# e = Eoo(b=11)

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance


a = Singleton()
b = Singleton()


# print(a is b)
# print(id(a))
# print(id(b))


class MetaSingleton(type):
    def __init__(self, *args, **kwargs):
        print('__init__')
        self._instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        print('__call__')
        if not self._instance:
            self._instance = super().__call__(*args, **kwargs)
        return self._instance


class Objects(metaclass=MetaSingleton):
    pass


c = Objects()
d = Objects()

print(c is d)
print(id(c))
print(id(d))


# print(Objects.__dict__)

# for x in dir(Objects):
#     print(x)
#     print(getattr(Objects, x))


class SingletonObject(type):
    def __new__(cls, cls_name, cls_parents, cls_attrs):
        print("?" * 66)
        cls_attrs['_instance'] = None
        return super().__new__(cls, cls_name, cls_parents, cls_attrs)

    def __call__(self, *args, **kwargs):
        print("/" * 66)
        if not self._instance:
            self._instance = super().__call__(*args, **kwargs)
        return self._instance


class Foo(metaclass=SingletonObject):
    pass


z = Foo()
x = Foo()
print(z is x)
print(id(x))
print(id(z))


class A(type):
    pass


class B(metaclass=A):
    pass


class C(B, metaclass=type):
    pass


class D(A):
    pass


print("?" * 66)
print(C.__class__)
print(C.__mro__)
print(D.__class__)
exit()


class D(B, C):
    pass


print(B.__class__)
print(C.__class__)

print(B.__mro__)
print(C.__mro__)

print(type(D))
