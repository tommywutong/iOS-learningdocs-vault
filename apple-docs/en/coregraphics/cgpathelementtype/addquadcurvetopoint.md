---
title: CGPathElementType.addQuadCurveToPoint
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpathelementtype/addquadcurvetopoint
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpathelementtype/addquadcurvetopoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpathelementtype/addquadcurvetopoint.json'
content_hash: 'sha256:5f7bea1d043b2c53'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPathElementType](../cgpathelementtype.md)

# CGPathElementType.addQuadCurveToPoint

<sub>Case</sub>

The path element that adds a quadratic curve from the current point to the specified point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case addQuadCurveToPoint
```

## Discussion

The element holds a control point and a destination point. See the function [CGPathAddQuadCurveToPoint](../cgpathaddquadcurvetopoint.md).

## See Also

### Constants

- [kCGPathElementMoveToPoint](movetopoint.md) — The path element that starts a new subpath.
- [kCGPathElementAddLineToPoint](addlinetopoint.md) — The path element that adds a line from the current point to a new point.
- [kCGPathElementAddCurveToPoint](addcurvetopoint.md) — The path element that adds a cubic curve from the current point to the specified point.
- [kCGPathElementCloseSubpath](closesubpath.md) — The path element that closes and completes a subpath. The element does not contain any points. See the function [CGPathCloseSubpath](<../cgmutablepath/closesubpath().md>).
