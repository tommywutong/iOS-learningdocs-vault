---
title: 'pushItem(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationbar/pushitem(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbar/pushitem(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbar/pushitem%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:d94cff3f7a9322f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBar](../uinavigationbar.md)

# pushItem(_:animated:)

<sub>Instance Method</sub>

Pushes the given navigation item onto the navigation bar’s stack and updates the UI.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func pushItem(_ item: UINavigationItem, animated: Bool)
```

## Parameters

- `item` — The navigation item to push on the stack.

- `animated` — [true](../../swift/true.md) if the navigation bar should be animated; otherwise, [false](../../swift/false.md).

## Discussion

Pushing a navigation item displays the item’s title in the center on the navigation bar. The previous top navigation item (if it exists) is displayed as a Back button on the left side of the navigation bar. If the new top item has a left custom view, it is displayed instead of the back button.

## See Also

### Pushing and popping items

- [- popNavigationItemAnimated:](<popitem(animated_).md>) — Pops the top item from the navigation bar’s stack and updates the UI.
- [- setItems:animated:](<setitems(__animated_).md>) — Replaces the navigation items currently managed by the navigation bar with the specified items.
- [items](items.md) — An array of navigation items managed by the navigation bar.
- [topItem](topitem.md) — The navigation item at the top of the navigation bar’s stack.
- [backItem](backitem.md) — The navigation item that is immediately below the topmost item on a navigation bar’s stack.
