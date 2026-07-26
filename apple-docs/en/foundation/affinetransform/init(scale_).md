---
title: 'init(scale:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/affinetransform/init(scale:)'
source_url: 'https://developer.apple.com/documentation/foundation/affinetransform/init(scale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/affinetransform/init%28scale%3A%29.json'
content_hash: 'sha256:84538877c44fbdea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AffineTransform](../affinetransform.md)

# init(scale:)

<sub>Initializer</sub>

Creates an affine transformation matrix from scaling a single value.

<sub>macOS</sub>

```swift
init(scale factor: CGFloat)
```

## Parameters

- `factor` — The scale factor.

## Discussion

The matrix takes the following form:

```swift
[ f  0  0 ]
[ 0  f  0 ]
[ 0  0  1 ]
```

## See Also

### Creating Transforms

- [init()](<init().md>) — Creates an affine transformation matrix with identity values.
- [init(rotationByDegrees:)](<init(rotationbydegrees_).md>) — Creates an affine transformation matrix from a rotation angle.
- [init(rotationByRadians:)](<init(rotationbyradians_).md>) — Creates an affine transformation matrix from a rotation angle.
- [init(scaleByX:byY:)](<init(scalebyx_byy_).md>) — Creates an affine transformation matrix from scaling values.
- [init(translationByX:byY:)](<init(translationbyx_byy_).md>) — Creates an affine transformation matrix from translation values.
- [init(m11:m12:m21:m22:tX:tY:)](<init(m11_m12_m21_m22_tx_ty_).md>) — Creates an affine transformation.
