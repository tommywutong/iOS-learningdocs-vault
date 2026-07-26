---
title: sizeFunction
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspointerfunctions/sizefunction
source_url: 'https://developer.apple.com/documentation/foundation/nspointerfunctions/sizefunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointerfunctions/sizefunction.json'
content_hash: 'sha256:d46a24bbfb11b201'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPointerFunctions](../nspointerfunctions.md)

# sizeFunction

<sub>Instance Property</sub>

The function used to determine the size of pointers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sizeFunction: ((UnsafeRawPointer) -> Int)? { get set }
```

## Discussion

This function is used for copy-in operations (unless the collection has an object personality).

## See Also

### Personality Functions

- [hashFunction](hashfunction.md) — The hash function.
- [isEqualFunction](isequalfunction.md) — The function used to compare pointers.
- [descriptionFunction](descriptionfunction.md) — The function used to describe elements.
