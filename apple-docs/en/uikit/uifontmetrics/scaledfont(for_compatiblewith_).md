---
title: 'scaledFont(for:compatibleWith:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifontmetrics/scaledfont(for:compatiblewith:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifontmetrics/scaledfont(for:compatiblewith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontmetrics/scaledfont%28for%3Acompatiblewith%3A%29.json'
content_hash: 'sha256:0b44fea3d27a49e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFontMetrics](../uifontmetrics.md)

# scaledFont(for:compatibleWith:)

<sub>Instance Method</sub>

Returns a version of the specified font that adopts the current font metrics and supports the specified traits.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func scaledFont(for font: UIFont, compatibleWith traitCollection: UITraitCollection?) -> UIFont
```

## Parameters

- `font` — The base font to use when applying the style information. Set the size of your font to the standard Dynamic Type size that you use for the corresponding content. Do not specify a font that has already been scaled; doing so results in an exception.

- `traitCollection` — The trait collection to use when determining compatibility. The returned font is appropriate for use in an interface that adopts the specified traits.

## Return Value

A version of the specified font with the appropriate style information applied to it, and scaled to the current Dynamic Type setting.

## See Also

### Creating Scaled Fonts

- [Scaling fonts automatically](../scaling-fonts-automatically.md) — Scale text in your interface automatically using Dynamic Type.
- [- scaledFontForFont:](<scaledfont(for_).md>) — Returns a version of the specified font that adopts the current font metrics.
- [- scaledFontForFont:maximumPointSize:](<scaledfont(for_maximumpointsize_).md>) — Returns a version of the specified font that adopts the current font metrics and is constrained to the specified maximum size.
- [- scaledFontForFont:maximumPointSize:compatibleWithTraitCollection:](<scaledfont(for_maximumpointsize_compatiblewith_).md>) — Returns a version of the specified font that adopts the current font metrics and is constrained to the specified traits and size.
