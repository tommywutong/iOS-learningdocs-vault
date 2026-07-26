---
title: 'append(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibezierpath/append(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibezierpath/append(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibezierpath/append%28_%3A%29.json'
content_hash: 'sha256:cdbc0f89b6a0103f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBezierPath](../uibezierpath.md)

# append(_:)

<sub>Instance Method</sub>

Appends the contents of the specified path object to the path.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func append(_ bezierPath: UIBezierPath)
```

## Parameters

- `bezierPath` — The path to add to the receiver.

## Discussion

This method adds the commands used to create the path in `bezierPath` to the end of the receiver’s path. This method does not explicitly try to connect the subpaths in the two objects, although the operations in `bezierPath` might still cause that effect.

## See Also

### Constructing a path

- [- moveToPoint:](<move(to_).md>) — Moves the path’s current point to the specified location.
- [- addLineToPoint:](<addline(to_).md>) — Appends a straight line to the path.
- [- addArcWithCenter:radius:startAngle:endAngle:clockwise:](<addarc(withcenter_radius_startangle_endangle_clockwise_).md>) — Appends an arc to the path.
- [- addCurveToPoint:controlPoint1:controlPoint2:](<addcurve(to_controlpoint1_controlpoint2_).md>) — Appends a cubic Bézier curve to the path.
- [- addQuadCurveToPoint:controlPoint:](<addquadcurve(to_controlpoint_).md>) — Appends a quadratic Bézier curve to the path.
- [- closePath](<close().md>) — Closes the most recent subpath.
- [- removeAllPoints](<removeallpoints().md>) — Removes all points from the path, effectively deleting all subpaths.
- [CGPath](cgpath.md) — The Core Graphics representation of the path.
- [currentPoint](currentpoint.md) — The current point in the graphics path.
