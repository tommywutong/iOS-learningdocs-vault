---
title: Core Foundation Design Concepts
apple_id: 10000122i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: General
technology: CoreFoundation
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/VarietyOfObjects.html
archived_at: '2026-07-15T07:22:26.187719Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Foundation Design Concepts](Introduction%20to%20Core%20Foundation%20Design%20Concepts.md)


[Next](Naming%20Conventions.md)[Previous](Polymorphic%20Functions.md)

# Varieties of Objects

Opaque types come in up to three basic varieties, or “flavors,” based on the characteristics of editability and expandability expected in their objects:

- immutable and fixed size
- mutable and fixed size
- mutable and variable size

Mutable objects are editable, meaning their contents can be changed. Immutable objects are not editable; once they are created they cannot be changed. Any attempt to change an immutable object usually results in an error of some kind. A fixed-size object has a maximum limit that it can grow to; in the case of a CFString, that would be the number of characters, and for a collection the limit would be the number of elements.

Some opaque types, such as CFString and CFArray, can create all three flavors of objects. Most opaque types can create immutable, fixed-size objects and typically have at least one unqualified creation function to do the job (such as `CFArrayCreate`). The determinant for mutable fixed-size versus variable-size is the value of the capacity or maximum-length parameter in the _Type_`CreateMutable` function; any positive value results in a fixed-size object, but a 0 specifies a variable-size object.

References to mutable objects include “Mutable” in the type name, for example, `CFMutableStringRef`.

[Next](Naming%20Conventions.md)[Previous](Polymorphic%20Functions.md)

