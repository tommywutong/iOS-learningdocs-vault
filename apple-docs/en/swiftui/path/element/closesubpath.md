---
title: Path.Element.closeSubpath
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/path/element/closesubpath
source_url: 'https://developer.apple.com/documentation/swiftui/path/element/closesubpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/path/element/closesubpath.json'
content_hash: 'sha256:e685f4ae1fee69dd'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [Path](../../path.md) · [Element](../element.md)

# Path.Element.closeSubpath

<sub>Case</sub>

A line from the start point of the current subpath (if any) to the current point, which terminates the subpath.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case closeSubpath
```

## Discussion

After closing the subpath, the current point becomes undefined.

## See Also

### Getting path elements

- [Path.Element.curve(to:control1:control2:)](<curve(to_control1_control2_).md>) — A cubic Bézier curve from the previous current point to the given end-point, using the two control points to define the curve.
- [Path.Element.line(to:)](<line(to_).md>) — A line from the previous current point to the given point, which becomes the new current point.
- [Path.Element.move(to:)](<move(to_).md>) — A path element that terminates the current subpath (without closing it) and defines a new current point.
- [Path.Element.quadCurve(to:control:)](<quadcurve(to_control_).md>) — A quadratic Bézier curve from the previous current point to the given end-point, using the single control point to define the curve.
