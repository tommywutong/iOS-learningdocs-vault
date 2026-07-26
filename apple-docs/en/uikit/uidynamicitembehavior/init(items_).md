---
title: 'init(items:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidynamicitembehavior/init(items:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicitembehavior/init(items:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicitembehavior/init%28items%3A%29.json'
content_hash: 'sha256:900d473e0c777d3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicItemBehavior](../uidynamicitembehavior.md)

# init(items:)

<sub>Initializer</sub>

Initializes a dynamic item behavior with an array of dynamic items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(items: [any UIDynamicItem])
```

## Parameters

- `items` — The dynamic items that you want to be subject to the dynamic item behavior.

## Return Value

The initialized dynamic item behavior, or `nil` if there was a problem initializing the object.

## See Also

### Initializing and managing a dynamic item behavior

- [- addItem:](<additem(__).md>) — Adds a dynamic item to the dynamic item behavior’s item array.
- [- removeItem:](<removeitem(__).md>) — Removes a specific dynamic item from the dynamic item behavior.
- [items](items.md) — Returns the set of dynamic items you’ve added to the dynamic item behavior.
