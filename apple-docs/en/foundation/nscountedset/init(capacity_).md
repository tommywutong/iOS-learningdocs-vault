---
title: 'init(capacity:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscountedset/init(capacity:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscountedset/init(capacity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscountedset/init%28capacity%3A%29.json'
content_hash: 'sha256:85b61788dc4940e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCountedSet](../nscountedset.md)

# init(capacity:)

<sub>Initializer</sub>

Returns a counted set object initialized with enough memory to hold a given number of objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(capacity numItems: Int)
```

## Parameters

- `numItems` — The initial capacity of the new counted set.

## Return Value

A counted set object initialized with enough memory to hold `numItems` objects

## Discussion

The method is the designated initializer for [NSCountedSet](../nscountedset.md).

Note that the capacity is simply a hint to help initial memory allocation—the initial count of the object is `0`, and the set still grows and shrinks as you add and remove objects. The hint is typically useful if the set will become large.

## See Also

### Related Documentation

- [- initWithCapacity:](<../nsmutableset/init(capacity_).md>) — Returns an initialized mutable set with a given initial capacity.

### Initializing a Counted Set

- [- initWithArray:](<init(array_).md>) — Returns a counted set object initialized with the contents of a given array.
- [- initWithSet:](<init(set_).md>) — Returns a counted set object initialized with the contents of a given set.
