---
title: backItem
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationbar/backitem
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbar/backitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbar/backitem.json'
content_hash: 'sha256:0594640f0b6a861f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBar](../uinavigationbar.md)

# backItem

<sub>Instance Property</sub>

The navigation item that is immediately below the topmost item on a navigation bar’s stack.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var backItem: UINavigationItem? { get }
```

## Discussion

If the [leftBarButtonItem](../uinavigationitem/leftbarbuttonitem.md) property of the topmost navigation item is `nil`, the navigation bar displays a back button whose title is derived from the item in this property.

If there is only one item on the navigation bar’s stack, the value of this property is `nil`.

## See Also

### Pushing and popping items

- [- pushNavigationItem:animated:](<pushitem(__animated_).md>) — Pushes the given navigation item onto the navigation bar’s stack and updates the UI.
- [- popNavigationItemAnimated:](<popitem(animated_).md>) — Pops the top item from the navigation bar’s stack and updates the UI.
- [- setItems:animated:](<setitems(__animated_).md>) — Replaces the navigation items currently managed by the navigation bar with the specified items.
- [items](items.md) — An array of navigation items managed by the navigation bar.
- [topItem](topitem.md) — The navigation item at the top of the navigation bar’s stack.
