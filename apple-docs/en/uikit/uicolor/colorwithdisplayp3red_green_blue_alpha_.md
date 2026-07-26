---
title: 'colorWithDisplayP3Red:green:blue:alpha:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicolor/colorwithdisplayp3red:green:blue:alpha:'
source_url: 'https://developer.apple.com/documentation/uikit/uicolor/colorwithdisplayp3red:green:blue:alpha:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolor/colorwithdisplayp3red%3Agreen%3Ablue%3Aalpha%3A.json'
content_hash: 'sha256:9c9f343e342c741b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColor](../uicolor.md)

# colorWithDisplayP3Red:green:blue:alpha:

<sub>Type Method</sub>

Creates a color object using the specified opacity and RGB component values in the Display P3 color space.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (UIColor *) colorWithDisplayP3Red:(CGFloat) displayP3Red green:(CGFloat) green blue:(CGFloat) blue alpha:(CGFloat) alpha;
```

## Parameters

- `displayP3Red` — The red component of the color object, specified as a value from 0.0 to 1.0.

- `green` — The green component of the color object, specified as a value from 0.0 to 1.0.

- `blue` — The blue component of the color object, specified as a value from 0.0 to 1.0.

- `alpha` — The opacity value of the color object, specified as a value from 0.0 to 1.0. Alpha values below 0.0 are interpreted as 0.0, and values above 1.0 are interpreted as 1.0.

## Return Value

The color object. The color information represented by this object is in an extended range sRGB colorspace. On applications linked for iOS 10 or later, the color is specified in an extended range sRGB color space.

## Discussion

Values below 0.0 are interpreted as 0.0, and values above 1.0 are interpreted as 1.0.

## See Also

### Creating a color from component values

- [colorWithWhite:alpha:](colorwithwhite_alpha_.md) — Creates a color object using the specified opacity and grayscale values.
- [colorWithHue:saturation:brightness:alpha:](colorwithhue_saturation_brightness_alpha_.md) — Creates a color object using the specified opacity and HSB color space component values.
- [colorWithRed:green:blue:alpha:](colorwithred_green_blue_alpha_.md) — Creates a color object using the specified opacity and RGB component values.
- [- initWithWhite:alpha:](<init(white_alpha_).md>) — Creates a color object using the specified opacity and grayscale values.
- [- initWithHue:saturation:brightness:alpha:](<init(hue_saturation_brightness_alpha_).md>) — Creates a color object using the specified opacity and HSB color space component values.
- [- initWithRed:green:blue:alpha:](<init(red_green_blue_alpha_).md>) — Creates a color object using the specified opacity and RGB component values.
- [- initWithRed:green:blue:alpha:exposure:](<init(red_green_blue_alpha_exposure_).md>) — Generates an HDR color by applying an exposure to the SDR color defined by the red, green, and blue components. The `red`, `green`, and `blue` components have a nominal range of [0..1], `exposure` is a value \>= 0. To produce an HDR color, we process the given color in a linear color space, multiplying component values by `2^exposure`. The produced color will have a `contentHeadroom` equal to the linearized exposure value. Each whole value of exposure produces a color that is twice as bright.
- [- initWithRed:green:blue:alpha:linearExposure:](<init(red_green_blue_alpha_linearexposure_).md>) — Generates an HDR color by applying an exposure to the SDR color defined by the red, green, and blue components. The `red`, `green`, and `blue` components have a nominal range of [0..1], `linearExposure` is a value \>= 1. To produce an HDR color, we process the given color in a linear color space, multiplying component values by `linearExposure `. The produced color will have a `contentHeadroom` equal to `linearExposure`. Each doubling of `linearExposure` produces a color that is twice as bright.
- [- initWithDisplayP3Red:green:blue:alpha:](<init(displayp3red_green_blue_alpha_).md>) — Creates a color object using the specified opacity and RGB component values in the Display P3 color space.
- [+ colorNamed:](<init(named_).md>) — Creates a color object using the information from the named asset.
