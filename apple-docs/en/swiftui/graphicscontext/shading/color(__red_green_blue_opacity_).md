---
title: 'color(_:red:green:blue:opacity:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/shading/color(_:red:green:blue:opacity:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/shading/color(_:red:green:blue:opacity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/shading/color%28_%3Ared%3Agreen%3Ablue%3Aopacity%3A%29.json'
content_hash: 'sha256:3653a1d30281b497'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [Shading](../shading.md)

# color(_:red:green:blue:opacity:)

<sub>Type Method</sub>

Returns a shading instance that fills with a color in the given color space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func color(_ colorSpace: Color.RGBColorSpace = .sRGB, red: Double, green: Double, blue: Double, opacity: Double = 1) -> GraphicsContext.Shading
```

## Parameters

- `colorSpace` — The RGB color space used to define the color. The default is [Color.RGBColorSpace.sRGB](../../color/rgbcolorspace/srgb.md).

- `red` — The red component of the color.

- `green` — The green component of the color.

- `blue` — The blue component of the color.

- `opacity` — The opacity of the color. The default is `1`, which means fully opaque.

## Return Value

A shading instance filled with a color.

## See Also

### Colors

- [color(_:)](<color(__).md>) — Returns a shading instance that fills with a color.
- [color(_:white:opacity:)](<color(__white_opacity_).md>) — Returns a shading instance that fills with a monochrome color in the given color space.
