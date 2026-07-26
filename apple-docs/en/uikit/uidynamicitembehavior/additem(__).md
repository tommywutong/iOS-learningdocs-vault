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
doc_path: '/documentation/uikit/uidynamicitembehavior/additem(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicitembehavior/additem(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicitembehavior/additem%28_%3A%29.json'
content_hash: 'sha256:1984e761b09e5eed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicItemBehavior](../uidynamicitembehavior.md)

# addItem(_:)

<sub>Instance Method</sub>

Adds a dynamic item to the dynamic item behavior’s item array.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addItem(_ item: any UIDynamicItem)
```

## Parameters

- `item` — The dynamic item to add to the item array.

## Discussion

You can add a dynamic item to one or more dynamic item behaviors. For example, you could add a dynamic item to one dynamic item behavior to configure the item’s elasticity and to a second dynamic item behavior to configure its density. This is especially useful when you are defining custom, combined behaviors for your dynamic items.

## See Also

### Initializing and managing a dynamic item behavior

- [- initWithItems:](<init(items_).md>) — Initializes a dynamic item behavior with an array of dynamic items.
- [- removeItem:](<removeitem(__).md>) — Removes a specific dynamic item from the dynamic item behavior.
- [items](items.md) — Returns the set of dynamic items you’ve added to the dynamic item behavior.
