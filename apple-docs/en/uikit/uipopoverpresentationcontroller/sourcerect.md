---
title: sourceRect
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipopoverpresentationcontroller/sourcerect
source_url: 'https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/sourcerect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopoverpresentationcontroller/sourcerect.json'
content_hash: 'sha256:ff33677829aa49e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverPresentationController](../uipopoverpresentationcontroller.md)

# sourceRect

<sub>Instance Property</sub>

The area in the source view in which you anchor the popover.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var sourceRect: CGRect { get set }
```

## Discussion

Use this property to define the rectangle that the popover’s arrow points to. The rectangle must be in the coordinate space of [sourceView](sourceview.md).

In iOS 13.2 and later, the default value is [CGRectNull](../../coregraphics/cgrectnull.md), which instructs the system to use the current frame of [sourceView](sourceview.md). The controller observes changes to this frame and updates the popover accordingly.

In iOS 13.1 and earlier, the default value is [zero](../../corefoundation/cgrect/zero.md) (Swift) or [CGRectZero](../../coregraphics/cgrectzero.md) (Objective-C); using [CGRectNull](../../coregraphics/cgrectnull.md) results in undefined behavior.

[UIPopoverPresentationController](../uipopoverpresentationcontroller.md) ignores this property if you set the [barButtonItem](barbuttonitem.md) property.

## See Also

### Specifying the popover’s anchor point

- [sourceItem](sourceitem.md) — The item on which to anchor the popover.
- [UIPopoverPresentationControllerSourceItem](../uipopoverpresentationcontrollersourceitem.md) — A type that can be an anchor for a popover presentation controller.
- [sourceView](sourceview.md) — The view containing the anchor rectangle for the popover.
- [barButtonItem](barbuttonitem.md) — The bar button item on which to anchor the popover. _(deprecated)_
