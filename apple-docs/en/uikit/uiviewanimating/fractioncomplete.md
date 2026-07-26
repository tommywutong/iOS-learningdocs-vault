---
title: fractionComplete
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewanimating/fractioncomplete
source_url: 'https://developer.apple.com/documentation/uikit/uiviewanimating/fractioncomplete'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewanimating/fractioncomplete.json'
content_hash: 'sha256:b3138e2763344b2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewAnimating](../uiviewanimating.md)

# fractionComplete

<sub>Instance Property</sub>

The completion percentage of the animation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var fractionComplete: CGFloat { get set }
```

## Discussion

The value of this property is `0.0` at the beginning of the animation and `1.0` at the end of the animation. Intermediate values represent progress in the execution of the animation. For example, the value `0.5` indicates that the animation is exactly half way complete.

Assigning a new value to this property causes the animator to update the animation progress to the value you specify. You can use this capability to create interactive animations. For example, you might use a pan gesture recognizer to update the value based on the completion progress of that gesture. You can update the value of this property only while the animator is paused. Changing the value of this property on an inactive animator moves it to the active state.

When defining a custom animator, you may allow values greater than `1.0` or less than `0.0` if you support animations running past their beginning or end points.

## See Also

### Getting the animator’s state

- [reversed](isreversed.md) — A Boolean value indicating whether the animation is running in the reverse direction.
- [state](state.md) — The current state of the animation.
- [running](isrunning.md) — A Boolean value indicating whether the animation is currently running.
