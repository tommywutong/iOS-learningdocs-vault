---
title: displayLocation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprinter/displaylocation
source_url: 'https://developer.apple.com/documentation/uikit/uiprinter/displaylocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinter/displaylocation.json'
content_hash: 'sha256:d64ac44304555977'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrinter](../uiprinter.md)

# displayLocation

<sub>Instance Property</sub>

The human-readable text that describes the location of the printer.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var displayLocation: String? { get }
```

## Discussion

Many printers can be configured with a location string to reflect the printer’s physical location in an office. This property contains that location string or `nil` if no such string is available.

For printers you create yourself using the [+ printerWithURL:](<init(url_)-1mibn.md>) method, the value of this property is `nil` until you successfully connect to the printer using the [- contactPrinter:](<contactprinter(__).md>) method.

## See Also

### Getting the printer information

- [displayName](displayname.md) — The human-readable printer name.
- [makeAndModel](makeandmodel.md) — A string that contains the manufacturer’s name and the model name of the printer.
- [supportedJobTypes](supportedjobtypes.md) — The capabilities of the printer.
- [JobTypes](jobtypes.md) — Constants that indicate the types of jobs that the printer supports.
- [supportsColor](supportscolor.md) — A Boolean value that indicates whether the printer supports color printing.
- [supportsDuplex](supportsduplex.md) — A Boolean value that indicates whether the printer supports printing on both sides of a sheet of paper.
