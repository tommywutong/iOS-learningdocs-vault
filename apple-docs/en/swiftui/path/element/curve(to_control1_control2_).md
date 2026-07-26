---
title: 'Path.Element.curve(to:control1:control2:)'
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/path/element/curve(to:control1:control2:)'
source_url: 'https://developer.apple.com/documentation/swiftui/path/element/curve(to:control1:control2:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/path/element/curve%28to%3Acontrol1%3Acontrol2%3A%29.json'
content_hash: 'sha256:c6709d3a301fb2b9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [Path](../../path.md) · [Element](../element.md)

# Path.Element.curve(to:control1:control2:)

<sub>Case</sub>

A cubic Bézier curve from the previous current point to the given end-point, using the two control points to define the curve.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case curve(to: CGPoint, control1: CGPoint, control2: CGPoint)
```

## Discussion

The end-point of the curve becomes the new current point.

## See Also

### Getting path elements

- [Path.Element.closeSubpath](closesubpath.md) — A line from the start point of the current subpath (if any) to the current point, which terminates the subpath.
- [Path.Element.line(to:)](<line(to_).md>) — A line from the previous current point to the given point, which becomes the new current point.
- [Path.Element.move(to:)](<move(to_).md>) — A path element that terminates the current subpath (without closing it) and defines a new current point.
- [Path.Element.quadCurve(to:control:)](<quadcurve(to_control_).md>) — A quadratic Bézier curve from the previous current point to the given end-point, using the single control point to define the curve.
