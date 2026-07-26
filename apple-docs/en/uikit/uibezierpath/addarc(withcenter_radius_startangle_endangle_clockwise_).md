---
title: 'addArc(withCenter:radius:startAngle:endAngle:clockwise:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibezierpath/addarc(withcenter:radius:startangle:endangle:clockwise:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibezierpath/addarc(withcenter:radius:startangle:endangle:clockwise:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibezierpath/addarc%28withcenter%3Aradius%3Astartangle%3Aendangle%3Aclockwise%3A%29.json'
content_hash: 'sha256:d9861a1af4a6ed5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBezierPath](../uibezierpath.md)

# addArc(withCenter:radius:startAngle:endAngle:clockwise:)

<sub>Instance Method</sub>

Appends an arc to the path.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func addArc(withCenter center: CGPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool)
```

## Parameters

- `center` — Specifies the center point of the circle (in the current coordinate system) used to define the arc.

- `radius` — Specifies the radius of the circle used to define the arc.

- `startAngle` — Specifies the starting angle of the arc (measured in radians).

- `endAngle` — Specifies the end angle of the arc (measured in radians).

- `clockwise` — The direction in which to draw the arc.

## Discussion

This method adds the specified arc beginning at the current point. The created arc lies on the perimeter of the specified circle. When drawn in the default coordinate system, the start and end angles are based on the unit circle shown in the image in [+ bezierPathWithArcCenter:radius:startAngle:endAngle:clockwise:](<init(arccenter_radius_startangle_endangle_clockwise_).md>). For example, specifying a start angle of `0` radians, an end angle of `π` radians, and setting the `clockwise` parameter to [true](../../swift/true.md) draws the bottom half of the circle. However, specifying the same start and end angles but setting the `clockwise` parameter set to [false](../../swift/false.md) draws the top half of the circle.

After calling this method, the current point is set to the point on the arc at the end angle of the circle.

## See Also

### Constructing a path

- [- moveToPoint:](<move(to_).md>) — Moves the path’s current point to the specified location.
- [- addLineToPoint:](<addline(to_).md>) — Appends a straight line to the path.
- [- addCurveToPoint:controlPoint1:controlPoint2:](<addcurve(to_controlpoint1_controlpoint2_).md>) — Appends a cubic Bézier curve to the path.
- [- addQuadCurveToPoint:controlPoint:](<addquadcurve(to_controlpoint_).md>) — Appends a quadratic Bézier curve to the path.
- [- closePath](<close().md>) — Closes the most recent subpath.
- [- removeAllPoints](<removeallpoints().md>) — Removes all points from the path, effectively deleting all subpaths.
- [- appendPath:](<append(__).md>) — Appends the contents of the specified path object to the path.
- [CGPath](cgpath.md) — The Core Graphics representation of the path.
- [currentPoint](currentpoint.md) — The current point in the graphics path.
