---
title: transformStruct
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsaffinetransform/transformstruct
source_url: 'https://developer.apple.com/documentation/foundation/nsaffinetransform/transformstruct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsaffinetransform/transformstruct.json'
content_hash: 'sha256:071369e41c6a5d7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAffineTransform](../nsaffinetransform.md)

# transformStruct

<sub>Instance Property</sub>

The matrix coefficients stored as the transformation matrix.

<sub>Mac Catalyst, macOS</sub>

```swift
var transformStruct: NSAffineTransformStruct { get set }
```

## Discussion

The matrix is of the form shown in [Transform Mathematics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Transforms/Transforms.html#//apple_ref/doc/uid/TP40003290-CH204-BCIIICJI), and the six-element structure defined by the [NSAffineTransformStruct](../nsaffinetransformstruct.md) structure is of the form:

```objc
{m11, m12, m21, m22, tX, tY}
```

The [NSAffineTransformStruct](../nsaffinetransformstruct.md) structure is an alternate representation of a transformation matrix that can be used to specify matrix values directly.

## See Also

### Related Documentation

- [- initWithTransform:](<init(transform_).md>) — Initializes the receiver’s matrix using another transform object.

### Accessing the Transformation Matrix

- [NSAffineTransformStruct](../nsaffinetransformstruct.md) — A structure that defines the three-by-three matrix that performs an affine transform between two coordinate systems.
