---
title: Code Loading Programming Topics
apple_id: 10000052i
resource_type: Guide
platform: macOS
topic: General
technology: Foundation
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingCode/Tasks/runtime.html
archived_at: '2026-07-15T07:16:32.497387Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Code Loading Programming Topics](Introduction%20to%20Dynamically%20Loading%20Code.md)


[Next](Document%20Revision%20History.md)[Previous](Preventing%20Name%20Conflicts.md)

# Loading Objective-C Libraries From Java

To load Objective-C dynamic libraries into Java applications, use the NSRuntime class. If the libraries are contained within a bundle, using the NSBundle class may be more appropriate.

NSRuntime’s principal method, `loadLibrary`, takes a String argument identifying the dynamic library to load. The string can be either the absolute path to the library or just the library name. If just the library name is given, either with or without the standard prefix `lib` or suffix `.dylib`, NSRuntime searches through a list of directories until it finds the library. For example, to load a library named `libMyCode.dylib` located at `/usr/lib`, all of the following works:

```
NSRuntime.loadLibrary("/usr/lib/libMyCode.dylib");
// Or, if /usr/lib is in the search paths
NSRuntime.loadLibrary("MyCode");
NSRuntime.loadLibrary("libMyCode.dylib");
```

After loading the library, the library is initialized by calling the function _basename_`Initialization` where _basename_ is the library’s name with the prefix and suffix stripped off. For example, when creating a library named `libMyCode.dylib`, create a function named `MyCodeInitialization` to initialize the library when it gets loaded. The function takes no arguments.

If the library is not found or if the library lacks an initialization function, the application exits with an `UnsatisfiedLinkError` error.

The NSRuntime class manages a list of directories that are searched when you attempt to load a library without providing its absolute path. Initially, the search path includes `/usr/lib/java` and `/usr/local/lib/java`. You can add paths to the list by using the method `addPathToLibrarySearchPaths`. This method takes a single String argument containing the absolute path of the directory to add to the search list. For example, to add `/usr/lib` to the list, do the following:

```
NSRuntime.addPathToLibraryPaths("/usr/lib");
```

To obtain the current list of search paths, invoke `librarySearchPaths`.

[Next](Document%20Revision%20History.md)[Previous](Preventing%20Name%20Conflicts.md)

