---
title: 'removeChildBehavior(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidynamicbehavior/removechildbehavior(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicbehavior/removechildbehavior(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicbehavior/removechildbehavior%28_%3A%29.json'
content_hash: 'sha256:23a163c2cf867060'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicBehavior](../uidynamicbehavior.md)

# removeChildBehavior(_:)

<sub>Instance Method</sub>

Removes a child dynamic behavior from a custom dynamic behavior.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func removeChildBehavior(_ behavior: UIDynamicBehavior)
```

## Parameters

- `behavior` — The child dynamic behavior you want to remove. The parent behavior ignores your use of this method if you: - Provide a `nil` value - Provide a behavior instance that is not a child of the parent behavior

## Discussion

This method applies only to custom subclasses of the [UIDynamicBehavior](../uidynamicbehavior.md) class. UIKit concrete dynamic behaviors (such as an instance of [UICollisionBehavior](../uicollisionbehavior.md)) cannot have child behaviors.

## See Also

### Configuring a dynamic behavior

- [action](action.md) — The block you want to execute during dynamic animation.
- [- addChildBehavior:](<addchildbehavior(__).md>) — Adds a dynamic behavior, as a child, to a custom dynamic behavior.
- [childBehaviors](childbehaviors.md) — Returns the array of dynamic behaviors that are children of a custom dynamic behavior.
