---
title: C++ Runtime Environment Programming Guide
apple_id: TP40001666
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2009-10-09'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/CppRuntimeEnv/Articles/CompatibleLibs.html
archived_at: '2026-07-15T07:24:21.594658Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [C++ Runtime Environment Programming Guide](Introduction.md)


[Next](Controlling%20Symbol%20Visibility.md)[Previous](Deploying%20Applications%20With%20the%20C%2B%2B%20Runtime.md)

# Creating Compatible Libraries

The GCC 4.0 compiler ships with version 6.0.3 of the dynamic C++ runtime. Future minor versions of the library are guaranteed to retain binary compatibility with version 6.0.3; however, major versions are not guaranteed to be compatible, and developers should assume that a future compiler release will include an incompatible version of `libstdc++.dylib`.

If you distribute dynamic shared libraries that use the dynamic C++ runtime, changes to that runtime could potentially break clients of your library. For example, this can happen if your library’s interface includes types or classes defined by the dynamic C++ runtime. The following sections explain ways to remain compatible between major updates to the dynamic C++ runtime.

Because any component of the dynamic C++ runtime may change between major versions, your own dynamic shared libraries must avoid using classes, templates, and structures of the dynamic C++ runtime in their exported interfaces. The size and layout of standard C++ classes may change between different versions of the dynamic C++ standard library. If that happens and your library exports interfaces that rely on the current class information, clients of your library will break and require recompilation with an updated version of your library.

For any symbols your library exports to clients, you should follow these rules.

- Avoid inheriting from classes in the dynamic C++ standard library, such as `std::ostream`.
- In your class definition, avoid member variables (even private members) whose type is a class defined by the dynamic C++ runtime. For example, do not include member variables of type `std::auto_ptr`.
- Avoid using classes defined in the dynamic C++ runtime as arguments or return values of functions or methods.
- If your function or method throws exceptions, be sure your exception classes do not derive from dynamic C++ runtime classes, such as `std::runtime_error`

Keep in mind that the prohibitions on using dynamic C++ runtime classes applies only to your exported symbols. Within your library’s internal implementation, you are free to use the classes of `libstdc++` as you choose. Also keep in mind that these rules are to prevent clients of your library from breaking when the dynamic C++ runtime is updated. Your own library might still require recompilation.

Remember that a dynamic shared library’s exported interface consists of all public symbols, not just classes and functions declared in the library’s header files. In particular, template instantiations are public by default. So, if you instantiate a template with the declaration `std::vector<my_type>`, your library exposes a public instance of `std::vector` and will experience problems with any major version changes to the dynamic C++ runtime.

As you create your library, you should be mindful of which interfaces you want to make public and mark them appropriately. For information on how to limit the exported symbols in your library, see [Controlling Symbol Visibility](Controlling%20Symbol%20Visibility.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmnzqfvbuuqshijeeksq).

In certain cases, a C++ application can supply code that is used by the dynamic C++ runtime itself. The most relevant example of this is when an application replaces the global `new` and `delete` operators. Rarer examples include I/O stream callbacks defined through `std::ios_base::register_callback` and user-defined facets imbued into the global locale.

If you implement your own version of `operator new`, that version is used by all other libraries that link with the same version of `libstdc++.dylib`. If this is not what you intended with your implementation, you should mark your version of the method with the `__private_extern__` tag to prevent it from ever being seen by other libraries.

For more information on controlling the visibility of symbols in your libraries, see [Controlling Symbol Visibility](Controlling%20Symbol%20Visibility.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmnzqfvbuuqshijeeksq).

[Next](Controlling%20Symbol%20Visibility.md)[Previous](Deploying%20Applications%20With%20the%20C%2B%2B%20Runtime.md)

