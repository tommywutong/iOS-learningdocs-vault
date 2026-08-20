---
title: Building Objective-C static libraries with categories
apple_id: DTS10004097
resource_type: QA
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2014-08-05'
source_url: https://developer.apple.com/library/archive/qa/qa1490/_index.html
archived_at: '2026-07-18T02:31:25.334930Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1490

# Building Objective-C static libraries with categories

## Q:  How do I fix "selector not recognized" runtime exceptions when trying to use category methods from a static library?

A: If you're seeing a "selector not recognized" runtime exception when calling a [category method](https://developer.apple.com/library/ios/documentation/General/Conceptual/DevPedia-CocoaCore/Category.html) that is implemented in a static library, you are hitting the link-time build issue described here, and need to add the -ObjC linker flag to your project, by following these steps:

1. In Xcode, choose __View__ > __Navigators__ > __Show Project Navigator__, or press `⌘1`.
2. Select your project under the __PROJECT__ heading in the Project Navigator, then select the __Build Settings__ tab.
3. Scroll down to the __Other Linker Flags__ build setting under the __Linking__ collection, or type "Other Linker Flags" into the search bar.
4. Set the value of the __Other Linker Flags__ build setting to `$(OTHER_LDFLAGS) -ObjC`.

__Figure 1__  Modifying the Other Linker Flags build setting

!!

If adding the `-ObjC` flag isn't fixing the problem, double check that a conflicting Target build setting is not overriding it, by following the above steps, but selecting the current target under "TARGETS" in step 2, instead of the project.

The most common causes of a "selector not recognized" exception are:

The method really does not exist. Check your spelling. Check documentation to verify that the method exists on the version of the operating system your app is using.

Your app is trying to use an object after it has been deallocated, use the Zombies instrument to debug this kind of problem. You are seeing "selector not recognized" because the memory has been re-allocated as a different kind of object.

An impedance mismatch between UNIX static libraries and the dynamic nature of Objective-C can cause category methods in static libraries to not be linked into an app, resulting in "selector not recognized" exceptions when the methods aren't found at runtime.

When a C program is compiled, each "[source file](http://en.wikipedia.org/wiki/Translation_unit_%28programming%29)" is turned into an "object file" that contains executable functions and static data. The [linker](https://en.wikipedia.org/wiki/Linker_%28computing%29) glues these object files together into a final executable. That executable is eventually bundled into an app by Xcode.

When a source file uses something (like a function) defined in another file, then an __undefined symbol__ is written into the object file, to "stand in" for the missing thing. The linker resolves these symbols by pulling in the object files that include definitions of undefined symbols when building the final executable.

For example, if `main.c` uses the function `foo()`, where `foo` is defined in another file, `B.c`, then the object file `main.o` will have an unresolved symbol for `foo()`, and `B.o` will include an implementation of `foo()`. At link time, `B.o` will be brought into the final executable, so that the code in `main.o` now references the implementation of `foo()` defined in `B.o`.

A UNIX static library is just a collection of object files. Normally the linker only pulls in an object file from a static library if doing so would resolve some undefined symbol. Not pulling in all object files reduces the size of the final executable.

The dynamic nature of Objective-C complicates things slightly. Because the code that implements a method is not determined until the method is actually called, Objective-C does not define linker symbols for methods. Linker symbols are only defined for classes.

For example, if main.m includes the code `[[FooClass alloc] initWithBar:nil];` then `main.o` will contain an undefined symbol for `FooClass`, but no linker symbols for the `-initWithBar:` method will be in `main.o`.

Since categories are a collection of methods, using a category's method does not generate an undefined symbol. This means the linker does not know to load an object file defining the category, if the class itself is already defined. This causes the same "selector not recognized" runtime exception you would see for any unimplemented method.

Passing the `-ObjC` option to the linker causes it to load __all__ members of static libraries that implement any Objective-C class or category. This will pickup any category method implementations. But it can make the resulting executable larger, and may pickup unnecessary objects. For this reason it is not on by default.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-08-05 | Removed discussion of workarounds that are unnecessary in Xcode 4 and later. Added pointers to more common causes of 'selector not recognized' errors. |
| 2010-04-30 | Describes how to pass the "-ObjC" option to the linker. Updated for Mac OS X v10.6 and later. |
| 2006-10-03 | Changed "and" to "an" in order to make the content correct. |
| 2006-09-25 | New document that describes how to properly build Objective-C static libraries that contain categories on existing classes. |

