---
title: strongObjects()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspointerarray/strongobjects()
source_url: 'https://developer.apple.com/documentation/foundation/nspointerarray/strongobjects()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointerarray/strongobjects%28%29.json'
content_hash: 'sha256:984380e9724a91d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPointerArray](../nspointerarray.md)

# strongObjects()

<sub>Type Method</sub>

Returns a new pointer array that maintains strong references to its elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func strongObjects() -> NSPointerArray
```

## Return Value

A new pointer array that maintains strong references to its elements.

## See Also

### Creating and Initializing a New Pointer Array

- [- initWithOptions:](<init(options_).md>) — Initializes the receiver to use the given options.
- [- initWithPointerFunctions:](<init(pointerfunctions_).md>) — Initializes the receiver to use the given functions.
- [+ weakObjectsPointerArray](<weakobjects().md>) — Returns a new pointer array that maintains weak references to its elements.
