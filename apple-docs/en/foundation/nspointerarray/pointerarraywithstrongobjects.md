---
title: pointerArrayWithStrongObjects
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.5+（10.8 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nspointerarray/pointerarraywithstrongobjects
source_url: 'https://developer.apple.com/documentation/foundation/nspointerarray/pointerarraywithstrongobjects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointerarray/pointerarraywithstrongobjects.json'
content_hash: 'sha256:04c29d736bc43944'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPointerArray](../nspointerarray.md)

# pointerArrayWithStrongObjects

<sub>Type Method</sub>

Returns a new pointer array that maintains strong references to its elements.

> [!warning] Deprecated
> Use the [+ strongObjectsPointerArray](<strongobjects().md>) class method.

<sub>macOS</sub>

```objc
+ (id) pointerArrayWithStrongObjects;
```

## Return Value

A new pointer array that maintains strong references to its elements.

## See Also

### Creating and Initializing a New Pointer Array

- [- initWithOptions:](<init(options_).md>) — Initializes the receiver to use the given options.
- [- initWithPointerFunctions:](<init(pointerfunctions_).md>) — Initializes the receiver to use the given functions.
- [pointerArrayWithOptions:](pointerarraywithoptions_.md) — Returns a new pointer array initialized to use the given options.
- [pointerArrayWithPointerFunctions:](pointerarraywithpointerfunctions_.md) — A new pointer array initialized to use the given functions.
- [+ strongObjectsPointerArray](<strongobjects().md>) — Returns a new pointer array that maintains strong references to its elements.
- [+ weakObjectsPointerArray](<weakobjects().md>) — Returns a new pointer array that maintains weak references to its elements.
- [pointerArrayWithWeakObjects](pointerarraywithweakobjects.md) — Returns a new pointer array that maintains weak references to its elements. _(deprecated)_
