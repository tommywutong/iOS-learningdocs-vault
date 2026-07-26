---
title: pointerFunctions
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspointerarray/pointerfunctions
source_url: 'https://developer.apple.com/documentation/foundation/nspointerarray/pointerfunctions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointerarray/pointerfunctions.json'
content_hash: 'sha256:3eb47670a53cad6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPointerArray](../nspointerarray.md)

# pointerFunctions

<sub>Instance Property</sub>

The functions in use by the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var pointerFunctions: NSPointerFunctions { get }
```

## Discussion

The returned object is a new `NSPointerFunctions` object that you can modify and/or use directly to create other pointer collections.

## See Also

### Getting the Pointer Functions

- [NSPointerFunctions](../nspointerfunctions.md) — An instance of `NSPointerFunctions` defines callout functions appropriate for managing a pointer reference held somewhere else.
