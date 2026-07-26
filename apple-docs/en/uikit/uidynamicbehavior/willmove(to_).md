---
title: 'willMove(to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidynamicbehavior/willmove(to:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicbehavior/willmove(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicbehavior/willmove%28to%3A%29.json'
content_hash: 'sha256:91b8a354bd00398a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicBehavior](../uidynamicbehavior.md)

# willMove(to:)

<sub>Instance Method</sub>

Called when the dynamic behavior is added to, or removed from, a dynamic animator.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func willMove(to dynamicAnimator: UIDynamicAnimator?)
```

## Parameters

- `dynamicAnimator` — The dynamic animator that the behavior is being added to, or `nil` if being removed from an animator.

## Discussion

Use this method as the override point for responding to changes in the UIKit Dynamics behavior tree that involve the dynamic behavior.

## See Also

### Responding to changes in the behavior tree

- [dynamicAnimator](dynamicanimator.md) — The dynamic animator that the dynamic behavior is associated with.
