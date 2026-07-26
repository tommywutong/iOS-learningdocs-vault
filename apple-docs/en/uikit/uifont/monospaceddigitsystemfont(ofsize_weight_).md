---
title: 'monospacedDigitSystemFont(ofSize:weight:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifont/monospaceddigitsystemfont(ofsize:weight:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifont/monospaceddigitsystemfont(ofsize:weight:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifont/monospaceddigitsystemfont%28ofsize%3Aweight%3A%29.json'
content_hash: 'sha256:06845e6bf9f70a3f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFont](../uifont.md)

# monospacedDigitSystemFont(ofSize:weight:)

<sub>Type Method</sub>

Returns the standard system font with all digits of consistent width.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class func monospacedDigitSystemFont(ofSize fontSize: CGFloat, weight: UIFont.Weight) -> UIFont
```

## Parameters

- `fontSize` — The size (in points) for the font. This value must be greater than `0.0`.

- `weight` — The weight of the font, specified as a font weight constant. For a list of possible values, see [Weight](weight.md). Avoid passing an arbitrary floating-point number for `weight`, because a font might not include a variant for every weight.

## Return Value

A font object of the specified size and weight, with variable-width text and fixed-width digits.

## Discussion

The system font uses proportional spacing. When displaying numerical data, you can use this method to retrieve a monospace font for displaying that data. With a monospaced font, each digit occupies the same amount of space, which makes it easier to read numbers that are stacked vertically.

> [!note] Note
> This method returns the same font as [+ systemFontOfSize:weight:](<systemfont(ofsize_weight_).md>), but with modified digits. If you want all characters to be fixed-width, use [+ monospacedSystemFontOfSize:weight:](<monospacedsystemfont(ofsize_weight_).md>) instead.

## See Also

### Creating System Fonts

- [+ systemFontOfSize:](<systemfont(ofsize_).md>) — Returns the font object for standard interface items in the specified size.
- [+ systemFontOfSize:weight:](<systemfont(ofsize_weight_).md>) — Returns the font object for standard interface items in the specified size and weight.
- [Weight](weight.md) — Constants that represent standard typeface styles.
- [+ systemFontOfSize:weight:width:](<systemfont(ofsize_weight_width_).md>)
- [Width](width.md)
- [+ boldSystemFontOfSize:](<boldsystemfont(ofsize_).md>) — Returns the font object for standard interface items in boldface type in the specified size.
- [+ italicSystemFontOfSize:](<italicsystemfont(ofsize_).md>) — Returns the font object for standard interface items in italic type in the specified size.
- [+ monospacedSystemFontOfSize:weight:](<monospacedsystemfont(ofsize_weight_).md>) — Returns the fixed-width font for standard interface text in the specified size.
