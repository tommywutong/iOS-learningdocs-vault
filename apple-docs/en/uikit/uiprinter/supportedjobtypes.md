---
title: supportedJobTypes
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprinter/supportedjobtypes
source_url: 'https://developer.apple.com/documentation/uikit/uiprinter/supportedjobtypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinter/supportedjobtypes.json'
content_hash: 'sha256:428976783d393bdb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrinter](../uiprinter.md)

# supportedJobTypes

<sub>Instance Property</sub>

The capabilities of the printer.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var supportedJobTypes: UIPrinter.JobTypes { get }
```

## Discussion

Job types indicate the types of operations you can perform with the printer. You might use this information when deciding whether or not to use a printer for a particular task. For example, a photo app might prevent a printer picker interface from displaying printers that do not support the [UIPrinterJobTypePhoto](jobtypes/photo.md) job type.

For printers you create yourself using the [+ printerWithURL:](<init(url_)-1mibn.md>) method, the value of this property is [UIPrinterJobTypeUnknown](jobtypes/unknown.md) until you successfully connect to the printer using the [- contactPrinter:](<contactprinter(__).md>) method.

## See Also

### Getting the printer information

- [displayName](displayname.md) — The human-readable printer name.
- [displayLocation](displaylocation.md) — The human-readable text that describes the location of the printer.
- [makeAndModel](makeandmodel.md) — A string that contains the manufacturer’s name and the model name of the printer.
- [JobTypes](jobtypes.md) — Constants that indicate the types of jobs that the printer supports.
- [supportsColor](supportscolor.md) — A Boolean value that indicates whether the printer supports color printing.
- [supportsDuplex](supportsduplex.md) — A Boolean value that indicates whether the printer supports printing on both sides of a sheet of paper.
