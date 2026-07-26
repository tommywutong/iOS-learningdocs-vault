---
title: 'init(cgPath:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibezierpath/init(cgpath:)-833n8'
source_url: 'https://developer.apple.com/documentation/uikit/uibezierpath/init(cgpath:)-833n8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibezierpath/init%28cgpath%3A%29-833n8.json'
content_hash: 'sha256:cf575cd53691eafe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBezierPath](../uibezierpath.md)

# init(cgPath:)

<sub>Initializer</sub>

Creates and returns a new Bézier path object with the contents of a Core Graphics path.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
convenience init(cgPath CGPath: CGPath)
```

## Parameters

- `CGPath` — The Core Graphics path from which to obtain the initial path information. If this parameter is `nil`, the method raises an exception.

## Return Value

A new path object with the specified path information.

## See Also

### Creating a Bézier path

- [+ bezierPathWithRect:](<init(rect_).md>) — Creates and returns a new Bézier path object with a rectangular path.
- [+ bezierPathWithOvalInRect:](<init(ovalin_).md>) — Creates and returns a new Bézier path object with an inscribed oval path in the specified rectangle.
- [+ bezierPathWithRoundedRect:cornerRadius:](<init(roundedrect_cornerradius_).md>) — Creates and returns a new Bézier path object with a rounded rectangular path.
- [+ bezierPathWithRoundedRect:byRoundingCorners:cornerRadii:](<init(roundedrect_byroundingcorners_cornerradii_).md>) — Creates and returns a new Bézier path object with a rectangular path rounded at the specified corners.
- [+ bezierPathWithArcCenter:radius:startAngle:endAngle:clockwise:](<init(arccenter_radius_startangle_endangle_clockwise_).md>) — Creates and returns a new Bézier path object with an arc of a circle.
- [- bezierPathByReversingPath](<reversing().md>) — Creates and returns a new Bézier path object with the reversed contents of the current path.
- [- init](<init().md>) — Creates and returns an empty path object.
- [- initWithCoder:](<init(coder_).md>) — Creates a Bézier path object from data in an unarchiver.
