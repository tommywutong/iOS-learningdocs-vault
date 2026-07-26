---
title: 'init(red:green:blue:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicolor/init(red:green:blue:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cicolor/init(red:green:blue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolor/init%28red%3Agreen%3Ablue%3A%29.json'
content_hash: 'sha256:3c6ee1a15bfce461'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIColor](../cicolor.md)

# init(red:green:blue:)

<sub>Initializer</sub>

Create a Core Image color object in the sRGB color space with the specified red, green, and blue component values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init(red: CGFloat, green: CGFloat, blue: CGFloat)
```

## Parameters

- `red` — The color’s unpremultiplied red component value between 0 and 1.

- `green` — The color’s unpremultiplied green component value between 0 and 1.

- `blue` — The color’s unpremultiplied blue component value between 0 and 1.

## Return Value

An autoreleased [CIColor](../cicolor.md) instance.

## Discussion

On macOS before 10.10, the CIColor’s color space will be Generic RGB.

## See Also

### Creating Color Objects

- [+ colorWithString:](<init(string_).md>) — Create a Core Image color object in the sRGB color space using a string containing the RGBA color component values.
- [+ colorWithRed:green:blue:colorSpace:](<init(red_green_blue_colorspace_)-2og6y.md>) — Create a Core Image color object with the specified red, green, and blue component values as measured in the specified color space.
- [+ colorWithRed:green:blue:alpha:colorSpace:](<init(red_green_blue_alpha_colorspace_)-5mvff.md>) — Create a Core Image color object with the specified red, green, blue, and alpha component values as measured in the specified color space.
