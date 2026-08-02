---
title: Debugging Programming Topics for Core Foundation
apple_id: 10000126i
resource_type: Guide
platform: macOS
topic: General
technology: CoreFoundation
published: '2003-01-17'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDebugging/Tasks/DebuggingUtilities.html
archived_at: '2026-07-15T07:22:21.669339Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging Programming Topics for Core Foundation](Introduction%20to%20Debugging.md)


[Next](Document%20Revision%20History.md)[Previous](Handling%20Errors.md)

# Debugging Utilities

Because Core Foundation types are opaque, it is difficult
to inspect the Core Foundation objects created by your code using
traditional means. However, Core Foundation implements a couple
of functions that print descriptions of Core Foundation objects,
either from your code or in any debugger that supports functions
calls.

The first of these functions is `CFShow`,
which takes a reference to any Core Foundation object (that is,
its sole parameter is typed as `CFTypeRef`).
This function calls the `CFDescription` function
on the object, causing it to return a reference to a CFString object
containing the description. The `CFShow` function
then prints this description to the output device.

The second “inspection” function is `CFShowStr`,
which takes a reference to a CFString object. This function displays
the attributes of a CFString object but not its contents.

[Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge2dkljrgaytambwfvbuqrcdjbcecsa) shows the information printed by both functions in
a debugger.

__Listing 1__  Calling
the inspection functions in a debugger

```
(gdb) s
stringGettingContentsAsCStringExample () at StringExample.c:105
105         str = CFStringCreateWithCString(NULL, "Hello World", CFStringGetSystemEncoding());
(gdb) n
111         bytes = CFStringGetCStringPtr(str, CFStringGetSystemEncoding());
(gdb) call CFShow(str)
Hello World
$1 = 0
(gdb) call CFShowStr(str)

Length 11
IsEightBit 1
HasLengthByte 1
HasNullByte 1
InlineContents 1
Allocator SystemDefault
Mutable 0
Contents 0x4e7c0
$2 = 17
(gdb)
```

[Next](Document%20Revision%20History.md)[Previous](Handling%20Errors.md)

