---
title: UIGraphicsImageRendererFormat.Range
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigraphicsimagerendererformat/range
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsimagerendererformat/range'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsimagerendererformat/range.json'
content_hash: 'sha256:d32ad91a3b793997'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsImageRendererFormat](../uigraphicsimagerendererformat.md)

# UIGraphicsImageRendererFormat.Range

<sub>Enumeration</sub>

Constants that specify the color range of the image renderer context.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum Range
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIGraphicsImageRendererFormatRangeAutomatic](range/automatic.md) — The system automatically chooses the image renderer context’s pixel format according to the color range of its content.
- [UIGraphicsImageRendererFormatRangeExtended](range/extended.md) — The image renderer context supports wide color.
- [UIGraphicsImageRendererFormatRangeStandard](range/standard.md) — The image renderer context doesn’t support extended colors.
- [UIGraphicsImageRendererFormatRangeUnspecified](range/unspecified.md) — The image renderer context doesn’t specify a color range.

### Initializers

- [init(rawValue:)](<range/init(rawvalue_).md>)

## See Also

### Configuring the renderer attributes

- [opaque](opaque.md) — A Boolean value that indicates whether the underlying Core Graphics context has an alpha channel.
- [scale](scale.md) — The display scale of the image renderer context.
- [preferredRange](preferredrange.md) — The preferred color range of the image renderer context.
- [prefersExtendedRange](prefersextendedrange.md) — A Boolean value that specifies whether the bitmap context uses extended color. _(deprecated)_
