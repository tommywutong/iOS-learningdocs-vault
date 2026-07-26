---
title: 'move(to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibezierpath/move(to:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibezierpath/move(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibezierpath/move%28to%3A%29.json'
content_hash: 'sha256:19a3b893103b4d4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBezierPath](../uibezierpath.md)

# move(to:)

<sub>Instance Method</sub>

Moves the path’s current point to the specified location.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func move(to point: CGPoint)
```

## Parameters

- `point` — A point in the current coordinate system.

## Discussion

This method implicitly ends the current subpath (if any) and sets the current point to the value in the `point` parameter. When ending the previous subpath, this method does not actually close the subpath. Therefore, the first and last points of the previous subpath are not connected to each other.

For many path operations, you must call this method before issuing any commands that cause a line or curve segment to be drawn.

## See Also

### Constructing a path

- [- addLineToPoint:](<addline(to_).md>) — Appends a straight line to the path.
- [- addArcWithCenter:radius:startAngle:endAngle:clockwise:](<addarc(withcenter_radius_startangle_endangle_clockwise_).md>) — Appends an arc to the path.
- [- addCurveToPoint:controlPoint1:controlPoint2:](<addcurve(to_controlpoint1_controlpoint2_).md>) — Appends a cubic Bézier curve to the path.
- [- addQuadCurveToPoint:controlPoint:](<addquadcurve(to_controlpoint_).md>) — Appends a quadratic Bézier curve to the path.
- [- closePath](<close().md>) — Closes the most recent subpath.
- [- removeAllPoints](<removeallpoints().md>) — Removes all points from the path, effectively deleting all subpaths.
- [- appendPath:](<append(__).md>) — Appends the contents of the specified path object to the path.
- [CGPath](cgpath.md) — The Core Graphics representation of the path.
- [currentPoint](currentpoint.md) — The current point in the graphics path.
