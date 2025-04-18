import inspect


def introspection_info(obj):
    atribut = []
    methods = []
    for elem in dir(obj):
        if not elem.startswith("_"):
            atribut.append(elem)
        else:
            methods.append(elem)
    type_obj = type(obj)
    modul = inspect.getmodule(obj)
    info = {"type": str(type_obj), "attributes":atribut, "methods": methods, "module": modul}
    return info


number_info = introspection_info(42)
print(number_info)

a = True
print(introspection_info(a))
