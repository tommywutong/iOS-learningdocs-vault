---
title: 'pointerArrayWithPointerFunctions:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nspointerarray/pointerarraywithpointerfunctions:'
source_url: 'https://developer.apple.com/documentation/foundation/nspointerarray/pointerarraywithpointerfunctions:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointerarray/pointerarraywithpointerfunctions%3A.json'
content_hash: 'sha256:36a6f2684e20ccf6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPointerArray](../nspointerarray.md)

# pointerArrayWithPointerFunctions:

<sub>Type Method</sub>

A new pointer array initialized to use the given functions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSPointerArray *) pointerArrayWithPointerFunctions:(NSPointerFunctions *) functions;
```

## Parameters

- `functions` — The pointer functions for the new instance.

## Return Value

A new pointer array initialized to use the given pointer functions.

## See Also

### Creating and Initializing a New Pointer Array

- [- initWithOptions:](<init(options_).md>) — Initializes the receiver to use the given options.
- [- initWithPointerFunctions:](<init(pointerfunctions_).md>) — Initializes the receiver to use the given functions.
- [pointerArrayWithOptions:](pointerarraywithoptions_.md) — Returns a new pointer array initialized to use the given options.
- [+ strongObjectsPointerArray](<strongobjects().md>) — Returns a new pointer array that maintains strong references to its elements.
- [pointerArrayWithStrongObjects](pointerarraywithstrongobjects.md) — Returns a new pointer array that maintains strong references to its elements. _(deprecated)_
- [+ weakObjectsPointerArray](<weakobjects().md>) — Returns a new pointer array that maintains weak references to its elements.
- [pointerArrayWithWeakObjects](pointerarraywithweakobjects.md) — Returns a new pointer array that maintains weak references to its elements. _(deprecated)_
