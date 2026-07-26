---
title: 'init(red:green:blue:alpha:exposure:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicolor/init(red:green:blue:alpha:exposure:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicolor/init(red:green:blue:alpha:exposure:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolor/init%28red%3Agreen%3Ablue%3Aalpha%3Aexposure%3A%29.json'
content_hash: 'sha256:018e74264da440c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColor](../uicolor.md)

# init(red:green:blue:alpha:exposure:)

<sub>Initializer</sub>

Generates an HDR color by applying an exposure to the SDR color defined by the red, green, and blue components. The `red`, `green`, and `blue` components have a nominal range of [0..1], `exposure` is a value \>= 0. To produce an HDR color, we process the given color in a linear color space, multiplying component values by `2^exposure`. The produced color will have a `contentHeadroom` equal to the linearized exposure value. Each whole value of exposure produces a color that is twice as bright.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat, exposure: CGFloat)
```

## See Also

### Creating a color from component values

- [- initWithWhite:alpha:](<init(white_alpha_).md>) — Creates a color object using the specified opacity and grayscale values.
- [- initWithHue:saturation:brightness:alpha:](<init(hue_saturation_brightness_alpha_).md>) — Creates a color object using the specified opacity and HSB color space component values.
- [- initWithRed:green:blue:alpha:](<init(red_green_blue_alpha_).md>) — Creates a color object using the specified opacity and RGB component values.
- [- initWithRed:green:blue:alpha:linearExposure:](<init(red_green_blue_alpha_linearexposure_).md>) — Generates an HDR color by applying an exposure to the SDR color defined by the red, green, and blue components. The `red`, `green`, and `blue` components have a nominal range of [0..1], `linearExposure` is a value \>= 1. To produce an HDR color, we process the given color in a linear color space, multiplying component values by `linearExposure `. The produced color will have a `contentHeadroom` equal to `linearExposure`. Each doubling of `linearExposure` produces a color that is twice as bright.
- [- initWithDisplayP3Red:green:blue:alpha:](<init(displayp3red_green_blue_alpha_).md>) — Creates a color object using the specified opacity and RGB component values in the Display P3 color space.
- [+ colorNamed:](<init(named_).md>) — Creates a color object using the information from the named asset.
- [init(named:inBundle:compatibleWithTraitCollection:)](<init(named_inbundle_compatiblewithtraitcollection_).md>) — Creates a color object using the named asset that’s compatible with the specified trait collection.
