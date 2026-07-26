---
title: isReversed
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewanimating/isreversed
source_url: 'https://developer.apple.com/documentation/uikit/uiviewanimating/isreversed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewanimating/isreversed.json'
content_hash: 'sha256:b29581fab9a57c94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewAnimating](../uiviewanimating.md)

# isReversed

<sub>Instance Property</sub>

A Boolean value indicating whether the animation is running in the reverse direction.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isReversed: Bool { get set }
```

## Discussion

When the value of this property is [true](../../swift/true.md), animations run in the reverse direction—that is, view properties animate back to their original values. When the value is [false](../../swift/false.md), view properties animate to their intended final values.

When implementing this property, changes should cause the animation to reverse direction. If you allow changes while the animation is running, it is best to pause the animation briefly and then start it again in the opposite direction. Once the animation transitions to the [UIViewAnimatingStateStopped](../uiviewanimatingstate/stopped.md) state, you can ignore changes to this property.

## See Also

### Getting the animator’s state

- [fractionComplete](fractioncomplete.md) — The completion percentage of the animation.
- [state](state.md) — The current state of the animation.
- [running](isrunning.md) — A Boolean value indicating whether the animation is currently running.
