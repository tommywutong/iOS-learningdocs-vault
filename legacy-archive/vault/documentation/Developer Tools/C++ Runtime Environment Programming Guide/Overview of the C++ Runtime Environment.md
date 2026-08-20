---
title: C++ Runtime Environment Programming Guide
apple_id: TP40001666
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2009-10-09'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/CppRuntimeEnv/Articles/CPPROverview.html
archived_at: '2026-07-15T07:24:21.089689Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [C++ Runtime Environment Programming Guide](Introduction.md)


[Next](Deploying%20Applications%20With%20the%20C%2B%2B%20Runtime.md)[Previous](Introduction.md)

# Overview of the C++ Runtime Environment

The C++ runtime environment has evolved over the course of OS X development. Early versions of the library were shipped as a static archive file while the latest version is delivered as a dynamic shared library. The following is a summary of the history of the runtime:

- __OS X v10.3.8 and earlier__ - the C++ standard library is available only as a static archive file. It can be compiled using GCC 3.3.
- __OS X v10.3.9 and later__ - the runtime is delivered as a dynamic shared library. System frameworks are modified to use the dynamic library but the static library is also available.

The following sections provide more detailed information about the dynamic and static C++ runtimes. An additional section provides information about checking the version numbers of the runtime.

In OS X v10.3.8 and earlier, the standard C++ library is packaged as the static archive file `libstdc++.a`. This library is designed with multiple clients in mind and provides syncing of I/O streams as well as hidden symbols to alleviate namespace conflicts. Symbols in the library are marked `__private_extern__` to prevent them from being exported to other code modules. Versions of this library are available in all versions of OS X but programs must be built using the GCC 3.3 compiler.

In OS X v10.3.9 and later, you have the option of linking against a static or dynamic version of the C++ runtime.

With the introduction of Xcode Tools 2.3, a new version of the standard C++ library is made available in the static archive file `libstdc++-static.a`. This new static library is closer in nature to the dynamic shared library introduced in OS X v10.3.9 than to the previous static library. It conforms to the Itanium C++ ABI and requires the use of GCC 4.0 for compilation. Programs linking to the library must run in OS X v10.3.9 or later. For more information, see [Deploying With the New Static Runtime](Deploying%20Applications%20With%20the%20C%2B%2B%20Runtime.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmnryfvjvomi).

In OS X v10.3.9 and later, the C++ runtime is available as a dynamic shared library `libstdc++.dylib`. This change in packaging brings the C++ runtime in line with the C runtime, which has always been packaged as part of the dynamic shared library `libSystem.dylib`. The dynamic library conforms to the Itanium C++ ABI, which is a standard for compiled C++ code that provides better link-compatibility between C++ binaries. Because it is shared, the namespace limitations present with static versions of the library are gone and symbols are no longer marked `__private_extern__`. For information about designing and using C++–based dynamic libraries, see _[Dynamic Library Programming Topics](../Dynamic%20Library%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnrz)_.

Packaging the standard C++ library as a dynamic shared library is important for ensuring performance and correctness of your program. If your executable links to `libstdc++.a` and to several dynamic shared libraries, and one or more of those shared libraries also links to `libstdc++.a`, then multiple copies of the library are loaded into memory at runtime.

For correctness, all components of a program should use the exact same copy of the standard C++ library. The reason is that some data in the C++ runtime must be shared by all components or unexpected results may occur. For example, if two components both use the C++ I/O mechanism to write to standard output, the results can become garbled if they use different buffers.

For performance, having multiple copies of the same library leads to increased disk activity as each copy is read into memory. The extra copies can also lead to increased paging and cache misses due to the increased memory footprint of the application. Eliminating the duplicated libraries can reduce the footprint of your application dramatically. For example, consider the following “hello world” program compiled with `libstdc++.a` and GCC 3.3:

```
int main ()
{
    std::cout << "Hello, World!\n" << std::endl;
    return 0;
}
```

The size of the resulting binary on an OS X v10.4 system is 650 KB. The same program compiled on the same system using GCC 4.0 and `libstdc++.dylib` is 17 KB.

GCC 4.0 conforms to the Itanium C++ ABI, which is a standard for compiled C++ code. The specifications for this standard are maintained by a multi-vendor consortium and cover issues such as name mangling, class member layout, virtual method invocation protocols, exception handling, and runtime type information (RTTI) formats. You can find the latest version of this specification at [http://www.codesourcery.com/cxx-abi/abi.html](http://www.codesourcery.com/cxx-abi/abi.html).

Because GCC 4.0 conforms to the Itanium C++ ABI, C++ objects are link-compatible with objects built by other OS X compilers that conform to this specification. Apple guarantees that future releases of GCC for OS X will also conform to the Itanium C++ ABI. This means that developers may safely ship dynamic shared libraries whose interfaces involve C++ classes, albeit with some caveats:

- Apple guarantees ABI stability only for core language features. It does not guarantee stability for library classes, including `std::string`, `std::map<T>`, and `std::ostream` among others.
- Apple does not guarantee binary compatibility between different major versions of `libstdc++`. GCC 4.0 ships with version 6.0.3 of the library. If a new major version (version 7.0.0) is released in the future, that library is not guaranteed to be compatible with 6.x versions.
- Binary compatibility between different versions of a third-party dynamic shared library also depends on the design of the library, not just on the compiler support for a standard ABI. You must ensure that you do not introduce compatibility issues.

If you are designing a dynamic shared library for distribution, it is still your responsibility to ensure that you do not create binary compatibility problems. For example, you should not introduce member variables or virtual methods to a base class. Doing so causes a fragile base class problem and requires clients of the library to be recompiled.

For more information on binary compatibility, see [Creating Compatible Libraries](Creating%20Compatible%20Libraries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmnrzfvbeeq2fjjbekry).

Traditionally, Xcode has shipped with matching versions of the GCC compiler and the C++ runtime. However, Xcode 3.0 broke with this tradition by shipping version 4.2 of GCC with version 4.0 of the runtime. You may need to check for this configuration to write portable code. The compiler macros `__GNUC__` and `__GNUC_MINOR__` are defined as the major and minor version numbers of the compiler itself. In the SDKs included in Xcode 3.2 and later, the macros `__GNUC_LIBSTD__` and `__GNUC_LIBSTD_MINOR__` are defined as the major and minor version numbers of the runtime. All four macros are defined at compile time only, not at run time.

The following example shows how to use macros to check the version of the C++ runtime:

```c
#if (__GNUC_LIBSTD__ > 4) || ((__GNUC_LIBSTD__ == 4) && (__GNUC_LIBSTD_MINOR__ >= 2))
#include <ext/atomicity.h>
#else
#include <bits/atomicity.h>
#endif
```

[Next](Deploying%20Applications%20With%20the%20C%2B%2B%20Runtime.md)[Previous](Introduction.md)

