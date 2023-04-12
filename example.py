import pluggy

hookspec = pluggy.HookspecMarker("example_for_pycon")
hookimpl = pluggy.HookimplMarker("example_for_pycon")


class ExampleSpec:
    """A hook specification namespace."""

    @hookspec
    def myhook(self, arg1, arg2):
        """My special little hook that you can customize."""

class MyPlugin:
    """A hook implementation namespace."""

    @hookimpl
    def myhook(self, arg1, arg2):
        print("inside Plugin_1.myhook()")
        return arg1 + arg2

# create a manager and add the spec
pm = pluggy.PluginManager("example_for_pycon")
pm.add_hookspecs(ExampleSpec)

# register plugins
pm.register(MyPlugin())

# call our `myhook` hook
results = pm.hook.myhook(arg1=1, arg2=2)
print(results)
