---
title: UIPrintInfo
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintinfo
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinfo.json'
content_hash: 'sha256:eeb567affc41c13b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPrintInfo

<sub>Class</sub>

Information about a print job that the system uses when it prints.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIPrintInfo
```

## Overview

A [UIPrintInfo](uiprintinfo.md) object encapsulates information about a print job, including printer identifier, job name, output type (photo, normal, grayscale), orientation (portrait or landscape), and any selected duplex mode.

Typically, you create a [UIPrintInfo](uiprintinfo.md) object and assign it to the [printInfo](uiprintinteractioncontroller/printinfo.md) property of the shared [UIPrintInteractionController](uiprintinteractioncontroller.md) instance. However, it isn’t necessary to create a [UIPrintInfo](uiprintinfo.md) object for a print job; UIKit assumes certain defaults. In the printing-options user interface, users can select the printer, single-sided or double-sided printing for duplex printers, and (if the app allows it) a range of pages to print.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a print info object

- [+ printInfo](<uiprintinfo/printinfo().md>) — Returns a print-information object initialized with default values.
- [+ printInfoWithDictionary:](<uiprintinfo/init(dictionary_).md>) — Returns a print-information object that is initialized with the data in the passed-in dictionary.
- [dictionaryRepresentation](uiprintinfo/dictionaryrepresentation.md) — A dictionary representation of a print-information object.
- [- initWithCoder:](<uiprintinfo/init(coder_).md>) — Creates a print info object from data in an unarchiver.

### Managing print-job attributes

- [duplex](uiprintinfo/duplex-swift.property.md) — The duplex mode to use for the print job.
- [Duplex](uiprintinfo/duplex-swift.enum.md) — Constants that describe the duplex mode of a selected printer.
- [jobName](uiprintinfo/jobname.md) — The name of the print job.
- [orientation](uiprintinfo/orientation-swift.property.md) — The orientation of the printed content, portrait or landscape.
- [Orientation](uiprintinfo/orientation-swift.enum.md) — Constants that describe the orientation of printing on a page.
- [outputType](uiprintinfo/outputtype-swift.property.md) — The kind of printable content.
- [OutputType](uiprintinfo/outputtype-swift.enum.md) — Constants that describe the output type, which is an indication of the type of content the app is drawing or providing.
- [printerID](uiprintinfo/printerid.md) — An identifier of the printer to use for the print job.

### Initializers

- [init()](<uiprintinfo/init().md>)

## See Also

### Job info

- [UIPrinter](uiprinter.md) — A printer on the network.
- [UIPrintPaper](uiprintpaper.md) — The size of paper for a print job and the rectangular area that the content prints within.
