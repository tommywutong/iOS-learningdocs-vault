---
title: Carbon-Cocoa Integration Guide
apple_id: TP30000893
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CarbonCocoaDoc/Articles/WrapperFunctions.html
archived_at: '2026-07-15T07:11:57.988719Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Carbon-Cocoa Integration Guide](Introduction%20to%20Carbon-Cocoa%20Integration%20Guide.md)


[Next](Using%20Cocoa%20Functionality%20in%20a%20Carbon%20Application.md)[Previous](Interchangeable%20Data%20Types.md)

# Using Carbon and Cocoa in the Same Application

It has always been possible to integrate Cocoa and Carbon functionality in the same application, at least when it comes to functionality that doesn’t handle user interface elements.

For a Cocoa application to call Carbon functions, the only requirements are that the compiler has access to the appropriate header files and the application is linked against the appropriate frameworks. To access Carbon functionality, you can simply import `Carbon.h` and link against the Carbon framework. Since Objective-C is a superset of ANSI C, calling Carbon functions from a Cocoa application is easy (although prior to Mac OS X v10.2 the functions could not be user interface functions).

A Carbon application, by taking a few extra steps, can use many Cocoa and Objective-C technologies. To access Cocoa functionality, you can simply import `Cocoa.h` and link against the Cocoa framework. To access other Objective-C technologies, you may need to import additional headers and link against additional frameworks. For example, to use Web Kit, you need to import `WebKit.h` and link against the WebKit framework.

You also need to take these steps:

- Prepare your Carbon application to use Cocoa by calling the [NSApplicationLoad](https://developer.apple.com/documentation/appkit/1428475-nsapplicationload) function. Typically, you do this in your main function before executing any other Cocoa code.
- In functions where you’re using Cocoa, allocate and initialize an [NSAutoreleasePool](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAutoreleasePool/Description.html#//apple_ref/occ/cl/NSAutoreleasePool) object and release it when it is no longer needed. Note that if your application is running in Mac OS X v10.4 or later, an autorelease pool already exists when your functions are called, directly or indirectly, by the toolbox. For example, an `NSAutoReleasePool` object is automatically established and drained in the following locations:

  - `RunApplicationEventLoop`
  - `RunAppModalLoopForWindow`
  - `ModalDialog`
  - Window drag and resize tracking
  - Control tracking and indicator dragging
  - Across dispatch of an event by the event dispatcher target
  - When a window's compositing views are redrawn
- Use the Objective-C compiler to build those parts of your project that use Cocoa. In Xcode, there are several ways to do this:

  - Use Objective-C filename extensions.
  - Use the File Info panel to set the file type of a source file to `sourcecode.c.objc`.
  - Change the project or target build setting “Compile Sources As” to Objective-C.

When integrating Objective-C code into a Carbon project, a common approach is to write C-callable wrapper functions (or simply C-wrapper functions) for the Objective-C portion of the code. In the context of Carbon and Cocoa integration, a _C-callable wrapper function_ is a C function whose body contains Objective-C code that allows data to be passed to or obtained from Cocoa. These C-wrapper functions can be placed in a separate Objective-C source file and compiled using the Objective-C compiler.

Let’s look at a typical scenario for a Carbon application that accesses functionality provided in a Cocoa source file. The Cocoa source must contain all the necessary Objective-C code for its classes and methods. It must also contain a C-callable wrapper function for each method whose functionality is needed by the Carbon application. For example, for a `changeText:` method that takes a string and manipulates it in some way, the C-callable wrapper function would look similar to the following:

```
OSStatus changeText (CFStringRef message)
{
    NSAutoreleasePool *localPool;

    localPool = [[NSAutoreleasePool alloc] init];
    [[Controller sharedController] changeText:(NSString *)message];
    [localPool release];
    return noErr;
}
```

In summary, here’s how C-callable wrapper functions are used to allow Carbon applications to access Cocoa functionality:

1. Access to the Cocoa functionality is provided in an Objective-C source file. The file contains C-callable wrapper functions for any Cocoa method that’s needed by the Carbon application.
2. The Carbon application invokes the C-wrapper functions as needed.

[Next](Using%20Cocoa%20Functionality%20in%20a%20Carbon%20Application.md)[Previous](Interchangeable%20Data%20Types.md)

