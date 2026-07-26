---
title: 'removeItem(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigravitybehavior/removeitem(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigravitybehavior/removeitem(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigravitybehavior/removeitem%28_%3A%29.json'
content_hash: 'sha256:12b2831a23e5d813'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGravityBehavior](../uigravitybehavior.md)

# removeItem(_:)

<sub>Instance Method</sub>

Removes the specified dynamic item from the gravity behavior.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func removeItem(_ item: any UIDynamicItem)
```

## Parameters

- `item` — The dynamic item that you want to remove. If the specified item is not associated with the behavior, this method does nothing.

## Discussion

If the gravity behavior has an associated dynamic animator, this method notifies the dynamic animator of the removal of the item so that it can stop any associated animations.

## See Also

### Managing a gravity behavior’s items

- [items](items.md) — The set of dynamic items associated with the gravity behavior.
- [- addItem:](<additem(__).md>) — Associates the specified dynamic item with the gravity behavior.
