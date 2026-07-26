---
title: 'systemFont(ofSize:weight:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.2+, iPadOS 8.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifont/systemfont(ofsize:weight:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifont/systemfont(ofsize:weight:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifont/systemfont%28ofsize%3Aweight%3A%29.json'
content_hash: 'sha256:c11bd66405bb5877'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFont](../uifont.md)

# systemFont(ofSize:weight:)

<sub>Type Method</sub>

Returns the font object for standard interface items in the specified size and weight.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class func systemFont(ofSize fontSize: CGFloat, weight: UIFont.Weight) -> UIFont
```

## Parameters

- `fontSize` — The size (in points) to which the font is scaled. This value must be greater than 0.0.

- `weight` — The weight of the font, specified as a font weight constant. For a list of possible values, see “Font Weights” in [UIFontDescriptor](../uifontdescriptor.md). Avoid passing an arbitrary floating-point number for `weight`, because a font might not include a variant for every weight.

## Return Value

A font object of the specified size and weight.

## Discussion

Instead of using this method to get a font, it’s often more appropriate to use [+ preferredFontForTextStyle:](<preferredfont(fortextstyle_).md>) because that method respects the user’s selected content size category.

## See Also

### Creating System Fonts

- [+ systemFontOfSize:](<systemfont(ofsize_).md>) — Returns the font object for standard interface items in the specified size.
- [Weight](weight.md) — Constants that represent standard typeface styles.
- [+ systemFontOfSize:weight:width:](<systemfont(ofsize_weight_width_).md>)
- [Width](width.md)
- [+ boldSystemFontOfSize:](<boldsystemfont(ofsize_).md>) — Returns the font object for standard interface items in boldface type in the specified size.
- [+ italicSystemFontOfSize:](<italicsystemfont(ofsize_).md>) — Returns the font object for standard interface items in italic type in the specified size.
- [+ monospacedSystemFontOfSize:weight:](<monospacedsystemfont(ofsize_weight_).md>) — Returns the fixed-width font for standard interface text in the specified size.
- [+ monospacedDigitSystemFontOfSize:weight:](<monospaceddigitsystemfont(ofsize_weight_).md>) — Returns the standard system font with all digits of consistent width.
