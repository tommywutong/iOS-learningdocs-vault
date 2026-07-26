---
title: descriptionFunction
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspointerfunctions/descriptionfunction
source_url: 'https://developer.apple.com/documentation/foundation/nspointerfunctions/descriptionfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointerfunctions/descriptionfunction.json'
content_hash: 'sha256:0406579b2c612f38'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPointerFunctions](../nspointerfunctions.md)

# descriptionFunction

<sub>Instance Property</sub>

The function used to describe elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var descriptionFunction: ((UnsafeRawPointer) -> String?)? { get set }
```

## Discussion

This function is used by description methods for hash and map tables.

## See Also

### Personality Functions

- [hashFunction](hashfunction.md) — The hash function.
- [isEqualFunction](isequalfunction.md) — The function used to compare pointers.
- [sizeFunction](sizefunction.md) — The function used to determine the size of pointers.
