---
title: Core Foundation Design Concepts
apple_id: 10000122i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: General
technology: CoreFoundation
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/OtherTypes.html
archived_at: '2026-07-15T07:22:25.185603Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Foundation Design Concepts](Introduction%20to%20Core%20Foundation%20Design%20Concepts.md)


[Next](Comparing%20Objects.md)[Previous](Naming%20Conventions.md)

# Other Types

Core Foundation defines a number of data types for general use in functions. The purpose of some of these types is to abstract primitive values that might have to change as the processor address space changes. The CFIndex type, for example, is used in index, count, length, and size parameters. The CFOptionFlags type is used for bitfield parameters and the CFHashCode type holds hashing results returned from the `CFHash` function and certain hashing callbacks.

Other base types are used in functions that take and return comparison and range values. CFRange is a structure that specifies any part of a linear sequence of items, from characters in a string to elements in a collection. For comparison functions, the CFComparisonResult type defines `enum` constants to represent appropriate return values (equal, less than, greater than). Some Core Foundation functions take callbacks to comparator functions; if you want a custom comparator, the function must conform to the signature specified by the CFComparatorFunction type.

Other opaque types provided by Core Foundation are discussed in separate topics.

[Next](Comparing%20Objects.md)[Previous](Naming%20Conventions.md)

