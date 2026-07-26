---
title: printingItem
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintinteractioncontroller/printingitem
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/printingitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontroller/printingitem.json'
content_hash: 'sha256:1e53ba333795bba6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInteractionController](../uiprintinteractioncontroller.md)

# printingItem

<sub>Instance Property</sub>

A single ready-to-print object.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var printingItem: Any? { get set }
```

## Discussion

The object must be an instance of the [NSURL](../../foundation/nsurl.md), [NSData](../../foundation/nsdata.md), or [UIImage](../uiimage.md) class. An object of the first two types must reference or contain image data or PDF data. `NSURL` objects must use the `file:` or any scheme that can return an [NSData](../../foundation/nsdata.md) object with a registered protocol. Image data (including that encapsulated by [UIImage](../uiimage.md)) must be in a format supported by the Image I/O framework; see [UIImage](../uiimage.md) for more information. The object is released at the end of the print job. The default value is `nil`.

If you set this property, `UIPrintInteractionController` sets the [printingItems](printingitems.md), [printPageRenderer](printpagerenderer.md), and [printFormatter](printformatter.md) properties to `nil`. (You can only set one of these properties for a print job).

If this property is set and the [showsPageRange](showspagerange.md) property is set to [true](../../swift/true.md)—and the printing item is a PDF document of more than one page—the printing options include the control for selecting a page range.

## See Also

### Providing the source of printable content

- [printingItems](printingitems.md) — An array of ready-to-print objects.
- [printPageRenderer](printpagerenderer.md) — An object that draws pages of printable content when UIKit requests it.
- [printFormatter](printformatter.md) — An object that lays out the content of pages according to the kind of content.
