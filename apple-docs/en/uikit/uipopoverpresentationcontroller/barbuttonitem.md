---
title: barButtonItem
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（27.0 起废弃）, iPadOS 8.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uipopoverpresentationcontroller/barbuttonitem
source_url: 'https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/barbuttonitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopoverpresentationcontroller/barbuttonitem.json'
content_hash: 'sha256:bff3ce29fd3d672a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverPresentationController](../uipopoverpresentationcontroller.md)

# barButtonItem

<sub>Instance Property</sub>

The bar button item on which to anchor the popover.

> [!warning] Deprecated
> Use the [sourceItem](sourceitem.md) property to anchor the popover to a [UIBarButtonItem](../uibarbuttonitem.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var barButtonItem: UIBarButtonItem? { get set }
```

## Discussion

Assign a value to this property to anchor the popover to the specified bar button item. When presented, the popover’s arrow points to the specified item. Alternatively, you may specify the anchor location for the popover using the [sourceView](sourceview.md) and [sourceRect](sourcerect.md) properties.

Prior to presentation, the presentation controller adds all sibling bar button items of the specified item (but not the item itself) to the popover’s list of passthrough views. UIKit automatically intercepts taps in the specified item and uses them to dismiss the popover. If you want taps in the other bar button items to dismiss the popover, you must add code to the action handlers of those items.

The default value of this property is `nil`.

## See Also

### Specifying the popover’s anchor point

- [sourceItem](sourceitem.md) — The item on which to anchor the popover.
- [UIPopoverPresentationControllerSourceItem](../uipopoverpresentationcontrollersourceitem.md) — A type that can be an anchor for a popover presentation controller.
- [sourceView](sourceview.md) — The view containing the anchor rectangle for the popover.
- [sourceRect](sourcerect.md) — The area in the source view in which you anchor the popover.
