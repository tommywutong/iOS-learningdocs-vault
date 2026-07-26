---
title: cgColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicolor/cgcolor
source_url: 'https://developer.apple.com/documentation/uikit/uicolor/cgcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolor/cgcolor.json'
content_hash: 'sha256:4ead116826aa0d91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColor](../uicolor.md)

# cgColor

<sub>Instance Property</sub>

The Quartz color that corresponds to the color object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var cgColor: CGColor { get }
```

## Discussion

The color object in this property doesn’t adapt automatically to Dark Mode changes. If you use it to set the color of interface elements, you must update that color yourself. You update that color when the [userInterfaceStyle](../uitraitcollection/userinterfacestyle.md) trait of the current trait collection changes.

For information on how to apply color information reliably, see [Supporting Dark Mode in your interface](../supporting-dark-mode-in-your-interface.md).

## See Also

### Getting the color information

- [Determining color values with color spaces](../determining-color-values-with-color-spaces.md) — Change the system’s interpretation of a color value for display by selecting a color space.
- [CIColor](cicolor.md) — The Core Image color that corresponds to the color object.
- [- getHue:saturation:brightness:alpha:](<gethue(__saturation_brightness_alpha_).md>) — Returns the components that form the color in the HSB color space.
- [- getRed:green:blue:alpha:](<getred(__green_blue_alpha_).md>) — Returns the components that form the color in the RGB color space.
- [- getWhite:alpha:](<getwhite(__alpha_).md>) — Returns the grayscale components of the color.
- [linearExposure](linearexposure.md) — The linear brightness multiplier that was applied when generating this color. Colors created with an exposure by UIColor create CGColors that are tagged with a contentHeadroom value. While CGColors created without a contentHeadroom tag will return 0 from CGColorGetHeadroom, UIColors generated in a similar fashion return a linearExposure of 1.0.
- [accessibilityName](accessibilityname.md) — A localized description of the color for accessibility attributes.
