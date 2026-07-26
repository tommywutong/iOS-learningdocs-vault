---
title: 'scaleX(by:yBy:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsaffinetransform/scalex(by:yby:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsaffinetransform/scalex(by:yby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsaffinetransform/scalex%28by%3Ayby%3A%29.json'
content_hash: 'sha256:ce09f6cafcf91609'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAffineTransform](../nsaffinetransform.md)

# scaleX(by:yBy:)

<sub>Instance Method</sub>

Applies scaling factors to each axis of the receiver’s transformation matrix.

<sub>Mac Catalyst, macOS</sub>

```swift
func scaleX(by scaleX: Double, yBy scaleY: Double)
```

## Parameters

- `scaleX` — The scaling factor to apply to the x axis.

- `scaleY` — The scaling factor to apply to the y axis.

## Discussion

After invoking this method, applying the receiver’s matrix modifies the unit length on the x axis by a factor of `scaleX` and the y axis by a factor of `scaleY`, in addition to performing all previous transformations. A value of 1.0 for either axis scales the content on that axis to the same size.

## See Also

### Accumulating Transformations

- [- rotateByDegrees:](<rotate(bydegrees_).md>) — Applies a rotation factor (measured in degrees) to the receiver’s transformation matrix.
- [- rotateByRadians:](<rotate(byradians_).md>) — Applies a rotation factor (measured in radians) to the receiver’s transformation matrix.
- [- scaleBy:](<scale(by_).md>) — Applies the specified scaling factor along both x and y axes to the receiver’s transformation matrix.
- [- translateXBy:yBy:](<translatex(by_yby_).md>) — Applies the specified translation factors to the receiver’s transformation matrix.
- [- appendTransform:](<append(__).md>) — Appends the specified matrix to the receiver’s matrix.
- [- prependTransform:](<prepend(__).md>) — Prepends the specified matrix to the receiver’s matrix.
- [- invert](<invert().md>) — Replaces the receiver’s matrix with its inverse matrix.
