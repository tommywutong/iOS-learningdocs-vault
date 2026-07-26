---
title: 'append(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsaffinetransform/append(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsaffinetransform/append(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsaffinetransform/append%28_%3A%29.json'
content_hash: 'sha256:c702d23b106c803b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAffineTransform](../nsaffinetransform.md)

# append(_:)

<sub>Instance Method</sub>

Appends the specified matrix to the receiver’s matrix.

<sub>Mac Catalyst</sub>

```swift
func append(_ transform: NSAffineTransform)
```

<sub>macOS</sub>

```swift
func append(_ transform: AffineTransform)
```

## Parameters

- `transform` — The matrix to append to the receiver.

## Discussion

This method multiplies the receiver’s matrix by the matrix in `aTransform` and replaces the receiver’s matrix with the results. This type of operation is the same as applying the transformations in the receiver followed by the transformations in `aTransform`.

## See Also

### Accumulating Transformations

- [- rotateByDegrees:](<rotate(bydegrees_).md>) — Applies a rotation factor (measured in degrees) to the receiver’s transformation matrix.
- [- rotateByRadians:](<rotate(byradians_).md>) — Applies a rotation factor (measured in radians) to the receiver’s transformation matrix.
- [- scaleBy:](<scale(by_).md>) — Applies the specified scaling factor along both x and y axes to the receiver’s transformation matrix.
- [- scaleXBy:yBy:](<scalex(by_yby_).md>) — Applies scaling factors to each axis of the receiver’s transformation matrix.
- [- translateXBy:yBy:](<translatex(by_yby_).md>) — Applies the specified translation factors to the receiver’s transformation matrix.
- [- prependTransform:](<prepend(__).md>) — Prepends the specified matrix to the receiver’s matrix.
- [- invert](<invert().md>) — Replaces the receiver’s matrix with its inverse matrix.
