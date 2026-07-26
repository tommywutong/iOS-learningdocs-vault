---
title: active
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipushbehavior/active
source_url: 'https://developer.apple.com/documentation/uikit/uipushbehavior/active'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipushbehavior/active.json'
content_hash: 'sha256:dfecdd1005832c04'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPushBehavior](../uipushbehavior.md)

# active

<sub>Instance Property</sub>

The state of the push behavior’s force: either active or inactive.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var active: Bool { get set }
```

## Discussion

After you’ve added a push behavior to a dynamic animator, use this property to activate or deactivate the behavior’s force (rather than removing and then re-adding the behavior to the animator).

## See Also

### Initializing and managing a push behavior

- [- addItem:](<additem(__).md>) — Adds a dynamic item to the behavior’s dynamic item array.
- [- initWithItems:mode:](<init(items_mode_).md>) — Initializes a push behavior with an array of dynamic items.
- [- removeItem:](<removeitem(__).md>) — Removes a specific dynamic item from the behavior.
- [items](items.md) — Returns the set of dynamic items you’ve added to the push behavior.
