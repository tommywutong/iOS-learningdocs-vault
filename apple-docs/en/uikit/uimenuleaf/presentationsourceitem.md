---
title: presentationSourceItem
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimenuleaf/presentationsourceitem
source_url: 'https://developer.apple.com/documentation/uikit/uimenuleaf/presentationsourceitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenuleaf/presentationsourceitem.json'
content_hash: 'sha256:08930fa8eeea1b06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuLeaf](../uimenuleaf.md)

# presentationSourceItem

<sub>Instance Property</sub>

The item you can use as an anchor for subsequent presentations.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var presentationSourceItem: (any UIPopoverPresentationControllerSourceItem)? { get }
```

## Discussion

The system populates this property during the execution of the menu element’s action (its handler or selector). For example, for a menu element in a menu that presents from a [UIButton](../uibutton.md), the system may populate this property with that button.

Use this property to specify where to anchor popovers when a person taps the menu element, like in the following code.

```swift
let share = UIAction(title: "Share") { [unowned self] action in
    let shareVC = UIActivityViewController(activityItems: items, applicationActivities: activities)
    shareVC.modalPresentationStyle = .popover
    shareVC.popoverPresentationController?.sourceItem = action.presentationSourceItem
    present(shareVC, animated: true)
}
```

## See Also

### Managing the appearance

- [title](title.md) — A short display title for the menu element.
- [discoverabilityTitle](discoverabilitytitle.md) — A long, informative title to use in the keyboard shortcut overlay.
- [image](image.md) — An image that appears next to the menu element.
- [attributes](attributes.md) — The attributes that determine the style of the menu element.
