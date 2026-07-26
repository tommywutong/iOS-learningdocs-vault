---
title: Color.RGBColorSpace
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/color/rgbcolorspace
source_url: 'https://developer.apple.com/documentation/swiftui/color/rgbcolorspace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/color/rgbcolorspace.json'
content_hash: 'sha256:0b7c72fff21fe2d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Color](../color.md)

# Color.RGBColorSpace

<sub>Enumeration</sub>

A profile that specifies how to interpret a color value for display.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum RGBColorSpace
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting color spaces

- [Color.RGBColorSpace.sRGB](rgbcolorspace/srgb.md) — The extended red, green, blue (sRGB) color space.
- [Color.RGBColorSpace.sRGBLinear](rgbcolorspace/srgblinear.md) — The extended sRGB color space with a linear transfer function.
- [Color.RGBColorSpace.displayP3](rgbcolorspace/displayp3.md) — The Display P3 color space.

## See Also

### Creating a color from component values

- [init(hue:saturation:brightness:opacity:)](<init(hue_saturation_brightness_opacity_).md>) — Creates a constant color from hue, saturation, and brightness values.
- [init(_:white:opacity:)](<init(__white_opacity_).md>) — Creates a constant grayscale color.
- [init(_:red:green:blue:opacity:)](<init(__red_green_blue_opacity_).md>) — Creates a constant color from red, green, and blue component values.
