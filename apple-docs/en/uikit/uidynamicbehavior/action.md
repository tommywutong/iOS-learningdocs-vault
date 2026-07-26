---
title: action
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidynamicbehavior/action
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicbehavior/action'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicbehavior/action.json'
content_hash: 'sha256:ac5e9e0bbf118633'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicBehavior](../uidynamicbehavior.md)

# action

<sub>Instance Property</sub>

The block you want to execute during dynamic animation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var action: (() -> Void)? { get set }
```

## Discussion

The dynamic animator calls the action block on every animation step.

## See Also

### Related Documentation

- [- willMoveToAnimator:](<willmove(to_).md>) — Called when the dynamic behavior is added to, or removed from, a dynamic animator.

### Configuring a dynamic behavior

- [- addChildBehavior:](<addchildbehavior(__).md>) — Adds a dynamic behavior, as a child, to a custom dynamic behavior.
- [childBehaviors](childbehaviors.md) — Returns the array of dynamic behaviors that are children of a custom dynamic behavior.
- [- removeChildBehavior:](<removechildbehavior(__).md>) — Removes a child dynamic behavior from a custom dynamic behavior.
