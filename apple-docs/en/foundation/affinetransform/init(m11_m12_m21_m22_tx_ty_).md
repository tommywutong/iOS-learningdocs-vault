---
title: 'init(m11:m12:m21:m22:tX:tY:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/affinetransform/init(m11:m12:m21:m22:tx:ty:)'
source_url: 'https://developer.apple.com/documentation/foundation/affinetransform/init(m11:m12:m21:m22:tx:ty:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/affinetransform/init%28m11%3Am12%3Am21%3Am22%3Atx%3Aty%3A%29.json'
content_hash: 'sha256:9485c3a6fb881498'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AffineTransform](../affinetransform.md)

# init(m11:m12:m21:m22:tX:tY:)

<sub>Initializer</sub>

Creates an affine transformation.

<sub>macOS</sub>

```swift
init(m11: CGFloat, m12: CGFloat, m21: CGFloat, m22: CGFloat, tX: CGFloat, tY: CGFloat)
```

## Discussion

Create an affine tranform by directly specifying the key values of the transform matrix.

```swift
[ m11 m12  0 ]
[ m21 m22  0 ]
[  tX  tY  1 ]
```

## See Also

### Creating Transforms

- [init()](<init().md>) — Creates an affine transformation matrix with identity values.
- [init(rotationByDegrees:)](<init(rotationbydegrees_).md>) — Creates an affine transformation matrix from a rotation angle.
- [init(rotationByRadians:)](<init(rotationbyradians_).md>) — Creates an affine transformation matrix from a rotation angle.
- [init(scale:)](<init(scale_).md>) — Creates an affine transformation matrix from scaling a single value.
- [init(scaleByX:byY:)](<init(scalebyx_byy_).md>) — Creates an affine transformation matrix from scaling values.
- [init(translationByX:byY:)](<init(translationbyx_byy_).md>) — Creates an affine transformation matrix from translation values.
