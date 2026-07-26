---
title: UIPrintInfo.Duplex
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintinfo/duplex-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinfo/duplex-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinfo/duplex-swift.enum.json'
content_hash: 'sha256:35ce1159015e4446'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInfo](../uiprintinfo.md)

# UIPrintInfo.Duplex

<sub>Enumeration</sub>

Constants that describe the duplex mode of a selected printer.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum Duplex
```

## Overview

You use these constants when setting the value of the [duplex](duplex-swift.property.md) property of a `UIPrintInfo` object.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIPrintInfoDuplexNone](duplex-swift.enum/none.md) — No double-sided (duplex) printing; single-sided printing only.
- [UIPrintInfoDuplexLongEdge](duplex-swift.enum/longedge.md) — Duplex printing that flips the back page along the long edge of the paper.
- [UIPrintInfoDuplexShortEdge](duplex-swift.enum/shortedge.md) — Duplex print that flips the back page along the short edge of the paper.

### Initializers

- [init(rawValue:)](<duplex-swift.enum/init(rawvalue_).md>)

## See Also

### Managing print-job attributes

- [duplex](duplex-swift.property.md) — The duplex mode to use for the print job.
- [jobName](jobname.md) — The name of the print job.
- [orientation](orientation-swift.property.md) — The orientation of the printed content, portrait or landscape.
- [Orientation](orientation-swift.enum.md) — Constants that describe the orientation of printing on a page.
- [outputType](outputtype-swift.property.md) — The kind of printable content.
- [OutputType](outputtype-swift.enum.md) — Constants that describe the output type, which is an indication of the type of content the app is drawing or providing.
- [printerID](printerid.md) — An identifier of the printer to use for the print job.
