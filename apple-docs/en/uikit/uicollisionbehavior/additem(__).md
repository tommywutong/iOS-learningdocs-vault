---
title: 'addItem(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollisionbehavior/additem(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollisionbehavior/additem(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollisionbehavior/additem%28_%3A%29.json'
content_hash: 'sha256:41358deaf26ee271'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollisionBehavior](../uicollisionbehavior.md)

# addItem(_:)

<sub>Instance Method</sub>

Adds a dynamic item to the collision behavior’s item array.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addItem(_ item: any UIDynamicItem)
```

## Parameters

- `item` — The dynamic item to add to the item array.

## Discussion

You can add a dynamic item to one or more collision behaviors. For example, you can use two collision behaviors to specify that item _A_ can collide with item _B_ and that item _C_ can collide with item _D_, but that items _A_ and _B_ ignore items _C_ and _D_.

There is no hard limit to the number of dynamic items you can add to a collision behavior. However, adding a large number of items might result in a performance impact. Be sure to test your behaviors on the device configurations you are targeting.

## See Also

### Initializing and managing a collision behavior

- [- initWithItems:](<init(items_).md>) — Initializes a collision behavior with an array of dynamic items.
- [- removeItem:](<removeitem(__).md>) — Removes a specific dynamic item from the collision behavior.
- [items](items.md) — Returns the set of dynamic items you’ve added to the collision behavior.
