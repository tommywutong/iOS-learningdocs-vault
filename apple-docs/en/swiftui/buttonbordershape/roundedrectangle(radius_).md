---
title: 'roundedRectangle(radius:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/buttonbordershape/roundedrectangle(radius:)'
source_url: 'https://developer.apple.com/documentation/swiftui/buttonbordershape/roundedrectangle(radius:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/buttonbordershape/roundedrectangle%28radius%3A%29.json'
content_hash: 'sha256:c47dcfe13e308983'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ButtonBorderShape](../buttonbordershape.md)

# roundedRectangle(radius:)

<sub>Type Method</sub>

A rounded rectangle shape.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func roundedRectangle(radius: CGFloat) -> ButtonBorderShape
```

## Parameters

- `radius` — The corner radius of the rectangle.

## Discussion

Use the [buttonBorderShape(_:)](<../view/buttonbordershape(__).md>) view modifier to apply the shape to bordered buttons within a view hierarchy.

> [!note] Note
> This has no effect on non-widget system buttons in macOS.

## See Also

### Getting border shapes

- [automatic](automatic.md) — A shape that defers to the system to determine an appropriate shape for the given context and platform.
- [capsule](capsule.md) — A capsule shape.
- [circle](circle.md) — A circular shape.
- [roundedRectangle](roundedrectangle.md) — A rounded rectangle shape.
