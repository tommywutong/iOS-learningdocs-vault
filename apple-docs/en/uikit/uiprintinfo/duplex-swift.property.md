---
title: duplex
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintinfo/duplex-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinfo/duplex-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinfo/duplex-swift.property.json'
content_hash: 'sha256:aa526849e2df7e7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInfo](../uiprintinfo.md)

# duplex

<sub>Instance Property</sub>

The duplex mode to use for the print job.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var duplex: UIPrintInfo.Duplex { get set }
```

## Discussion

Some printers can print either duplex (double-sided) or single-sided. If double-sided is selected, a printer can either print flipping the back page along the long edge of the paper or along the short edge. The default option for duplex-capable printers is based on document type: single-sided (none) for photos, double-sided and long edge for other documents. If a printer is capable of duplex printing, a switch in the printing options allows users to toggle between single-side and double-sided printing. See the description of the [Duplex](duplex-swift.enum.md) constants for more information.

## See Also

### Managing print-job attributes

- [Duplex](duplex-swift.enum.md) — Constants that describe the duplex mode of a selected printer.
- [jobName](jobname.md) — The name of the print job.
- [orientation](orientation-swift.property.md) — The orientation of the printed content, portrait or landscape.
- [Orientation](orientation-swift.enum.md) — Constants that describe the orientation of printing on a page.
- [outputType](outputtype-swift.property.md) — The kind of printable content.
- [OutputType](outputtype-swift.enum.md) — Constants that describe the output type, which is an indication of the type of content the app is drawing or providing.
- [printerID](printerid.md) — An identifier of the printer to use for the print job.
