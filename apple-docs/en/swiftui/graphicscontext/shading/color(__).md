---
title: 'color(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/shading/color(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/shading/color(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/shading/color%28_%3A%29.json'
content_hash: 'sha256:9831b694dc83aa60'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [Shading](../shading.md)

# color(_:)

<sub>Type Method</sub>

Returns a shading instance that fills with a color.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func color(_ color: Color) -> GraphicsContext.Shading
```

## Parameters

- `color` — A [Color](../../color.md) instance that defines the color of the shading.

## Return Value

A shading instance filled with a color.

## See Also

### Colors

- [color(_:red:green:blue:opacity:)](<color(__red_green_blue_opacity_).md>) — Returns a shading instance that fills with a color in the given color space.
- [color(_:white:opacity:)](<color(__white_opacity_).md>) — Returns a shading instance that fills with a monochrome color in the given color space.
