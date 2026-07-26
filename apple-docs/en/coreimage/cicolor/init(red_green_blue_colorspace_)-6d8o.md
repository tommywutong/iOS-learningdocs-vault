---
title: 'init(red:green:blue:colorSpace:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicolor/init(red:green:blue:colorspace:)-6d8o'
source_url: 'https://developer.apple.com/documentation/coreimage/cicolor/init(red:green:blue:colorspace:)-6d8o'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolor/init%28red%3Agreen%3Ablue%3Acolorspace%3A%29-6d8o.json'
content_hash: 'sha256:88229321333f2544'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIColor](../cicolor.md)

# init(red:green:blue:colorSpace:)

<sub>Initializer</sub>

Initialize a Core Image color object with the specified red, green, and blue component values as measured in the specified color space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
convenience init?(red: CGFloat, green: CGFloat, blue: CGFloat, colorSpace: CGColorSpace)
```

## Parameters

- `red` — The color’s unpremultiplied red component value.

- `green` — The color’s unpremultiplied green component value.

- `blue` — The color’s unpremultiplied blue component value.

- `colorSpace` — The color’s `CGColorSpace` which must have `kCGColorSpaceModelRGB`.

## Return Value

An initialized [CIColor](../cicolor.md) instance.

## Discussion

This will return null if the `CGColorSpace` is not `kCGColorSpaceModelRGB`. The RGB values can be outside the `0...1` range if the `CGColorSpace` is unclamped.
