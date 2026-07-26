---
title: 'popItem(animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationbar/popitem(animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbar/popitem(animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbar/popitem%28animated%3A%29.json'
content_hash: 'sha256:2e37524ce6fb1f7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBar](../uinavigationbar.md)

# popItem(animated:)

<sub>Instance Method</sub>

Pops the top item from the navigation bar’s stack and updates the UI.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func popItem(animated: Bool) -> UINavigationItem?
```

## Parameters

- `animated` — [true](../../swift/true.md) if the navigation bar should be animated; otherwise, [false](../../swift/false.md).

## Return Value

The top item that was popped.

## Discussion

Popping a navigation item removes the top item from the stack and replaces it with the back item. The back item’s title is centered on the navigation bar and its other properties are displayed.

## See Also

### Pushing and popping items

- [- pushNavigationItem:animated:](<pushitem(__animated_).md>) — Pushes the given navigation item onto the navigation bar’s stack and updates the UI.
- [- setItems:animated:](<setitems(__animated_).md>) — Replaces the navigation items currently managed by the navigation bar with the specified items.
- [items](items.md) — An array of navigation items managed by the navigation bar.
- [topItem](topitem.md) — The navigation item at the top of the navigation bar’s stack.
- [backItem](backitem.md) — The navigation item that is immediately below the topmost item on a navigation bar’s stack.
