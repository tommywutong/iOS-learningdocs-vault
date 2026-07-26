---
title: leading
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifont/leading
source_url: 'https://developer.apple.com/documentation/uikit/uifont/leading'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifont/leading.json'
content_hash: 'sha256:70405991f8c6970b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFont](../uifont.md)

# leading

<sub>Instance Property</sub>

The font’s leading information.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var leading: CGFloat { get }
```

## Discussion

The leading value represents additional space between lines of text and is measured in points.

## See Also

### Getting Font Metrics

- [pointSize](pointsize.md) — The font’s point size, or the effective vertical point size for a font with a nonstandard matrix.
- [ascender](ascender.md) — The top y-coordinate, offset from the baseline, of the font’s longest ascender.
- [descender](descender.md) — The bottom y-coordinate, offset from the baseline, of the font’s longest descender.
- [capHeight](capheight.md) — The font’s cap height information.
- [xHeight](xheight.md) — The x-height of the font.
- [lineHeight](lineheight.md) — The height, in points, of text lines.
