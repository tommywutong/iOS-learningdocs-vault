---
title: backAction
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/backaction
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/backaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/backaction.json'
content_hash: 'sha256:896de45830b0fcb0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# backAction

<sub>Instance Property</sub>

The back action for the navigation bar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@NSCopying var backAction: UIAction? { get set }
```

## Discussion

If a back button already appears in the navigation bar, setting this property replaces its action without modifying its appearance. Otherwise, setting this property generates a back button with the image or title from the action you specify, unless you use the [UINavigationItemStyleEditor](itemstyle/editor.md) navigation style.

## See Also

### Configuring the Back button

- [backBarButtonItem](backbarbuttonitem.md) — The bar button item for adding a Back button to the navigation bar.
- [backButtonTitle](backbuttontitle.md) — The custom title of the Back button.
- [backButtonDisplayMode](backbuttondisplaymode-swift.property.md) — The display mode of the Back button.
- [BackButtonDisplayMode](backbuttondisplaymode-swift.enum.md) — Constants that describe the display modes of the Back button.
- [hidesBackButton](hidesbackbutton.md) — A Boolean value that determines whether the navigation item hides the Back button.
- [- setHidesBackButton:animated:](<sethidesbackbutton(__animated_).md>) — Hides or shows the Back button, optionally animating the transition.
