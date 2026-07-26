---
title: 'translateX(by:yBy:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsaffinetransform/translatex(by:yby:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsaffinetransform/translatex(by:yby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsaffinetransform/translatex%28by%3Ayby%3A%29.json'
content_hash: 'sha256:1a14044985293626'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAffineTransform](../nsaffinetransform.md)

# translateX(by:yBy:)

<sub>Instance Method</sub>

Applies the specified translation factors to the receiver’s transformation matrix.

<sub>Mac Catalyst, macOS</sub>

```swift
func translateX(by deltaX: Double, yBy deltaY: Double)
```

## Parameters

- `deltaX` — The number of units to move along the x axis.

- `deltaY` — The number of units to move along the y axis.

## Discussion

Subsequent transformations cause coordinates to be shifted by `deltaX` units along the x axis and by `deltaY` units along the y axis. Translation factors do not affect `NSSize` values, which specify a differential between points.

## See Also

### Accumulating Transformations

- [- rotateByDegrees:](<rotate(bydegrees_).md>) — Applies a rotation factor (measured in degrees) to the receiver’s transformation matrix.
- [- rotateByRadians:](<rotate(byradians_).md>) — Applies a rotation factor (measured in radians) to the receiver’s transformation matrix.
- [- scaleBy:](<scale(by_).md>) — Applies the specified scaling factor along both x and y axes to the receiver’s transformation matrix.
- [- scaleXBy:yBy:](<scalex(by_yby_).md>) — Applies scaling factors to each axis of the receiver’s transformation matrix.
- [- appendTransform:](<append(__).md>) — Appends the specified matrix to the receiver’s matrix.
- [- prependTransform:](<prepend(__).md>) — Prepends the specified matrix to the receiver’s matrix.
- [- invert](<invert().md>) — Replaces the receiver’s matrix with its inverse matrix.
