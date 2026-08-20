---
title: Variable arguments in Objective-C methods
apple_id: DTS10003482
resource_type: QA
platform: macOS
topic: Languages & Utilities
technology: null
published: '2005-01-13'
source_url: https://developer.apple.com/library/archive/qa/qa1405/_index.html
archived_at: '2026-07-18T02:30:31.761640Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1405

# Variable arguments in Objective-C methods

## Q:  How can I write a method that takes a variable number of arguments, like NSString's +stringWithFormat:?

A: How can I write a method that takes a variable number of arguments, like NSString's +stringWithFormat:?

Methods that take variable arguments are known as __variadic__ methods.

Keep in mind that the implementation of an Objective-C method is just a block of code, like a C function. The variadic argument macros described in the stdarg(3) manual page work the same way in a method as they do in an ordinary function.

Here's an example of an Objective-C category, containing a variadic method that appends all the objects in a nil-terminated list of arguments to an NSMutableArray instance:

__Listing 1__  A typical variadic method.

```objc
#import <Cocoa/Cocoa.h>  @interface NSMutableArray (variadicMethodExample)  - (void) appendObjects:(id) firstObject, ...; // This method takes a nil-terminated list of objects.  @end  @implementation NSMutableArray (variadicMethodExample)  - (void) appendObjects:(id) firstObject, ... { id eachObject; va_list argumentList; if (firstObject) // The first argument isn't part of the varargs list,   {                                   // so we'll handle it separately.   [self addObject: firstObject];   va_start(argumentList, firstObject); // Start scanning for arguments after firstObject.   while (eachObject = va_arg(argumentList, id)) // As many times as we can get an argument of type "id"       [self addObject: eachObject]; // that isn't nil, add it to self's contents.   va_end(argumentList);   } }  @end
```

See the stdarg(3) manual page for the full documentation of the `va_list` type, and the `va_start()`, `va_arg()`, and `va_end()` macros.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-01-13 | New document that how to implement methods which take a variable number of arguments. |

