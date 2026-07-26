---
title: linearExposure
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicolor/linearexposure
source_url: 'https://developer.apple.com/documentation/uikit/uicolor/linearexposure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolor/linearexposure.json'
content_hash: 'sha256:d1545254c13af21d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColor](../uicolor.md)

# linearExposure

<sub>Instance Property</sub>

The linear brightness multiplier that was applied when generating this color. Colors created with an exposure by UIColor create CGColors that are tagged with a contentHeadroom value. While CGColors created without a contentHeadroom tag will return 0 from CGColorGetHeadroom, UIColors generated in a similar fashion return a linearExposure of 1.0.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var linearExposure: CGFloat { get }
```

## See Also

### Getting the color information

- [Determining color values with color spaces](../determining-color-values-with-color-spaces.md) — Change the system’s interpretation of a color value for display by selecting a color space.
- [CGColor](cgcolor.md) — The Quartz color that corresponds to the color object.
- [CIColor](cicolor.md) — The Core Image color that corresponds to the color object.
- [- getHue:saturation:brightness:alpha:](<gethue(__saturation_brightness_alpha_).md>) — Returns the components that form the color in the HSB color space.
- [- getRed:green:blue:alpha:](<getred(__green_blue_alpha_).md>) — Returns the components that form the color in the RGB color space.
- [- getWhite:alpha:](<getwhite(__alpha_).md>) — Returns the grayscale components of the color.
- [accessibilityName](accessibilityname.md) — A localized description of the color for accessibility attributes.
