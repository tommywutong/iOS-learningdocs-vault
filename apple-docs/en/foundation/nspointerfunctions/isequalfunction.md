---
title: isEqualFunction
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspointerfunctions/isequalfunction
source_url: 'https://developer.apple.com/documentation/foundation/nspointerfunctions/isequalfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointerfunctions/isequalfunction.json'
content_hash: 'sha256:7c3d45997d04c78f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPointerFunctions](../nspointerfunctions.md)

# isEqualFunction

<sub>Instance Property</sub>

The function used to compare pointers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isEqualFunction: ((UnsafeRawPointer, UnsafeRawPointer, ((UnsafeRawPointer) -> Int)?) -> ObjCBool)? { get set }
```

## See Also

### Personality Functions

- [hashFunction](hashfunction.md) — The hash function.
- [sizeFunction](sizefunction.md) — The function used to determine the size of pointers.
- [descriptionFunction](descriptionfunction.md) — The function used to describe elements.
