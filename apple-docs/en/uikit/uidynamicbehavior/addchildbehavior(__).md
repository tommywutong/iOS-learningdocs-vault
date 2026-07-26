---
title: 'addChildBehavior(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidynamicbehavior/addchildbehavior(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicbehavior/addchildbehavior(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicbehavior/addchildbehavior%28_%3A%29.json'
content_hash: 'sha256:c8c66ff4a16f7620'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicBehavior](../uidynamicbehavior.md)

# addChildBehavior(_:)

<sub>Instance Method</sub>

Adds a dynamic behavior, as a child, to a custom dynamic behavior.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addChildBehavior(_ behavior: UIDynamicBehavior)
```

## Parameters

- `behavior` — The dynamic behavior you want to add as a child. The parent behavior ignores your use of this method if you: - Provide a `nil` value - Provide a behavior instance that you’ve already added to the behavior

## Discussion

Call this method only on custom subclasses of the [UIDynamicBehavior](../uidynamicbehavior.md) class.

## See Also

### Configuring a dynamic behavior

- [action](action.md) — The block you want to execute during dynamic animation.
- [childBehaviors](childbehaviors.md) — Returns the array of dynamic behaviors that are children of a custom dynamic behavior.
- [- removeChildBehavior:](<removechildbehavior(__).md>) — Removes a child dynamic behavior from a custom dynamic behavior.
