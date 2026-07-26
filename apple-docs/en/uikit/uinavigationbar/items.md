---
title: items
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationbar/items
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbar/items'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbar/items.json'
content_hash: 'sha256:7bd154c8cd14e961'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBar](../uinavigationbar.md)

# items

<sub>Instance Property</sub>

An array of navigation items managed by the navigation bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var items: [UINavigationItem]? { get set }
```

## Discussion

The bottom item is at index `0`, the back item is at index `n-2`, and the top item is at index `n-1`, where `n` is the number of items in the array.

## See Also

### Pushing and popping items

- [- pushNavigationItem:animated:](<pushitem(__animated_).md>) — Pushes the given navigation item onto the navigation bar’s stack and updates the UI.
- [- popNavigationItemAnimated:](<popitem(animated_).md>) — Pops the top item from the navigation bar’s stack and updates the UI.
- [- setItems:animated:](<setitems(__animated_).md>) — Replaces the navigation items currently managed by the navigation bar with the specified items.
- [topItem](topitem.md) — The navigation item at the top of the navigation bar’s stack.
- [backItem](backitem.md) — The navigation item that is immediately below the topmost item on a navigation bar’s stack.
