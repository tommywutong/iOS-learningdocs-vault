---
title: 'init(red:green:blue:alpha:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicolor/init(red:green:blue:alpha:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cicolor/init(red:green:blue:alpha:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolor/init%28red%3Agreen%3Ablue%3Aalpha%3A%29.json'
content_hash: 'sha256:513bc92916456e88'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIColor](../cicolor.md)

# init(red:green:blue:alpha:)

<sub>Initializer</sub>

Initialize a Core Image color object in the sRGB color space with the specified red, green, blue, and alpha component values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)
```

## Parameters

- `red` — The color’s unpremultiplied red component value between 0 and 1.

- `green` — The color’s unpremultiplied green component value between 0 and 1.

- `blue` — The color’s unpremultiplied blue component value between 0 and 1.

- `alpha` — The color’s alpha (opacity) value between 0 and 1.

## Return Value

An initialized [CIColor](../cicolor.md) instance.

## Discussion

On macOS before 10.10, the CIColor’s color space will be Generic RGB.

## See Also

### Initializing Color Objects

- [- initWithCGColor:](<init(cgcolor_)-1hzk4.md>) — Create a Core Image color object with a Core Graphics color object.
- [- initWithColor:](<init(color_).md>)
