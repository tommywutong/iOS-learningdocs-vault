---
title: Debugging Programming Topics for Core Foundation
apple_id: 10000126i
resource_type: Guide
platform: macOS
topic: General
technology: CoreFoundation
published: '2003-01-17'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDebugging/Concepts/CFLibraries.html
archived_at: '2026-07-15T07:22:19.661076Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging Programming Topics for Core Foundation](Introduction%20to%20Debugging.md)


[Next](Debuggers.md)[Previous](Introduction%20to%20Debugging.md)

# Core Foundation Libraries

When Core Foundation is installed on a Mac
OS 9 systems, you have two libraries at your disposal: a production
library (`CoreFoundationLib`)
and a debug library (`CoreFoundationLib Debug`).
When you use the debug version of the library you automatically
get assertion checking on common programming errors such as

- accessing a collection out of bounds
- attempting to change an immutable object
- passing an argument of a wrong type

Currently assertions print a log message and cause a break
in the debugger.

The production version of the Core Foundation library is optimized
and performs no error checking; invalid parameters, even references
to the wrong Core Foundation type, will cause indeterminate and
probably incorrect behavior. Obviously, you should use the debug
version of the Core Foundation library during development to catch
errors in programming.

On Mac OS X, Core Foundation is a framework: a package consisting
of a dynamic shared library and associated resources, including
public header files. `CoreFoundation.framework` also
includes a production version and a debug version of the library.
To use the debug version, set the environment variable `DYLD_IMAGE_SUFFIX` to `_debug` before
running the application; the dynamic linker will then check for
and link against the debug versions of any dynamic libraries, such
as Core Foundation, that your application uses.

[Next](Debuggers.md)[Previous](Introduction%20to%20Debugging.md)

