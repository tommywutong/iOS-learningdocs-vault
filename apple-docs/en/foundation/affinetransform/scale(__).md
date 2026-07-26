---
title: 'scale(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/affinetransform/scale(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/affinetransform/scale(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/affinetransform/scale%28_%3A%29.json'
content_hash: 'sha256:12ab979f7a9bdf6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AffineTransform](../affinetransform.md)

# scale(_:)

<sub>Instance Method</sub>

Mutates an affine transformation matrix to apply scaling in both x and y dimensions.

<sub>macOS</sub>

```swift
mutating func scale(_ scale: CGFloat)
```

## Parameters

- `scale` — The scale factor.

## See Also

### Accumulating Tranformations

- [rotate(byDegrees:)](<rotate(bydegrees_).md>) — Mutates an affine transformation matrix to apply a rotation.
- [rotate(byRadians:)](<rotate(byradians_).md>) — Mutates an affine transformation matrix to apply a rotation.
- [scale(x:y:)](<scale(x_y_).md>) — Mutates an affine transformation matrix to apply scaling in each of the x and y dimensions.
- [translate(x:y:)](<translate(x_y_).md>) — Mutates an affine transformation matrix to perform the specified translation.
- [append(_:)](<append(__).md>) — Mutates an affine transformation by appending another affine transform.
- [prepend(_:)](<prepend(__).md>) — Mutates an affine transformation by prepending another affine transform.
- [invert()](<invert().md>) — Inverts the transformation matrix, if possible.
- [inverted()](<inverted().md>) — Returns an inverted version of the matrix, if possible, or nil if not.
