---
title: set
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsorderedset/set
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/set'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/set.json'
content_hash: 'sha256:33dd68a1d488b276'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# set

<sub>Instance Property</sub>

A representation of the set containing the contents of the ordered set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var set: Set<AnyHashable> { get }
```

## Discussion

This returns a proxy object for the receiving ordered set, which acts like an immutable set.

While you cannot mutate the ordered set through this proxy, mutations to the original ordered set will be reflected in the proxy and it will appear to change spontaneously, because a copy of the ordered set is not being made.

## See Also

### Converting Other Collections

- [array](array.md) — A representation of the ordered set as an array.
