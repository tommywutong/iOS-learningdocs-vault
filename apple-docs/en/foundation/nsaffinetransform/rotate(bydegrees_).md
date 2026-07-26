---
title: 'rotate(byDegrees:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsaffinetransform/rotate(bydegrees:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsaffinetransform/rotate(bydegrees:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsaffinetransform/rotate%28bydegrees%3A%29.json'
content_hash: 'sha256:d6baf3afd86cf108'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAffineTransform](../nsaffinetransform.md)

# rotate(byDegrees:)

<sub>Instance Method</sub>

Applies a rotation factor (measured in degrees) to the receiver’s transformation matrix.

<sub>Mac Catalyst, macOS</sub>

```swift
func rotate(byDegrees angle: Double)
```

## Parameters

- `angle` — The rotation angle, measured in degrees.

## Discussion

After invoking this method, applying the receiver’s matrix turns the axes counterclockwise about the current origin by `angle` degrees, in addition to performing all previous transformations.

## See Also

### Accumulating Transformations

- [- rotateByRadians:](<rotate(byradians_).md>) — Applies a rotation factor (measured in radians) to the receiver’s transformation matrix.
- [- scaleBy:](<scale(by_).md>) — Applies the specified scaling factor along both x and y axes to the receiver’s transformation matrix.
- [- scaleXBy:yBy:](<scalex(by_yby_).md>) — Applies scaling factors to each axis of the receiver’s transformation matrix.
- [- translateXBy:yBy:](<translatex(by_yby_).md>) — Applies the specified translation factors to the receiver’s transformation matrix.
- [- appendTransform:](<append(__).md>) — Appends the specified matrix to the receiver’s matrix.
- [- prependTransform:](<prepend(__).md>) — Prepends the specified matrix to the receiver’s matrix.
- [- invert](<invert().md>) — Replaces the receiver’s matrix with its inverse matrix.
