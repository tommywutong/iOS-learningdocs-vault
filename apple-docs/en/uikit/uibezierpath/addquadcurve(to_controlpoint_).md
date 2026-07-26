---
title: 'addQuadCurve(to:controlPoint:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibezierpath/addquadcurve(to:controlpoint:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibezierpath/addquadcurve(to:controlpoint:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibezierpath/addquadcurve%28to%3Acontrolpoint%3A%29.json'
content_hash: 'sha256:38c9831e6e93234b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBezierPath](../uibezierpath.md)

# addQuadCurve(to:controlPoint:)

<sub>Instance Method</sub>

Appends a quadratic Bézier curve to the path.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func addQuadCurve(to endPoint: CGPoint, controlPoint: CGPoint)
```

## Parameters

- `endPoint` — The end point of the curve.

- `controlPoint` — The control point of the curve.

## Discussion

This method appends a quadratic Bézier curve from the current point to the end point specified by the `endPoint` parameter. The relationships between the current point, control point, and end point are what defines the actual curve. The following image shows some examples of quadratic curves and the approximate curve shape based on some sample points. The exact curvature of the segment involves a complex mathematical relationship between the points and is well documented online.

![](../../../../attachments/a44987bfb6a4516273a636cbbca7e5d8/media-1965858.jpg)

You must set the path’s current point (using the [- moveToPoint:](<move(to_).md>) method or through the previous creation of a line or curve segment) before you call this method. If the path is empty, this method does nothing. After adding the curve segment, this method updates the current point to the value in `point`.

## See Also

### Constructing a path

- [- moveToPoint:](<move(to_).md>) — Moves the path’s current point to the specified location.
- [- addLineToPoint:](<addline(to_).md>) — Appends a straight line to the path.
- [- addArcWithCenter:radius:startAngle:endAngle:clockwise:](<addarc(withcenter_radius_startangle_endangle_clockwise_).md>) — Appends an arc to the path.
- [- addCurveToPoint:controlPoint1:controlPoint2:](<addcurve(to_controlpoint1_controlpoint2_).md>) — Appends a cubic Bézier curve to the path.
- [- closePath](<close().md>) — Closes the most recent subpath.
- [- removeAllPoints](<removeallpoints().md>) — Removes all points from the path, effectively deleting all subpaths.
- [- appendPath:](<append(__).md>) — Appends the contents of the specified path object to the path.
- [CGPath](cgpath.md) — The Core Graphics representation of the path.
- [currentPoint](currentpoint.md) — The current point in the graphics path.
