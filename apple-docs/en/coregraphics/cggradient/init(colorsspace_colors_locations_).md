---
title: 'init(colorsSpace:colors:locations:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cggradient/init(colorsspace:colors:locations:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cggradient/init(colorsspace:colors:locations:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cggradient/init%28colorsspace%3Acolors%3Alocations%3A%29.json'
content_hash: 'sha256:991059fcabd6c00e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGGradient](../cggradient.md)

# init(colorsSpace:colors:locations:)

<sub>Initializer</sub>

Creates a gradient object from a color space and the provided color objects and locations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(colorsSpace space: CGColorSpace?, colors: CFArray, locations: UnsafePointer<CGFloat>?)
```

## Parameters

- `space` — The color space to use for the gradient. You cannot use a pattern or indexed color space.

- `colors` — A non-empty array of [CGColor](../cgcolor.md) objects that should be in the color space specified by `space`. If `space` is not `NULL`, each color will be converted (if necessary) to that color space and the gradient will drawn in that color space. Otherwise, each color will be converted to and drawn in the GenericRGB color space.

- `locations` — The location for each color provided in `colors`; each location must be a [CGFloat](../../corefoundation/cgfloat-swift.struct.md) value in the range of `0` to `1`, inclusive. If `0` and `1` are not in the `locations` array, Quartz uses the colors provided that are closest to `0` and `1` for those locations. If `locations` is `NULL`, the first color in `colors` is assigned to location `0`, the last color in `colors` is assigned to location `1`, and intervening colors are assigned locations that are at equal intervals in between. The `locations` array should contain the same number of items as the `colors` array.

## Return Value

A [CGGradient](../cggradient.md) object.

## See Also

### Related Documentation

- [CGContextDrawRadialGradient](<../cgcontext/drawradialgradient(__startcenter_startradius_endcenter_endradius_options_).md>) — Paints a gradient fill that varies along the area defined by the provided starting and ending circles.
- [CGContextDrawLinearGradient](<../cgcontext/drawlineargradient(__start_end_options_).md>) — Paints a gradient fill that varies along the line defined by the provided starting and ending points.

### Creating Gradient Instances

- [CGGradientCreateWithColorComponents](<init(colorspace_colorcomponents_locations_count_).md>) — Creates a CGGradient object from a color space and the provided color components and locations.
