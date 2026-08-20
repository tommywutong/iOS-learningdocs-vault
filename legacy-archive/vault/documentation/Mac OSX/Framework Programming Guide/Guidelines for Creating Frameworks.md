---
title: Framework Programming Guide
apple_id: 10000183i
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2013-09-17'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFrameworks/Concepts/CreationGuidelines.html
archived_at: '2026-07-15T08:15:36.732307Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Framework Programming Guide](Introduction%20to%20Framework%20Programming%20Guide.md)


[Next](Creating%20a%20Framework.md)[Previous](Frameworks%20and%20Weak%20Linking.md)

# Guidelines for Creating Frameworks

The following sections provide guidance on how best to implement custom frameworks.

Elements in the global namespace, such as classes, functions, and global variables should all have unique names. While two-level namespaces help the dynamic-link editor find the correct symbols at runtime, the feature does not prevent static link errors from occurring because of multiply-defined symbols. For example, suppose two different frameworks define a symbol with the same name. If you were to create a project that included both frameworks, you would encounter static linking errors if you referenced the symbol in question. The static linker is responsible for selecting which framework to use and to then generate the two-level namespace hint needed by the dynamic link editor. Because both frameworks define the symbol, the static linker cannot choose and generates an error.

You should try to choose names that clearly associate each symbol with your framework. For example, consider adding a short prefix to all external symbol names. Prefixes help differentiate the symbols in your framework from those in other frameworks and libraries. They also make it clear to other developers which framework is being used. Typical prefixes include the first couple of letters or an acronym of your framework name. For example, functions in the Core Graphics framework use the prefix “CG”.

If you are writing a category for an Objective-C class, you should also use some sort of unique prefix in your method names. Because categories can be loaded dynamically from multiple sources, a unique prefix helps ensure that the methods in your category don’t conflict with those in other categories.

For detailed guidelines on Cocoa naming conventions, see _[Coding Guidelines for Cocoa](../../Cocoa/Coding%20Guidelines%20for%20Cocoa/Introduction%20to%20Coding%20Guidelines%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2dm2i)_.

Before you actually create a custom framework, you should carefully consider its intended use. There is a certain amount of overhead associated with loading and using frameworks at runtime. While this overhead is not high—especially if your framework and application are prebound—it may be unnecessary in some situations.

Frameworks are most effective when their code is shared by multiple applications. If you are designing a suite of applications, you may create a custom framework to store common code accessed by all applications in the suite. Similarly, you may want to create a private framework internally to separate out generic, reusable code from your application-specific code. Although you may embed this framework in each application you create, you simplify your maintenance of the reusable code.

Frameworks provide shared resources for multiple applications. If you are defining a custom framework, you should keep that goal in mind. As much as possible, your framework should not contain code that is tied to a particular application. Instead, it should contain code that is reusable or that is common to multiple applications.

In addition to code, you can include other types of resources in your frameworks. In the `Resources` directory of your framework, you can include nib files, images, sound files, localized text, and any other type of resource that you might find in an application. At runtime, applications load your framework’s resources using the same bundle mechanism they use for their application-specific resources.

There are problems inherent with exporting C++ class interfaces from dynamic shared libraries. These problems are the result of a lack of standardized calling conventions for the extensions that differentiate the C++ language from C.

In order to eliminate linking problems between libraries built with different compilers, compiler vendors agreed to support a set standardized calling conventions for the C language. These standards required the vendors to generate C code in a consistent way that guaranteed the code from one library could call code from another library. While such a standard has been proposed for the C++ language extensions, it has yet to be finalized. As a result, there is no guarantee that calls between two different C++ libraries would work.

If you are intent on using C++ code in your frameworks, the best way to avoid incompatibility issues is to wrap the interface for your C++ classes with ANSI C functions. By using C++ for your implementation and ANSI C for your interface, you can continue to develop in your preferred language while providing a compatible interface for clients to call.

If you need to export class interfaces from your framework, Apple recommends you use Objective-C instead of C++ to define your classes. The Objective-C language does have a standardized set of calling conventions that enable you to expose class interfaces from your frameworks.

For additional information and guidance about using C++ in shared libraries, see _[C++ Runtime Environment Programming Guide](../../Developer%20Tools/C%2B%2B%20Runtime%20Environment%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmnrw)_.

While it is possible to create umbrella frameworks using Xcode, doing so is unnecessary for most developers and is not recommended. Apple uses umbrella frameworks to mask some of the interdependencies between libraries in the operating system. In nearly all cases, you should be able to include your code in a single, standard framework bundle. Alternatively, if your code was sufficiently modular, you could create multiple frameworks, but in that case, the dependencies between modules would be minimal or nonexistent and should not warrant the creation of an umbrella for them.

OS X looks for public frameworks in several fixed locations on the system. If you are creating a framework for other developers to use, you should put it in one of these locations. If you are creating a private framework, you can either embed it inside an application or put it in a custom location. In either case, you must do some extra work to load your framework code and resources.

For details on where to install frameworks, see [Installing Your Framework](Installing%20Your%20Framework.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3dclkcijbugrscjjaq).

[Next](Creating%20a%20Framework.md)[Previous](Frameworks%20and%20Weak%20Linking.md)

