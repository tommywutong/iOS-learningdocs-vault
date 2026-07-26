---
title: 'transform(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsaffinetransform/transform(_:)-5r6ol'
source_url: 'https://developer.apple.com/documentation/foundation/nsaffinetransform/transform(_:)-5r6ol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsaffinetransform/transform%28_%3A%29-5r6ol.json'
content_hash: 'sha256:451b17c72ff65970'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAffineTransform](../nsaffinetransform.md)

# transform(_:)

<sub>Instance Method</sub>

Applies the receiver’s transform to the specified size and returns the results.

<sub>Mac Catalyst, macOS</sub>

```swift
func transform(_ aSize: NSSize) -> NSSize
```

## Parameters

- `aSize` — The size data to which you want to apply the matrix.

## Return Value

The resulting size after applying the receiver’s transformations.

## Discussion

This method applies the current rotation and scaling factors to `aSize`; it does not apply translation factors. You can think of this method as transforming a vector whose origin is (0, 0) and whose end point is specified by the value in `aSize`. After the rotation and scaling factors are applied, this method effectively returns the end point of the new vector.

This method is useful for transforming delta or distance values when you need to take scaling and rotation factors into account.

## See Also

### Transforming Data and Objects

- [- transformPoint:](<transform(__)-41p16.md>) — Applies the receiver’s transform to the specified point and returns the result.
- [- transformBezierPath:](<transform(__)-6z1xo.md>) — Creates and returns a new Bézier path object with each point in the given path transformed by the receiver.
