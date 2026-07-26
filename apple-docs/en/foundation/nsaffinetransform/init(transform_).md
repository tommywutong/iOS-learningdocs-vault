---
title: 'init(transform:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsaffinetransform/init(transform:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsaffinetransform/init(transform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsaffinetransform/init%28transform%3A%29.json'
content_hash: 'sha256:be9f343440edf2f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAffineTransform](../nsaffinetransform.md)

# init(transform:)

<sub>Initializer</sub>

Initializes the receiver’s matrix using another transform object.

<sub>Mac Catalyst</sub>

```swift
convenience init(transform: NSAffineTransform)
```

<sub>macOS</sub>

```swift
convenience init(transform: AffineTransform)
```

## Parameters

- `transform` — The transform object whose matrix values should be copied to this object.

## Return Value

A new transform object initialized with the matrix values of `aTransform`.

## See Also

### Creating an Affine Transform

- [- init](<init().md>) — Initializes an affine transform matrix to the identity matrix.
