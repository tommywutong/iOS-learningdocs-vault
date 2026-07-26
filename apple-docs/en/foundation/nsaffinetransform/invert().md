---
title: invert()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsaffinetransform/invert()
source_url: 'https://developer.apple.com/documentation/foundation/nsaffinetransform/invert()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsaffinetransform/invert%28%29.json'
content_hash: 'sha256:a047c9c91c13cc80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAffineTransform](../nsaffinetransform.md)

# invert()

<sub>Instance Method</sub>

Replaces the receiver’s matrix with its inverse matrix.

<sub>Mac Catalyst, macOS</sub>

```swift
func invert()
```

## Discussion

Inverse matrices are useful for undoing the effects of a matrix. If a previous point (x,y) was transformed to (x’,y’), inverting the matrix and applying it to point (x’,y’) yields the point (x,y).

You can also use inverse matrices in conjunction with the [- concat](<concat().md>) method to remove the effects of concatenating the matrix to the current transformation matrix of the current graphic context.

## See Also

### Accumulating Transformations

- [- rotateByDegrees:](<rotate(bydegrees_).md>) — Applies a rotation factor (measured in degrees) to the receiver’s transformation matrix.
- [- rotateByRadians:](<rotate(byradians_).md>) — Applies a rotation factor (measured in radians) to the receiver’s transformation matrix.
- [- scaleBy:](<scale(by_).md>) — Applies the specified scaling factor along both x and y axes to the receiver’s transformation matrix.
- [- scaleXBy:yBy:](<scalex(by_yby_).md>) — Applies scaling factors to each axis of the receiver’s transformation matrix.
- [- translateXBy:yBy:](<translatex(by_yby_).md>) — Applies the specified translation factors to the receiver’s transformation matrix.
- [- appendTransform:](<append(__).md>) — Appends the specified matrix to the receiver’s matrix.
- [- prependTransform:](<prepend(__).md>) — Prepends the specified matrix to the receiver’s matrix.
