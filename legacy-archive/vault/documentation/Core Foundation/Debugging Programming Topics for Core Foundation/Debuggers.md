---
title: Debugging Programming Topics for Core Foundation
apple_id: 10000126i
resource_type: Guide
platform: macOS
topic: General
technology: CoreFoundation
published: '2003-01-17'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDebugging/Concepts/Debugger.html
archived_at: '2026-07-15T07:22:20.162710Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging Programming Topics for Core Foundation](Introduction%20to%20Debugging.md)


[Next](Handling%20Errors.md)[Previous](Core%20Foundation%20Libraries.md)

# Debuggers

You can use the debugger to reveal the contents
of Core Foundation objects, but how you use it depends on your development
platform.

- _Mac OS X_: Because Core Foundation
  uses opaque types, `CFShow` is
  a convenient tool for discovering the contents of objects. Call `CFShow` within
  the debugger or programmatically on an object to print a description
  of that object. The description is appropriate to the type of object.
  For example, calling `CFShow` on
  CFNumber prints a number; for a CFArray, `CFShow` prints
  information general to the array as well as information on each
  element of the array.
- _Mac OS 9_: Because you cannot use the debugger
  to call functions (such as `CFShow`)
  at runtime, you must use other techniques to examine memory. Consult
  the Core Foundation release notes for the latest debugging tips
  and techniques.

[Next](Handling%20Errors.md)[Previous](Core%20Foundation%20Libraries.md)

