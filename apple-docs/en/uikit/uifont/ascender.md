---
title: ascender
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifont/ascender
source_url: 'https://developer.apple.com/documentation/uikit/uifont/ascender'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifont/ascender.json'
content_hash: 'sha256:30807b4285a30989'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFont](../uifont.md)

# ascender

<sub>Instance Property</sub>

The top y-coordinate, offset from the baseline, of the font’s longest ascender.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var ascender: CGFloat { get }
```

## Discussion

The ascender value is measured in points.

## See Also

### Getting Font Metrics

- [pointSize](pointsize.md) — The font’s point size, or the effective vertical point size for a font with a nonstandard matrix.
- [descender](descender.md) — The bottom y-coordinate, offset from the baseline, of the font’s longest descender.
- [leading](leading.md) — The font’s leading information.
- [capHeight](capheight.md) — The font’s cap height information.
- [xHeight](xheight.md) — The x-height of the font.
- [lineHeight](lineheight.md) — The height, in points, of text lines.
