---
title: currentPoint
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibezierpath/currentpoint
source_url: 'https://developer.apple.com/documentation/uikit/uibezierpath/currentpoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibezierpath/currentpoint.json'
content_hash: 'sha256:19ee0d79ca89f510'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBezierPath](../uibezierpath.md)

# currentPoint

<sub>Instance Property</sub>

The current point in the graphics path.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var currentPoint: CGPoint { get }
```

## Discussion

The value in this property represents the starting point for new line and curve segments. If the path is currently empty, this property contains the value [CGPointZero](../../coregraphics/cgpointzero.md).

## See Also

### Related Documentation

- [empty](isempty.md) — A Boolean value that indicates whether the path has any valid elements.

### Constructing a path

- [- moveToPoint:](<move(to_).md>) — Moves the path’s current point to the specified location.
- [- addLineToPoint:](<addline(to_).md>) — Appends a straight line to the path.
- [- addArcWithCenter:radius:startAngle:endAngle:clockwise:](<addarc(withcenter_radius_startangle_endangle_clockwise_).md>) — Appends an arc to the path.
- [- addCurveToPoint:controlPoint1:controlPoint2:](<addcurve(to_controlpoint1_controlpoint2_).md>) — Appends a cubic Bézier curve to the path.
- [- addQuadCurveToPoint:controlPoint:](<addquadcurve(to_controlpoint_).md>) — Appends a quadratic Bézier curve to the path.
- [- closePath](<close().md>) — Closes the most recent subpath.
- [- removeAllPoints](<removeallpoints().md>) — Removes all points from the path, effectively deleting all subpaths.
- [- appendPath:](<append(__).md>) — Appends the contents of the specified path object to the path.
- [CGPath](cgpath.md) — The Core Graphics representation of the path.
