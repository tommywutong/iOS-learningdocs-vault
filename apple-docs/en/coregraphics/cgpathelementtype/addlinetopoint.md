---
title: CGPathElementType.addLineToPoint
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpathelementtype/addlinetopoint
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpathelementtype/addlinetopoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpathelementtype/addlinetopoint.json'
content_hash: 'sha256:7c7946c3eadfa665'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPathElementType](../cgpathelementtype.md)

# CGPathElementType.addLineToPoint

<sub>Case</sub>

The path element that adds a line from the current point to a new point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case addLineToPoint
```

## Discussion

The element holds a single point for the destination. See the function [CGPathAddLineToPoint](../cgpathaddlinetopoint.md).

## See Also

### Constants

- [kCGPathElementMoveToPoint](movetopoint.md) — The path element that starts a new subpath.
- [kCGPathElementAddQuadCurveToPoint](addquadcurvetopoint.md) — The path element that adds a quadratic curve from the current point to the specified point.
- [kCGPathElementAddCurveToPoint](addcurvetopoint.md) — The path element that adds a cubic curve from the current point to the specified point.
- [kCGPathElementCloseSubpath](closesubpath.md) — The path element that closes and completes a subpath. The element does not contain any points. See the function [CGPathCloseSubpath](<../cgmutablepath/closesubpath().md>).
