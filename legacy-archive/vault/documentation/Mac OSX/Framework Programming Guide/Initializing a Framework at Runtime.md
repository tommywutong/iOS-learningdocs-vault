---
title: Framework Programming Guide
apple_id: 10000183i
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2013-09-17'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFrameworks/Tasks/InitializingFrameworks.html
archived_at: '2026-07-15T08:15:45.107705Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Framework Programming Guide](Introduction%20to%20Framework%20Programming%20Guide.md)


[Next](Exporting%20Your%20Framework%20Interface.md)[Previous](Creating%20a%20Framework.md)

# Initializing a Framework at Runtime

When a framework is first loaded by a unique process, the system calls the framework’s initialization code. Prior to OS X v10.4, framework initialization typically consisted of a single routine that was called when the framework was first loaded; however, in OS X v10.4 and later, the use of module initializers and finalizers became the preferred technique. The main advantage of module initializers is that they can be called after the dynamic linker has a chance to load any other libraries on which the module initializer depends. The same is not true of framework initialization routines, which are called immediately on load and may occur before other important modules (like the C++ runtime) are loaded.

Because all types of initialization routines are called at framework load-time, they are often called while an application is launching. Launch time is generally a bad time to perform large amounts of work because it can make the corresponding application feel sluggish. When writing your initialization routines, try to do as little work as possible to put your framework in a known state. For example, instead of allocating your framework data structures immediately, consider lazily initializing your data structures as they are needed. Also, avoid performing any operations that might cause a potential delay, such as accessing the network.

Remember that if your framework contains static data, that data must be initialized at load-time as well. Minimizing the number of static variables your framework uses can also help reduce initialization performance. For more information about improving the launch time of applications, see _[Launch Time Performance Guidelines](../../Performance/Launch%20Time%20Performance%20Guidelines/Introduction%20to%20Launch%20Time%20Performance%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2dq2i)_.

Module initializers are the preferred way to initialize a framework. A module initializer is a static function that takes no arguments and returns no value. It is declared using the `constructor` compiler attribute as shown in Listing 1. As with any static initialization function, you should guard against the function being called twice by placing a guard variable around your initialization code.

__Listing 1__  Module initializer for a framework

```
__attribute__((constructor))
static void MyModuleInitializer()
{
    static initialized = 0;
    if (!initialized)
    {
        // Initialization code.
        initialized = 1;
    }
}
```

Frameworks can define multiple module initializer functions. The dynamic link editor calls any module initializer functions after initializing any static variables but before calling any other functions or methods in your framework. If the code in a module initializer function relies on other libraries, such as the C++ runtime, the dynamic linker loads those libraries prior to calling the function. Each module initializer function is called only once when the framework is loaded by a process. Module initializers are executed in the order they are encountered by the compiler.

The symbols for any module initializer functions must not be exported by your framework. By default, Xcode exports all symbols declared in your project’s header files. You can restrict the set of exported symbols by explicitly exporting a list of symbols or by hiding specific symbols (and exporting everything else). For information on how to configure your framework’s exports, see [Exporting Your Framework Interface](Exporting%20Your%20Framework%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3dalkcijbuuskdivbq).

In OS X v10.4 and later, module initializers can access the launch arguments for the current process, as shown in Listing 2. A framework might use these arguments to get information about the launch configuration of the application, such as any environment variables or flags passed in on the launch line.

__Listing 2__  Module initializer with launch arguments

```
__attribute__((constructor))
static void initializer(int argc, char** argv, char** envp)
{
    // Initialization code.
}
```

In addition to module initializer functions, you can also define module finalizer functions, which implement any clean up code for your framework. Module finalizers are declared using the `destructor` compiler attribute as shown in Listing 3. Like module initializers, the symbols for module finalizers must not be exported by your framework. Module finalizers execute in the reverse order that they are encountered by the compiler.

__Listing 3__  Module finalizer function

```
__attribute__((destructor))
static void finalizer()
{
   // Clean up code.
}
```


If your framework must run in versions of OS X prior to 10.4, you can still use a framework initialization function as needed to initialize your framework data structures. When implementing your initialization routine, however, it is important to do as little work as possible. Because your initialization routine runs immediately at load time, other code modules may not be loaded and available for use, so it is important that you do not perform any complex initialization involving other libraries.

The signature of an initialization function is the same as that for a standard module initializer:

```
void MyFrameworkInit()
```

To load your routine, you must pass the name of your routine to the linker using the `INIT_ROUTINE` flag. From the command line you set this flag using the `-init` option, followed by the name of your initialization routine. In Xcode, you set this flag by doing the following:

1. Select your framework target and open an inspector window.
2. In the Build pane, find the Initialization Routine build setting. It is with the Linking options.
3. Set the value of this setting to the symbol name of your initialization routine.

For ANSI C–based routines, the symbol name is simply the function name with a leading underscore character. For example, the symbol name for the `MyFrameworkInit` function is `_MyFrameworkInit`. You should not use C++ routines for initialization functions.

If you have trouble building your framework with the specified initialization routine, there are a few things you can try to fix the problem. Use the `nm` command-line tool to confirm the symbol name of your routine. You can also use `nm` with the `-g` option to make sure that a global symbol for your routine is exported by the library. If it isn’t, check to see if you have an exports file and make sure your routine is included in it.

[Next](Exporting%20Your%20Framework%20Interface.md)[Previous](Creating%20a%20Framework.md)

