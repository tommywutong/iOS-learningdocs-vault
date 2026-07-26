---
title: UIPrintPaper
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintpaper
source_url: 'https://developer.apple.com/documentation/uikit/uiprintpaper'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintpaper.json'
content_hash: 'sha256:d122381ae6a6f0a4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPrintPaper

<sub>Class</sub>

The size of paper for a print job and the rectangular area that the content prints within.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class UIPrintPaper
```

## Overview

In most cases, UIKit automatically creates an instance of [UIPrintPaper](uiprintpaper.md) that is appropriate for a print job. The UIKit framework has default paper sizes based on a print job’s output type ([outputType](uiprintinfo/outputtype-swift.property.md) is a property of the [UIPrintInfo](uiprintinfo.md) class). If the output type is [UIPrintInfoOutputPhoto](uiprintinfo/outputtype-swift.enum/photo.md), the default paper size is 4x6 or A6 or some other standard size, depending on locale; if the output type is [UIPrintInfoOutputGeneral](uiprintinfo/outputtype-swift.enum/general.md) or [UIPrintInfoOutputGrayscale](uiprintinfo/outputtype-swift.enum/grayscale.md), the default paper size is US Letter (8 1/2 by 11 inches) or A4 or some other standard size, depending on locale.

Applications may have special requirements for paper sizes. For example, a word-processing application may have items of “stationery” in which printable content must be drawn. If your application fits the special case, the delegate of [UIPrintInteractionController](uiprintinteractioncontroller.md) can implement the [- printInteractionController:choosePaper:](<uiprintinteractioncontrollerdelegate/printinteractioncontroller(__choosepaper_).md>) method of the [UIPrintInteractionControllerDelegate](uiprintinteractioncontrollerdelegate.md) protocol to return a suitable print paper object. One way to do this is to call the [+ bestPaperForPageSize:withPapersFromArray:](<uiprintpaper/bestpaper(forpagesize_withpapersfrom_).md>) class method of [UIPrintPaper](uiprintpaper.md), passing in a array of print paper objects representing the paper sizes supported by a printer. The print paper object returned from this method represents the paper size best matched to the size requirement of the application.

The printable rectangle ([printableRect](uiprintpaper/printablerect.md)) is the imageable area for the printer on a paper of a given size.

If you are using a [UIPrintPageRenderer](uiprintpagerenderer.md) object to draw the content for printing, the rectangle stored in the [printableRect](uiprintpaper/printablerect.md) property is stored in the page renderer’s property of the same name and the paper size used for a print job is stored as part of the [paperRect](uiprintpagerenderer/paperrect.md) property.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting the paper size and the printing area

- [paperSize](uiprintpaper/papersize.md) — The size of the sheet to use for printing.
- [printableRect](uiprintpaper/printablerect.md) — The rectangle that represents the portion of the paper that can be imaged upon.

### Obtaining the best paper size for printing

- [+ bestPaperForPageSize:withPapersFromArray:](<uiprintpaper/bestpaper(forpagesize_withpapersfrom_).md>) — The print-paper object that UIKit determines to be the best for a print job based on the specified page size and the paper size–imageable area combinations specific to the printer.

### Deprecated

- [- printRect](<uiprintpaper/printrect().md>) — Deprecated. _(deprecated)_

## See Also

### Job info

- [UIPrinter](uiprinter.md) — A printer on the network.
- [UIPrintInfo](uiprintinfo.md) — Information about a print job that the system uses when it prints.
