---
title: backButtonDisplayMode
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/backbuttondisplaymode-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/backbuttondisplaymode-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/backbuttondisplaymode-swift.property.json'
content_hash: 'sha256:38dc09fefdc2f21c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# backButtonDisplayMode

<sub>Instance Property</sub>

The display mode of the Back button.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var backButtonDisplayMode: UINavigationItem.BackButtonDisplayMode { get set }
```

## Discussion

When the `backBarButtonItem` property is `nil`, the navigation item uses this display mode to determine the title of its Back button. The default value of this property is [UINavigationItemBackButtonDisplayModeDefault](backbuttondisplaymode-swift.enum/default.md).

## See Also

### Configuring the Back button

- [backBarButtonItem](backbarbuttonitem.md) — The bar button item for adding a Back button to the navigation bar.
- [backButtonTitle](backbuttontitle.md) — The custom title of the Back button.
- [BackButtonDisplayMode](backbuttondisplaymode-swift.enum.md) — Constants that describe the display modes of the Back button.
- [hidesBackButton](hidesbackbutton.md) — A Boolean value that determines whether the navigation item hides the Back button.
- [- setHidesBackButton:animated:](<sethidesbackbutton(__animated_).md>) — Hides or shows the Back button, optionally animating the transition.
- [backAction](backaction.md) — The back action for the navigation bar.
