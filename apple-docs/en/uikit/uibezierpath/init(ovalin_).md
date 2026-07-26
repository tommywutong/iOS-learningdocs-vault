---
title: 'init(ovalIn:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibezierpath/init(ovalin:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibezierpath/init(ovalin:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibezierpath/init%28ovalin%3A%29.json'
content_hash: 'sha256:3a76289df8008059'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBezierPath](../uibezierpath.md)

# init(ovalIn:)

<sub>Initializer</sub>

Creates and returns a new Bézier path object with an inscribed oval path in the specified rectangle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
convenience init(ovalIn rect: CGRect)
```

## Parameters

- `rect` — The rectangle in which to inscribe an oval.

## Return Value

A new path object with the oval path.

## Discussion

This method creates a closed subpath that approximates the oval using a sequence of Bézier curves. The path is created in a clockwise direction (relative to the default coordinate system). If the `rect` parameter specifies a square, the inscribed path is a circle.

## See Also

### Creating a Bézier path

- [+ bezierPathWithRect:](<init(rect_).md>) — Creates and returns a new Bézier path object with a rectangular path.
- [+ bezierPathWithRoundedRect:cornerRadius:](<init(roundedrect_cornerradius_).md>) — Creates and returns a new Bézier path object with a rounded rectangular path.
- [+ bezierPathWithRoundedRect:byRoundingCorners:cornerRadii:](<init(roundedrect_byroundingcorners_cornerradii_).md>) — Creates and returns a new Bézier path object with a rectangular path rounded at the specified corners.
- [+ bezierPathWithArcCenter:radius:startAngle:endAngle:clockwise:](<init(arccenter_radius_startangle_endangle_clockwise_).md>) — Creates and returns a new Bézier path object with an arc of a circle.
- [+ bezierPathWithCGPath:](<init(cgpath_)-833n8.md>) — Creates and returns a new Bézier path object with the contents of a Core Graphics path.
- [- bezierPathByReversingPath](<reversing().md>) — Creates and returns a new Bézier path object with the reversed contents of the current path.
- [- init](<init().md>) — Creates and returns an empty path object.
- [- initWithCoder:](<init(coder_).md>) — Creates a Bézier path object from data in an unarchiver.
