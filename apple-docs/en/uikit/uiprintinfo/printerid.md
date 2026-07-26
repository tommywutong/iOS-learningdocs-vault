---
title: printerID
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintinfo/printerid
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinfo/printerid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinfo/printerid.json'
content_hash: 'sha256:bdfe4d029965107f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInfo](../uiprintinfo.md)

# printerID

<sub>Instance Property</sub>

An identifier of the printer to use for the print job.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var printerID: String? { get set }
```

## Discussion

This property is set through user selection in the printing user interface. You may provide a printer ID as a hint (for example, the last printer used from a particular print job). The default value is `nil`.

## See Also

### Managing print-job attributes

- [duplex](duplex-swift.property.md) — The duplex mode to use for the print job.
- [Duplex](duplex-swift.enum.md) — Constants that describe the duplex mode of a selected printer.
- [jobName](jobname.md) — The name of the print job.
- [orientation](orientation-swift.property.md) — The orientation of the printed content, portrait or landscape.
- [Orientation](orientation-swift.enum.md) — Constants that describe the orientation of printing on a page.
- [outputType](outputtype-swift.property.md) — The kind of printable content.
- [OutputType](outputtype-swift.enum.md) — Constants that describe the output type, which is an indication of the type of content the app is drawing or providing.
