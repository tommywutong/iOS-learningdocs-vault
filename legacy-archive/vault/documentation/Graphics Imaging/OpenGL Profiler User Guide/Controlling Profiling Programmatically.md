---
title: OpenGL Profiler User Guide
apple_id: TP40006475
resource_type: Guide
platform: Xcode Developer Tools
topic: Languages & Utilities
technology: OpenGL
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/OpenGLProfilerUserGuide/ProgrammaticControl/ProgrammaticControl.html
archived_at: '2026-07-15T07:37:04.509383Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OpenGL Profiler User Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Identifying%20and%20Solving%20Performance%20Issues.md)

# Controlling Profiling Programmatically

You can add code to your application that allows it to interact with OpenGL Profiler during a profiling session. This chapter shows you how to perform these tasks programmatically:

- [Setting a Breakpoint](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinzvfvbuqnjqfvjvomi)
- [Writing Comments to the Trace Window](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinzvfvbuqnjqfvjvomq)
- [Controlling Trace Collection](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinzvfvbuqnjqfvjvomy)
- [Controlling Statistics Collection](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinzvfvbuqnjqfvjvona)

Your application can programmatically set breakpoints when it is attached to OpenGL Profiler.

To set a breakpoint:

1. Include the `CGLProfiler.h` and `CGLProfilerFunctionEnum.h` header files in your application.
2. Declare an array of three `GLint` values, set to the following:

   - The function ID, as defined in the header file `CGLProfilerFunctionEnum.h`.
   - The logical `OR` of `kCGLProfBreakBefore` or `kCGLProfBreakAfter`, indicating how you want the breakpoint to stop—before entering the OpenGL function, on return from it, or both.
   - A Boolean that turns the breakpoint on or off.
3. Call the function `CGLSetOption`, passing the array as a parameter.

[Listing 4-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinzvfvbuqnjqfvjvomjq) shows code that sets a breakpoint before the `CGLFlushDrawable` function.

__Listing 4-1__  Code that sets a breakpoint

```c
#include "OpenGL/CGLProfiler.h"
#include "OpenGL/CGLProfilerFunctionEnum.h"
...
   GLint myBreakpoint[] = { kCGLFECGLFlushDrawable, kCGLProfBreakBefore, 1;}
   CGLSetOption( kCGLGOEnableBreakpoint, myBreakpoint );
...
```


Your application can programmatically write comments to the Trace window during a profiling session. To write comments:

1. Include the `CGLProfiler.h` header file in your application.
2. Call the function `CGLSetOption` with the constant `kCGLGOComment` and your comment cast as a long.

[Listing 4-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinzvfvbuqnjqfvjvoni) shows code that writes a comment that looks like this in the Trace window:

`21561: 0.00 µs /* ***** My Comment is here ***** */`

__Listing 4-2__  Code that writes a comment to the Trace window

```c
#include <OpenGL/CGLProfiler.h>
...
  CGLSetOption(kCGLGOComment, (long) "***** My Comment is here *****");
...
```


Your application can programmatically control when to start and stop collecting a trace, which lets you control which traces to collect in a specific part of your application or during a particular period of time. You can also clear the Trace window.

To control trace collection:

1. Include the `CGLProfiler.h` header file in your application.
2. Call the function `CGLSetOption` with the constant `kCGLGOEnableFunctionTrace` and either `GL_TRUE` (to turn on trace collection) or `GL_FALSE` (to turn off trace collection).

[Listing 4-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinzvfvbuqnjqfvjvonq) shows code that enables trace collection.

__Listing 4-3__  Code that enables trace collection

```c
#include <OpenGL/CGLProfiler.h>
...
  CGLSetOption(kCGLGOEnableFunctionTrace, GL_TRUE);
...
```

To clear the Trace window:

1. Include the `CGLProfiler.h` header file in your application.
2. Call the function `CGLSetOption` with the constant `kCGLGOResetFunctionTrace` and the value `NULL`.

[Listing 4-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinzvfvbuqnjqfvjvony) shows code that enables trace collection.

__Listing 4-4__  Code that clears the Trace window

```c
#include <OpenGL/CGLProfiler.h>
...
  CGLSetOption(kCGLGOResetFunctionTrace, NULL);
...
```


You application can programmatically control when to start and stop collecting statistics. You must make sure that the Statistics window in OpenGL Profiler is open when you profile your application.

To control statistics collection:

1. Include the `CGLProfiler.h` header file in your application.
2. Call the function `CGLSetOption` with the constant `kCGLGOResetFunctionStatistics` and the value `NULL` to first reset counters to 0. This step is optional.
3. Call the function `CGLSetOption` with the constant `kCGLGOResetFunctionStatistics` and the value `GL_TRUE` to start statistics collection.
4. When you are done collecting statistics, call the function `CGLSetOption` with the constant `kCGLGOResetFunctionStatistics` and the value `GL_FALSE`.

[Listing 4-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinzvfvbuqnjqfvjvooa) shows code that resets counters, starts statistics collection, and then stops it.

__Listing 4-5__  Code that starts and stops statistics collection

```c
#include <OpenGL/CGLProfiler.h>
...
  // Reset counters to 0
  CGLSetOption(kCGLGOResetFunctionStatistics, NULL);
  // Start statistics collection
  CGLSetOption(kCGLGOEnableFunctionStatistics, GL_TRUE);
...
  // Stop statistics collection
  CGLSetOption(kCGLGOEnableFunctionStatistics, GL_FALSE);
...
```

[Next](Document%20Revision%20History.md)[Previous](Identifying%20and%20Solving%20Performance%20Issues.md)

