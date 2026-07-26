---
title: 'orderedSetWithCapacity:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableorderedset/orderedsetwithcapacity:'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableorderedset/orderedsetwithcapacity:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableorderedset/orderedsetwithcapacity%3A.json'
content_hash: 'sha256:448f84afe1428db5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableOrderedSet](../nsmutableorderedset.md)

# orderedSetWithCapacity:

<sub>Type Method</sub>

Creates and returns an mutable ordered set with a given initial capacity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) orderedSetWithCapacity:(NSUInteger) numItems;
```

## Parameters

- `numItems` — The initial capacity of the new ordered set.

## Return Value

A mutable ordered set with initial capacity to hold `numItems` members.

## Discussion

Mutable ordered sets allocate additional memory as needed, so `numItems` simply establishes the set’s initial capacity.

## See Also

### Creating a Mutable Ordered Set

- [- initWithCapacity:](<init(capacity_).md>) — Returns an initialized mutable ordered set with a given initial capacity.
- [- init](<init().md>) — Initializes a newly allocated mutable ordered set.
