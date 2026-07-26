---
title: 'setWithCapacity:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableset/setwithcapacity:'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableset/setwithcapacity:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableset/setwithcapacity%3A.json'
content_hash: 'sha256:dfcbf7e12535bdbf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableSet](../nsmutableset.md)

# setWithCapacity:

<sub>Type Method</sub>

Creates and returns a mutable set with a given initial capacity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) setWithCapacity:(NSUInteger) numItems;
```

## Parameters

- `numItems` — The initial capacity of the new set.

## Return Value

A mutable set with initial capacity to hold `numItems` members.

## Discussion

Mutable sets allocate additional memory as needed, so `numItems` simply establishes the object’s initial capacity.

## See Also

### Related Documentation

- [set](../nsset/set.md) — Creates and returns an empty set.
- [Collections Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Collections.html#//apple_ref/doc/uid/10000034i)
- [+ setWithObjects:count:](<../nsset/init(objects_count_)-65ni4.md>) — Creates and returns a set containing a specified number of objects from a given C array of objects.

### Creating a mutable set

- [- initWithCapacity:](<init(capacity_).md>) — Returns an initialized mutable set with a given initial capacity.
- [- init](<init().md>) — Initializes a newly allocated set.
