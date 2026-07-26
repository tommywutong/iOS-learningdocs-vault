---
title: 'scaledFont(for:maximumPointSize:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifontmetrics/scaledfont(for:maximumpointsize:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifontmetrics/scaledfont(for:maximumpointsize:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontmetrics/scaledfont%28for%3Amaximumpointsize%3A%29.json'
content_hash: 'sha256:004bb42e01572b4a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFontMetrics](../uifontmetrics.md)

# scaledFont(for:maximumPointSize:)

<sub>Instance Method</sub>

Returns a version of the specified font that adopts the current font metrics and is constrained to the specified maximum size.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func scaledFont(for font: UIFont, maximumPointSize: CGFloat) -> UIFont
```

## Parameters

- `font` — The base font to use when applying the style information. Set the size of your font to the standard Dynamic Type size that you use for the corresponding content. Do not specify a font that has already been scaled; doing so results in an exception.

- `maximumPointSize` — The maximum point size allowed for the font. Use this value to constrain the font to the specified size when your interface cannot accommodate text that is any larger.

## Return Value

A version of the specified font with the appropriate style information applied to it, and scaled appropriately for the specified settings.

## See Also

### Creating Scaled Fonts

- [Scaling fonts automatically](../scaling-fonts-automatically.md) — Scale text in your interface automatically using Dynamic Type.
- [- scaledFontForFont:](<scaledfont(for_).md>) — Returns a version of the specified font that adopts the current font metrics.
- [- scaledFontForFont:compatibleWithTraitCollection:](<scaledfont(for_compatiblewith_).md>) — Returns a version of the specified font that adopts the current font metrics and supports the specified traits.
- [- scaledFontForFont:maximumPointSize:compatibleWithTraitCollection:](<scaledfont(for_maximumpointsize_compatiblewith_).md>) — Returns a version of the specified font that adopts the current font metrics and is constrained to the specified traits and size.
