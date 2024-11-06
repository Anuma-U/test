import inspect


def introspection_info(obj):
    if isinstance(obj, (int, list, str, tuple, float, dict, bool)):
        atribut = dir(obj) # помимо атрибутов, выведет что-то еще
        methods = obj.__dir__()
    else:
        atribut = list(vars(obj).keys())
        methods = inspect.getmembers(obj, predicate=inspect.ismethod)
    type_obj = type(obj)
    modul = inspect.getmodule(obj)
    info = {"type": str(type_obj), "attributes":atribut, "methods": methods, "module": modul}
    return info

# здесь класс для того чтобы проверить другую часть функции(else)
# class Cucumber:
#     def __init__(self):
#         self.aaa = 12
#         self.a = 56
#
#     def plus(self):
#         return self.aaa + self.a
#
#     def minus(self):
#         return self.a - self.aaa
#
#
# fakt = Cucumber()
# print(introspection_info(fakt))
number_info = introspection_info(42)
print(number_info)

a = True
print(introspection_info(a))