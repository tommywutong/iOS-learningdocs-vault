---
title: isPrintingAvailable
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintinteractioncontroller/isprintingavailable
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/isprintingavailable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontroller/isprintingavailable.json'
content_hash: 'sha256:047987605dc5dfb1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInteractionController](../uiprintinteractioncontroller.md)

# isPrintingAvailable

<sub>Type Property</sub>

A Boolean value that indicates whether the device supports printing.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class var isPrintingAvailable: Bool { get }
```

## Discussion

This value is [true](../../swift/true.md) if the device supports printing, otherwise [false](../../swift/false.md). An application can show or hide any print buttons based on this value.

## See Also

### Determining printability

- [+ canPrintData:](<canprint(__)-4e0bs.md>) — Returns a Boolean value that indicates whether UIKit can print the contents of a data object.
- [+ canPrintURL:](<canprint(__)-364vj.md>) — Returns a Boolean value that indicates whether UIKit can print the file that the specified URL references.
- [printableUTIs](printableutis.md) — Returns a set of the Uniform Type Identifiers for the types of data that UIKit can print.
