---
title: 'init(array:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscountedset/init(array:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscountedset/init(array:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscountedset/init%28array%3A%29.json'
content_hash: 'sha256:9dbcdbddf6a2b3e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCountedSet](../nscountedset.md)

# init(array:)

<sub>Initializer</sub>

Returns a counted set object initialized with the contents of a given array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(array: [Any])
```

## Parameters

- `array` — An array of objects to add to the new set.

## Return Value

An initialized counted set object with the contents of `array`. The returned object might be different than the original receiver.

## See Also

### Related Documentation

- [Collections Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Collections.html#//apple_ref/doc/uid/10000034i)
- [- initWithArray:](<../nsset/init(array_).md>) — Initializes a newly allocated set with the objects that are contained in a given array.

### Initializing a Counted Set

- [- initWithSet:](<init(set_).md>) — Returns a counted set object initialized with the contents of a given set.
- [- initWithCapacity:](<init(capacity_).md>) — Returns a counted set object initialized with enough memory to hold a given number of objects.
