---
title: orientation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintinfo/orientation-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinfo/orientation-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinfo/orientation-swift.property.json'
content_hash: 'sha256:2cec252b75748903'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInfo](../uiprintinfo.md)

# orientation

<sub>Instance Property</sub>

The orientation of the printed content, portrait or landscape.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var orientation: UIPrintInfo.Orientation { get set }
```

## Discussion

An application can set this property to a value thats appropriate to the printable content or it can put up a user interface that enables users to pick the printing orientation. The default value is [UIPrintInfoOrientationPortrait](orientation-swift.enum/portrait.md). See the descriptions of the [Orientation](orientation-swift.enum.md) constants for more information.

> [!note] Note
> UIKit ignores this property when printable content is assigned to the `printingItem` or `printingItems` properties of the shared [UIPrintInteractionController](../uiprintinteractioncontroller.md) object. It determines the orientation based on the type of content.

## See Also

### Managing print-job attributes

- [duplex](duplex-swift.property.md) — The duplex mode to use for the print job.
- [Duplex](duplex-swift.enum.md) — Constants that describe the duplex mode of a selected printer.
- [jobName](jobname.md) — The name of the print job.
- [Orientation](orientation-swift.enum.md) — Constants that describe the orientation of printing on a page.
- [outputType](outputtype-swift.property.md) — The kind of printable content.
- [OutputType](outputtype-swift.enum.md) — Constants that describe the output type, which is an indication of the type of content the app is drawing or providing.
- [printerID](printerid.md) — An identifier of the printer to use for the print job.
