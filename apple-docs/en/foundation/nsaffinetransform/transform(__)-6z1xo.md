---
title: 'transform(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsaffinetransform/transform(_:)-6z1xo'
source_url: 'https://developer.apple.com/documentation/foundation/nsaffinetransform/transform(_:)-6z1xo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsaffinetransform/transform%28_%3A%29-6z1xo.json'
content_hash: 'sha256:04059176b39fd5c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAffineTransform](../nsaffinetransform.md)

# transform(_:)

<sub>Instance Method</sub>

Creates and returns a new Bézier path object with each point in the given path transformed by the receiver.

<sub>macOS</sub>

```swift
func transform(_ path: NSBezierPath) -> NSBezierPath
```

## Parameters

- `path` — An object representing the bezier path to be used in the transformation.

## Discussion

The original `NSBezierPath` object is not modified.

## See Also

### Transforming Data and Objects

- [- transformPoint:](<transform(__)-41p16.md>) — Applies the receiver’s transform to the specified point and returns the result.
- [- transformSize:](<transform(__)-5r6ol.md>) — Applies the receiver’s transform to the specified size and returns the results.
