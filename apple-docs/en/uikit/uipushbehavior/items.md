---
title: items
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipushbehavior/items
source_url: 'https://developer.apple.com/documentation/uikit/uipushbehavior/items'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipushbehavior/items.json'
content_hash: 'sha256:4c8d640c1153cdbb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPushBehavior](../uipushbehavior.md)

# items

<sub>Instance Property</sub>

Returns the set of dynamic items you’ve added to the push behavior.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var items: [any UIDynamicItem] { get }
```

## See Also

### Initializing and managing a push behavior

- [active](active.md) — The state of the push behavior’s force: either active or inactive.
- [- addItem:](<additem(__).md>) — Adds a dynamic item to the behavior’s dynamic item array.
- [- initWithItems:mode:](<init(items_mode_).md>) — Initializes a push behavior with an array of dynamic items.
- [- removeItem:](<removeitem(__).md>) — Removes a specific dynamic item from the behavior.
