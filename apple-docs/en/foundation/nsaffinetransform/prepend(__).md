---
title: 'prepend(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsaffinetransform/prepend(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsaffinetransform/prepend(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsaffinetransform/prepend%28_%3A%29.json'
content_hash: 'sha256:d401a223d07a3ac5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAffineTransform](../nsaffinetransform.md)

# prepend(_:)

<sub>Instance Method</sub>

Prepends the specified matrix to the receiver’s matrix.

<sub>Mac Catalyst</sub>

```swift
func prepend(_ transform: NSAffineTransform)
```

<sub>macOS</sub>

```swift
func prepend(_ transform: AffineTransform)
```

## Parameters

- `transform` — The matrix to prepend to the receiver.

## Discussion

This method multiplies the matrix in `transform` by the receiver’s matrix and replaces the receiver’s matrix with the result. This type of operation is the same as applying the transformations in `transform` followed by the transformations in the receiver.

## See Also

### Accumulating Transformations

- [- rotateByDegrees:](<rotate(bydegrees_).md>) — Applies a rotation factor (measured in degrees) to the receiver’s transformation matrix.
- [- rotateByRadians:](<rotate(byradians_).md>) — Applies a rotation factor (measured in radians) to the receiver’s transformation matrix.
- [- scaleBy:](<scale(by_).md>) — Applies the specified scaling factor along both x and y axes to the receiver’s transformation matrix.
- [- scaleXBy:yBy:](<scalex(by_yby_).md>) — Applies scaling factors to each axis of the receiver’s transformation matrix.
- [- translateXBy:yBy:](<translatex(by_yby_).md>) — Applies the specified translation factors to the receiver’s transformation matrix.
- [- appendTransform:](<append(__).md>) — Appends the specified matrix to the receiver’s matrix.
- [- invert](<invert().md>) — Replaces the receiver’s matrix with its inverse matrix.
