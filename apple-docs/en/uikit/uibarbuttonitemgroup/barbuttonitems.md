---
title: barButtonItems
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibarbuttonitemgroup/barbuttonitems
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/barbuttonitems'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitemgroup/barbuttonitems.json'
content_hash: 'sha256:e5a739710821741a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItemGroup](../uibarbuttonitemgroup.md)

# barButtonItems

<sub>Instance Property</sub>

The bar button items to display on the bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var barButtonItems: [UIBarButtonItem] { get set }
```

## Discussion

You may include any number of bar button items in a group, but you should keep the total number of items relatively small because of space considerations. The items in a group are typically related to each other, but need not be. The array must contain at least one item.

Items can belong to only one group at a time. If you specify an item that’s already in a group, UIKit removes the item from its previous group before assigning it to the current group.

## See Also

### Configuring the group

- [representativeItem](representativeitem.md) — The item to display for a group when space is constrained.
- [alwaysAvailable](alwaysavailable.md) — A Boolean value that determines whether the group is always available through the UI.
