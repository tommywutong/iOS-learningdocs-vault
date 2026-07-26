---
title: printPageRenderer
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintinteractioncontroller/printpagerenderer
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/printpagerenderer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontroller/printpagerenderer.json'
content_hash: 'sha256:74d3c9854f39fb2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInteractionController](../uiprintinteractioncontroller.md)

# printPageRenderer

<sub>Instance Property</sub>

An object that draws pages of printable content when UIKit requests it.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var printPageRenderer: UIPrintPageRenderer? { get set }
```

## Discussion

The object assigned to this property must be an instance of a custom subclass of [UIPrintPageRenderer](../uiprintpagerenderer.md). The `UIPrintInteractionController` class retains the page-renderer object and releases it at the end of the print job. The default value is `nil`.

If you set this property, `UIPrintInteractionController` sets the [printingItems](printingitems.md), [printingItem](printingitem.md), [printFormatter](printformatter.md) properties to `nil`. (Only one of these properties can be set for a print job.)

If this property is set and the [showsPageRange](showspagerange.md) property is set to [true](../../swift/true.md)—and the rendered content is greater than one page—the printing options include the control for selecting a page range.

## See Also

### Providing the source of printable content

- [printingItem](printingitem.md) — A single ready-to-print object.
- [printingItems](printingitems.md) — An array of ready-to-print objects.
- [printFormatter](printformatter.md) — An object that lays out the content of pages according to the kind of content.
