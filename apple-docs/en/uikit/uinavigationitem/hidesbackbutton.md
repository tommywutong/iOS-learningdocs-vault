---
title: hidesBackButton
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/hidesbackbutton
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/hidesbackbutton'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/hidesbackbutton.json'
content_hash: 'sha256:a8a5035a19a6b416'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# hidesBackButton

<sub>Instance Property</sub>

A Boolean value that determines whether the navigation item hides the Back button.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var hidesBackButton: Bool { get set }
```

## Discussion

When set to [true](../../swift/true.md), the Back button is hidden when this navigation item is the top item. This is true regardless of the value in the [leftItemsSupplementBackButton](leftitemssupplementbackbutton.md) property. When set to [false](../../swift/false.md), the Back button is shown if it’s still present. (It can be replaced by values in either the [leftBarButtonItem](leftbarbuttonitem.md) or [leftBarButtonItems](leftbarbuttonitems.md) properties.) The default value is [false](../../swift/false.md).

## See Also

### Related Documentation

- [backItem](../uinavigationbar/backitem.md) — The navigation item that is immediately below the topmost item on a navigation bar’s stack.

### Configuring the Back button

- [backBarButtonItem](backbarbuttonitem.md) — The bar button item for adding a Back button to the navigation bar.
- [backButtonTitle](backbuttontitle.md) — The custom title of the Back button.
- [backButtonDisplayMode](backbuttondisplaymode-swift.property.md) — The display mode of the Back button.
- [BackButtonDisplayMode](backbuttondisplaymode-swift.enum.md) — Constants that describe the display modes of the Back button.
- [- setHidesBackButton:animated:](<sethidesbackbutton(__animated_).md>) — Hides or shows the Back button, optionally animating the transition.
- [backAction](backaction.md) — The back action for the navigation bar.
