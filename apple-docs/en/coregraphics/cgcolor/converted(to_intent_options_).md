---
title: 'converted(to:intent:options:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcolor/converted(to:intent:options:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolor/converted(to:intent:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolor/converted%28to%3Aintent%3Aoptions%3A%29.json'
content_hash: 'sha256:8693c38b12faf753'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColor](../cgcolor.md)

# converted(to:intent:options:)

<sub>Instance Method</sub>

Creates a new color in a different color space that matches the provided color.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func converted(to _: CGColorSpace, intent: CGColorRenderingIntent, options: CFDictionary?) -> CGColor?
```

### Parameters

- **CGColorSpaceRef** — The destination color space.
- **to** — The destination color space.
- **intent** — The mechanism to use to match the color when the color is outside the gamut of the new color space.
- **color** — The color to convert.
- **options** — A dictionary of options used to convert the color. Currently, you should pass `NULL`.

### Returns

A new color in the destination color space that matches (or closely approximates) the source color.

## Discussion

To create the new color, this method creates a `CFColorConverterRef` using the options you specified and applies it to the source color.

## See Also

### Converting Between Color Spaces

- [kCGColorConversionTRCSize](conversiontrcsize.md)
