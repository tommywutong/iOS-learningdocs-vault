---
title: Concepts in Objective-C Programming
apple_id: TP40010810
resource_type: Guide
platform: watchOS|iOS|macOS
topic: General
technology: null
published: '2012-01-09'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/ObjectAllocation/ObjectAllocation.html
archived_at: '2026-07-15T07:33:41.930393Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Concepts in Objective-C Programming](About%20the%20Basic%20Programming%20Concepts%20for%20Cocoa%20and%20Cocoa%20Touch.md)


[Next](Object%20Initialization.md)[Previous](Introspection.md)

# Object Allocation

When you allocate an object, part of what happens is what you might expect, given the term. Cocoa allocates enough memory for the object from a region of application virtual memory. To calculate how much memory to allocate, it takes the object’s instance variables into account—including their types and order—as specified by the object’s class.

To allocate an object, you send the message [alloc](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/alloc) or [allocWithZone:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/allocWithZone:) to the object’s class. In return, you get a “raw” (uninitialized) instance of the class. The `alloc` variant of the method uses the application’s default zone. A zone is a page-aligned area of memory for holding related objects and data allocated by an application. See _[Advanced Memory Management Programming Guide](../../Cocoa/Advanced%20Memory%20Management%20Programming%20Guide/About%20Memory%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaytc2i)_ for more information on zones.

An allocation message does other important things besides allocating memory:

- It sets the object’s retain count to one.
- It initializes the object’s `isa`instance variable to point to the object’s class, a runtime object in its own right that is compiled from the class definition.
- It initializes all other instance variables to zero (or to the equivalent type for zero, such as `nil`, `NULL`, and `0.0`).

An object’s `isa` instance variable is inherited from [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/cl/NSObject), so it is common to all Cocoa objects. After allocation sets `isa` to the object’s class, the object is integrated into the runtime’s view of the inheritance hierarchy and the current network of objects (class and instance) that constitute a program. Consequently an object can find whatever information it needs at runtime, such as another object’s place in the inheritance hierarchy, the protocols that other objects conform to, and the location of the method implementations it can perform in response to messages.

In summary, allocation not only allocates memory for an object but initializes two small but very important attributes of any object: its `isa` instance variable and its retain count. It also sets all remaining instance variables to zero. But the resulting object is not yet usable. Initializing methods such as `init` must yet initialize objects with their particular characteristics and return a functional object.

[Next](Object%20Initialization.md)[Previous](Introspection.md)

