---
title: Color creation
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/color-creation
source_url: 'https://developer.apple.com/documentation/uikit/color-creation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/color-creation.json'
content_hash: 'sha256:80339d75e5e30dcd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Drawing](drawing.md) · [UIColor](uicolor.md)

# Color creation

<sub>API Collection</sub>

Load colors from asset catalogs and create colors from raw component values.

## Overview

Create color objects when you want to use specific colors in your UI, altering the raw component values used by grayscale, RGB, HSB, and CMYK. You can set the specified opacity and RGB component values to create personalized colors that fit your needs. Create colors dynamically by component values changing based on the currently active traits. You can use pattern colors to set the fill or stroke color.

## Topics

### Creating a color from component values

- [- initWithWhite:alpha:](<uicolor/init(white_alpha_).md>) — Creates a color object using the specified opacity and grayscale values.
- [- initWithHue:saturation:brightness:alpha:](<uicolor/init(hue_saturation_brightness_alpha_).md>) — Creates a color object using the specified opacity and HSB color space component values.
- [- initWithRed:green:blue:alpha:](<uicolor/init(red_green_blue_alpha_).md>) — Creates a color object using the specified opacity and RGB component values.
- [- initWithRed:green:blue:alpha:exposure:](<uicolor/init(red_green_blue_alpha_exposure_).md>) — Generates an HDR color by applying an exposure to the SDR color defined by the red, green, and blue components. The `red`, `green`, and `blue` components have a nominal range of [0..1], `exposure` is a value \>= 0. To produce an HDR color, we process the given color in a linear color space, multiplying component values by `2^exposure`. The produced color will have a `contentHeadroom` equal to the linearized exposure value. Each whole value of exposure produces a color that is twice as bright.
- [- initWithRed:green:blue:alpha:linearExposure:](<uicolor/init(red_green_blue_alpha_linearexposure_).md>) — Generates an HDR color by applying an exposure to the SDR color defined by the red, green, and blue components. The `red`, `green`, and `blue` components have a nominal range of [0..1], `linearExposure` is a value \>= 1. To produce an HDR color, we process the given color in a linear color space, multiplying component values by `linearExposure `. The produced color will have a `contentHeadroom` equal to `linearExposure`. Each doubling of `linearExposure` produces a color that is twice as bright.
- [- initWithDisplayP3Red:green:blue:alpha:](<uicolor/init(displayp3red_green_blue_alpha_).md>) — Creates a color object using the specified opacity and RGB component values in the Display P3 color space.
- [+ colorNamed:](<uicolor/init(named_).md>) — Creates a color object using the information from the named asset.
- [init(named:inBundle:compatibleWithTraitCollection:)](<uicolor/init(named_inbundle_compatiblewithtraitcollection_).md>) — Creates a color object using the named asset that’s compatible with the specified trait collection.

### Creating a color dynamically

- [- initWithDynamicProvider:](<uicolor/init(dynamicprovider_).md>) — Creates a color object that uses the specified block to generate its color data dynamically.

### Creating a color from another color object

- [init(_:)](<uicolor/init(__).md>) — Creates a color object that encapsulates a SwiftUI color.
- [- initWithCIColor:](<uicolor/init(cicolor_)-2z057.md>) — Creates a color object that encapsulates a Core Image color.
- [- initWithCGColor:](<uicolor/init(cgcolor_)-27r9g.md>) — Creates a color object using the specified Quartz color reference.
- [- colorWithAlphaComponent:](<uicolor/withalphacomponent(__).md>) — Creates a color object that has the same color space and component values as the receiver, but has the specified alpha component.

### Creating a pattern-based color

- [- initWithPatternImage:](<uicolor/init(patternimage_).md>) — Creates a color object using the specified image object.

### Creating a color from a resource

- [init(resource:)](<uicolor/init(resource_).md>)

## See Also

### Getting existing colors

- [UI element colors](ui-element-colors.md) — Choose colors for UI elements such as labels, text, backgrounds, and links.
- [Standard colors](standard-colors.md) — Define standard color objects for specific shades, such as red, blue, green, black, white, and more.
