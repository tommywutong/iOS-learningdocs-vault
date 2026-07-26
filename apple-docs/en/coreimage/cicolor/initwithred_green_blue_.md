---
title: 'initWithRed:green:blue:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicolor/initwithred:green:blue:'
source_url: 'https://developer.apple.com/documentation/coreimage/cicolor/initwithred:green:blue:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolor/initwithred%3Agreen%3Ablue%3A.json'
content_hash: 'sha256:aa171353ad8a484d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIColor](../cicolor.md)

# initWithRed:green:blue:

<sub>Instance Method</sub>

Initialize a Core Image color object in the sRGB color space with the specified red, green, and blue component values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (instancetype) initWithRed:(CGFloat) red green:(CGFloat) green blue:(CGFloat) blue;
```

## Parameters

- `red` — The color’s unpremultiplied red component value between 0 and 1.

- `green` — The color’s unpremultiplied green component value between 0 and 1.

- `blue` — The color’s unpremultiplied blue component value between 0 and 1.

## Return Value

An initialized [CIColor](../cicolor.md) instance.

## Discussion

On macOS before 10.10, the CIColor’s color space will be Generic RGB.

## See Also

### Initializing Color Objects

- [- initWithCGColor:](<init(cgcolor_)-1hzk4.md>) — Create a Core Image color object with a Core Graphics color object.
- [- initWithColor:](<init(color_).md>)
- [- initWithRed:green:blue:alpha:](<init(red_green_blue_alpha_).md>) — Initialize a Core Image color object in the sRGB color space with the specified red, green, blue, and alpha component values.
