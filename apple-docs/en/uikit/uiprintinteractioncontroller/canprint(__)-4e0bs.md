---
title: 'canPrint(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprintinteractioncontroller/canprint(_:)-4e0bs'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/canprint(_:)-4e0bs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontroller/canprint%28_%3A%29-4e0bs.json'
content_hash: 'sha256:df67d8eaa37e35d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInteractionController](../uiprintinteractioncontroller.md)

# canPrint(_:)

<sub>Type Method</sub>

Returns a Boolean value that indicates whether UIKit can print the contents of a data object.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class func canPrint(_ data: Data) -> Bool
```

## Parameters

- `data` — An instance of the [NSData](../../foundation/nsdata.md) class that contains PDF data or an image in a format supported by the Image I/O framework. See [View Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewPG_iPhoneOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009503) in [View Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewPG_iPhoneOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009503) for a list of the supported image formats.

## Return Value

[true](../../swift/true.md) if UIKit can print the contents of the data object, otherwise [false](../../swift/false.md). The method returns [false](../../swift/false.md) if `data` is PDF data that specifies that printing is not allowed.

## Discussion

You should call this method to test a data object prior to assigning it to [printingItem](printingitem.md) or [printingItems](printingitems.md).

## See Also

### Determining printability

- [printingAvailable](isprintingavailable.md) — A Boolean value that indicates whether the device supports printing.
- [+ canPrintURL:](<canprint(__)-364vj.md>) — Returns a Boolean value that indicates whether UIKit can print the file that the specified URL references.
- [printableUTIs](printableutis.md) — Returns a set of the Uniform Type Identifiers for the types of data that UIKit can print.
