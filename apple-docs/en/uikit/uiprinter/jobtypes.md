---
title: UIPrinter.JobTypes
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprinter/jobtypes
source_url: 'https://developer.apple.com/documentation/uikit/uiprinter/jobtypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinter/jobtypes.json'
content_hash: 'sha256:f9de4e1d013a767d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrinter](../uiprinter.md)

# UIPrinter.JobTypes

<sub>Structure</sub>

Constants that indicate the types of jobs that the printer supports.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct JobTypes
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [UIPrinterJobTypeUnknown](jobtypes/unknown.md) — The printer support is unknown.
- [UIPrinterJobTypeDocument](jobtypes/document.md) — The printer supports standard document printing.
- [UIPrinterJobTypeEnvelope](jobtypes/envelope.md) — The printer supports printing on envelopes.
- [UIPrinterJobTypeLabel](jobtypes/label.md) — The printer supports printing on cut labels.
- [UIPrinterJobTypePhoto](jobtypes/photo.md) — The printer supports printing with photographic print quality.
- [UIPrinterJobTypeReceipt](jobtypes/receipt.md) — The printer supports printing receipts on a continuous roll of paper.
- [UIPrinterJobTypeRoll](jobtypes/roll.md) — The printer supports printing documents or photos on a continuous roll of paper.
- [UIPrinterJobTypeLargeFormat](jobtypes/largeformat.md) — The printer supports printing larger than the ISO A3 size.
- [UIPrinterJobTypePostcard](jobtypes/postcard.md) — The printer supports printing on postcards.

### Initializers

- [init(rawValue:)](<jobtypes/init(rawvalue_).md>)

## See Also

### Getting the printer information

- [displayName](displayname.md) — The human-readable printer name.
- [displayLocation](displaylocation.md) — The human-readable text that describes the location of the printer.
- [makeAndModel](makeandmodel.md) — A string that contains the manufacturer’s name and the model name of the printer.
- [supportedJobTypes](supportedjobtypes.md) — The capabilities of the printer.
- [supportsColor](supportscolor.md) — A Boolean value that indicates whether the printer supports color printing.
- [supportsDuplex](supportsduplex.md) — A Boolean value that indicates whether the printer supports printing on both sides of a sheet of paper.
