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
doc_path: '/documentation/uikit/uiprintinteractioncontroller/canprint(_:)-364vj'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/canprint(_:)-364vj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontroller/canprint%28_%3A%29-364vj.json'
content_hash: 'sha256:202715a47a24de84'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInteractionController](../uiprintinteractioncontroller.md)

# canPrint(_:)

<sub>Type Method</sub>

Returns a Boolean value that indicates whether UIKit can print the file that the specified URL references.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class func canPrint(_ url: URL) -> Bool
```

## Parameters

- `url` — An object representing a URL. Valid `NSURL` objects must use the `file:` or any scheme that can return an [NSData](../../foundation/nsdata.md) object with a registered protocol. The file referenced by the URL must contain PDF data or an image in a format supported by the Image I/O framework. See [View Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewPG_iPhoneOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009503) in [View Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewPG_iPhoneOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009503) for a list of the supported image formats.

## Return Value

[true](../../swift/true.md) if UIKit can print the contents of the referenced file, otherwise [false](../../swift/false.md). The method returns [false](../../swift/false.md) if `url` references PDF data that specifies that printing is not allowed.

## Discussion

You should call this method to test the data referenced by a URL prior to assigning that URL to [printingItem](printingitem.md) or [printingItems](printingitems.md).

## See Also

### Determining printability

- [printingAvailable](isprintingavailable.md) — A Boolean value that indicates whether the device supports printing.
- [+ canPrintData:](<canprint(__)-4e0bs.md>) — Returns a Boolean value that indicates whether UIKit can print the contents of a data object.
- [printableUTIs](printableutis.md) — Returns a set of the Uniform Type Identifiers for the types of data that UIKit can print.
