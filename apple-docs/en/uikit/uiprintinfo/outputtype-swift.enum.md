---
title: UIPrintInfo.OutputType
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintinfo/outputtype-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinfo/outputtype-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinfo/outputtype-swift.enum.json'
content_hash: 'sha256:a40ab4eb22087392'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInfo](../uiprintinfo.md)

# UIPrintInfo.OutputType

<sub>Enumeration</sub>

Constants that describe the output type, which is an indication of the type of content the app is drawing or providing.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum OutputType
```

## Overview

You use these constants when setting the value of the [outputType](outputtype-swift.property.md) property of a `UIPrintInfo` object.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIPrintInfoOutputGeneral](outputtype-swift.enum/general.md) — Specifies that the printed content consists of mixed text, graphics, and images. The default paper is Letter, A4, or similar locale-specific designation. Output is normal quality, duplex.
- [UIPrintInfoOutputPhoto](outputtype-swift.enum/photo.md) — Specifies that the printed content consists of black-and-white or color images. The default paper is 4x6, A6, or similar locale-specific designation. Output is high quality, simplex.
- [UIPrintInfoOutputGrayscale](outputtype-swift.enum/grayscale.md) — Specifies that the printed content is grayscale. Set the output type to this value when your printable content contains no color—for example, it’s black text only. The default paper is Letter/A4. Output is grayscale quality, duplex. This content type can produce a performance improvement in some cases.
- [UIPrintInfoOutputPhotoGrayscale](outputtype-swift.enum/photograyscale.md) — Specifies that the printed content is a grayscale image. Set the output type to this value when your printable content contains no color—for example, it’s black text only. The default paper is Letter/A4. Output is high quality grayscale, duplex.

### Initializers

- [init(rawValue:)](<outputtype-swift.enum/init(rawvalue_).md>)

## See Also

### Managing print-job attributes

- [duplex](duplex-swift.property.md) — The duplex mode to use for the print job.
- [Duplex](duplex-swift.enum.md) — Constants that describe the duplex mode of a selected printer.
- [jobName](jobname.md) — The name of the print job.
- [orientation](orientation-swift.property.md) — The orientation of the printed content, portrait or landscape.
- [Orientation](orientation-swift.enum.md) — Constants that describe the orientation of printing on a page.
- [outputType](outputtype-swift.property.md) — The kind of printable content.
- [printerID](printerid.md) — An identifier of the printer to use for the print job.
