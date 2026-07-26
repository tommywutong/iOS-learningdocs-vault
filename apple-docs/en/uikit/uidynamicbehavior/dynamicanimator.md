---
title: dynamicAnimator
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidynamicbehavior/dynamicanimator
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicbehavior/dynamicanimator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicbehavior/dynamicanimator.json'
content_hash: 'sha256:138b9c02eaae38c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicBehavior](../uidynamicbehavior.md)

# dynamicAnimator

<sub>Instance Property</sub>

The dynamic animator that the dynamic behavior is associated with.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var dynamicAnimator: UIDynamicAnimator? { get }
```

## Discussion

If the dynamic behavior is not associated with a dynamic animator, the value of this property is `nil`.

## See Also

### Responding to changes in the behavior tree

- [- willMoveToAnimator:](<willmove(to_).md>) — Called when the dynamic behavior is added to, or removed from, a dynamic animator.
