---
title: jobName
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintinfo/jobname
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinfo/jobname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinfo/jobname.json'
content_hash: 'sha256:0b9c5fba7cd43f81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInfo](../uiprintinfo.md)

# jobName

<sub>Instance Property</sub>

The name of the print job.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var jobName: String { get set }
```

## Discussion

The name of the print job appears in the Print Center when the job is printing. An app should set this property to a name appropriate to the content that’s printing. The default job name is the app name.

## See Also

### Managing print-job attributes

- [duplex](duplex-swift.property.md) — The duplex mode to use for the print job.
- [Duplex](duplex-swift.enum.md) — Constants that describe the duplex mode of a selected printer.
- [orientation](orientation-swift.property.md) — The orientation of the printed content, portrait or landscape.
- [Orientation](orientation-swift.enum.md) — Constants that describe the orientation of printing on a page.
- [outputType](outputtype-swift.property.md) — The kind of printable content.
- [OutputType](outputtype-swift.enum.md) — Constants that describe the output type, which is an indication of the type of content the app is drawing or providing.
- [printerID](printerid.md) — An identifier of the printer to use for the print job.
