---
title: sourceView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipopoverpresentationcontroller/sourceview
source_url: 'https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/sourceview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopoverpresentationcontroller/sourceview.json'
content_hash: 'sha256:b39e6e0c12de7d9f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverPresentationController](../uipopoverpresentationcontroller.md)

# sourceView

<sub>Instance Property</sub>

The view containing the anchor rectangle for the popover.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var sourceView: UIView? { get set }
```

## Discussion

Use this property in conjunction with the [sourceRect](sourcerect.md) property to specify the anchor location for the popover. Alternatively, you may specify the anchor location for the popover using the [barButtonItem](barbuttonitem.md) property.

## See Also

### Specifying the popover’s anchor point

- [sourceItem](sourceitem.md) — The item on which to anchor the popover.
- [UIPopoverPresentationControllerSourceItem](../uipopoverpresentationcontrollersourceitem.md) — A type that can be an anchor for a popover presentation controller.
- [sourceRect](sourcerect.md) — The area in the source view in which you anchor the popover.
- [barButtonItem](barbuttonitem.md) — The bar button item on which to anchor the popover. _(deprecated)_
