---
title: Framework Programming Guide
apple_id: 10000183i
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2013-09-17'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFrameworks/Tasks/IncludingFrameworks.html
archived_at: '2026-07-15T08:15:43.818566Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Framework Programming Guide](Introduction%20to%20Framework%20Programming%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Installing%20Your%20Framework.md)

# Including Frameworks

For OS X software developers the guideline for including header files and linking with system software is straightforward: add the framework to your project and include only the top-level header file in your source files. For umbrella frameworks, include only the umbrella header file.

To include a framework in your Xcode project, choose Project > Add to Project and select the framework directory. Alternatively, you can control-click your project group and choose Add Files > Existing Frameworks from the contextual menu. When you add an existing framework to your project, Xcode asks you to associate it with one or more targets in your project. Once associated, Xcode automatically links the framework against the resulting executable.

You include framework header files in your code using the `#include` directive. If you are working in Objective-C, you may use the `#import` directive instead of the `#include` directive. The two directives have the same basic results. but the `#import` directive guarantees that the same header file is never included more than once. There are two ways for including framework headers:

```objc
#include <Framework_name/Header_filename.h>
#import <Framework_name/Header_filename.h>
```

In both cases, `Framework_name` is the name of the framework and `Header_filename` is the name of a header file in that framework or in one of its subframeworks.

When including framework header files, it is traditional to include only the master framework header file. The master header file is the header file whose name matches the name of the framework. For example, the Address Book framework has a master header file with the name `AddressBook.h`. To include this header in your source, you would use the following directive:

```objc
#include <AddressBook/AddressBook.h>
#import <AddressBook/AddressBook.h>
```

For most frameworks, you can include header files other than the master header file. You can include any specific header file you want as long as it is available in the framework’s `Headers` directory. However, if you are including an umbrella framework, you must include the master header file. Umbrella frameworks do not allow you to include the headers of their constituent subframeworks directly. See [Restrictions on Subframework Linking](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2toljzg4ytioi) for more information.

If your project links to frameworks that are not included in any of the standard locations, you must explicitly specify the location of that framework before Xcode can locate its header files. To specify the location of such a framework, add the directory containing the framework to the “Framework Search Paths” option of your Xcode project. Xcode passes this list of directories to the compiler and linker, which both use the list to search for the framework resources.

If you are worried that including a master header file may cause your program to bloat, don’t worry. Because OS X interfaces are implemented using frameworks, the code for those interfaces resides in a dynamic shared library and not in your executable. In addition, only the code used by your program is ever loaded into memory at runtime, so your in-memory footprint similarly stays small.

As for including a large number of header files during compilation, once again, don’t worry. Xcode provides a precompiled header facility to speed up compile times. By compiling all the framework headers at once, there is no need to recompile the headers unless you add a new framework. In the meantime, you can use any interface from the included frameworks with little or no performance penalty.

OS X includes two mechanisms for ensuring that developers link only with umbrella frameworks. One mechanism is an Xcode feature that prevents you from selecting subframeworks. The other mechanism is a compile-time error that occurs when you attempt to include subframework header files.

In Xcode, the Add Frameworks command displays the available frameworks in `/System/Library/Frameworks`. However, when you select one of these frameworks, the Open dialog displays information about the framework and not a list of subdirectories.

If you try to include a header file that is in a subframework, Xcode generates a compile-time error message. The umbrella header files and the subframework header files contain preprocessor variables and checks to guard against the inclusion of subframework header files. If you compile your project with an improper `#include` statement, the compiler generates an error message.

[Next](Document%20Revision%20History.md)[Previous](Installing%20Your%20Framework.md)

