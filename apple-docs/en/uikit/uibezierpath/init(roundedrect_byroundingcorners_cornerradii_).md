---
title: 'init(roundedRect:byRoundingCorners:cornerRadii:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibezierpath/init(roundedrect:byroundingcorners:cornerradii:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibezierpath/init(roundedrect:byroundingcorners:cornerradii:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibezierpath/init%28roundedrect%3Abyroundingcorners%3Acornerradii%3A%29.json'
content_hash: 'sha256:768228d5c73cc283'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBezierPath](../uibezierpath.md)

# init(roundedRect:byRoundingCorners:cornerRadii:)

<sub>Initializer</sub>

Creates and returns a new Bézier path object with a rectangular path rounded at the specified corners.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
convenience init(roundedRect rect: CGRect, byRoundingCorners corners: UIRectCorner, cornerRadii: CGSize)
```

## Parameters

- `rect` — The rectangle that defines the basic shape of the path.

- `corners` — A bitmask value that identifies the corners that you want rounded. You can use this parameter to round only a subset of the corners of the rectangle.

- `cornerRadii` — The radius of each corner oval. Values larger than half the rectangle’s width or height are clamped appropriately to half the width or height.

## Return Value

A new path object with the rounded rectangular path.

## Discussion

This method creates a closed subpath, proceeding in a clockwise direction (relative to the default coordinate system) as it creates the necessary line and curve segments.

## See Also

### Creating a Bézier path

- [+ bezierPathWithRect:](<init(rect_).md>) — Creates and returns a new Bézier path object with a rectangular path.
- [+ bezierPathWithOvalInRect:](<init(ovalin_).md>) — Creates and returns a new Bézier path object with an inscribed oval path in the specified rectangle.
- [+ bezierPathWithRoundedRect:cornerRadius:](<init(roundedrect_cornerradius_).md>) — Creates and returns a new Bézier path object with a rounded rectangular path.
- [+ bezierPathWithArcCenter:radius:startAngle:endAngle:clockwise:](<init(arccenter_radius_startangle_endangle_clockwise_).md>) — Creates and returns a new Bézier path object with an arc of a circle.
- [+ bezierPathWithCGPath:](<init(cgpath_)-833n8.md>) — Creates and returns a new Bézier path object with the contents of a Core Graphics path.
- [- bezierPathByReversingPath](<reversing().md>) — Creates and returns a new Bézier path object with the reversed contents of the current path.
- [- init](<init().md>) — Creates and returns an empty path object.
- [- initWithCoder:](<init(coder_).md>) — Creates a Bézier path object from data in an unarchiver.
