---
title: 'setItems(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationbar/setitems(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbar/setitems(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbar/setitems%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:c7f6191e2e67627b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBar](../uinavigationbar.md)

# setItems(_:animated:)

<sub>Instance Method</sub>

Replaces the navigation items currently managed by the navigation bar with the specified items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setItems(_ items: [UINavigationItem]?, animated: Bool)
```

## Parameters

- `items` — The [UINavigationItem](../uinavigationitem.md) objects to place in the stack. The front-to-back order of the items in this array represents the new bottom-to-top order of the items in the navigation stack. Thus, the last item added to the array becomes the top item of the navigation stack.

- `animated` — If [true](../../swift/true.md), animate the pushing or popping of the top stack item. If [false](../../swift/false.md), replace the stack items without any animations.

## Discussion

You can use this method to update or replace the navigation items in the stack without pushing or popping each item explicitly. In addition, this method lets you update the stack without animating the changes, which might be appropriate at launch time when you want to restore the state of the navigation stack to some previous state.

If animations are enabled, this method decides which type of transition to perform based on whether the last item in the [items](items.md) array is already on the current navigation stack. If the item is currently on the stack, but is not the topmost item, this method uses a pop transition; if it is the topmost item, no transition is performed. If the item is not on the stack, this method uses a push transition. Only one transition is performed, but when that transition finishes, the entire contents of the stack are replaced with the new items. For example, if items A, B, and C are on the stack and you set items D, A, and B, this method uses a pop transition and the resulting stack contains the items D, A, and B.

## See Also

### Pushing and popping items

- [- pushNavigationItem:animated:](<pushitem(__animated_).md>) — Pushes the given navigation item onto the navigation bar’s stack and updates the UI.
- [- popNavigationItemAnimated:](<popitem(animated_).md>) — Pops the top item from the navigation bar’s stack and updates the UI.
- [items](items.md) — An array of navigation items managed by the navigation bar.
- [topItem](topitem.md) — The navigation item at the top of the navigation bar’s stack.
- [backItem](backitem.md) — The navigation item that is immediately below the topmost item on a navigation bar’s stack.
