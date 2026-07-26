---
title: 'init(rotationByRadians:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/affinetransform/init(rotationbyradians:)'
source_url: 'https://developer.apple.com/documentation/foundation/affinetransform/init(rotationbyradians:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/affinetransform/init%28rotationbyradians%3A%29.json'
content_hash: 'sha256:f6f5b2912020f33f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AffineTransform](../affinetransform.md)

# init(rotationByRadians:)

<sub>Initializer</sub>

Creates an affine transformation matrix from a rotation angle.

<sub>macOS</sub>

```swift
init(rotationByRadians angle: CGFloat)
```

## Parameters

- `angle` — The rotation angle in radians.

## Discussion

The matrix takes the following form:

```swift
[  cos α   sin α  0 ]
[ -sin α   cos α  0 ]
[    0       0    1 ]
```

## See Also

### Creating Transforms

- [init()](<init().md>) — Creates an affine transformation matrix with identity values.
- [init(rotationByDegrees:)](<init(rotationbydegrees_).md>) — Creates an affine transformation matrix from a rotation angle.
- [init(scale:)](<init(scale_).md>) — Creates an affine transformation matrix from scaling a single value.
- [init(scaleByX:byY:)](<init(scalebyx_byy_).md>) — Creates an affine transformation matrix from scaling values.
- [init(translationByX:byY:)](<init(translationbyx_byy_).md>) — Creates an affine transformation matrix from translation values.
- [init(m11:m12:m21:m22:tX:tY:)](<init(m11_m12_m21_m22_tx_ty_).md>) — Creates an affine transformation.
