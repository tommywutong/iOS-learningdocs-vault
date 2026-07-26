---
title: CGRectNull
framework: Core Graphics
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgrectnull
source_url: 'https://developer.apple.com/documentation/coregraphics/cgrectnull'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgrectnull.json'
content_hash: 'sha256:bb9ca1d403a613c6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGRectNull

<sub>Global Variable</sub>

The null rectangle, representing an invalid value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let CGRectNull: CGRect
```

## Discussion

This is the rectangle returned when, for example, you intersect two disjoint rectangles. Note that the null rectangle is not the same as the [CGRectZero](cgrectzero.md) rectangle. For example, the union of a rectangle with the null rectangle is the original rectangle (that is, the null rectangle contributes nothing).

## See Also

### Constants

- [CGRectInfinite](cgrectinfinite.md) — A rectangle that has infinite extent.
- [Geometric Zeros](geometric-zeros.md) — A zero point, zero rectangle, or zero size.
- [CGRectEdge](../corefoundation/cgrectedge.md)
- [CGFloat Informational Macros](cgfloat-informational-macros.md) — Informational macros for the `CGFloat` type.
