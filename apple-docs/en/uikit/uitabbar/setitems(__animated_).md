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
doc_path: '/documentation/uikit/uitabbar/setitems(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbar/setitems(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbar/setitems%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:17fdf3be72136611'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBar](../uitabbar.md)

# setItems(_:animated:)

<sub>Instance Method</sub>

Sets the items on the tab bar, optionally animating any changes into position.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setItems(_ items: [UITabBarItem]?, animated: Bool)
```

## Parameters

- `items` — The array of [UITabBarItem](../uitabbaritem.md) objects to display.

- `animated` — A Boolean indicating whether changes should be animated. Specify [true](../../swift/true.md) to animate changes or [false](../../swift/false.md) to display the new items without animations. When animations are enabled, the tab bar fades out removed items and fades in new items, adjusting the spacing between items as needed.

## Discussion

Use this method to make changes to the currently visible items at runtime. Calling this method on a tab bar that is managed by a [UITabBarController](../uitabbarcontroller.md) object raises an exception. When the tab bar is owned by a tab bar controller, use the tab bar controller’s methods to make changes to items.

## See Also

### Configuring tab bar items

- [items](items.md) — The items displayed by the tab bar.
- [selectedItem](selecteditem.md) — The currently selected item on the tab bar.
