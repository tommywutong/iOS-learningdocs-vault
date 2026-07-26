---
title: 'getWhite(_:alpha:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicolor/getwhite(_:alpha:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicolor/getwhite(_:alpha:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolor/getwhite%28_%3Aalpha%3A%29.json'
content_hash: 'sha256:b5b6795b971f269f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColor](../uicolor.md)

# getWhite(_:alpha:)

<sub>Instance Method</sub>

Returns the grayscale components of the color.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func getWhite(_ white: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?) -> Bool
```

## Parameters

- `white` — On return, the grayscale component of the color object. On applications linked for iOS 10 or later, an extended range gray color space specifies the grayscale component and can have any value. Values between `0.0` and `1.0` are inside the sRGB color gamut. On earlier versions of iOS, the specified value is always between `0.0` and `1.0`.

- `alpha` — On return, the opacity component of the color object, specified as a value between `0.0` and `1.0`.

## Return Value

[true](../../swift/true.md) if the color could be converted, [false](../../swift/false.md) otherwise.

## Discussion

If the color is in a compatible color space, it converts into grayscale format and its returned to your application. If the color isn’t in a compatible color space, the parameters don’t change.

## See Also

### Getting the color information

- [Determining color values with color spaces](../determining-color-values-with-color-spaces.md) — Change the system’s interpretation of a color value for display by selecting a color space.
- [CGColor](cgcolor.md) — The Quartz color that corresponds to the color object.
- [CIColor](cicolor.md) — The Core Image color that corresponds to the color object.
- [- getHue:saturation:brightness:alpha:](<gethue(__saturation_brightness_alpha_).md>) — Returns the components that form the color in the HSB color space.
- [- getRed:green:blue:alpha:](<getred(__green_blue_alpha_).md>) — Returns the components that form the color in the RGB color space.
- [linearExposure](linearexposure.md) — The linear brightness multiplier that was applied when generating this color. Colors created with an exposure by UIColor create CGColors that are tagged with a contentHeadroom value. While CGColors created without a contentHeadroom tag will return 0 from CGColorGetHeadroom, UIColors generated in a similar fashion return a linearExposure of 1.0.
- [accessibilityName](accessibilityname.md) — A localized description of the color for accessibility attributes.
