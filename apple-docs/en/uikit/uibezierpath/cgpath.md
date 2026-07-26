---
title: cgPath
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibezierpath/cgpath
source_url: 'https://developer.apple.com/documentation/uikit/uibezierpath/cgpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibezierpath/cgpath.json'
content_hash: 'sha256:eda308112f5c912b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBezierPath](../uibezierpath.md)

# cgPath

<sub>Instance Property</sub>

The Core Graphics representation of the path.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var cgPath: CGPath { get set }
```

## Discussion

This property contains a snapshot of the path at any given point in time. Getting this property returns an immutable path object that you can pass to Core Graphics functions. The path object itself is owned by the `UIBezierPath` object and is valid only until you make further modifications to the path.

You can set the value of this property to a path you built using the functions of the Core Graphics framework. When setting a new path, this method makes a copy of the path you provide.

## See Also

### Constructing a path

- [- moveToPoint:](<move(to_).md>) — Moves the path’s current point to the specified location.
- [- addLineToPoint:](<addline(to_).md>) — Appends a straight line to the path.
- [- addArcWithCenter:radius:startAngle:endAngle:clockwise:](<addarc(withcenter_radius_startangle_endangle_clockwise_).md>) — Appends an arc to the path.
- [- addCurveToPoint:controlPoint1:controlPoint2:](<addcurve(to_controlpoint1_controlpoint2_).md>) — Appends a cubic Bézier curve to the path.
- [- addQuadCurveToPoint:controlPoint:](<addquadcurve(to_controlpoint_).md>) — Appends a quadratic Bézier curve to the path.
- [- closePath](<close().md>) — Closes the most recent subpath.
- [- removeAllPoints](<removeallpoints().md>) — Removes all points from the path, effectively deleting all subpaths.
- [- appendPath:](<append(__).md>) — Appends the contents of the specified path object to the path.
- [currentPoint](currentpoint.md) — The current point in the graphics path.
