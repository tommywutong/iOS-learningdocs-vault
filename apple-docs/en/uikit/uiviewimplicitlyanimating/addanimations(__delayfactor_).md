---
title: 'addAnimations(_:delayFactor:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewimplicitlyanimating/addanimations(_:delayfactor:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewimplicitlyanimating/addanimations(_:delayfactor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewimplicitlyanimating/addanimations%28_%3Adelayfactor%3A%29.json'
content_hash: 'sha256:86fe61b9f8ae77de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewImplicitlyAnimating](../uiviewimplicitlyanimating.md)

# addAnimations(_:delayFactor:)

<sub>Instance Method</sub>

Adds the specified animation block to the animator with a delay.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func addAnimations(_ animation: @escaping () -> Void, delayFactor: CGFloat)
```

## Parameters

- `animation` — A block containing the animations to add to the animator object. This block has no return value and takes no parameters.

- `delayFactor` — The factor to use for delaying the start of the animations. The value must be between `0.0` and `1.0`. Multiply this value by the animator’s remaining duration to determine the actual delay in seconds. For example, if the value `0.5` and the animator’s duration is `2.0`, delay the start of the animations by one second.

## Discussion

Use this method to add new animation blocks to your custom animator object. The animations in the new block should run alongside any previously configured animations, starting after the specified delay and finishing at the same time as any original animations. Your implementation must be able to handle multiple calls to this method.

## See Also

### Modifying animations

- [- addAnimations:](<addanimations(__).md>) — Adds the specified animation block to the animator.
- [- addCompletion:](<addcompletion(__).md>) — Adds the specified completion block to the animator.
- [- continueAnimationWithTimingParameters:durationFactor:](<continueanimation(withtimingparameters_durationfactor_).md>) — Adjusts the final timing and duration of a paused animation.
