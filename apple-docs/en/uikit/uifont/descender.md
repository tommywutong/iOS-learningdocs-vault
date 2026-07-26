---
title: descender
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifont/descender
source_url: 'https://developer.apple.com/documentation/uikit/uifont/descender'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifont/descender.json'
content_hash: 'sha256:45fb5737608e6f26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFont](../uifont.md)

# descender

<sub>Instance Property</sub>

The bottom y-coordinate, offset from the baseline, of the font’s longest descender.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var descender: CGFloat { get }
```

## Discussion

The descender value is measured in points. This value may be positive or negative. For example, if the longest descender extends 2 points below the baseline, this method returns `-2.0` .

## See Also

### Getting Font Metrics

- [pointSize](pointsize.md) — The font’s point size, or the effective vertical point size for a font with a nonstandard matrix.
- [ascender](ascender.md) — The top y-coordinate, offset from the baseline, of the font’s longest ascender.
- [leading](leading.md) — The font’s leading information.
- [capHeight](capheight.md) — The font’s cap height information.
- [xHeight](xheight.md) — The x-height of the font.
- [lineHeight](lineheight.md) — The height, in points, of text lines.
