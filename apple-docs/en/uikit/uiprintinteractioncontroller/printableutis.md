---
title: printableUTIs
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintinteractioncontroller/printableutis
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/printableutis'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontroller/printableutis.json'
content_hash: 'sha256:038f5cf9317cdb49'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInteractionController](../uiprintinteractioncontroller.md)

# printableUTIs

<sub>Type Property</sub>

Returns a set of the Uniform Type Identifiers for the types of data that UIKit can print.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class var printableUTIs: Set<String> { get }
```

## Return Value

A set object that contains, as strings, the UTIs identifying data types that UIKit knows how to print natively.

## See Also

### Determining printability

- [printingAvailable](isprintingavailable.md) — A Boolean value that indicates whether the device supports printing.
- [+ canPrintData:](<canprint(__)-4e0bs.md>) — Returns a Boolean value that indicates whether UIKit can print the contents of a data object.
- [+ canPrintURL:](<canprint(__)-364vj.md>) — Returns a Boolean value that indicates whether UIKit can print the file that the specified URL references.
