---
title: UIGraphicsImageRendererFormat.Range.standard
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigraphicsimagerendererformat/range/standard
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsimagerendererformat/range/standard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsimagerendererformat/range/standard.json'
content_hash: 'sha256:0e078dfc5bb2e41b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIGraphicsImageRendererFormat](../../uigraphicsimagerendererformat.md) · [Range](../range.md)

# UIGraphicsImageRendererFormat.Range.standard

<sub>Case</sub>

The image renderer context doesn’t support extended colors.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case standard
```

## Discussion

If you draw wide-color content into an image renderer context that uses the standard color range, you may lose color information. The system matches the colors to the standard range of their corresponding color space.

## See Also

### Constants

- [UIGraphicsImageRendererFormatRangeAutomatic](automatic.md) — The system automatically chooses the image renderer context’s pixel format according to the color range of its content.
- [UIGraphicsImageRendererFormatRangeExtended](extended.md) — The image renderer context supports wide color.
- [UIGraphicsImageRendererFormatRangeUnspecified](unspecified.md) — The image renderer context doesn’t specify a color range.
