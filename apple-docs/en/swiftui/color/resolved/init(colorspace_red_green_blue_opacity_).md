---
title: 'init(colorSpace:red:green:blue:opacity:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/color/resolved/init(colorspace:red:green:blue:opacity:)'
source_url: 'https://developer.apple.com/documentation/swiftui/color/resolved/init(colorspace:red:green:blue:opacity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/color/resolved/init%28colorspace%3Ared%3Agreen%3Ablue%3Aopacity%3A%29.json'
content_hash: 'sha256:83c6b9f3f1d24cf7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [Color](../../color.md) · [Resolved](../resolved.md)

# init(colorSpace:red:green:blue:opacity:)

<sub>Initializer</sub>

Creates a resolved color from red, green, and blue component values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(colorSpace: Color.RGBColorSpace = .sRGB, red: Float, green: Float, blue: Float, opacity: Float = 1)
```

## Parameters

- `colorSpace` — The profile that specifies how to interpret the color for display. The default is [Color.RGBColorSpace.sRGB](../rgbcolorspace/srgb.md).

- `red` — The amount of red in the color.

- `green` — The amount of green in the color.

- `blue` — The amount of blue in the color.

- `opacity` — An optional degree of opacity, given in the range `0` to `1`. A value of `0` means 100% transparency, while a value of `1` means 100% opacity. The default is `1`.

## Discussion

A standard sRGB color space clamps each color component — `red`, `green`, and `blue` — to a range of `0` to `1`, but SwiftUI colors use an extended sRGB color space, so you can use component values outside that range. This makes it possible to create colors using the [Color.RGBColorSpace.sRGB](../rgbcolorspace/srgb.md) or [Color.RGBColorSpace.sRGBLinear](../rgbcolorspace/srgblinear.md) color space that make full use of the wider gamut of a diplay that supports [Color.RGBColorSpace.displayP3](../rgbcolorspace/displayp3.md).
