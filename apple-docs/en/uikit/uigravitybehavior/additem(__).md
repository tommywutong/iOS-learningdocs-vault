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
doc_path: '/documentation/uikit/uigravitybehavior/additem(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigravitybehavior/additem(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigravitybehavior/additem%28_%3A%29.json'
content_hash: 'sha256:dc12174d680d4f11'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGravityBehavior](../uigravitybehavior.md)

# addItem(_:)

<sub>Instance Method</sub>

Associates the specified dynamic item with the gravity behavior.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addItem(_ item: any UIDynamicItem)
```

## Parameters

- `item` — The dynamic item to add to the item array. If the specified item is already associated with the gravity behavior, this method does nothing.

## Discussion

Use this method to add new dynamic items to the gravity behavior after initialization. All the dynamic items added to a gravity behavior are subject to the same gravity vector.

If the gravity behavior has an associated dynamic animator, this method notifies the dynamic animator of the presence of the new item so that it can initiate any needed animations.

## See Also

### Managing a gravity behavior’s items

- [items](items.md) — The set of dynamic items associated with the gravity behavior.
- [- removeItem:](<removeitem(__).md>) — Removes the specified dynamic item from the gravity behavior.
