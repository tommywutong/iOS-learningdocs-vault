---
title: UIPrintInfo.Orientation
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintinfo/orientation-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinfo/orientation-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinfo/orientation-swift.enum.json'
content_hash: 'sha256:d2c0a24710624364'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInfo](../uiprintinfo.md)

# UIPrintInfo.Orientation

<sub>Enumeration</sub>

Constants that describe the orientation of printing on a page.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum Orientation
```

## Overview

You use these constants when setting the value of the [orientation](orientation-swift.property.md) property of a `UIPrintInfo` object.

> [!note] Note
> UIKit ignores the [orientation](orientation-swift.property.md) property when printable content is assigned to the `printingItem` or `printingItems` properties of the shared [UIPrintInteractionController](../uiprintinteractioncontroller.md) object. It determines the orientation based on the type of content.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIPrintInfoOrientationPortrait](orientation-swift.enum/portrait.md) — Pages are printed in portrait orientation.
- [UIPrintInfoOrientationLandscape](orientation-swift.enum/landscape.md) — Pages are printed in landscape orientation.

### Initializers

- [init(rawValue:)](<orientation-swift.enum/init(rawvalue_).md>)

## See Also

### Managing print-job attributes

- [duplex](duplex-swift.property.md) — The duplex mode to use for the print job.
- [Duplex](duplex-swift.enum.md) — Constants that describe the duplex mode of a selected printer.
- [jobName](jobname.md) — The name of the print job.
- [orientation](orientation-swift.property.md) — The orientation of the printed content, portrait or landscape.
- [outputType](outputtype-swift.property.md) — The kind of printable content.
- [OutputType](outputtype-swift.enum.md) — Constants that describe the output type, which is an indication of the type of content the app is drawing or providing.
- [printerID](printerid.md) — An identifier of the printer to use for the print job.
