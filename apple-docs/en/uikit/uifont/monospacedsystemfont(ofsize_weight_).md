---
title: 'monospacedSystemFont(ofSize:weight:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifont/monospacedsystemfont(ofsize:weight:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifont/monospacedsystemfont(ofsize:weight:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifont/monospacedsystemfont%28ofsize%3Aweight%3A%29.json'
content_hash: 'sha256:32223c0455ffd28e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFont](../uifont.md)

# monospacedSystemFont(ofSize:weight:)

<sub>Type Method</sub>

Returns the fixed-width font for standard interface text in the specified size.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class func monospacedSystemFont(ofSize fontSize: CGFloat, weight: UIFont.Weight) -> UIFont
```

## Parameters

- `fontSize` — The size (in points) for the font. This value must be greater than `0.0`.

- `weight` — The weight of the font, specified as a font weight constant. For a list of possible values, see [Weight](weight.md). Avoid passing an arbitrary floating-point number for `weight`, because a font might not include a variant for every weight.

## Return Value

A font object of the specified size.

## Discussion

This method provides the same font as the [UIFontDescriptorSystemDesignMonospaced](../uifontdescriptor/systemdesign/monospaced.md) system font descriptor. For design guidance, see [Typography](https://developer.apple.com/design/human-interface-guidelines/ios/visual-design/typography/) in the Human Interface Guidelines.

> [!note] Note
> To display text in the standard system font, but with fixed-width digits, use [+ monospacedDigitSystemFontOfSize:weight:](<monospaceddigitsystemfont(ofsize_weight_).md>) instead.

## See Also

### Creating System Fonts

- [+ systemFontOfSize:](<systemfont(ofsize_).md>) — Returns the font object for standard interface items in the specified size.
- [+ systemFontOfSize:weight:](<systemfont(ofsize_weight_).md>) — Returns the font object for standard interface items in the specified size and weight.
- [Weight](weight.md) — Constants that represent standard typeface styles.
- [+ systemFontOfSize:weight:width:](<systemfont(ofsize_weight_width_).md>)
- [Width](width.md)
- [+ boldSystemFontOfSize:](<boldsystemfont(ofsize_).md>) — Returns the font object for standard interface items in boldface type in the specified size.
- [+ italicSystemFontOfSize:](<italicsystemfont(ofsize_).md>) — Returns the font object for standard interface items in italic type in the specified size.
- [+ monospacedDigitSystemFontOfSize:weight:](<monospaceddigitsystemfont(ofsize_weight_).md>) — Returns the standard system font with all digits of consistent width.
