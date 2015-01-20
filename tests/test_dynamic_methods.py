from dynamic_class_methods import DynamicClass
# reload(dynamic)

def test_dynamic_methods():
    assert DynamicClass().method_a()

def test_dynamic_static_methods():
    assert DynamicClass.static_a()

def test_dynamic_static_methods_with_args():
    assert DynamicClass.static_args_a("Hello", "World") == ("Hello", "World")
