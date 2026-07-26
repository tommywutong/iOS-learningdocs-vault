---
title: 'addLine(to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibezierpath/addline(to:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibezierpath/addline(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibezierpath/addline%28to%3A%29.json'
content_hash: 'sha256:85425155c2e108c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBezierPath](../uibezierpath.md)

# addLine(to:)

<sub>Instance Method</sub>

Appends a straight line to the path.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func addLine(to point: CGPoint)
```

## Parameters

- `point` — The destination point of the line segment, specified in the current coordinate system.

## Discussion

This method creates a straight line segment starting at the current point and ending at the point specified by the `point` parameter. After adding the line segment, this method updates the current point to the value in `point`.

You must set the path’s current point (using the [- moveToPoint:](<move(to_).md>) method or through the previous creation of a line or curve segment) before you call this method. If the path is empty, this method does nothing.

## See Also

### Constructing a path

- [- moveToPoint:](<move(to_).md>) — Moves the path’s current point to the specified location.
- [- addArcWithCenter:radius:startAngle:endAngle:clockwise:](<addarc(withcenter_radius_startangle_endangle_clockwise_).md>) — Appends an arc to the path.
- [- addCurveToPoint:controlPoint1:controlPoint2:](<addcurve(to_controlpoint1_controlpoint2_).md>) — Appends a cubic Bézier curve to the path.
- [- addQuadCurveToPoint:controlPoint:](<addquadcurve(to_controlpoint_).md>) — Appends a quadratic Bézier curve to the path.
- [- closePath](<close().md>) — Closes the most recent subpath.
- [- removeAllPoints](<removeallpoints().md>) — Removes all points from the path, effectively deleting all subpaths.
- [- appendPath:](<append(__).md>) — Appends the contents of the specified path object to the path.
- [CGPath](cgpath.md) — The Core Graphics representation of the path.
- [currentPoint](currentpoint.md) — The current point in the graphics path.
