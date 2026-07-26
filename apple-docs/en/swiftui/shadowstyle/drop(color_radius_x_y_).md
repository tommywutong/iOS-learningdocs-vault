---
title: 'drop(color:radius:x:y:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shadowstyle/drop(color:radius:x:y:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shadowstyle/drop(color:radius:x:y:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shadowstyle/drop%28color%3Aradius%3Ax%3Ay%3A%29.json'
content_hash: 'sha256:d7eda72448efd029'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShadowStyle](../shadowstyle.md)

# drop(color:radius:x:y:)

<sub>Type Method</sub>

Creates a custom drop shadow style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func drop(color: Color = .init(.sRGBLinear, white: 0, opacity: 0.33), radius: CGFloat, x: CGFloat = 0, y: CGFloat = 0) -> ShadowStyle
```

## Parameters

- `color` — The shadow’s color.

- `radius` — The shadow’s size.

- `x` — A horizontal offset you use to position the shadow relative to this view.

- `y` — A vertical offset you use to position the shadow relative to this view.

## Return Value

A new shadow style.

## Discussion

Drop shadows draw behind the source content by blurring, tinting and offsetting its per-pixel alpha values.

## See Also

### Getting shadow styles

- [inner(color:radius:x:y:)](<inner(color_radius_x_y_).md>) — Creates a custom inner shadow style.
