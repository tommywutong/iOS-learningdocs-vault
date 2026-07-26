---
title: NSAffineTransformStruct
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsaffinetransformstruct
source_url: 'https://developer.apple.com/documentation/foundation/nsaffinetransformstruct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsaffinetransformstruct.json'
content_hash: 'sha256:70c82742040f16f8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSAffineTransformStruct

<sub>Structure</sub>

A structure that defines the three-by-three matrix that performs an affine transform between two coordinate systems.

<sub>Mac Catalyst, macOS</sub>

```swift
struct NSAffineTransformStruct
```

## Overview

For more details, see [Cocoa Drawing Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40003290).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init()](<nsaffinetransformstruct/init().md>) — Initializes a zero-filled transformation matrix.
- [init(m11:m12:m21:m22:tX:tY:)](<nsaffinetransformstruct/init(m11_m12_m21_m22_tx_ty_).md>)

### Instance Properties

- [m11](nsaffinetransformstruct/m11.md) — An element of the transform matrix that contributes scaling, rotation, and shear.
- [m12](nsaffinetransformstruct/m12.md) — An element of the transform matrix that contributes scaling, rotation, and shear.
- [m21](nsaffinetransformstruct/m21.md) — An element of the transform matrix that contributes scaling, rotation, and shear.
- [m22](nsaffinetransformstruct/m22.md) — An element of the transform matrix that contributes scaling, rotation, and shear.
- [tX](nsaffinetransformstruct/tx.md) — An element of the transform matrix that contributes translation.
- [tY](nsaffinetransformstruct/ty.md) — An element of the transform matrix that contributes translation.

## See Also

### Accessing the Transformation Matrix

- [transformStruct](nsaffinetransform/transformstruct.md) — The matrix coefficients stored as the transformation matrix.
