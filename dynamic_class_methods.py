class DynamicClass(object):
    def __init__(self):
        pass

    @staticmethod
    def run_me(*args):
        return args

#
# Dynamic instance methods
#
methods = ["a","b"]

def myMethod(self):
    return True

for m in methods:
    setattr(DynamicClass, "method_%s" % m, myMethod)

#
# Dynamic static methods
#

def staticMethod():
    return True

for m in methods:
    setattr(DynamicClass, "static_%s" % m, staticmethod(staticMethod))


#
# Dynamic static methods
#

def staticMethodWithArgs(arg_a, arg_b):
    return DynamicClass.run_me(arg_a, arg_b)

for m in methods:
    setattr(DynamicClass, "static_args_%s" % m, staticmethod(staticMethodWithArgs))
