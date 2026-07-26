---
title: 'getRed(_:green:blue:alpha:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicolor/getred(_:green:blue:alpha:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicolor/getred(_:green:blue:alpha:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolor/getred%28_%3Agreen%3Ablue%3Aalpha%3A%29.json'
content_hash: 'sha256:e57a91bb74c1a4f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColor](../uicolor.md)

# getRed(_:green:blue:alpha:)

<sub>Instance Method</sub>

Returns the components that form the color in the RGB color space.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func getRed(_ red: UnsafeMutablePointer<CGFloat>?, green: UnsafeMutablePointer<CGFloat>?, blue: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?) -> Bool
```

## Parameters

- `red` — On return, the red component of the color object. On applications linked for iOS 10 or later, an extended range sRGB color space specifies the red component and can have any value. Values between `0.0` and `1.0` are inside the sRGB color gamut. On earlier versions of iOS, the specified value is always between `0.0` and `1.0`.

- `green` — On return, the green component of the color object. On applications linked for iOS 10 or later,an extended range sRGB color space specifies the green component and can have any value. Values between `0.0` and `1.0` are inside the sRGB color gamut. On earlier versions of iOS, the specified value is always between `0.0` and `1.0`.

- `blue` — On return, the blue component of the color object. On applications linked for iOS 10 or later, an extended range sRGB color space specifies the blue component and can have any value. Values between `0.0` and `1.0` are inside the sRGB color gamut. On earlier versions of iOS, the specified value is always between `0.0` and `1.0`.

- `alpha` — On return, the opacity component of the color object, specified as a value between `0.0` and `1.0`.

## Return Value

[true](../../swift/true.md) if the color could be converted, [false](../../swift/false.md) otherwise.

## Discussion

If the color is in a compatible color space, it converts into RGB format and its components return to your application. If the color isn’t in a compatible color space, the parameters don’t change.

## See Also

### Getting the color information

- [Determining color values with color spaces](../determining-color-values-with-color-spaces.md) — Change the system’s interpretation of a color value for display by selecting a color space.
- [CGColor](cgcolor.md) — The Quartz color that corresponds to the color object.
- [CIColor](cicolor.md) — The Core Image color that corresponds to the color object.
- [- getHue:saturation:brightness:alpha:](<gethue(__saturation_brightness_alpha_).md>) — Returns the components that form the color in the HSB color space.
- [- getWhite:alpha:](<getwhite(__alpha_).md>) — Returns the grayscale components of the color.
- [linearExposure](linearexposure.md) — The linear brightness multiplier that was applied when generating this color. Colors created with an exposure by UIColor create CGColors that are tagged with a contentHeadroom value. While CGColors created without a contentHeadroom tag will return 0 from CGColorGetHeadroom, UIColors generated in a similar fashion return a linearExposure of 1.0.
- [accessibilityName](accessibilityname.md) — A localized description of the color for accessibility attributes.
