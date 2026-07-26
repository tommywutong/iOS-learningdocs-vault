---
title: outputType
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintinfo/outputtype-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinfo/outputtype-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinfo/outputtype-swift.property.json'
content_hash: 'sha256:739c116923eb4ca9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInfo](../uiprintinfo.md)

# outputType

<sub>Instance Property</sub>

The kind of printable content.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var outputType: UIPrintInfo.OutputType { get set }
```

## Discussion

The output type can be general, photo, or grayscale. An application can set this property to a value thats appropriate to the printable content. The default is [UIPrintInfoOutputGeneral](outputtype-swift.enum/general.md).  See the descriptions of the [OutputType](outputtype-swift.enum.md) constants for more information.

The output type controls the quality and default paper size used in printing. For example, if your application only prints black text, setting this property to [UIPrintInfoOutputGrayscale](outputtype-swift.enum/grayscale.md) can result in better performance in many cases. See [UIPrintPaper](../uiprintpaper.md) for details.

## See Also

### Managing print-job attributes

- [duplex](duplex-swift.property.md) — The duplex mode to use for the print job.
- [Duplex](duplex-swift.enum.md) — Constants that describe the duplex mode of a selected printer.
- [jobName](jobname.md) — The name of the print job.
- [orientation](orientation-swift.property.md) — The orientation of the printed content, portrait or landscape.
- [Orientation](orientation-swift.enum.md) — Constants that describe the orientation of printing on a page.
- [OutputType](outputtype-swift.enum.md) — Constants that describe the output type, which is an indication of the type of content the app is drawing or providing.
- [printerID](printerid.md) — An identifier of the printer to use for the print job.
