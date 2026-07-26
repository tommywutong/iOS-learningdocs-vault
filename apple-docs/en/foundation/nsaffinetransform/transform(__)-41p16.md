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
doc_path: '/documentation/foundation/nsaffinetransform/transform(_:)-41p16'
source_url: 'https://developer.apple.com/documentation/foundation/nsaffinetransform/transform(_:)-41p16'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsaffinetransform/transform%28_%3A%29-41p16.json'
content_hash: 'sha256:9136c21120d1e9b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAffineTransform](../nsaffinetransform.md)

# transform(_:)

<sub>Instance Method</sub>

Applies the receiver’s transform to the specified point and returns the result.

<sub>Mac Catalyst, macOS</sub>

```swift
func transform(_ aPoint: NSPoint) -> NSPoint
```

## Parameters

- `aPoint` — The point in the current coordinate system to which you want to apply the matrix.

## Return Value

The resulting point after applying the receiver’s transformations.

## See Also

### Transforming Data and Objects

- [- transformSize:](<transform(__)-5r6ol.md>) — Applies the receiver’s transform to the specified size and returns the results.
- [- transformBezierPath:](<transform(__)-6z1xo.md>) — Creates and returns a new Bézier path object with each point in the given path transformed by the receiver.
