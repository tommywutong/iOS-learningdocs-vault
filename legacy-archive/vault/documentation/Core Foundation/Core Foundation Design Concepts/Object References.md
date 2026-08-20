---
title: Core Foundation Design Concepts
apple_id: 10000122i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: General
technology: CoreFoundation
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/ObjectReferences.html
archived_at: '2026-07-15T07:22:23.677035Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Foundation Design Concepts](Introduction%20to%20Core%20Foundation%20Design%20Concepts.md)


[Next](Polymorphic%20Functions.md)[Previous](Opaque%20Types.md)

# Object References

You refer to Core Foundation objects (opaque types) through references. In every header file for an opaque type, you will notice a line or two similar to the following:

```
typedef const struct __CFArray * CFArrayRef;
typedef struct __CFArray * CFMutableArrayRef;
```

Declarations such as these are pointer references to immutable and mutable versions of the (private) structure defining the opaque type. The parameters and return values of many Core Foundation functions take the type of these object references and never a `typedef` of the private structure. For example:

```
CFStringRef CFStringCreateByCombiningStrings(CFAllocatorRef alloc, CFArrayRef array, CFStringRef separatorString);
```

See [Varieties of Objects](Varieties%20of%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeydslkdjjbeksscjbea) for more on immutable, mutable, and other variants of opaque-type objects.

Every Core Foundation opaque type defines a unique type ID for its objects, as in `CFArrayRef` above for CFArray objects. A type ID is an integer of type `CFTypeID` that identifies the opaque type to which a Core Foundation object “belongs.” You use type IDs in various contexts, such as when you are operating on heterogeneous collections. Core Foundation provides programmatic interfaces for obtaining and evaluating type IDs.

In addition, Core Foundation defines a generic object-reference type, `CFTypeRef`, analogous to a root class in some object-oriented programming languages. This generic reference serves as a placeholder type for parameters and returned values of polymorphic functions, which can take references to any Core Foundation object. See [Polymorphic Functions](Polymorphic%20Functions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeydqlkdjjbeksscjbea) for more on this subject. See _[Memory Management Programming Guide for Core Foundation](../Memory%20Management%20Programming%20Guide%20for%20Core%20Foundation/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdo2i)_ for issues relating to memory management when using object references.

[Next](Polymorphic%20Functions.md)[Previous](Opaque%20Types.md)

