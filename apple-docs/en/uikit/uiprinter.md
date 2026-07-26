---
title: UIPrinter
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprinter
source_url: 'https://developer.apple.com/documentation/uikit/uiprinter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinter.json'
content_hash: 'sha256:afb6d4d323f3c56b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPrinter

<sub>Class</sub>

A printer on the network.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIPrinter
```

## Overview

You use a printer object to obtain information about a printer so that you can display that information in your app’s interface. You do not use printer objects to communicate with the printer directly.

Most of the time, you use a [UIPrinterPickerController](uiprinterpickercontroller.md) object to retrieve a printer object representing the printer selected by the user. If you already have a URL containing the address of a printer—perhaps one that was previously selected by the user—you can use that URL to create a printer object directly. When creating your own printer objects, you must connect to the printer using the [- contactPrinter:](<uiprinter/contactprinter(__).md>) method before retrieving any of the printer’s attributes.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a printer object

- [+ printerWithURL:](<uiprinter/init(url_)-1mibn.md>) — Creates and returns a printer with the specified location.

### Getting the printer’s address

- [URL](uiprinter/url.md) — The full address of the printer.

### Getting the printer information

- [displayName](uiprinter/displayname.md) — The human-readable printer name.
- [displayLocation](uiprinter/displaylocation.md) — The human-readable text that describes the location of the printer.
- [makeAndModel](uiprinter/makeandmodel.md) — A string that contains the manufacturer’s name and the model name of the printer.
- [supportedJobTypes](uiprinter/supportedjobtypes.md) — The capabilities of the printer.
- [JobTypes](uiprinter/jobtypes.md) — Constants that indicate the types of jobs that the printer supports.
- [supportsColor](uiprinter/supportscolor.md) — A Boolean value that indicates whether the printer supports color printing.
- [supportsDuplex](uiprinter/supportsduplex.md) — A Boolean value that indicates whether the printer supports printing on both sides of a sheet of paper.

### Connecting to the printer

- [- contactPrinter:](<uiprinter/contactprinter(__).md>) — Connects to the printer and gathers information about its capabilities.

### Constants

- [CutterBehavior](uiprinter/cutterbehavior.md) — Constants that specify the cutter behavior of a roll-fed printer.

### Initializers

- [init(URL:)](<uiprinter/init(url_)-80zxj.md>)

## See Also

### Job info

- [UIPrintInfo](uiprintinfo.md) — Information about a print job that the system uses when it prints.
- [UIPrintPaper](uiprintpaper.md) — The size of paper for a print job and the rectangular area that the content prints within.
