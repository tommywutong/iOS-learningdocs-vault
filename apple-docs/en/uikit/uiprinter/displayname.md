---
title: displayName
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprinter/displayname
source_url: 'https://developer.apple.com/documentation/uikit/uiprinter/displayname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinter/displayname.json'
content_hash: 'sha256:876dc8d3fa65a990'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrinter](../uiprinter.md)

# displayName

<sub>Instance Property</sub>

The human-readable printer name.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var displayName: String { get }
```

## Discussion

This property contains a printer name that is suitable for display in your app’s user interface. For printers you create yourself using the [+ printerWithURL:](<init(url_)-1mibn.md>) method, the value of this property is `nil` until you successfully connect to the printer using the [- contactPrinter:](<contactprinter(__).md>) method.

## See Also

### Getting the printer information

- [displayLocation](displaylocation.md) — The human-readable text that describes the location of the printer.
- [makeAndModel](makeandmodel.md) — A string that contains the manufacturer’s name and the model name of the printer.
- [supportedJobTypes](supportedjobtypes.md) — The capabilities of the printer.
- [JobTypes](jobtypes.md) — Constants that indicate the types of jobs that the printer supports.
- [supportsColor](supportscolor.md) — A Boolean value that indicates whether the printer supports color printing.
- [supportsDuplex](supportsduplex.md) — A Boolean value that indicates whether the printer supports printing on both sides of a sheet of paper.
