---
title: close()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibezierpath/close()
source_url: 'https://developer.apple.com/documentation/uikit/uibezierpath/close()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibezierpath/close%28%29.json'
content_hash: 'sha256:63e121752a078585'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBezierPath](../uibezierpath.md)

# close()

<sub>Instance Method</sub>

Closes the most recent subpath.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func close()
```

## Discussion

This method closes the current subpath by creating a line segment between the first and last points in the subpath. This method subsequently updates the current point to the end of the newly created line segment, which is also the first point in the now closed subpath.

## See Also

### Constructing a path

- [- moveToPoint:](<move(to_).md>) — Moves the path’s current point to the specified location.
- [- addLineToPoint:](<addline(to_).md>) — Appends a straight line to the path.
- [- addArcWithCenter:radius:startAngle:endAngle:clockwise:](<addarc(withcenter_radius_startangle_endangle_clockwise_).md>) — Appends an arc to the path.
- [- addCurveToPoint:controlPoint1:controlPoint2:](<addcurve(to_controlpoint1_controlpoint2_).md>) — Appends a cubic Bézier curve to the path.
- [- addQuadCurveToPoint:controlPoint:](<addquadcurve(to_controlpoint_).md>) — Appends a quadratic Bézier curve to the path.
- [- removeAllPoints](<removeallpoints().md>) — Removes all points from the path, effectively deleting all subpaths.
- [- appendPath:](<append(__).md>) — Appends the contents of the specified path object to the path.
- [CGPath](cgpath.md) — The Core Graphics representation of the path.
- [currentPoint](currentpoint.md) — The current point in the graphics path.
