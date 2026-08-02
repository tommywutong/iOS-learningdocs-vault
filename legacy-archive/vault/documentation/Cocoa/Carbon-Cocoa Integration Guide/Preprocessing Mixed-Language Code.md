---
title: Carbon-Cocoa Integration Guide
apple_id: TP30000893
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CarbonCocoaDoc/Articles/CompilerPreprocessors.html
archived_at: '2026-07-15T07:11:54.489096Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Carbon-Cocoa Integration Guide](Introduction%20to%20Carbon-Cocoa%20Integration%20Guide.md)


[Next](Interchangeable%20Data%20Types.md)[Previous](Carbon%20and%20Cocoa%20User%20Interface%20Communication.md)

# Preprocessing Mixed-Language Code

Carbon and Cocoa use different languages for their APIs. Carbon uses C while Cocoa uses Objective-C. In addition, Carbon programmers may prefer to use C++. When you build an application that uses any combination of C, Objective-C, Objective-C++, and C++ files, you must make sure the compiler performs the appropriate preprocessing. The filename extension of the file you are compiling indicates the kind of compilation that is done, as shown in Table 1.

__Table 1__  Filename extensions and compilation

| Filename extension | Indicates to the compiler |
| `.c` | C source code that must be preprocessed |
| `.m` | Objective-C source code |
| `.mm` | Objective-C++ source code |
| `.h` | Header file (not to be compiled or linked) |
| `.cc`, `.cp`, `.cxx`, `.cpp`, `.c++`, `.C` | C++ source code that must be preprocessed |

In an Xcode project, you can override the filename extension of a source file by changing its file type. The file type determines how Xcode preprocesses and compiles the file. For example, suppose you want to add Objective-C code to a C source file with a `.c` filename extension. You can examine and change the file type of this source file as follows:

1. Select the C source file in the project window.
2. Open the File Info window and select the General pane.
3. Find the “File Type” setting.
4. Change its value to “sourcecode.c.objc”.

Now Xcode will compile the Objective-C code in the file.

You can also direct Xcode to handle all the source files in a project as one language, regardless of their filename extensions and file types. For example, suppose you want to add Objective-C code to many of your C++ source files. To specify that the compiler treat all source files as Objective-C++ files:

1. Select the project in the Groups and Files pane of the project window.
2. Open the the Project Info window and select the Build pane.
3. Find the “Compile Sources As” setting.
4. Change its value from “According to File Type” to “Objective-C++“.

Now Xcode will compile the Objective-C code in all your C++ files. You can also change this setting on a per-target basis.

For complete Xcode documentation, see the Tools category of the ADC Reference Library. The Xcode user guide is also available from the Help menu in the Xcode application.

[Next](Interchangeable%20Data%20Types.md)[Previous](Carbon%20and%20Cocoa%20User%20Interface%20Communication.md)

