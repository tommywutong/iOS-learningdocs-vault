---
title: 'removeItem(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifieldbehavior/removeitem(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifieldbehavior/removeitem(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifieldbehavior/removeitem%28_%3A%29.json'
content_hash: 'sha256:af0cdf56bac32ecc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFieldBehavior](../uifieldbehavior.md)

# removeItem(_:)

<sub>Instance Method</sub>

Removes the field behavior from the specified dynamic item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func removeItem(_ item: any UIDynamicItem)
```

## Parameters

- `item` — The dynamic item whose behavior you want to modify.

## Discussion

Use this method to remove a field from a dynamic item in your interface. This method removes the specified dynamic item from the field behavior’s list of dynamic item.

## See Also

### Managing the associated dynamic items

- [- addItem:](<additem(__).md>) — Associates the field behavior with the specified dynamic item.
- [items](items.md) — The dynamic items associated with the current field behavior.
