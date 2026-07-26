---
title: 'init(string:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicolor/init(string:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cicolor/init(string:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolor/init%28string%3A%29.json'
content_hash: 'sha256:d28e4a207239db11'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIColor](../cicolor.md)

# init(string:)

<sub>Initializer</sub>

Create a Core Image color object in the sRGB color space using a string containing the RGBA color component values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init(string representation: String)
```

## Parameters

- `representation` — A string that contains color and alpha float values. For example, the string: `"0.5 0.7 0.3 1.0"` indicates an RGB color whose components are 50% red, 70% green, 30% blue, and 100% opaque. If the string contains only 3 float values, the alpha component will be `1.0` If the string contains no float values, then `/CIColor/clearColor` will be returned.

## Return Value

An autoreleased [CIColor](../cicolor.md) instance.

## Discussion

On macOS before 10.10, the CIColor’s color space will be Generic RGB.

## See Also

### Creating Color Objects

- [+ colorWithRed:green:blue:](<init(red_green_blue_).md>) — Create a Core Image color object in the sRGB color space with the specified red, green, and blue component values.
- [+ colorWithRed:green:blue:colorSpace:](<init(red_green_blue_colorspace_)-2og6y.md>) — Create a Core Image color object with the specified red, green, and blue component values as measured in the specified color space.
- [+ colorWithRed:green:blue:alpha:colorSpace:](<init(red_green_blue_alpha_colorspace_)-5mvff.md>) — Create a Core Image color object with the specified red, green, blue, and alpha component values as measured in the specified color space.
