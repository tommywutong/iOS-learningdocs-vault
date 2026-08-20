---
title: Debugging Programming Topics for Core Foundation
apple_id: 10000126i
resource_type: Guide
platform: macOS
topic: General
technology: CoreFoundation
published: '2003-01-17'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDebugging/Concepts/HandlingErrors.html
archived_at: '2026-07-15T07:22:20.659082Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging Programming Topics for Core Foundation](Introduction%20to%20Debugging.md)


[Next](Debugging%20Utilities.md)[Previous](Debuggers.md)

# Handling Errors

Mostly in the interest of code simplification,
Core Foundation functions do not follow the Mac OS `OSErr` convention
for error reporting. However, if you rigorously test your program
with the debug version of the Core Foundation library (or framework),
then the possibilities for error are much reduced.

Yet there can be occasions when you want to test whether a
function succeeds in its intended purpose and proceed conditionally
from there. By a common-sense interpretation of returned values
(and sometimes by a quick check of the reference documentation),
you can usually determine the reason for failure, as in these examples:

- If functions that are supposed to create or copy
  objects return `NULL`,
  the probable reason is an error in the allocation of memory.
- If functions that are supposed to return an element from a
  index-based collection (that is, a CFArray) return an indeterminate
  value, the probable cause is an index parameter that is out of bounds.
- If a function is supposed to return a CFArray of values, each
  element of which satisfies some condition specified by the function,
  and an empty CFArray is returned, then no object has satisfied that
  condition.

Some Core Foundation functions return a value of type `Boolean` or
an `enum` constant or some
other explicitly typed indication of the reason for an outcome.
Consult the Core Foundation reference documentation for an explanation
of these return values.

[Next](Debugging%20Utilities.md)[Previous](Debuggers.md)

