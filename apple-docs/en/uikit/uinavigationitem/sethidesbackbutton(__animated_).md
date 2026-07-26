---
title: 'setHidesBackButton(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationitem/sethidesbackbutton(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/sethidesbackbutton(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/sethidesbackbutton%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:bf6a99135bc0fcd5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# setHidesBackButton(_:animated:)

<sub>Instance Method</sub>

Hides or shows the Back button, optionally animating the transition.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setHidesBackButton(_ hidesBackButton: Bool, animated: Bool)
```

## Parameters

- `hidesBackButton` — Specify [true](../../swift/true.md) if the Back button should be hidden when this navigation item is the top item. Specify [false](../../swift/false.md) if the Back button should be visible, assuming it hasn’t been replaced by a custom item.

- `animated` — [true](../../swift/true.md) to animate the transition; otherwise, [false](../../swift/false.md).

## See Also

### Related Documentation

- [backItem](../uinavigationbar/backitem.md) — The navigation item that is immediately below the topmost item on a navigation bar’s stack.

### Configuring the Back button

- [backBarButtonItem](backbarbuttonitem.md) — The bar button item for adding a Back button to the navigation bar.
- [backButtonTitle](backbuttontitle.md) — The custom title of the Back button.
- [backButtonDisplayMode](backbuttondisplaymode-swift.property.md) — The display mode of the Back button.
- [BackButtonDisplayMode](backbuttondisplaymode-swift.enum.md) — Constants that describe the display modes of the Back button.
- [hidesBackButton](hidesbackbutton.md) — A Boolean value that determines whether the navigation item hides the Back button.
- [backAction](backaction.md) — The back action for the navigation bar.
