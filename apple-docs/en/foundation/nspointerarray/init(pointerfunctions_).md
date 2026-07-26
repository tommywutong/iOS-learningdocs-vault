---
title: 'init(pointerFunctions:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nspointerarray/init(pointerfunctions:)'
source_url: 'https://developer.apple.com/documentation/foundation/nspointerarray/init(pointerfunctions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointerarray/init%28pointerfunctions%3A%29.json'
content_hash: 'sha256:846dd0558853f85c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPointerArray](../nspointerarray.md)

# init(pointerFunctions:)

<sub>Initializer</sub>

Initializes the receiver to use the given functions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(pointerFunctions functions: NSPointerFunctions)
```

## Parameters

- `functions` — The pointer functions for the new instance.

## Return Value

The receiver, initialized to use the given functions.

## See Also

### Creating and Initializing a New Pointer Array

- [- initWithOptions:](<init(options_).md>) — Initializes the receiver to use the given options.
- [+ strongObjectsPointerArray](<strongobjects().md>) — Returns a new pointer array that maintains strong references to its elements.
- [+ weakObjectsPointerArray](<weakobjects().md>) — Returns a new pointer array that maintains weak references to its elements.
