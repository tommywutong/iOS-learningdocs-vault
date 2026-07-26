---
title: 'boldSystemFont(ofSize:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifont/boldsystemfont(ofsize:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifont/boldsystemfont(ofsize:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifont/boldsystemfont%28ofsize%3A%29.json'
content_hash: 'sha256:54ca2b4a49a9d128'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFont](../uifont.md)

# boldSystemFont(ofSize:)

<sub>Type Method</sub>

Returns the font object for standard interface items in boldface type in the specified size.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class func boldSystemFont(ofSize fontSize: CGFloat) -> UIFont
```

## Parameters

- `fontSize` — The size (in points) for the font. This value must be greater than `0.0`.

## Return Value

A font object of the specified size.

## Discussion

Instead of using this method to get a font, it’s often more appropriate to use [+ preferredFontForTextStyle:](<preferredfont(fortextstyle_).md>) because that method respects the user’s selected content size category.

## See Also

### Creating System Fonts

- [+ systemFontOfSize:](<systemfont(ofsize_).md>) — Returns the font object for standard interface items in the specified size.
- [+ systemFontOfSize:weight:](<systemfont(ofsize_weight_).md>) — Returns the font object for standard interface items in the specified size and weight.
- [Weight](weight.md) — Constants that represent standard typeface styles.
- [+ systemFontOfSize:weight:width:](<systemfont(ofsize_weight_width_).md>)
- [Width](width.md)
- [+ italicSystemFontOfSize:](<italicsystemfont(ofsize_).md>) — Returns the font object for standard interface items in italic type in the specified size.
- [+ monospacedSystemFontOfSize:weight:](<monospacedsystemfont(ofsize_weight_).md>) — Returns the fixed-width font for standard interface text in the specified size.
- [+ monospacedDigitSystemFontOfSize:weight:](<monospaceddigitsystemfont(ofsize_weight_).md>) — Returns the standard system font with all digits of consistent width.
