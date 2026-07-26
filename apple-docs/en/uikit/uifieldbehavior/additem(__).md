---
title: 'addItem(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifieldbehavior/additem(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifieldbehavior/additem(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifieldbehavior/additem%28_%3A%29.json'
content_hash: 'sha256:50fd1b119687ecfe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFieldBehavior](../uifieldbehavior.md)

# addItem(_:)

<sub>Instance Method</sub>

Associates the field behavior with the specified dynamic item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addItem(_ item: any UIDynamicItem)
```

## Parameters

- `item` — The dynamic item whose behavior you want to modify.

## Discussion

Use this method to apply a field to a dynamic item in your interface. This method adds the specified dynamic item to the field behavior’s list of dynamic items.

## See Also

### Managing the associated dynamic items

- [- removeItem:](<removeitem(__).md>) — Removes the field behavior from the specified dynamic item.
- [items](items.md) — The dynamic items associated with the current field behavior.
