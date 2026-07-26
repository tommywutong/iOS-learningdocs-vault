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
doc_path: '/documentation/uikit/uicollisionbehavior/init(items:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollisionbehavior/init(items:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollisionbehavior/init%28items%3A%29.json'
content_hash: 'sha256:4b0469b07b1f8977'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollisionBehavior](../uicollisionbehavior.md)

# init(items:)

<sub>Initializer</sub>

Initializes a collision behavior with an array of dynamic items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(items: [any UIDynamicItem])
```

## Parameters

- `items` — The dynamic items that you want to participate in the collision behavior.

## Return Value

The initialized collision behavior, or `nil` if there was a problem initializing the object.

## See Also

### Initializing and managing a collision behavior

- [- addItem:](<additem(__).md>) — Adds a dynamic item to the collision behavior’s item array.
- [- removeItem:](<removeitem(__).md>) — Removes a specific dynamic item from the collision behavior.
- [items](items.md) — Returns the set of dynamic items you’ve added to the collision behavior.
