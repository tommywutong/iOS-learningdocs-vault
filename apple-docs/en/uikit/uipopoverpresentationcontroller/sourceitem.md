---
title: sourceItem
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipopoverpresentationcontroller/sourceitem
source_url: 'https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/sourceitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopoverpresentationcontroller/sourceitem.json'
content_hash: 'sha256:e1da8e4c71791b6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverPresentationController](../uipopoverpresentationcontroller.md)

# sourceItem

<sub>Instance Property</sub>

The item on which to anchor the popover.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var sourceItem: (any UIPopoverPresentationControllerSourceItem)? { get set }
```

## Discussion

Assign a value to this property to anchor the popover to the specified [UIBarButtonItem](../uibarbuttonitem.md) or [NSToolbarItem](../../appkit/nstoolbaritem.md). In iOS 18 and earlier, the popover’s arrow points to the specified item. In iOS 26 and later, the popover animates from and replaces the specified item until someone selects an action item or dismisses the popover.

Alternatively, you may specify the anchor location for the popover using the [sourceView](sourceview.md) and [sourceRect](sourcerect.md) properties.

The default value of this property is `nil`.

## See Also

### Specifying the popover’s anchor point

- [UIPopoverPresentationControllerSourceItem](../uipopoverpresentationcontrollersourceitem.md) — A type that can be an anchor for a popover presentation controller.
- [sourceView](sourceview.md) — The view containing the anchor rectangle for the popover.
- [sourceRect](sourcerect.md) — The area in the source view in which you anchor the popover.
- [barButtonItem](barbuttonitem.md) — The bar button item on which to anchor the popover. _(deprecated)_
