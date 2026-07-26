---
title: 'init(_:red:green:blue:opacity:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/color/init(_:red:green:blue:opacity:)'
source_url: 'https://developer.apple.com/documentation/swiftui/color/init(_:red:green:blue:opacity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/color/init%28_%3Ared%3Agreen%3Ablue%3Aopacity%3A%29.json'
content_hash: 'sha256:e5140fad72514b3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Color](../color.md)

# init(_:red:green:blue:opacity:)

<sub>Initializer</sub>

Creates a constant color from red, green, and blue component values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ colorSpace: Color.RGBColorSpace = .sRGB, red: Double, green: Double, blue: Double, opacity: Double = 1)
```

## Parameters

- `colorSpace` — The profile that specifies how to interpret the color for display. The default is [Color.RGBColorSpace.sRGB](rgbcolorspace/srgb.md).

- `red` — The amount of red in the color.

- `green` — The amount of green in the color.

- `blue` — The amount of blue in the color.

- `opacity` — An optional degree of opacity, given in the range `0` to `1`. A value of `0` means 100% transparency, while a value of `1` means 100% opacity. The default is `1`.

## Discussion

This initializer creates a constant color that doesn’t change based on context. For example, it doesn’t have distinct light and dark appearances, unlike various system-defined colors, or a color that you load from an Asset Catalog with [init(_:bundle:)](<init(__bundle_).md>).

A standard sRGB color space clamps each color component — `red`, `green`, and `blue` — to a range of `0` to `1`, but SwiftUI colors use an extended sRGB color space, so you can use component values outside that range. This makes it possible to create colors using the [Color.RGBColorSpace.sRGB](rgbcolorspace/srgb.md) or [Color.RGBColorSpace.sRGBLinear](rgbcolorspace/srgblinear.md) color space that make full use of the wider gamut of a diplay that supports [Color.RGBColorSpace.displayP3](rgbcolorspace/displayp3.md).

## See Also

### Creating a color from component values

- [init(hue:saturation:brightness:opacity:)](<init(hue_saturation_brightness_opacity_).md>) — Creates a constant color from hue, saturation, and brightness values.
- [init(_:white:opacity:)](<init(__white_opacity_).md>) — Creates a constant grayscale color.
- [RGBColorSpace](rgbcolorspace.md) — A profile that specifies how to interpret a color value for display.
