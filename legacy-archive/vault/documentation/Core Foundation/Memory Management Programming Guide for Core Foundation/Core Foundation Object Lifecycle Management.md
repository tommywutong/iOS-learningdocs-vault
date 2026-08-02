---
title: Memory Management Programming Guide for Core Foundation
apple_id: 10000127i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Performance
technology: CoreFoundation
published: '2009-10-21'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Articles/lifecycle.html
archived_at: '2026-07-15T07:22:29.268337Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Memory Management Programming Guide for Core Foundation](Introduction.md)


[Next](Copy%20Functions.md)[Previous](Ownership%20Policy.md)

# Core Foundation Object Lifecycle Management

The life span of a Core Foundation object is determined by its reference count—an internal count of the number of clients who want the object to persist. When you create or copy an object in Core Foundation, its reference count is set to one. Subsequent clients can claim ownership of the object by calling `CFRetain` which increments the reference count. Later, when you have no more use for the object, you call `CFRelease`. When the reference count reaches 0, the object’s allocator deallocates the object’s memory.

To increment the reference count of a Core Foundation object, pass a reference to that object as the parameter of the `CFRetain` function:

```
/* myString is a CFStringRef received from elsewhere */
myString = (CFStringRef)CFRetain(myString);
```


To decrement the reference count of a Core Foundation object, pass a reference to that object as the parameter of the `CFRelease` function:

```
CFRelease(myString);
```


When you copy an object, the resulting object has a reference count of one regardless of the reference count of the original object. For more on copying objects, see [Copy Functions](Copy%20Functions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge2dslkdjjbeksscjbea).

If you want to know the current reference count of a Core Foundation object, pass a reference to that object as the parameter of the `CFGetRetainCount` function:

```
CFIndex count = CFGetRetainCount(myString);
```

Note, however, that there should typically be little need to determine the reference count of a Core Foundation object, except in debugging. If you find yourself needing to know the retain count of an object, check that you are properly adhering to the ownership policy rules (see [Ownership Policy](Ownership%20Policy.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge2dqlkdjjbeksscjbea)).

[Next](Copy%20Functions.md)[Previous](Ownership%20Policy.md)

