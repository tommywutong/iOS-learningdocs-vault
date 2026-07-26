---
title: CGPathElementType.moveToPoint
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpathelementtype/movetopoint
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpathelementtype/movetopoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpathelementtype/movetopoint.json'
content_hash: 'sha256:f42c467e72620ab0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPathElementType](../cgpathelementtype.md)

# CGPathElementType.moveToPoint

<sub>Case</sub>

The path element that starts a new subpath.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case moveToPoint
```

## Discussion

The element holds a single point for the destination. See the function [CGPathMoveToPoint](../cgpathmovetopoint.md).

## See Also

### Constants

- [kCGPathElementAddLineToPoint](addlinetopoint.md) — The path element that adds a line from the current point to a new point.
- [kCGPathElementAddQuadCurveToPoint](addquadcurvetopoint.md) — The path element that adds a quadratic curve from the current point to the specified point.
- [kCGPathElementAddCurveToPoint](addcurvetopoint.md) — The path element that adds a cubic curve from the current point to the specified point.
- [kCGPathElementCloseSubpath](closesubpath.md) — The path element that closes and completes a subpath. The element does not contain any points. See the function [CGPathCloseSubpath](<../cgmutablepath/closesubpath().md>).
