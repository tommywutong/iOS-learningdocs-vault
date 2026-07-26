---
title: invert()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/affinetransform/invert()
source_url: 'https://developer.apple.com/documentation/foundation/affinetransform/invert()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/affinetransform/invert%28%29.json'
content_hash: 'sha256:bc874b9bc50c85af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AffineTransform](../affinetransform.md)

# invert()

<sub>Instance Method</sub>

Inverts the transformation matrix, if possible.

<sub>macOS</sub>

```swift
mutating func invert()
```

## Discussion

Matrices with a determinant less than the smallest valid representation of a double value and greater than zero are invalid for representing as an inverse. If this can potentially happen to the input transform, use the [inverted()](<inverted().md>) method instead. The [inverted()](<inverted().md>) method returns `nil` if the function can’t reliably invert the matrix.

You can calculate the determinant using the following formula:

```swift
D = (m11 * m22) - (m12 * m21)
```

## See Also

### Accumulating Tranformations

- [rotate(byDegrees:)](<rotate(bydegrees_).md>) — Mutates an affine transformation matrix to apply a rotation.
- [rotate(byRadians:)](<rotate(byradians_).md>) — Mutates an affine transformation matrix to apply a rotation.
- [scale(_:)](<scale(__).md>) — Mutates an affine transformation matrix to apply scaling in both x and y dimensions.
- [scale(x:y:)](<scale(x_y_).md>) — Mutates an affine transformation matrix to apply scaling in each of the x and y dimensions.
- [translate(x:y:)](<translate(x_y_).md>) — Mutates an affine transformation matrix to perform the specified translation.
- [append(_:)](<append(__).md>) — Mutates an affine transformation by appending another affine transform.
- [prepend(_:)](<prepend(__).md>) — Mutates an affine transformation by prepending another affine transform.
- [inverted()](<inverted().md>) — Returns an inverted version of the matrix, if possible, or nil if not.
