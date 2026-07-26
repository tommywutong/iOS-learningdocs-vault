---
title: 'init(options:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nspointerarray/init(options:)'
source_url: 'https://developer.apple.com/documentation/foundation/nspointerarray/init(options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointerarray/init%28options%3A%29.json'
content_hash: 'sha256:38f68a62f561f916'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPointerArray](../nspointerarray.md)

# init(options:)

<sub>Initializer</sub>

Initializes the receiver to use the given options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(options: NSPointerFunctions.Options = [])
```

## Parameters

- `options` — The pointer functions options for the new instance.

## Return Value

The receiver, initialized to use the given options.

## See Also

### Related Documentation

- [Collections Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Collections.html#//apple_ref/doc/uid/10000034i)

### Creating and Initializing a New Pointer Array

- [- initWithPointerFunctions:](<init(pointerfunctions_).md>) — Initializes the receiver to use the given functions.
- [+ strongObjectsPointerArray](<strongobjects().md>) — Returns a new pointer array that maintains strong references to its elements.
- [+ weakObjectsPointerArray](<weakobjects().md>) — Returns a new pointer array that maintains weak references to its elements.
