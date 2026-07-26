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
doc_path: /documentation/uikit/uitabbar/items
source_url: 'https://developer.apple.com/documentation/uikit/uitabbar/items'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbar/items.json'
content_hash: 'sha256:11154edec0c5cb75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBar](../uitabbar.md)

# items

<sub>Instance Property</sub>

The items displayed by the tab bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var items: [UITabBarItem]? { get set }
```

## Discussion

This property contains an array of [UITabBarItem](../uitabbaritem.md) objects, each of which corresponds to a tab displayed by the tab bar. The order of the items in this property corresponds to the order of the items onscreen. You can use this property to access the items as needed.

For tab bars you create, you can assign a new set of items to this property to change the displayed items. Changing the items replaces them immediately without animations. You must not modify this property if the tab bar is managed by a [UITabBarController](../uitabbarcontroller.md) object, and doing so raises an exception. When the tab bar is owned by a tab bar controller, use the tab bar controller’s methods to make changes.

The default value of this property is `nil`.

## See Also

### Configuring tab bar items

- [- setItems:animated:](<setitems(__animated_).md>) — Sets the items on the tab bar, optionally animating any changes into position.
- [selectedItem](selecteditem.md) — The currently selected item on the tab bar.
