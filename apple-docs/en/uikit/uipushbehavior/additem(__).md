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
doc_path: '/documentation/uikit/uipushbehavior/additem(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipushbehavior/additem(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipushbehavior/additem%28_%3A%29.json'
content_hash: 'sha256:319e956007098ccf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPushBehavior](../uipushbehavior.md)

# addItem(_:)

<sub>Instance Method</sub>

Adds a dynamic item to the behavior’s dynamic item array.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addItem(_ item: any UIDynamicItem)
```

## Parameters

- `item` — The dynamic item to add to the item array.

## Discussion

All the dynamic items added to a push behavior are subject to the same force vector.

## See Also

### Initializing and managing a push behavior

- [active](active.md) — The state of the push behavior’s force: either active or inactive.
- [- initWithItems:mode:](<init(items_mode_).md>) — Initializes a push behavior with an array of dynamic items.
- [- removeItem:](<removeitem(__).md>) — Removes a specific dynamic item from the behavior.
- [items](items.md) — Returns the set of dynamic items you’ve added to the push behavior.
