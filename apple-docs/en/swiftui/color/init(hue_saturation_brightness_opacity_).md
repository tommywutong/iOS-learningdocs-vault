---
title: 'init(hue:saturation:brightness:opacity:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/color/init(hue:saturation:brightness:opacity:)'
source_url: 'https://developer.apple.com/documentation/swiftui/color/init(hue:saturation:brightness:opacity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/color/init%28hue%3Asaturation%3Abrightness%3Aopacity%3A%29.json'
content_hash: 'sha256:87c2a82b970ca6ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Color](../color.md)

# init(hue:saturation:brightness:opacity:)

<sub>Initializer</sub>

Creates a constant color from hue, saturation, and brightness values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(hue: Double, saturation: Double, brightness: Double, opacity: Double = 1)
```

## Parameters

- `hue` — A value in the range `0` to `1` that maps to an angle from 0° to 360° to represent a shade on the color wheel.

- `saturation` — A value in the range `0` to `1` that indicates how strongly the hue affects the color. A value of `0` removes the effect of the hue, resulting in gray. As the value increases, the hue becomes more prominent.

- `brightness` — A value in the range `0` to `1` that indicates how bright a color is. A value of `0` results in black, regardless of the other components. The color lightens as you increase this component.

- `opacity` — An optional degree of opacity, given in the range `0` to `1`. A value of `0` means 100% transparency, while a value of `1` means 100% opacity. The default is `1`.

## Discussion

This initializer creates a constant color that doesn’t change based on context. For example, it doesn’t have distinct light and dark appearances, unlike various system-defined colors, or a color that you load from an Asset Catalog with [init(_:bundle:)](<init(__bundle_).md>).

## See Also

### Creating a color from component values

- [init(_:white:opacity:)](<init(__white_opacity_).md>) — Creates a constant grayscale color.
- [init(_:red:green:blue:opacity:)](<init(__red_green_blue_opacity_).md>) — Creates a constant color from red, green, and blue component values.
- [RGBColorSpace](rgbcolorspace.md) — A profile that specifies how to interpret a color value for display.
