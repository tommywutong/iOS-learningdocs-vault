---
title: Color.RGBColorSpace.sRGB
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/color/rgbcolorspace/srgb
source_url: 'https://developer.apple.com/documentation/swiftui/color/rgbcolorspace/srgb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/color/rgbcolorspace/srgb.json'
content_hash: 'sha256:0d69971f19c11ba6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [Color](../../color.md) · [RGBColorSpace](../rgbcolorspace.md)

# Color.RGBColorSpace.sRGB

<sub>Case</sub>

The extended red, green, blue (sRGB) color space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case sRGB
```

## Discussion

For information about the sRGB colorimetry and nonlinear transform function, see the IEC 61966-2-1 specification.

Standard sRGB color spaces clamp the red, green, and blue components of a color to a range of `0` to `1`, but SwiftUI colors use an extended sRGB color space, so you can use component values outside that range.

## See Also

### Getting color spaces

- [Color.RGBColorSpace.sRGBLinear](srgblinear.md) — The extended sRGB color space with a linear transfer function.
- [Color.RGBColorSpace.displayP3](displayp3.md) — The Display P3 color space.
