from dynamic_class_methods import DynamicClass
# reload(dynamic)

def test_dynamic_methods():
    assert DynamicClass().method_a()
    assert DynamicClass().method_b()

def test_dynamic_static_methods():
    assert DynamicClass.static_a()
    assert DynamicClass.static_b()

def test_dynamic_static_methods_with_args():
    assert DynamicClass.static_args_a("Hello", "World") == ("Hello", "World")
    assert DynamicClass.static_args_b("Hello", "World") == ("Hello", "World")
