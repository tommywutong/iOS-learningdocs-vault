---
title: C++ Runtime Environment Programming Guide
apple_id: TP40001666
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2009-10-09'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/CppRuntimeEnv/Articles/LibCPPDeployment.html
archived_at: '2026-07-15T07:24:22.099201Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [C++ Runtime Environment Programming Guide](Introduction.md)


[Next](Creating%20Compatible%20Libraries.md)[Previous](Overview%20of%20the%20C%2B%2B%20Runtime%20Environment.md)

# Deploying Applications With the C++ Runtime

In most situations, you should never have to worry about linking against the C++ runtime environment. When you build your C++ code, GCC chooses the most appropriate version of the C++ standard library and links to it. For applications compiled using GCC 3.3, the compiler links to the static C++ standard library `libstdc++.a`. For applications compiled using GCC 4.0, the compiler links to the dynamic C++ standard library `libstdc++.dylib` by default (`libstdc++.a` is also available as an option).

The following sections describe issues you may encounter when linking against the dynamic runtime or the new static runtime. There are no known issues worth noting for deploying code using the original static C++ runtime.

The following caveats apply to the new static and dynamic C++ runtimes.

- If your program must run on versions of OS X prior to 10.3.9, as well as OS X v10.3.9 and later, you must use the GCC 3.3 compiler and build your program using the original static C++ standard library (`libstdc++.a`).
- Applications that run on OS X v10.3.9 must not try to use the `long double` type or any of the functions associated with it. Support for the 128-bit `long double` type was not introduced until OS X v10.4. Similarly, full support for `sinl`, `expl`, and all other `long double` math functions defined by the C standard is available only in 10.4 and later.
- When overriding the `new` and `delete` operators, your overrides will be visible across shared library boundaries (application wide) unless you specifically takes steps to make them hidden (such as with an (un)export list). Even uses of `new`/`delete` in system frameworks, in the dynamic C++ runtime (even if you are only indirectly linked to it) or in other modules (possibly linked statically or dynamically to the C++ runtime) will use your overrides, unless that module also has overridden `new`/`delete` operators.

  Unless you are sure that code modules are using the same operator `new` and `delete`, do not transfer memory ownership across shared library boundaries.
- Multithreaded applications which use the standard stream (`std::cin`, `std::cout`, and so on) must explicitly synchronize their use of these global objects if there is any chance that two threads may simultaneously access one of them. Functions that set global state (such as `set_terminate`, `set_unexpected`, and so on) must also be explicitly synchronized if multiple threads can call them at once. In general:

  1. It is safe to simultaneously call `const` and non-`const` methods from different threads to distinct objects.
  2. It is safe to simultaneously call `const` methods, and methods otherwise guaranteed not to alter the state of an object (or invalidate outstanding references and iterators of a container) from different threads to the same object.
  3. It is not safe for different threads to simultaneously access the same object when at least one thread calls non-`const` methods, or methods that invalidate outstanding references or iterators to the object. The programmer is responsible for using thread synchronization primitives to avoid such situations.

This is the library used by default when using GCC 4.0 and is appropriate when targeting OS X v10.3.9 and later. For a list of caveats for using this library, see [Caveats for Using the New C++ Runtimes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmnryfvjvomy).

In Xcode 2.3, a new version of the static C++ standard library `libstdc++-static.a` was introduced. You can link against the new static C++ standard library using Xcode 2.3 or the command line. To link against the library using Xcode, simply set "C++ Standard Library Type" in the build settings to "Static". To link against this library on the command line, use `gcc` instead of `g++` and append the following two commands to the end of the command: `-shared-libgcc` and `-lstdc++-static`. For example:

```
gcc one.o two.o -o my_application -shared-libgcc -lstdc++-static
```

For a list of caveats for using this library, see [Caveats for Using the New C++ Runtimes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmnryfvjvomy) and the next section.

The new static C++ standard library marks all of its symbols as "hidden", which means those symbols are not exported by an application that links to the library. It is still possible, however, for symbols from the C++ library to be exported by your application. For example, your application might include symbols from the library in header files or other visible locations. To prevent symbols from being accidentally exported, you must use an export list for any binaries that link against the static C++ library. (For more information about the use of export lists, see [Reducing the Number of Exported Symbols](../Xcode%20Build%20System%20Guide/Linking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmojufvjvomy). For information on using visibility pragmas and visibility switches to control symbol visibility in your own code, see [Controlling Symbol Visibility](Controlling%20Symbol%20Visibility.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmnzqfvbuuqshijeeksq).)

Callback functions (such as registered with `std::set_terminate`) are only effective when triggered within the same code module.

This static library has the same size disadvantages as the one used with gcc 3.3. For details about this issue, see [Advantages of a Shared C++ Runtime](Overview%20of%20the%20C%2B%2B%20Runtime%20Environment.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmnrxfu4tonbyg4).

[Next](Creating%20Compatible%20Libraries.md)[Previous](Overview%20of%20the%20C%2B%2B%20Runtime%20Environment.md)

