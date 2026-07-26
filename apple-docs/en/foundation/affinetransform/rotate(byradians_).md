---
title: 'rotate(byRadians:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/affinetransform/rotate(byradians:)'
source_url: 'https://developer.apple.com/documentation/foundation/affinetransform/rotate(byradians:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/affinetransform/rotate%28byradians%3A%29.json'
content_hash: 'sha256:72d81c3af5bd6ca8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AffineTransform](../affinetransform.md)

# rotate(byRadians:)

<sub>Instance Method</sub>

Mutates an affine transformation matrix to apply a rotation.

<sub>macOS</sub>

```swift
mutating func rotate(byRadians angle: CGFloat)
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

### Accumulating Tranformations

- [rotate(byDegrees:)](<rotate(bydegrees_).md>) — Mutates an affine transformation matrix to apply a rotation.
- [scale(_:)](<scale(__).md>) — Mutates an affine transformation matrix to apply scaling in both x and y dimensions.
- [scale(x:y:)](<scale(x_y_).md>) — Mutates an affine transformation matrix to apply scaling in each of the x and y dimensions.
- [translate(x:y:)](<translate(x_y_).md>) — Mutates an affine transformation matrix to perform the specified translation.
- [append(_:)](<append(__).md>) — Mutates an affine transformation by appending another affine transform.
- [prepend(_:)](<prepend(__).md>) — Mutates an affine transformation by prepending another affine transform.
- [invert()](<invert().md>) — Inverts the transformation matrix, if possible.
- [inverted()](<inverted().md>) — Returns an inverted version of the matrix, if possible, or nil if not.
