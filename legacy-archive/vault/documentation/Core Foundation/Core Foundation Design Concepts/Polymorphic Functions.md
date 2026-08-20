---
title: Core Foundation Design Concepts
apple_id: 10000122i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: General
technology: CoreFoundation
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/PolymorphicFunctions.html
archived_at: '2026-07-15T07:22:25.686177Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Foundation Design Concepts](Introduction%20to%20Core%20Foundation%20Design%20Concepts.md)


[Next](Varieties%20of%20Objects.md)[Previous](Object%20References.md)

# Polymorphic Functions

Core Foundation provides several polymorphic functions. These functions can take any Core Foundation object as a parameter and (in one instance, `CFRetain`) can return any Core Foundation object. These parameters and return values are given the type of `CFTypeRef`, a generic object-reference type. CFType is analogous to a root class in object-oriented languages because its functions can be reused by all other objects.

You use polymorphic functions for operations that are common to all Core Foundation objects:

- Reference counting.

  CFType provides several polymorphic functions for manipulating and obtaining the reference count of objects. See _[Memory Management Programming Guide for Core Foundation](../Memory%20Management%20Programming%20Guide%20for%20Core%20Foundation/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdo2i)_ for more about these functions.
- Comparing objects.

  The `CFEqual` function compares any two Core Foundation objects (see [Comparing Objects](Comparing%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeytelkdjjbekscbifdq)). The basis of equality depends on the type of objects compared. For example, if both are CFString objects the test involves a character-by-character comparison.
- Hashing objects.

  The `CFHash` function returns a unique hash code identifying a Core Foundation object (see [Comparing Objects](Comparing%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeytelkdjjbekscbifdq)). You can use the hash code as a table address in a hash table structure. If two objects are equal (as determined by the `CFEqual` function), they must have the same hash value.
- Inspecting objects.

  CFType gives you the means to inspect objects and thereby learn about their contents and the type to which they “belong.” The `CFCopyDescription` function returns a string (more precisely, a reference to a CFString object) that describes an object. The `CFCopyTypeIDDescription` function, which takes a `CFTypeID` rather than a `CFTypeRef` parameter, returns a string reference that describes the opaque type identified by the type ID. These functions are primarily intended to assist debugging; see [Inspecting Objects](Inspecting%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeytglkdjjbekscbifdq) for more on these functions.

  You can also determine the opaque type to which a generically typed object belongs by getting its type ID with the `CFGetTypeID` function and then comparing that value with known type IDs. See [Inspecting Objects](Inspecting%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeytglkdjjbekscbifdq) for more on this task.

[Next](Varieties%20of%20Objects.md)[Previous](Object%20References.md)

