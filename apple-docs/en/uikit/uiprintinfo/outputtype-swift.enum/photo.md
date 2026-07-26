---
title: UIPrintInfo.OutputType.photo
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintinfo/outputtype-swift.enum/photo
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinfo/outputtype-swift.enum/photo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinfo/outputtype-swift.enum/photo.json'
content_hash: 'sha256:761136f668ef2552'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIPrintInfo](../../uiprintinfo.md) · [OutputType](../outputtype-swift.enum.md)

# UIPrintInfo.OutputType.photo

<sub>Case</sub>

Specifies that the printed content consists of black-and-white or color images. The default paper is 4x6, A6, or similar locale-specific designation. Output is high quality, simplex.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case photo
```

## See Also

### Constants

- [UIPrintInfoOutputGeneral](general.md) — Specifies that the printed content consists of mixed text, graphics, and images. The default paper is Letter, A4, or similar locale-specific designation. Output is normal quality, duplex.
- [UIPrintInfoOutputGrayscale](grayscale.md) — Specifies that the printed content is grayscale. Set the output type to this value when your printable content contains no color—for example, it’s black text only. The default paper is Letter/A4. Output is grayscale quality, duplex. This content type can produce a performance improvement in some cases.
- [UIPrintInfoOutputPhotoGrayscale](photograyscale.md) — Specifies that the printed content is a grayscale image. Set the output type to this value when your printable content contains no color—for example, it’s black text only. The default paper is Letter/A4. Output is high quality grayscale, duplex.
