---
title: 'init(red:green:blue:colorSpace:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicolor/init(red:green:blue:colorspace:)-2og6y'
source_url: 'https://developer.apple.com/documentation/coreimage/cicolor/init(red:green:blue:colorspace:)-2og6y'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolor/init%28red%3Agreen%3Ablue%3Acolorspace%3A%29-2og6y.json'
content_hash: 'sha256:3991815ae58cc0f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIColor](../cicolor.md)

# init(red:green:blue:colorSpace:)

<sub>Initializer</sub>

Create a Core Image color object with the specified red, green, and blue component values as measured in the specified color space.

<sub>visionOS</sub>

```swift
convenience init?(red: CGFloat, green: CGFloat, blue: CGFloat, colorSpace: CGColorSpace)
```

## Parameters

- `red` — The color’s unpremultiplied red component value.

- `green` — The color’s unpremultiplied green component value.

- `blue` — The color’s unpremultiplied blue component value.

- `colorSpace` — The color’s `CGColorSpace` which must have `kCGColorSpaceModelRGB`.

## Return Value

An autoreleased [CIColor](../cicolor.md) instance.

## Discussion

This will return `null` if the `CGColorSpace` is not `kCGColorSpaceModelRGB`.

The RGB values can be outside the `0...1` range if the `CGColorSpace` is unclamped.

## See Also

### Creating Color Objects

- [+ colorWithRed:green:blue:](<init(red_green_blue_).md>) — Create a Core Image color object in the sRGB color space with the specified red, green, and blue component values.
- [+ colorWithString:](<init(string_).md>) — Create a Core Image color object in the sRGB color space using a string containing the RGBA color component values.
- [+ colorWithRed:green:blue:alpha:colorSpace:](<init(red_green_blue_alpha_colorspace_)-5mvff.md>) — Create a Core Image color object with the specified red, green, blue, and alpha component values as measured in the specified color space.
