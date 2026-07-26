---
title: UIGraphicsImageRendererFormat.Range.unspecified
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigraphicsimagerendererformat/range/unspecified
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsimagerendererformat/range/unspecified'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsimagerendererformat/range/unspecified.json'
content_hash: 'sha256:4b9e6eb5977e6867'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIGraphicsImageRendererFormat](../../uigraphicsimagerendererformat.md) · [Range](../range.md)

# UIGraphicsImageRendererFormat.Range.unspecified

<sub>Case</sub>

The image renderer context doesn’t specify a color range.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case unspecified
```

## Discussion

In general, avoid specifying this value for an image renderer format. Some color spaces that you access using the [imageRendererFormat](../../uiimage/imagerendererformat.md) property of [UIImage](../../uiimage.md) may use this value.

## See Also

### Constants

- [UIGraphicsImageRendererFormatRangeAutomatic](automatic.md) — The system automatically chooses the image renderer context’s pixel format according to the color range of its content.
- [UIGraphicsImageRendererFormatRangeExtended](extended.md) — The image renderer context supports wide color.
- [UIGraphicsImageRendererFormatRangeStandard](standard.md) — The image renderer context doesn’t support extended colors.
