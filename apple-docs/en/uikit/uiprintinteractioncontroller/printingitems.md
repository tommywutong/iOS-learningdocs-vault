---
title: printingItems
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintinteractioncontroller/printingitems
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/printingitems'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontroller/printingitems.json'
content_hash: 'sha256:befce0d6dc3cd118'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInteractionController](../uiprintinteractioncontroller.md)

# printingItems

<sub>Instance Property</sub>

An array of ready-to-print objects.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var printingItems: [Any]? { get set }
```

## Discussion

The array must contain [NSURL](../../foundation/nsurl.md), [NSData](../../foundation/nsdata.md), [UIImage](../uiimage.md), or [ALAsset](../../assetslibrary/alasset.md) objects in any combination. Objects of the first two types must reference or contain image data or PDF data. `NSURL` objects must use the `file:` or `assets-library:` scheme or any scheme that can return an [NSData](../../foundation/nsdata.md) object with a registered protocol. Image data (including that encapsulated by [UIImage](../uiimage.md) and [ALAsset](../../assetslibrary/alasset.md) objects) must be in a format supported by the Image I/O framework; see [UIImage](../uiimage.md) for more information. An [ALAsset](../../assetslibrary/alasset.md) object must be of type [ALAssetTypePhoto](../../assetslibrary/alassettypephoto.md). Items are printed in array-index order. The array is released at the end of the print job. The default value is `nil`.

If you set this property, `UIPrintInteractionController` sets the [printingItem](printingitem.md), [printPageRenderer](printpagerenderer.md), and [printFormatter](printformatter.md) properties to `nil`. (Only one of these properties can be set for a print job.)

If this property is set, the printing options do not include the control for selecting a page range, even if the [showsPageRange](showspagerange.md) property is set to [true](../../swift/true.md). If you want page-range selection, you should use the [printingItem](printingitem.md) property instead.

## See Also

### Providing the source of printable content

- [printingItem](printingitem.md) — A single ready-to-print object.
- [printPageRenderer](printpagerenderer.md) — An object that draws pages of printable content when UIKit requests it.
- [printFormatter](printformatter.md) — An object that lays out the content of pages according to the kind of content.
