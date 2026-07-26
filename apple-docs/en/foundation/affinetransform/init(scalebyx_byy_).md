---
title: 'init(scaleByX:byY:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/affinetransform/init(scalebyx:byy:)'
source_url: 'https://developer.apple.com/documentation/foundation/affinetransform/init(scalebyx:byy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/affinetransform/init%28scalebyx%3Abyy%3A%29.json'
content_hash: 'sha256:fbd9dcba4af3d189'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AffineTransform](../affinetransform.md)

# init(scaleByX:byY:)

<sub>Initializer</sub>

Creates an affine transformation matrix from scaling values.

<sub>macOS</sub>

```swift
init(scaleByX x: CGFloat, byY y: CGFloat)
```

## Parameters

- `x` — The horizontal scale factor.

- `y` — The vertical scale factor.

## Discussion

The matrix takes the following form:

```swift
[ x  0  0 ]
[ 0  y  0 ]
[ 0  0  1 ]
```

## See Also

### Creating Transforms

- [init()](<init().md>) — Creates an affine transformation matrix with identity values.
- [init(rotationByDegrees:)](<init(rotationbydegrees_).md>) — Creates an affine transformation matrix from a rotation angle.
- [init(rotationByRadians:)](<init(rotationbyradians_).md>) — Creates an affine transformation matrix from a rotation angle.
- [init(scale:)](<init(scale_).md>) — Creates an affine transformation matrix from scaling a single value.
- [init(translationByX:byY:)](<init(translationbyx_byy_).md>) — Creates an affine transformation matrix from translation values.
- [init(m11:m12:m21:m22:tX:tY:)](<init(m11_m12_m21_m22_tx_ty_).md>) — Creates an affine transformation.
