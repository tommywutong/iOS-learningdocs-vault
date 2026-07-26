---
title: hashFunction
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspointerfunctions/hashfunction
source_url: 'https://developer.apple.com/documentation/foundation/nspointerfunctions/hashfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointerfunctions/hashfunction.json'
content_hash: 'sha256:872c69fb4f5ed5f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPointerFunctions](../nspointerfunctions.md)

# hashFunction

<sub>Instance Property</sub>

The hash function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hashFunction: ((UnsafeRawPointer, ((UnsafeRawPointer) -> Int)?) -> Int)? { get set }
```

## See Also

### Personality Functions

- [isEqualFunction](isequalfunction.md) — The function used to compare pointers.
- [sizeFunction](sizefunction.md) — The function used to determine the size of pointers.
- [descriptionFunction](descriptionfunction.md) — The function used to describe elements.
