---
title: Path.Element
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/path/element
source_url: 'https://developer.apple.com/documentation/swiftui/path/element'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/path/element.json'
content_hash: 'sha256:2ae6c8445fcd027b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Path](../path.md)

# Path.Element

<sub>Enumeration</sub>

An element of a path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum Element
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Copyable](../../swift/copyable.md), [Equatable](../../swift/equatable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting path elements

- [Path.Element.closeSubpath](element/closesubpath.md) — A line from the start point of the current subpath (if any) to the current point, which terminates the subpath.
- [Path.Element.curve(to:control1:control2:)](<element/curve(to_control1_control2_).md>) — A cubic Bézier curve from the previous current point to the given end-point, using the two control points to define the curve.
- [Path.Element.line(to:)](<element/line(to_).md>) — A line from the previous current point to the given point, which becomes the new current point.
- [Path.Element.move(to:)](<element/move(to_).md>) — A path element that terminates the current subpath (without closing it) and defines a new current point.
- [Path.Element.quadCurve(to:control:)](<element/quadcurve(to_control_).md>) — A quadratic Bézier curve from the previous current point to the given end-point, using the single control point to define the curve.

## See Also

### Operating over path elements

- [forEach(_:)](<foreach(__).md>) — Calls `body` with each element in the path.
