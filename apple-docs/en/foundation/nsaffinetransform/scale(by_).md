---
title: 'scale(by:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsaffinetransform/scale(by:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsaffinetransform/scale(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsaffinetransform/scale%28by%3A%29.json'
content_hash: 'sha256:b4636b9620760891'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAffineTransform](../nsaffinetransform.md)

# scale(by:)

<sub>Instance Method</sub>

Applies the specified scaling factor along both x and y axes to the receiver’s transformation matrix.

<sub>Mac Catalyst, macOS</sub>

```swift
func scale(by scale: Double)
```

## Parameters

- `scale` — The scaling factor to apply to both axes. Specifying a negative value has the effect of inverting the direction of the axes in addition to scaling them. A scaling factor of 1.0 scales the content to exactly the same size.

## Discussion

After invoking this method, applying the receiver’s matrix modifies the unit lengths along the current x and y axes by a factor of `scale`, in addition to performing all previous transformations.

## See Also

### Accumulating Transformations

- [- rotateByDegrees:](<rotate(bydegrees_).md>) — Applies a rotation factor (measured in degrees) to the receiver’s transformation matrix.
- [- rotateByRadians:](<rotate(byradians_).md>) — Applies a rotation factor (measured in radians) to the receiver’s transformation matrix.
- [- scaleXBy:yBy:](<scalex(by_yby_).md>) — Applies scaling factors to each axis of the receiver’s transformation matrix.
- [- translateXBy:yBy:](<translatex(by_yby_).md>) — Applies the specified translation factors to the receiver’s transformation matrix.
- [- appendTransform:](<append(__).md>) — Appends the specified matrix to the receiver’s matrix.
- [- prependTransform:](<prepend(__).md>) — Prepends the specified matrix to the receiver’s matrix.
- [- invert](<invert().md>) — Replaces the receiver’s matrix with its inverse matrix.
