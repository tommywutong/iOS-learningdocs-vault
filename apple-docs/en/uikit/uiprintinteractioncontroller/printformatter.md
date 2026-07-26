---
title: printFormatter
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintinteractioncontroller/printformatter
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/printformatter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontroller/printformatter.json'
content_hash: 'sha256:3230a0671138c4c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInteractionController](../uiprintinteractioncontroller.md)

# printFormatter

<sub>Instance Property</sub>

An object that lays out the content of pages according to the kind of content.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var printFormatter: UIPrintFormatter? { get set }
```

## Discussion

Assign to this property an instance of one of the concrete subclasses of [UIPrintFormatter](../uiprintformatter.md): [UISimpleTextPrintFormatter](../uisimpletextprintformatter.md), [UIMarkupTextPrintFormatter](../uimarkuptextprintformatter.md), and [UIViewPrintFormatter](../uiviewprintformatter.md). This object is released at the end of the print job.

If you set this property, `UIPrintInteractionController` sets the [printingItems](printingitems.md), [printingItem](printingitem.md), and [printPageRenderer](printpagerenderer.md) properties to `nil`. (Only one of these properties can be set for a print job.)

If this property is set and the [showsPageRange](showspagerange.md) property is set to [true](../../swift/true.md)—and if the formatter represents content of more than one page—the printing options include the control for selecting a page range.

## See Also

### Providing the source of printable content

- [printingItem](printingitem.md) — A single ready-to-print object.
- [printingItems](printingitems.md) — An array of ready-to-print objects.
- [printPageRenderer](printpagerenderer.md) — An object that draws pages of printable content when UIKit requests it.
