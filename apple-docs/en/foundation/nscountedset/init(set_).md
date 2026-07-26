---
title: 'init(set:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscountedset/init(set:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscountedset/init(set:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscountedset/init%28set%3A%29.json'
content_hash: 'sha256:29268f2bd85134ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCountedSet](../nscountedset.md)

# init(set:)

<sub>Initializer</sub>

Returns a counted set object initialized with the contents of a given set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(set: Set<AnyHashable>)
```

## Parameters

- `set` — An set of objects to add to the new set.

## Return Value

An initialized counted set object with the contents of `set`. The returned object might be different than the original receiver.

## See Also

### Related Documentation

- [- initWithSet:](<../nsset/init(set_)-1xovx.md>) — Initializes a newly allocated set and adds to it objects from another given set.

### Initializing a Counted Set

- [- initWithArray:](<init(array_).md>) — Returns a counted set object initialized with the contents of a given array.
- [- initWithCapacity:](<init(capacity_).md>) — Returns a counted set object initialized with enough memory to hold a given number of objects.
