---
title: 'init(items:mode:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipushbehavior/init(items:mode:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipushbehavior/init(items:mode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipushbehavior/init%28items%3Amode%3A%29.json'
content_hash: 'sha256:02750f310290e5a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPushBehavior](../uipushbehavior.md)

# init(items:mode:)

<sub>Initializer</sub>

Initializes a push behavior with an array of dynamic items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(items: [any UIDynamicItem], mode: UIPushBehavior.Mode)
```

## Parameters

- `items` — The dynamic items that you want to be subject to the push behavior.

- `mode` — The mode for the new push behavior; one of the values defined in the [Mode](mode-swift.enum.md) enumeration. You must supply a value.

## Return Value

The initialized push behavior, or `nil` if there was a problem initializing the object.

## See Also

### Initializing and managing a push behavior

- [active](active.md) — The state of the push behavior’s force: either active or inactive.
- [- addItem:](<additem(__).md>) — Adds a dynamic item to the behavior’s dynamic item array.
- [- removeItem:](<removeitem(__).md>) — Removes a specific dynamic item from the behavior.
- [items](items.md) — Returns the set of dynamic items you’ve added to the push behavior.
