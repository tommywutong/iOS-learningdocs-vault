---
title: Color.RGBColorSpace.sRGBLinear
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/color/rgbcolorspace/srgblinear
source_url: 'https://developer.apple.com/documentation/swiftui/color/rgbcolorspace/srgblinear'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/color/rgbcolorspace/srgblinear.json'
content_hash: 'sha256:653a75778ec10a9a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [Color](../../color.md) · [RGBColorSpace](../rgbcolorspace.md)

# Color.RGBColorSpace.sRGBLinear

<sub>Case</sub>

The extended sRGB color space with a linear transfer function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case sRGBLinear
```

## Discussion

This color space has the same colorimetry as [Color.RGBColorSpace.sRGB](srgb.md), but uses a linear transfer function.

Standard sRGB color spaces clamp the red, green, and blue components of a color to a range of `0` to `1`, but SwiftUI colors use an extended sRGB color space, so you can use component values outside that range.

## See Also

### Getting color spaces

- [Color.RGBColorSpace.sRGB](srgb.md) — The extended red, green, blue (sRGB) color space.
- [Color.RGBColorSpace.displayP3](displayp3.md) — The Display P3 color space.
